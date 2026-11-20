"""Gere uma tomada de dois quadros no OpenRouter a partir do ambiente local."""

import argparse
import base64
from decimal import Decimal, InvalidOperation
from getpass import GetPassWarning, getpass
from http.client import HTTPException
import json
import os
from pathlib import Path
import re
import shutil
import sys
from tempfile import NamedTemporaryFile
import time
from urllib.error import HTTPError
from urllib.parse import urlsplit
from urllib.request import HTTPRedirectHandler, Request, build_opener
import warnings


API = "https://openrouter.ai/api/v1/videos"
KEY_NAME = "OPENROUTER_API_KEY"
DEFAULT_ENV = Path.home() / ".universe" / ".env"
DEFAULT_MODEL = "google/veo-3.1-lite"
FRAME_ROLES = ("first_frame", "last_frame")
MEDIA_TYPES = {".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".png": "image/png", ".webp": "image/webp"}


class VideoError(Exception):
    pass


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def request(path, key=None, payload=None):
    headers = {}
    if key:
        headers["Authorization"] = "Bearer " + key
    body = None
    if payload is not None:
        headers["Content-Type"] = "application/json"
        body = json.dumps(payload).encode("utf-8")
    try:
        return build_opener(NoRedirect()).open(Request(API + path, data=body, headers=headers), timeout=30)
    except HTTPError as error:
        error.close()
        raise VideoError(f"OpenRouter respondeu HTTP {error.code}.") from None
    except (OSError, HTTPException):
        raise VideoError("A comunicação com o OpenRouter foi interrompida.") from None


def read_json(path, key=None, payload=None):
    with request(path, key, payload) as response:
        return json.load(response)


def atomic_write(path, content):
    temporary = None
    try:
        with NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent, delete=False) as stream:
            temporary = Path(stream.name)
            stream.write(content)
        temporary.replace(path)
    finally:
        if temporary:
            temporary.unlink(missing_ok=True)


def configure(env_file):
    with warnings.catch_warnings():
        warnings.simplefilter("error", GetPassWarning)
        try:
            key = getpass("Chave do OpenRouter (entrada oculta): ").strip()
        except (GetPassWarning, EOFError):
            raise VideoError("Abra um terminal interativo para configurar a chave.") from None
    if not re.fullmatch(r"[A-Za-z0-9_-]+", key):
        raise VideoError("A chave informada tem formato inválido.")
    env_file.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
    previous = env_file.read_text(encoding="utf-8-sig").splitlines() if env_file.exists() else []
    lines = [line for line in previous if not re.match(r"^\s*(?:export\s+)?" + KEY_NAME + r"\s*=", line)]
    atomic_write(env_file, "\n".join([*lines, f"{KEY_NAME}={key}"]) + "\n")
    print(f"Chave salva em {env_file}.")


def api_key(env_file):
    key = os.environ.get(KEY_NAME, "").strip()
    if not key and env_file.is_file():
        for line in env_file.read_text(encoding="utf-8-sig").splitlines():
            match = re.fullmatch(r"\s*(?:export\s+)?" + KEY_NAME + r"\s*=\s*['\"]?([A-Za-z0-9_-]+)['\"]?\s*", line)
            if match:
                key = match[1]
    if not re.fullmatch(r"[A-Za-z0-9_-]+", key):
        raise VideoError(f"Configure {KEY_NAME} no ambiente ou execute o comando configurar.")
    return key


def amount(value):
    try:
        parsed = Decimal(value)
    except (InvalidOperation, TypeError, ValueError):
        raise argparse.ArgumentTypeError("Informe um valor positivo em dólares.") from None
    if not parsed.is_finite() or parsed <= 0:
        raise argparse.ArgumentTypeError("Informe um valor positivo em dólares.")
    return parsed


