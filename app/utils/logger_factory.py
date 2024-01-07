import logging
from logging.handlers import RotatingFileHandler
import os

def configure_logger(name):
    """
    Create and configure a logger with the given name.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)   #set the logging level

    #create a file handler which logs even debug messages
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/flask_app.log', maxBytes=10240, backupCount=10)

    #create a logging format
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger