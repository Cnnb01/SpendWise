#!/usr/bin/env python3

"""Represents an expense"""

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Numeric
from datetime import datetime
from base_model import Base

class Expense(Base):
    """Represents an expense"""

    __tablename__ = 'expenses'

    expenseId = Column(Integer, nullable=False, autoincrement=True)
    userId = Column(Integer, ForeignKey('users.userId'), nullable=False)
    categoryId = Column(
        Integer, ForeignKey('categories.categoryId'), nullable=False
    )
    dateAdded = Column(DateTime, default=datetime.utcnow)
    expenseAmount = Column(Numeric(10, 2), nullable=False)
