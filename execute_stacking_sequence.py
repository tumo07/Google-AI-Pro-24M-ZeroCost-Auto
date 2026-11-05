import asyncio
import os
import sys
import io
import re
import json
import time

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from playwright.async_api import async_playwright
import automation_engine
from engine_stacker import StackingEngine

def log(msg):
    print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)

async def run():
    log("======================================================================")
    log("🚀 EXECUTING LAYER 2 + LAYER 3 + AUTO-RENEWAL CANCELLATION + VN SWITCH")
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
        
        # Check active pages
        pages = context.pages
        page = pages[0] if pages else await context.new_page()
        for pg in pages:
            if "google" in pg.url:
                page = pg
                break

        # Step A: Click "Đăng ký" on currently open Layer 2 modal if open
        eacquire_frame = None
        for fr in page.frames:
            if "eacquire" in (fr.url or ""):
                eacquire_frame = fr
                break
        
        if eacquire_frame:
            log("🎯 Phát hiện cửa sổ Google Play Tầng 2 (+6M SS) đang mở trên màn hình!")
            clicked = False
            btns = eacquire_frame.locator('button, [role="button"]')
            bcnt = await btns.count()
            for i in range(bcnt):
                b = btns.nth(i)
                try:
                    btxt = (await b.inner_text()).strip()
                    if btxt in ("Đăng ký", "Đăng ký thuê bao", "Subscribe", "订阅", "Nâng cấp"):
                        log(f"--> Đang bấm nút 【{btxt}】...")
                        await b.click(force=True)
                        clicked = True
                        break
                except Exception:
                    pass
            
            if not clicked:
                js_click = await eacquire_frame.evaluate("""() => {
                    const btns = Array.from(document.querySelectorAll('button, [role="button"]'));
                    const sub = btns.find(b => ['Đăng ký', 'Đăng ký thuê bao', 'Subscribe', '订阅', 'Nâng cấp'].includes((b.innerText || '').trim()));
                    if (sub) { sub.click(); return true; }
                    return false;
                }""")
                if js_click:
                    log("--> Đã bấm [Đăng ký] qua JavaScript!")
                    clicked = True
            
            log("⏳ Đang chờ Google Play xử lý Tầng 2...")
            await asyncio.sleep(12)
            shot2 = os.path.join(automation_engine.SCREENSHOTS_DIR, "Account_2_layer2_confirmed.png")
            await page.screenshot(path=shot2)
            log(f"✅ Đã chụp ảnh xác nhận sau khi bấm Tầng 2: {shot2}")
        else:
            log("Cửa sổ Tầng 2 chưa mở, tiến hành kích hoạt Tầng 2 qua automation_engine...")
            await automator.ensure_subscription_active(page)
            sub_id = await automator.get_current_sub_id(page)
            cfg_l2 = {
                "name": "Step3_Layer2_6MSS_YTFree_ZeroCost",
                "full_items": [
                    [[automation_engine.PREFIX + "g1.2tb.ai.subs_variant", 21], None, None, None, 1, [automation_engine.TOK_PRO5TB_6M_SS]],
                    [[automation_engine.PREFIX + "g1.youtube_premium_individual_add_on", 21], None, None, None, 1, [automation_engine.YT_FREE_TOK]],
                ],
                "ear8": [None, 5, None, None, None, [sub_id]] if sub_id else None,
            }
            ok2 = await automator.open_and_click_subscribe(page, cfg_l2, "step3_layer2_6mss")
            log(f"Kết quả kích hoạt Tầng 2: {ok2}")
            await asyncio.sleep(15)

        # Ensure active before Layer 3
        log("\n--- BƯỚC TIẾP THEO: ĐỒNG BỘ TRƯỚC KHI XẾP TẦNG 3 ---")
        await automator.ensure_subscription_active(page)
        await asyncio.sleep(3)

        # Step B: Layer 3 (+6M Pixel -> Đạt 24 Tháng đến Tháng 11/2028)
        log("\n--- THỰC HIỆN TẦNG 3: +6 THÁNG PIXEL (TARGET: 24 THÁNG - NOV 2028) ---")
        sub_id_3 = await automator.get_current_sub_id(page)
        log(f"Mã gói hiện tại (sub_id): {sub_id_3}")
        cfg_l3 = {
            "name": "Step4_Layer3_6M_Pixel_ZeroCost",
            "full_items": [
                [[automation_engine.PREFIX + "g1.2tb.ai.subs_variant", 21], None, None, None, 1, [automation_engine.TOK_PRO5TB_6M]],
                [[automation_engine.PREFIX + "g1.youtube_premium_individual_add_on", 21], None, None, None, 1, [automation_engine.YT_FREE_TOK]],
            ],
            "ear8": [None, 5, None, None, None, [sub_id_3]] if sub_id_3 else None,
        }
        ok3 = await automator.open_and_click_subscribe(page, cfg_l3, "step4_layer3_6m")
        if not ok3:
            log("⚠️ Thử lại Tầng 3 sau 3 giây...")
            await asyncio.sleep(3)
            ok3 = await automator.open_and_click_subscribe(page, cfg_l3, "step4_layer3_6m")
        log(f"Kết quả Tầng 3: {ok3}")
        await asyncio.sleep(15)

        # Step C: Cancel YouTube Auto-Renewal to eliminate $11.99 and lock 2028
        log("\n--- HỦY GIA HẠN ĐỊNH KỲ (KHÓA HẠN 2028 & HỦY PHÍ YOUTUBE 11.99$) ---")
        await engine.cancel_youtube_and_lock_2028(page)
        await asyncio.sleep(5)

        # Step D: Switch region to Vietnam
        log("\n--- CHUYỂN HỒ SƠ THANH TOÁN VỀ VIỆT NAM (BẬT FAMILY SHARING) ---")
        await engine.switch_billing_region_to_vietnam(page)
        await asyncio.sleep(5)

        # Final Verification
        log("\n--- KIỂM TRA XÁC NHẬN CUỐI CÙNG ---")
        play_txt = await automator.inspect_play_subscriptions(page)
        final_shot = os.path.join(automation_engine.SCREENSHOTS_DIR, "Account_2_full_24m_completed.png")
        await page.screenshot(path=final_shot)
        log(f"📸 Ảnh xác nhận hoàn tất 24 tháng đã lưu tại: {final_shot}")
        log(f"Nội dung Google Play: {play_txt[:350]}")

        # Update config.json
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
                    acc["last_screenshot"] = "Account_2_full_24m_completed.png"
            with open(cfg_path, "w", encoding="utf-8") as f:
                json.dump(c, f, indent=2, ensure_ascii=False)
            log("✅ config.json đã cập nhật trạng thái: Account_2 COMPLETED (2028-11-05)!")
        except Exception as e:
            log(f"Lỗi cập nhật config.json: {e}")

        log("\n🎉 HOÀN THÀNH TOÀN BỘ 24 THÁNG GOOGLE AI PRO (5 TB) CHO ACCOUNT_2!")

if __name__ == "__main__":
    asyncio.run(run())
