#!/usr/bin/env python3
"""Handles APIs for budgets"""

from flask import Blueprint, jsonify, abort, request, make_response
from flask import session as flask_session
from ...models import storage
from ...models.budget import Budget
# from .decorators import requires_logged_in_user
from ...models.category import Category
from ...models.budget_category import BudgetCategory
from .decorators import requires_logged_in_user
from . import apis

@apis.route('/budgets/<Id>/categories', methods=['GET'])
def get_budget_categories(Id):
    budget = storage.get(Budget, Id)
    if not budget:
        abort(404)
    test_categories = [
        category.to_dict() for category in budget.categories
    ]

    print(test_categories)
    categories = [
            {
            'category_id': category.categoryId,
            'amount_budgeted': category.amountBudgeted}
            for category in budget.categories
        ]

    return jsonify({
        'budgetTitle': budget.budgetTitle,
        'categories': categories
    })

@apis.route('/budgets/add', methods=['POST'], strict_slashes=False)
@requires_logged_in_user
def add_budget():
    data = request.get_json()
    if (
        'categories' not in data
        or 'budgetTitle' not in data
        # or 'amountPredicted' not in data
    ):
        abort(400, description="Missing required fields")
    budget_title = data['budgetTitle']
    user_id = flask_session.get('current_user_id')
    

    # sum all amounts across all categories in the budget
    amount_predicted = sum(
        int(item['amountBudgeted'])
        for item in data['categories']
    )

    item_name = data['categories'][0].get('itemName', 'No item name')

    # Create a new budget
    new_budget = Budget(
        userId=user_id,
        budgetTitle=budget_title,
        amountPredicted=amount_predicted
        )
    storage.new(new_budget)
    storage.save()

    # get all categories present in the db
    # fetch all existing categories and their ids
    categories = {
        category.categoryName.lower(): category.Id
        for category in storage.session.query(Category).all()
        }

    # Create entries in the junction table
    for category_data in data['categories']:
        category_name = category_data['categoryName'].lower()
        amount_budgeted = category_data['amountBudgeted']

        # Create this category if it does not exist
        if category_name not in categories:
            category = Category(categoryName=category_name)
            storage.new(category)
            storage.save()
            categories.update({category.categoryName: category.Id}) # update categories dict with the new category
        # Create an entry in the junction table
        budget_category = BudgetCategory(
            budgetId=new_budget.Id,
            categoryId=category.Id,
            amountBudgeted=amount_budgeted,
            itemName=item_name)

        storage.new(budget_category)

    storage.save()
    return make_response(jsonify(new_budget.to_dict()), 201)


@apis.route('/budgets/get', methods=['GET'], strict_slashes=False)
@requires_logged_in_user
def get_budgets():
    budgets = storage.all(Budget).values()
    budgets_list = [budget.to_dict() for budget in budgets]
    return jsonify(budgets_list)


@apis.route('/budgets/update/<Id>', methods=['PUT'], strict_slashes=False)
@requires_logged_in_user
def update_budget(Id):
    budget = storage.get(Budget, Id)
    if not budget:
        abort(404)
    if not request.get_json():
        abort(400, description="Not a JSON")
    data = request.get_json()
    for k, v in data.items():
        if k != 'Id':
            setattr(budget, k, v)
    storage.save()
    return make_response(jsonify(budget.to_dict()), 200)


@apis.route('/budgets/delete/<Id>', methods=['DELETE'], strict_slashes=False)
@requires_logged_in_user
def delete_budget(Id):
    budget = storage.get(Budget, Id)
    if not budget:
        abort(404)
    storage.delete(budget)
    storage.save()
    return make_response(jsonify({}), 200)


# commands i used to test out the APIs, you have to have a user and a category and the budget in the db
# curl -X GET http://localhost:5000/api/v1/budgets
# curl -X GET "http://localhost:5000/api/v1/budgets/1/categories"
# curl -X PUT http://localhost:5000/api/v1/budgets/1 -H "Content-Type: application/json" -d '{"amountSpent": 200.00}'
# curl -X POST http://localhost:5000/api/v1/budgets -H "Content-Type: application/json" -d '{"userId": 1, "categoryId": 2, "budgetTitle": "Wedding", "amountPredicted": 500.00}'
# curl -X POST http://localhost:5000/api/v1/budgets -H "Content-Type: application/json" -d '{"userId": 1, "budgetTitle": "Wedding", "amountPredicted": 500.00}'
# curl -X DELETE http://localhost:5000/api/v1/budgets/1
