@echo off
REM ==============================================================================
REM Google AI Pro 24M Zero-Cost Auto -- Environment and Dependency Bootstrapper
REM Author: Trinh Dang Khoa (Alex Trinh) <tumo07@io.vn> | GitHub: @tumo07
REM SPDX-License-Identifier: MIT
REM ==============================================================================

set "BOOTSTRAP_DIR=%~dp0"
set "PROJECT_ROOT=%BOOTSTRAP_DIR%.."
cd /d "%PROJECT_ROOT%"

set PY_CMD=

:: 1. Check if 'python' works and is NOT the Microsoft Store placeholder stub
python -c "import sys; sys.exit(0)" >nul 2>nul
if %errorlevel% equ 0 (
    set PY_CMD=python
    goto py_found
)

:: 2. Check if 'py' (Python Launcher) works
py -3 -c "import sys; sys.exit(0)" >nul 2>nul
if %errorlevel% equ 0 (
    set PY_CMD=py -3
    goto py_found
)
py -c "import sys; sys.exit(0)" >nul 2>nul
if %errorlevel% equ 0 (
    set PY_CMD=py
    goto py_found
)

:: 3. Scan common Windows installation directories
for %%D in (
    "%LocalAppData%\Programs\Python\Python313\python.exe"
    "%LocalAppData%\Programs\Python\Python312\python.exe"
    "%LocalAppData%\Programs\Python\Python311\python.exe"
    "%LocalAppData%\Programs\Python\Python310\python.exe"
    "C:\Program Files\Python313\python.exe"
    "C:\Program Files\Python312\python.exe"
    "C:\Program Files\Python311\python.exe"
    "C:\Program Files\Python310\python.exe"
    "C:\Python313\python.exe"
    "C:\Python312\python.exe"
    "C:\Python311\python.exe"
    "C:\Python310\python.exe"
) do (
    if exist "%%~D" (
        "%%~D" -c "import sys; sys.exit(0)" >nul 2>nul
        if %errorlevel% equ 0 (
            set PY_CMD="%%~D"
            goto py_found
        )
    )
)

:: If Python was NOT found:
echo ======================================================================
echo   [!] KHONG TIM THAY PYTHON 3 TREN HE THONG!
echo ======================================================================
echo.
echo May tinh cua ban hien chua cai dat Python hoac Python chua duoc them
echo vao bien moi truong PATH.
echo.

:: Try auto-installing via winget if available
where winget >nul 2>nul
if %errorlevel% equ 0 (
    echo [*] Phat hien trinh cai dat Windows Package Manager (winget).
    echo Dang chuan bi tu dong cai dat Python 3.12 chinh chu tu Microsoft/Python.org...
    echo.
    winget install --id Python.Python.3.12 --exact --accept-package-agreements --accept-source-agreements
    if %errorlevel% equ 0 (
        echo.
        echo [OK] Da cai dat xong Python 3.12!
        echo Vui long dong cua so nay va chay lai file .bat de tiep tuc.
        pause
        exit /b 1
    )
)

echo [GIAI PHAP TOI UU]:
echo 1. TAI BAN STANDALONE .EXE (KHONG CAN CAI PYTHON):
echo    https://github.com/tumo07/Google-AI-Pro-24M-ZeroCost-Auto/releases
echo.
echo 2. HOAC TAI VA CAI DAT PYTHON 3:
echo    https://www.python.org/downloads/
echo    (Luu y: Nho tich chon muc "Add python.exe to PATH" khi cai dat)
echo.
start https://www.python.org/downloads/
pause
exit /b 1

:py_found
REM Run automated package and Playwright Chromium verification
%PY_CMD% "%BOOTSTRAP_DIR%check_dependencies.py"
if %errorlevel% neq 0 (
    echo.
    echo [LOI] Khong the tu dong cai dat thu vien phu thuoc!
    pause
    exit /b 1
)

:: Environment is ready
exit /b 0
