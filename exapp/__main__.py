from flask import Flask

app = Flask(__name__)


@app.get("/hello")
def hello() -> str:
    return "hello"


def main():
    app.run(host="0.0.0.0", debug=True, port=20091)


if __name__ == "__main__":
    main()
