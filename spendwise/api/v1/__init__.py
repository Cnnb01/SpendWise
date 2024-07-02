#!/usr/bin/env python3

"""For version 1 of the spendwise api"""

from flask import Blueprint

# define the blueprint to be used in all api files
apis = Blueprint('apis', __name__)

# make sure these modules are registered later
from . import auth, budgets, categories, expenses
