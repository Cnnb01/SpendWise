#!/usr/bin/env python3

from flask import Flask, Blueprint, request, jsonify, url_for
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
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = storage.session.query(User).filter_by(email=email).first()
    if not user or not check_password_hash(user.hashedPwd, password):
        return jsonify({'message': 'Invalid email or password'}), 401

    return jsonify(
        {
            'message': 'Successfully logged in!',
            'redirect': url_for('home_page'),
        }
    ), 200

app = Flask(__name__)
app.register_blueprint(auth_bp, url_prefix='/api/v1')

if __name__ == '__main__':
    app.run(debug=True)
