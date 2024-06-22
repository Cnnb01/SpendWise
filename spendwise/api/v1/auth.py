#!/usr/bin/env python3

from flask import Flask, Blueprint, request
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

    # create user to be added to the db
    user = User(
        lastName=last_name,
        firstName=first_name,
        email=email,
    )
    user.get_pwd_hash(passwd)  # set user.hashedPwd with the hashed password
    storage.new(user)
    storage.save()

    return "Registration successful!"
