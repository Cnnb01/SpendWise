#!/usr/bin/env python3

"""Runs the spendwise application"""
import os
from dotenv import load_dotenv
from flask_session import Session
from flask_cors import CORS
from flask import Flask, render_template, session, abort, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from spendwise.api.v1 import apis
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://{}:{}@{}/{}'.format(
                os.getenv('SPENDWISE_MYSQL_USER'),
                os.getenv('SPENDWISE_MYSQL_PWD'),
                os.getenv('SPENDWISE_MYSQL_HOST'),
                os.getenv('SPENDWISE_MYSQL_DB'))

# For database migrations
db = SQLAlchemy(app)
migrate = Migrate(app=app, db=db)

# Import all models here for the migrations to work properly
from spendwise.models.user import User
from spendwise.models.category import Category
from spendwise.models.expense import Expense
from spendwise.models.budget import Budget
from spendwise.models.budget_category import BudgetCategory

# Initialize the server-side session
Session(app)

# register blueprints
app.register_blueprint(apis, url_prefix='/api/v1')
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

@app.errorhandler(503)
def maintenance_mode(error):
    """custom error handler for maintenance mode"""
    return render_template('errors/maintenance.html'), 503

@app.before_request
def check_for_maintenance():
    """Renders a maintenance page if the site is in maintenance mode"""
    if os.getenv('MAINTENANCE_MODE') == 'maintenance_mode' and not request.path.startswith('/static/'):
        abort(503)

@app.route('/', strict_slashes=False)
def landing_page():
    """Shows the landing page of the application"""
    return render_template('landing_page.html')

@app.route('/home', strict_slashes=False)
@requires_logged_in_user
def home_page():
    """Shows the home page for this user"""
    return render_template('homepage.html')

@app.route('/signup', strict_slashes=False)
def signup():
    """Shows the sign up page of the application"""
    return render_template('signup.html')

@app.route('/login', strict_slashes=False)
def home():
    """Shows the login page of the application as the first page"""
    return render_template('login.html')

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

@app.route('/budgets/<Id>/categories', strict_slashes=False)
def create_specific_budget(Id):
    """Shows the budget creation page of the application"""
    return render_template('category_display.html')

@app.route('/expenses/create', strict_slashes=False)
def create_expense():
    """Shows the expenses creation page of the application"""
    return render_template('expenses_create.html')

@app.route('/expenses/display')
def display_expenses():
    """Displays the list of expenses added"""
    return render_template('expenses_display.html')

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
