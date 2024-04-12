#!/usr/bin/python3
"""Web application"""
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join
                                   (os.path.dirname(__file__), '..')))
from flask import Flask, render_template  # noqa: E402
from models import storage  # noqa: E402
from models.state import State  # noqa: E402

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


@app.route("/cities_by_states", strict_slashes=False)
def states_list_cities():
    """
    States display
    """
    states = storage.all("State").values()
    return render_template('8-cities_by_states.html', states=states)

@app.route("/states", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def states_list_city1(id=None):
    states = storage.all(State).values()
    state = None
    if id:
        state = next((s for s in states if s.id == id), None)
    return render_template('9-states.html', states=states, state=state)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
