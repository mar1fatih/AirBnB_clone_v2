#!/usr/bin/python3
"""/hbnb: display “HBNB”"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home_page():
    """returns Hello HBNB"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb_page():
    """returns HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def cisfun(text):
    """display C followed by text variable"""
    return 'C ' + text.replace('_', ' ')


@app.route("/python/<text>", strict_slashes=False)
def pythoniscool(text='is cool'):
    """display python followed by text variable"""
    return 'Python ' + text.replace('_', ' ')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
