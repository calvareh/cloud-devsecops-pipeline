from flask import Flask, request, escape

app = Flask(__name__)

@app.route("/ping")
def ping():
    name = request.args.get("name", "world")
    safe_name = escape(name)
    return f"Hello {safe_name}"
