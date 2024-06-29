#!/usr/bin/env python3

"""Runs the spendwise application"""
import os
from dotenv import load_dotenv
from flask_session import Session
from flask_cors import CORS
from flask import Flask, render_template, session
from spendwise.api.v1.auth import auth_bp
from spendwise.api.v1.expenses import app_views
from spendwise.api.v1.categories import app_views
from spendwise.api.v1.budgets import app_views
from spendwise.models import storage

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
app.register_blueprint(app_views, url_prefix='/api/v1')
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


@app.route('/', strict_slashes=False)
def home():
    """Shows the homepage of the application"""
    return render_template('signup.html')


@app.route('/login', methods=['GET'], strict_slashes=False)
def login():
    """Shows the login page of the application"""
    return render_template('login.html')


@app.route('/budgets/create', strict_slashes=False)
def create_budget():
    """Shows the budget creation page of the application"""
    return render_template('budgets_create.html')


@app.route('/home', strict_slashes=False)
def home_page():
    """Shows the home page for this user"""
    return render_template('homepage.html')


if __name__ == '__main__':
    app.run(debug=True)
