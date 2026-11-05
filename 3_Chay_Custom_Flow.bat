@echo off
title Google AI Pro - Custom 24M Flow Console
cd /d "%~dp0"

:menu
cls
echo ============================================================
echo   GOOGLE AI PRO 24-MONTH CUSTOM STACKING CONSOLE
echo ============================================================
echo.
echo [0] Mo payments.google.com de tao Ho So My (NY/OR) va dong ho so cu
echo [1] Chay Layer 1 (Goi 12 thang co ban)
echo [2] Chay Layer 2 (Goi cong don 6 thang - S25)
echo [3] Chay Layer 3 (Goi cong don 6 thang - Pixel de len 24 thang)
echo [4] Huy gia han tu dong tren Google Play (Khoa $0.00)
echo [5] Chay tu dong toan bo quy trinh (Layer 1 - 2 - 3 - Huy gia han)
echo [6] Thoat
echo.
set /p opt="Nhap lua chon cua ban [0-6]: "

if "%opt%"=="0" (
    echo.
    echo Dang mo payments.google.com...
    python custom_stacking_flow.py profile ny
    pause
    goto menu
)
if "%opt%"=="1" (
    echo.
    echo Dang chay Layer 1...
    python custom_stacking_flow.py layer1
    pause
    goto menu
)
if "%opt%"=="2" (
    echo.
    echo Dang chay Layer 2...
    python custom_stacking_flow.py layer2
    pause
    goto menu
)
if "%opt%"=="3" (
    echo.
    echo Dang chay Layer 3...
    python custom_stacking_flow.py layer3
    pause
    goto menu
)
if "%opt%"=="4" (
    echo.
    echo Dang huy gia han tu dong...
    python custom_stacking_flow.py cancel
    pause
    goto menu
)
if "%opt%"=="5" (
    echo.
    echo Dang chay tu dong toan bo chu trinh...
    python custom_stacking_flow.py auto
    pause
    goto menu
)
if "%opt%"=="6" exit
goto menu
