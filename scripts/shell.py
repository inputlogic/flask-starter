import importlib
from app import create_app
import config

def camel_case(string):
    return ''.join([x.title() for x in string.split('_')])

def load_models():
    for name in config.MODELS:
        module = importlib.import_module('app.models.{0}'.format(name))
        model = camel_case(name)
        globals()[model] = getattr(module, model)

create_app()
load_models()
