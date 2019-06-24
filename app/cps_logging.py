"""Central logging for whole app."""

import logging
from pathlib import Path
from datetime import datetime


def dir_exists(dirName):
    r"""Check if directory exists, if not create the directory.

    >>> import os
    >>> from pathlib import Path
    >>> dir_path = os.getcwd() + "\\log\\"
    >>> print(dir_path)
    R:\05_Ayush\Python\cps_io\log\
    >>> dir_exists(dir_path)
    True
    >>> Path(dir_path).is_dir()
    True
    >>> dir_path = os.getcwd() + "\\log\\"
    >>> dir_exists(dir_path)
    True
    """
    path = Path(dirName)
    if not path.is_dir():
        try:
            path.mkdir()
        except FileExistsError:
            logger = config_logging()
            logger.warning(f'Count not create {dirName} directory.')
    return path.is_dir()


def temp_output_file_exists(fileName):
    r"""Check if temp file from centricity exists.

    >>> import os
    >>> from pathlib import Path
    >>> dir_path = os.getcwd() + "\\log\\"
    >>> filename = dir_path + "test.log"
    >>> filename1 = dir_path + "test1.log"
    >>> temp_output_file_exists(filename)
    True
    >>> temp_output_file_exists(filename1)
    False
    """
    path = Path(fileName)
    return path.is_file()


def config_logging():
    """Test."""
    # Variables
    filename = __name__ + '_' + datetime.now().strftime('%Y-%m-%d') + '.log'
    format = '%(asctime)s - %(levelname)s: %(message)s '
    loglevel = logging.WARNING

    logger = logging.getLogger(__name__)
    if not logger.hasHandlers():
        logger.setLevel(loglevel)
        stream_handler = logging.FileHandler(filename)
        formattr = logging.Formatter(format)
        stream_handler.setFormatter(formattr)
        logger.addHandler(stream_handler)
        logger.setLevel(loglevel)
        logger.handler_set = True
    return logger


if __name__ == "__main__":
    import doctest
    doctest.testmod()
