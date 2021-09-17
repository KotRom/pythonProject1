from flask import Flask, redirect, url_for, render_template, request
# request is used to get information from forms

app = Flask(__name__)

'''
Files needed:
    base2.html
    home2.html
    login.html
'''


# First let's check what is GET and POST
# Run app, try refreshing, look in command line
# 127.0.0.1 - - [05/May/2021 14:50:42] "GET / HTTP/1.1" 200 -
# GET request is used
@app.route("/")
def home():
    return render_template('home2.html')

# POST method is used when we submit form from HTML page
# Check form in login.html


# methods=["POST", "GET"] is a must for pages with forms
@app.route("/login", methods=["POST", "GET"])
def login():
    # request.method returns method that is used to load a page
    if request.method == "POST":
        # request.form['<field_name>'] is used to get data from form inputs
        user_name = request.form['nm']
        return redirect(url_for('user', usr=user_name))
    else:
        return render_template("login.html")


@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"


if __name__ == "__main__":
    app.run(debug=True)