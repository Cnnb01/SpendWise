#!/usr/bin/env python3
"Handles APIs for expenses"

from flask import Blueprint, jsonify, abort, request, make_response
from ...models import storage
from ...models.expense import Expense
from . import apis


@apis.route('/expenses', methods=['GET'], strict_slashes=False)
def get_expenses():
    expenses = storage.all(Expense)
    cleaned_expenses = [obj.to_dict() for obj in expenses.values()]
    return jsonify(cleaned_expenses)


@apis.route('/expenses', methods=['POST'], strict_slashes=False)
def add_expense():
    if not request.get_json():
        abort(400, description="Not a JSON")
    data = request.get_json()
    if (
        'userId' not in data
        or 'categoryId' not in data
        or 'expenseAmount' not in data
    ):
        abort(400, description="Missing required fields")

    expense = Expense(
        userId=data['userId'],
        categoryId=data['categoryId'],
        expenseAmount=data['expenseAmount'],
    )
    storage.new(expense)
    storage.save()
    return make_response(jsonify(expense.to_dict()), 201)


@apis.route('/expenses/<expenseId>', methods=['PUT'], strict_slashes=False)
def update_expense(expenseId):
    expense = storage.get(Expense, expenseId)
    if not expense:
        abort(404)
    if not request.get_json():
        abort(400, description="Not a JSON")
    data = request.get_json()
    for k, v in data.items():
        if k != 'expenseId':
            setattr(expense, k, v)
    storage.save()
    return make_response(jsonify(expense.to_dict()), 200)


@apis.route('/expenses/<expenseId>', methods=['DELETE'], strict_slashes=False)
def delete_expense(expenseId):
    expense = storage.get(Expense, expenseId)
    if not expense:
        abort(404)
    storage.delete(expense)
    storage.save()
    return make_response(jsonify({}), 200)


# commands i used to test out the APIs, you have to have a user and an expense in the db
# curl -X GET http://localhost:5000/api/v1/expenses
# curl -X PUT http://localhost:5000/api/v1/expenses/1 -H "Content-Type: application/json" -d '{"expenseAmount": 150.00, "categoryId": 3}'
# curl -X POST http://localhost:5000/api/v1/expenses -H "Content-Type: application/json" -d '{"userId": 1, "categoryId": 1, "expenseAmount": 100.00}'
# curl -X DELETE http://localhost:5000/api/v1/expenses/1
