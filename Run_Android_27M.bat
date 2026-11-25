@echo off
chcp 65001 >nul
title "Google AI Pro 27M Zero-Cost Automator v2.0.0 (Android Play Billing)"
cd /d "%~dp0"

call "%~dp0tools\bootstrap_env.bat"
if %errorlevel% neq 0 exit /b %errorlevel%

echo ======================================================================
echo   GOOGLE AI PRO 27-MONTH ANDROID PLAY BILLING ENGINE (v2.0.0)
echo   Sequence: pro3 (3M) -^> pro12 (+12M) -^> pro6 (+6M) -^> pro6b (+6M)
echo ======================================================================
echo.
%PY_CMD% run_android_27m.py --check
if %errorlevel% neq 0 (
    echo [!] Fix ADB/Emulator connection and retry.
    pause
    exit /b 1
)
echo.
%PY_CMD% run_android_27m.py --list
echo.
%PY_CMD% run_android_27m.py --stack
echo.
pause
