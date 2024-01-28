#!/usr/bin/python3
"""
Starts a Flask web app on 0.0.0.0:5000
Routes:
    / - displays "Hello HBNB"
    /hbnb - displays "HBNB"
"""
from Flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def Hello_HBNB():
    return 'Hello HBNB'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
