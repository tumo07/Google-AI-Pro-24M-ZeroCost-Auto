@echo off
chcp 65001 >nul
title Google AI Pro - Dang Nhap va Tu Dong Nang Cap 24T Tron Goi
cd /d "%~dp0"

call "%~dp0tools\bootstrap_env.bat"
if %errorlevel% neq 0 exit /b %errorlevel%

echo ======================================================================
echo   GOOGLE AI PRO 24-MONTH: DANG NHAP VA TU DONG NANG CAP A - Z
echo ======================================================================
echo.
echo 1. Trinh duyet Edge se hien tren man hinh cua ban.
echo 2. Ban chi can dang nhap tai khoan Google.
echo 3. Ngay khi dang nhap thanh cong, script se tu dong lam toan bo:
echo    Layer 1 (12M) -^> Layer 2 (6M) -^> Layer 3 (6M) -^> Huy gia han ($0.00)
echo ======================================================================
echo.

%PY_CMD% launch_interactive_instance.py full %1

echo.
pause
