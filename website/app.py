from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import sqlalchemy as sa

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///main.db"
db = SQLAlchemy(app)
migrate = Migrate(app=app, db=db)


class Apparatus(db.Model):
    sl_no = sa.Column(sa.Integer, primary_key=True, unique=True)
    name = sa.Column(sa.String(60))
    count = sa.Column(sa.Integer)


class Chemical(db.Model):
    sl_no = sa.Column(sa.Integer, primary_key=True, unique=True)
    name = sa.Column(sa.String(60))
    count = sa.Column(sa.Integer)


@app.route("/")
def home():
    return render_template("index2.html")


if __name__ == "__main__":
    app.run(debug=True)
