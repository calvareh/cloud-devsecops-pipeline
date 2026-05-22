from flask import Flask, request

app = Flask(__name__)

@app.route("/ping")
def ping():
    name = request.args.get("name", "world")
    return f"Hello {name}"
