from flask_overlord import admin

from ..models import db
from ..models.user import User
from ..models.post import Post


def setup(app):
    admin.init_app(app, db)
    admin.add_model(User)
    admin.add_model(Post)
    admin.add_auth_handler(app, auth_admin)


def auth_admin():
    return True
