#!/usr/bin/env python3

import os
from flask import Flask, Blueprint, request, jsonify, url_for, session
from werkzeug.security import generate_password_hash
from ...models.user import User
from ...models import storage


auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/register', methods=['POST'])
def signup():
    # collect form data
    data = request.get_json()
    first_name = data.get('firstName')
    last_name = data.get('lastName')
    email = data.get('email')
    passwd = data.get('passwd')

    # check if this user already exists
    user_exists = storage.session.query(User).filter_by(email=email).first()
    if user_exists:
        print('User already exists!!!!!')  # DEBUG
        message = 'User already exists. If this is you, please log in'
        return (jsonify({'message': message}), 400)

    # create user to be added to the db
    user = User(
        lastName=last_name,
        firstName=first_name,
        email=email,
    )
    user.get_pwd_hash(passwd)  # set user.hashedPwd with the hashed password
    storage.new(user)
    storage.save()

    # return a success message, and where the user will be redirected
    secret_key = os.getenv('SECRET_KEY')
    session['current_user_id'] = user.Id

    return (
        jsonify(
            {
                'message': 'Successfully signed up!',
                'redirect': url_for('home_page'),
            }
        ),
        200,
    )


@auth_bp.route('/login', methods=['POST'])
def login():
    """Logs the user into the application, if they already have an account"""
    # collect form data
    data = request.get_json()

    # check if the user already exists
    email = data.get('email')
    existing_user = storage.session.query(User).filter_by(email=email).first()
    if not existing_user:
        message = 'No such user. Check your spellings and try again'
        return jsonify({'message': message}), 400

    # check that the password is valid
    password = data.get('password')
    hashed_password = existing_user.hashedPwd
    if not existing_user.pwd_is_correct(password):
        message = 'Incorrect email or password. Please try again'
        return jsonify({'message': message}), 400

    message = 'logged in successfully!'
    return (
        jsonify({'message': message, 'redirect': url_for('home_page')}),
        200,
    )
