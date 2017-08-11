import os
import logging


def get(key, default):
    """
    Used for getting default configs for dev but forces environment only configs in production.
    """
    value = os.environ.get(key)
    if not value and ENV == PRODUCTION:
        raise Exception('env config "{0}" is missing'.format(key))
    return value or default


# =============================================
# ENVIRONMENT SPECIFIC
#
# Don't put configs here unless they need some sort of logic or are
# unrelated to other envs. Prefer to use env vars with defaults using
# the `get` function.
# =============================================

LOCAL = 'local'
PRODUCTION = 'production'
TEST = 'test'
ENV = os.environ.get('FLASK_ENV', LOCAL)

# Environment specific
if ENV == LOCAL:
    LOG_LEVEL = logging.DEBUG
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    DEBUG_TB_PANELS = [
        'flask_debugtoolbar.panels.timer.TimerDebugPanel',
        'flask_debugtoolbar.panels.headers.HeaderDebugPanel',
        'flask_debugtoolbar.panels.request_vars.RequestVarsDebugPanel',
        'flask_debugtoolbar.panels.config_vars.ConfigVarsDebugPanel',
        'flask_debugtoolbar.panels.template.TemplateDebugPanel',
        'flask_mongoengine.panels.MongoDebugPanel',
        'flask_debugtoolbar.panels.route_list.RouteListDebugPanel',
        'flask_debugtoolbar.panels.profiler.ProfilerDebugPanel'
    ]

elif ENV == TEST:
    LOG_LEVEL = logging.DEBUG
    # https://github.com/jarus/flask-testing/issues/21
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    LIVESERVER_PORT = 1337

elif ENV == PRODUCTION:
    LOG_LEVEL = logging.WARN


# =============================================
# FLASK
# =============================================

DEBUG = True if ENV == LOCAL else False
SECRET_KEY = get('FLASK_SECRET_KEY', 'dev')

# Disable Flask logger
LOGGER_NAME = None
LOGGER_HANDLER_POLICY = 'never'

# Default log format used for `create_logger`
DEFAULT_LOG_FORMAT = '[%(asctime)s] %(levelname)s %(message)s (%(pathname)s:%(lineno)d)'

# Default log format used for request logs
REQUEST_LOG_FORMAT = '[%(asctime)s] %(message)s'

# Log HTTP status code and mimetype for responses
LOG_RESPONSE_STATUS = False

# A list of paths to ignore in requests log
# Will match anything that *starts with* the given string
LOG_REQUESTS_IGNORE = ('/_debug_toolbar',)


# =============================================
# APP
# =============================================

# Extensions (modules) to be loaded at run time and given an `app` instance
EXTENSIONS = ('errors', 'login')

# Models to be loaded, in the order specified
MODELS = ('user', 'post')

# View blueprints to be loaded, in the order specified
# See `load_blueprints` in `app/__init__.py` for more details
BLUEPRINTS = ('main', {'name': 'admin', 'url_prefix': '/admin'})

# MongoDB
MONGODB_SETTINGS = {
    'host': get('MONGODB_URI', 'mongodb://localhost:27017/flask-starter'),
    'connect': False # Lazy-load connections to avoid pre-fork issues
}


# =============================================
# 3RD PARTY
# =============================================

# Amazon S3
S3_KEY = get('S3_KEY', '')
S3_SECRET = get('S3_SECRET', '')
S3_BUCKET = get('S3_BUCKET', '')
S3_UPLOAD_DIRECTORY = get('S3_UPLOAD_DIRECTORY', '')
