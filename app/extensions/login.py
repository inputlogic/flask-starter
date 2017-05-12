from functools import wraps

from flask import request, redirect, url_for
from flask_login import LoginManager, current_user

from ..models.user import User


def setup(app):
    lm = LoginManager(app)
    lm.login_view = 'user.login'

    @lm.user_loader
    def load_user(user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None


def is_admin(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_admin:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function
