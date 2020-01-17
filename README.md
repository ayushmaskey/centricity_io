# centricity_io

## sql connection edits
1. rename sql_connection_dummy.py to sql_connection.py
2. enter variables:
    servername: centricity database server name
    db: centricity database rename
    username: user account with read only access to centricity database
    pwd: password for user

## Testing

` python cps_io.py "/o" "..\\log\\test.log" "/i" "1|case manager" `

` cps_io.exe "/o" "..\\log\\test.log" "/i" "1|case manager" `

### logging levelname
1. app/logging --> change `loglevel = logging.WARNING` to `loglevel = logging.DEBUG`

## create .exe from .py
`pyinstaller  --onedir --onefile  cps_io.py`

`pyinstaller --onefile main.spec`


## Usage
1. get comma separated users by job title
```
local argStr = "/i 1|case manager"
local caseManager = RunTextProcess(testPath, argStr)
```
returns `john m. doe [jdoe], alice r. smith [asmith]`
