from datetime import datetime
import bcrypt
import flask
import flask_sqlalchemy
import sqlalchemy

from flask import render_template, request, redirect, url_for

app = flask.Flask(__name__)
app.config["SECRET_KEY"] = "XXXXXXXXXXXXXXX"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TARCK_MODIFICATIONS"] = False

salt = bcrypt.gensalt()

db = flask_sqlalchemy.SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "users"

    id = sqlalchemy.Column(
        sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=False)
    email = sqlalchemy.Column(sqlalchemy.String)
    username = sqlalchemy.Column(sqlalchemy.String, unique=False)
    password = sqlalchemy.Column(sqlalchemy.String, unique=False)
    created_at = sqlalchemy.Column(
        sqlalchemy.DateTime, default=datetime.now, unique=False)
    updated_at = sqlalchemy.Column(
        sqlalchemy.DateTime, default=datetime.now, unique=False)

    def __Str__(self):
        return "id={},email={},username={},password={}".format(self.id, self.email, self.username, self.password)

    def generate_password_hash(self, password):
        self.password = bcrypt.hashpw(password.encode('utf8'), salt)

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf8'), self.password.encode('utf8'))


db.create_all()


@app.route("/", methods=["GET"])
def index():
    return "Flask_tutorial_HOME"


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        print(email)
        print(password)
        return redirect(url_for("index"))


@app.route("/regist", methods=["GET", "POST"])
def regist():
    if request.method == "GET":
        return render_template("regist.html")
    elif request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        print(username)
        print(email)
        print(password)

        username = User()
        username.email = email()
        db.session.add(email)
        db.session.commit()
        db.session.close()
        print(db.session.query(User).all())

        return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
