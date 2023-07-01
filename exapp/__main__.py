import os
from pathlib import Path
import sys


from flask import Flask, Response, make_response, send_from_directory
import click

app = Flask(__name__)

PUBLIC_DIR = Path(os.getcwd()) / "public"


@app.get("/hello")
def hello() -> str:
    return "hello"


@app.route('/<path:path>')
def download_file(path: str) -> Response:
    items = path.split("/")  # todo: 雑実装
    d = "/".join(items[:-1])
    f = items[-1]
    return send_from_directory(PUBLIC_DIR / d, f)


@app.route("/")
def index():
    return send_from_directory(PUBLIC_DIR, "index.html")


@click.command()
@click.option("--change-static", is_flag=True, default=False)
def main(change_static: bool):
    if change_static:
        app.static_folder = "static2"

    app.run(host="0.0.0.0", debug=True, port=20091)


if __name__ == "__main__":
    main()
