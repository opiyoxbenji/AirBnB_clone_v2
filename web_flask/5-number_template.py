#!/usr/bin/python3
"""
Starts a Flask web app
Routes:
    / - displays “Hello HBNB!”
    /hbnb - displays “HBNB”
    /c/<text> - displays “C ” followed by the value of the text variable
    /python/(<text>) - displays “Python ” followed by the value of the text variable
    /number/<n> - displays “n is a number” only if n is an integer
    /number_template/<n> - displays a HTML page only if n is an integer
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def Hello_HBNB():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_way(text):
    return 'C ' + text.replace('_', ' ')


@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def int_validator(n):
    return '{:d} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def html_int_validator(n):
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
