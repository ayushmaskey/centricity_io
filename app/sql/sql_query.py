"""Build query to pass into sql_connection."""

from sql.sql_connection import sqlConn
from sql.sql_result_to_string import sql_result_comma_separate_first_column
from cps_logging import config_logging
logger = config_logging()


def query_by_job_title(job_title):
    """Prepare query for job title.

    >>> query_by_job_title("Preloader")
    'c y test  [ctest]'
    """
    query = (
        "select  isnull(first, '') + ' ' + isnull(Middle, '') + ' ' + " +
        "isnull(last, '') + ' ' + isnull(df.Suffix, '') + ' [' + " +
        "df.LoginUser + ']' Name from doctorfacility df " +
        "left join JOBTITLE jt on jt.JTID = df.JobTitleGID " +
        "where Inactive = 0 " +
        "and LoginUser is not null " +
        "and pvid > 0 " +
        "and jt.DESCRIPTION = '%s' " +
        "order by Name "
    ) % (job_title)
    logger.debug(f'{__name__}: Query string is {query}')

    rows = sqlConn(query)
    result = sql_result_comma_separate_first_column(rows)
    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()
