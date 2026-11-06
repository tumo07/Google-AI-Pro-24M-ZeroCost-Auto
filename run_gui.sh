#!/usr/bin/env bash
# ==============================================================================
# Google AI Pro 24M Zero-Cost Automator — macOS GUI Launcher
# Author: Trinh Dang Khoa (Alex Trinh) <tumo07@io.vn> | GitHub: @tumo07
# Supports: Apple Silicon (arm64) & Intel (x86_64) Macs
# ==============================================================================

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

if [ -f ".venv/bin/activate" ]; then
    source .venv/bin/activate
fi

# Detect Python interpreter
PYTHON_CMD="python3"
if command -v python &> /dev/null && [ "$(python -c 'import sys; print(sys.version_info.major)')" -eq 3 ]; then
    PYTHON_CMD="python"
fi

exec $PYTHON_CMD gui_app.py "$@"
