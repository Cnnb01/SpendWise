#!/usr/bin/env python3

from sqlalchemy import Column, ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import relationship
from .base_model import Base

class BudgetCategory(Base):
    """Junction table for budgets and categories"""

    __tablename__ = 'budget_categories'

    Id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    budgetId = Column(Integer, ForeignKey('budgets.Id'), nullable=False)
    categoryId = Column(Integer, ForeignKey('categories.Id'), nullable=False)
    amountBudgeted = Column(Numeric(10, 2), nullable=False)
    itemName = Column(String(60), nullable=False)

    budget = relationship('Budget', back_populates='categories')
    category = relationship('Category')

    def to_dict(self):
        return {
            'category_name': self.categoryId,
            'amount_budgeted': self.amountBudgeted,
            'item_name': self.itemName
        }
