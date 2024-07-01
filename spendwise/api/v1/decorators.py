#!/usr/bin/env python3

"""For functions that will be used as decorators for other functions"""

from functools import wraps
from flask import session, redirect, url_for


def requires_logged_in_user(f):
    """Checks that a user is logged in, before executing a route function.
    Redirects the user to the login page, if they are not logged in.

    Ensures that the user cannot access pages even after logging out.
    """

    @wraps(f)
    def check_logged_status(*args, **kwargs):
        if 'current_user_id' not in session:
            return redirect(url_for('home'))
        # call the original function properly
        return f(*args, **kwargs)

    return check_logged_status
