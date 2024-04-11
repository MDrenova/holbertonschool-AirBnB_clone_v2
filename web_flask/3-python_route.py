#!/usr/bin/python3
"""Web application"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """Set route"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Set route"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def display_text(text):
    """Set route"""
    return "C " + text.replace("_"," ")

@app.route("/python/", defaults={'text': "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def display_text_python(text):
    """Set route"""
    if text:
        return "Python " + text.replace("_"," ")
    else:
        return "Python is cool"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
