# Sets up the Flask Debug Toolbar extension
import config


def setup(app):
    if config.ENV == config.LOCAL:
        from flask_debugtoolbar import DebugToolbarExtension
        DebugToolbarExtension(app)
