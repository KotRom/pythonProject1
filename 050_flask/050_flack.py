from flask import Flask, render_template, request, redirect, url_for, session
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(seconds=5)


# EmmetEverywhere Plugin for HTML edit
# https://getbootstrap.com/docs/5.1/getting-started/introduction/

# CSS v  head
# <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">

# BUNDLE v konec body
# <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>


@app.route("/")
def home():
    title = 'Hello FLASK'
    people = ['Bob', 'Jack', 'Roman', 'Mary']
    return render_template('home.html', mytitle=title, people=people)


@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        session.permanent = True
        user_name = request.form['nm']
        session['user'] = user_name
        return render_template("user.html", usr=user_name)
    return render_template('login.html')


@app.route("/user")
def user(user_name):
    if 'user' in session:
        user_name = session['user']
        return render_template("user.html", usr=user_name)
    else:
        return redirect(url_for('login'))


@app.route("/logout")
def logout():
    return "<p>LOGOUT page</p>"


if __name__ == '__main__':
    app.run(debug=True)
