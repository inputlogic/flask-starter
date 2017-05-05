from flask import render_template

from . import logger


log = logger.create(__name__)


def not_found(error):
    return render_template('errors/404.html'), 404


def server_error(error):
    return render_template('errors/500.html'), 500


def unhandled_exception(e):
    log.exception(e)
    return server_error(str(e))
