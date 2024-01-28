#!/usr/bin/python3
"""
Starts a flask web app on 0.0.0.0:5000 using data fetching
Defines routes for displaying State and City Objects
"""
from flask import Flask, render_template
from models import *
from models improt storage
app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def filters():
    states = storage.all("State").values()
    amenities = storage.all("Amenity").values()
    return render_template('10-hbnb_filters.html', states=states,
                           amenities=amenities)

    
@app.teardonw_appcontext
def teardonw_db(exception):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0", port=5000)
