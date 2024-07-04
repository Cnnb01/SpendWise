#!/usr/bin/env python3

"""Represents a budget created by a user"""

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Numeric
from sqlalchemy.orm import relationship
from datetime import datetime
from .base_model import Base


class Budget(Base):
    """Represents a budget created by a user"""

    __tablename__ = 'budgets'

    Id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    userId = Column(Integer, ForeignKey('users.Id'), nullable=False)
    budgetTitle = Column(String(60), nullable=False)
    dateCreated = Column(DateTime, default=datetime.utcnow)
    amountPredicted = Column(Numeric(10, 2), nullable=False)
    amountSpent = Column(Numeric(10, 2), nullable=True, default=0)
    balance = Column(
        Numeric(10, 2), nullable=True, default=0
    )  # balance should be amountPredicted - amountSpent

    # relationship with BudgetCategory
    categories = relationship('BudgetCategory', back_populates='budget')

    # one-to-many relationship with User
    user = relationship('User', back_populates='budgets')

    def to_dict(self):
        return {
            'Id': self.Id,
            'userId': self.userId,
            'budgetTitle': self.budgetTitle,
            'dateCreated': self.dateCreated.strftime('%Y-%m-%d %H:%M:%S'),
            'amountPredicted': float(self.amountPredicted),
            'amountSpent': (
                (
                    float(self.amountSpent)
                    if self.amountSpent is not None
                    else 0.0
                ),
            ),
            'balance': (
                float(self.balance) if self.balance is not None else 0.0,
            ),
            # Add other fields as needed
        }
