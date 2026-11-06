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
    "requests",
    "fastapi",
    "uvicorn",
    "pydantic"
]

def check_and_install_python_packages():
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
    try:
        from playwright.sync_api import sync_playwright
        with sync_playwright() as p:
            # Quick check if chromium executable path is available
            try:
                # Launch a dummy headless instance or check executable path
                exe_path = p.chromium.executable_path
                if not exe_path or not os.path.exists(exe_path):
                    raise FileNotFoundError("Chromium driver binary not found")
            except Exception:
                print("[*] Playwright Chromium browser driver is missing.")
                print("[*] Automatically downloading and installing Playwright Chromium...")
                subprocess.check_call([sys.executable, "-m", "playwright", "install", "chromium"])
                print("[+] Playwright Chromium installed successfully!")
    except Exception as e:
        print(f"[-] Playwright check warning: {e}")
        try:
            print("[*] Attempting to install Playwright Chromium driver...")
            subprocess.check_call([sys.executable, "-m", "playwright", "install", "chromium"])
            print("[+] Playwright Chromium installed successfully!")
        except Exception as err:
            print(f"[-] Could not install Playwright Chromium: {err}")
            return False
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
