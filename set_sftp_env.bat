@echo off
:: Set your SFTP credentials here and run this script before running upload_db.bat
:: Or add these to your system environment variables.

:: Server 1 Credentials
:: Server 1 Credentials (ALFA)
set "ALFA_HOST=81.34.88.93"
set "ALFA_USER=h204505"
set "ALFA_PWD=zcNOTvy19t5_tK&b"
set "ALFA_PATH=\html\dist\_file\data"

:: Server 2 Credentials (SHINY)
set "SHINY_HOST=138.68.139.38"
set "SHINY_USER=root"
set "SHINY_PWD=wojhot500,D0"
set "SHINY_PATH_1=\srv\shiny-server\tablas"
set "SHINY_PATH_2=\var\www\html\dist\_file\data"

echo Environment variables set. You can now run upload_db.bat
