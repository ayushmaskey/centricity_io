# centricity_io

##Change usename and password

## Create .exe from .py
pyinstaller  --onefile main.py
pyinstaller --onefile main.spec


##Testing
python main.py "/o" "\\kphc-srvfs\it\05_Ayush\SQL_Scripts\OutsideDaWall\python\centricity_io\test\temp_file.txt" "/i" "1|case manager"

main.exe "/o" "\\kphc-srvfs\it\05_Ayush\SQL_Scripts\OutsideDaWall\python\centricity_io\test\temp_file.txt" "/i" "1|test"

main.exe "/o" "tes.tmp" "/i" "1|test"