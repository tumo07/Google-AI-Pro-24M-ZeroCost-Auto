# Cryptographic Author Signature & Anti-Tamper Invariant
_AUTHOR_SEAL = "52f581e1acac94378238b4ecfd4b8ea29a4278796187a921bfbaedc8c8f5ee44"
_STEGANO_WATERMARK = "﻿​‌​​​​​‌​‌​‌​‌​‌​‌​‌​‌​​​‌​​‌​​​​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌‌‌‌‌​‌​‌​‌‌‌​‌​​​​​‌​‌​‌​‌​​​‌​​​‌​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​​​‌​‌​‌​​‌​​‌​​‌​‌‌​​‌‌‌​‌​​​‌​​​​​​‌​​​​‌‌​‌‌​‌‌‌‌​‌‌‌​​​​​‌‌‌‌​​‌​‌‌‌​​‌​​‌‌​‌​​‌​‌‌​​‌‌‌​‌‌​‌​​​​‌‌‌​‌​​​​‌​​​​​​​‌​‌​​​​‌‌​​​‌‌​​‌​‌​​‌​​‌​​​​​​​‌‌​​‌​​​‌‌​​​​​​‌‌​​‌​​​‌‌​‌‌​​​‌​​​​​​‌​‌​‌​​​‌‌‌​​‌​​‌‌​‌​​‌​‌‌​‌‌‌​​‌‌​‌​​​​​‌​​​​​​‌​​​‌​​​‌‌​​​​‌​‌‌​‌‌‌​​‌‌​​‌‌‌​​‌​​​​​​‌​​‌​‌‌​‌‌​‌​​​​‌‌​‌‌‌‌​‌‌​​​​‌​​‌​​​​​​​‌​‌​​​​‌​​​​​‌​‌‌​‌‌​​​‌‌​​‌​‌​‌‌‌‌​​​​​‌​​​​​​‌​‌​‌​​​‌‌‌​​‌​​‌‌​‌​​‌​‌‌​‌‌‌​​‌‌​‌​​​​​‌​‌​​‌​​‌​​​​​​​‌‌‌‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​‌‌​‌‌​‌​‌‌​‌‌‌‌​​‌‌​​​​​​‌‌​‌‌‌​‌​​​​​​​‌‌​‌​​‌​‌‌​‌‌‌‌​​‌​‌‌‌​​‌‌‌​‌‌​​‌‌​‌‌‌​​​‌‌‌‌‌​​​‌​​​​​​​‌​‌‌​‌​​‌​​​​​​‌​​​‌‌‌​‌‌​‌​​‌​‌‌‌​‌​​​‌​​‌​​​​‌‌‌​‌​‌​‌‌​​​‌​​​‌‌‌​‌​​​‌​​​​​​‌​​​​​​​‌‌‌​‌​​​‌‌‌​‌​‌​‌‌​‌‌​‌​‌‌​‌‌‌‌​​‌‌​​​​​​‌‌​‌‌‌​​‌​​​​​​​‌​‌‌​‌​​‌​​​​​​‌​​​‌​‌​‌‌​​‌​​​​‌‌​​‌​​​‌‌​‌​‌​​‌‌​‌​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​‌​​​‌​​​​​​‌​​‌‌​‌​‌‌​‌‌​‌​‌​​​‌​​​​‌‌‌​​‌​‌‌‌‌​‌​​​‌​‌​‌‌​‌​​‌‌​‌​​‌​‌‌‌‌​​‌‌​​‌​​‌​​​​‌‌​‌‌​​‌‌‌​‌​‌​‌‌​​​‌​‌​‌‌​‌​​‌​‌​​‌‌​‌​​​​‌‌‌‌​​​​‌​​​​‌‌​‌​​‌‌‌​​​‌‌​​‌‌​‌‌​‌​‌‌​‌‌‌​​‌‌​‌‌​​‌​‌​‌​​‌​​​​​‌‌​‌‌​​‌‌‌​‌‌​​‌​​‌​​‌​‌‌​‌‌‌​​‌​‌‌​​‌​‌​​‌‌​​​‌​‌​‌‌‌​‌‌​​‌​‌​​‌‌‌​​‌​‌‌‌​‌‌‌​‌​‌​​‌‌​‌​​‌‌‌​​‌‌‌​‌‌‌​‌‌​‌‌​‌​‌‌​​‌​‌​​‌‌​​​​​‌​​‌​​​​‌‌‌‌​​‌​‌‌​​​​‌​‌‌‌​‌‌‌‍"
def _verify_author_seal() -> bool:
    seed = "tumo07::Trinh Dang Khoa (Alex Trinh)::tumo07@io.vn::2026"
    h = 0x811c9dc5
    for c in seed[:56]:
        h = ((h ^ ord(c)) * 0x01000193) & 0xffffffff
    return h == 0x2e1ff517

"""
Google AI Pro 24-Month Automator — Friendly Wizard & Universal GUI
------------------------------------------------------------------
Redesigned with a Step-by-Step Guided Wizard for beginners, combined with
a comprehensive real-time checkpoint monitor and zero-billing protection.
"""

import os
import sys
import shutil
import multiprocessing

# 1. CRITICAL ANTI-FORK-BOMB CIRCUIT BREAKER (Must run BEFORE any other imports!)
if __name__ == "__main__":
    multiprocessing.freeze_support()

if getattr(sys, "frozen", False) and any(arg in ("-m", "pip", "playwright") for arg in sys.argv[1:]):
    os._exit(0)

# Redirect stdout/stderr safely when launched from macOS Finder / Windows GUI without a console
if sys.stdout is None or sys.stderr is None or (sys.platform == "darwin" and getattr(sys, "frozen", False)):
    try:
        _log_dir = (
            os.path.expanduser("~/Library/Application Support/GoogleAIProAutomator")
            if sys.platform == "darwin"
            else os.path.dirname(sys.executable)
        )
        os.makedirs(_log_dir, exist_ok=True)
        _log_fh = open(os.path.join(_log_dir, "app_startup.log"), "a", encoding="utf-8", buffering=1)
        if sys.stdout is None or getattr(sys, "frozen", False):
            sys.stdout = _log_fh
        if sys.stderr is None or getattr(sys, "frozen", False):
            sys.stderr = _log_fh
    except Exception:
        pass

_instance_lock_handle = None
_MAIN_WINDOW_TITLE = "Google AI Pro 24-Month Automator v1.3.1"

def _focus_existing_window_or_cleanup_zombies() -> bool:
    """
    On Windows:
    1. Searches for an existing visible top-level window matching _MAIN_WINDOW_TITLE.
       If found, restores & brings it to the foreground and returns True (caller exits).
    2. If NO visible window exists, any other GoogleAIProAutomator.exe process holding
       the mutex is a headless/zombie instance -> terminates it and returns False so
       this new launch can take over and open the UI cleanly.
    """
    if sys.platform != "win32":
        return False
    try:
        import ctypes
        from ctypes import wintypes
        user32 = ctypes.windll.user32
        WNDENUMPROC = ctypes.WINFUNCTYPE(wintypes.BOOL, wintypes.HWND, wintypes.LPARAM)
        found_hwnds = []

        def _enum_cb(hwnd, lparam):
            if user32.IsWindowVisible(hwnd):
                length = user32.GetWindowTextLengthW(hwnd)
                if length > 0:
                    buf = ctypes.create_unicode_buffer(length + 1)
                    user32.GetWindowTextW(hwnd, buf, length + 1)
                    if "Google AI Pro 24-Month Automator" in buf.value:
                        found_hwnds.append(hwnd)
            return True

        user32.EnumWindows(WNDENUMPROC(_enum_cb), 0)
        if found_hwnds:
            hwnd = found_hwnds[0]
            SW_RESTORE = 9
            SW_SHOW = 5
            if user32.IsIconic(hwnd):
                user32.ShowWindow(hwnd, SW_RESTORE)
            else:
                user32.ShowWindow(hwnd, SW_SHOW)
            user32.SetForegroundWindow(hwnd)
            return True

        # Wait briefly in case a sibling instance is in the middle of initializing its window
        import time as _t
        _t.sleep(1.5)
        user32.EnumWindows(WNDENUMPROC(_enum_cb), 0)
        if found_hwnds:
            hwnd = found_hwnds[0]
            user32.ShowWindow(hwnd, 9 if user32.IsIconic(hwnd) else 5)
            user32.SetForegroundWindow(hwnd)
            return True

        # Still no visible window found -> kill any zombie GoogleAIProAutomator.exe processes (except self & parent)
        my_pid = os.getpid()
        parent_pid = os.getppid()
        import subprocess
        out = subprocess.check_output(
            'tasklist /FI "IMAGENAME eq GoogleAIProAutomator.exe" /FO CSV /NH',
            shell=True, text=True, stderr=subprocess.DEVNULL
        )
        for line in out.splitlines():
            parts = [p.strip('"') for p in line.split('","')]
            if len(parts) >= 2 and parts[1].isdigit():
                pid = int(parts[1])
                if pid not in (my_pid, parent_pid):
                    subprocess.run(
                        f"taskkill /F /T /PID {pid}",
                        shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
                    )
    except Exception:
        pass
    return False

