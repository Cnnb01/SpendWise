from sqlalchemy import Column, ForeignKey, Integer, Numeric
from sqlalchemy.orm import relationship
from .base_model import Base

class BudgetCategory(Base):
    """Junction table for budgets and categories"""

    __tablename__ = 'budget_categories'

    budgetId = Column(Integer, ForeignKey('budgets.Id'), primary_key=True)
    categoryId = Column(Integer, ForeignKey('categories.Id'), primary_key=True)
    amountBudgeted = Column(Numeric(10, 2), nullable=False)
    
    budget = relationship('Budget', back_populates='categories')
    category = relationship('Category')

    def to_dict(self):
        return {
            'category_name': self.categoryId,
            'amount_budgeted': self.amountBudgeted
        }
