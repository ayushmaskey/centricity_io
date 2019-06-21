"""Convert SQL rows into comma separated string.."""


def sql_result_comma_separate_first_column(rows):
    """Convert single column sql result into comma separated string.

    >>> rows = [('test1', ), ('test2', )]
    >>> sql_result_comma_separate_first_column(rows)
    'test1,test2'
    """
    return_str = ""
    for row in rows:
        return_str = return_str + str(row[0]) + ","

    return_str = return_str[:-1]
    return return_str


if __name__ == "__main__":
    import doctest
    doctest.testmod()
