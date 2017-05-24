from flask_overlord import admin

from .. import app
from ..models import db
from ..models.user import User
from ..models.post import Post


admin.init_app(app(), db)
admin.add_model(User)
admin.add_model(Post)


@admin.authenticate()
def auth_admin():
    return True
