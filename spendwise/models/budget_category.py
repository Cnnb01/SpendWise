#!/usr/bin/python3

"""Represents the junction table to break up the many-to-many relationship
between Budget and Category table"""

from base_model import Base
from sqlalchemy import Column, ForeignKey, Integer


class BudgetCategory(Base):
    """Represents a junction table between Budget and Category"""

    __tablename__ = 'budget_category'

    budgetId = Column(Integer, ForeignKey('budgets.budgetId'))
    categoryId = Column(Integer, ForeignKey('categories.categoryId'))
