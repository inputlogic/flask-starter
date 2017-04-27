import logging


DEBUG = True
LOG_LEVEL = logging.DEBUG
SECRET_KEY = 'local'

SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:@localhost/app'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_ECHO = False
