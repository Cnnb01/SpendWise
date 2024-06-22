#!/usr/bin/env python3

"""Runs the spendwise application"""

from flask import Flask, render_template
from spendwise.api.v1.auth import auth_bp
from spendwise.models import storage

app = Flask(
    __name__,
    template_folder='spendwise/templates',
    static_folder='spendwise/static',
)

# register blueprints
app.register_blueprint(auth_bp, url_prefix='/api/v1')


@app.route('/', strict_slashes=False)
def home():
    """Shows the homepage of the application"""
    return render_template('signup.html')


if __name__ == '__main__':
    app.run(debug=True)
