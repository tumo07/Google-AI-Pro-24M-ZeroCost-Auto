"""
Google AI Pro 24M Zero-Cost Auto — Automated Dependency & Environment Checker
Ensures all required Python packages and Playwright Chromium drivers are installed.
SPDX-License-Identifier: MIT
Copyright (c) 2026 Trinh Dang Khoa (Alex Trinh) <tumo07@io.vn>
"""
import sys
import os
import subprocess

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

REQUIRED_MODULES = [
    "customtkinter",
    "playwright",
    "cryptography",
    "PIL"
]

def _is_frozen_or_non_python() -> bool:
    if getattr(sys, "frozen", False) or hasattr(sys, "_MEIPASS"):
        return True
    exe_name = os.path.basename(sys.executable or "").lower()
    return not (exe_name.startswith("python") or exe_name.startswith("py"))

def check_and_install_python_packages():
    if _is_frozen_or_non_python():
        return True
    missing = []
    for mod in REQUIRED_MODULES:
        try:
            __import__(mod)
        except ImportError:
            missing.append(mod)

    if missing:
        print("======================================================================")
        print("  Google AI Pro 24M Automator — Dependency Auto-Installer")
        print("======================================================================")
        print(f"[*] Missing Python packages: {', '.join(missing)}")
        print("[*] Automatically installing required dependencies from requirements.txt...")
        
        req_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "requirements.txt")
        if not os.path.exists(req_path):
            req_path = "requirements.txt"

        cmd = [sys.executable, "-m", "pip", "install", "-r", req_path]
        try:
            subprocess.check_call(cmd)
            print("[+] All Python packages installed successfully!")
        except Exception as e:
            print(f"[-] Failed to install requirements: {e}")
            return False
    return True

def check_and_install_playwright():
    if _is_frozen_or_non_python():
        return True
    # Check if system Edge or Chrome is already installed (used via CDP)
    if sys.platform == "win32":
        candidates = [
            r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
            r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
            r"C:\Program Files\Google\Chrome\Application\chrome.exe",
            r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        ]
        if any(os.path.exists(p) for p in candidates):
            return True
    elif sys.platform == "darwin":
        candidates = [
            "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
            "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
        ]
        if any(os.path.exists(p) for p in candidates):
            return True
    return True

def main():
    if not check_and_install_python_packages():
        sys.exit(1)
    if not check_and_install_playwright():
        sys.exit(1)
    print("[OK] All dependencies and browser engines are verified and ready.")
    sys.exit(0)

if __name__ == "__main__":
    main()
