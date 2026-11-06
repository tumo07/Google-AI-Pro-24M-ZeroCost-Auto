import os
import glob
from PIL import Image, ImageDraw, ImageFont

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_DIR = os.path.join(BASE_DIR, "docs", "media")
os.makedirs(MEDIA_DIR, exist_ok=True)

FFMPEG_PATHS = glob.glob(os.path.expanduser("~") + r"\AppData\Local\ms-playwright\ffmpeg*\ffmpeg*.exe")
FFMPEG_BIN = FFMPEG_PATHS[0] if FFMPEG_PATHS else "ffmpeg"

print(f"Generating guide clips into: {MEDIA_DIR}")
print(f"Using FFmpeg: {FFMPEG_BIN}")

# Base dimensions for our visual guides (16:9 ratio, 960x540 for high performance & crisp rendering)
WIDTH = 960
HEIGHT = 540

def get_font(size: int, bold: bool = False):
    try:
        font_name = "segoeuib.ttf" if bold else "segoeui.ttf"
        return ImageFont.truetype(font_name, size)
    except Exception:
        try:
            return ImageFont.truetype("arialbd.ttf" if bold else "arial.ttf", size)
        except Exception:
            return ImageFont.load_default()

def draw_window_frame(draw, title: str):
    # Dark modern window background
    draw.rectangle([0, 0, WIDTH, HEIGHT], fill="#121214")
    # Top title bar
    draw.rectangle([0, 0, WIDTH, 48], fill="#18181b")
    # Traffic lights (macOS / modern UI)
    draw.ellipse([16, 18, 28, 30], fill="#ef4444")
    draw.ellipse([34, 18, 46, 30], fill="#f59e0b")
    draw.ellipse([52, 18, 64, 30], fill="#10b981")
    # Title
    font_title = get_font(14, bold=True)
    draw.text((80, 15), title, fill="#f4f4f5", font=font_title)

