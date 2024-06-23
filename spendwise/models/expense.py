#!/usr/bin/env python3

"""Represents an expense"""

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Numeric
from datetime import datetime
from .base_model import Base


class Expense(Base):
    """Represents an expense"""

    __tablename__ = 'expenses'

    expenseId = Column(
        Integer, nullable=False, autoincrement=True, primary_key=True
    )
    userId = Column(Integer, ForeignKey('users.userId'), nullable=False)
    categoryId = Column(
        Integer, ForeignKey('categories.categoryId'), nullable=False
    )
    dateAdded = Column(DateTime, default=datetime.utcnow)
    expenseAmount = Column(Numeric(10, 2), nullable=False)

    def to_dict(self):#converts an Expense object to a dictionary for easy manipulation and JSON serialization.
        """Convert the Expense object to a dictionary"""
        return {
            'expenseId': self.expenseId,
            'userId': self.userId,
            'categoryId': self.categoryId,
            'dateAdded': self.dateAdded,
            'expenseAmount': str(self.expenseAmount)  # Convert Decimal to string
        }
