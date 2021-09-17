from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
# install sql-alchemy module first
# pip install flask-sqlalchemy
import sqlalchemy

app = Flask(__name__)
app.secret_key = "helloworld"

# URI to connect to database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:G173!ksdNNa295Asdg13@localhost/flask_test'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
# prevents flask from tracking db modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.permanent_session_lifetime = timedelta(minutes=5)

# Create database object
db = SQLAlchemy(app)


# class for db objects
class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.String(100))
    email = db.Column("email", db.String(100))

    def __init__(self, name, email):
        self.name = name
        self.email = email


@app.route("/")
def home():
    return render_template('home2.html')


@app.route("/view")
def view():
    return render_template("view.html", values=users.query.all())


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user_name = request.form['nm']
        session["user"] = user_name
        # filter_by() method gets filtered data from db
        # query is applied to a class
        found_user = users.query.filter_by(name=user_name).first()
        if found_user:
            session["email"] = found_user.email
        else:
            usr = users(user_name, '')
            # don't forget to commit changes
            db.session.add(usr)
            db.session.commit()
        flash("Login successful!")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Already logged in!")
            return redirect(url_for("user"))
        return render_template("login.html")


@app.route("/user", methods=["POST", "GET"])
def user():
    email = None
    if "user" in session:
        user_name = session["user"]
        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email
            found_user = users.query.filter_by(name=user_name).first()
            # in order to change value is db object is loaded from db
            # then variable can be assigned with = sign
            found_user.email = email
            # don't forget to commit changes
            db.session.commit()
            flash('Email was saved')

        # IF get request
        else:
            if "email" in session:
                email = session["email"]

        print(email)
        return render_template("user.html", email=email, user_name=user_name)
    else:
        flash("You are not logged in!")
        return redirect(url_for('login'))


@app.route("/logout")
def logout():
    if "user" in session:
        user_name = session["user"]
        flash(f"{user_name} you have been logged out!", "info")  # second parameter is category, not compulsary
    session.pop("user", None)
    session.pop("email", None)
    return redirect(url_for("login"))


@app.route("/delete")
def del_user():
    user_name = session['user']
    # .delete() method deletes entry from db
    found_user = users.query.filter_by(name=user_name).delete()
    db.session.commit()
    session.pop("user", None)
    session.pop("email", None)
    return redirect(url_for('login'))


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)