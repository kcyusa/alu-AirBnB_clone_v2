#!/usr/bin/python3
"""
Starts a Flask web application to display states and their cities.

This module contains a simple Flask web application that connects to a storage backend,
retrieves state and city information, and displays it in a rendered HTML template.
It includes routes for displaying states and their respective cities and a teardown
function to close the storage connection after each request.
"""

from flask import Flask, render_template
from models import *
from models import storage

app = Flask(__name__)

@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """
    Display a HTML page with states and their cities listed in alphabetical order.

    This route queries the storage backend for all State objects and their related
    City objects, and passes them to the '8-cities_by_states.html' template for rendering.
    """
    states = storage.all("State").values()
    return render_template('8-cities_by_states.html', states=states)

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

