"""Decide which sql statemnt to build depending on argument from centricity."""

from sql import sql_query


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
    input_str = param.split('|')
    return_str = ""
    input_str[0] = int(input_str[0])
    input_str[1] = input_str[1].strip()

    # 0 --> testing
    if input_str[0] == 0:
        return_str = "Zero"
    # 1 --> query by jobTitle
    elif input_str[0] == 1:
        result = sql_query.query_by_job_title(input_str[1])
        return_str = result

    # discard unknown argument
    else:
        return_str = "Input error"

    return return_str


if __name__ == "__main__":
    import doctest
    doctest.testmod()
