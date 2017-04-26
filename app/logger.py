import logging
import config


def get(name, log_level):
    logger = logging.getLogger(name)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(logging.Formatter('%(message)s [in %(pathname)s:%(lineno)d]'))
    logger.addHandler(stream_handler)
    logger.setLevel(log_level)
    return logger
