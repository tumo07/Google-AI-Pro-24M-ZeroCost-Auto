"""
Google AI Pro 24M Zero-Cost Auto — Animated Guide Generator
Renders authentic Windows 11 Fluent UI guides reflecting the real application interface.
SPDX-License-Identifier: MIT
Copyright (c) 2026 Trinh Dang Khoa (Alex Trinh) <tumo07@io.vn> | GitHub: @tumo07
"""
import os
import sys
from PIL import Image, ImageDraw, ImageFont

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_DIR = os.path.join(BASE_DIR, "docs", "media")
os.makedirs(MEDIA_DIR, exist_ok=True)

WIDTH = 1000
HEIGHT = 640

def get_font(size: int, bold: bool = False):
    try:
        font_name = "segoeuib.ttf" if bold else "segoeui.ttf"
        return ImageFont.truetype(font_name, size)
    except Exception:
        try:
            return ImageFont.truetype("arialbd.ttf" if bold else "arial.ttf", size)
        except Exception:
            return ImageFont.load_default()

def draw_fluent_app_frame(
    active_step: int = 0,
    active_tab: int = 0,
    console_lines: list = None,
    checkpoint_title: str = "SẴN SÀNG BẮT ĐẦU",
    checkpoint_desc: str = "Bấm nút xanh 'BẮT ĐẦU TỰ ĐỘNG TOÀN BỘ' để khởi động quy trình.",
    checkpoint_color: str = "#059669",
    progress_val: float = 0.0
) -> Image.Image:
    """Renders a pixel-perfect frame of the Windows 11 Fluent gui_app interface."""
    im = Image.new("RGB", (WIDTH, HEIGHT), color="#121214")
    draw = ImageDraw.Draw(im)

    f_title = get_font(12, bold=True)
    f_head = get_font(15, bold=True)
    f_sub = get_font(10)
    f_bold = get_font(11, bold=True)
    f_body = get_font(10)
    f_small = get_font(9)
    f_mono = get_font(10)

    # 1. Windows 11 Title Bar
    draw.rectangle([0, 0, WIDTH, 32], fill="#1c1c1f")
    draw.text((12, 8), "🚀 Google AI Pro 24-Month Automator v1.3.1 · Universal Edition (🪟 Windows (x64))", fill="#d4d4d8", font=f_title)
    
    # Win11 Caption Buttons
    draw.text((WIDTH - 90, 6), "─", fill="#a1a1aa", font=f_bold)
    draw.rectangle([WIDTH - 55, 11, WIDTH - 45, 21], outline="#a1a1aa", width=1)
    draw.text((WIDTH - 25, 7), "✕", fill="#a1a1aa", font=f_bold)
    draw.line([(0, 32), (WIDTH, 32)], fill="#27272a", width=1)

    # 2. Header Bar
    draw.rounded_rectangle([14, 38, WIDTH - 14, 98], radius=8, fill="#18181b", outline="#27272a", width=1)
    draw.text((28, 46), "🚀 Google AI Pro 24-Month Zero-Cost Automator", fill="#f4f4f5", font=f_head)
    draw.text((28, 68), "Tự động hóa cộng dồn 24 tháng 5 TB · Bảo vệ tuyệt đối US$0.00 · Tự động hủy gia hạn & gỡ thẻ", fill="#a1a1aa", font=f_sub)

    # Header Badges
    draw.rounded_rectangle([WIDTH - 150, 52, WIDTH - 28, 80], radius=6, fill="#27272a")
    draw.text((WIDTH - 138, 59), "🪟 Windows (x64)", fill="#e4e4e7", font=f_small)

    draw.rounded_rectangle([WIDTH - 320, 52, WIDTH - 160, 80], radius=6, fill="#14532d")
    draw.text((WIDTH - 308, 59), "🛡️ $0.00 Play Guard: BẬT", fill="#86efac", font=f_small)

    # 3. 4-Stage Stepper Roadmap Bar
    draw.rounded_rectangle([14, 104, WIDTH - 14, 142], radius=8, fill="#18181b", outline="#27272a", width=1)
    steps = [
        ("1", "Đăng Nhập Google", "#38bdf8"),
        ("2", "Nâng Cấp 24 Tháng", "#c084fc"),
        ("3", "Hủy Gia Hạn & Gỡ Thẻ", "#f59e0b"),
        ("4", "Chia Sẻ Gia Đình", "#10b981")
    ]
    step_x = 28
    for i, (num, name, col) in enumerate(steps):
        is_cur = (i == active_step)
        is_done = (i < active_step)
        bg_col = "#0369a1" if is_cur else ("#065f46" if is_done else "#27272a")
        txt_col = "#ffffff" if is_cur else ("#a7f3d0" if is_done else "#71717a")
        badge_col = col if (is_cur or is_done) else "#52525b"

        draw.rounded_rectangle([step_x, 110, step_x + 195, 136], radius=5, fill=bg_col)
        draw.rounded_rectangle([step_x + 4, 114, step_x + 24, 132], radius=3, fill=badge_col)
        draw.text((step_x + 10, 117), num, fill="#000000" if (is_cur or is_done) else "#ffffff", font=f_small)
        draw.text((step_x + 30, 117), name, fill=txt_col, font=f_small)

        if i < 3:
            draw.text((step_x + 204, 116), "➔", fill="#71717a", font=f_small)
        step_x += 238

    # 4. Main Workspace Split (Left: 460px | Right: rest)
    left_w = 460
    left_x1 = 14
    left_x2 = left_x1 + left_w
    right_x1 = left_x2 + 10
    right_x2 = WIDTH - 14
    main_top = 148
    main_bot = HEIGHT - 14

    # Left Container (Tabs & Controls)
    draw.rounded_rectangle([left_x1, main_top, left_x2, main_bot], radius=8, fill="#18181b", outline="#27272a", width=1)
    
    # Tab Buttons
    tabs = ["🧭 Hướng Dẫn Từng Bước", "👥 Nâng Cao", "💡 Hỏi Đáp"]
    tx = left_x1 + 8
    for idx, tname in enumerate(tabs):
        is_tab_act = (idx == active_tab)
        tbg = "#0284c7" if is_tab_act else "#27272a"
        ttxt = "#ffffff" if is_tab_act else "#a1a1aa"
        draw.rounded_rectangle([tx, main_top + 6, tx + 140, main_top + 32], radius=5, fill=tbg)
        draw.text((tx + 10, main_top + 11), tname, fill=ttxt, font=f_small)
        tx += 146

    # Left Tab 0: Wizard Content
    if active_tab == 0:
        # Green 1-Click Banner
        draw.rounded_rectangle([left_x1 + 10, main_top + 40, left_x2 - 10, main_top + 115], radius=6, fill="#064e3b", outline="#059669", width=1)
        draw.text((left_x1 + 18, main_top + 46), "✨ KHUYÊN DÙNG CHO NGƯỜI MỚI (1-CLICK A ĐẾN Z)", fill="#6ee7b7", font=f_bold)
        draw.text((left_x1 + 18, main_top + 64), "Tự động trọn gói: Đăng nhập ➔ 3 tầng 24 tháng ➔ Hủy gia hạn ➔ Gỡ thẻ.", fill="#d1fae5", font=f_small)
        draw.rounded_rectangle([left_x1 + 18, main_top + 82, left_x2 - 18, main_top + 108], radius=5, fill="#059669")
        draw.text((left_x1 + 60, main_top + 87), "🚀 BẮT ĐẦU TỰ ĐỘNG TOÀN BỘ TỪ A ĐẾN Z", fill="#ffffff", font=f_bold)

        # Step 1 Card
        draw.rounded_rectangle([left_x1 + 10, main_top + 122, left_x2 - 10, main_top + 195], radius=6, fill="#202023", outline="#2d2d30", width=1)
        draw.text((left_x1 + 18, main_top + 128), "BƯỚC 1: ĐĂNG NHẬP GOOGLE", fill="#38bdf8", font=f_bold)
        draw.text((left_x1 + 18, main_top + 146), "Bật trình duyệt sạch Edge kèm VPN US. Đăng nhập và xác nhận 2FA.", fill="#a1a1aa", font=f_small)
        draw.rounded_rectangle([left_x1 + 18, main_top + 164, left_x2 - 18, main_top + 188], radius=4, fill="#0284c7")
        draw.text((left_x1 + 110, main_top + 168), "🌐 1. Mở Cửa Sổ Đăng Nhập", fill="#ffffff", font=f_small)

        # Step 2 Card
        draw.rounded_rectangle([left_x1 + 10, main_top + 202, left_x2 - 10, main_top + 300], radius=6, fill="#202023", outline="#2d2d30", width=1)
        draw.text((left_x1 + 18, main_top + 208), "BƯỚC 2: CỘNG DỒN 24 THÁNG ($0.00)", fill="#c084fc", font=f_bold)
        draw.text((left_x1 + 18, main_top + 226), "Cộng dồn 3 tầng: 12M ➔ +6M ➔ +6M (5 TB). Play Guard bảo vệ giá $0.00.", fill="#a1a1aa", font=f_small)
        draw.text((left_x1 + 22, main_top + 246), "☑️ Tự động gỡ sạch thẻ sau khi xong ($0.00)", fill="#e4e4e7", font=f_small)
        draw.text((left_x1 + 22, main_top + 262), "☑️ Tự động chuyển vùng Việt Nam (Bật Family)", fill="#e4e4e7", font=f_small)
        draw.rounded_rectangle([left_x1 + 18, main_top + 276, left_x2 - 18, main_top + 296], radius=4, fill="#7c3aed")
        draw.text((left_x1 + 90, main_top + 280), "▶️ 2. Bắt Đầu Nâng Cấp 24 Tháng", fill="#ffffff", font=f_small)

        # Step 3 Card
        draw.rounded_rectangle([left_x1 + 10, main_top + 308, left_x2 - 10, main_top + 380], radius=6, fill="#202023", outline="#2d2d30", width=1)
        draw.text((left_x1 + 18, main_top + 314), "BƯỚC 3: HỦY GIA HẠN TỰ ĐỘNG & GỠ THẺ BẢO VỆ 0Đ", fill="#fbbf24", font=f_bold)
        draw.text((left_x1 + 18, main_top + 332), "Hủy gia hạn Play để bảo lưu trọn 24T và triệt tiêu mọi phát sinh phí.", fill="#a1a1aa", font=f_small)
        draw.rounded_rectangle([left_x1 + 18, main_top + 350, left_x2 - 18, main_top + 374], radius=4, fill="#d97706")
        draw.text((left_x1 + 105, main_top + 354), "🛡️ 3. Hủy Gia Hạn & Gỡ Thẻ", fill="#ffffff", font=f_small)

        # Step 4 Card
        draw.rounded_rectangle([left_x1 + 10, main_top + 388, left_x2 - 10, main_top + 458], radius=6, fill="#202023", outline="#2d2d30", width=1)
        draw.text((left_x1 + 18, main_top + 394), "BƯỚC 4: CHUYỂN VÙNG VN & GIA ĐÌNH", fill="#34d399", font=f_bold)
        draw.text((left_x1 + 18, main_top + 412), "Mời 5 thành viên gia đình sử dụng chung dung lượng 5 TB.", fill="#a1a1aa", font=f_small)
        draw.rounded_rectangle([left_x1 + 18, main_top + 430, left_x2 - 18, main_top + 452], radius=4, fill="#059669")
        draw.text((left_x1 + 100, main_top + 434), "👨‍👩‍👧‍👦 4. Mời Family Sharing (5 TB)", fill="#ffffff", font=f_small)

    # Right Container (Live Console & Real-Time Monitoring)
    draw.rounded_rectangle([right_x1, main_top, right_x2, main_bot], radius=8, fill="#18181b", outline="#27272a", width=1)

    # Terminal Header
    draw.text((right_x1 + 12, main_top + 10), "📋 Nhật Ký Hoạt Động (Live Terminal)", fill="#f4f4f5", font=f_bold)
    draw.rounded_rectangle([right_x2 - 130, main_top + 8, right_x2 - 76, main_top + 28], radius=4, fill="#27272a")
    draw.text((right_x2 - 122, main_top + 12), "Xóa Log", fill="#a1a1aa", font=f_small)
    draw.rounded_rectangle([right_x2 - 70, main_top + 8, right_x2 - 10, main_top + 28], radius=4, fill="#27272a")
    draw.text((right_x2 - 62, main_top + 12), "📸 Ảnh Chụp", fill="#a1a1aa", font=f_small)

    # Dark Console Window
    term_top = main_top + 36
    term_bot = main_bot - 68
    draw.rounded_rectangle([right_x1 + 8, term_top, right_x2 - 8, term_bot], radius=6, fill="#09090b", outline="#1e1e24", width=1)

    # Draw streaming console lines
    lines = console_lines or []
    ly = term_top + 10
    for tag, msg in lines[-14:]:
        tag_col = "#38bdf8"
        if tag in ["OK", "SUCCESS"]:
            tag_col = "#34d399"
        elif tag == "PLAY-GUARD":
            tag_col = "#fbbf24"
        elif tag == "CHECKPOINT":
            tag_col = "#f59e0b"
        elif tag == "STAGE":
            tag_col = "#c084fc"

        draw.text((right_x1 + 16, ly), f"[{tag}]", fill=tag_col, font=f_mono)
        draw.text((right_x1 + 110, ly), msg[:56], fill="#e4e4e7", font=f_mono)
        ly += 22

    # Bottom Checkpoint Card & Progress Bar
    draw.rounded_rectangle([right_x1 + 8, main_bot - 60, right_x2 - 8, main_bot - 8], radius=6, fill="#202023", outline="#27272a", width=1)
    draw.text((right_x1 + 16, main_bot - 52), checkpoint_title, fill=checkpoint_color, font=f_bold)
    draw.text((right_x1 + 16, main_bot - 34), checkpoint_desc[:65], fill="#a1a1aa", font=f_small)

    # Progress bar
    draw.rounded_rectangle([right_x1 + 16, main_bot - 16, right_x2 - 16, main_bot - 11], radius=3, fill="#27272a")
    fill_w = int((right_x2 - right_x1 - 32) * max(0.02, min(1.0, progress_val)))
    draw.rounded_rectangle([right_x1 + 16, main_bot - 16, right_x1 + 16 + fill_w, main_bot - 11], radius=3, fill=checkpoint_color)

    return im

