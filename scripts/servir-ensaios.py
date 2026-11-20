"""Sirva os exemplos em loopback, com HTTP Range para o MP4 de demonstração."""

import argparse
from functools import partial
from http import HTTPStatus
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import re


class ExampleHandler(SimpleHTTPRequestHandler):
    def send_head(self):
        self.remaining = None
        requested = self.headers.get("Range")
        path = Path(self.translate_path(self.path))
        if path.suffix != ".mp4" or not requested or not path.is_file():
            return super().send_head()

        length = path.stat().st_size
        match = re.fullmatch(r"bytes=(\d*)-(\d*)", requested.strip())
        if match is None or not any(match.groups()):
            self.send_error(HTTPStatus.BAD_REQUEST, "Use um intervalo de bytes")
            return None
        first, last = match.groups()
        start = int(first) if first else max(0, length - int(last))
        end = min(length - 1, int(last)) if first and last else length - 1
        if start > end:
            self.send_response(HTTPStatus.REQUESTED_RANGE_NOT_SATISFIABLE)
            self.send_header("Content-Range", f"bytes */{length}")
            self.end_headers()
            return None

        stream = path.open("rb")
        stream.seek(start)
        self.remaining = end - start + 1
        self.send_response(HTTPStatus.PARTIAL_CONTENT)
        self.send_header("Content-type", "video/mp4")
        self.send_header("Accept-Ranges", "bytes")
        self.send_header("Content-Range", f"bytes {start}-{end}/{length}")
        self.send_header("Content-Length", str(self.remaining))
        self.end_headers()
        return stream

    def copyfile(self, source, output):
        if self.remaining is None:
            return super().copyfile(source, output)
        remaining = self.remaining
        while remaining:
            data = source.read(min(65536, remaining))
            if not data:
                break
            output.write(data)
            remaining -= len(data)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", default=4173, type=int)
    args = parser.parse_args()
    directory = Path(__file__).resolve().parents[1]
    handler = partial(ExampleHandler, directory=str(directory))
    with ThreadingHTTPServer(("127.0.0.1", args.port), handler) as server:
        print(f"Abra http://127.0.0.1:{args.port}/examples/abertura/")
        server.serve_forever()


if __name__ == "__main__":
    main()
