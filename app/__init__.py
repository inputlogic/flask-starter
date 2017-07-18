import importlib
import logging

from flask import Flask, request

import config


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    setup_logging(app)
    load_models(app)
    load_extensions(app)
    load_blueprints(app)

    return app


def create_logger(name, format=None):
    log = logging.getLogger(name)
    log.setLevel(config.LOG_LEVEL)
    log.propagate = False

    log_format = format or config.DEFAULT_LOG_FORMAT
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(logging.Formatter(log_format))
    log.addHandler(stream_handler)

    return log


def setup_logging(app):
    # Quite down Flask/Werkzeug
    logging.getLogger('werkzeug').disabled = True
    app.logger.disabled = True

    # Avoid repetitive logging when in test mode
    if not app.config['TESTING']:
        log = create_logger(__name__, format=config.REQUEST_LOG_FORMAT)
        log.info('Running in "{0}" environment'.format(config.ENV))

        # Log our own HTTP requests
        @app.before_request
        def log_request():
            for i in config.LOG_REQUESTS_IGNORE:
                if request.path.startswith(i):
                    return
            log.info('{0} {1}'.format(request.method, request.path))

        if config.LOG_RESPONSE_STATUS:
            @app.after_request
            def log_response(response):
                log.info('{0} ({1})'.format(
                    response.status,
                    response.mimetype))
                return response


def load_extensions(app):
    """
    Dynamicaly load "extensions" specified in the `EXTENSIONS` config tuple.

    An extension doesn't have to be a Flask specific extension. Its basically
    any module that needs to be loaded at run time and given an `app` instance
    via a `setup` function.

    """
    for name in config.EXTENSIONS:
        module = importlib.import_module('app.extensions.{0}'.format(name))
        if hasattr(module, 'setup'):
            module.setup(app)


def load_models(app):
    """
    Dynamicaly load models specified in the `MODELS` config tuple.

    """
    from .models import db
    db.init_app(app)

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
            args = blueprint.copy()
            name = args.pop('name')
            kwargs = args

        view = importlib.import_module('app.views.{0}'.format(name))
        app.register_blueprint(view.bp, **kwargs)
