@echo off
chcp 65001 >nul
title "Google AI Pro - Chay Nang Cap 24 Thang (Stacking Flow)"
cd /d "%~dp0"

call "%~dp0tools\bootstrap_env.bat"
if %errorlevel% neq 0 exit /b %errorlevel%

echo ======================================================================
echo   GOOGLE AI PRO 24-MONTH: CHAY TU DONG CHONG GOI 24 THANG ($0.00)
echo ======================================================================
echo.
echo Quy trinh tu dong:
echo   - Kiem tra ket noi US VPN (Browsec)
echo   - Layer 1: Goi 12 thang co ban ($0.00)
echo   - Layer 2: Goi +6 thang S25 (Len thang 5/2028 - $0.00)
echo   - Layer 3: Goi +6 thang Pixel (Len thang 11/2028 - $0.00)
echo   - Huy gia han tu dong de triet tieu phi YouTube Premium $11.99
echo   - Khoa cung 24 thang Google AI Pro 5 TB den thang 11/2028!
echo.
echo ======================================================================
echo.

"%PY_CMD%" launch_interactive_instance.py exec %1

echo.
pause
