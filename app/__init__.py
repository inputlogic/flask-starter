# flake8: noqa
import logging

from flask import Flask
from flask_mongoengine import MongoEngine

import config


app = Flask(__name__)
app.config.from_object(config)

db = MongoEngine(app)

log = logging.getLogger(__name__)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(logging.Formatter(config.LOG_FORMAT))
log.addHandler(stream_handler)
log.setLevel(config.LOG_LEVEL)
log.info('Running in "{0}" environment'.format(config.ENV))

if config.ENV == config.LOCAL:
    from flask_debugtoolbar import DebugToolbarExtension
    DebugToolbarExtension(app)


from . import auth
from . import errors
from . import filters

from .models import *
from .views import *
