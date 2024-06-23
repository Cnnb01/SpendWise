#!/usr/bin/env python3
"handels APIs for expenses"
# from api.v1.views import app_views
from flask import Flask, Blueprint, jsonify, abort, request, make_response
from ...models import storage
from ...models.expense import Expense


app_views = Blueprint('app_views', __name__)


@app_views.route('/expenses', methods=['GET'], strict_slashes=False)
def get_expenses():
    expenses = storage.all(Expense)
    return jsonify([a.to_dict() for a in expenses.values()])


# def get_expense():


@app_views.route(
    '/expenses/<expenseId>', methods=['POST'], strict_slashes=False
)
def add_expense():
    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'name' not in request.get_json():
        abort(400, description="Missiong name")
    expense = Expense(name=request.get_json()['name'])
    storage.new(expense)
    storage.save()
    return make_response(jsonify(expense.to_dict()), 201)


@app_views.route(
'/expenses/<expenseId>', methods=['PUT'], strict_slashes=False
)
def update_expense(expenseId):
    expense = storage.get(Expense, expenseId)
    if expense is None:
        abort(404)
    if not request.get_json():
        abort(400, description="Not a JSON")
    data = request.get_json()
    for k, v in data.items():
        if k != 'id':
            setattr(expense, k, v)
    storage.save()
    return make_response(jsonify(expense.to_dict()), 200)
    # incomplete


# @app_views
# def delete_expense(expenseId):
#     expense = storage.get(Expense, expenseId)
#     if expense is None:
#         abort(404)
#     storage.delete(expense)
#     storage.save()
#     return make_response(jsonify({}), 200)
