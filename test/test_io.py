"""Unit testing.

Unit testing for centricity_io.py,
file_directory_exists.py and
parse_input.py.
"""


import sys

import unittest
import logging
import os
import context
import app.cps_io as cps_io
print(sys.path)
import app.cps_logging as fd
import app.parse_input as parse


logging.basicConfig(level=logging.CRITICAL)
logging.debug("Import Worked")


class unittest_main(unittest.TestCase):
    """Unit test for file_directory_exists.py."""

    def test_file_exists(self):
        """Check if file exists."""
        self.assertEqual(fd.temp_output_file_exists(".\\temp_file.txt"), True)

    @unittest.skip("Skip Test")
    def test_file_exists_create(self):
        """Check if file exists else create new file."""
        self.assertEqual(fd.temp_output_file_exists("../log/event.log"), True)

    def test_dir_exists(self):
        """Check if directory exists."""
        self.assertEqual(fd.dir_exists("../log"), True)

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
    unittest.main()
    # print(sys.path)
    # print(os.getcwd())
