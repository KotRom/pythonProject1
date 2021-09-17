# Flask needs to be installed with pip
# pip install flask


# Flask is main module, redirect and url_for are using links as navigation
from flask import Flask, redirect, url_for

# Initialise flask app
app = Flask(__name__)


# app.route is a decorator for function
# used to create a route and a page
@app.route('/')
def home():
    return '''Hello! This is the main page <h1>HELLO</h1>'''


# If you use <> for route, any name provided can be used
# <name> is a variable, anything after / will be taken as value
@app.route('/<name>')
# user() is a function for page
def user(name):
    return f'Hello {name}!'


# Example of redirect
@app.route('/admin')
# commented example will work with both '/admin' and '/admin/' routes
# @app.route('/admin/')
def admin():
    # admin='' is a variable
    return redirect(url_for("home", admin="Admin"))


# function to make sure that program runs from original file
if __name__ == "__main__":
    app.run()
