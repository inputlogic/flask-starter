from getpass import getpass

import config

from app import create_app
from app.models.user import User


# App needs to be setup before we can use db
create_app()

email = input('email: ')
password = getpass('password: ')

User.register(email=email, password=password, is_admin=True)
print('Super user created')
