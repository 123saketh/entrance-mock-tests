@echo off
REM Serves the entrance mock tests on http://localhost:5191
REM Leave this window open while you use the app; close it to stop the server.
cd /d "%~dp0"
if not exist node_modules (
  echo Installing dependencies, first run only...
  call npm install
)
echo.
echo   Entrance Mock Tests (BITSAT, TS ^& AP EAMCET)
echo   ------------------------------------------
echo   Starting server on http://localhost:5191
echo   Leave this window open. Press Ctrl+C to stop.
echo.
call npx vite --port 5191 --strictPort --open
pause
