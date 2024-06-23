#!/usr/bin/env python3
"Handles APIs for expenses"

from flask import Blueprint, jsonify, abort, request, make_response
from ...models import storage
from ...models.expense import Expense

app_views = Blueprint('app_views', __name__)

@app_views.route('/expenses', methods=['GET'], strict_slashes=False)
def get_expenses():
    expenses = storage.all(Expense)
    cleaned_expenses = [obj.to_dict() for obj in expenses.values()]
    return jsonify(cleaned_expenses)

@app_views.route('/expenses', methods=['POST'], strict_slashes=False)
def add_expense():
    if not request.get_json():
        abort(400, description="Not a JSON")
    data = request.get_json()
    if 'userId' not in data or 'categoryId' not in data or 'expenseAmount' not in data:
        abort(400, description="Missing required fields")
    
    expense = Expense(
        userId=data['userId'],
        categoryId=data['categoryId'],
        expenseAmount=data['expenseAmount']
    )
    storage.new(expense)
    storage.save()
    return make_response(jsonify(expense.to_dict()), 201)

@app_views.route('/expenses/<expenseId>', methods=['PUT'], strict_slashes=False)
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

@app_views.route('/expenses/<expenseId>', methods=['DELETE'], strict_slashes=False)
def delete_expense(expenseId):
    expense = storage.get(Expense, expenseId)
    if not expense:
        abort(404)
    storage.delete(expense)
    storage.save()
    return make_response(jsonify({}), 200)
