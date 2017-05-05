# Log format used by `app.logger` module
LOG_FORMAT = '%(message)s [%(pathname)s:%(lineno)d]'

# Models to be loaded, in the order specified
MODELS = ['user', 'post', 'comment']

# View blueprints to be loaded, in the order specified
BLUEPRINTS = ['main', 'user', 'admin']
