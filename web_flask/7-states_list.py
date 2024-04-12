#!/usr/bin/python3
"""Web application"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def close_all(error):
    """
    func to remove sqlalchemy session
    """
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    """
    States display
    """
    states = storage.all("State").values()
    return render_template('7-states_list.html', states=states)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
