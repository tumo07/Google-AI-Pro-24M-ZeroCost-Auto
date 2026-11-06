@echo off
chcp 65001 >nul
title "Google AI Pro 24M Zero-Cost Automator"
cd /d "%~dp0"

echo ======================================================================
echo   Google AI Pro 24M Zero-Cost Automator
echo   Tac gia: Trinh Dang Khoa (Alex Trinh) ^<tumo07@io.vn^>
echo   GitHub: @tumo07 ^| License: MIT
echo ======================================================================
echo Dang kiem tra moi truong va thu vien phu thuoc...

call "%~dp0tools\bootstrap_env.bat"
if %errorlevel% neq 0 exit /b %errorlevel%

echo Khoi chay giao dien dieu khien...
"%PY_CMD%" gui_app.py
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo [LOI] Khong the khoi chay gui_app.py!
    pause
)
