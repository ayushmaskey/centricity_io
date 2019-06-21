"""Central logging for whole app."""

import logging
from datetime import datetime
from file_directory_exists import dir_exists
import os


def config_logging():
    """Test."""
    # Custom Logger
    logger = logging.getLogger(__name__)

    # create log file and folder
    dir_path = os.getcwd() + "\\log\\"
    dir_exists(dir_path)
    filename = __name__ + '_' + datetime.now().strftime('%Y-%m-%d') + '.log'
    file_path = dir_path + filename

    # Handlers
    file_handler = logging.FileHandler(file_path)
    logging.getLogger().setLevel(logging.DEBUG)

    # Log Format
    format = '%(asctime)s - (%(name)s) %(levelname)s: %(message)s '
    log_format = logging.Formatter(format)
    file_handler.setFormatter(log_format)

    # Add handler to Logger
    logger.addHandler(file_handler)

    logger.debug('This is warning from config_logging function')

    return logger
