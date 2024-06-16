#!/usr/bin/python3
"""
Starts a Flask web application to display states and amenities.

This module contains a Flask web application that connects to a storage backend,
retrieves state and amenity information, and displays it in a rendered HTML template.
It includes routes for displaying a filtered view similar to a static HTML page,
as well as a teardown function to close the storage connection after each request.
"""

from flask import Flask, render_template
from models import *
from models import storage

app = Flask(__name__)

@app.route('/hbnb_filters', strict_slashes=False)
def filters():
    """
    Display a HTML page with states and amenities.

    This route queries the storage backend for all State and Amenity objects,
    and passes them to the '10-hbnb_filters.html' template for rendering.

    The rendered page is intended to be similar to the '6-index.html' static page,
    showing a list of states and amenities for filtering purposes.
    """
    states = storage.all("State").values()
    amenities = storage.all("Amenity").values()
    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)

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
