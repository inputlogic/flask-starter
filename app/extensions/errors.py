from flask import render_template

import config
from .. import create_logger


log = create_logger(__name__)


def setup(app):
    app.register_error_handler(404, not_found)
    app.register_error_handler(500, server_error)

    if config.ENV == config.PRODUCTION:
        app.register_error_handler(Exception, unhandled_exception)


def not_found(error):
    return render_template('errors/404.html'), 404


def server_error(error):
    return render_template('errors/500.html'), 500


def unhandled_exception(e):
    log.exception(e)
    return server_error(str(e))
