import random

from flask import render_template

from .. import app, log


@app.route('/')
def index():
    log.info('starting at index')
    greeting = random.choice(['Howdy', 'Hi There', 'Hola', 'Greetings'])
    raise Exception('nooooo')
    return render_template('index.html', greeting=greeting)
