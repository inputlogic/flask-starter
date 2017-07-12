from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField
from wtforms.validators import DataRequired, Length, Email


class AuthForm(FlaskForm):
    email = StringField(
        'Email', validators=(DataRequired(), Email()))
    password = PasswordField(
        'password', validators=(DataRequired(), Length(min=4)))


class UserForm(FlaskForm):
    first_name = StringField('First name', validators=(DataRequired(),))
    last_name = StringField('Last name', validators=(DataRequired(),))
    email = StringField(
        'Email', validators=(DataRequired(), Email()))
    password = PasswordField(
        'Password', validators=(DataRequired(), Length(min=4)))
    is_admin = BooleanField('Is admin?')
