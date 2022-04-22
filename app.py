import flask
from flask import render_template, request, redirect, url_for

app = flask.Flask(__name__)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        print(email)
        print(password)
        return redirect(url_for("regist"))


@app.route("/", methods=["GET"])
def index():
    return "ni-hao"


@app.route("/regist", methods=["GET", "POST"])
def regist():
    if request.method == "GET":
        return render_template("regist.html")
    elif request.method == "POST":
        user = request.form.get("user")
        email = request.form.get("email")
        password = request.form.get("password")
        print(user)
        print(email)
        print(password)
        return redirect(url_for("regist"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
