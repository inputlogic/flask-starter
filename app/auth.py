from flask_login import LoginManager

from .models.user import User


lm = LoginManager()
lm.login_view = 'user.login'


@lm.user_loader
def load_user(user_id):
    return User.objects.get(pk=user_id)
