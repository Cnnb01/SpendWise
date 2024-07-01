#!/usr/bin/env python3

"""Runs the spendwise application"""
import os
from dotenv import load_dotenv
from flask_session import Session
from flask_cors import CORS
from flask import Flask, render_template, session
from spendwise.api.v1.auth import auth_bp
from spendwise.api.v1.expenses import apis
from spendwise.api.v1.categories import apis
from spendwise.api.v1.budgets import apis
from spendwise.models import storage
from spendwise.api.v1.decorators import requires_logged_in_user

app = Flask(
    __name__,
    template_folder='spendwise/templates',
    static_folder='spendwise/static',
)

# app-specific configurations
load_dotenv()
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SESSION_TYPE'] = 'filesystem'

# Initialize the server-side session
Session(app)

# register blueprints
app.register_blueprint(auth_bp, url_prefix='/api/v1')
app.register_blueprint(apis, url_prefix='/api/v1')
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


@app.route('/', strict_slashes=False)
@app.route('/login', strict_slashes=False)
def home():
    """Shows the login page of the application as the first page"""
    return render_template('login.html')


@app.route('/signup', strict_slashes=False)
def signup():
    """Shows the sign up page of the application"""
    return render_template('signup.html')

@app.route('/budgets', strict_slashes=False)
def budgets():
    """Shows the budget page of the application"""
    return render_template('budgets.html')

@app.route('/budgets/create', strict_slashes=False)
def create_budget():
    """Shows the budget creation page of the application"""
    return render_template('budgets_create.html')


@app.route('/budgets/display')
def display_budgets():
    return render_template('budgets_display.html')


@app.route('/home', strict_slashes=False)
@requires_logged_in_user
def home_page():
    """Shows the home page for this user"""
    return render_template('homepage.html')


@app.after_request
def add_headers(response):
    """Adds the specified headers to the response object, to control browser
    behaviour

    MDN docs: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cache-Control
    """
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate'
    return response


if __name__ == '__main__':
    app.run(debug=True)
