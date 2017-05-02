import logging


DEBUG = True
LOG_LEVEL = logging.DEBUG
SECRET_KEY = 'local'

DEBUG_TB_INTERCEPT_REDIRECTS = False

MONGODB_SETTINGS = {
    'db': 'app',
    'host': 'localhost',
    'port': 27017
}
