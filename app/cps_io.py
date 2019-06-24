"""Get argument from Centricity and return SQL result."""

# !/usr/bin/python3
import parse_input
from cps_logging import config_logging, temp_output_file_exists
import sys
from datetime import datetime

logger = config_logging()


def get_details_from_argument(argv):
    r"""Input string from centricity individual parts.

    >>> param = ["/o", ".\\log\\test.log", "/i", "1|preloader"]
    >>> output_file, input_str = get_details_from_argument(param)
    >>> print(f"{output_file}")
    .\log\test.log
    >>> input_str
    '1|case manager'
    """
    try:
        # output_file_identifier = argv[0]
        output_file = argv[1]
        # input_str_identifier = argv[2]
        input_str = argv[3:]
        input_str = ' '.join(input_str)
        logger.info(f'{__name__}: Output temp file: ' + output_file +
                    ' Input String: ' + input_str)
    except IndexError:
        logger.warning(f'Index out of bound. Argument from centricity.')
    except Exception:
        logger.warning(f'{__name__} Unknown error:', exec_info=True)

    return output_file, input_str


def cps_temp_file_output(argv):
    r"""Take input from Centricity and return result to temp file.

    >>> param = ["/o", ".\\log\\test.log", "/i", "1|preloader"]
    >>> cps_temp_file_output(param)
    c y test  [ctest]
    """
    logger.debug(f'{__name__}: Input from CPS ' + str(argv))
    output_file, input_str = get_details_from_argument(argv)
    output_file_exists = temp_output_file_exists(output_file)

    if output_file_exists:
        logger.debug(f'{__name__}: Output temp file found.')
        result = parse_input.cps_parameter_parse(input_str)
        logger.info(result)
        file = open(output_file, "w")
        file.write(result)
        file.close()
    else:
        logger.warning(f'{__name__}: Output temp file not found.')


def test():
    """Unit test and path."""
    import doctest
    doctest.testmod()

    import os
    from cps_logging import dir_exists
    dir_path = os.getcwd() + "\\log\\"
    filename = __name__ + '_' + datetime.now().strftime('%Y-%m-%d') + '.log'
    file_path = dir_path + filename
    logger.info("current working directory:" + file_path)
    dir_exists(dir_path)


if __name__ == "__main__":
    cps_temp_file_output(sys.argv[1:])
    # test()
