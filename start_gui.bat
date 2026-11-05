@echo off
chcp 65001 >nul
title Google AI Pro 24M Zero-Cost Automator
echo ======================================================================
echo   Google AI Pro 24M Zero-Cost Automator
echo   Tac gia: Trinh Dang Khoa (Alex Trinh) ^<tumo07@io.vn^>
echo   GitHub: @tumo07 ^| License: MIT
echo ======================================================================
echo Dang kiem tra va khoi chay giao dien dieu khien...
python gui_app.py
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo [LOI] Khong the khoi chay gui_app.py!
    echo Vui long kiem tra Python da duoc cai dat va chay: pip install -r requirements.txt
    pause
)
