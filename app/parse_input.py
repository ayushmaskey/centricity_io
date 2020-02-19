"""Decide which sql statemnt to build depending on argument from centricity."""

from sql.sql_query import query_by_job_title
from cps_logging import config_logging
logger = config_logging()


def cps_parameter_parse(param):
    """If statement to determine which function to call.

    >>> zero_param = "0|case manager"
    >>> preloader_param = "1|Preloader"
    >>> error_param = "100|Preloader"
    >>> cps_parameter_parse(zero_param)
    'Zero'
    >>> cps_parameter_parse(preloader_param)
    'c y test  [ctest]'
    >>> cps_parameter_parse(error_param)
    'Input error'
    """
    logger.debug(f'{__name__}: parameter passes was {param}')
    input_str = param.split('|')
    return_str = ""

    try:
        query_switch = int(input_str[0])
        query = input_str[1].strip()
        logger.debug(f'{__name__}: Query switch - {query_switch}' +
                     f' Query - {query}')
    except ValueError:
        logger.warning(f"{__name__}: Error converting to int")
    except Exception:
        logger.warning(f'{__name__} Unknown error:', exec_info=True)

    # 0 --> testing
    if query_switch == 0:
        logger.warning(f'{__name__}: Query switch should not be 0')
        return_str = "Zero"
    # 1 --> query by jobTitle
    elif query_switch == 1:
        result = query_by_job_title(query)
        logger.debug(f'{__name__} Parsed output --> {result}')
        return_str = result
    # discard unknown argument
    else:
        logger.warning(f'{__name__}: Query switch is unknown')
        return_str = "Input error"

    return return_str


if __name__ == "__main__":
    import doctest
    doctest.testmod()
