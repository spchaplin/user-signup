from flask import Flask, request, redirect, render_template
import jinja2
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    page_title = "User Signup"
    return render_template('login.html', page_title=page_title)

@app.route("/welcome")
def welcome():
    username = request.args.get("username")
    page_title = "Welcome!"
    return render_template('welcome.html', username=username, page_title=page_title)

#handle posted form
@app.route("/", methods=['POST'])
#logic for form validation goes here
def validate():
    is_valid_form = True
    #anything that invalidates form goes below
    username = request.form['username']
    pw1 = request.form['password']
    pw2 = request.form['re_enter_password']
    email = request.form['email']


    if is_valid_form:
        username = request.form["username"]
        #get request
        return redirect("/welcome?username={0}".format(username))     
    else:
        #get request
        return redirect("/")
    
    
app.run()
