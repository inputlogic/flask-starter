# flake8: noqa
import logging

from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config


app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

log = logging.getLogger(__name__)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(logging.Formatter(config.LOG_FORMAT))
log.addHandler(stream_handler)
log.setLevel(config.LOG_LEVEL)
log.info('Running in "{0}" environment'.format(config.ENV))

if app.debug:
    DebugToolbarExtension(app)


from . import filters
from . import errors

from .models import *
from .views import *

from . import auth
