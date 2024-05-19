#!/usr/bin/python3
"""Flask web application"""
from flask import Flask, reder_template
from models import storage

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """display all states"""
    state = list(storage.all('State').values())
    states = sorted(state, key=state.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """close the storage"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
