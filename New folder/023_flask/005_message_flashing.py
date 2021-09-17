from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
# flash is used to output flashing messages


app = Flask(__name__)
app.secret_key = "helloworld"
app.permanent_session_lifetime = timedelta(minutes=5)

'''
Files needed:
    base2.html
    home2.html
    user.html
    login.html
'''


@app.route("/")
def home():
    return render_template('home2.html')


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST" and request.form['nm'] != '':
        session.permanent = True
        user_name = request.form['nm']
        session["user"] = user_name
        # flash('<string>') is used to create flashing message
        flash("Login successful!")
        # return redirect(url_for('user'))
        return render_template('user.html', user=user_name)
    else:
        if "user" in session:
            # flash('<string>') is used to create flashing message
            flash("Already logged in!")
            return render_template("user.html")
        return render_template("login.html")


@app.route("/logout")
def logout():
    if "user" in session:
        user_name = session["user"]
        # flash('<string>') is used to create flashing message
        # second arg is category, if you want to categorize messages
        flash(f"{user_name} you have been logged out!", "info")
        session.pop("user", None)
    return redirect(url_for("login"))


@app.route("/user")
def user():
    if "user" in session:
        user_name = session["user"]
        return f"<h1>{user_name}</h1>"
    else:
        # flash('<string>') is used to create flashing message
        flash("You are not logged in!")
        return redirect(url_for('login'))


if __name__ == "__main__":
    app.run(debug=True)