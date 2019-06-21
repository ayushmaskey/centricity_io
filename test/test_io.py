"""Unit testing.

Unit testing for centricity_io.py,
file_directory_exists.py and
parse_input.py.
"""


import unittest
import sys
import logging
import os
import app.sql.sql_connection

# from .context import app
from app import file_directory_exists as fd
# import app.parse_input as parse


logging.basicConfig(level=logging.DEBUG)
logging.debug("Import Worked")


class unittest_main(unittest.TestCase):
    """Unit test for file_directory_exists.py."""

    def test_file_exists(self):
        """Check if file exists."""
        self.assertEqual(fd.file_exists("temp_file.txt"), True)

    def test_file_exists_create(self):
        """Check if file exists else create new file."""
        self.assertEqual(fd.file_exists_create("../log/event.log"), True)

    def test_dir_exists(self):
        """Check if directory exists."""
        self.assertEqual(dir_exists("../log"), True)

    """Unit test for centricity_io.py."""

    def test_get_details_from_argument(self):
        """Unit test ro separate centricity arguments."""
        x_list = [
            "/o",
            "./temp_file.txt",
            "/i",
            "1|test"
            ]
        output_path, input_str = cps_io.get_details_from_argument(x_list)
        self.assertEqual(input_str, x_list[3])
        self.assertEqual(output_path, x_list[1])

    def test_udpate_log(self):
        """Test update log function."""
        log_status = cps_io.update_log("unittest", "../log/event.log")
        self.assertEqual(log_status, True)

    def test_cps_temp_file_output(self):
        """Someday."""
        pass

    """Unit test for parse_input.py."""

    def test_cps_parse_input(self):
        """Test parse_input function."""
        self.assertEqual(parse.cps_parameter_parse("0|Zero"), "Zero")
        self.assertIsNone(parse.cps_parameter_parse("10|Ten"))
        self.assertEqual(parse.cps_parameter_parse("1|case manager"),
                         'amaskey')


if __name__ == '__main__':
    # unittest.main()
    print(sys.path)
    print(os.getcwd())
