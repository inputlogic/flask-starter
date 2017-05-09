# Log format used by `app.logger` module
LOG_FORMAT = '%(message)s [%(pathname)s:%(lineno)d]'

# Models to be loaded, in the order specified
MODELS = ('user', 'post')

# View blueprints to be loaded, in the order specified
# See `load_blueprints` in `app/__init__.py` for more details
BLUEPRINTS = ('main', 'user', {'name': 'admin', 'url_prefix': '/admin'})
