## 🌟 Google AI Pro 24M Zero-Cost Auto — Release v1.3.1 (Fluent Design & Multi-Account Edition)

### 🚀 Điểm Mới Trong Phiên Bản v1.3.1:
- **🪟 Chuẩn Hóa Windows 11 Fluent Theme & DWM Titlebar:**
  - Tích hợp hàm `_apply_fluent_theme` kích hoạt `DWMWA_USE_IMMERSIVE_DARK_MODE` và góc bo tròn `DWMWA_WINDOW_CORNER_PREFERENCE` trên Windows 11.
  - Áp dụng bảng màu Fluent Dark hiện đại (`#18181b` / `#202023`) kèm viền thẻ tinh tế và phông chữ chuẩn bản địa `Segoe UI Variable`.
  - Khắc phục triệt để lỗi xung đột cổng socket bằng **Windows Kernel Named Mutex** (`Local\GoogleAIProAutomatorLock_tumo07`), miễn nhiễm 100% với dải cổng loại trừ của Hyper-V / WinNAT (`WinError 10013`).
- **👥 Nâng Cấp Quản Lý Đa Tài Khoản Mạnh Mẽ (Robust Multi-Account Manager):**
  - Bổ sung tùy chọn **`🗑️ Xóa Tài Khoản Này`**: Xóa tài khoản khỏi cấu hình và tự động giải phóng thư mục lưu trữ profile.
  - Bổ sung tùy chọn **`🧹 Reset Session / Dọn Cache`**: Làm sạch toàn bộ cookie và phiên duyệt web của tài khoản để đăng nhập lại sạch sẽ.
  - Bổ sung tùy chọn **`📂 Mở Thư Mục Profile`**: Mở trực tiếp thư mục lưu trữ profile của tài khoản trong File Explorer.
  - Hiển thị nhãn thông tin chi tiết: ID tài khoản đang chọn, đường dẫn lưu trữ và trạng thái phiên.
- **✨ Chuẩn Hóa Lại Câu Chữ Bước 3 (Hủy Gia Hạn Tự Động & Gỡ Thẻ):**
  - Loại bỏ hoàn toàn cụm từ gây hiểu nhầm "Khóa 2028".
  - Chuyển thành tên chính xác và dễ hiểu: **`BƯỚC 3: HỦY GIA HẠN TỰ ĐỘNG & GỠ THẺ BẢO VỆ 0Đ`** (bảo lưu trọn vẹn thời hạn 24 tháng và triệt tiêu nguy cơ phát sinh phí).
- **🎬 Cập Nhật Bộ 3 Media Clip Chuẩn Xác Theo Giao Diện Ứng Dụng:**
  - Kết xuất lại toàn bộ 3 video hướng dẫn trực quan dạng ảnh động GIF:
    1. `docs/media/quick_start_flow.gif`: Trình diễn toàn cảnh luồng tự động hóa 4 bước trên giao diện Windows 11.
    2. `docs/media/step1_login_checkpoint.gif`: Hướng dẫn đăng nhập và cơ chế cảm biến dừng chờ xác minh 2FA / điện thoại.
    3. `docs/media/step2_zero_dollar_guard.gif`: Minh họa cơ chế bảo vệ Play Guard $0.00 và tự động hủy gia hạn bảo lưu 24T.

---

### 🔐 Cryptographic Authenticity Verification
Signed using author's official Ed25519 key (`@tumo07`):

```bash
# Xác thực tính toàn vẹn và nguồn gốc chính chủ:
python tools/verify_release.py

# Trích xuất thủy vân bản quyền ẩn chống sao chép bằng AI:
python tools/reveal_watermark.py
```
