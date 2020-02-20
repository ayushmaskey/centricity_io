# centricity_io

## Usage
1. get comma separated users by job title
```Centricity
local argStr = "/i 1|case manager"
local caseManager = RunTextProcess(testPath, argStr)
```
returns `john m. doe [jdoe], alice r. smith [asmith]`


## Before running the program
### Modules Requred
```python
pip install pyodbc
pip install sql
pip install pyinstaller
pip install flake8 #tab vs space - ignore Error W191 in setting.json & increase the max-line-length
pip install pylint
doctest, sys, datetime, logging, pathlib, unittest, os #should be installed by default
```

### sql connection config file
rename config_sample.json to config.json
servername: centricity database server name
db: centricity database name
username: user account with read only access to centricity database
pwd: password for user

### logging levelname --> for debug
1. .\cps_io\app\logging --> change `loglevel = logging.WARNING` to `loglevel = logging.DEBUG`

## Test
### DocTest individual files

```python
Run from ".\cps_io\app" as base in powershell
#verbose
python -m cps_logging -v
python -m sql.sql_connection -v 
python -m sql.sql_result_to_string -v 
python -m sql.sql_query -v 
python -m parse_input -v 
python -m cps_io -v #change comment in __main__

#quick test -- no result is good
python -m cps_logging
python -m sql.sql_connection 
python -m sql.sql_result_to_string 
python -m sql.sql_query 
python -m parse_input 
python -m cps_io 

change comment in __main__
```

### Unittest
```bash
#Using context.py file to import main project folder cps_io (parent of test folder) into python path
#Run from .\cps_io\app
python ..\test\test_app.py -v
#Not ready 
python ..\test\test_io.py -v 
```

### Complete app Testing

```bash
#Run from .\cps_io\app
#Using context.py file to import modules  
python cps_io.py "/o" ".\\log\\test.log" "/i" "1|case manager" 
# comma separated case managers show up in .\cps_io\log\test.log
```

## Convert to .exe and test

### create .exe from .py
```bash
#Run from .\cps_io\app 
pyinstaller --onedir --onefile --windowed  cps_io.py
# pyinstaller --onefile cps_io.spec
```

### test .exe
```bash
.\dist\cps_io.exe "/o" ".\\log\\test.log" "/i" "1|case manager" 
```