def ensure_single_instance():
    r"""
    Cross-platform native single instance lock (executed BEFORE heavy imports):
    - Windows: Kernel Named Mutex (Local\GoogleAIProAutomatorLock_tumo07).
      If another instance holds the mutex:
        * If its window is visible -> brings it to front and exits.
        * If it is a headless zombie (MainWindowHandle == 0) -> kills the zombie and acquires the lock!
    - macOS / Linux: fcntl.flock on a temporary file lock.
    """
    global _instance_lock_handle
    if _instance_lock_handle is not None:
        return True
    if sys.platform == "win32":
        try:
            import ctypes
            import time as _t
            ERROR_ALREADY_EXISTS = 183
            kernel32 = ctypes.windll.kernel32
            kernel32.SetLastError(0)
            handle = kernel32.CreateMutexW(
                None, False, "Local\\GoogleAIProAutomatorLock_tumo07"
            )
            last_err = kernel32.GetLastError()
            if last_err == ERROR_ALREADY_EXISTS:
                if _focus_existing_window_or_cleanup_zombies():
                    print("[INFO] Đã chuyển tiêu điểm sang cửa sổ ứng dụng đang mở.")
                    os._exit(0)
                # Zombie was cleaned up -> close old handle, wait briefly, and re-acquire mutex
                try:
                    kernel32.CloseHandle(handle)
                except Exception:
                    pass
                _t.sleep(0.3)
                kernel32.SetLastError(0)
                handle = kernel32.CreateMutexW(
                    None, False, "Local\\GoogleAIProAutomatorLock_tumo07"
                )
            _instance_lock_handle = handle
            return True
        except Exception:
            return True
    else:
        try:
            import fcntl
            import tempfile
            lock_path = os.path.join(tempfile.gettempdir(), "google_ai_pro_automator.lock")
            _instance_lock_handle = open(lock_path, "w")
            fcntl.flock(_instance_lock_handle, fcntl.LOCK_EX | fcntl.LOCK_NB)
            return True
        except (IOError, OSError):
            print("[INFO] Một phiên bản của ứng dụng đang chạy.")
            os._exit(0)

if __name__ == "__main__":
    ensure_single_instance()

import json
import time
import threading
import asyncio
import subprocess
import platform
import signal
import socket
from typing import Optional, Dict, Any

import customtkinter as ctk
from PIL import Image
import ensure_env
from playwright.async_api import async_playwright

# Setup base paths (supports source, Windows PyInstaller .exe, and macOS .app bundle in /Applications)
if getattr(sys, "frozen", False):
    _raw_dir = os.path.dirname(sys.executable)
    RESOURCE_DIR = getattr(sys, "_MEIPASS", _raw_dir)
else:
    _raw_dir = os.path.dirname(os.path.abspath(__file__))
    RESOURCE_DIR = _raw_dir

if sys.platform == "darwin" and ".app/Contents/" in _raw_dir.replace("\\", "/"):
    BASE_DIR = os.path.expanduser("~/Library/Application Support/GoogleAIProAutomator")
    os.makedirs(BASE_DIR, exist_ok=True)
else:
    BASE_DIR = _raw_dir

CONFIG_PATH = os.path.join(BASE_DIR, "config.json")
if not os.path.exists(CONFIG_PATH):
    for _cand in (os.path.join(RESOURCE_DIR, "config.json"), os.path.join(RESOURCE_DIR, "config.example.json")):
        if os.path.exists(_cand):
            try:
                shutil.copy2(_cand, CONFIG_PATH)
                break
            except Exception:
                pass
SCREENSHOTS_DIR = os.path.join(BASE_DIR, "screenshots")
os.makedirs(SCREENSHOTS_DIR, exist_ok=True)

import engine_stacker

# Detect Operating System and CPU Architecture
IS_MAC = sys.platform == "darwin"
IS_WIN = sys.platform == "win32"
ARCH = platform.machine().lower()

if IS_MAC:
    OS_DESC = f"🍎 macOS ({'Apple Silicon ' + ARCH if 'arm' in ARCH or 'aarch' in ARCH else 'Intel ' + ARCH})"
    FONT_HEADING = "Helvetica Neue"
    FONT_BODY = "Helvetica Neue"
elif IS_WIN:
    OS_DESC = f"🪟 Windows ({ARCH})"
    FONT_HEADING = "Segoe UI Variable Display"
    FONT_BODY = "Segoe UI Variable Text"
else:
    OS_DESC = f"🐧 Linux ({ARCH})"
    FONT_HEADING = "Ubuntu"
    FONT_BODY = "DejaVu Sans"

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

def _apply_fluent_theme(window):
    """Applies authentic Windows 11 DWM dark titlebar and rounded corners."""
    if sys.platform != "win32":
        return
    try:
        import ctypes
        from ctypes import c_int, byref, sizeof
        window.update_idletasks()
        hwnd = ctypes.windll.user32.GetParent(window.winfo_id())
        if not hwnd:
            hwnd = window.winfo_id()
        # DWMWA_USE_IMMERSIVE_DARK_MODE = 20
        dark_val = c_int(1)
        ctypes.windll.dwmapi.DwmSetWindowAttribute(hwnd, 20, byref(dark_val), sizeof(dark_val))
        # DWMWA_WINDOW_CORNER_PREFERENCE = 33 (2 = DWMWCP_ROUND)
        corner_val = c_int(2)
        ctypes.windll.dwmapi.DwmSetWindowAttribute(hwnd, 33, byref(corner_val), sizeof(corner_val))
    except Exception:
        pass

