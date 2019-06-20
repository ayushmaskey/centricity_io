#!/usr/bin/python3

from app import sql_connection
from app import sql_result_to_string



def query_by_job_title(job_title):
	"""prepare query for job title
		take job title as parameter
		return comma separated users from centricity
	"""
	query = "select  isnull(first,'') + ' ' + \
				 isnull(Middle,'') + ' ' + \
				 isnull(last,'') + ' ' + \
				 isnull(df.Suffix,'') + \
				 ' [' + df.LoginUser + ']' Name \
			from doctorfacility df \
				left join JOBTITLE jt on jt.JTID = df.JobTitleGID \
			where Inactive = 0  \
				and LoginUser is not null \
				and pvid > 0 \
				and jt.DESCRIPTION = '%s' \
			order by Name" %(job_title)

	rows = sql_connection.sqlConn(query)

	result = sql_result_to_string.sql_result_comma_separate_first_column(rows)
	return result


