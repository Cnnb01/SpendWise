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

# classes = {"Budget": Budget, "BudgetCategory":BudgetCategory, "Category":Category, "Expense":Expense, "User":User}

class DB:
    """Manages database storage actions for the application"""

    def __init__(self):
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                os.getenv('SPENDWISE_MYSQL_USER'),
                os.getenv('SPENDWISE_MYSQL_PWD'),
                os.getenv('SPENDWISE_MYSQL_HOST'),
                os.getenv('SPENDWISE_MYSQL_DB'),
            )
        )
        # drop all tables in the test environment
        if os.getenv('SPENDWISE_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    @property
    def session(self):
        """Returns the current database session"""
        return self.__session

    # def all(self, cls=None):
    #     """query on the current database session"""
    #     new_dict = {}
    #     for clss in classes:
    #         if cls is None or cls is classes[clss] or cls is clss:
    #             objs = self.__session.query(classes[clss]).all()
    #             for obj in objs:
    #                 key = obj.__class__.__name__ + '.' + obj.id
    #                 new_dict[key] = obj
    #     return (new_dict)


    def new(self, obj):
        """Adds this object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Saves and applies all current db session changes"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Creates all tables defined in the database schema, and starts a database
        session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False
        )
        Session = scoped_session(session_factory)
        self.__session = Session
