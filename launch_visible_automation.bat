@echo off
title "Google AI Pro 2-Year ZeroCost Automation"
cd /d "%~dp0"

call "%~dp0tools\bootstrap_env.bat"
if %errorlevel% neq 0 exit /b %errorlevel%

echo ============================================================
echo Executing Step 5: Auto-Cancel Renewal ^& Verify Subscription
echo ============================================================
%PY_CMD% run_account.py 5
echo.
echo Automation finished.
pause
