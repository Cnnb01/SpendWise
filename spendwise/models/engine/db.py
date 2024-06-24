#!/usr/bin/env python3

"""Starts the database, and defines possible database actions"""

import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
from ..base_model import Base
from ..budget import Budget
from ..category import Category
from ..expense import Expense
from ..user import User

# our classes and id mapping
classes = {
    "Budget": Budget,
    "Category": Category,
    "Expense": Expense,
    "User": User,
}

id_names = {
    "Budget": 'budgetId',
    "Category": 'categoryId',
    "Expense": 'expenseId',
    "User": 'userId',
}

class DB:
    """Manages database storage actions for the application"""

    def __init__(self):
        #create_engine creates a connection to db using creds from env vars
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                os.getenv('SPENDWISE_MYSQL_USER'),
                os.getenv('SPENDWISE_MYSQL_PWD'),
                os.getenv('SPENDWISE_MYSQL_HOST'),
                os.getenv('SPENDWISE_MYSQL_DB'),
            )
        )
        self.__session = None
        # drop all tables in the test environment
        if os.getenv('SPENDWISE_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)

        self.reload() #initializes the db session.

    @property
    def session(self):
        """Returns the current database session"""
        return self.__session

    def all(self, cls):
        """Returns all objects for the provided class"""
        objs = self.__session.query(cls).all()#retrieves all records of the given class from the database.
        new_dict = {}

        for obj in objs:
            key_name = id_names.get(obj.__class__.__name__)#retrieves the name of the pk for the class of the current object (obj). It looks up the class name in the id_names dictionary
            if key_name:
                key = obj.__class__.__name__ + '.' + str(getattr(obj, key_name))
                #key = 'Expense' + '.' + '1'
                new_dict[key] = obj #stores each object in a dictionary with a unique key
            else:
                print(f"Warning: Attribute not found for class {obj.__class__.__name__}")
        return new_dict

    def new(self, obj):
        """Adds this object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Saves and applies all current db session changes"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Creates all tables defined in the database schema, and starts a database session"""
        Base.metadata.create_all(self.__engine) #creates all tables in the database that are defined by the models.
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def get(self, cls, id):
        """Retrieve an object based on its class and primary key"""
        key_name = id_names.get(cls.__name__) #cls.__name__ is the name of the class specified eh Expense
        if not key_name:
            return None
        return self.__session.query(cls).filter(getattr(cls, key_name) == id).first()
