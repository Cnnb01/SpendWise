#!/usr/bin/env python3

"""Represents an expense"""

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Numeric
from datetime import datetime
from .base_model import Base


class Expense(Base):
    """Represents an expense"""

    __tablename__ = 'expenses'

    Id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    userId = Column(Integer, ForeignKey('users.Id'), nullable=False)
    categoryId = Column(Integer, ForeignKey('categories.Id'), nullable=False)
    dateAdded = Column(DateTime, default=datetime.utcnow)
    expenseAmount = Column(Numeric(10, 2), nullable=False)
    itemName = Column(String(128), nullable=False)

    def to_dict(
        self,
    ):  # converts an Expense object to a dictionary for easy manipulation and JSON serialization.
        """Convert the Expense object to a dictionary"""
        return {
            'Id': self.Id,
            'userId': self.userId,
            'categoryId': self.categoryId,
            'dateAdded': self.dateAdded,
            'expenseAmount': str(
                self.expenseAmount
            ),  # Convert Decimal to string
            'itemName': self.itemName
        }
