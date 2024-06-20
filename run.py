#!/usr/bin/env python3

"""Runs the spendwise application"""

from flask import Flask, render_template
from spendwise.models import storage

app = Flask(
    __name__, template_folder='spendwise/templates', static_folder='spendwise/static'
)


@app.route('/', strict_slashes=False)
def home():
    """Shows the homepage of the application"""
    return render_template('signup.html')


if __name__ == '__main__':
    app.run(debug=True)
