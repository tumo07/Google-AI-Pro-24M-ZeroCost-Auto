@echo off
chcp 65001 >nul
title Google AI Pro 24-Month Automator
cd /d "%~dp0"

echo ======================================================================
echo   GOOGLE AI PRO 24-MONTH AUTOMATOR (UNIVERSAL APP)
echo ======================================================================
echo Dang kiem tra va khoi dong giao dien...
echo.

where python >nul 2>nul
if %errorlevel% equ 0 (
    python gui_app.py
    goto end
)

where py >nul 2>nul
if %errorlevel% equ 0 (
    py gui_app.py
    goto end
)

echo [LOI] Khong tim thay Python tren he thong!
echo Vui long cai dat Python 3.10+ tu https://www.python.org/ va nho tich "Add Python to PATH"
pause

:end
