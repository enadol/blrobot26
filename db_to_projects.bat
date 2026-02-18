@echo off
setlocal enabledelayedexpansion

REM Set the source file path
set "SOURCE_FILE=F:\blrotob26\season25.sqlite"

REM Set the destination directories
set "DEST_DIR1=F:\bundesliga-century\docs\data"
set "DEST_DIR2=C:\destination\folder2"

REM Copy to first directory
copy "%SOURCE_FILE%" "%DEST_DIR1%" /Y
if errorlevel 1 (
    echo Error copying to %DEST_DIR1%
    exit /b 1
)
echo Successfully copied to %DEST_DIR1%

REM Copy to second directory
copy "%SOURCE_FILE%" "%DEST_DIR2%" /Y
if errorlevel 1 (
    echo Error copying to %DEST_DIR2%
    exit /b 1
)
echo Successfully copied to %DEST_DIR2%

echo Copying completed successfully!
pause