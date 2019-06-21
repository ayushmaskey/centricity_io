"""Get argument from Centricity and return SQL result."""

# !/usr/bin/python3
import parse_input
from file_directory_exists import temp_output_file_exists
from cps_logging import config_logging
import sys


logger = config_logging()


def get_details_from_argument(argv):
    r"""Input string from centricity individual parts.

    >>> param = ["/o", ".\\log\\test.log", "/i", "1|case manager"]
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
        input_str = argv[3]
        logger.debug(f'{__name__}: Output temp file:' +
                     ' {output_file},' +
                     'Input String: {input_str}')
    except IndexError:
        logger.warning(f'Index out of bound. Argument from centricity.')
    except Exception:
        logger.warning(f'{__name__} has error:', exec_info=True)

    return output_file, input_str


def cps_temp_file_output(argv):
    r"""Take input from Centricity and return result to temp file.

    >>> param = ["/o", ".\\log\\test.log", "/i", "1|preloader"]
    >>> cps_temp_file_output(param)
    c y test  [ctest]
    """
    output_file, input_str = get_details_from_argument(argv)
    output_file_exists = temp_output_file_exists(output_file)

    if output_file_exists:
        result = parse_input.cps_parameter_parse(input_str)
        file = open(output_file, "w")
        file.write(result)
        file.close()
        logger.debug(result)
    else:
        logger.warning('Output temp file not found.')


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    cps_temp_file_output(sys.argv[1:])