def clip_cost(model, duration, resolution):
    skus = model.get("pricing_skus") or {}
    # Use a tarifa silenciosa específica. As tarifas sem sufixo do Veo são de 1080p.
    rate = skus.get("duration_seconds_without_audio_" + resolution)
    if not rate and resolution == "1080p":
        rate = skus.get("duration_seconds_without_audio")
    if rate:
        return amount(rate) * duration
    if model["id"] == "alibaba/wan-2.7" and skus.get("duration_seconds"):
        return amount(skus["duration_seconds"]) * duration
    if model["id"] == "black-forest-labs/flux-3-video":
        rate = skus.get("cents_per_second_output_" + resolution)
        if rate:
            return amount(rate) * duration / 100
    return None


def candidates(args):
    ranked = []
    for model in read_json("/models")["data"]:
        if not set(FRAME_ROLES).issubset(model.get("supported_frame_images") or []):
            continue
        if (args.duration not in (model.get("supported_durations") or [])
                or args.resolution not in (model.get("supported_resolutions") or [])
                or args.aspect not in (model.get("supported_aspect_ratios") or [])):
            continue
        try:
            cost = clip_cost(model, args.duration, args.resolution)
        except argparse.ArgumentTypeError:
            cost = None
        ranked.append((model["id"], cost))
    return sorted(ranked, key=lambda entry: (entry[1] is None, entry[1] or 0, entry[0]))


def frame_input(value, role):
    if value.startswith("https://"):
        url = urlsplit(value)
        if not url.hostname or url.username or url.password:
            raise VideoError(f"Forneça uma URL HTTPS de imagem válida para {role}.")
    else:
        image = Path(value)
        mime = MEDIA_TYPES.get(image.suffix.lower())
        if not mime or not image.is_file() or image.stat().st_size == 0:
            raise VideoError(f"Forneça um arquivo JPEG, PNG ou WebP válido para {role}.")
        value = f"data:{mime};base64," + base64.b64encode(image.read_bytes()).decode("ascii")
    return {"type": "image_url", "image_url": {"url": value}, "frame_type": role}


def job_id(value):
    if not isinstance(value, str) or not re.fullmatch(r"[A-Za-z0-9_-]+", value):
        raise VideoError("ID de vídeo indisponível. Confira o painel do OpenRouter antes de nova tentativa.")
    return value


def submit(args):
    if args.job.exists():
        raise VideoError("Já existe um registro para esta cena. Use retomar ou confira o ID no painel.")
    key = api_key(args.env_file)
    available = dict(candidates(args))
    if args.model not in available:
        raise VideoError("O modelo não declara compatibilidade com os dois quadros e a configuração solicitada.")
    cost = available[args.model] or args.estimate_usd
    if cost is None:
        raise VideoError("Confira a tarifa desta configuração e informe a estimativa verificada em --estimate-usd.")
    if cost > args.max_usd:
        raise VideoError(f"Estimativa de US$ {cost} acima do limite autorizado de US$ {args.max_usd}.")
    prompt = args.prompt.read_text(encoding="utf-8-sig").strip()
    if not prompt:
        raise VideoError("O arquivo precisa conter a direção da tomada.")
    frames = [frame_input(value, role) for value, role in zip((args.first, args.last), FRAME_ROLES)]
    payload = {
        "model": args.model, "prompt": prompt, "duration": args.duration, "resolution": args.resolution,
        "aspect_ratio": args.aspect, "generate_audio": False, "frame_images": frames,
    }
    record = {"model": args.model, "estimated_usd": str(cost), "status": "submitting"}
    args.job.parent.mkdir(parents=True, exist_ok=True)
    # Reserve antes do POST. Uma interrupção sem ID mantém o registro até a conta ser verificada.
    with args.job.open("x", encoding="utf-8") as stream:
        json.dump(record, stream)
        stream.flush()
        os.fsync(stream.fileno())
    result = read_json("", key, payload)
    record.update(id=job_id(result.get("id")), status="submitted")
    atomic_write(args.job, json.dumps(record, indent=2) + "\n")
    print(f"Job {record['id']} registrado em {args.job}. Estimativa: US$ {cost}.")


