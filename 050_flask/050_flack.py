# https://github.com/GammaIntelligenceTraining/Python5
# pip install flask-
# pip install flask-sqlalchemy
# pip install pymysql
# pip install cryptography
# code comment plugins
# comment High Lighter plugins
# Kate AI autocomplete plugins

from flask_sqlalchemy import SQLAlchemy
import datetime

import flask
from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
import hashlib

app = Flask(__name__)
app.secret_key = 'helloworld'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:12345@localhost/flask_test_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.permanent_session_lifetime = timedelta(minutes=10)

db = SQLAlchemy(app)


class Users(db.Model):
    _id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(100))
    password = db.Column('password', db.String(100))
    email = db.Column('email', db.String(100))

    def __init__(self, name, password, email):
        self.name = name
        self.email = email
        self.password = password


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        session.permanent = True
        user_name = request.form['nm']
        user_pass = hashlib.md5(request.form['pw'].encode()).hexdigest()
        user_in_db = Users.query.filter_by(name=user_name).first()
        if user_in_db:
            if user_pass == user_in_db.password:
                session['user'] = user_name
                session['email'] = user_in_db.email
                flash('login successful')
                return redirect(url_for('user', name=user_name, email=user_in_db.email))
            else:
                flash('Wrong password')
                return render_template('login.html')
        else:
            new_user = Users(user_name, user_pass, '')
            db.session.add(new_user)
            db.session.commit()
            session['user'] = user_name
            session['email'] = ''
            flash('login successful')
            return redirect(url_for('user', name=user_name))

        session['user'] = user_name
        return redirect(url_for('user', name=user_name))
    else:
        if 'user' in session:
            flash('Already logged inn')
            return redirect(url_for('user', name=session['user']))
        else:
            return render_template('login.html')


@app.route('/user', methods=['POST', 'GET'])
def user():
    email = None
    if 'user' in session:
        user_name = session['user']
        if request.method == 'POST':
            email = request.form['em']
            session['email'] = email
            user_in_db = Users.query.filter_by(name=user_name).first()
            user_in_db.email = email
            flash('email was saved')
            db.session.commit()
        else:
            if 'email' in session:
                email = session['email']
            else:
                email = ''
        return render_template('user.html', name=user_name, email=email)
    else:
        flash('you are not logged inn')
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    if 'user' in session:
        user_name = session['user']
        session.pop('user', None)
        session.pop('email', None)
        flash('logged out')
    return redirect(url_for('login'))


@app.route('/delete')
def delete():
    if 'user' in session:
        user_name = session['user']
        user_in_db = Users.query.filter_by(name=user_name).delete()
        db.session.commit()
        session.pop('user', None)
        session.pop('email', None)
        flash('account was deleted')
        return redirect(url_for('login'))
    else:
        pass


if __name__ == '__main__':  # proveka chto main window eto main window
    db.create_all()  # sozdajot vse tablicy v baze dannyh po mpdeli users (bazu nado sozdat' samim)
    app.run(debug=True)

# EmmetEverywhere Plugin for HTML edit
# https://getbootstrap.com/docs/5.1/getting-started/introduction/

# CSS v  head
# <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">

# BUNDLE v konec body
# <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
