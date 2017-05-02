from flask_login import LoginManager

from . import app
from .models.user import User


lm = LoginManager(app)
lm.init_app(app)
lm.login_view = 'login'


@lm.user_loader
def load_user(user_id):
    return User.objects.get(user_id)
