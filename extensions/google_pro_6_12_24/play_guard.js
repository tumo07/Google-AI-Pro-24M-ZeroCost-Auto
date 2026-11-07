/*
 * Google AI Pro 24M Offer Injector — Checkout Price Guard
 * Inspects checkout terms inside Play acquire iframe to verify US$0.00 zero billing.
 * Shows green banner if free trial is verified, red banner if charges detected.
 * Developed & Maintained by Trinh Dang Khoa (Alex Trinh) <tumo07@io.vn>
 * Licensed under the MIT License.
 */
(() => {
  if (window.__GAPT_GUARD || window.top === window || (!location.href.includes("eacquire") && !location.href.includes("tokenized.play.google.com")) || location.href.includes("instrumentmanager")) return; // Only run inside Play iframe
  window.__GAPT_GUARD = true;

  const FREE_WORDS = [
    "free trial", "start your free trial", "dùng thử miễn phí", "bắt đầu dùng thử miễn phí",
    "miễn phí", "US$0.00", "$0.00", "0,00", "€0.00", "0 đ", "0đ", "các khoản phí sắp tới", "ngày bắt đầu:", "starting on", "nhận điểm google play", "sau khi đăng ký", "đã đăng ký",
    "won't be charged", "sẽ không bị tính phí", "﻿​‌​​​​​‌​‌​‌​‌​‌​‌​‌​‌​​​‌​​‌​​​​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌‌‌‌‌​‌​‌​‌‌‌​‌​​​​​‌​‌​‌​‌​​​‌​​​‌​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​​​‌​‌​‌​​‌​​‌​​‌​‌‌​​‌‌‌​‌​​​‌​​​​​​‌​​​​‌‌​‌‌​‌‌‌‌​‌‌‌​​​​​‌‌‌‌​​‌​‌‌‌​​‌​​‌‌​‌​​‌​‌‌​​‌‌‌​‌‌​‌​​​​‌‌‌​‌​​​​‌​​​​​​​‌​‌​​​​‌‌​​​‌‌​​‌​‌​​‌​​‌​​​​​​​‌‌​​‌​​​‌‌​​​​​​‌‌​​‌​​​‌‌​‌‌​​​‌​​​​​​‌​‌​‌​​​‌‌‌​​‌​​‌‌​‌​​‌​‌‌​‌‌‌​​‌‌​‌​​​​​‌​​​​​​‌​​​‌​​​‌‌​​​​‌​‌‌​‌‌‌​​‌‌​​‌‌‌​​‌​​​​​​‌​​‌​‌‌​‌‌​‌​​​​‌‌​‌‌‌‌​‌‌​​​​‌​​‌​​​​​​​‌​‌​​​​‌​​​​​‌​‌‌​‌‌​​​‌‌​​‌​‌​‌‌‌‌​​​​​‌​​​​​​‌​‌​‌​​​‌‌‌​​‌​​‌‌​‌​​‌​‌‌​‌‌‌​​‌‌​‌​​​​​‌​‌​​‌​​‌​​​​​​​‌‌‌‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​‌‌​‌‌​‌​‌‌​‌‌‌‌​​‌‌​​​​​​‌‌​‌‌‌​‌​​​​​​​‌‌​‌​​‌​‌‌​‌‌‌‌​​‌​‌‌‌​​‌‌‌​‌‌​​‌‌​‌‌‌​​​‌‌‌‌‌​​​‌​​​​​​​‌​‌‌​‌​​‌​​​​​​‌​​​‌‌‌​‌‌​‌​​‌​‌‌‌​‌​​​‌​​‌​​​​‌‌‌​‌​‌​‌‌​​​‌​​​‌‌‌​‌​​​‌​​​​​​‌​​​​​​​‌‌‌​‌​​​‌‌‌​‌​‌​‌‌​‌‌​‌​‌‌​‌‌‌‌​​‌‌​​​​​​‌‌​‌‌‌​​‌​​​​​​​‌​‌‌​‌​​‌​​​​​​‌​​​‌​‌​‌‌​​‌​​​​‌‌​​‌​​​‌‌​‌​‌​​‌‌​‌​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​‌​​​‌​​​​​​‌​​‌‌​‌​‌‌​‌‌​‌​‌​​​‌​​​​‌‌‌​​‌​‌‌‌‌​‌​​​‌​‌​‌‌​‌​​‌‌​‌​​‌​‌‌‌‌​​‌‌​​‌​​‌​​​​‌‌​‌‌​​‌‌‌​‌​‌​‌‌​​​‌​‌​‌‌​‌​​‌​‌​​‌‌​‌​​​​‌‌‌‌​​​​‌​​​​‌‌​‌​​‌‌‌​​​‌‌​​‌‌​‌‌​‌​‌‌​‌‌‌​​‌‌​‌‌​​‌​‌​‌​​‌​​​​​‌‌​‌‌​​‌‌‌​‌‌​​‌​​‌​​‌​‌‌​‌‌‌​​‌​‌‌​​‌​‌​​‌‌​​​‌​‌​‌‌‌​‌‌​​‌​‌​​‌‌‌​​‌​‌‌‌​‌‌‌​‌​‌​​‌‌​‌​​‌‌‌​​‌‌‌​‌‌‌​‌‌​‌‌​‌​‌‌​​‌​‌​​‌‌​​​​​‌​​‌​​​​‌‌‌‌​​‌​‌‌​​​​‌​‌‌‌​‌‌‌‍", "không bị trừ tiền", "không thu phí"
  ];
  const PAID_WORDS = [
    "/mo after", "/month after", "per month after",
    "thanh toán ngay", "trả ngay", "pay now",
    "charged today", "charge today"
  ];

  let bar = null;
  function paint(kind, text) {
    if (!document.body) return;
    if (!bar) {
      bar = document.createElement("div");
      bar.style.cssText = "position:fixed;left:0;right:0;top:0;z-index:2147483647;padding:10px 14px;" +
        "font:13px/1.5 -apple-system,Segoe UI,Roboto,'Segoe UI',sans-serif;text-align:center;font-weight:600;";
      document.body.appendChild(bar);
    }
    if (bar.textContent === text && bar.dataset.kind === kind) return;
    bar.dataset.kind = kind;
    bar.style.background = kind === "ok" ? "#1a7f37" : (kind === "bad" ? "#c62828" : "#616161");
    bar.style.color = "#fff";
    bar.textContent = text;
  }

  function judge() {
    let t = "";
    try {
      t = (document.body && document.body.innerText || "").toLowerCase();
    } catch (e) {
      return;
    }
    if (!t || t.length < 5) return;
    const free = FREE_WORDS.some((w) => t.includes(w.toLowerCase()));
    const paid = PAID_WORDS.some((w) => t.includes(w.toLowerCase()));

    if (free && !paid) {
      paint("ok", "✅ ĐÃ XÁC NHẬN MIỄN PHÍ ($0.00) —— Cửa sổ an toàn để bấm Đăng ký (Hãy đối chiếu lại số tiền)");
    } else if (paid && !free) {
      paint("bad", "❌ CẢNH BÁO: Phát hiện có tính phí! DỪNG LẠI không nhấn đăng ký —— Hãy kiểm tra lại tầng!");
    } else if (free && paid) {
      paint("warn", "⚠️ Lưu ý: Điều khoản xuất hiện cả miễn phí và tính phí —— Vui lòng kiểm tra kỹ số tiền $0.00 trước khi bấm!");
    } else {
      paint("warn", "… Đang kiểm tra điều khoản giá gói...");
    }
  }

  setTimeout(judge, 1200);
  setTimeout(judge, 3000);
  setTimeout(judge, 6000);
  try {
    let _t = null;
    const mo = new MutationObserver(() => { if (_t) clearTimeout(_t); _t = setTimeout(judge, 300); });
    setInterval(judge, 1200); if (document.body) mo.observe(document.body, { childList: true, subtree: true }); else document.addEventListener("DOMContentLoaded", () => { if (document.body) mo.observe(document.body, { childList: true, subtree: true }); });
  } catch (e) {}
})();
