"""Function to initialize connection  to SQL Server."""

import pyodbc
import json
from cps_logging import config_logging
logger = config_logging()


def sqlConnection():

    with open('config.json') as config_file:
        sql = json.load(config_file)

    odbc_driver_10 = '{SQL Server Native Client 10.0}'
    # basic_sql_driver = '{SQL Server}'
    # odbc_driver_13 = '{ODBC Driver 13 for SQL Server}'
    try:
        conn_string = (
            f'DRIVER={odbc_driver_10}; SERVER={sql["servername"]};' +
            f'DATABASE={sql["db"]}; UID={sql["username"]}; PWD={sql["password"]}'
        )
        conn = pyodbc.connect(conn_string)
        logger.debug(f'{__name__}: Successfully connected to SQL')
    except pyodbc.Error as ex:
        sql_state = ex.args[1]
        logger.warning(f'{__name__}: {sql_state}')
    except Exception:
        logger.warning(f'{__name__} Unknown error:', exec_info=True)
    return conn


def sqlQuery(query):
    """Connect to SQL and run query provided.

    >>> q = "select LoginUser from DoctorFacility where LoginUser = 'amaskey'"
    >>> result = sqlQuery(q)
    >>> print(result)
    [('Amaskey', )]
    """
    try:
        conn = sqlConnection()
        cur = conn.cursor()
        cur.execute(query)
        res = cur.fetchall()
        conn.close()
    except pyodbc.Error as ex:
        sql_state = ex.args[1]
        logger.warning(f'{__name__}: {sql_state}')
    except Exception:
        logger.warning(f'{__name__} Unknown error:', exec_info=True)
    logger.debug(f'{__name__}: Exit try except for sql connection.')
    return res


if __name__ == "__main__":
    import doctest
    doctest.testmod()
