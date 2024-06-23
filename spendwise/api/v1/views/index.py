#!/usr/bin/env python3
"index"
from api.v1.views import app_views
from models.budget import Budget
from models.budget_category import BudgetCategory
from models.category import Category
from models.expense import Expense
from models.user import User
from models import storage #for the count method to be created
from flask import jsonify

@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ Status of API """
    return jsonify({"status": "OK"})

@app_views.routes('/stats', methods=['GET'], strict_slashes=False)
def number_objects():
    "retrieves number of each obj by type"
    classes = [Budget, BudgetCategory, Category, Expense, User]
    names = ["budgets", "budget_categories", "categories", "expenses", "users"]

    nums_objs = {}
    for i in range(len(classes)):
        nums_objs[names[i]] = storage.count(classes[i])

    return jsonify(nums_objs)