def create_overview_clip():
    """Creates an animated guide clip showcasing the complete 4-step wizard workflow."""
    frames = []
    
    stages = [
        ("BƯỚC 1: KHỞI TẠO & ĐĂNG NHẬP GMAIL",
         "Nhấp 'Mở Cửa Sổ Đăng Nhập' để bật trình duyệt sạch kèm VPN US.\nĐăng nhập tài khoản Google và xác nhận 2FA trên điện thoại.",
         "#0284c7", "🚀 1. Mở Cửa Sổ Đăng Nhập", "🟡 Trạng thái: Đang chờ đăng nhập..."),
        
        ("BƯỚC 2: CỘNG DỒN 24 THÁNG ($0.00)",
         "Công cụ tự động kích hoạt 3 tầng ưu đãi:\nTầng 1 (12M) ➔ Tầng 2 (SS +6M) ➔ Tầng 3 (Pixel +6M) = Đủ 24 Tháng 5 TB.",
         "#7c3aed", "▶️ 2. Bắt Đầu Nâng Cấp 24 Tháng", "🟢 Trạng thái: Play Guard xác nhận US$0.00"),
         
        ("BƯỚC 3: KHÓA HẠN 2028 & HỦY PHÍ ĐỊNH KỲ",
         "Hủy gia hạn tự động trên Google Play để khóa cứng quyền lợi đến 2028.\nTriệt tiêu hoàn toàn nguy cơ bị trừ phí YouTube Premium $11.99/tháng.",
         "#d97706", "🛡️ 3. Hủy Gia Hạn (Khóa 2028)", "🟡 Trạng thái: Đã hủy gia hạn thành công"),
         
        ("BƯỚC 4: GỠ THẺ BẢO VỆ 0 ĐỒNG & CHIA SẺ GIA ĐÌNH",
         "Tự động gỡ sạch thẻ thanh toán khỏi Google Payments (100% Zero-Billing).\nChuyển vùng về Việt Nam để chia sẻ dung lượng 5 TB cho cả gia đình.",
         "#059669", "🎉 4. Hoàn Tất 24 Tháng Google AI Pro", "🟢 Trạng thái: Tài khoản an toàn tuyệt đối 0đ!")
    ]

    for idx, (stage_title, stage_desc, accent_color, btn_text, status_msg) in enumerate(stages):
        # Generate 4-6 frames per stage with subtle pulse / progress
        for f in range(6):
            img = Image.new("RGB", (WIDTH, HEIGHT), "#121214")
            draw = ImageDraw.Draw(img)
            draw_window_frame(draw, "Google AI Pro 24M Automator · Hướng Dẫn Nhanh Cho Người Mới")
            
            # Draw Stepper Header
            stepper_y = 60
            draw.rectangle([20, stepper_y, WIDTH - 20, stepper_y + 44], fill="#18181b", outline="#27272a", width=1)
            
            step_names = ["1. Đăng Nhập", "2. Nâng Cấp 24T", "3. Khóa 2028", "4. Chia Sẻ VN"]
            for s_i, s_name in enumerate(step_names):
                s_x = 40 + s_i * 220
                is_active = (s_i == idx)
                is_past = (s_i < idx)
                
                pill_bg = "#0369a1" if is_active else ("#065f46" if is_past else "#27272a")
                txt_col = "#ffffff" if is_active else ("#a7f3d0" if is_past else "#71717a")
                
                draw.rectangle([s_x, stepper_y + 8, s_x + 180, stepper_y + 36], fill=pill_bg, outline="#3f3f46", width=1)
                font_step = get_font(12, bold=True)
                check_icon = "✓ " if is_past else ("▶ " if is_active else "• ")
                draw.text((s_x + 12, stepper_y + 13), check_icon + s_name, fill=txt_col, font=font_step)

            # Left Card: Action Card
            card_x, card_y, card_w, card_h = 24, 120, 480, 390
            draw.rectangle([card_x, card_y, card_x + card_w, card_y + card_h], fill="#18181b", outline=accent_color, width=2)
            
            # Card Badge
            draw.rectangle([card_x + 16, card_y + 16, card_x + 120, card_y + 40], fill=accent_color)
            draw.text((card_x + 24, card_y + 20), f"BƯỚC {idx + 1}/4", fill="#ffffff", font=get_font(12, bold=True))
            
            # Card Title
            draw.text((card_x + 16, card_y + 52), stage_title, fill="#ffffff", font=get_font(15, bold=True))
            
            # Card Desc
            draw.text((card_x + 16, card_y + 86), stage_desc, fill="#d4d4d8", font=get_font(12))
            
            # Simulated Big Action Button
            btn_y = card_y + 190
            draw.rectangle([card_x + 16, btn_y, card_x + card_w - 16, btn_y + 48], fill=accent_color)
            draw.text((card_x + 36, btn_y + 14), btn_text, fill="#ffffff", font=get_font(14, bold=True))
            
            # Checkbox indicator
            draw.rectangle([card_x + 18, card_y + 260, card_x + 32, card_y + 274], fill="#0284c7")
            draw.text((card_x + 21, card_y + 260), "✓", fill="#ffffff", font=get_font(10, bold=True))
            draw.text((card_x + 40, card_y + 260), "Tự động gỡ sạch thẻ thanh toán (Bảo vệ tuyệt đối 0đ)", fill="#e4e4e7", font=get_font(11))
            
            draw.rectangle([card_x + 18, card_y + 290, card_x + 32, card_y + 304], fill="#0284c7")
            draw.text((card_x + 21, card_y + 290), "✓", fill="#ffffff", font=get_font(10, bold=True))
            draw.text((card_x + 40, card_y + 290), "Tự động đổi vùng Việt Nam (Bật Family Sharing)", fill="#e4e4e7", font=get_font(11))
            
            # Right Panel: Live Monitor Card
            mon_x, mon_y, mon_w, mon_h = 520, 120, 416, 390
            draw.rectangle([mon_x, mon_y, mon_x + mon_w, mon_y + mon_h], fill="#18181b", outline="#27272a", width=1)
            
            # Status Alert Pill in Monitor
            draw.rectangle([mon_x + 16, mon_y + 16, mon_x + mon_w - 16, mon_y + 80], fill="#1e293b", outline=accent_color, width=1)
            draw.text((mon_x + 26, mon_y + 26), status_msg, fill="#38bdf8", font=get_font(13, bold=True))
            draw.text((mon_x + 26, mon_y + 50), "Hệ thống tự động điều khiển trình duyệt qua Remote CDP...", fill="#94a3b8", font=get_font(11))
            
            # Progress bar
            progress_pct = (idx * 25) + int((f / 6.0) * 25)
            draw.text((mon_x + 16, mon_y + 96), f"Tiến trình tổng thể: {progress_pct}%", fill="#a1a1aa", font=get_font(11, bold=True))
            draw.rectangle([mon_x + 16, mon_y + 116, mon_x + mon_w - 16, mon_y + 126], fill="#27272a")
            bar_fill_w = int((mon_w - 32) * (progress_pct / 100.0))
            if bar_fill_w > 0:
                draw.rectangle([mon_x + 16, mon_y + 116, mon_x + 16 + bar_fill_w, mon_y + 126], fill=accent_color)
                
            # Simulated Console Output Box
            draw.rectangle([mon_x + 16, mon_y + 140, mon_x + mon_w - 16, mon_y + mon_h - 16], fill="#09090b", outline="#27272a", width=1)
            sample_logs = [
                f"[INFO] Khởi động trình duyệt Edge với remote CDP port 9320",
                f"[INFO] Kết nối Browsec VPN Hoa Kỳ (US) - Đã xác thực",
                f"[BƯỚC] Đang nạp Xi Offer Injector Extension (Bản Tiếng Việt)",
                f"[KIỂM TRA] Giá Play Checkout: US$0.00 (Play Guard: OK)",
                f"[TIẾP TỤC] Hoàn tất Tầng {min(idx + 1, 3)} - Hạn mức nâng lên tương ứng"
            ]
            for l_i, l_text in enumerate(sample_logs[:idx + 2]):
                draw.text((mon_x + 24, mon_y + 152 + l_i * 26), l_text, fill="#e4e4e7", font=get_font(10))

            frames.append(img)
            
    # Save as high-quality GIF
    gif_path = os.path.join(MEDIA_DIR, "quick_start_flow.gif")
    frames[0].save(
        gif_path,
        save_all=True,
        append_images=frames[1:],
        duration=900,  # 0.9s per frame
        loop=0,
        optimize=True
    )
    print(f"[OK] Generated animated walkthrough: {gif_path} ({os.path.getsize(gif_path) / 1024:.2f} KB)")
    
    # Also compile to MP4 using FFmpeg if available
    mp4_path = os.path.join(MEDIA_DIR, "quick_start_flow.mp4")
    if os.path.exists(FFMPEG_BIN):
        import subprocess
        cmd = [
            FFMPEG_BIN, "-y",
            "-i", gif_path,
            "-movflags", "faststart",
            "-pix_fmt", "yuv420p",
            "-vf", "scale=trunc(iw/2)*2:trunc(ih/2)*2",
            mp4_path
        ]
        try:
            subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print(f"[OK] Compiled video clip: {mp4_path} ({os.path.getsize(mp4_path) / 1024:.2f} KB)")
        except Exception as e:
            print(f"[-] FFmpeg conversion note: {e}")

if __name__ == "__main__":
    create_overview_clip()
