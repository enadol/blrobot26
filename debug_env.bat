@echo off
echo Environment Variable Debug:
echo --------------------------
echo ALFA_HOST: "%ALFA_HOST%"
echo ALFA_USER: "%ALFA_USER%"
echo ALFA_PATH: "%ALFA_PATH%"
echo SHINY_HOST: "%SHINY_HOST%"
echo SHINY_USER: "%SHINY_USER%"
echo SHINY_PATH_1: "%SHINY_PATH_1%"
echo SHINY_PATH_2: "%SHINY_PATH_2%"
echo.
echo Password Check (Not showing full password):
if defined ALFA_PASS (
    echo ALFA_PASS is set. (Length: %ALFA_PASS:~0,1%...)
) else (
    echo ALFA_PASS is NOT set.
)
if defined SHINY_PASS (
    echo SHINY_PASS is set. (Length: %SHINY_PASS:~0,1%...)
) else (
    echo SHINY_PASS is NOT set.
)
pause
