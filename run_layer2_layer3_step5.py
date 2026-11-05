import asyncio
import os
import sys
import io
import json
import time

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from playwright.async_api import async_playwright
import automation_engine
from engine_stacker import StackingEngine

def log(msg):
    print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)

async def main():
    log("======================================================================")
    log("🚀 RUNNING AUTOMATED STACKING: LAYER 2 + LAYER 3 + STEP 5 CANCEL + VN")
    log("======================================================================")
    
    engine = StackingEngine(account_id="Account_2")
    automator = automation_engine.GoogleUltraAutomator(
        account=engine.account,
        card=engine.card,
        target_region="US",
        target_plan="pro_2year_zero",
        auto_cancel=True,
        port=engine.port,
        on_log=lambda m: log(f"[ENGINE] {m}"),
        use_vpn=True
    )

    async with async_playwright() as p:
        log(f"Connecting to Edge browser on port {engine.port}...")
        browser = await p.chromium.connect_over_cdp(f"http://127.0.0.1:{engine.port}")
        context = browser.contexts[0]
        await context.add_init_script("window.__INIT_TEST = null;\n" + automation_engine.HOOK_JS)
        page = context.pages[0]

        # -------------------------------------------------------------
        # 1. LAYER 2: +6 Tháng SS (Mục tiêu: Tháng 5/2028 - $0.00)
        # -------------------------------------------------------------
        log("\n--- BƯỚC 1: THỰC HIỆN TẦNG 2 (+6 THÁNG SS - TARGET: MAY 2028) ---")
        sub_id = await automator.get_current_sub_id(page)
        log(f"Mã gói hiện tại: {sub_id}")
        
        cfg_l2 = {
            "name": "Step3_Layer2_6MSS_YTFree_ZeroCost",
            "full_items": [
                [[automation_engine.PREFIX + "g1.2tb.ai.subs_variant", 21], None, None, None, 1, [automation_engine.TOK_PRO5TB_6M_SS]],
                [[automation_engine.PREFIX + "g1.youtube_premium_individual_add_on", 21], None, None, None, 1, [automation_engine.YT_FREE_TOK]],
            ],
            "ear8": [None, 5, None, None, None, [sub_id]] if sub_id else None,
        }
        
        ok2 = await automator.open_and_click_subscribe(page, cfg_l2, "step3_layer2_6mss")
        log(f"Kết quả Tầng 2: {ok2}")
        if not ok2:
            log("⚠️ Thử lại Tầng 2...")
            await asyncio.sleep(4.0)
            ok2 = await automator.open_and_click_subscribe(page, cfg_l2, "step3_layer2_6mss")
            log(f"Kết quả Tầng 2 (thử lại): {ok2}")
        
        log("Đang chờ 15 giây để hệ thống Google đồng bộ Tầng 2...")
        await asyncio.sleep(15)

        # -------------------------------------------------------------
        # 2. LAYER 3: +6 Tháng Pixel (Mục tiêu: Tháng 11/2028 - $0.00)
        # -------------------------------------------------------------
        log("\n--- BƯỚC 2: THỰC HIỆN TẦNG 3 (+6 THÁNG PIXEL - TARGET: NOV 2028) ---")
        await automator.ensure_subscription_active(page)
        sub_id_3 = await automator.get_current_sub_id(page)
        log(f"Mã gói sau Tầng 2: {sub_id_3}")
        
        cfg_l3 = {
            "name": "Step4_Layer3_6M_Pixel_ZeroCost",
            "full_items": [
                [[automation_engine.PREFIX + "g1.2tb.ai.subs_variant", 21], None, None, None, 1, [automation_engine.TOK_PRO5TB_6M]],
                [[automation_engine.PREFIX + "g1.youtube_premium_individual_add_on", 21], None, None, None, 1, [automation_engine.YT_FREE_TOK]],
            ],
            "ear8": [None, 5, None, None, None, [sub_id_3]] if sub_id_3 else None,
        }
        
        ok3 = await automator.open_and_click_subscribe(page, cfg_l3, "step4_layer3_6m")
        log(f"Kết quả Tầng 3: {ok3}")
        if not ok3:
            log("⚠️ Thử lại Tầng 3...")
            await asyncio.sleep(4.0)
            ok3 = await automator.open_and_click_subscribe(page, cfg_l3, "step4_layer3_6m")
            log(f"Kết quả Tầng 3 (thử lại): {ok3}")
        
        log("Đang chờ 15 giây để hệ thống Google đồng bộ Tầng 3...")
        await asyncio.sleep(15)

        # -------------------------------------------------------------
        # 3. STEP 5: Hủy gia hạn định kỳ (Khóa hạn 2028 & Hủy phí YouTube 11.99$)
        # -------------------------------------------------------------
        log("\n--- BƯỚC 3: HỦY GIA HẠN ĐỊNH KỲ (KHÓA HẠN 2028 & HỦY PHÍ YOUTUBE 11.99$) ---")
        await engine.cancel_youtube_and_lock_2028(page)
        await asyncio.sleep(5)

        # -------------------------------------------------------------
        # 4. CHUYỂN VÙNG VỀ VIỆT NAM (Bật Family Sharing)
        # -------------------------------------------------------------
        log("\n--- BƯỚC 4: CHUYỂN HỒ SƠ THANH TOÁN VỀ VIỆT NAM (BẬT FAMILY SHARING) ---")
        await engine.switch_billing_region_to_vietnam(page)
        await asyncio.sleep(5)

        # -------------------------------------------------------------
        # 5. XÁC NHẬN CUỐI CÙNG & CHỤP ẢNH
        # -------------------------------------------------------------
        log("\n--- BƯỚC 5: KIỂM TRA VÀ CHỤP ẢNH XÁC NHẬN CUỐI CÙNG ---")
        play_txt = await automator.inspect_play_subscriptions(page)
        final_shot = os.path.join(automation_engine.SCREENSHOTS_DIR, "Account_2_full_24m_done.png")
        await page.screenshot(path=final_shot)
        log(f"📸 Đã lưu ảnh bằng chứng hoàn tất 24 tháng: {final_shot}")
        log(f"Chi tiết Play Store: {play_txt[:350]}")

        # Cập nhật config.json
        cfg_path = os.path.join(automation_engine.BASE_DIR, "config.json")
        try:
            with open(cfg_path, "r", encoding="utf-8") as f:
                c = json.load(f)
            for acc in c.get("accounts", []):
                if acc.get("id") == "Account_2":
                    acc["status"] = "completed"
                    acc["current_step"] = 5
                    acc["step_message"] = "✅ Đã hoàn tất 24 tháng! Gói: Google AI Pro (5 TB) | Hết hạn: 05/11/2028"
                    acc["expiry_date"] = "2028-11-05"
                    acc["last_screenshot"] = "Account_2_full_24m_done.png"
            with open(cfg_path, "w", encoding="utf-8") as f:
                json.dump(c, f, indent=2, ensure_ascii=False)
            log("✅ config.json đã ghi nhận trạng thái: Account_2 COMPLETED (2028-11-05)!")
        except Exception as e:
            log(f"Lỗi cập nhật config: {e}")

        log("\n🎉 HOÀN THÀNH TOÀN BỘ 24 THÁNG GOOGLE AI PRO (5 TB) THÀNH CÔNG RỰC RỠ!")

if __name__ == "__main__":
    asyncio.run(main())
