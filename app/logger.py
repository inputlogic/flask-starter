import logging

import config


def create(name):
    """
    Creates a new log with the log format specified in config.

    Should be used over the Flask app logger for consitency and control between
    app contexts as well utils and worker queues (Celery).

    """
    log = logging.getLogger(name)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(logging.Formatter(config.LOG_FORMAT))
    log.addHandler(stream_handler)
    log.setLevel(config.LOG_LEVEL)
    return log
