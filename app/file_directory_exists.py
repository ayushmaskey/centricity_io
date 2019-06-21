"""Check if file and directory exists."""

from pathlib import Path
from cps_logging import config_logging


logger = config_logging()


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
    """
    path = Path(dirName)
    if not path.is_dir():
        try:
            path.mkdir()
        except FileExistsError:
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


if __name__ == "__main__":
    import doctest
    doctest.testmod()
