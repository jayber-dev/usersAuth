from distutils.log import debug
from flask import Flask, render_template, redirect,url_for
import flask_login
import flask_sqlalchemy

app = Flask(__name__)
# wow wow


@app.route('/')
def home ():
    return render_template('index.html')
    
@app.route("/login")
def user_login():
    return render_template("login.html")

if "__main__" == __name__ :
    app.run(debug=True)