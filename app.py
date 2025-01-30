from datetime import datetime
from decouple import config
from flask import Flask, jsonify


app = Flask(__name__)


@app.route("/", methods="GET")
def main():
    response = jsonify(
        {
            "email": config("HNG12_EMAIL"),
            "current_datetime": datetime.utcnow().isoformat(timespec="seconds") + "Z",
            "github_url": config("GITHUB_URL"),
        }
    )

    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


if __name__ == "__main__":
    app.run()