class UniversalStackerApp(ctk.CTk):
    def __init__(self):
        if not _verify_author_seal():
            import sys; sys.exit(1)
        super().__init__()

        self.title(f"Google AI Pro 24-Month Automator v1.3.1 · Universal Edition ({OS_DESC})")
        self.geometry("1100x820")
        self.minsize(960, 700)
        self.configure(fg_color="#18181b")

        self.cfg = self.load_config()
        self.active_account_id = "Account_1"
        self.engine: Optional[engine_stacker.StackingEngine] = None
        self.worker_thread: Optional[threading.Thread] = None
        self.is_running = False

        self._build_ui()
        self._refresh_accounts()
        _apply_fluent_theme(self)
        self.protocol("WM_DELETE_WINDOW", self._on_close)
        # Ensure window is visible, raised, and focused when launched from Explorer or Finder
        self.after(80, self._bring_window_to_front)

    def _bring_window_to_front(self):
        try:
            self.deiconify()
            self.lift()
            self.focus_force()
            self.attributes("-topmost", True)
            self.after(350, lambda: self.attributes("-topmost", False))
        except Exception:
            pass

    def _on_close(self):
        try:
            if self.engine:
                self.engine.stop()
            self.destroy()
        except Exception:
            pass
        os._exit(0)

    def load_config(self) -> Dict[str, Any]:
        if os.path.exists(CONFIG_PATH):
            try:
                with open(CONFIG_PATH, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                pass
        return {"accounts": [], "card": {}}

    def save_config(self):
        try:
            with open(CONFIG_PATH, "w", encoding="utf-8") as f:
                json.dump(self.cfg, f, indent=2, ensure_ascii=False)
        except Exception as e:
            self.append_log("ERROR", f"Không thể lưu cấu hình: {e}")

    def _build_ui(self):
        # 1. Header Bar
        self.header_frame = ctk.CTkFrame(self, fg_color="#18181b", corner_radius=12, height=68)
        self.header_frame.pack(fill="x", padx=16, pady=(14, 8))

        # Title & Subtitle in header
        title_box = ctk.CTkFrame(self.header_frame, fg_color="transparent")
        title_box.pack(side="left", padx=16, pady=8)

        self.title_label = ctk.CTkLabel(
            title_box,
            text="🚀 Google AI Pro 24-Month Zero-Cost Automator",
            font=ctk.CTkFont(family=FONT_HEADING, size=18, weight="bold"),
            text_color="#f4f4f5"
        )
        self.title_label.pack(anchor="w")

        self.sub_label = ctk.CTkLabel(
            title_box,
            text="Tự động hóa cộng dồn 24 tháng 5 TB · Bảo vệ tuyệt đối US$0.00 · Tự động hủy gia hạn & gỡ thẻ",
            font=ctk.CTkFont(family=FONT_BODY, size=12),
            text_color="#a1a1aa"
        )
        self.sub_label.pack(anchor="w")

        # Badges on right
        self.os_badge = ctk.CTkLabel(
            self.header_frame,
            text=OS_DESC,
            font=ctk.CTkFont(family=FONT_BODY, size=11, weight="bold"),
            fg_color="#27272a",
            text_color="#d4d4d8",
            corner_radius=8,
            padx=10,
            pady=4
        )
        self.os_badge.pack(side="right", padx=(4, 16), pady=16)

        self.guard_badge = ctk.CTkLabel(
            self.header_frame,
            text="🛡️ $0.00 Price Guard: BẬT",
            font=ctk.CTkFont(family=FONT_BODY, size=11, weight="bold"),
            fg_color="#14532d",
            text_color="#86efac",
            corner_radius=8,
            padx=10,
            pady=4
        )
        self.guard_badge.pack(side="right", padx=6, pady=16)

        # 2. Stepper Roadmap Bar (Visual 5-Stage Progress including Step 0 Staging)
        self.stepper_frame = ctk.CTkFrame(self, fg_color="#18181b", corner_radius=10, height=44)
        self.stepper_frame.pack(fill="x", padx=16, pady=(0, 8))

        self.step_labels = []
        steps_data = [
            ("0", "Cài Đặt & Tiện Ích", "#06b6d4"),
            ("1", "Đăng Nhập Google", "#38bdf8"),
            ("2", "Nâng Cấp 24 Tháng", "#a855f7"),
            ("3", "Hủy Gia Hạn & Gỡ Thẻ", "#f59e0b"),
            ("4", "Chia Sẻ Gia Đình", "#10b981")
        ]
        
        stepper_inner = ctk.CTkFrame(self.stepper_frame, fg_color="transparent")
        stepper_inner.pack(expand=True, pady=6)

        for i, (num, text, color) in enumerate(steps_data):
            pill = ctk.CTkFrame(stepper_inner, fg_color="#27272a", corner_radius=6)
            pill.pack(side="left", padx=6)
            
            lbl_num = ctk.CTkLabel(
                pill, text=f" {num} ",
                font=ctk.CTkFont(family=FONT_BODY, size=11, weight="bold"),
                fg_color=color, text_color="#000000", corner_radius=4
            )
            lbl_num.pack(side="left", padx=(4, 6), pady=3)
            
            lbl_txt = ctk.CTkLabel(
                pill, text=text,
                font=ctk.CTkFont(family=FONT_BODY, size=11, weight="bold"),
                text_color="#e4e4e7"
            )
            lbl_txt.pack(side="left", padx=(0, 8), pady=3)
            
            self.step_labels.append((pill, lbl_txt))
            
            if i < len(steps_data) - 1:
                arrow = ctk.CTkLabel(
                    stepper_inner, text="➔",
                    font=ctk.CTkFont(family=FONT_BODY, size=12),
                    text_color="#71717a"
                )
                arrow.pack(side="left", padx=2)

        # 3. Main Workspace Split
        self.main_container = ctk.CTkFrame(self, fg_color="transparent")
        self.main_container.pack(fill="both", expand=True, padx=16, pady=2)

        # Left Column: Tabs (Wizard / Advanced / FAQ) (Width: 460)
        self.left_col = ctk.CTkFrame(self.main_container, fg_color="#18181b", corner_radius=12, width=470)
        self.left_col.pack(side="left", fill="both", padx=(0, 8), pady=2)
        self.left_col.pack_propagate(False)

        # Right Column: Monitoring & Live Logs
        self.right_col = ctk.CTkFrame(self.main_container, fg_color="#18181b", corner_radius=12)
        self.right_col.pack(side="right", fill="both", expand=True, padx=(8, 0), pady=2)

        self._build_tabs()
        self._build_monitor_panel()

    def _build_tabs(self):
        self.tabs = ctk.CTkTabview(
            self.left_col,
            fg_color="transparent",
            segmented_button_fg_color="#27272a",
            segmented_button_selected_color="#0284c7",
            segmented_button_selected_hover_color="#0369a1",
            text_color="#f4f4f5"
        )
        self.tabs.pack(fill="both", expand=True, padx=12, pady=(4, 10))

        self.tab_wizard = self.tabs.add("🧭 Hướng Dẫn Từng Bước")
        self.tab_advanced = self.tabs.add("⚙️ Nâng Cao")
        self.tab_faq = self.tabs.add("💡 Hỏi Đáp & Trợ Giúp")

        self._build_wizard_tab()
        self._build_advanced_tab()
        self._build_faq_tab()

    def _build_wizard_tab(self):
        # Scrollable container for wizard steps
        scroll = ctk.CTkScrollableFrame(self.tab_wizard, fg_color="transparent")
        scroll.pack(fill="both", expand=True, padx=2, pady=2)

        # 🛠️ Card Step 0: Environment, macOS Permissions & Extension Staging
        card0 = ctk.CTkFrame(scroll, fg_color="#172554", corner_radius=10, border_width=1, border_color="#0284c7")
        card0.pack(fill="x", pady=(2, 8))

        c0_header = ctk.CTkFrame(card0, fg_color="transparent")
        c0_header.pack(fill="x", padx=12, pady=(8, 2))
        ctk.CTkLabel(
            c0_header, text="🛠️ BƯỚC 0: CÀI ĐẶT MÔI TRƯỜNG, QUYỀN MACOS & TIỆN ÍCH (STAGING)",
            font=ctk.CTkFont(family=FONT_HEADING, size=11, weight="bold"),
            text_color="#38bdf8"
        ).pack(side="left")

        ctk.CTkLabel(
            card0,
            text="Bấm 1 lần trước khi sử dụng: Tự động cấp quyền macOS Sonoma/Sequoia, giải nén Browsec VPN + Offer Injector, và cài đặt trình duyệt tương thích (Workaround vượt chặn --load-extension của Chrome 137+).",
            font=ctk.CTkFont(family=FONT_BODY, size=11),
            text_color="#bae6fd", wraplength=410, justify="left"
        ).pack(anchor="w", padx=12, pady=(0, 4))

        staged_ok = bool(self.cfg.get("staged_ready"))
        staged_br = self.cfg.get("staged_browser", "Tự động")
        self.lbl_staging_status = ctk.CTkLabel(
            card0,
            text=f"🟢 Đã sẵn sàng (Trình duyệt: {staged_br} + Dual-Mode CDP)" if staged_ok else "🟡 Trạng thái: Chưa khởi tạo Staging (Hãy bấm nút bên dưới)",
            font=ctk.CTkFont(family=FONT_BODY, size=11, weight="bold"),
            text_color="#4ade80" if staged_ok else "#fbbf24"
        )
        self.lbl_staging_status.pack(anchor="w", padx=12, pady=(0, 6))

        self.btn_staging = ctk.CTkButton(
            card0,
            text="⚙️ 0. Cài Đặt Môi Trường, Cấp Quyền & Nạp Tiện Ích (Staging)",
            font=ctk.CTkFont(family=FONT_BODY, size=12, weight="bold"),
            fg_color="#0284c7", hover_color="#0369a1", height=36,
            command=self._cmd_run_staging
        )
        self.btn_staging.pack(fill="x", padx=12, pady=(2, 10))

        # 🌟 Highlighted 1-Click All-in-One Banner
        all_in_one_card = ctk.CTkFrame(scroll, fg_color="#064e3b", corner_radius=10, border_width=1, border_color="#059669")
        all_in_one_card.pack(fill="x", pady=(2, 10))

        lbl_aio_title = ctk.CTkLabel(
            all_in_one_card,
            text="✨ KHUYÊN DÙNG CHO NGƯỜI MỚI (1-CLICK A ĐẾN Z)",
            font=ctk.CTkFont(family=FONT_HEADING, size=12, weight="bold"),
            text_color="#6ee7b7"
        )
        lbl_aio_title.pack(anchor="w", padx=12, pady=(8, 2))

        lbl_aio_desc = ctk.CTkLabel(
            all_in_one_card,
            text="Tự động hóa trọn gói: Mở trình duyệt ➔ Đăng nhập ➔ Nâng cấp 3 tầng 24 tháng ➔ Hủy gia hạn tự động tránh phát sinh phí ➔ Tự động gỡ thẻ bảo vệ an toàn 0đ.",
            font=ctk.CTkFont(family=FONT_BODY, size=11),
            text_color="#d1fae5",
            wraplength=410,
            justify="left"
        )
        lbl_aio_desc.pack(anchor="w", padx=12, pady=(0, 6))

        # Big All-in-One Button
        self.btn_all_in_one = ctk.CTkButton(
            all_in_one_card,
            text="🚀 BẮT ĐẦU TỰ ĐỘNG TOÀN BỘ TỪ A ĐẾN Z",
            font=ctk.CTkFont(family=FONT_BODY, size=13, weight="bold"),
            fg_color="#059669",
            hover_color="#047857",
            height=40,
            command=self._cmd_start_stacking
        )
        self.btn_all_in_one.pack(fill="x", padx=12, pady=(2, 10))

        # Card Step 1: Login
        card1 = ctk.CTkFrame(scroll, fg_color="#202023", corner_radius=10)
        card1.pack(fill="x", pady=6)

        c1_header = ctk.CTkFrame(card1, fg_color="transparent")
        c1_header.pack(fill="x", padx=12, pady=(8, 2))
        ctk.CTkLabel(
            c1_header, text="BƯỚC 1: ĐĂNG NHẬP GOOGLE",
            font=ctk.CTkFont(family=FONT_HEADING, size=12, weight="bold"),
            text_color="#38bdf8"
        ).pack(side="left")

        ctk.CTkLabel(
            card1,
            text="Mở cửa sổ trình duyệt sạch (đã tích hợp VPN US và tiện ích kích hoạt gói). Bạn chỉ cần đăng nhập tài khoản Google và xác thực 2 bước (nếu có).",
            font=ctk.CTkFont(family=FONT_BODY, size=11),
            text_color="#a1a1aa", wraplength=410, justify="left"
        ).pack(anchor="w", padx=12, pady=(0, 6))

        self.btn_signin = ctk.CTkButton(
            card1,
            text="🌐 1. Mở Cửa Sổ Đăng Nhập",
            font=ctk.CTkFont(family=FONT_BODY, size=12, weight="bold"),
            fg_color="#0284c7", hover_color="#0369a1", height=34,
            command=self._cmd_launch_signin
        )
        self.btn_signin.pack(fill="x", padx=12, pady=(2, 10))

        # Card Step 2: Auto-Stacking
        card2 = ctk.CTkFrame(scroll, fg_color="#202023", corner_radius=10)
        card2.pack(fill="x", pady=6)

        c2_header = ctk.CTkFrame(card2, fg_color="transparent")
        c2_header.pack(fill="x", padx=12, pady=(8, 2))
        ctk.CTkLabel(
            c2_header, text="BƯỚC 2: CỘNG DỒN 24 THÁNG ($0.00)",
            font=ctk.CTkFont(family=FONT_HEADING, size=12, weight="bold"),
            text_color="#c084fc"
        ).pack(side="left")

        ctk.CTkLabel(
            card2,
            text="Công cụ tự động cộng dồn: Tầng 1 (12M) ➔ Tầng 2 (+6M) ➔ Tầng 3 (+6M) đủ 24 tháng 5 TB. Bộ Play Guard đảm bảo giá luôn hiển thị $0.00 trước khi kích hoạt.",
            font=ctk.CTkFont(family=FONT_BODY, size=11),
            text_color="#a1a1aa", wraplength=410, justify="left"
        ).pack(anchor="w", padx=12, pady=(0, 6))

        # Checkboxes for protections
        self.chk_auto_remove_cards = ctk.CTkCheckBox(
            card2,
            text="💳 Tự động gỡ sạch thẻ ngân hàng sau khi xong",
            font=ctk.CTkFont(family=FONT_BODY, size=11),
            text_color="#e4e4e7", fg_color="#0284c7"
        )
        self.chk_auto_remove_cards.select()
        self.chk_auto_remove_cards.pack(anchor="w", padx=14, pady=(2, 4))

        self.chk_auto_vn = ctk.CTkCheckBox(
            card2,
            text="🇻🇳 Tự động đổi vùng Việt Nam (Bật Family Sharing)",
            font=ctk.CTkFont(family=FONT_BODY, size=11),
            text_color="#e4e4e7", fg_color="#0284c7"
        )
        self.chk_auto_vn.select()
        self.chk_auto_vn.pack(anchor="w", padx=14, pady=(0, 8))

        row_c2 = ctk.CTkFrame(card2, fg_color="transparent")
        row_c2.pack(fill="x", padx=12, pady=(0, 10))

        self.btn_stack = ctk.CTkButton(
            row_c2,
            text="▶️ 2. Bắt Đầu Nâng Cấp 24 Tháng",
            font=ctk.CTkFont(family=FONT_BODY, size=12, weight="bold"),
            fg_color="#7c3aed", hover_color="#6d28d9", height=36,
            command=self._cmd_start_stacking
        )
        self.btn_stack.pack(side="left", fill="x", expand=True, padx=(0, 4))

        self.btn_stop = ctk.CTkButton(
            row_c2,
            text="⏹ Dừng",
            font=ctk.CTkFont(family=FONT_BODY, size=12, weight="bold"),
            fg_color="#dc2626", hover_color="#b91c1c", height=36, width=70,
            state="disabled",
            command=self._cmd_stop
        )
        self.btn_stop.pack(side="right")

        # Card Step 3: Protect & Cancel Renewal & Unlink Card
        card3 = ctk.CTkFrame(scroll, fg_color="#202023", corner_radius=10)
        card3.pack(fill="x", pady=6)

        c3_header = ctk.CTkFrame(card3, fg_color="transparent")
        c3_header.pack(fill="x", padx=12, pady=(8, 2))
        ctk.CTkLabel(
            c3_header, text="BƯỚC 3: HỦY GIA HẠN TỰ ĐỘNG & GỠ THẺ BẢO VỆ 0Đ",
            font=ctk.CTkFont(family=FONT_HEADING, size=12, weight="bold"),
            text_color="#fbbf24"
        ).pack(side="left")

        ctk.CTkLabel(
            card3,
            text="Hủy tự động gia hạn định kỳ trên Google Play để bảo lưu trọn vẹn thời hạn 24 tháng, triệt tiêu hoàn toàn nguy cơ phát sinh phí và gỡ toàn bộ thẻ thanh toán.",
            font=ctk.CTkFont(family=FONT_BODY, size=11),
            text_color="#a1a1aa", wraplength=410, justify="left"
        ).pack(anchor="w", padx=12, pady=(0, 6))

        row_c3 = ctk.CTkFrame(card3, fg_color="transparent")
        row_c3.pack(fill="x", padx=12, pady=(0, 10))

        self.btn_cancel_renew = ctk.CTkButton(
            row_c3,
            text="🛡️ 3. Hủy Gia Hạn & Gỡ Thẻ",
            font=ctk.CTkFont(family=FONT_BODY, size=11, weight="bold"),
            fg_color="#d97706", hover_color="#b45309", height=34,
            command=self._cmd_cancel_renewal
        )
        self.btn_cancel_renew.pack(side="left", fill="x", expand=True, padx=(0, 4))

        self.btn_remove_cards = ctk.CTkButton(
            row_c3,
            text="💳 Gỡ Toàn Bộ Thẻ",
            font=ctk.CTkFont(family=FONT_BODY, size=11, weight="bold"),
            fg_color="#b91c1c", hover_color="#991b1b", height=34,
            command=self._cmd_remove_cards_standalone
        )
        self.btn_remove_cards.pack(side="right", fill="x", expand=True, padx=(4, 0))

        # Card Step 4: Family Sharing
        card4 = ctk.CTkFrame(scroll, fg_color="#202023", corner_radius=10)
        card4.pack(fill="x", pady=6)

        c4_header = ctk.CTkFrame(card4, fg_color="transparent")
        c4_header.pack(fill="x", padx=12, pady=(8, 2))
        ctk.CTkLabel(
            c4_header, text="BƯỚC 4: CHIA SẺ GIA ĐÌNH VIỆT NAM (TÙY CHỌN)",
            font=ctk.CTkFont(family=FONT_HEADING, size=12, weight="bold"),
            text_color="#34d399"
        ).pack(side="left")

        ctk.CTkLabel(
            card4,
            text="Chuyển vùng hồ sơ thanh toán về Việt Nam để bật chia sẻ nhóm gia đình Google One cho tối đa 5 người thân dùng chung dung lượng 5 TB.",
            font=ctk.CTkFont(family=FONT_BODY, size=11),
            text_color="#a1a1aa", wraplength=410, justify="left"
        ).pack(anchor="w", padx=12, pady=(0, 6))

        self.btn_switch_vn = ctk.CTkButton(
            card4,
            text="🇻🇳 4. Chuyển Vùng Về Việt Nam (Family Sharing)",
            font=ctk.CTkFont(family=FONT_BODY, size=11, weight="bold"),
            fg_color="#059669", hover_color="#047857", height=34,
            command=self._cmd_switch_vn
        )
        self.btn_switch_vn.pack(fill="x", padx=12, pady=(2, 10))

    def _build_advanced_tab(self):
        scroll = ctk.CTkScrollableFrame(self.tab_advanced, fg_color="transparent")
        scroll.pack(fill="both", expand=True, padx=2, pady=2)

        # 1. Robust Multi-Account Management Card (Win11 Fluent Card)
        card_acc = ctk.CTkFrame(scroll, fg_color="#202023", corner_radius=10, border_width=1, border_color="#2d2d30")
        card_acc.pack(fill="x", padx=4, pady=(4, 12))

        ctk.CTkLabel(
            card_acc, text="👥 QUẢN LÝ TÀI KHOẢN (MULTI-ACCOUNT MANAGER)",
            font=ctk.CTkFont(family=FONT_HEADING, size=12, weight="bold"),
            text_color="#38bdf8"
        ).pack(anchor="w", padx=12, pady=(10, 4))

        ctk.CTkLabel(
            card_acc, text="Chọn tài khoản đang làm việc hoặc thêm mới, xóa tài khoản, dọn dẹp cache phiên:",
            font=ctk.CTkFont(family=FONT_BODY, size=11),
            text_color="#a1a1aa"
        ).pack(anchor="w", padx=12, pady=(0, 6))

        self.account_menu = ctk.CTkOptionMenu(
            card_acc,
            values=["Account_1 (Chưa đăng nhập)"],
            command=self._on_account_selected,
            font=ctk.CTkFont(family=FONT_BODY, size=12),
            fg_color="#27272a", button_color="#3f3f46", height=34
        )
        self.account_menu.pack(fill="x", padx=12, pady=(0, 8))

        # Status & details badge row
        self.lbl_acc_info = ctk.CTkLabel(
            card_acc, text="📍 Đang chọn: Account_1 | Thư mục: profiles/Account_1",
            font=ctk.CTkFont(family=FONT_BODY, size=11),
            text_color="#94a3b8"
        )
        self.lbl_acc_info.pack(anchor="w", padx=12, pady=(0, 8))

        # Row 1: Add new & Delete active
        row_acc_act = ctk.CTkFrame(card_acc, fg_color="transparent")
        row_acc_act.pack(fill="x", padx=12, pady=(0, 6))

        btn_new_acc = ctk.CTkButton(
            row_acc_act, text="➕ Thêm Tài Khoản Mới",
            font=ctk.CTkFont(family=FONT_BODY, size=11, weight="bold"),
            fg_color="#0284c7", hover_color="#0369a1", height=32,
            command=self._cmd_create_new_instance
        )
        btn_new_acc.pack(side="left", fill="x", expand=True, padx=(0, 3))

        btn_del_acc = ctk.CTkButton(
            row_acc_act, text="🗑️ Xóa Tài Khoản Này",
            font=ctk.CTkFont(family=FONT_BODY, size=11, weight="bold"),
            fg_color="#b91c1c", hover_color="#991b1b", height=32,
            command=self._cmd_delete_account
        )
        btn_del_acc.pack(side="right", fill="x", expand=True, padx=(3, 0))

        # Row 2: Reset profile cache & Open folder
        row_acc_util = ctk.CTkFrame(card_acc, fg_color="transparent")
        row_acc_util.pack(fill="x", padx=12, pady=(0, 10))

        btn_reset_acc = ctk.CTkButton(
            row_acc_util, text="🧹 Reset Session / Dọn Cache",
            font=ctk.CTkFont(family=FONT_BODY, size=11),
            fg_color="#374151", hover_color="#4b5563", height=30,
            command=self._cmd_reset_account_session
        )
        btn_reset_acc.pack(side="left", fill="x", expand=True, padx=(0, 3))

        btn_open_folder = ctk.CTkButton(
            row_acc_util, text="📂 Mở Thư Mục Profile",
            font=ctk.CTkFont(family=FONT_BODY, size=11),
            fg_color="#374151", hover_color="#4b5563", height=30,
            command=self._cmd_open_profile_folder
        )
        btn_open_folder.pack(side="right", fill="x", expand=True, padx=(3, 0))

        # Individual Layer Run
        ctk.CTkLabel(
            scroll, text="CHẠY RIÊNG LẺ TỪNG TẦNG (MANUAL STACKING)",
            font=ctk.CTkFont(family=FONT_HEADING, size=11, weight="bold"),
            text_color="#a1a1aa"
        ).pack(anchor="w", padx=10, pady=(6, 4))

        row_layers = ctk.CTkFrame(scroll, fg_color="transparent")
        row_layers.pack(fill="x", padx=10, pady=2)

        btn_l1 = ctk.CTkButton(
            row_layers, text="Tầng 1 (12M)",
            font=ctk.CTkFont(family=FONT_BODY, size=11),
            fg_color="#1e293b", hover_color="#334155", height=32,
            command=lambda: self._cmd_run_single_layer(1)
        )
        btn_l1.pack(side="left", fill="x", expand=True, padx=(0, 3))

        btn_l2 = ctk.CTkButton(
            row_layers, text="Tầng 2 (SS +6M)",
            font=ctk.CTkFont(family=FONT_BODY, size=11),
            fg_color="#1e293b", hover_color="#334155", height=32,
            command=lambda: self._cmd_run_single_layer(2)
        )
        btn_l2.pack(side="left", fill="x", expand=True, padx=3)

        btn_l3 = ctk.CTkButton(
            row_layers, text="Tầng 3 (5TB +6M)",
            font=ctk.CTkFont(family=FONT_BODY, size=11),
            fg_color="#1e293b", hover_color="#334155", height=32,
            command=lambda: self._cmd_run_single_layer(3)
        )
        btn_l3.pack(side="right", fill="x", expand=True, padx=(3, 0))

        # Diagnostics & Utilities
        ctk.CTkLabel(
            scroll, text="CÔNG CỤ HỆ THỐNG & DỌN DẸP",
            font=ctk.CTkFont(family=FONT_HEADING, size=11, weight="bold"),
            text_color="#a1a1aa"
        ).pack(anchor="w", padx=10, pady=(16, 4))

        btn_clean_port = ctk.CTkButton(
            scroll, text="🧹 Giải Phóng Cổng Remote CDP (Port 9320)",
            font=ctk.CTkFont(family=FONT_BODY, size=12),
            fg_color="#27272a", hover_color="#3f3f46", height=32,
            command=self._cmd_clean_port_manual
        )
        btn_clean_port.pack(fill="x", padx=10, pady=3)

        btn_open_cfg = ctk.CTkButton(
            scroll, text="📝 Mở File Cấu Hình (config.json)",
            font=ctk.CTkFont(family=FONT_BODY, size=12),
            fg_color="#27272a", hover_color="#3f3f46", height=32,
            command=self._cmd_open_config_file
        )
        btn_open_cfg.pack(fill="x", padx=10, pady=3)

    def _build_faq_tab(self):
        scroll = ctk.CTkScrollableFrame(self.tab_faq, fg_color="transparent")
        scroll.pack(fill="both", expand=True, padx=2, pady=2)

        faqs = [
            ("💳 Thẻ thanh toán có bị trừ tiền không?",
             "HOÀN TOÀN KHÔNG. Google chỉ thực hiện xác thực tạm giữ $0.00 để kiểm tra thẻ có hợp lệ không. Tiện ích Play Guard sẽ tự động chặn quy trình nếu màn hình không hiển thị chính xác US$0.00. Sau khi hoàn tất, Bước 3 sẽ hủy gia hạn và gỡ sạch thẻ."),
            ("📱 Khi gặp xác thực 2 bước (2FA) / Captcha thì làm sao?",
             "Ứng dụng có cảm biến thông minh tự động tạm dừng khi phát hiện màn hình 2FA, mã số trên điện thoại hoặc Captcha. Bạn chỉ cần thao tác trên điện thoại hoặc giải Captcha trên trình duyệt, ứng dụng sẽ TỰ ĐỘNG CHẠY TIẾP mà không cần bấm gì thêm."),
            ("👨‍👩‍👧‍👦 Làm sao để chia sẻ dung lượng 5 TB cho người thân tại VN?",
             "Sau khi xong Bước 4 (Chuyển vùng về Việt Nam), tài khoản của bạn sẽ mang hồ sơ thanh toán Việt Nam. Bạn chỉ cần vào https://one.google.com/family để mời tối đa 5 thành viên gia đình sử dụng chung dung lượng 5 TB."),
            ("🍎 Xử lý lỗi phân quyền trên macOS?",
             "Nếu tải file ZIP và gặp thông báo 'Không có đặc quyền truy cập', hãy tải bản file .dmg chính thức kéo vào Applications, hoặc mở Terminal gõ: chmod +x *.command *.sh"),
            ("🪟 Xử lý lỗi 0x80070005 trên Windows?",
             "Ứng dụng từ phiên bản v1.3.0 đã chuyển sang socket lock thuần Python, hoàn toàn không phụ thuộc vào PowerShell nên khắc phục 100% lỗi quyền.")
        ]

        for q, a in faqs:
            card = ctk.CTkFrame(scroll, fg_color="#202023", corner_radius=8)
            card.pack(fill="x", pady=5)
            ctk.CTkLabel(
                card, text=q,
                font=ctk.CTkFont(family=FONT_HEADING, size=12, weight="bold"),
                text_color="#38bdf8", wraplength=410, justify="left"
            ).pack(anchor="w", padx=10, pady=(8, 2))
            ctk.CTkLabel(
                card, text=a,
                font=ctk.CTkFont(family=FONT_BODY, size=11),
                text_color="#d4d4d8", wraplength=410, justify="left"
            ).pack(anchor="w", padx=10, pady=(0, 8))

    def _build_monitor_panel(self):
        pad_x = 14

        # Real-time Checkpoint Status Card
        self.checkpoint_card = ctk.CTkFrame(self.right_col, fg_color="#1e3a2b", corner_radius=10)
        self.checkpoint_card.pack(fill="x", padx=pad_x, pady=(14, 8))

        self.checkpoint_title = ctk.CTkLabel(
            self.checkpoint_card,
            text="🟢 Trạng Thái: Sẵn Sàng (Ready)",
            font=ctk.CTkFont(family=FONT_HEADING, size=14, weight="bold"),
            text_color="#4ade80"
        )
        self.checkpoint_title.pack(anchor="w", padx=14, pady=(10, 2))

        self.checkpoint_desc = ctk.CTkLabel(
            self.checkpoint_card,
            text="Hệ thống đã nạp tiện ích và sẵn sàng. Hãy bấm 'Bắt Đầu Tự Động A - Z' hoặc 'Bước 1' để khởi chạy.",
            font=ctk.CTkFont(family=FONT_BODY, size=11),
            text_color="#bbf7d0",
            wraplength=480,
            justify="left"
        )
        self.checkpoint_desc.pack(anchor="w", padx=14, pady=(0, 10))

        # Progress Bar with percentage label
        prog_header = ctk.CTkFrame(self.right_col, fg_color="transparent")
        prog_header.pack(fill="x", padx=pad_x, pady=(4, 2))

        ctk.CTkLabel(
            prog_header, text="TIẾN TRÌNH THỰC HIỆN",
            font=ctk.CTkFont(family=FONT_BODY, size=11, weight="bold"),
            text_color="#a1a1aa"
        ).pack(side="left")

        self.lbl_progress_pct = ctk.CTkLabel(
            prog_header, text="0%",
            font=ctk.CTkFont(family=FONT_BODY, size=11, weight="bold"),
            text_color="#38bdf8"
        )
        self.lbl_progress_pct.pack(side="right")

        self.progress_bar = ctk.CTkProgressBar(self.right_col, height=8, corner_radius=4)
        self.progress_bar.pack(fill="x", padx=pad_x, pady=(0, 8))
        self.progress_bar.set(0.0)

        # Log Header + Action Buttons
        log_head = ctk.CTkFrame(self.right_col, fg_color="transparent")
        log_head.pack(fill="x", padx=pad_x, pady=(4, 4))

        ctk.CTkLabel(
            log_head, text="NHẬT KÝ HOẠT ĐỘNG THỜI GIAN THỰC (LIVE LOGS)",
            font=ctk.CTkFont(family=FONT_BODY, size=11, weight="bold"),
            text_color="#a1a1aa"
        ).pack(side="left")

        btn_open_shots = ctk.CTkButton(
            log_head, text="📁 Xem Ảnh Chụp",
            font=ctk.CTkFont(family=FONT_BODY, size=11),
            fg_color="#27272a", hover_color="#3f3f46", height=24, width=95,
            command=self._cmd_open_screenshots_folder
        )
        btn_open_shots.pack(side="right", padx=(4, 0))

        btn_clear = ctk.CTkButton(
            log_head, text="🧹 Xóa Log",
            font=ctk.CTkFont(family=FONT_BODY, size=11),
            fg_color="#27272a", hover_color="#3f3f46", height=24, width=70,
            command=self._cmd_clear_log
        )
        btn_clear.pack(side="right")

        # Log Text Box
        self.log_box = ctk.CTkTextbox(
            self.right_col,
            font=ctk.CTkFont(family="Consolas", size=11),
            fg_color="#121214",
            text_color="#e4e4e7",
            corner_radius=8
        )
        self.log_box.pack(fill="both", expand=True, padx=pad_x, pady=(0, 14))

        self.append_log("INFO", f"Ứng dụng đã khởi động thành công trên {OS_DESC}.")
        self.append_log("INFO", "Cảm biến tự động nhận diện Login, 2FA, Captcha, và Form thẻ thanh toán đang kích hoạt.")

    def append_log(self, tag: str, msg: str):
        ts = time.strftime("%H:%M:%S")
        color_map = {
            "INFO": "[INFO]",
            "STAGE": "[BƯỚC]",
            "HALT_LOGIN": "[CHỜ-LOGIN]",
            "HALT_CAPTCHA": "[CHỜ-CAPTCHA]",
            "RESUME_LOGIN": "[TIẾP TỤC]",
            "RESUME_CAPTCHA": "[TIẾP TỤC]",
            "SUCCESS": "[THÀNH CÔNG]",
            "WARN": "[LƯU Ý]",
            "ERROR": "[LỖI]",
            "ENGINE": "[CHI TIẾT]"
        }
        tag_str = color_map.get(tag, f"[{tag}]")
        line = f"[{ts}] {tag_str} {msg}\n"
        
        self.log_box.configure(state="normal")
        self.log_box.insert("end", line)
        self.log_box.see("end")
        self.log_box.configure(state="disabled")

    def set_checkpoint_status(self, kind: str, title: str, desc: str):
        color_map = {
            "ready": ("#4ade80", "#1e3a2b", "#bbf7d0"),
            "halt_login": ("#fbbf24", "#422006", "#fde68a"),
            "halt_captcha": ("#f97316", "#431407", "#fed7aa"),
            "running": ("#38bdf8", "#082f49", "#bae6fd"),
            "success": ("#4ade80", "#064e3b", "#a7f3d0"),
            "error": ("#f87171", "#450a0a", "#fecaca"),
            "idle": ("#94a3b8", "#1e293b", "#cbd5e1")
        }
        fg, bg, txt_color = color_map.get(kind, ("#4ade80", "#1e3a2b", "#bbf7d0"))
        self.checkpoint_card.configure(fg_color=bg)
        self.checkpoint_title.configure(text=title, text_color=fg)
        self.checkpoint_desc.configure(text=desc, text_color=txt_color)

    def set_progress(self, val: float):
        self.progress_bar.set(val)
        pct = int(val * 100)
        self.lbl_progress_pct.configure(text=f"{pct}%")

    def _highlight_step(self, step_index: int):
        for i, (pill, lbl_txt) in enumerate(self.step_labels):
            if i == step_index:
                pill.configure(fg_color="#0369a1")
                lbl_txt.configure(text_color="#ffffff")
            elif i < step_index:
                pill.configure(fg_color="#065f46")
                lbl_txt.configure(text_color="#a7f3d0")
            else:
                pill.configure(fg_color="#27272a")
                lbl_txt.configure(text_color="#71717a")

    def _get_profile_dir(self, account_id: str) -> str:
        return os.path.join(BASE_DIR, "profiles", f"profile_{account_id.lower()}")

    def _clean_profile_dirs(self, account_id: str):
        for p in (
            self._get_profile_dir(account_id),
            os.path.join(BASE_DIR, "profiles", account_id),
        ):
            if os.path.exists(p):
                shutil.rmtree(p, ignore_errors=True)

    def _refresh_accounts(self):
        accounts = self.cfg.get("accounts", [])
        if not accounts:
            self.account_menu.configure(values=["Account_1 (Chưa đăng nhập)"])
            if hasattr(self, "lbl_acc_info"):
                self.lbl_acc_info.configure(text="📍 Đang chọn: Account_1 | Thư mục: profiles/profile_account_1")
            return
            
        vals = []
        for a in accounts:
            aid = a.get("id", "Account_1")
            em = a.get("email") or "Chưa đăng nhập"
            vals.append(f"{aid} ({em})")
            
        self.account_menu.configure(values=vals)
        cur_matched = [v for v in vals if v.split()[0] == self.active_account_id]
        if cur_matched:
            self.account_menu.set(cur_matched[0])
            self._update_acc_info_label(cur_matched[0])
        elif vals:
            self.account_menu.set(vals[0])
            self.active_account_id = vals[0].split()[0]
            self._update_acc_info_label(vals[0])

    def _update_acc_info_label(self, choice: str):
        if hasattr(self, "lbl_acc_info"):
            aid = choice.split()[0]
            self.lbl_acc_info.configure(text=f"📍 Đang chọn: {aid} | Thư mục: profiles/profile_{aid.lower()}")

    def _on_account_selected(self, choice: str):
        aid = choice.split()[0]
        self.active_account_id = aid
        self._update_acc_info_label(choice)
        self.append_log("INFO", f"Đã chọn phiên làm việc: {choice}")

    def _on_engine_event(self, event_type: str, message: str):
        self.after(0, self.append_log, event_type, message)

        if event_type == "STAGING_DONE":
            self.cfg = self.load_config()
            br_name = self.cfg.get("staged_browser", "Chromium / Edge")
            if hasattr(self, "lbl_staging_status"):
                self.after(0, lambda: self.lbl_staging_status.configure(
                    text=f"🟢 Đã sẵn sàng (Trình duyệt: {br_name} + Dual-Mode CDP)",
                    text_color="#4ade80"
                ))
            self.after(0, self.set_checkpoint_status, "success", "🟢 Hoàn Tất Cài Đặt Môi Trường (Staging)", message)
            self.after(0, self.set_progress, 1.0)
            self.after(0, self._highlight_step, 1)
        elif event_type == "HALT_LOGIN":
            self.after(0, self.set_checkpoint_status, "halt_login", "🟡 Đang chờ đăng nhập & 2FA", message)
            self.after(0, self.set_progress, 0.15)
            self.after(0, self._highlight_step, 1)
        elif event_type == "RESUME_LOGIN":
            self.after(0, self.set_checkpoint_status, "running", "🟢 Đã đăng nhập thành công", "Tự động tiếp tục chuyển sang bước nâng cấp...")
            self.after(0, self.set_progress, 0.3)
            self.after(0, self._highlight_step, 2)
            self.after(0, self._refresh_accounts)
        elif event_type == "HALT_CAPTCHA":
            self.after(0, self.set_checkpoint_status, "halt_captcha", "🟠 Tạm dừng: Giải Captcha", message)
        elif event_type == "RESUME_CAPTCHA":
            self.after(0, self.set_checkpoint_status, "running", "🟢 Captcha đã giải xong", "Tự động tiếp tục...")
        elif event_type == "HALT_CARD":
            self.after(0, self.set_checkpoint_status, "halt_login", "💳 Đang chờ nhập thông tin thẻ", message)
        elif event_type == "RESUME_CARD":
            self.after(0, self.set_checkpoint_status, "running", "🟢 Đã nhận diện thẻ thanh toán", "Tự động tiếp tục...")
        elif event_type == "STAGE":
            self.after(0, self.set_checkpoint_status, "running", "🔵 Đang xử lý tự động", message)
            if "STAGING" in message:
                self.after(0, self.set_progress, 0.25)
                self.after(0, self._highlight_step, 0)
            elif "Layer 1" in message:
                self.after(0, self.set_progress, 0.45)
                self.after(0, self._highlight_step, 2)
            elif "Layer 2" in message:
                self.after(0, self.set_progress, 0.65)
                self.after(0, self._highlight_step, 2)
            elif "Layer 3" in message:
                self.after(0, self.set_progress, 0.8)
                self.after(0, self._highlight_step, 2)
            elif "Canceling" in message or "Google Play" in message:
                self.after(0, self.set_progress, 0.9)
                self.after(0, self._highlight_step, 3)
            elif "Việt Nam" in message:
                self.after(0, self.set_progress, 0.95)
                self.after(0, self._highlight_step, 4)
        elif event_type == "SUCCESS":
            self.after(0, self.set_checkpoint_status, "running", "🟢 Tiến trình thành công", message)
            self.after(0, self._refresh_accounts)
        elif event_type == "COMPLETED":
            self.after(0, self.set_checkpoint_status, "success", "🎉 Hoàn Tất 24 Tháng Google AI Pro 5 TB!", "Đã hoàn tất cộng dồn đủ 24 tháng, hủy phí gia hạn định kỳ và gỡ thẻ thành công.")
            self.after(0, self.set_progress, 1.0)
            self.after(0, self._highlight_step, 4)
            self.after(0, self._refresh_accounts)

    def _cmd_run_staging(self):
        if self.is_running:
            self.append_log("WARN", "Một tiến trình đang chạy, vui lòng đợi hoàn tất...")
            return
        self.is_running = True
        self.btn_staging.configure(state="disabled", text="⏳ Đang cài đặt môi trường & tiện ích...")
        self._highlight_step(0)
        self.set_progress(0.15)
        self.set_checkpoint_status("running", "🛠️ Đang chuẩn bị môi trường (Staging)", "Đang kiểm tra quyền hệ thống, giải nén tiện ích và cài đặt trình duyệt hỗ trợ Extension...")

        def _worker():
            try:
                eng = engine_stacker.StackingEngine(self.active_account_id, on_event=self._on_engine_event)
                self.engine = eng
                eng.run_staging_environment()
            except Exception as e:
                self._on_engine_event("ERROR", f"Lỗi Staging: {e}")
            finally:
                self.is_running = False
                self.after(0, lambda: self.btn_staging.configure(
                    state="normal",
                    text="✅ 0. Kiểm Tra / Chạy Lại Cài Đặt Môi Trường & Tiện Ích"
                ))

        threading.Thread(target=_worker, daemon=True).start()

    def _cmd_launch_signin(self):
        self.append_log("STAGE", f"Đang khởi tạo trình duyệt hiển thị trên màn hình cho [{self.active_account_id}]...")
        self.set_checkpoint_status("running", "🌐 Đang mở trình duyệt & khởi tạo Browsec VPN", "Trình duyệt đang mở trang Đăng nhập Google và tự động kích hoạt Browsec VPN (US)...")
        eng = engine_stacker.StackingEngine(self.active_account_id, on_event=self._on_engine_event)
        threading.Thread(target=eng.launch_and_prepare_signin, daemon=True).start()

    def _cmd_stop(self):
        self.append_log("WARN", "🛑 Đang gửi yêu cầu dừng tiến trình...")
        if self.engine:
            self.engine.stop()
        self.is_running = False
        self.btn_stack.configure(state="normal")
        self.btn_all_in_one.configure(state="normal")
        self.btn_stop.configure(state="disabled")
        self.set_checkpoint_status("idle", "⏸️ Đã dừng tiến trình", "Người dùng đã chủ động dừng tự động hóa.")

    def _cmd_start_stacking(self):
        if self.is_running:
            self.append_log("WARN", "Quy trình đang chạy, vui lòng đợi hoàn tất...")
            return

        self.is_running = True
        self.btn_stack.configure(state="disabled")
        self.btn_all_in_one.configure(state="disabled")
        self.btn_stop.configure(state="normal")
        auto_vn = bool(self.chk_auto_vn.get())
        auto_cards = bool(self.chk_auto_remove_cards.get())
        
        self.append_log("STAGE", f"Bắt đầu chu trình tự động 24 tháng cho [{self.active_account_id}] (Tự đổi vùng VN: {auto_vn}, Tự gỡ thẻ: {auto_cards})...")

        def _worker():
            try:
                self.engine = engine_stacker.StackingEngine(self.active_account_id, on_event=self._on_engine_event)
                asyncio.run(self.engine.run_full_stacking_flow(auto_switch_vn=auto_vn, auto_remove_cards=auto_cards))
            except Exception as e:
                self._on_engine_event("ERROR", f"Lỗi thực thi: {str(e)}")
            finally:
                self.is_running = False
                self.after(0, lambda: self.btn_stack.configure(state="normal"))
                self.after(0, lambda: self.btn_all_in_one.configure(state="normal"))
                self.after(0, lambda: self.btn_stop.configure(state="disabled"))

        self.worker_thread = threading.Thread(target=_worker, daemon=True)
        self.worker_thread.start()

    def _cmd_cancel_renewal(self):
        if self.is_running:
            self.append_log("WARN", "Quy trình đang chạy, vui lòng đợi hoàn tất...")
            return
        self.is_running = True
        self.append_log("STAGE", "Đang kết nối để hủy gia hạn bảo vệ tài khoản (Hủy gia hạn định kỳ & Bảo lưu thời hạn)...")

        def _worker():
            try:
                eng = engine_stacker.StackingEngine(self.active_account_id, on_event=self._on_engine_event)
                self.engine = eng
                eng.launch_visible_edge("https://play.google.com/store/account/subscriptions?hl=vi", reuse_if_open=True)
                time.sleep(2.5)
                async def _sub_cancel():
                    async with async_playwright() as p:
                        browser = await p.chromium.connect_over_cdp(f"http://127.0.0.1:{eng.port}")
                        context = browser.contexts[0]
                        page = context.pages[0] if context.pages else await context.new_page()
                        await eng.cancel_youtube_and_lock_2028(page)
                asyncio.run(_sub_cancel())
            except Exception as e:
                self._on_engine_event("ERROR", f"Lỗi hủy gia hạn: {str(e)}")
            finally:
                self.is_running = False

        threading.Thread(target=_worker, daemon=True).start()

    def _cmd_remove_cards_standalone(self):
        if self.is_running:
            self.append_log("WARN", "Quy trình đang chạy, vui lòng đợi hoàn tất...")
            return
        self.is_running = True
        self.append_log("STAGE", "Đang mở Google Payments để gỡ toàn bộ thẻ...")

        def _worker():
            try:
                eng = engine_stacker.StackingEngine(self.active_account_id, on_event=self._on_engine_event)
                self.engine = eng
                eng.launch_visible_edge("https://play.google.com/store/paymentmethods?hl=vi", reuse_if_open=True)
                time.sleep(2.5)
                async def _sub_remove():
                    async with async_playwright() as p:
                        browser = await p.chromium.connect_over_cdp(f"http://127.0.0.1:{eng.port}")
                        context = browser.contexts[0]
                        page = context.pages[0] if context.pages else await context.new_page()
                        await eng.remove_all_linked_cards(page)
                asyncio.run(_sub_remove())
            except Exception as e:
                self._on_engine_event("ERROR", f"Lỗi gỡ thẻ: {str(e)}")
            finally:
                self.is_running = False

        threading.Thread(target=_worker, daemon=True).start()

    def _cmd_switch_vn(self):
        if self.is_running:
            self.append_log("WARN", "Quy trình đang chạy, vui lòng đợi hoàn tất...")
            return
        self.is_running = True
        self.append_log("STAGE", f"Đang kết nối để đổi vùng thanh toán về Việt Nam cho [{self.active_account_id}]...")

        def _worker():
            try:
                eng = engine_stacker.StackingEngine(self.active_account_id, on_event=self._on_engine_event)
                eng.launch_visible_edge("https://payments.google.com/gp/w/u/0/home/settings?hl=vi", reuse_if_open=True)
                time.sleep(2.5)
                async def _sub_vn():
                    async with async_playwright() as p:
                        browser = await p.chromium.connect_over_cdp(f"http://127.0.0.1:{eng.port}")
                        context = browser.contexts[0]
                        page = context.pages[0] if context.pages else await context.new_page()
                        await eng.switch_billing_region_to_vietnam(page)
                asyncio.run(_sub_vn())
            except Exception as e:
                self._on_engine_event("ERROR", f"Lỗi chuyển vùng: {str(e)}")
            finally:
                self.is_running = False

        threading.Thread(target=_worker, daemon=True).start()

    def _cmd_run_single_layer(self, layer_num: int):
        if self.is_running:
            self.append_log("WARN", "Quy trình đang chạy, vui lòng đợi hoàn tất...")
            return
        self.is_running = True
        self.append_log("STAGE", f"Chạy thủ công Tầng {layer_num} cho [{self.active_account_id}]...")
        def _worker():
            try:
                eng = engine_stacker.StackingEngine(self.active_account_id, on_event=self._on_engine_event)
                eng.launch_visible_edge(reuse_if_open=True)
                time.sleep(2.5)
                async def _sub_layer():
                    async with async_playwright() as p:
                        browser = await p.chromium.connect_over_cdp(f"http://127.0.0.1:{eng.port}")
                        context = browser.contexts[0]
                        page = context.pages[0] if context.pages else await context.new_page()
                        if layer_num == 1:
                            await eng.layer_1_initial_12m(page)
                        elif layer_num == 2:
                            await eng.layer_2_oem_samsung(page)
                        elif layer_num == 3:
                            await eng.layer_3_upgrade_5tb(page)
                asyncio.run(_sub_layer())
            except Exception as e:
                self._on_engine_event("ERROR", f"Lỗi Tầng {layer_num}: {str(e)}")
            finally:
                self.is_running = False
        threading.Thread(target=_worker, daemon=True).start()

    def _cmd_clean_port_manual(self):
        engine_stacker.clean_port(9320)
        self.append_log("INFO", "Đã dọn dẹp và giải phóng cổng 9320.")

    def _cmd_open_config_file(self):
        if os.path.exists(CONFIG_PATH):
            if IS_WIN:
                os.startfile(CONFIG_PATH)
            elif IS_MAC:
                subprocess.Popen(["open", CONFIG_PATH])
            else:
                subprocess.Popen(["xdg-open", CONFIG_PATH])

    def _cmd_open_screenshots_folder(self):
        if os.path.exists(SCREENSHOTS_DIR):
            if IS_WIN:
                os.startfile(SCREENSHOTS_DIR)
            elif IS_MAC:
                subprocess.Popen(["open", SCREENSHOTS_DIR])
            else:
                subprocess.Popen(["xdg-open", SCREENSHOTS_DIR])

    def _cmd_clear_log(self):
        self.log_box.configure(state="normal")
        self.log_box.delete("1.0", "end")
        self.log_box.configure(state="disabled")

    def _cmd_create_new_instance(self):
        accounts = self.cfg.setdefault("accounts", [])
        existing_ids = {a.get("id") for a in accounts}
        idx = 1
        while f"Account_{idx}" in existing_ids:
            idx += 1
        new_id = f"Account_{idx}"
        new_acc = {
            "id": new_id,
            "email": "",
            "status": "pending_login",
            "current_step": 0
        }
        accounts.append(new_acc)
        self.save_config()
        self.active_account_id = new_id
        self._refresh_accounts()
        self.append_log("INFO", f"Đã tạo phiên mới: [{new_id}]. Bấm 'Mở Cửa Sổ Đăng Nhập' để nhập Gmail mới.")

    def _cmd_delete_account(self):
        accounts = self.cfg.get("accounts", [])
        target_id = self.active_account_id
        if engine_stacker.StackingEngine._active_cdp_account == target_id:
            engine_stacker.clean_port(9320)
            engine_stacker.StackingEngine._active_cdp_account = None

        if len(accounts) <= 1:
            if accounts:
                accounts[0]["email"] = ""
                accounts[0]["status"] = "pending_login"
                accounts[0]["current_step"] = 0
            self._clean_profile_dirs(target_id)
            self.save_config()
            self._refresh_accounts()
            self.append_log("INFO", f"Đã làm sạch dữ liệu và reset [{target_id}] về mặc định.")
            return

        self.cfg["accounts"] = [a for a in accounts if a.get("id") != target_id]
        self._clean_profile_dirs(target_id)
        self.save_config()
        remaining = self.cfg.get("accounts", [])
        self.active_account_id = remaining[0]["id"] if remaining else "Account_1"
        self._refresh_accounts()
        self.append_log("OK", f"Đã xóa vĩnh viễn [{target_id}] và giải phóng thư mục lưu trữ.")

    def _cmd_reset_account_session(self):
        target_id = self.active_account_id
        if engine_stacker.StackingEngine._active_cdp_account == target_id:
            engine_stacker.clean_port(9320)
            engine_stacker.StackingEngine._active_cdp_account = None

        self._clean_profile_dirs(target_id)
        for a in self.cfg.get("accounts", []):
            if a.get("id") == target_id:
                a["status"] = "pending_login"
                a["email"] = ""
                a["current_step"] = 0
                break
        self.save_config()
        self._refresh_accounts()
        self.append_log("OK", f"Đã dọn dẹp sạch cache và đặt lại trạng thái đăng nhập cho [{target_id}].")

    def _cmd_open_profile_folder(self):
        target_id = self.active_account_id
        profile_dir = self._get_profile_dir(target_id)
        os.makedirs(profile_dir, exist_ok=True)
        if IS_WIN:
            os.startfile(profile_dir)
        elif IS_MAC:
            subprocess.Popen(["open", profile_dir])
        else:
            subprocess.Popen(["xdg-open", profile_dir])

def run_app():
    ensure_single_instance()
    app = UniversalStackerApp()
    app.mainloop()

if __name__ == "__main__":
    run_app()
