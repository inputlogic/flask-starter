from flask_wtf import FlaskForm
from wtforms import (
    BooleanField,
    StringField,
    PasswordField,
    HiddenField
)
from wtforms.validators import DataRequired, Length, Email


class AuthForm(FlaskForm):
    email = StringField(
        'Email', validators=(DataRequired(), Email()))
    password = PasswordField(
        'password', validators=(DataRequired(), Length(min=4)))


class UserForm(FlaskForm):
    first_name = StringField('First name', validators=(DataRequired(),))
    last_name = StringField('Last name', validators=(DataRequired(),))
    avatar = HiddenField('Avatar')
    email = StringField(
        'Email', validators=(DataRequired(), Email()))
    is_admin = BooleanField('Is admin?')
