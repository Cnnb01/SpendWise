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

    def new(self, obj):
        """Adds this object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Saves and applies all current db session changes"""
        self.__session.commit()

    def reload(self):
        """Creates all tables defined in the database schema, and starts a database
        session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False
        )
        Session = scoped_session(session_factory)
        self.__session = Session
