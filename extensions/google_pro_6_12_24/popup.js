/*
 * Google AI Pro 24M Offer Injector — Popup Controller
 * Manages layer selection and syncs with content script in active tab.
 * Developed & Maintained by Trinh Dang Khoa (Alex Trinh) <tumo07@io.vn>
 * Licensed under the MIT License.
 */
const LABELS = {
  off: "Chưa kích hoạt",
  "12m": "Tầng 1 (12 tháng)",
  "6m_ss": "Tầng 2 (6 tháng SS)",
  "6m": "Tầng 3 (6 tháng)",
  "6m_2": "Dự phòng (6 tháng)"
};
const stateEl = document.getElementById("state");

function paintState(st) {
  const layer = (st && st.layer) || "off";
  const mounted = !!(st && st.mounted) && layer !== "off";
  stateEl.className = mounted ? "ok" : "warn";
  stateEl.textContent = mounted
    ? "Đã sẵn sàng: " + (LABELS[layer] || layer) + " —— Hãy bấm 'Get discount' trên trang Google One"
    : "Chưa kích hoạt trên trang (Vui lòng mở one.google.com/plans và tải lại F5)";
}

function queryTab() {
  chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
    const t = tabs && tabs[0];
    if (!t) return paintState(null);
    chrome.tabs.sendMessage(t.id, { type: "getState" }, (resp) => {
      if (chrome.runtime.lastError || !resp) return paintState(null);
      paintState(resp);
    });
  });
}

chrome.storage.local.get(["gapt_layer"], (r) => {
  const layer = (r && r.gapt_layer) || "off";
  document.querySelectorAll('input[name="layer"]').forEach((el) => {
    el.checked = el.value === layer;
    el.addEventListener("change", () => {
      if (!el.checked) return;
      chrome.storage.local.set({ gapt_layer: el.value }, () => {
        chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
          const t = tabs && tabs[0];
          if (!t) return queryTab();
          chrome.tabs.sendMessage(t.id, { type: "setLayer", layer: el.value }, () => {
            void chrome.runtime.lastError;
            setTimeout(queryTab, 350);
          });
        });
      });
    });
  });
  queryTab();
  setTimeout(queryTab, 800);
});

setInterval(queryTab, 1500);
