# flake8: noqa
from flask import Blueprint


bp = None


if not bp:
    bp = Blueprint('main', __name__)

    from . import main
