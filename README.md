# centricity_io

## sql connection edits
1. rename sql_connection_dummy.py to sql_connection.py
2. enter variables:
    servername: centricity database server name
    db: centricity database rename
    username: user account with read only access to centricity database
    pwd: password for user

## Create .exe from .py
`pyinstaller  --onefile  main.py`

`pyinstaller --onefile main.spec`


## Testing

` python centricity_io.py "/o" "..\\log\\test.log" "/i" "1|case manager" `

` centricity_io.exe "/o" "..\\log\\test.log" "/i" "1|case manager" `

`main.exe "/o" "tes.tmp" "/i" "1|test"`

## Usage
1. get comma separated users by job title
```
local argStr = "/i 1|case manager"
local caseManager = RunTextProcess(testPath, argStr)
```
returns `john m. doe [jdoe], alice r. smith [asmith]`
