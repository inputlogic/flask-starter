import logging
import os


DEBUG = False
LOG_LEVEL = logging.INFO
SECRET_KEY = os.environ.get('FLASK_SECRET_KEY')

SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
SQLALCHEMY_TRACK_MODIFICATIONS = False
