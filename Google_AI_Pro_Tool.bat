@echo off
chcp 65001 >nul
title Google AI Pro 24-Month Automator - Windows 11 Fluent App
cd /d "%~dp0"

echo ======================================================================
echo   GOOGLE AI PRO 24-MONTH AUTOMATOR (WINDOWS 11 FLUENT APP)
echo ======================================================================
echo Dang khoi dong giao dien Windows 11 Fluent Design...
echo.

"C:\Users\khoa\AppData\Local\Microsoft\WindowsApps\python.exe" gui_app.py

if %errorlevel% neq 0 (
    echo.
    echo Phat hien loi khi chay GUI!
    pause
)
