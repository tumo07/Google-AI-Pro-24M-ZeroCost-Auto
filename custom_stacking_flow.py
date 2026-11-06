import ensure_env
"""
Custom 24-Month Stacking Flow for Google AI Pro (5 TB)
Based on Browser Control Infrastructure and Manual Community Flow.

Steps:
  0. Setup US Payments Profile on payments.google.com (New York 10118 or Oregon 97201) & Close Old Profile.
  1. Layer 1 (12M): Inject TOK_PRO5TB_12M -> Verify Green Banner ($0.00) -> Subscribe.
  2. Layer 2 (6M): Capture Sub ID -> Inject TOK_PRO5TB_6M_SS -> Verify Green Banner ($0.00) -> Stack.
  3. Layer 3 (6M): Inject TOK_PRO5TB_6M / 6M_2 -> Verify Green Banner ($0.00) -> Stack to 24 Months.
  4. Final: Cancel auto-renewal on play.google.com to lock in $0.00.
"""

import asyncio
import json
import os
import sys
import time
from typing import Optional, Dict, Any

if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

import automation_engine

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(BASE_DIR, "config.json")
LOG_PATH = os.path.join(BASE_DIR, "execution.log")

SAMPLE_ADDRESS_NY = {
    "holder": "Le Ha",
    "address_line1": "350 Fifth Avenue",
    "address_line2": "",
    "locality": "New York",
    "province": "NY",
    "postal_code": "10118",
    "country": "US"
}

SAMPLE_ADDRESS_OR = {
    "holder": "Alex Trinh",
    "address_line1": "700 SW 5th Ave",
    "address_line2": "",
    "locality": "Portland",
    "province": "OR",
    "postal_code": "97201",
    "country": "US"
}

def log(msg: str):
    ts = time.strftime("%H:%M:%S")
    line = f"[{ts}] [CustomFlow] {msg}"
    print(line, flush=True)
    try:
        with open(LOG_PATH, "a", encoding="utf-8") as f:
            f.write(line + "\n")
    except Exception:
        pass

def load_config():
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

