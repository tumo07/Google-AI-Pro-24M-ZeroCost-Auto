@echo off
chcp 65001 >nul
title "Google AI Pro 24-Month Automator"
cd /d "%~dp0"

echo ======================================================================
echo   GOOGLE AI PRO 24-MONTH AUTOMATOR (UNIVERSAL APP)
echo ======================================================================
echo Dang kiem tra moi truong va tu dong cai dat thu vien...
echo.

call "%~dp0tools\bootstrap_env.bat"
if %errorlevel% neq 0 exit /b %errorlevel%

%PY_CMD% gui_app.py
