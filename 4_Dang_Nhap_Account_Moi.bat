@echo off
chcp 65001 >nul
title "Google AI Pro - Dang Nhap Account Moi (Interactive Session)"
cd /d "%~dp0"

call "%~dp0tools\bootstrap_env.bat"
if %errorlevel% neq 0 exit /b %errorlevel%

echo ======================================================================
echo   GOOGLE AI PRO 24-MONTH: KHOI DONG CUA SO DANG NHAP INSTANCE MOI
echo ======================================================================
echo.
echo Cua so trinh duyet Edge voi Browsec VPN va Tien ich tiem Offer
echo se tu dong bat len tren man hinh cua ban (Session 1).
echo.
echo Hay thuc hien:
echo   1. Dang nhap tai khoan Google moi can nang cap.
echo   2. Xac nhan 2FA / Passkey tren dien thoai (neu co).
echo   3. Vao payments.google.com de dam bao da them ho so My (ZIP 97201 / 10118).
echo.
echo He thong se tu dong nhan dien khi ban dang nhap thanh cong!
echo ======================================================================
echo.

"%PY_CMD%" launch_interactive_instance.py launch %1

echo.
echo Dang nhap da san sang! Ban co the chay tiep file:
echo "5_Chay_Nang_Cap_24T.bat" de nang cap 24 thang.
echo.
pause
