# 📝 Nhật Ký Thay Đổi (Changelog)

Toàn bộ các thay đổi, tính năng mới và cải tiến của dự án **Google AI Pro 24M Zero-Cost Auto** được ghi nhận chi tiết tại đây theo chuẩn [Keep a Changelog](https://keepachangelog.com/).

---

## [v1.3.0] - 2026-11-06

### 🧭 Tái Cấu Trúc Toàn Diện Trải Nghiệm Người Dùng (Beginner-Friendly UX Overhaul)
- **🚀 Giao Diện Hướng Dẫn Wizard 4 Bước (Guided Stepper Roadmap):**
  - Trực quan hóa quy trình bằng thanh tiến trình trực quan: `[1. Đăng Nhập] ➔ [2. Nâng Cấp 24T] ➔ [3. Khóa 2028 & Gỡ Thẻ] ➔ [4. Chia Sẻ Gia Đình]`.
  - Bổ sung nút hành động 1-Click nổi bật: **`🚀 BẮT ĐẦU TỰ ĐỘNG TOÀN BỘ TỪ A ĐẾN Z`** dành cho người mới không cần cấu hình phức tạp.
  - Tách bạch rõ ràng 3 phân hệ: `🧭 Hướng Dẫn Từng Bước (Wizard)`, `⚙️ Nâng Cao (Advanced Multi-Account)`, và `💡 Hỏi Đáp & Trợ Giúp (FAQ)`.
- **🎬 Bộ Clip Hướng Dẫn Trực Quan (Animated Visual Guide Clips):**
  - Tích hợp 3 video hướng dẫn dạng ảnh động tối ưu hóa siêu nhẹ (`< 200 KB`) trực tiếp vào tài liệu và ứng dụng:
    - `quick_start_flow.gif`: Trình diễn toàn bộ dòng chảy tự động hóa từ A đến Z.
    - `step1_login_checkpoint.gif`: Hướng dẫn đăng nhập và vượt mã xác nhận 2FA trên điện thoại.
    - `step2_zero_dollar_guard.gif`: Minh họa lá chắn an toàn $0.00, cộng dồn 3 gói và hủy gia hạn.
- **📦 Tự Động Kiểm Tra & Nạp Thư Viện (Automated Dependency Bootstrapper):**
  - Khởi chạy script tự động dò tìm Python chuẩn trên máy, phát hiện thiếu thư viện và tự động gọi `pip install -r requirements.txt`.
  - Tự động tải browser driver `playwright install chromium` mà không đòi hỏi người dùng phải gõ lệnh terminal thủ công.
- **🛡️ Khắc Phục Lỗi Phân Quyền & Cú Pháp Batch Shell:**
  - Khắc phục lỗi `0x80070005` (Access Denied PowerShell) bằng kiến trúc Single-Instance Socket Lock thuần Python.
  - Sửa lỗi `'Tu' is not recognized as an internal or external command` trong các tệp `.bat` bằng cách escape ký tự `&` trong lệnh `title`.
  - Khắc phục lỗi thiếu quyền thực thi trên macOS (`Google_AI_Pro_Automator.command`) bằng việc đóng gói sẵn thuộc tính POSIX `0755` (`rwxr-xr-x`) và cung cấp bộ cài ảnh đĩa `.dmg`.

---

## [v1.2.0] - 2026-11-06

### 🍎 Hỗ Trợ Toàn Diện Cho macOS (Apple Silicon M1-M4 & Intel Universal)
- **🚀 Tương Thích Hoàn Hảo Cả 2 Kiến Trúc Apple Silicon (arm64) & Intel (x86_64):**
  - Tự động nhận diện cấu trúc phần cứng máy Mac (`uname -m` ➔ `arm64` cho dòng chip Apple M1/M2/M3/M4 hoặc `x86_64` cho Intel).
  - Điều chỉnh tương thích toàn bộ hệ thống lõi: `automation_engine.py`, `engine_stacker.py`, `launch_interactive_instance.py`.
- **🖥️ Tự Động Định Vị Trình Duyệt macOS (macOS Native Browser Discovery):**
  - Quét và nhận diện tự động các trình duyệt trong thư mục `/Applications`: **Google Chrome**, **Microsoft Edge**, **Brave Browser**, **Arc**, **Chromium** (bao gồm cả thư mục `~/Applications`).
  - Tự động fallback linh hoạt sang biến môi trường `$PATH` (`shutil.which`).
- **🪟 Khởi Chạy Cửa Sổ Trực Tiếp Trên Màn Hình macOS (Aqua Window Management):**
  - Khởi động trình duyệt độc lập với đầy đủ tham số Remote CDP (Port 9320), nạp tiện ích mở rộng Browsec VPN và bộ Offer Injector qua tiến trình `start_new_session=True` và lệnh dự phòng `open -a`.
  - Quản lý cổng CDP bằng `lsof -ti :9320` và tín hiệu POSIX `SIGKILL` chuyên dụng trên môi trường UNIX/macOS.
- **⚡ Bộ Trình Khởi Chạy 1-Click Dành Riêng Cho Mac:**
  - `Google_AI_Pro_Automator.command`: File thực thi trực tiếp bằng 1 cú click chuột (Double-Click) trong Finder của macOS, tự động khởi tạo môi trường và mở giao diện ứng dụng.
  - `setup_macos.sh`: Kịch bản cài đặt tự động, kiểm tra phiên bản Python 3, tạo môi trường ảo `.venv`, cài đặt Playwright Chromium driver và cấp quyền thực thi.
  - `run_gui.sh` & `run_stacker.sh`: Bộ lệnh khởi chạy trực tiếp qua Terminal (GUI hoặc CLI).
- **🎨 Giao Diện Đa Nền Tảng Universal Fluent & Aqua GUI (`gui_app.py`):**
  - Hiển thị huy hiệu nhận diện hệ điều hành và vi kiến trúc thời gian thực: `🍎 macOS (Apple Silicon arm64)` hoặc `🍎 macOS (Intel x86_64)` hoặc `🪟 Windows (x64)`.
  - Tối ưu hóa phông chữ bản địa: chuẩn **SF Pro Display / SF Pro Text** trên macOS và **Segoe UI Variable** trên Windows.
  - Xử lý tiến trình chạy đơn (`ensure_single_instance`) bằng `pgrep -f` trên macOS/UNIX.

---

## [v1.1.0] - 2026-11-06

### 🌟 Tính Năng Mới (Added)
- **💳 Quy Trình Tự Động Gỡ Thẻ Toàn Diện (Automated Card Unlinking Workflow):**
  - Tích hợp phương thức `unlink_all_cards()` trong `engine_stacker.py`, `gui_app.py` và giao diện tiện ích `popup.html`.
  - Tự động hóa việc điều hướng đến Google Wallet (`wallet.google.com`) và Google Payments Center để gỡ bỏ triệt để thẻ ngân hàng (`Visa-2217`, `Visa-7551`...) sau khi gói 24 tháng đã được chốt mốc năm 2028.
  - Đảm bảo **100% Zero-Billing Risk** — không còn thẻ lưu trên hệ thống, không có bất kỳ rủi ro phát sinh phí định kỳ.
- **🌐 Hỗ Trợ Đa Trình Duyệt & Chrome Fallback (Multi-Browser Support):**
  - Tự động nhận diện trình duyệt có sẵn trên Windows theo thứ tự ưu tiên: **Microsoft Edge ➔ Google Chrome ➔ Brave**.
  - Bổ sung cờ bypass `--disable-extensions-except` và cơ chế nạp CDP init script in-page để tiện ích mở rộng hoạt động ổn định trên cả Chrome và Edge.
- **💬 Hộp Thoại Hướng Dẫn Trực Quan Trong Trình Duyệt (In-Browser Guidance Modals):**
  - Tích hợp hàm `show_guidance_popup()` hiển thị thông báo hướng dẫn từng bước trực tiếp trên tab trình duyệt của người dùng, giúp nắm rõ các bước cần làm (như xác nhận 2FA trên điện thoại, kiểm tra giá 0 đồng).
- **🔒 Mã Hóa Thủy Vân Chống Trộm Bằng AI (AI-Resistant Steganographic Watermark):**
  - Nhúng thủy vân vô hình Zero-Width Unicode (`U+200B`, `U+200C`, `U+200D`, `U+FEFF`) và con dấu bất biến cryptographic invariant seal (`0x2e1ff517`) trên 6 file lõi của dự án.
  - Đi kèm công cụ kiểm tra bản quyền tác giả: `tools/reveal_watermark.py` (chứng minh quyền tác giả Trịnh Đăng Khoa / `@tumo07` ngay cả khi code bị AI viết lại).

### 🛠️ Cải Tiến & Sửa Lỗi (Improved & Fixed)
- Cập nhật giao diện Desktop Fluent GUI v1.1.0 với hiển thị trạng thái từng bước rõ ràng hơn.
- Cập nhật tài liệu hướng dẫn [`HUONG_DAN_CHI_TIET.md`](HUONG_DAN_CHI_TIET.md) và [`README.md`](README.md) phản ánh quy trình gỡ thẻ và giải pháp Chrome.
- Cập nhật bảng kiểm tra mã băm SHA-256 (`CHECKSUMS.sha256`) và chữ ký số Ed25519 (`CHECKSUMS.sha256.sig`).

---

## [v1.0.0] - 2026-11-05

### 🚀 Phát Hành Đầu Tiên (Initial Open-Source Release)
- **Tự động hóa cộng dồn 24 tháng Google AI Pro (5 TB):** Tầng 1 (12 tháng), Tầng 2 (6 tháng), Tầng 3 (6 tháng).
- **Tuyệt đối 0 đồng (Zero-Billing Price Guard):** Giám sát giá qua `play_guard.js`, chỉ tiếp tục khi giá là US$0.00.
- **Bản địa hóa 100% Tiếng Việt:** Toàn bộ extension `extensions/google_pro_6_12_24` được dịch và loại bỏ hoàn toàn tiếng Trung.
- **Bảo vệ chữ ký số Ed25519:** Đi kèm bộ công cụ ký số `tools/sign_release.py` và thẩm định `tools/verify_release.py`.
- **Giấy phép MIT:** Phát hành mã nguồn mở minh bạch dưới giấy phép MIT License.
