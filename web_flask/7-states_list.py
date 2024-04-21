#!/usr/bin/python3
"""Flask web application"""
from flask import Flask, reder_template
from models import *

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """display all states"""
    states = list(storage.all('states').values())
    states = sorted(states, key=states.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(exception):
    """closes the storage on teardown"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
