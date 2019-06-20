#!/usr/bin/python3

def sql_result_comma_separate_first_column(rows):
	""" loop over sql result 
		convert first column of each row into string
		return comma separated
	"""
	return_str = ""
	for row in rows:
		return_str = return_str + str(row[0]) + ","
	return_str = return_str[:-1]
	return return_str 