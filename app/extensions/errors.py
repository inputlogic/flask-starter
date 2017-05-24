from flask import render_template

import config
from .. import app, create_logger


handler = app()
log = create_logger(__name__)


@handler.errorhandler(404)
def not_found(error):
    return render_template('errors/404.html'), 404


@handler.errorhandler(500)
def server_error(error):
    return render_template('errors/500.html'), 500


if config.ENV == config.PRODUCTION:
    @handler.errorhandler(Exception)
    def unhandled_exception(e):
        log.exception(e)
        return server_error(str(e))
