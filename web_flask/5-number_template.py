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

