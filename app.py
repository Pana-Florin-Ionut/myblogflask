from flask import Flask, render_template
import psycopg2
from psycopg2.pool import SimpleConnectionPool
import os
from dotenv import load_dotenv
from contextlib import contextmanager
from flask_sqlalchemy import SQLAlchemy

load_dotenv()
app = Flask(__name__)

database_url = os.environ["POSTGRES_URI"]
# print(database_url)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("POSTGRESQL_DATABASE_URI")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


@app.route("/")
def index():
    return render_template("/index.html")


if __name__ == "__main__":
    app.run(debug=True)
