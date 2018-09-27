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
    is_valid_form = False
    if is_valid_form:
        username = request.form["username"]
        #get request
        return redirect("/welcome?username={0}".format(username))     
    else:
        #get request
        return redirect("/")
    
    

# def validate():
#     username = request.form['username']
#     pw1 = request.form['password']
#     pw2 = request.form['re_enter_password']
#     email = request.form['email']


















@app.route("/validate-time")
def display_time_form():
    return render_template('time_form.html')

def is_integer(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

@app.route("/validate-time", methods=['POST'])
def validate_time():
    hours = request.form['hours']
    minutes = request.form['minutes']

    hours_error = ''
    minutes_error = ''

    if not is_integer(hours):
        hours_error = "Not a valid integer."
        hours = ''
    else:
        hours = int(hours)
        if hours > 23 or hours < 0:
            hours_error = "Hours value out of range(0-23)"
            hours = ''
    if not is_integer(minutes):
        minutes_error = "Not a valid integer."
        minutes = ''
    else:
        minutes = int(minutes)
        if minutes > 59 or minutes < 0:
            minutes_error = "Minutes value out of range(0-59)"
            minutes = ''

    if not minutes_error and not hours_error:
        time = str(hours) + ":" + str(minutes)
        return redirect('/valid-time?time={0}'.format(time))
    else:  
        return render_template('time_form.html', hours_error=hours_error, minutes_error=minutes_error, hours=hours,minutes=minutes)
                                
@app.route('/valid-time')
def valid_time():
    time = request.args.get('time')
    return '<h1>You submitted {0}. Thanks for submitting a valid time!</h1><br><a href="http://127.0.0.1:5000/validate-time">Back to Main</a>'.format(time)

tasks = []

@app.route('/todos', methods=['POST', 'GET'])
def todos():

    if request.method == 'POST':
        task = request.form["task"]
        tasks.append(task)

    return render_template('todos.html', title="TODOs", tasks=tasks)

app.run()


app.run()
