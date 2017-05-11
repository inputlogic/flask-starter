"""
Imports all modules based on the current `FLASK_ENV` environment variable.

"""
import os


LOCAL = 'local'
PRODUCTION = 'production'
TEST = 'test'

ENV = os.environ.get('FLASK_ENV', LOCAL)


from .common import *

if ENV == PRODUCTION:
    from .production import *
elif ENV == LOCAL:
    from .local import *
elif ENV == TEST:
    from .test import *
