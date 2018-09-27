from flask import Flask, request, redirect, render_template
import os
import jinja2

template_dir= os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader= jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/valid-time')
def valid_time():
    time = request.args.get('time')
    return '<h1>You submitted {0}.  Thanks for submitting a valid time!</h1>'.format(time)

tasks = []

@app.route('/todos', methods=['POST', 'GET'])
def todos():

    if request.method == 'POST':
        task = request.form["task"]
        tasks.append(task)

    template = jinja_env.get_template('todos.html')
    return template.render(title="TODOs", tasks=tasks)

app.run()
