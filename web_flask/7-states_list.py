#!/usr/bin/python3
"""
Flask application module to display a list of states.

This module contains a simple Flask web application that connects to a storage backend,
retrieves state information, and displays it in a rendered HTML template. It includes
routes for displaying a list of states and a teardown function to close the storage
connection after each request.
"""

from flask import Flask, render_template
from models import *
from models import storage

app = Flask(__name__)

@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    Display a HTML page with the states listed in alphabetical order.

    This route queries the storage backend for all State objects, sorts them
    alphabetically by name, and passes them to the '7-states_list.html' template
    for rendering.
    """
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)

@app.teardown_appcontext
def teardown_db(exception):
    """
    Closes the storage on teardown.

    This function is called after each request to close the connection to the
    storage backend, ensuring that resources are properly released.
    """
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')

