import importlib

from flask import Flask

import config
from . import logger


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    # Avoid repetitive logging when in test mode
    if not app.config['TESTING']:
        log = logger.create(__name__)
        log.info('Running in "{0}" environment'.format(config.ENV))

    load_models(app)
    load_blueprints(app)
    load_errorhandlers(app)
    load_utils(app)

    return app


def load_models(app):
    """
    Dynamicaly load models specified in the `MODELS` config tuple.

    """
    for name in config.MODELS:
        importlib.import_module('app.models.{0}'.format(name))


def load_blueprints(app):
    """
    Dynamicaly load view blueprints specified in the `BLUEPRINTS` config tuple.

    String values are assumed to be the name of a module to import. For more
    advanced Blueprint loading, you can specify a dict.

    Example:

        BLUEPRINTS = (
            'basic',
            {
                name: 'advanced',
                url_prefix: '/advanced'
            }
        )

    In the above example, the "basic" Blueprint will be loaded with no
    additional settings. The second example will load the "advanced" Blueprint
    with the `url_prefix` set to "/advanced".

    All `Blueprint` kwargs are supported in the advanced version.

    """
    for blueprint in config.BLUEPRINTS:
        if isinstance(blueprint, str):
            name = blueprint
            kwargs = {}
        else:
            name = blueprint.pop('name')
            kwargs = blueprint

        view = importlib.import_module('app.views.{0}'.format(name))
        app.register_blueprint(view.bp, **kwargs)


def load_errorhandlers(app):
    """
    Load view error handlers for 404, 500 and uncaught exceptions.

    """
    from .errors import not_found, server_error, unhandled_exception
    app.errorhandler(404)(not_found)
    app.errorhandler(500)(server_error)

    # Only hide exceptions in production
    if config.ENV == config.PRODUCTION:
        app.errorhandler(Exception)(unhandled_exception)


def load_utils(app):
    """
    Load misc utils and Flask extensions.

    """
    from .auth import lm
    lm.init_app(app)

    if config.ENV == config.LOCAL:
        from flask_debugtoolbar import DebugToolbarExtension
        DebugToolbarExtension(app)
