#!/usr/bin/env python3

"""Represents a category that any item can belong to"""

from sqlalchemy import Column, Integer, String


class Category:
    """Represents a category that any item can belong to"""

    __tablename__ = 'categories'

    categoryId = Column(Integer, nullable=False)
    categoryName = Column(String(60), nullable=False)
