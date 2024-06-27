#!/usr/bin/env python3

"""Represents a user of the application"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource
from flask_bcrypt import Bcrypt
from sqlalchemy import Column, Integer, String
from .base_model import Base
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'  # Example config, adjust as necessary

db = SQLAlchemy(app)
api = Api(app)
bcrypt = Bcrypt(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)



class User(Base):
    """A user of the application"""

    __tablename__ = 'users'

    Id = Column(
        Integer, nullable=False, autoincrement=True, primary_key=True
    )
    lastName = Column(String(150), nullable=False)
    firstName = Column(String(150), nullable=False)
    email = Column(String(80), nullable=False)
    hashedPwd = Column(String(256), nullable=False)

    # one-to-many relationship with Budget
    budgets = relationship('Budget', back_populates='user')

    def get_pwd_hash(self, password):
        """Gets a hashed version of the provided password"""
        self.hashedPwd = generate_password_hash(password)

    def pwd_is_correct(self, password):
        """Checks whether the provided password matches the stored hash for this
        user"""
        return check_password_hash(self.hashedPwd, password)
