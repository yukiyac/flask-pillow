from flask import Flask
from flask import render_template, request, redirect, flash
from process import paste_frame
import secrets


app = Flask(__name__)

app.secret_key = secrets.token_urlsafe(32)


@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["uploadFile"]
    img = Image.open(file)
    return "Hello Upload"


if __name__ == "__main__":
    app.run(debug=True)
