#!/usr/bin/env python3

from flask import Flask, Blueprint, request, jsonify
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

    return (
        jsonify({'message': 'Successfully signed up!'}),
        200,
    )
