#!/usr/bin/env python3

"""Represents a category that any item can belong to"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from base_model import Base


class Category(Base):
    """Represents a category that any item can belong to"""

    __tablename__ = 'categories'

    categoryId = Column(Integer, nullable=False, primary_key=True)
    categoryName = Column(String(60), nullable=False, primary_key=True)

    # many-to-many relationship with Budget, via BudgetCategory junction table
    budgets = relationship(
        'Budget', secondary='budget_category', back_populates='categories'
    )
