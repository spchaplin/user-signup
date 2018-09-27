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
    username_format_error = request.args.get("username_format_error")
    pw1_format_error = request.args.get("pw1_format_error")
    pw2_format_error = request.args.get("pw2_format_error")
    pw_match_error = request.args.get("pw_match_error")
    email_format_error = request.args.get("email_format_error")

    if not username:
        username = ""
    if not email:
        email = ""
    
    if not username_format_error:
        username_format_error = ""
    else:
        username = ""

    if not email_format_error:
        email_format_error = ""
    else:
        email = ""
    
    if not pw1_format_error:
        pw1_format_error = ""
    if not pw2_format_error:
        pw2_format_error = ""
    if not pw_match_error:
        pw_match_error = ""
    return render_template('login.html', page_title=page_title, username=username, email=email, username_format_error=username_format_error, pw1_format_error=pw1_format_error, pw2_format_error=pw2_format_error, pw_match_error=pw_match_error, email_format_error=email_format_error)

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

    #test for valid username
    if " " in username or len(username) < 3 or len(username) >20:
        is_valid_form = False
        username_format_error = "Usernames must be 3 to 20 characters, and cannot include spaces."
    else:
        username_format_error = ""

    #test pw1 format
    if " " in pw1 or len(pw1) < 3 or len(pw1) >20:
        is_valid_form = False
        pw1_format_error = "Passwords must be 3 to 20 characters, and cannot include spaces."
    else:
        pw1_format_error = ""
     #test pw2 format
    if " " in pw2 or len(pw2) < 3 or len(pw2) >20:
        is_valid_form = False
        pw2_format_error = "Passwords must be 3 to 20 characters, and cannot include spaces."
    else:
        pw2_format_error = ""
     #test pw match format
    if pw1 != pw2:
        is_valid_form = False
        pw_match_error = "Passwords must match."
    else:
        pw_match_error = ""

    #test for valid email
    if len(email) > 0 and (email.count(" ") != 0 or email.count("@") != 1 or email.count(".") != 1 or len(email) < 3 or len(email) > 20):
        is_valid_form = False
        email_format_error = 'If provided, email must have one "@", one ".", no spaces, and be 3 to 20 characters long.'
    else:
        email_format_error = ""

    if is_valid_form:
        #get request
        return redirect("/welcome?username={0}".format(username))     
    else:
        #get request
        return redirect("/?username={username}&email={email}&username_format_error={username_format_error}&pw1_format_error={pw1_format_error}&pw2_format_error={pw2_format_error}&pw_match_error={pw_match_error}&email_format_error={email_format_error}".format(username=username, email=email, username_format_error=username_format_error, pw1_format_error=pw1_format_error, pw2_format_error=pw2_format_error, pw_match_error=pw_match_error, email_format_error=email_format_error))
    
app.run()
