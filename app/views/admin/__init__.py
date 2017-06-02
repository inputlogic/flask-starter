# flake8: noqa
from flask import Blueprint


bp = None


if not bp:
    bp = Blueprint('admin', __name__)

    from . import auth
    from . import posts
    from . import users
