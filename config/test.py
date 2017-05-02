import logging


TESTING = True
LIVESERVER_PORT = 1337

DEBUG = True
LOG_LEVEL = logging.DEBUG
SECRET_KEY = 'test'

# https://github.com/jarus/flask-testing/issues/21
PRESERVE_CONTEXT_ON_EXCEPTION = False

MONGODB_SETTINGS = {
    'db': 'app_test',
    'host': 'localhost',
    'port': 27017
}
