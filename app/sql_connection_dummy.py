#!/usr/bin/python3
import pyodbc

def sqlConn(query):
	"""start a sql connection
		get the result
		close the connection
		return the result
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

