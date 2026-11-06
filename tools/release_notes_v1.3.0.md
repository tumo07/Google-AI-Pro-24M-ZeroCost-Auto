## 🌟 Google AI Pro 24M Zero-Cost Auto — Release v1.3.0 (Friendly Wizard Edition)

### 🚀 Điểm Mới Trong Phiên Bản v1.3.0:
- **🧭 Tái Cấu Trúc Toàn Diện Trải Nghiệm Người Dùng (Beginner-Friendly UX Overhaul):**
  - **4-Stage Visual Stepper Roadmap**: Lộ trình 4 bước trực quan: `[1. Đăng Nhập] ➔ [2. Nâng Cấp 24T] ➔ [3. Khóa 2028 & Gỡ Thẻ] ➔ [4. Chia Sẻ Gia Đình]`.
  - **Nút Hành Động 1-Click Nổi Bật**: `🚀 BẮT ĐẦU TỰ ĐỘNG TOÀN BỘ TỪ A ĐẾN Z` giúp người mới kích hoạt toàn bộ quy trình mà không cần thao tác từng nút lẻ.
  - **Phân chia 3 Tabs chức năng**:
    - `🧭 Hướng Dẫn Từng Bước (Guided Wizard)`: Giao diện thẻ trực quan với đầy đủ checklist và badge trạng thái.
    - `⚙️ Nâng Cao (Advanced Multi-Account)`: Kích hoạt từng Layer riêng lẻ, đổi cổng CDP 9320 và quản lý tài khoản.
    - `💡 Hỏi Đáp & Trợ Giúp (FAQ)`: Giải đáp cặn kẽ thắc mắc về tạm giữ $0.00, xử lý xác minh 2FA / Captcha và cách chia sẻ 5 TB cho gia đình.
- **🎬 Bộ Clip Hướng Dẫn Trực Quan (Animated Visual Guide Clips):**
  - Tích hợp 3 video hoạt họa GIF siêu nhẹ (`< 200 KB`) vào trực tiếp README và bộ cài:
    1. `docs/media/quick_start_flow.gif`: Trình diễn toàn cảnh luồng tự động hóa 4 bước.
    2. `docs/media/step1_login_checkpoint.gif`: Hướng dẫn đăng nhập và cơ chế cảm biến dừng chờ xác minh 2FA / điện thoại.
    3. `docs/media/step2_zero_dollar_guard.gif`: Minh họa cơ chế bảo vệ Play Guard $0.00 và tự động hủy gia hạn khóa hạn 2028.
- **📦 Tự Động Kiểm Tra & Nạp Thư Viện (Automated Dependency Bootstrapper):**
  - Tích hợp `tools/bootstrap_env.bat` và `tools/check_dependencies.py`.
  - Tự động dò tìm Python chuẩn trên máy, phát hiện thiếu package và tự động gọi `pip install -r requirements.txt`.
  - Tự động tải driver trình duyệt `playwright install chromium` hoàn toàn tự động.
- **🛡️ Khắc Phục Lỗi Phân Quyền & Cú Pháp Batch Shell:**
  - Khắc phục lỗi `0x80070005` (Access Denied PowerShell) bằng kiến trúc Single-Instance Socket Lock thuần Python.
  - Sửa lỗi `'Tu' is not recognized as an internal or external command` trong các tệp `.bat` bằng cách escape ký tự `&` trong lệnh `title`.
  - Khắc phục lỗi thiếu quyền thực thi trên macOS (`Google_AI_Pro_Automator.command`) bằng việc đóng gói sẵn thuộc tính POSIX `0755` (`rwxr-xr-x`) và cung cấp bộ cài ảnh đĩa `.dmg`.

---

### 🔐 Cryptographic Authenticity Verification
Signed using author's official Ed25519 key (`@tumo07`):

```bash
# Xác thực tính toàn vẹn và nguồn gốc chính chủ:
python tools/verify_release.py

# Trích xuất thủy vân bản quyền ẩn chống sao chép bằng AI:
python tools/reveal_watermark.py
```
