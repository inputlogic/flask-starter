import random

from flask import render_template

from . import app


@app.route('/')
def index():
    greeting = random.choice(['Howdy', 'Hi There', 'Hola', 'Greetings'])
    return render_template('index.html', greeting=greeting)
