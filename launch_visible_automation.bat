@echo off
title Google AI Pro 2-Year ZeroCost Automation
cd /d "%~dp0"
echo ============================================================
echo Executing Step 5: Auto-Cancel Renewal & Verify Subscription
echo ============================================================
python run_account.py 5
echo.
echo Automation finished.
pause
