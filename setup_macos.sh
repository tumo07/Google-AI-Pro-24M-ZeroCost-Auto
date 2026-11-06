#!/usr/bin/env bash
# ==============================================================================
# Google AI Pro 24M Zero-Cost Automator — macOS Universal Setup
# Author: Trinh Dang Khoa (Alex Trinh) <tumo07@io.vn> | GitHub: @tumo07
# Supports: Apple Silicon (M1/M2/M3/M4 arm64) & Intel (x86_64) Macs
# ==============================================================================

set -e

echo "======================================================================"
echo "  Google AI Pro 24M Zero-Cost Auto — macOS Setup"
echo "======================================================================"

ARCH=$(uname -m)
echo "[*] Detecting CPU Architecture: $ARCH"
if [ "$ARCH" = "arm64" ]; then
    echo "    ✅ Running natively on Apple Silicon (M1/M2/M3/M4)"
elif [ "$ARCH" = "x86_64" ]; then
    echo "    ✅ Running on Intel Mac (x86_64)"
else
    echo "    ℹ️ Running on architecture: $ARCH"
fi

# Detect Python 3
PYTHON_BIN=""
if command -v python3 &> /dev/null; then
    PYTHON_BIN="python3"
elif [ -f "/opt/homebrew/bin/python3" ]; then
    PYTHON_BIN="/opt/homebrew/bin/python3"
elif [ -f "/usr/local/bin/python3" ]; then
    PYTHON_BIN="/usr/local/bin/python3"
fi

if [ -z "$PYTHON_BIN" ]; then
    echo "[-] Python 3 not found!"
    echo "    Please install Python 3 via Homebrew: brew install python"
    echo "    Or download from: https://www.python.org/downloads/macos/"
    exit 1
fi

PY_VER=$($PYTHON_BIN -c "import sys; print('.'.join(map(str, sys.version_info[:2])))")
echo "[+] Found Python $PY_VER at $PYTHON_BIN"

# Check Virtual Environment
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

if [ ! -d ".venv" ]; then
    echo "[*] Creating virtual environment (.venv)..."
    $PYTHON_BIN -m venv .venv
fi

echo "[*] Activating virtual environment..."
source .venv/bin/activate

echo "[*] Upgrading pip..."
pip install --upgrade pip

echo "[*] Installing Python dependencies..."
pip install -r requirements.txt

echo "[*] Installing Playwright Chromium browser driver..."
python -m playwright install chromium

# Detect installed browsers on macOS
echo "[*] Checking for installed browsers in /Applications..."
BROWSER_FOUND=0

if [ -d "/Applications/Google Chrome.app" ]; then
    echo "    ✅ Google Chrome detected"
    BROWSER_FOUND=1
fi
if [ -d "/Applications/Microsoft Edge.app" ]; then
    echo "    ✅ Microsoft Edge detected"
    BROWSER_FOUND=1
fi
if [ -d "/Applications/Brave Browser.app" ]; then
    echo "    ✅ Brave Browser detected"
    BROWSER_FOUND=1
fi

if [ $BROWSER_FOUND -eq 0 ]; then
    echo "    ⚠️ Neither Chrome, Edge, nor Brave was detected in /Applications."
    echo "    The tool can still operate using Playwright's built-in Chromium,"
    echo "    but installing Google Chrome or Microsoft Edge is recommended."
fi

# Make scripts executable
chmod +x run_gui.sh 2>/dev/null || true
chmod +x run_stacker.sh 2>/dev/null || true
chmod +x Google_AI_Pro_Automator.command 2>/dev/null || true
chmod +x setup_macos.sh 2>/dev/null || true

echo ""
echo "======================================================================"
echo "  ✅ macOS Setup Complete! (Apple Silicon & Intel Universal Ready)"
echo "======================================================================"
echo ""
echo "You can now launch the application via:"
echo "  1. Double-click: Google_AI_Pro_Automator.command in Finder"
echo "  2. Terminal GUI: ./run_gui.sh"
echo "  3. Terminal CLI: ./run_stacker.sh"
echo "======================================================================"
