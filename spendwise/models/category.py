#!/usr/bin/env python3

"""Represents a category that any item can belong to"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base_model import Base
from .junction_tables import budget_category_table


class Category(Base):
    """Represents a category that any item can belong to"""

    __tablename__ = 'categories'

    categoryId = Column(Integer, nullable=False, primary_key=True)
    categoryName = Column(String(60), nullable=False)

    # many-to-many relationship with Budget, via BudgetCategory junction table
    budgets = relationship(
        'Budget', secondary=budget_category_table, back_populates='categories'
    )

    def to_dict(self):#converts category obj to a dictionary
        return{
            'categoryId': self.categoryId,
            'categoryName': self.categoryName
        }
