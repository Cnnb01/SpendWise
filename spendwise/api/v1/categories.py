#!/usr/bin/env python3
"Handles APIs for categories"

from flask import Blueprint, jsonify, abort, request, make_response
from ...models import storage
from ...models.category import Category

apis = Blueprint('apis', __name__)


@apis.route('/categories', methods=['GET'], strict_slashes=False)
def get_categories():
    categories = storage.all(Category).values()
    categories_list = [category.to_dict() for category in categories]
    return jsonify(categories_list)


@apis.route('/categories', methods=['POST'], strict_slashes=False)
def add_category():
    if not request.get_json():
        abort(400, description="Not a JSON")
    data = request.get_json()
    if 'categoryName' not in data:
        abort(400, description="Missing categoryName")
    new_category = Category(categoryName=data['categoryName'])
    storage.new(new_category)
    storage.save()
    return make_response(jsonify(new_category.to_dict()), 201)


@apis.route(
    '/categories/<categoryId>', methods=['PUT'], strict_slashes=False
)
def update_category(categoryId):
    category = storage.get(Category, categoryId)
    if not category:
        abort(404)
    if not request.get_json():
        abort(400, description="Not a JSON")
    data = request.get_json()
    for k, v in data.items():
        if k != 'categoryId':
            setattr(category, k, v)
    storage.save()
    return make_response(jsonify(category.to_dict()), 200)


# not sure we wanna delete a category, maybe an expense but thinking categories can just stay
# @apis.route('/categories/<categoryId>', methods=['DELETE'], strict_slashes=False)
# def delete_category(categoryId):
#     category = storage.get(Category, categoryId)
#     if not category:
#         abort(404)
#     storage.delete(category)
#     storage.save()
#     return make_response(jsonify({}), 200)

# commands i used to test out the APIs, you have to have a user and an expense in the db
# curl -X GET http://localhost:5000/api/v1/categories
# curl -X POST http://localhost:5000/api/v1/categories -H "Content-Type: application/json" -d '{"categoryName": "Groceries"}'
# curl -X PUT http://localhost:5000/api/v1/categories/1 -H "Content-Type: application/json" -d '{"categoryName": "Updated Category"}'
