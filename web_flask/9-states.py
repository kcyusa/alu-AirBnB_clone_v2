#!/usr/bin/python3
"""
Starts a Flask web application to display states and their cities.

This module contains a Flask web application that connects to a storage backend,
retrieves state and city information, and displays it in a rendered HTML template.
It includes routes for displaying a list of states and optionally the cities within
a specified state, as well as a teardown function to close the storage connection
after each request.
"""

from flask import Flask, render_template
from models import *
from models import storage

app = Flask(__name__)

@app.route('/states', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def states(state_id=None):
    """
    Display a HTML page with states and optionally cities listed in alphabetical order.

    This route queries the storage backend for all State objects. If a state_id is
    provided, it modifies the state_id to match the storage key format. The states
    and state_id are passed to the '9-states.html' template for rendering.

    Args:
        state_id (str): The ID of a specific state to display its cities (optional).
    """
    states = storage.all("State")
    if state_id is not None:
        state_id = 'State.' + state_id
    return render_template('9-states.html', states=states, state_id=state_id)

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
