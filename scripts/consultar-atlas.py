"""Localize quadros e referências técnicas no atlas sem abrir o corpus inteiro."""

import argparse
import json
from pathlib import Path
import unicodedata


ROOT = Path(__file__).resolve().parents[1] / "references"
CORPUS = ROOT / "corpus"


def read(name):
    return json.loads((CORPUS / name).read_text(encoding="utf-8"))


def key(text):
    return "".join(
        char for char in unicodedata.normalize("NFD", text.casefold())
        if unicodedata.category(char) != "Mn"
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("caso", nargs="?", help="ID ou nome, como torra, Veio ou Figma for Motion")
    args = parser.parse_args()
    imagery = read("visual.json")
    css = read("tokens-css.json")
    if args.caso is None:
        for row in imagery:
            print(row["id"], "·", row["titulo"])
        print("universe-legado · Universe Digital, versão histórica")
        return

    query = key(args.caso)
    matches = [item for item in imagery if query in (key(item["id"]), key(item["titulo"]))]
    if not matches:
        matches = [item for item in imagery if query in key(item["titulo"])]
    if not matches and query in css:
        print("Fonte:", css[query]["source"])
        print(CORPUS / "universe.md")
        print(CORPUS / "tokens-css.json")
        return
    if len(matches) != 1:
        labels = ", ".join(row["titulo"] for row in matches)
        parser.error("Escolha um caso único" + (f" ({labels})" if labels else " listado no atlas"))

    row = matches[0]
    id_ = row["id"]
    print(row["titulo"])
    print("Abra a prancha:", ROOT / row["visual"])
    print("Origem:", row["fonte"])
    print("Evidência:", row["evidencia"])
    print("Marcos:", " · ".join(row["amostras"]))
    print("Tons das imagens:", ", ".join(row["amostra_cores"]))

    if id_.startswith("profitize-"):
        print("Leitura do caso:", CORPUS / "profitize.md", "·", row["titulo"])
    elif id_ in {"kyvo", "digigo", "figma-motion", "figma-secret"}:
        print("Leitura do caso:", CORPUS / "externos.md", "·", row["titulo"])
    else:
        print("Código e decisões:", CORPUS / "universe.md", "·", row["titulo"])
        print("Cenas por tempo:", CORPUS / "anexos.md", "·", row["titulo"])
        print("Tokens e aplicação:", CORPUS / "decisoes.md", "·", row["titulo"])
    if id_ in css:
        print("Tokens declarados:", CORPUS / "tokens-css.json", "·", id_)
        print("Fonte CSS:", css[id_]["source"])
    for observation in read("tokens-renderizados.json"):
        if observation["id"] != id_ or "sample" not in observation:
            continue
        heading = observation["sample"].get("h1")
        if heading:
            width = observation["viewport"]["width"]
            print("H1", width, "px:", heading["size"], "/", heading["line"], "em", heading["type"])


if __name__ == "__main__":
    main()
