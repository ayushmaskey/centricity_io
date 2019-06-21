"""Function to initial connection  to SQL Server."""

import pyodbc


def sqlConn(query):
    """Connect to SQL and run query provided.

    >>> q = "select LoginUser from DoctorFacility where LoginUser = 'username'"
    >>> result = sqlConn(q)
    >>> print(result)
    [('username', )]
    """
    servername = 'server.domain.com'
    db = 'database name'
    username = 'read only user'
    pwd = 'password'

    conn = pyodbc.connect(driver='{ODBC Driver 13 for SQL Server}',
                          host=servername,
                          database=db,
                          trusted_connection='yes',
                          user=username,
                          password=pwd
                          )
    cur = conn.cursor()
    cur.execute(query)
    res = cur.fetchall()
    conn.close()

    return res


if __name__ == "__main__":
    import doctest
    doctest.testmod()
