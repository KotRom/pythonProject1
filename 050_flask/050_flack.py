# https://github.com/GammaIntelligenceTraining/Python5
import datetime

import flask
from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
import hashlib

app = Flask(__name__)
app.secret_key = 'helloworld'
app.permanent_session_lifetime = timedelta(minutes=10)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        session.permanent = True
        user_name = request.form['nm']
        session['user'] = user_name
        return redirect(url_for('user', name=user_name))
    else:
        if 'user' in session:
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
        else:
            if 'email' in session:
                email = session['email']
            else:
                email = ''
        return render_template('user.html', name=user_name, email=email)
    else:
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    if 'user' in session:
        user_name = session['user']
    session.pop('user', None)
    session.pop('email', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)

# EmmetEverywhere Plugin for HTML edit
# https://getbootstrap.com/docs/5.1/getting-started/introduction/

# CSS v  head
# <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">

# BUNDLE v konec body
# <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>

