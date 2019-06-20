#!/usr/bin/python3

from app import sql_query  

def cps_parameter_parse(param):
	"""if statement to determine which function to call"""
	input_str = param.split('|')
	return_str = ""
	input_str[0] = int(input_str[0])
	input_str[1] = input_str[1].strip()

	if input_str[0] == 0:
		return_str = "Zero"
	elif input_str[0] == 1:
		result = sql_query.query_by_job_title(input_str[1])
		return_str = result
	elif input_str[0] == 2:
		return_str = "Two"
	else:
		return_str = None

	return return_str
