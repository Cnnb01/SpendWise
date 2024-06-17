#!/usr/bin/env python3

"""Represents a user of the application"""

from sqlalchemy import Column, Integer, String


class User:
    """A user of the application"""

    __tablename__ = 'users'

    userId = Column(Integer, nullable=False, autoincrement=True)
    lastName = Column(String(150), nullable=False)
    firstName = Column(String(150), nullable=False)
