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
    ("PIL", "pillow>=10.0.0")
]

def _is_frozen_or_non_python() -> bool:
    """Returns True if running inside a PyInstaller/frozen binary or if sys.executable is not a Python interpreter."""
    if getattr(sys, "frozen", False) or hasattr(sys, "_MEIPASS"):
        return True
    exe_name = os.path.basename(sys.executable or "").lower()
    if not (exe_name.startswith("python") or exe_name.startswith("py")):
        return True
    return False

def auto_ensure_environment():
    # CRITICAL SAFETY GUARD: Never spawn subprocesses with sys.executable inside a frozen .exe (prevents fork bomb)
    if _is_frozen_or_non_python():
        return
    if os.environ.get("GOOGLE_AI_PRO_ENV_CHECKED") == "1":
        return
    os.environ["GOOGLE_AI_PRO_ENV_CHECKED"] = "1"

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
            req_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "requirements.txt")
            if os.path.exists(req_file):
                subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", req_file])
            else:
                subprocess.check_call([sys.executable, "-m", "pip", "install"] + missing)
            print("[+] All Python packages installed successfully!")
        except Exception as e:
            print(f"[-] Error installing Python dependencies: {e}")
            print("[-] Continuing startup...")

# Execute self-check once upon module import (no-op in frozen .exe)
auto_ensure_environment()
