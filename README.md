# 🚀 Google AI Pro 24-Month Zero-Cost Stacking Automator

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.10+](https://img.shields.io/badge/Python-3.10%2B-brightgreen.svg)](https://www.python.org/)
[![Playwright](https://img.shields.io/badge/Playwright-CDP%20Automation-orange.svg)](https://playwright.dev/)
[![Verified Author](https://img.shields.io/badge/Author-tumo07-purple.svg)](https://github.com/tumo07)
[![Cryptographically Signed](https://img.shields.io/badge/Release-Ed25519%20Signed-success.svg)](tools/verify_release.py)

**Google AI Pro 24M Zero-Cost Auto** là bộ công cụ mã nguồn mở tự động hóa quy trình nghiên cứu cấu trúc gói đăng ký Google One / Google AI Pro (5 TB) và YouTube Premium 24 tháng với cơ chế bảo vệ nghiêm ngặt **US$0.00 (Zero-Billing Price Guard)**.

---

## 🌟 Tính Năng Nổi Bật (Key Features)

- **🛡️ Tuyệt Đối 0 Đồng (Zero-Billing Guarantee):** Tích hợp bộ kiểm soát giá đa tầng (`play_guard.js` & `automation_engine.py`). Chỉ thực hiện thao tác khi màn hình Google Play Checkout xác nhận hiển thị chính xác **$0.00 / Miễn phí**.
- **🧩 Extension Đã Bản Địa Hóa Tiếng Việt:** Toàn bộ tiện ích mở rộng (`extensions/google_pro_6_12_24`) được dịch và thiết kế lại 100% bằng Tiếng Việt, hiển thị hướng dẫn chi tiết từng bước và trạng thái kích hoạt thời gian thực.
- **🔄 Đa Tầng Cộng Dồn (Multi-Layer Stacking Engine):**
  - **Tầng 1 (12 tháng):** Khởi tạo gói đăng ký Google AI Pro 2 TB + YouTube Premium Add-on.
  - **Tầng 2 (6 tháng):** Cộng dồn ưu đãi OEM Samsung (SS) kéo dài lên 18 tháng.
  - **Tầng 3 (6 tháng):** Nâng cấp gói 5 TB / kết hợp ưu đãi, khóa mốc đủ 24 tháng (hạn sử dụng đến năm 2028).
  - **Bước 5 (Khóa hạn 2028):** Tự động điều hướng sang Google Play để hủy gia hạn định kỳ, triệt tiêu mọi nguy cơ trừ tiền hàng tháng mà vẫn bảo lưu trọn vẹn 24 tháng quyền lợi.
- **🇻🇳 Sẵn Sàng Cho Chia Sẻ Gia Đình (Vietnam Family Sharing Ready):** Tự động hướng dẫn và chuyển vùng hồ sơ để kích hoạt Google One Family Sharing cho các tài khoản thành viên tại Việt Nam.
- **🔐 Chữ Ký Số Mã Hóa Ed25519 (Cryptographically Signed):** Toàn bộ mã nguồn phát hành được bảo vệ và xác thực bằng chữ ký số bất đối xứng Ed25519 của tác giả (@tumo07), chống giả mạo, tráo đổi mã độc hoặc chiếm đoạt bản quyền.

---

## 🏗️ Kiến Trúc Hệ Thống (Architecture)

```mermaid
flowchart TD
    A["Desktop GUI / CLI Controller<br/>(gui_app.py / engine_stacker.py)"] --> B["Microsoft Edge with Remote CDP (Port 9320)"]
    B --> C["Xi Offer Injector Extension (Vietnamese Edition)"]
    C -->|Intercepts RPC 'Ngbm'| D["Google One (one.google.com)"]
    C -->|Modifies 'ear' query parameter| E["Play Checkout (tokenized.play.google.com)"]
    E --> F{"Play Guard Check:<br/>Is amount == US$0.00?"}
    F -->|YES: Green Banner| G["Proceed with Zero-Cost Subscription"]
    F -->|NO: Red Banner| H["ABORT: Halt immediately to protect funds"]
    G --> I["Google Play Subscriptions (play.google.com)"]
    I --> J["Cancel Auto-Renew -> Lock 24 Months until 2028"]
```

---

## 📋 Yêu Cầu Hệ Thống (Prerequisites)

1. **Hệ điều hành:** Windows 10 / 11 (64-bit).
2. **Trình duyệt:** Microsoft Edge hoặc Google Chrome đã cài đặt mặc định.
3. **Python:** Phiên bản 3.10 trở lên ([python.org](https://www.python.org/downloads/)). Nhớ tích chọn **"Add Python to PATH"** khi cài đặt.
4. **Thẻ thanh toán quốc tế:** Visa hoặc Mastercard hỗ trợ thanh toán quốc tế và mở chiều thanh toán trực tuyến (Thẻ chỉ dùng để xác thực danh tính với Google $0.00 Temporary Hold, hoàn toàn không trừ tiền).

---

## ⚡ Hướng Dẫn Cài Đặt & Sử Dụng (Quick Start)

### 1. Cài đặt thư viện phụ thuộc
Mở PowerShell hoặc Command Prompt tại thư mục dự án và chạy:
```powershell
pip install -r requirements.txt
python -m playwright install chromium
```

### 2. Cấu hình mẫu (`config.json`)
Sao chép file mẫu `config.example.json` thành `config.json` và điền thông tin của bạn:
```powershell
copy config.example.json config.json
```
Nội dung file `config.json`:
```json
{
  "target_region": "US",
  "target_plan": "pro_2year_zero",
  "auto_cancel": true,
  "use_vpn": true,
  "card": {
    "number": "4000000000000000",
    "exp_month": "12",
    "exp_year": "28",
    "cvc": "000",
    "holder": "NGUYEN VAN A",
    "address_line1": "700 SW 5th Ave",
    "postal_code": "97201",
    "locality": "Portland",
    "province": "OR",
    "country": "US"
  },
  "accounts": [
    {
      "id": "Account_1",
      "email": "your_account@gmail.com",
      "status": "pending_login",
      "current_step": 0
    }
  ]
}
```
*(Ghi chú: Mã bưu chính 97201 là vùng miễn thuế bang Oregon, Hoa Kỳ).*

### 3. Khởi chạy ứng dụng
Chạy giao diện trực quan:
```powershell
python gui_app.py
```
Hoặc chạy trực tiếp file khởi động tiện lợi:
- **`start_gui.bat`**: Khởi chạy giao diện điều khiển Desktop hiện đại.

---

## 🔒 Xác Minh Chữ Ký Số Bản Phát Hành (Release Verification)

Để đảm bảo bạn đang sử dụng phiên bản chính chủ từ tác giả **Trinh Dang Khoa (@tumo07)** và không bị chèn mã độc bởi các bên reup trái phép, hãy chạy lệnh xác minh:

```powershell
python tools/verify_release.py
```

Kết quả hợp lệ sẽ hiển thị:
```text
======================================================================
  Google AI Pro 24M Zero-Cost Auto — Authenticity Verification
  Author: Trinh Dang Khoa (Alex Trinh) <tumo07@io.vn> | GitHub: @tumo07
======================================================================
[+] [1/2] DIGITAL SIGNATURE VERIFIED: Authentic cryptographic signature from author (@tumo07).
[+] [2/2] INTEGRITY VERIFIED: All repository files match official SHA-256 hashes.

>>> VERIFICATION PASSED: Genuine, Untampered Open-Source Release. <<<
```

---

## 🛡️ Cam Kết Bảo Mật (Security & Privacy)

- **Không lưu trữ bí mật:** Mã nguồn không chứa bất kỳ máy chủ thu thập dữ liệu (no telemetry, no analytics, no external C2).
- **Mã nguồn mở 100%:** Toàn bộ logic script và extension ở dạng văn bản rõ (plain JavaScript/Python), bất kỳ ai cũng có thể đọc và audit trước khi sử dụng.
- **Tránh rò rỉ thông tin cá nhân:** File `config.local.json`, cache trình duyệt và hồ sơ phiên đăng nhập đều được loại trừ trong `.gitignore`.

---

## 📜 Giấy Phép (License)

Dự án được phân phối dưới giấy phép [MIT License](LICENSE).
Bản quyền thuộc về **© 2026 Trinh Dang Khoa (Alex Trinh) <tumo07@io.vn>**.

---

## ⚠️ Tuyên Bố Miễn Trừ Trách Nhiệm (Disclaimer)

Dự án này được tạo ra cho mục đích nghiên cứu học thuật về giao thức phân phối ưu đãi OEM và thử nghiệm tự động hóa giao diện trình duyệt. Tác giả không chịu trách nhiệm đối với bất kỳ việc sử dụng sai mục đích nào vi phạm Điều khoản dịch vụ của bên thứ ba.
