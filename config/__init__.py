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


LOCAL = 'local'
PRODUCTION = 'production'
ENV = os.environ.get('FLASK_ENV', LOCAL)


from .common import *

if ENV == PRODUCTION:
    from .production import *
elif ENV == LOCAL:
    from .local import *
