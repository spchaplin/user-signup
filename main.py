from flask import Flask, request, redirect, render_template
import jinja2
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    page_title = "User Signup"
    username = request.args.get("username")
    email = request.args.get("email")
    empty_field_error = request.args.get("empty_field_error")
    pw_error = request.args.get("pw_error")
    if not username:
        username = ""
    if not email:
        email = ""
    if not empty_field_error:
         empty_field_error = ""
    if not pw_error:
         pw_error = ""
    return render_template('login.html', page_title=page_title, empty_field_error=empty_field_error, username=username, email=email, pw_error=pw_error)

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

    #test for empty fields
    if username == "" or pw1 == "" or pw2 == "":
        is_valid_form = False
        empty_field_error = "field(s) were left blank"
    else:
        empty_field_error = ""
    #test password format and matching
    if " " in pw1 or pw1 != pw2 or len(pw1) < 3 or len(pw1) >20 or len(pw2) < 3 or len(pw2) > 20:
        pw_error = "Passwords must be 3 to 20 characters, cannot include spaces, and must match."
        is_valid_form = False
    else:
        pw_error = ""


    if is_valid_form:
        #get request
        return redirect("/welcome?username={0}".format(username))     
    else:
        #get request
        return redirect("/?empty_field_error={empty}&username={user}&email={email}&pw_error={pw_error}".format(empty=empty_field_error, user=username, email=email, pw_error=pw_error))
    
    
app.run()
