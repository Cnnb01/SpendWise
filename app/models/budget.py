#!/usr/bin/env python3

"""Represents a budget created by a user"""

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Numeric
from datetime import datetime
from base_model import Base


class Budget(Base):
    """Represents a budget created by a user"""

    __tablename__ = 'budgets'

    expenseId = Column(Integer, nullable=False)
    categoryId = Column(
        Integer, ForeignKey('categories.categoryId'), nullable=False
    )
    userId = Column(Integer, ForeignKey('users.userId'))
    dateAdded = Column(DateTime, default=datetime.utcnow)
    expenseAmount = Column(Numeric(10, 2))
