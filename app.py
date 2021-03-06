from flask import Flask, render_template, request, flash
import psycopg2
from psycopg2.pool import SimpleConnectionPool
import os
from dotenv import load_dotenv
from contextlib import contextmanager
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SubmitField,
)
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea
from flask_ckeditor import CKEditorField


load_dotenv()
app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY")
database_url = os.environ["POSTGRES_URI"]
# print(database_url)
app.config["SQLALCHEMY_DATABASE_URI"] = database_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self) -> str:
        return f"User - {self.username} \nEmail - {self.email}"


class UserForm(FlaskForm):
    no = StringField("ID", validators=[DataRequired()])
    username = StringField("Username", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    submit = SubmitField("Add users")


@app.route("/", methods=["GET", "POST"])
def index():
    form = UserForm()
    if request.method == "POST":
        user = User(id=form.no.data, username=form.username.data, email=form.email.data)
        form.no.data = ""
        form.username.data = ""
        form.email.data = ""

        db.session.add(user)
        db.session.commit()
        flash("User added")
    return render_template("/index.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
