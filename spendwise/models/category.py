#!/usr/bin/env python3

"""Represents a category that any item can belong to"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base_model import Base
from .budget_category import BudgetCategory


class Category(Base):
    """Represents a category that any item can belong to"""

    __tablename__ = 'categories'

    Id = Column(Integer, nullable=False, primary_key=True)
    categoryName = Column(String(60), nullable=False)

    # relationship with BudgetCategory
    budget_categories = relationship('BudgetCategory', back_populates='category')

    def to_dict(self):  # converts category obj to a dictionary
        return {
            'categoryId': self.Id,
            'categoryName': self.categoryName,
        }
