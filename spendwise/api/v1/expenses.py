#!/usr/bin/env python3
"Handles APIs for expenses"

from flask import Blueprint, jsonify, abort, request, make_response
from ...models import storage
from ...models.expense import Expense
from ...models.category import Category
from . import apis


@apis.route('/expenses/get', methods=['GET'], strict_slashes=False)
def get_expenses():
    expenses = storage.all(Expense)
    # add the category name to the dictionary representation of an expense before returning to the frontend
    cleaned_expenses = []
    for obj in expenses.values():
        obj_dict = obj.to_dict()
        obj_dict.update({
            'categoryName': storage.session.query(Category).filter_by(Id = (obj.categoryId)).one().categoryName
            })
        # remove the category id from the expense
        if 'categoryId' in obj_dict:
            del obj_dict['categoryId']
        cleaned_expenses.append(obj_dict)
    print(cleaned_expenses)
    return jsonify(cleaned_expenses)

@apis.route('/expenses/add', methods=['POST'], strict_slashes=False)
def add_expense():
    if not request.get_json():
        abort(400, description="Not a JSON")
    data = request.get_json()
    if 'entries' not in data or not isinstance(data['entries'], list):
        abort(400, description="Missing required fields or invalid format")

    expense_entries = data['entries']
    if not expense_entries:
        abort(400, description="No expense entries provided")

    # fetch all existing categories and their ids
    categories = {
        category.categoryName.lower(): category.Id
        for category in storage.session.query(Category).all()
        }
    new_expenses = []
    for entry in expense_entries:
        if (
            'category' not in entry
            or 'amount' not in entry
            or 'item' not in entry
        ):
            abort(400, description="Missing required fields in one of the entries")

        # add this user category to the database if it does not exist
        category_name = entry.get('category').lower()
        if category_name not in categories:
            category = Category(categoryName=category_name)
            storage.new(category)
            storage.save()
            categories.update({category.categoryName: category.Id}) # update categories dict with the new category

        new_expense = Expense(
            userId=1,  # Replace with actual user ID if needed #DEBUG
            categoryId=categories[category_name],
            expenseAmount=entry['amount'],
            itemName=entry['item']  # Assuming you have this field in your Expense model
        )

        storage.new(new_expense)
        new_expenses.append(new_expense)

    storage.save()
    return make_response(jsonify([expense.to_dict() for expense in new_expenses]), 201)



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
