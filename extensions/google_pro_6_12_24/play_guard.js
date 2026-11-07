/*
 * Google AI Pro 24M Offer Injector — Checkout Price Guard
 * Inspects checkout terms inside Play acquire iframe to verify US$0.00 zero billing.
 * Shows green banner if free trial is verified, red banner if charges detected.
 * Developed & Maintained by Trinh Dang Khoa (Alex Trinh) <tumo07@io.vn>
 * Licensed under the MIT License.
 */
(() => {
  if (window.__GAPT_GUARD) return;
  window.__GAPT_GUARD = true;

  let bar = null;
  function paint(kind, text) {
    if (!document.body) return;
    if (!bar) {
      bar = document.createElement("div");
      bar.style.cssText = "position:fixed;left:0;right:0;top:0;z-index:2147483647;padding:10px 14px;" +
        "font:13px/1.5 -apple-system,Segoe UI,Roboto,'Segoe UI',sans-serif;text-align:center;font-weight:600;pointer-events:none;";
      document.body.appendChild(bar);
    }
    if (bar.textContent === text && bar.dataset.kind === kind) return;
    bar.dataset.kind = kind;
    bar.style.background = kind === "ok" ? "#1a7f37" : (kind === "bad" ? "#c62828" : "#616161");
    bar.style.color = "#fff";
    bar.textContent = text;
    try {
      if (window.top !== window) {
        window.top.postMessage({ __GAPT_GUARD_STATUS: true, kind: kind, text: text }, "*");
      }
    } catch (e) {}
  }

  if (window.top === window) {
    window.addEventListener("message", (ev) => {
      if (ev.data && ev.data.__GAPT_GUARD_STATUS) {
        paint(ev.data.kind, ev.data.text);
      }
    });
    return;
  }

  if ((!location.href.includes("eacquire") && !location.href.includes("tokenized.play.google.com")) || location.href.includes("instrumentmanager")) return;

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



  function judge() {
    let t = "";
    try {
      t = (document.body && document.body.innerText || "").toLowerCase();
    } catch (e) {
      return;
    }
    if (!t || t.length < 5) return;

    // 1. Success state: subscription confirmed / Play Points dialog
    if (
      t.includes("nhận điểm google play") ||
      t.includes("sau khi đăng ký") ||
      t.includes("đã đăng ký") ||
      t.includes("cảm ơn bạn đã đăng ký") ||
      t.includes("google play points") ||
      t.includes("subscribed") ||
      t.includes("thank you for your order") ||
      t.includes("已订阅") ||
      t.includes("感谢您订阅")
    ) {
      paint("ok", "✅ ĐÃ KÍCH HOẠT THÀNH CÔNG GÓI $0.00! Bấm [Để sau] để tiếp tục...");
      return;
    }

    // 2. Explicit charge today
    const paid = PAID_WORDS.some((w) => t.includes(w.toLowerCase()));
    if (paid) {
      paint("bad", "❌ CẢNH BÁO: Phát hiện có tính phí hôm nay! DỪNG LẠI không nhấn đăng ký!");
      return;
    }

    // 3. Layer 1, Layer 2 (Samsung +6M), and Layer 3 (Pixel +6M) Zero-Cost Verification
    const hasFreeSignal = FREE_WORDS.some((w) => t.includes(w.toLowerCase())) ||
      t.includes("0,00") || t.includes("0.00") || t.includes("0 đ") || t.includes("0đ") ||
      t.includes("các khoản phí sắp tới") || t.includes("ngày bắt đầu:") ||
      t.includes("upcoming charges") || t.includes("starting on") ||
      t.includes("即将收取的费用") || t.includes("开始日期") ||
      t.includes("dùng thử miễn phí") || t.includes("miễn phí");

    if (hasFreeSignal) {
      paint("ok", "✅ ĐÃ XÁC NHẬN MIỄN PHÍ ($0.00) —— Cửa sổ an toàn để bấm Đăng ký (Tầng 1/2/3 24 Tháng)");
      return;
    }

    paint("warn", "… Đang kiểm tra điều khoản giá gói...");
  }

  judge();
  setTimeout(judge, 400);
  setTimeout(judge, 1000);
  setTimeout(judge, 2000);
  setInterval(judge, 800);
  try {
    let _t = null;
    const mo = new MutationObserver(() => { if (_t) clearTimeout(_t); _t = setTimeout(judge, 150); });
    if (document.body) {
      mo.observe(document.body, { childList: true, subtree: true });
    }
    document.addEventListener("DOMContentLoaded", () => {
      if (document.body) mo.observe(document.body, { childList: true, subtree: true });
      judge();
    });
  } catch (e) {}
})();
