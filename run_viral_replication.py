"""Utility script to preview the viral_replication.html page in a browser."""
from __future__ import annotations

import argparse
import functools
import http.server
import socket
import socketserver
import webbrowser
from pathlib import Path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Serve viral_replication.html over HTTP so it can be viewed in a browser."
    )
    parser.add_argument(
        "file",
        nargs="?",
        default="viral_replication.html",
        help="Path to the HTML file to preview (default: viral_replication.html).",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=8000,
        help="Port to bind the temporary HTTP server to (default: 8000).",
    )
    parser.add_argument(
        "--no-browser",
        action="store_true",
        help="Only start the server; do not try to open a browser window automatically.",
    )
    return parser


def ensure_port_available(port: int) -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        try:
            sock.bind(("127.0.0.1", port))
        except OSError as exc:  # pragma: no cover - informative branch
            raise SystemExit(f"Port {port} is not available: {exc}") from exc


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    file_path = Path(args.file).expanduser().resolve()
    if not file_path.exists():
        parser.error(f"Could not find HTML file at {file_path}")

    ensure_port_available(args.port)

    handler = functools.partial(
        http.server.SimpleHTTPRequestHandler,
        directory=str(file_path.parent),
    )
    with socketserver.TCPServer(("127.0.0.1", args.port), handler) as httpd:
        url = f"http://127.0.0.1:{args.port}/{file_path.name}"
        print(f"Serving {file_path.name} at {url}\nPress Ctrl+C to stop.")

        if not args.no_browser:
            try:
                webbrowser.open(url)
            except webbrowser.Error as exc:  # pragma: no cover - environment specific
                print(f"Could not open browser automatically: {exc}")

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
