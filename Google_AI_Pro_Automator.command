#!/usr/bin/env bash
# ==============================================================================
# Google AI Pro 24M Zero-Cost Automator — macOS 1-Click Finder Launcher
# Author: Trinh Dang Khoa (Alex Trinh) <tumo07@io.vn> | GitHub: @tumo07
# Supports: Apple Silicon (arm64) & Intel (x86_64) Macs
# ==============================================================================

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

echo "======================================================================"
echo "  Google AI Pro 24M Zero-Cost Automator · macOS Universal"
echo "  Architecture: $(uname -m) | Apple Silicon & Intel Compatible"
echo "======================================================================"

# If virtual environment doesn't exist, run setup first
if [ ! -d ".venv" ]; then
    echo "[*] First-time setup detected. Initializing environment..."
    bash setup_macos.sh
fi

source .venv/bin/activate
exec python3 gui_app.py
