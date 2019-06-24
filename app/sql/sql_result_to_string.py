"""Convert SQL rows into comma separated string.."""

from cps_logging import config_logging
logger = config_logging()


def sql_result_comma_separate_first_column(rows):
    """Convert single column sql result into comma separated string.

    >>> rows = [('test1', ), ('test2', )]
    >>> sql_result_comma_separate_first_column(rows)
    'test1,test2'
    """
    return_str = ""
    for row in rows:
        return_str = return_str + str(row[0]) + ","
        logger.debug(f'{__name__} loop {return_str}')
    return_str = return_str[:-1]
    return return_str


if __name__ == "__main__":
    import doctest
    doctest.testmod()
