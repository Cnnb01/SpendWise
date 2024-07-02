#!/usr/bin/env python3
"""Handles APIs for budgets"""

from flask import Blueprint, jsonify, abort, request, make_response, session
from ...models import storage
from ...models.budget import Budget
from .decorators import requires_logged_in_user
from . import apis


@apis.route('/budgets/add', methods=['POST'], strict_slashes=False)
@requires_logged_in_user
def add_budget():
    if not request.get_json():
        abort(400, description="Not a JSON")
    data = request.get_json()
    if (
        'categoryId' not in data
        or 'budgetTitle' not in data
        or 'amountPredicted' not in data
    ):
        abort(400, description="Missing required fields")
    new_budget = Budget(
        userId=session['current_user_id'],
        categoryId=data['categoryId'],
        budgetTitle=data['budgetTitle'],
        amountPredicted=data['amountPredicted'],
        amountSpent=data.get('amountSpent', None),
        balance=data.get('balance', None),
    )
    storage.new(new_budget)
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


@apis.route('/budgets/delete/Id>', methods=['DELETE'], strict_slashes=False)
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
# curl -X PUT http://localhost:5000/api/v1/budgets/1 -H "Content-Type: application/json" -d '{"amountSpent": 200.00}'
# curl -X POST http://localhost:5000/api/v1/budgets -H "Content-Type: application/json" -d '{"userId": 1, "categoryId": 2, "budgetTitle": "Wedding", "amountPredicted": 500.00}'
# curl -X DELETE http://localhost:5000/api/v1/budgets/1
