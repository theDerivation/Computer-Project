from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import sqlalchemy as sa
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///main.db"
app.secret_key = "sYqCrrQ3mUtsK9URfbKHG47Dvyer8TmKvtKA3_1Xqcg"
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


class AddApparatusForm(FlaskForm):
    name = StringField()
    count = IntegerField()

    submit = SubmitField("Add Apparatus")


@app.route("/", methods=["GET", "POST"])
def home():
    apparatuses = Apparatus.query.all()
    form = AddApparatusForm()
    if form.validate_on_submit():
        apparatus = Apparatus(name=form.name.data, count=form.count.data)
        db.session.add(apparatus)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("index2.html", apparatuses=apparatuses, form=form)


if __name__ == "__main__":
    app.run(debug=True)
