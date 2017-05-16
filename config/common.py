# Disable Flask logger
LOGGER_NAME = None
LOGGER_HANDLER_POLICY = 'never'

# Default log format used for `create_logger`
DEFAULT_LOG_FORMAT = '[%(asctime)s] %(levelname)s %(message)s (%(pathname)s:%(lineno)d)'

# Default log format used for request logs
REQUEST_LOG_FORMAT = '[%(asctime)s] %(message)s'

# Log status code and mimetype of responses
LOG_RESPONSE_STATUS = False

# A list of paths to ignore in requests log
# Will match anything that *starts with* the given string
LOG_REQUESTS_IGNORE = ('/_debug_toolbar',)

# Extensions (modules) to be loaded at run time and given an `app` instance
EXTENSIONS = ('debugtoolbar', 'errors', 'filters', 'login', 'overlord')

# Models to be loaded, in the order specified
MODELS = ('user', 'post')

# View blueprints to be loaded, in the order specified
# See `load_blueprints` in `app/__init__.py` for more details
BLUEPRINTS = ('main', 'user')
