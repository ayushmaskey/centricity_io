#!/usr/bin/python3

import unittest
import context
import app.sql.sql_connection as sql
import app.sql.sql_result_to_string as sql_str
# import sys
# print(sys.path)


class unittest_app(unittest.TestCase):

	def test(self):
		pass

	""" unit test for sql_connection.py """
	def test_sql_result_type_check(self):
		expectation = 'amaskey'
		q = "select LoginUser from DoctorFacility where LoginUser = '%s'" % (expectation)
		rows = sql.sqlQuery(q)
		self.assertEqual(type(rows), list)

	def test_sql_conn(self):
		expectation = 'amaskey'
		q = "select LoginUser from DoctorFacility where LoginUser = '%s'" % (expectation)
		rows = sql.sqlQuery(q)
		for row in rows:
			result = row[0].lower()
			break
		self.assertEqual(result, expectation)

	""" unit test for sql_result_to_string.py """
	def test_sql_result_comma_separate_first_column(self):
		rows = [('amaskey', 'it'), ('jeff', )]
		expectation = "amaskey,jeff"
		str1 = sql_str.sql_result_comma_separate_first_column(rows)
		self.assertEqual(str1, expectation)


if __name__ == '__main__':
	unittest.main()
