"""
Google AI Pro 24M Zero-Cost Auto — Self-Healing Environment & Dependency Bootstrapper
Automatically detects, downloads, and installs any missing Python packages and Playwright
browser drivers on the fly before the main application code executes.
SPDX-License-Identifier: MIT
Copyright (c) 2026 Trinh Dang Khoa (Alex Trinh) <tumo07@io.vn>
"""
import sys
import os
import subprocess

if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

REQUIRED_PACKAGES = [
    ("playwright", "playwright>=1.40.0"),
    ("customtkinter", "customtkinter>=5.2.0"),
    ("cryptography", "cryptography>=41.0.0"),
    ("requests", "requests>=2.31.0"),
    ("fastapi", "fastapi>=0.100.0"),
    ("uvicorn", "uvicorn>=0.22.0"),
    ("pydantic", "pydantic>=2.0.0"),
    ("PIL", "pillow>=10.0.0")
]

def auto_ensure_environment():
    missing = []
    for mod_name, pkg_spec in REQUIRED_PACKAGES:
        try:
            __import__(mod_name)
        except ImportError:
            missing.append(pkg_spec)

    if missing:
        print("======================================================================")
        print("  Google AI Pro 24M Zero-Cost Auto — Auto Dependency Installer")
        print("======================================================================")
        print(f"[*] Missing dependencies detected ({len(missing)} package(s)): {', '.join(missing)}")
        print("[*] Automatically installing required packages via pip...")
        print("    Please wait a moment while packages are being installed...")
        print("----------------------------------------------------------------------")
        
        try:
            subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "pip", "--quiet"], check=False)
            req_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "requirements.txt")
            if os.path.exists(req_file):
                subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", req_file])
            else:
                subprocess.check_call([sys.executable, "-m", "pip", "install"] + missing)
            print("[+] All Python packages installed successfully!")
        except Exception as e:
            print(f"[-] Error installing Python dependencies: {e}")
            print("[-] Continuing startup...")

    # Check and install Playwright Chromium browser engine
    try:
        from playwright.sync_api import sync_playwright
        with sync_playwright() as p:
            exe = p.chromium.executable_path
            if not exe or not os.path.exists(exe):
                raise FileNotFoundError("Chromium driver not found")
    except Exception:
        print("[*] Playwright Chromium browser driver is missing.")
        print("[*] Automatically downloading Playwright Chromium (one-time setup)...")
        try:
            subprocess.check_call([sys.executable, "-m", "playwright", "install", "chromium"])
            print("[+] Playwright Chromium browser installed successfully!")
        except Exception as err:
            print(f"[-] Warning: Failed to install Playwright Chromium: {err}")

# Execute self-check immediately upon module import
auto_ensure_environment()
