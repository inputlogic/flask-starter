"""
Imports all modules based on the current `FLASK_ENV` environment variable.

This is typically used with Flask:

    app = Flask(__name__)
    app.config.from_object('config')

You can also use the configs directly (in Celery for example) via regular import.

    import configs

"""
from importlib import import_module
import os


ENV = os.environ.get('FLASK_ENV', 'local')


from .common import *

if ENV == 'production':
    from .production import *
elif ENV == 'local':
    from .local import *
