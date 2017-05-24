# Sets up the Flask Debug Toolbar extension
import config

from .. import app


if config.ENV == config.LOCAL:
    from flask_debugtoolbar import DebugToolbarExtension
    DebugToolbarExtension(app())
