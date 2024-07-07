#!/usr/bin/env python3

import os
from flask import (
    Flask,
    Blueprint,
    request,
    jsonify,
    url_for,
    session,
    redirect,
    flash
)
from werkzeug.security import generate_password_hash
from ...models.user import User
from ...models import storage
from . import apis


@apis.route('/register', methods=['POST'])
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
    message = 'Successfully signed up!'
    flash(message, 'success')

    return (
        jsonify(
            {
                'redirect': url_for('home_page'),
            }
        ),
        200,
    )


@apis.route('/login', methods=['POST'])
def login():
    """Logs the user into the application, if they already have an account"""
    # collect form data
    data = request.get_json()

    # check if the user already exists
    email = data.get('email')
    try:
        existing_user = storage.session.query(User).filter_by(email=email).first()
    except Exception as e:
        storage.session.rollback()
        return jsonify({'error': str(e)}), 500

    if not existing_user:
        message = 'Incorrect email or password. Please try again'
        flash(message, 'error')
        return jsonify({'message': message}), 400

    # check that the password is valid
    password = data.get('password')
    hashed_password = existing_user.hashedPwd
    if not existing_user.pwd_is_correct(password):
        message = 'Incorrect email or password. Please try again'
        flash(message, 'error')
        return jsonify({'message': message}), 400

    session['current_user_id'] = existing_user.Id
    message = 'You logged in successfully!'
    flash(message, 'success')
    return (
        jsonify({'message': message, 'redirect': url_for('home_page')}),
        200,
    )


@apis.route('/logout')
def logout():
    """Logs the user out of the application, redirecting them to the login page"""
    session.pop('current_user_id', None)  # end this users session

    # redirect the user to the login page
    return redirect(url_for('home'))
