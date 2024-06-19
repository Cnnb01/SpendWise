#!/usr/bin/env python3

"""Represents a category that any item can belong to"""

from sqlalchemy import Column, Integer, String
from base_model import Base


class Category(Base):
    """Represents a category that any item can belong to"""

    __tablename__ = 'categories'

    categoryId = Column(Integer, nullable=False, primary_key=True)
    categoryName = Column(String(60), nullable=False, primary_key=True)
