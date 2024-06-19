#!/usr/bin/env python3

"""Starts the database, and defines possible database actions"""

import os
from sqlalchemy import create_engine, MetaData
from models.base_model import Base
from models.budget import Budget
from models.category import Category
from models.expense import Expense
from models.user import User


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
            Base.metadata.dropall(bind=self.__engine)

    def reload(self):
        """Creates all tables defined in the database schema, and starts a database
        session"""
        Base.metadata.create_all(self.__engine)
