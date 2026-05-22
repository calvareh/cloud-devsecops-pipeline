from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route("/ping")
def ping():
    name = request.args.get("name", "world")
    return render_template_string("Hello {{ name }}", name=name)
