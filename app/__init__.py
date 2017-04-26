from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension

import config
from . import logger


name = 'app'
app = Flask(name)
app.config.from_object(config)

log = logger.get(name, config.LOG_LEVEL)
log.info('Running in "{0}" environment'.format(config.ENV))

if app.debug:
    toolbar = DebugToolbarExtension(app)


from . import filters
from . import views
