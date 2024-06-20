#!/usr/bin/env python3

"""Runs the spendwise application"""

from flask import Flask
from app.models import storage

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """The home screen that is shown"""
    return 'Welcome to spendwise!'


if __name__ == '__main__':
    app.run()
