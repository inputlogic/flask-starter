from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, Email


class UserForm(FlaskForm):
    first_name = StringField('first_name')
    last_name = StringField('last_name')
    email = StringField(
        'email', validators=(DataRequired(), Email()))
    password = PasswordField(
        'password', validators=(DataRequired(), Length(min=6)))
