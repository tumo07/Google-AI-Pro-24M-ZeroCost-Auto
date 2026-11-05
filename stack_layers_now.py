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

async def main():
    print("======================================================================")
    print("🚀 GOOGLE AI PRO (5 TB) 24-MONTH CONTINUATION RUNNER")
    print("======================================================================")
    
    engine = StackingEngine(account_id="Account_2")
    automator = automation_engine.GoogleUltraAutomator(
        account=engine.account,
        card=engine.card,
        target_region="US",
        target_plan="pro_2year_zero",
        auto_cancel=True,
        port=engine.port,
        on_log=lambda m: print(f"[ENGINE] {m}"),
        use_vpn=True
    )

    async with async_playwright() as p:
        print(f"Connecting to Edge on port {engine.port}...")
        browser = await p.chromium.connect_over_cdp(f"http://127.0.0.1:{engine.port}")
        context = browser.contexts[0]
        await context.add_init_script("window.__INIT_TEST = null;\n" + automation_engine.HOOK_JS)
        
        # Pick or create a page
        page = context.pages[0] if context.pages else await context.new_page()
        for pg in context.pages:
            if "google" in pg.url:
                page = pg
                break

        print("1. Kiểm tra trạng thái gói hiện tại trên Google Play...")
        play_txt = await automator.inspect_play_subscriptions(page)
        print(f"Thông tin gói hiện tại: {play_txt[:300]}")

        has_base = ("Google AI Pro" in play_txt or "Google One" in play_txt or "5 TB" in play_txt)
        if not has_base:
            # Check one.google.com/settings
            await automator.safe_goto(page, "https://one.google.com/settings?expand=upgrade&hl=vi", timeout=30000)
            await asyncio.sleep(2.5)
            s_txt = await page.inner_text("body")
            if "Google AI Pro" in s_txt or "5 TB" in s_txt:
                has_base = True
                print("✅ Nhận diện gói Google AI Pro (5 TB) đang hoạt động trên Google One!")

        if not has_base:
            print("Chưa có gói nền 12M, đang thực hiện đăng ký tầng 1 (12 tháng)...")
            ok1 = await automator.step2_layer1_12m(page)
            print(f"Kết quả Tầng 1: {ok1}")
            await asyncio.sleep(10.0)

        await automator.ensure_subscription_active(page)

        # Layer 2 (+6M SS)
        print("\n--- 2. Đang thực hiện Tầng 2: +6 Tháng Miễn Phí (Target: 18 Tháng) ---")
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
        if not ok2:
            print("⚠️ Thử lại Tầng 2...")
            await asyncio.sleep(3.0)
            ok2 = await automator.open_and_click_subscribe(page, cfg_l2, "step3_layer2_6mss")
        print(f"Kết quả Tầng 2: {ok2}")
        await asyncio.sleep(12.0)

        await automator.ensure_subscription_active(page)

        # Layer 3 (+6M Pixel)
        print("\n--- 3. Đang thực hiện Tầng 3: +6 Tháng Pixel Miễn Phí (Target: 24 Tháng - Nov 2028) ---")
        sub_id_3 = await automator.get_current_sub_id(page)
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
            print("⚠️ Thử lại Tầng 3...")
            await asyncio.sleep(3.0)
            ok3 = await automator.open_and_click_subscribe(page, cfg_l3, "step4_layer3_6m")
        print(f"Kết quả Tầng 3: {ok3}")
        await asyncio.sleep(12.0)

        # Cancel auto-renewal to lock 2028 and drop YouTube charge
        print("\n--- 4. Hủy gia hạn định kỳ (Khóa hạn 2028 & Hủy phí YouTube 11.99$) ---")
        await engine.cancel_youtube_and_lock_2028(page)

        # Switch region to Vietnam
        print("\n--- 5. Chuyển hồ sơ thanh toán về Việt Nam (Bật Family Sharing) ---")
        await engine.switch_billing_region_to_vietnam(page)

        # Final check
        print("\n--- 6. Hoàn tất kiểm tra cuối cùng ---")
        final_txt = await automator.inspect_play_subscriptions(page)
        shot_path = os.path.join(automation_engine.SCREENSHOTS_DIR, "Account_2_completed_final.png")
        await page.screenshot(path=shot_path)
        print(f"✅ Ảnh xác nhận cuối cùng đã lưu tại: {shot_path}")
        print("TẤT CẢ CÁC BƯỚC ĐÃ HOÀN TẤT!")

if __name__ == "__main__":
    asyncio.run(main())