def generate_quick_start_flow_gif():
    """Renders the complete 4-step wizard execution walkthrough GIF."""
    print("[*] Rendering quick_start_flow.gif reflecting authentic Win11 app...")
    frames = []

    stages = [
        # Frame 1: Ready
        (0, [
            ("INFO", "Hệ thống sẵn sàng. Nhấn Bắt Đầu để khởi động tự động hóa."),
            ("INFO", "Kiểm tra kết nối và cấu hình tài khoản Account_1...")
        ], "SẴN SÀNG BẮT ĐẦU A-Z", "Nhấp nút 'BẮT ĐẦU TỰ ĐỘNG TOÀN BỘ' để kích hoạt.", "#0284c7", 0.05),

        # Frame 2: Step 1 Sign-in
        (0, [
            ("INFO", "Khởi tạo môi trường trình duyệt Microsoft Edge..."),
            ("STAGE", "Kích hoạt tiện ích Browsec VPN US & Offer Injector."),
            ("CHECKPOINT", "Màn hình đăng nhập Google xuất hiện trên desktop."),
            ("INFO", "Cảm biến đang theo dõi phiên đăng nhập...")
        ], "BƯỚC 1: ĐĂNG NHẬP GMAIL", "Đăng nhập Google và xác nhận mã số 2FA trên điện thoại.", "#38bdf8", 0.2),

        # Frame 3: Step 1 Complete -> Auto Resume
        (1, [
            ("RESUME", "Đăng nhập thành công! Cảm biến nhận diện trạng thái."),
            ("INFO", "Tự động kích hoạt quy trình cộng dồn ưu đãi 24 tháng..."),
            ("STAGE", "Đang mở trang ưu đãi Google AI Pro 24M...")
        ], "ĐĂNG NHẬP THÀNH CÔNG", "Tự động chuyển tiếp sang bước nâng cấp 24 tháng...", "#34d399", 0.35),

        # Frame 4: Step 2 Layer 1 (12M)
        (1, [
            ("PLAY-GUARD", "Kiểm tra giá Google Play: US$0.00 / 12 tháng -> HỢP LỆ!"),
            ("STAGE", "Kích hoạt Tầng 1 (12 Tháng AI Pro 2 TB thành công)."),
            ("STAGE", "Chuẩn bị kích hoạt Tầng 2 (Samsung +6M)...")
        ], "BƯỚC 2: TẦNG 1 HOÀN TẤT (12M)", "Play Guard xác thực $0.00. Đang nạp tiếp Tầng 2...", "#c084fc", 0.55),

        # Frame 5: Step 2 Layer 2 & 3 (24M Total)
        (1, [
            ("PLAY-GUARD", "Kiểm tra giá Tầng 2: US$0.00 -> HỢP LỆ (+6 Tháng)."),
            ("PLAY-GUARD", "Kiểm tra giá Tầng 3 (Pixel 5TB): US$0.00 -> HỢP LỆ (+6 Tháng)."),
            ("OK", "ĐÃ CỘNG DỒN ĐỦ 24 THÁNG GOOGLE AI PRO 5 TB!")
        ], "BƯỚC 2: HOÀN TẤT 24 THÁNG 5 TB", "Đủ 24 tháng! Tự động chuyển sang hủy gia hạn...", "#c084fc", 0.75),

        # Frame 6: Step 3 Cancel Renewal & Unlink Card
        (2, [
            ("STAGE", "Mở Google Play Subscriptions để hủy gia hạn định kỳ..."),
            ("OK", "Đã hủy gia hạn thành công! Quyền lợi 24 tháng giữ nguyên $0.00."),
            ("STAGE", "Mở Google Payments / Wallet để tự động gỡ thẻ..."),
            ("OK", "Đã gỡ sạch thẻ ngân hàng! An toàn tuyệt đối 100% Zero-Billing.")
        ], "BƯỚC 3: HỦY GIA HẠN & GỠ THẺ", "Triệt tiêu mọi nguy cơ trừ phí. Thẻ đã được gỡ sạch.", "#f59e0b", 0.90),

        # Frame 7: Complete
        (3, [
            ("OK", "Đã đổi hồ sơ thanh toán về Việt Nam thành công."),
            ("OK", "Sẵn sàng chia sẻ dung lượng 5 TB cho 5 thành viên gia đình."),
            ("SUCCESS", "🎉 CHÚC MỪNG: HOÀN TẤT TOÀN BỘ 24 THÁNG GOOGLE AI PRO 5 TB ($0.00)!")
        ], "🎉 HOÀN TẤT TRỌN GÓI 24 THÁNG", "Tài khoản an toàn 100%. Sẵn sàng mời Family Sharing.", "#10b981", 1.0)
    ]

    for step_idx, logs, title, desc, col, prog in stages:
        img = draw_fluent_app_frame(
            active_step=step_idx,
            active_tab=0,
            console_lines=logs,
            checkpoint_title=title,
            checkpoint_desc=desc,
            checkpoint_color=col,
            progress_val=prog
        )
        # Duplicate frames for smooth timing (1.2 seconds per stage)
        for _ in range(3):
            frames.append(img.convert("P", palette=Image.ADAPTIVE, colors=128))

    out_path = os.path.join(MEDIA_DIR, "quick_start_flow.gif")
    frames[0].save(
        out_path,
        save_all=True,
        append_images=frames[1:],
        duration=400,
        loop=0,
        optimize=True
    )
    print(f"[+] Saved: {out_path} ({os.path.getsize(out_path) / 1024:.2f} KB)")

