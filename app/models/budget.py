#!/usr/bin/env python3

"""Represents a budget created by a user"""

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Numeric
from sqlalchemy.orm import relationship
from datetime import datetime
from base_model import Base


class Budget(Base):
    """Represents a budget created by a user"""

    __tablename__ = 'budgets'

    budgetId = Column(
        Integer, nullable=False, autoincrement=True, primary_key=True
    )
    categoryId = Column(
        Integer, ForeignKey('categories.categoryId'), nullable=False
    )
    userId = Column(Integer, ForeignKey('users.userId'), nullable=False)
    budgetTitle = Column(String(60), nullable=False)
    dateCreated = Column(DateTime, default=datetime.utcnow)
    amountPredicted = Column(Numeric(10, 2), nullable=False)
    amountSpent = Column(Numeric(10, 2), nullable=True)
    balance = Column(Numeric(10, 2), nullable=True)

    # many-to-many relationship with Category, via BudgetCategory junction table
    categories = relationship(
        'Category', secondary='budget_category', back_populates='budgets'
    )
    # one-to-many relationship with User
    user = relationship('User', back_populates='budgets')
