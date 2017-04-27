from flask import render_template

from . import app, log


@app.errorhandler(404)
def not_found(error):
    return render_template('errors/404.html'), 404


@app.errorhandler(500)
def server_error(error):
    return render_template('errors/500.html'), 500


if not app.debug:
    """
    Only render exceptions as 500 when not in local debug mode. This would otherwise the
    Flask debug output.

    """
    @app.errorhandler(Exception)
    def unhandled_exception(e):
        log.exception(e)
        return server_error(str(e))