def generate_step1_login_gif():
    """Renders Step 1 login checkpoint GIF with Edge browser challenge simulation."""
    print("[*] Rendering step1_login_checkpoint.gif reflecting authentic Win11 app...")
    frames = []

    stages = [
        ("MỞ TRÌNH DUYỆT EDGE KÈM VPN", [
            ("INFO", "Khởi chạy Edge profile: profiles/Account_1..."),
            ("STAGE", "Kích hoạt tiện ích IP United States (Browsec VPN)..."),
            ("INFO", "Điều hướng đến accounts.google.com...")
        ], "🌐 Đang mở trình duyệt", "Trình duyệt đang mở trên màn hình của bạn...", "#38bdf8", 0.1),

        ("PHÁT HIỆN XÁC MINH 2FA / SỐ ĐIỆN THOẠI", [
            ("STAGE", "Trang đăng nhập Google đã tải xong."),
            ("CHECKPOINT", "Phát hiện màn hình xác thực 2 bước (2FA Challenge)..."),
            ("CHECKPOINT", "CẢM BIẾN TỰ ĐỘNG TẠM DỪNG: Vui lòng chạm số trên điện thoại.")
        ], "📱 Cảm biến tạm dừng: Xác nhận 2FA", "Chạm số xác nhận trên điện thoại của bạn...", "#f59e0b", 0.25),

        ("CẢM BIẾN NHẬN DIỆN & TỰ ĐỘNG CHẠY TIẾP", [
            ("RESUME", "Đã xác nhận 2FA thành công! Cảm biến tự động thức dậy."),
            ("OK", "Đăng nhập Google hoàn tất. Phiên đăng nhập hợp lệ."),
            ("STAGE", "Tự động chuyển tiếp sang Bước 2: Nâng Cấp 24 Tháng...")
        ], "🟢 Đã đăng nhập thành công", "Cảm biến tự động tiếp tục sang bước nâng cấp...", "#34d399", 0.4)
    ]

    for title, logs, c_title, c_desc, col, prog in stages:
        img = draw_fluent_app_frame(
            active_step=0,
            active_tab=0,
            console_lines=logs,
            checkpoint_title=c_title,
            checkpoint_desc=c_desc,
            checkpoint_color=col,
            progress_val=prog
        )
        for _ in range(4):
            frames.append(img.convert("P", palette=Image.ADAPTIVE, colors=128))

    out_path = os.path.join(MEDIA_DIR, "step1_login_checkpoint.gif")
    frames[0].save(
        out_path,
        save_all=True,
        append_images=frames[1:],
        duration=400,
        loop=0,
        optimize=True
    )
    print(f"[+] Saved: {out_path} ({os.path.getsize(out_path) / 1024:.2f} KB)")

