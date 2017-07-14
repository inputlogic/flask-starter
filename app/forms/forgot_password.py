from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email


class ForgotPasswordForm(FlaskForm):
    email = StringField(
        'Email', validators=(DataRequired(), Email()))


class ResetPasswordForm(FlaskForm):
    new_password = PasswordField('New Password')
