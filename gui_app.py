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
Google AI Pro 24-Month Automator — Windows 11 Fluent GUI
--------------------------------------------------------
Crafted with CustomTkinter for native Windows 11 Fluent Design styling.
Features:
  - Halts at Login, Captcha, and Card details with Auto-Detection & Auto-Resume
  - Step 5 YouTube Protection: Cancels auto-renewal to eliminate $11.99 charges
  - Full 24-Month Zero-Cost Stacking to late 2028
  - Real-time live log and checkpoint visualizer
"""

import os
import sys
import json
import time
import threading
import asyncio
import subprocess
from typing import Optional, Dict, Any

import customtkinter as ctk
from PIL import Image
from playwright.async_api import async_playwright

# Setup base paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(BASE_DIR, "config.json")
ARTIFACTS_DIR = r"C:\Users\khoa\.gemini\antigravity\brain\bdb8ac8f-261e-4351-8267-5fe6b7181fb3"

import engine_stacker

# Set CustomTkinter theme to Windows 11 Fluent style
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class Windows11StackerApp(ctk.CTk):
    def __init__(self):
        if not _verify_author_seal():
            import sys; sys.exit(1)
        super().__init__()

        self.title("Google AI Pro 24-Month Automator · Windows 11 Edition")
        self.geometry("980x740")
        self.minsize(880, 640)

        # Apply dark background
        self.configure(fg_color="#18181b")

        self.cfg = self.load_config()
        self.active_account_id = "Account_1"
        self.engine: Optional[engine_stacker.StackingEngine] = None
        self.worker_thread: Optional[threading.Thread] = None
        self.is_running = False

        self._build_ui()
        self._refresh_accounts()

    def load_config(self) -> Dict[str, Any]:
        if os.path.exists(CONFIG_PATH):
            with open(CONFIG_PATH, "r", encoding="utf-8") as f:
                return json.load(f)
        return {"accounts": [], "card": {}}

    def save_config(self):
        with open(CONFIG_PATH, "w", encoding="utf-8") as f:
            json.dump(self.cfg, f, indent=2, ensure_ascii=False)

    def _build_ui(self):
        # 1. Top Header Bar (Windows 11 Fluent Header)
        self.header_frame = ctk.CTkFrame(self, fg_color="#202023", corner_radius=12, height=64)
        self.header_frame.pack(fill="x", padx=16, pady=(16, 10))

        # Title + Subtitle
        self.title_label = ctk.CTkLabel(
            self.header_frame,
            text="Google AI Pro (5 TB) 24-Month Automator",
            font=ctk.CTkFont(family="Segoe UI Variable Display", size=18, weight="bold"),
            text_color="#ffffff"
        )
        self.title_label.pack(side="left", padx=18, pady=(10, 2))

        # Status badge pill on right
        self.vpn_badge = ctk.CTkLabel(
            self.header_frame,
            text="🟢 US VPN: Browsec Ready",
            font=ctk.CTkFont(family="Segoe UI Variable Text", size=12, weight="bold"),
            fg_color="#1e3a2b",
            text_color="#4ade80",
            corner_radius=8,
            padx=12,
            pady=4
        )
        self.vpn_badge.pack(side="right", padx=16, pady=14)

        # 2. Main Content Split (Left: Control Panel, Right: Logs & Monitor)
        self.main_container = ctk.CTkFrame(self, fg_color="transparent")
        self.main_container.pack(fill="both", expand=True, padx=16, pady=4)

        # Left Column: Controls & Cards (width 380)
        self.left_col = ctk.CTkFrame(self.main_container, fg_color="#202023", corner_radius=12, width=380)
        self.left_col.pack(side="left", fill="both", padx=(0, 8), pady=4)
        self.left_col.pack_propagate(False)

        # Right Column: Checkpoints & Live Logs
        self.right_col = ctk.CTkFrame(self.main_container, fg_color="#202023", corner_radius=12)
        self.right_col.pack(side="right", fill="both", expand=True, padx=(8, 0), pady=4)

        self._build_left_panel()
        self._build_right_panel()

    def _build_left_panel(self):
        pad_x = 16

        # --- Section: Instance / Account Selector ---
        lbl_acc = ctk.CTkLabel(
            self.left_col, text="TÀI KHOẢN & INSTANCE",
            font=ctk.CTkFont(family="Segoe UI Variable Text", size=11, weight="bold"),
            text_color="#a1a1aa"
        )
        lbl_acc.pack(anchor="w", padx=pad_x, pady=(14, 4))

        self.account_menu = ctk.CTkOptionMenu(
            self.left_col,
            values=["Account_1 (user@gmail.com)"],
            command=self._on_account_selected,
            font=ctk.CTkFont(family="Segoe UI Variable Text", size=13),
            fg_color="#27272a",
            button_color="#3f3f46",
            button_hover_color="#52525b",
            height=34
        )
        self.account_menu.pack(fill="x", padx=pad_x, pady=(0, 10))

        # --- Section: Checkpoint Banner (Halt Indicator) ---
        self.checkpoint_card = ctk.CTkFrame(self.left_col, fg_color="#27272a", corner_radius=10)
        self.checkpoint_card.pack(fill="x", padx=pad_x, pady=6)

        self.checkpoint_title = ctk.CTkLabel(
            self.checkpoint_card,
            text="🟢 Trạng thái: Sẵn sàng",
            font=ctk.CTkFont(family="Segoe UI Variable Text", size=13, weight="bold"),
            text_color="#4ade80"
        )
        self.checkpoint_title.pack(anchor="w", padx=12, pady=(10, 2))

        self.checkpoint_desc = ctk.CTkLabel(
            self.checkpoint_card,
            text="Hệ thống tự động dừng tại Login, Captcha, và Form thẻ, sau đó tự tiếp tục.",
            font=ctk.CTkFont(family="Segoe UI Variable Text", size=11),
            text_color="#94a3b8",
            wraplength=330,
            justify="left"
        )
        self.checkpoint_desc.pack(anchor="w", padx=12, pady=(0, 10))

        # --- Section: Action Buttons ---
        lbl_actions = ctk.CTkLabel(
            self.left_col, text="THAO TÁC ĐIỀU KHIỂN",
            font=ctk.CTkFont(family="Segoe UI Variable Text", size=11, weight="bold"),
            text_color="#a1a1aa"
        )
        lbl_actions.pack(anchor="w", padx=pad_x, pady=(12, 4))

        # Button 1: Launch interactive sign-in
        self.btn_signin = ctk.CTkButton(
            self.left_col,
            text="🚀 Bật cửa sổ đăng nhập (Màn hình chính)",
            font=ctk.CTkFont(family="Segoe UI Variable Text", size=13, weight="bold"),
            fg_color="#0284c7",
            hover_color="#0369a1",
            height=38,
            command=self._cmd_launch_signin
        )
        self.btn_signin.pack(fill="x", padx=pad_x, pady=4)

        # Row: Start Stacking + Stop Button
        row_action = ctk.CTkFrame(self.left_col, fg_color="transparent")
        row_action.pack(fill="x", padx=pad_x, pady=4)

        self.btn_stack = ctk.CTkButton(
            row_action,
            text="▶ Bắt đầu nâng cấp 24T ($0.00)",
            font=ctk.CTkFont(family="Segoe UI Variable Text", size=13, weight="bold"),
            fg_color="#16a34a",
            hover_color="#15803d",
            height=38,
            command=self._cmd_start_stacking
        )
        self.btn_stack.pack(side="left", fill="x", expand=True, padx=(0, 4))

        self.btn_stop = ctk.CTkButton(
            row_action,
            text="⏹ Dừng (Stop)",
            font=ctk.CTkFont(family="Segoe UI Variable Text", size=12, weight="bold"),
            fg_color="#dc2626",
            hover_color="#b91c1c",
            height=38,
            width=90,
            state="disabled",
            command=self._cmd_stop
        )
        self.btn_stop.pack(side="right")

        # Checkbox: Auto-switch to Vietnam after stacking
        self.chk_auto_vn = ctk.CTkCheckBox(
            self.left_col,
            text="🇻🇳 Tự động đổi vùng VN (Bật Family Sharing)",
            font=ctk.CTkFont(family="Segoe UI Variable Text", size=11),
            text_color="#e4e4e7",
            fg_color="#0284c7",
            hover_color="#0369a1"
        )
        self.chk_auto_vn.select()
        self.chk_auto_vn.pack(anchor="w", padx=pad_x + 2, pady=(2, 6))

        # Button 3: Cancel Auto-Renewal (Eliminate YouTube & Lock 2028)
        self.btn_cancel_renew = ctk.CTkButton(
            self.left_col,
            text="🛡️ Hủy gia hạn ngay (Khóa 2028 & Hủy phí YT)",
            font=ctk.CTkFont(family="Segoe UI Variable Text", size=12),
            fg_color="#dc2626",
            hover_color="#b91c1c",
            height=34,
            command=self._cmd_cancel_renewal
        )
        self.btn_cancel_renew.pack(fill="x", padx=pad_x, pady=4)

        # Button 4: Switch Billing Region to Vietnam (Family Sharing)
        self.btn_switch_vn = ctk.CTkButton(
            self.left_col,
            text="🇻🇳 Chuyển vùng về VN (Bật Family Sharing)",
            font=ctk.CTkFont(family="Segoe UI Variable Text", size=12),
            fg_color="#0d9488",
            hover_color="#0f766e",
            height=34,
            command=self._cmd_switch_vn
        )
        self.btn_switch_vn.pack(fill="x", padx=pad_x, pady=4)

        # Button 5: Add New Account Instance
        self.btn_new_instance = ctk.CTkButton(
            self.left_col,
            text="➕ Tạo phiên (Instance) tài khoản mới",
            font=ctk.CTkFont(family="Segoe UI Variable Text", size=12),
            fg_color="#3f3f46",
            hover_color="#52525b",
            height=32,
            command=self._cmd_create_new_instance
        )
        self.btn_new_instance.pack(fill="x", padx=pad_x, pady=4)

        # Production Security & Privacy Status Box
        self.privacy_box = ctk.CTkFrame(self.left_col, fg_color="#18181b", corner_radius=8)
        self.privacy_box.pack(fill="x", padx=pad_x, pady=(12, 10))

        info_txt = "🔒 Chế độ Bảo mật (Production Ver):\n• Thẻ thanh toán: Nhập trực tiếp trên cửa sổ Google\n• Không lưu trữ số thẻ / CVC trên mã nguồn\n• Tự động dừng tại bước thanh toán & tự chạy tiếp"
        self.lbl_privacy_info = ctk.CTkLabel(
            self.privacy_box, text=info_txt,
            font=ctk.CTkFont(family="Segoe UI Variable Text", size=11),
            text_color="#94a3b8", justify="left"
        )
        self.lbl_privacy_info.pack(padx=10, pady=8)

    def _build_right_panel(self):
        # Top of right panel: Step Tracker indicators
        tracker_frame = ctk.CTkFrame(self.right_col, fg_color="transparent")
        tracker_frame.pack(fill="x", padx=16, pady=(12, 6))

        lbl_log = ctk.CTkLabel(
            tracker_frame, text="TIẾN TRÌNH 24 THÁNG & NHẬT KÝ HOẠT ĐỘNG",
            font=ctk.CTkFont(family="Segoe UI Variable Text", size=11, weight="bold"),
            text_color="#a1a1aa"
        )
        lbl_log.pack(side="left")

        # Live Progress bar
        self.progress_bar = ctk.CTkProgressBar(self.right_col, height=8, corner_radius=4)
        self.progress_bar.pack(fill="x", padx=16, pady=(0, 10))
        self.progress_bar.set(0.0)

        # Log Text Box
        self.log_box = ctk.CTkTextbox(
            self.right_col,
            font=ctk.CTkFont(family="Consolas", size=12),
            fg_color="#18181b",
            text_color="#e4e4e7",
            corner_radius=8
        )
        self.log_box.pack(fill="both", expand=True, padx=16, pady=(0, 14))

        self.append_log("INFO", "Google AI Pro 24-Month Windows 11 GUI initialized.")
        self.append_log("INFO", "Tất cả các mốc kiểm tra (Login, Captcha, Card) đã được gắn cảm biến tự dừng và tự tiếp tục.")

    def append_log(self, tag: str, msg: str):
        ts = time.strftime("%H:%M:%S")
        color_map = {
            "INFO": "[INFO]",
            "STAGE": "[BƯỚC]",
            "HALT_LOGIN": "[DỪNG-LOGIN]",
            "HALT_CAPTCHA": "[DỪNG-CAPTCHA]",
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
            "ready": ("#4ade80", "#1e3a2b"),
            "halt_login": ("#fbbf24", "#3a2e1e"),
            "halt_captcha": ("#f97316", "#3a221e"),
            "running": ("#38bdf8", "#1e2e3a"),
            "success": ("#4ade80", "#1e3a2b"),
            "error": ("#f87171", "#3a1e1e")
        }
        fg, bg = color_map.get(kind, ("#4ade80", "#1e3a2b"))
        self.checkpoint_card.configure(fg_color=bg)
        self.checkpoint_title.configure(text=title, text_color=fg)
        self.checkpoint_desc.configure(text=desc)

    def _refresh_accounts(self):
        accounts = self.cfg.get("accounts", [])
        if not accounts:
            self.account_menu.configure(values=["Account_1 (Chưa đăng nhập)"])
            return
            
        vals = []
        for a in accounts:
            aid = a.get("id", "Account_1")
            em = a.get("email") or "Chưa đăng nhập"
            vals.append(f"{aid} ({em})")
            
        self.account_menu.configure(values=vals)
        if vals:
            self.account_menu.set(vals[0])

    def _on_account_selected(self, choice: str):
        aid = choice.split()[0]
        self.active_account_id = aid
        self.append_log("INFO", f"Đã chọn phiên làm việc: {choice}")

    def _on_engine_event(self, event_type: str, message: str):
        # Update logs on UI thread
        self.after(0, self.append_log, event_type, message)

        # Update checkpoint indicators
        if event_type == "HALT_LOGIN":
            self.after(0, self.set_checkpoint_status, "halt_login", "🟡 Đang chờ đăng nhập", message)
            self.after(0, self.progress_bar.set, 0.2)
        elif event_type == "RESUME_LOGIN":
            self.after(0, self.set_checkpoint_status, "running", "🟢 Đã đăng nhập", "Tự động tiếp tục quy trình...")
            self.after(0, self.progress_bar.set, 0.4)
            self.after(0, self._refresh_accounts)
        elif event_type == "HALT_CAPTCHA":
            self.after(0, self.set_checkpoint_status, "halt_captcha", "🟠 Phát hiện Captcha", message)
        elif event_type == "RESUME_CAPTCHA":
            self.after(0, self.set_checkpoint_status, "running", "🟢 Captcha đã giải xong", "Tự động tiếp tục quy trình...")
        elif event_type == "HALT_VPN":
            self.after(0, self.set_checkpoint_status, "halt_login", "🔴 Dừng: VPN Hoa Kỳ chưa kết nối", message)
        elif event_type == "RESUME_VPN":
            self.after(0, self.set_checkpoint_status, "running", "🟢 Đã kết nối VPN Hoa Kỳ (US)", message)
        elif event_type == "HALT_CARD":
            self.after(0, self.set_checkpoint_status, "halt_login", "💳 Đang chờ nhập thông tin thẻ", message)
        elif event_type == "RESUME_CARD":
            self.after(0, self.set_checkpoint_status, "running", "🟢 Đã nhận diện thẻ thanh toán", "Tự động tiếp tục quy trình...")
        elif event_type == "STAGE":
            self.after(0, self.set_checkpoint_status, "running", "🔵 Đang xử lý", message)
            if "Layer 1" in message:
                self.after(0, self.progress_bar.set, 0.5)
            elif "Layer 2" in message:
                self.after(0, self.progress_bar.set, 0.7)
            elif "Layer 3" in message:
                self.after(0, self.progress_bar.set, 0.85)
            elif "Canceling" in message:
                self.after(0, self.progress_bar.set, 0.95)
        elif event_type == "COMPLETED" or event_type == "SUCCESS":
            self.after(0, self.set_checkpoint_status, "success", "🎉 Hoàn tất 24 Tháng", "Đã khóa cứng mốc tháng 11/2028 và hủy phí YouTube!")
            self.after(0, self.progress_bar.set, 1.0)
            self.after(0, self._refresh_accounts)

    def _cmd_launch_signin(self):
        self.append_log("STAGE", f"Đang khởi tạo trình duyệt Edge hiển thị trên màn hình cho [{self.active_account_id}]...")
        eng = engine_stacker.StackingEngine(self.active_account_id, on_event=self._on_engine_event)
        threading.Thread(target=eng.launch_visible_edge, daemon=True).start()

    def _cmd_stop(self):
        self.append_log("WARN", "🛑 Đang gửi yêu cầu dừng tiến trình...")
        if self.engine:
            self.engine.stop()
        self.is_running = False
        self.btn_stack.configure(state="normal")
        self.btn_stop.configure(state="disabled")
        self.set_checkpoint_status("idle", "⏸️ Đã dừng tiến trình", "Người dùng đã chủ động dừng tự động hóa.")

    def _cmd_start_stacking(self):
        if self.is_running:
            self.append_log("WARN", "Quy trình đang chạy, vui lòng đợi hoàn tất...")
            return

        self.is_running = True
        self.btn_stack.configure(state="disabled")
        self.btn_stop.configure(state="normal")
        auto_vn = bool(self.chk_auto_vn.get())
        auto_cards = bool(self.chk_auto_remove_cards.get())
        self.append_log("STAGE", f"Bắt đầu chu trình tự động 24 tháng cho [{self.active_account_id}] (Tự đổi vùng VN: {auto_vn})...")

        def _worker():
            try:
                self.engine = engine_stacker.StackingEngine(self.active_account_id, on_event=self._on_engine_event)
                asyncio.run(self.engine.run_full_stacking_flow(auto_switch_vn=auto_vn, auto_remove_cards=auto_cards))
            except Exception as e:
                self._on_engine_event("ERROR", f"Lỗi thực thi: {str(e)}")
            finally:
                self.is_running = False
                self.after(0, lambda: self.btn_stack.configure(state="normal"))
                self.after(0, lambda: self.btn_stop.configure(state="disabled"))

        self.worker_thread = threading.Thread(target=_worker, daemon=True)
        self.worker_thread.start()

    def _cmd_cancel_renewal(self):
        self.append_log("STAGE", "Đang kết nối để hủy gia hạn bảo vệ tài khoản (Khóa 2028 & Triệt tiêu phí YouTube)...")

        def _worker():
            try:
                eng = engine_stacker.StackingEngine(self.active_account_id, on_event=self._on_engine_event)
                eng.launch_visible_edge("https://play.google.com/store/account/subscriptions?hl=vi")
                time.sleep(3.5)
                async def _sub_cancel():
                    async with async_playwright() as p:
                        browser = await p.chromium.connect_over_cdp(f"http://127.0.0.1:{eng.port}")
                        context = browser.contexts[0]
                        page = context.pages[0] if context.pages else await context.new_page()
                        await eng.cancel_youtube_and_lock_2028(page)
                asyncio.run(_sub_cancel())
            except Exception as e:
                self._on_engine_event("ERROR", f"Lỗi hủy gia hạn: {str(e)}")

        threading.Thread(target=_worker, daemon=True).start()

    def _cmd_switch_vn(self):
        self.append_log("STAGE", f"Đang kết nối để đổi vùng thanh toán về Việt Nam cho [{self.active_account_id}]...")

        def _worker():
            try:
                eng = engine_stacker.StackingEngine(self.active_account_id, on_event=self._on_engine_event)
                eng.launch_visible_edge("https://payments.google.com/gp/w/u/0/home/settings?hl=vi")
                time.sleep(3.5)
                async def _sub_vn():
                    async with async_playwright() as p:
                        browser = await p.chromium.connect_over_cdp(f"http://127.0.0.1:{eng.port}")
                        context = browser.contexts[0]
                        page = context.pages[0] if context.pages else await context.new_page()
                        await eng.switch_billing_region_to_vietnam(page)
                asyncio.run(_sub_vn())
            except Exception as e:
                self._on_engine_event("ERROR", f"Lỗi chuyển vùng: {str(e)}")

        threading.Thread(target=_worker, daemon=True).start()

    def _cmd_create_new_instance(self):
        accounts = self.cfg.get("accounts", [])
        idx = len(accounts) + 1
        new_id = f"Account_{idx}"
        new_acc = {
            "id": new_id,
            "email": "",
            "status": "pending_login",
            "current_step": 0
        }
        self.cfg.setdefault("accounts", []).append(new_acc)
        self.save_config()
        self._refresh_accounts()
        self.active_account_id = new_id
        # Select in menu
        for val in self.account_menu._values:
            if val.startswith(new_id):
                self.account_menu.set(val)
                break
        self.append_log("INFO", f"Đã tạo phiên mới: [{new_id}]. Bấm 'Bật cửa sổ đăng nhập' để nhập Gmail mới.")

def ensure_single_instance():
    curr_pid = os.getpid()
    try:
        cmd = f'powershell -Command "Get-CimInstance Win32_Process | Where-Object {{ $_.ProcessId -ne {curr_pid} -and $_.CommandLine -like \'*gui_app.py*\' }} | ForEach-Object {{ Stop-Process -Id $_.ProcessId -Force }}"'
        subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception:
        pass

def run_app():
    ensure_single_instance()
    app = Windows11StackerApp()
    app.mainloop()

if __name__ == "__main__":
    run_app()