def generate_step2_zero_dollar_gif():
    """Renders Step 2 Zero-Dollar Guard and 3 layers stacking walkthrough GIF."""
    print("[*] Rendering step2_zero_dollar_guard.gif reflecting authentic Win11 app...")
    frames = []

    stages = [
        ("PLAY GUARD XÁC THỰC $0.00 TẦNG 1", [
            ("STAGE", "Kích hoạt Tầng 1: Google AI Pro 2 TB (12 Tháng)..."),
            ("PLAY-GUARD", "Kiểm tra giá Google Play: US$0.00 -> HỢP LỆ!"),
            ("OK", "Tầng 1 (12 Tháng) kích hoạt thành công.")
        ], "TẦNG 1 (12M): US$0.00", "Play Guard xác nhận giá $0.00 trước khi kích hoạt.", "#c084fc", 0.5),

        ("CỘNG DỒN TẦNG 2 & TẦNG 3 ĐỦ 24 THÁNG", [
            ("STAGE", "Kích hoạt Tầng 2: OEM Samsung (+6 Tháng)..."),
            ("PLAY-GUARD", "Tầng 2 giá: US$0.00 -> HỢP LỆ!"),
            ("STAGE", "Kích hoạt Tầng 3: Pixel 5 TB (+6 Tháng)..."),
            ("PLAY-GUARD", "Tầng 3 giá: US$0.00 -> HỢP LỆ!"),
            ("OK", "Tổng cộng quyền lợi: ĐỦ 24 THÁNG 5 TB!")
        ], "CỘNG DỒN ĐỦ 24 THÁNG 5 TB", "Đã cộng dồn thành công 3 tầng ưu đãi.", "#a855f7", 0.75),

        ("HỦY GIA HẠN ĐỊNH KỲ & GỠ SẠCH THẺ", [
            ("STAGE", "Mở Google Play Subscriptions để hủy gia hạn..."),
            ("OK", "Đã hủy gia hạn thành công! Quyền lợi 24 tháng giữ nguyên."),
            ("STAGE", "Mở Google Wallet / Payments để gỡ thẻ..."),
            ("OK", "Đã gỡ sạch thẻ ngân hàng! An toàn tuyệt đối 100% Zero-Billing.")
        ], "HỦY GIA HẠN & GỠ THẺ XONG", "Không phát sinh bất kỳ khoản phí nào định kỳ.", "#f59e0b", 0.95)
    ]

    for title, logs, c_title, c_desc, col, prog in stages:
        img = draw_fluent_app_frame(
            active_step=1 if "CỘNG DỒN" in title else (2 if "HỦY" in title else 1),
            active_tab=0,
            console_lines=logs,
            checkpoint_title=c_title,
            checkpoint_desc=c_desc,
            checkpoint_color=col,
            progress_val=prog
        )
        for _ in range(4):
            frames.append(img.convert("P", palette=Image.ADAPTIVE, colors=128))

    out_path = os.path.join(MEDIA_DIR, "step2_zero_dollar_guard.gif")
    frames[0].save(
        out_path,
        save_all=True,
        append_images=frames[1:],
        duration=400,
        loop=0,
        optimize=True
    )
    print(f"[+] Saved: {out_path} ({os.path.getsize(out_path) / 1024:.2f} KB)")

def main():
    print("=== Generating High-Fidelity Windows 11 Visual Guides ===")
    generate_quick_start_flow_gif()
    generate_step1_login_gif()
    generate_step2_zero_dollar_gif()
    print("[SUCCESS] All 3 guide clips generated successfully!")

if __name__ == "__main__":
    main()
