#!/usr/bin/python3

import sys
import os
from pathlib import Path
import time
from app.parse_input import cps_parameter_parse


def dir_exists(dirName):
    """check if directory exists, if not create the directory"""
    path = Path(dirName)
    if not Path(dirName).is_dir():
        Path(dirName).mkdir()
    return Path(dirName).is_dir()

def file_exists(fileName):
    """ check if file exists"""
    path = Path(fileName)
    return Path(fileName).is_file()

def file_exists_create(fileName):
    """check if file exists, if not create the file"""
    path = Path(fileName)
    if not path.is_file():
        open(fileName, 'wb')
    return Path(fileName).is_file()
        
def get_details_from_argument(argv):
    """input string from centricity individual parts"""
    output_file_identifier = argv[0]
    output_file = argv[1]
    input_str_identifier = argv[2]
    input_str = argv[3]
    return output_file, input_str
  
def update_log( log_str, filename ):
    """append success and failure log with 
        timestamp --> custom with date, and time
        and success or failure
    """
    current_time = time.localtime()
    time_str = time.strftime('%a, %m-%d-%Y %H:%M:%S', current_time)

    try:
        if file_exists_create(filename):
            file = open(filename, "a")
            file.write(time_str + "|" + log_str + "\n\r")
            file.close()
            return True
    except:
        return False

def cps_temp_file_output(argv):
    """ 
    get output file name and input string from argument provided from centricity
    if the output file exists --> save result to output file
    if output file does not exists --> update the log file
    """
    output_file, input_str = get_details_from_argument( argv )
    test_success_str = "Success accessing^%s^input string:^%s" %(output_file,input_str)
    log_str = "Cannot find file:^%s" %(output_file)

    dir_path = os.getcwd() + "\\log\\"
    fname = "event.log"
    filename = dir_path  + fname


    if file_exists(output_file) and dir_exists(dir_path):
        result = cps_parameter_parse(input_str)
        
        log_str = "file:" + output_file + ", result: " + result
        update_log(log_str, filename)

        file = open(output_file, "w")
        file.write(result)
        file.close()
        log_str = result
        
    update_log(log_str, filename)

        
if __name__ == "__main__":
    cps_temp_file_output(sys.argv[1:])
