from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import sqlalchemy as sa
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, PasswordField
from flask_login import current_user, LoginManager, UserMixin, logout_user, login_user, login_required

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///main.db"
app.secret_key = "sYqCrrQ3mUtsK9URfbKHG47Dvyer8TmKvtKA3_1Xqcg"
db = SQLAlchemy(app)
migrate = Migrate(app=app, db=db)
login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.login_view = "login"


class Apparatus(db.Model):
    sl_no = sa.Column(sa.Integer, primary_key=True, unique=True)
    name = sa.Column(sa.String(60))
    count = sa.Column(sa.Integer)


class Chemical(db.Model):
    sl_no = sa.Column(sa.Integer, primary_key=True, unique=True)
    name = sa.Column(sa.String(60))
    count = sa.Column(sa.Integer)


class User(db.Model, UserMixin):
    id = sa.Column(sa.Integer, primary_key=True, unique=True)
    username = sa.Column(sa.String(60))
    password = sa.Column(sa.String(60)) #60 ch


class AddApparatusForm(FlaskForm):
    name = StringField()
    count = IntegerField()

    submit = SubmitField("Add Apparatus")


class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Enter Password")

    submit = SubmitField("Login")


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))


@app.route("/", methods=["GET", "POST"])
@login_required
def home():
    apparatuses = Apparatus.query.all()
    form = AddApparatusForm()
    if form.validate_on_submit():
        apparatus = Apparatus(name=form.name.data, count=form.count.data)
        db.session.add(apparatus)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("index.html", apparatuses=apparatuses, form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.query.filter_by(username = username).first()
        if user.password == password:
            login_user(user)
            return redirect(url_for("home"))
        else:
            return redirect(url_for("login"))
    return render_template("login.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)