class CustomStackingAutomator:
    def __init__(self, target_account_id: str = "Account_1"):
        self.cfg = load_config()
        self.account = next((a for a in self.cfg.get("accounts", []) if a["id"] == target_account_id), None)
        if not self.account:
            raise ValueError(f"Account {target_account_id} not found in config.json")
        self.card = self.cfg.get("card", {})
        self.engine = automation_engine.GoogleUltraAutomator(
            account=self.account,
            card=self.card,
            target_region="US",
            target_plan="pro_2year_zero",
            auto_cancel=True,
            port=9320,
            on_log=log,
            use_vpn=self.cfg.get("use_vpn", True),
        )

    async def open_browser_session(self):
        """Launches Edge with Browsec US VPN and connects Playwright over CDP."""
        log("🌐 Launching Edge Browser with US VPN...")
        self.engine.ensure_edge_running()
        await asyncio.sleep(4)
        browser, context, page = await self.engine.attach_playwright()
        
        # Initialize VPN if required
        if self.engine.use_vpn:
            vpn_ok = await self.engine.activate_vpn_to_us(browser, context, page)
            if vpn_ok:
                log("✅ US VPN Connected successfully.")
            else:
                log("⚠️ VPN Check warning, continuing with active proxy/profile.")
            page = context.pages[0] if context.pages else await context.new_page()
            await page.set_viewport_size({"width": 1400, "height": 950})

        await self.engine.verify_ip_environment(page)
        return browser, context, page

    async def check_modal_banner_status(self, page) -> str:
        """
        Inspects Google Play purchase modal for Green vs Red banner:
          - 'green': Eligible for free subscription ($0.00).
          - 'red': Ineligible / rejected.
          - 'unknown': Banner not explicitly styled or recognized.
        """
        frames_to_check = page.frames
        for fr in frames_to_check:
            if "eacquire" in (fr.url or ""):
                try:
                    status = await fr.evaluate("""() => {
                        const bodyTxt = (document.body.innerText || '');
                        if (bodyTxt.includes('US$0.00') || bodyTxt.includes('免费试用') || bodyTxt.includes('Free trial')) {
                            const errorBanners = document.querySelectorAll('[role="alert"], .error, .warning');
                            for (const b of errorBanners) {
                                if (b.innerText && b.innerText.trim().length > 0) {
                                    return { color: 'red', text: b.innerText };
                                }
                            }
                            return { color: 'green', text: 'Eligible US$0.00' };
                        }
                        if (bodyTxt.includes('无法免费试用') || bodyTxt.includes('不符合条件') || bodyTxt.includes('Something went wrong')) {
                            return { color: 'red', text: bodyTxt.slice(0, 200) };
                        }
                        return { color: 'unknown', text: bodyTxt.slice(0, 100) };
                    }""")
                    log(f"Banner Check: [{status['color'].upper()}] - {status['text']}")
                    return status['color']
                except Exception:
                    pass
        return "unknown"

    async def run_payments_profile_guide(self, page, address_choice: str = "ny"):
        """Navigates to payments.google.com and displays the setup template."""
        addr = SAMPLE_ADDRESS_NY if address_choice.lower() == "ny" else SAMPLE_ADDRESS_OR
        log("============================================================")
        log(f"👉 Phase 0: payments.google.com US Profile Setup ({addr['locality']})")
        log(f"   Name: {addr['holder']}")
        log(f"   Address 1: {addr['address_line1']}")
        log(f"   City: {addr['locality']} | State: {addr['province']} | ZIP: {addr['postal_code']}")
        log("============================================================")
        await self.engine.safe_goto(page, "https://payments.google.com/gp/w/u/0/home/settings", timeout=40000)
        await asyncio.sleep(4)
        log("ℹ️ Open in Session 1 for user to verify/close old non-US profile if present.")

    async def execute_layer(self, page, layer_num: int):
        """Executes a specific Layer (1, 2, or 3) with exact community tokens."""
        if layer_num == 1:
            log("🚀 Executing Layer 1: 12-Month Base (TOK_PRO5TB_12M)...")
            sub_id = await self.engine.get_current_sub_id(page)
            cfg = {
                "name": "Custom_Layer1_12M",
                "full_items": [
                    [[automation_engine.PREFIX + "g1.2tb.ai.subs_variant", 21], None, None, None, 1, [automation_engine.TOK_PRO5TB_12M]],
                    [[automation_engine.PREFIX + "g1.youtube_premium_individual_add_on", 21], None, None, None, 1, [automation_engine.YT_FREE_TOK]],
                ],
                "ear8": [None, 5, None, None, None, [sub_id]] if sub_id else None,
            }
            ok = await self.engine.open_and_click_subscribe(page, cfg, "layer1_12m")
            log(f"Layer 1 result: {'SUCCESS' if ok else 'FAILED'}")
            return ok

        elif layer_num == 2:
            log("🚀 Executing Layer 2: +6 Month Stack (S25 Pro 6M - TOK_PRO5TB_6M_SS)...")
            sub_id = await self.engine.get_current_sub_id(page)
            cfg = {
                "name": "Custom_Layer2_6M_SS",
                "full_items": [
                    [[automation_engine.PREFIX + "g1.2tb.ai.subs_variant", 21], None, None, None, 1, [automation_engine.TOK_PRO5TB_6M_SS]],
                    [[automation_engine.PREFIX + "g1.youtube_premium_individual_add_on", 21], None, None, None, 1, [automation_engine.YT_FREE_TOK]],
                ],
                "ear8": [None, 5, None, None, None, [sub_id]] if sub_id else None,
            }
            ok = await self.engine.open_and_click_subscribe(page, cfg, "layer2_6m_ss")
            log(f"Layer 2 result: {'SUCCESS' if ok else 'FAILED'}")
            return ok

        elif layer_num == 3:
            log("🚀 Executing Layer 3: +6 Month Final Stack (Pixel 6M - TOK_PRO5TB_6M)...")
            sub_id = await self.engine.get_current_sub_id(page)
            cfg = {
                "name": "Custom_Layer3_6M_Pixel",
                "full_items": [
                    [[automation_engine.PREFIX + "g1.2tb.ai.subs_variant", 21], None, None, None, 1, [automation_engine.TOK_PRO5TB_6M]],
                    [[automation_engine.PREFIX + "g1.youtube_premium_individual_add_on", 21], None, None, None, 1, [automation_engine.YT_FREE_TOK]],
                ],
                "ear8": [None, 5, None, None, None, [sub_id]] if sub_id else None,
            }
            ok = await self.engine.open_and_click_subscribe(page, cfg, "layer3_6m_pixel")
            log(f"Layer 3 result: {'SUCCESS' if ok else 'FAILED'}")
            return ok

    async def execute_cancel_auto_renew(self, page):
        """Executes Step 5: Clean auto-renewal cancellation."""
        log("🛡️ Executing auto-renewal cancellation on Google Play...")
        await self.engine.step5_cancel_and_verify(page)
        log("✅ Auto-renewal cancellation and verification complete.")

async def main():
    action = sys.argv[1].lower() if len(sys.argv) > 1 else "help"
    automator = CustomStackingAutomator("Account_1")

    if action == "help":
        print("""
Usage: python custom_stacking_flow.py <command>
Commands:
  profile [ny|or]   - Opens payments.google.com to setup US profile & close old profile
  layer1            - Injects Layer 1 (12-Month Base) on one.google.com/plans
  layer2            - Injects Layer 2 (+6-Month S25 Stack)
  layer3            - Injects Layer 3 (+6-Month Pixel Stack)
  cancel            - Cancels auto-renewal on Google Play
  auto              - Runs full custom stacking flow end-to-end
""")
        return

    browser, context, page = await automator.open_browser_session()
    try:
        if action == "profile":
            choice = sys.argv[2] if len(sys.argv) > 2 else "ny"
            await automator.run_payments_profile_guide(page, choice)
            log("Browser opened to payments.google.com. Press Ctrl+C when finished.")
            while True:
                await asyncio.sleep(10)

        elif action == "layer1":
            await automator.execute_layer(page, 1)

        elif action == "layer2":
            await automator.execute_layer(page, 2)

        elif action == "layer3":
            await automator.execute_layer(page, 3)

        elif action == "cancel":
            await automator.execute_cancel_auto_renew(page)

        elif action == "auto":
            log("▶ Running Full Custom Stacking Sequence...")
            await automator.execute_layer(page, 1)
            await asyncio.sleep(15)
            await automator.execute_layer(page, 2)
            await asyncio.sleep(15)
            await automator.execute_layer(page, 3)
            await asyncio.sleep(20)
            await automator.execute_cancel_auto_renew(page)
            log("🎉 Custom Stacking Sequence Finished!")

    finally:
        log("Finished custom flow command.")

if __name__ == "__main__":
    asyncio.run(main())
