from flask_login import LoginManager

from .models import user as user_model


lm = LoginManager()
lm.login_view = 'user.login'


@lm.user_loader
def load_user(user_id):
    return user_model.get_by_id(user_id)
