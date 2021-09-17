from flask import Flask, redirect, url_for, render_template

# Initialise flask app
app = Flask(__name__)


'''
Files needed:
    home.html
    index.html
'''


# # Sample below shows how to send many variables
# @app.route('/<name>')
# def home(name):
#     # return render_template('index.html', name=name, r=2, content=['Jack', 'Mary', 'Sarah'])
#     return render_template('index.html', name=name, r=2, content=['Jack', 'Mary', 'Sarah'])


@app.route('/home')
def home_2():
    # first arg is a html file, other are optional variables
    return render_template("home.html", content="Testing")


# app.run(debug=True) will start server in debug mode
# meaning that it will refresh all changes in code automatically
if __name__ == "__main__":
    app.run(debug=True)
