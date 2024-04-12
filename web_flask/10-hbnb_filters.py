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


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """
    dynamic routing
    """
    data = [value for value in storage.all(State).values()]
    amenities = [amenity.to_dict()['name'] for amenity in
                 storage.all(Amenity).values()]
    return render_template('10-hbnb_filters.html',
                           data=data, amenities=amenities)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
