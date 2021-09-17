from flask import Flask, redirect, url_for, render_template, request, session
# session is for saving user data to cookies
# Import timedelta for permanent sessions permanent sessions
from datetime import timedelta


'''
Files needed:
    base2.html
    home2.html
    login.html
'''

app = Flask(__name__)

'''Each Flask web application contains a secret key which used to sign session cookies for protection 
against cookie data tampering. It's very important that an attacker doesn't know the value of this secret key. 
Your application is using a weak/known secret key and Acunetix managed to guess this key.'''

# Secret key
app.secret_key = "helloworld"

# timedelta is used to set session timeout
# permanent_session_lifetime used to limit session
app.permanent_session_lifetime = timedelta(seconds=5)
# app.permanent_session_lifetime = timedelta(minutes=10)


@app.route("/")
def home():
    return render_template('home2.html')


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        # session.permanent activates session limit while True
        session.permanent = True
        user_name = request.form['nm']
        session["user"] = user_name
        return redirect(url_for('user'))
    else:
        # Check if user is in a session
        # session is a dictionary where "user" is a key
        # this is why we pass it as string
        if "user" in session:
            return redirect(url_for("user"))
        return render_template("login.html")


# logout function will delete user data from session
@app.route("/logout")
def logout():
    # None must be as a second argument, comes from documentation
    session.pop("user", None)
    return redirect(url_for("login"))


@app.route("/user")
def user():
    if "user" in session:
        user_name = session["user"]
        return f"<h1>{user_name}</h1>"
    else:
        return redirect(url_for('login'))


if __name__ == "__main__":
    app.run(debug=True)