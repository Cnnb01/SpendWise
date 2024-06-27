#!/usr/bin/python3

"""Represents the junction table to break up the many-to-many relationship
between Budget and Category table"""

from .base_model import Base
from sqlalchemy import Column, ForeignKey, Integer, PrimaryKeyConstraint, Table


budget_category_table = Table(
    'budget_category',
    Base.metadata,
    Column('budgetId', ForeignKey('budgets.Id'), primary_key=True),
    Column('categoryId', ForeignKey('categories.Id'), primary_key=True),
)
