#!/usr/bin/python3

import unittest

import sys
sys.path.insert(0, '../')
import main

sys.path.append('../app/')
import parse_input


class unittest_main(unittest.TestCase):
	""" unit test for main.py """
	def test_file_exists(self):
		self.assertEqual(main.file_exists("temp_file.txt"), True)

	def test_file_exists_create(self):
		self.assertEqual(main.file_exists_create("../log/event.log"), True)

	def test_dir_exists(self):
		self.assertEqual(main.dir_exists("../log"), True )

	def test_get_details_from_argument(self):
		x_list = [
				"/o", 
				"./temp_file.txt", 
				"/i", 
				"1|test"
			]
		output_path, input_str = main.get_details_from_argument(x_list)
		self.assertEqual( input_str, x_list[3])
		self.assertEqual( output_path, x_list[1] )

	def test_udpate_log(self):
		log_status = main.update_log( "unittest", "../log/event.log")
		self.assertEqual( log_status, True)

	def test_cps_temp_file_output(self):
		pass

	""" unit test for parse_input.py"""
	def test_cps_parse_input(self):
		self.assertEqual(parse_input.cps_parameter_parse("0|Zero"), "Zero")
		self.assertIsNone(parse_input.cps_parameter_parse("10|Ten"))
		self.assertEqual(parse_input.cps_parameter_parse("1|case manager"), 'amaskey')

if __name__ == '__main__':
    unittest.main()