def resume(args):
    identifier = job_id(args.id or json.loads(args.job.read_text(encoding="utf-8")).get("id"))
    key = api_key(args.env_file)
    if args.output.exists():
        raise VideoError("O arquivo de saída já existe. Escolha outro caminho ou use o vídeo local.")
    deadline = time.monotonic() + 600
    while True:
        status = read_json("/" + identifier, key)
        state = status.get("status")
        if state == "completed":
            break
        if state in ("failed", "cancelled", "expired"):
            raise VideoError(f"Job {identifier} encerrou com status {state}.")
        if state not in ("pending", "in_progress"):
            raise VideoError(f"Status inesperado para o job {identifier}.")
        if not args.wait or time.monotonic() >= deadline:
            print(f"Job {identifier}: {state}. Use retomar para consultar novamente.")
            return
        time.sleep(30)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    temporary = None
    try:
        with request(f"/{identifier}/content?index=0", key) as response:
            with NamedTemporaryFile(dir=args.output.parent, delete=False) as stream:
                temporary = Path(stream.name)
                shutil.copyfileobj(response, stream)
        with temporary.open("rb") as stream:
            if stream.read(8)[4:8] != b"ftyp":
                raise VideoError("O conteúdo retornado não é um MP4 reconhecível.")
        # O link publica o arquivo inteiro sem substituir outra descarga concorrente.
        os.link(temporary, args.output)
    finally:
        if temporary:
            temporary.unlink(missing_ok=True)
    cost = (status.get("usage") or {}).get("cost")
    print(f"Vídeo do job {identifier} salvo em {args.output}.")
    if isinstance(cost, (int, float)):
        print(f"Custo retornado: US$ {cost}.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--env-file", type=Path, default=DEFAULT_ENV)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("configurar", help="Guarde a chave na máquina com entrada oculta")
    plan = commands.add_parser("planejar", help="Consulte compatibilidade e custo sem gerar")
    generate = commands.add_parser("gerar", help="Submeta um único trabalho autorizado")
    for command in (plan, generate):
        command.add_argument("--duration", type=int, default=4)
        command.add_argument("--resolution", default="720p")
        command.add_argument("--aspect", default="16:9")
    generate.add_argument("--model", default=DEFAULT_MODEL)
    generate.add_argument("--first", required=True)
    generate.add_argument("--last", required=True)
    generate.add_argument("--prompt", type=Path, required=True)
    generate.add_argument("--job", type=Path, required=True)
    generate.add_argument("--max-usd", type=amount, required=True)
    generate.add_argument("--estimate-usd", type=amount, help="Estimativa verificada quando o catálogo não permite calcular")
    download = commands.add_parser("retomar", help="Consulte ou baixe um trabalho existente")
    job = download.add_mutually_exclusive_group(required=True)
    job.add_argument("--job", type=Path)
    job.add_argument("--id", help="ID recuperado no painel")
    download.add_argument("--output", type=Path, required=True)
    download.add_argument("--wait", action="store_true")
    args = parser.parse_args()
    try:
        if args.command == "configurar":
            configure(args.env_file)
        elif args.command == "planejar":
            for model, cost in candidates(args):
                quote = f"US$ {cost}" if cost is not None else "preço depende de verificação"
                print(f"{model}: {quote}")
        elif args.command == "gerar":
            submit(args)
        else:
            resume(args)
    except (VideoError, OSError, HTTPException, ValueError, KeyError) as error:
        message = str(error) if isinstance(error, (VideoError, FileNotFoundError, FileExistsError)) else "A operação foi interrompida."
        print(message, file=sys.stderr)
        if args.command == "gerar" and args.job.exists():
            print("Confira o registro ou o painel antes de autorizar outro POST.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
