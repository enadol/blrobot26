@echo off
setlocal

:: Configuration
set "DB_FILE=season25.sqlite"

:: Check if database file exists
if not exist "%DB_FILE%" (
    echo Error: Database file "%DB_FILE%" not found.
    exit /b 1
)

:: Check for required environment variables (just a few to be safe)
if "%ALFA_HOST%"=="" (
    echo Error: Environment variables not set. Please set ALFA_HOST, ALFA_USER, ALFA_PASS, etc.
    echo You can use a separate batch file to set these, e.g., set_sftp_env.bat
    exit /b 1
)

echo Starting upload for %DB_FILE%...

:: Sanitize paths (replace backslashes with forward slashes)
set "ALFA_PATH=%ALFA_PATH:\=/%"
set "SHINY_PATH_1=%SHINY_PATH_1:\=/%"
set "SHINY_PATH_2=%SHINY_PATH_2:\=/%"

:: --- Server 1 ---
echo.
echo Uploading to Server 1 (%ALFA_HOST%)...
curl -k -u "%ALFA_USER%:%ALFA_PWD%" -T "%DB_FILE%" "sftp://%ALFA_HOST%%ALFA_PATH%/" --ftp-create-dirs
if %ERRORLEVEL% NEQ 0 (
    echo Error uploading to Server 1
) else (
    echo Server 1 upload successful.
)

:: --- Server 2 Path 1 ---
echo.
echo Uploading to Server 2 (%SHINY_HOST%) - Path 1...
curl -k -u "%SHINY_USER%:%SHINY_PWD%" -T "%DB_FILE%" "sftp://%SHINY_HOST%%SHINY_PATH_1%/" --ftp-create-dirs
if %ERRORLEVEL% NEQ 0 (
    echo Error uploading to Server 2 Path 1
) else (
    echo Server 2 Path 1 upload successful.
)

:: --- Server 2 Path 2 ---
echo.
echo Uploading to Server 2 (%SHINY_HOST%) - Path 2...
curl -k -u "%SHINY_USER%:%SHINY_PWD%" -T "%DB_FILE%" "sftp://%SHINY_HOST%%SHINY_PATH_2%/" --ftp-create-dirs
if %ERRORLEVEL% NEQ 0 (
    echo Error uploading to Server 2 Path 2
) else (
    echo Server 2 Path 2 upload successful.
)

echo.
echo All tasks completed.
pause
