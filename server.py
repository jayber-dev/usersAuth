
from distutils.log import debug
from flask import Flask, render_template, redirect,url_for,request,flash
from flask_login import LoginManager, login_required, current_user, logout_user 
import flask_sqlalchemy
import flask_wtf
import flask_wtf


app = Flask(__name__)

user = {
    'email':'jayber1@gmail.com',
    'pass':'1234',
}

@app.route('/',methods=['GET','POST'])
def home ():
        
    return render_template('index.html')
    
@app.route("/user_home")
def user_page():   
    data = request.args
    print(data)
    if data['pass'] == user['pass']:
        return render_template("user_home.html" , name=data['email'])
    else:
        return redirect(url_for('home'))
    

if "__main__" == __name__ :
    app.run(debug=True)