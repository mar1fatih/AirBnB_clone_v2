#!/usr/bin/python3
"""/hbnb: display “HBNB”"""
from flask import Flask
app = Flask(__name__)


@app.route('/')
def home_page():
    """returns Hello HBNB"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb_page():
    """returns HBNB"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
