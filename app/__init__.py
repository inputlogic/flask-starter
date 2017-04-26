from flask import Flask, render_template

import config
from . import logger


name = 'app'
app = Flask(name)
app.config.from_object(config)

log = logger.get(name, config.LOG_LEVEL)
log.info('Running in "{0}" environment'.format(config.ENV))


from . import filters
from . import views
