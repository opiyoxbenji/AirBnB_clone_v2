#!/usr/bin/python3
"""
Starts a Flask web app
Routes:
    / - display “Hello HBNB!”
    /hbnb - display “HBNB”
    /c/<text> - display “C ” followed by the value of the text variable
    /python/(<text>) - display “Python ” followed by the value of the text variable
    /number/<n> - display “n is a number” only if n is an integer
    /number_template/<n> - display a HTML page only if n is an integer
    /number_odd_or_even/<n> - display a HTML page only if n is an integer
"""
from flask import Flask, render_template
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


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def html_even_odd_validator(n):
    if n % 2 == 0:
        even_or_odd = 'even'
    else:
        even_or_odd = 'odd'
    return render_template('6-number_odd_or_even.html',
                           n=n, even_or_odd=even_or_odd)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
