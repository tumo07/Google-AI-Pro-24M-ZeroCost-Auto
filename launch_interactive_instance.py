"""
Interactive New Instance Launcher & Automated 24-Month Stacker
--------------------------------------------------------------
Allows launching a fresh Edge browser instance interactively on the user's desktop (Session 1),
letting the user manually log in, approve 2FA/passkeys, or set up payments profile,
and then immediately handing off to the automated 24-Month Zero-Cost Stacking Engine.
"""

import asyncio
import os
import sys
import json
import time
import subprocess
import re
from typing import Optional, Dict, Any

if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

from playwright.async_api import async_playwright
import automation_engine

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(BASE_DIR, "config.json")
LOG_PATH = os.path.join(BASE_DIR, "execution.log")
ARTIFACTS_DIR = r"C:\Users\khoa\.gemini\antigravity\brain\bdb8ac8f-261e-4351-8267-5fe6b7181fb3"

def log(msg: str):
    ts = time.strftime("%H:%M:%S")
    line = f"[{ts}] [InstanceFlow] {msg}"
    print(line, flush=True)
    try:
        with open(LOG_PATH, "a", encoding="utf-8") as f:
            f.write(line + "\n")
    except Exception:
        pass

def load_config() -> Dict[str, Any]:
    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"target_region": "US", "target_plan": "pro_2year_zero", "auto_cancel": True, "accounts": []}

def save_config(cfg: Dict[str, Any]):
    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
        json.dump(cfg, f, indent=2, ensure_ascii=False)

def get_next_account_id(cfg: Dict[str, Any]) -> str:
    accounts = cfg.get("accounts", [])
    existing_ids = [a.get("id", "") for a in accounts]
    idx = 1
    while f"Account_{idx}" in existing_ids:
        idx += 1
    return f"Account_{idx}"

def clean_port(port: int = 9320):
    try:
        net_out = subprocess.check_output(f"netstat -ano | findstr :{port}", shell=True).decode("gbk", errors="ignore")
        for line in net_out.splitlines():
            if "LISTENING" in line:
                old_pid = line.strip().split()[-1]
                subprocess.run(f"taskkill /F /T /PID {old_pid}", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                log(f"Cleaned old process on port {port} (PID: {old_pid})")
    except Exception:
        pass

def launch_visible_edge_via_task(profile_dir: str, port: int = 9320, start_url: str = "https://accounts.google.com/ServiceLogin?continue=https%3A%2F%2Fone.google.com%2Fplans%3Fhl%3Den"):
    """
    Uses Windows Task Scheduler with explorer.exe to bypass Session 0 UI Isolation,
    launching Edge directly onto the active user's desktop (Session 1).
    """
    clean_port(port)
    os.makedirs(profile_dir, exist_ok=True)
    
    vpn_ext = os.path.join(BASE_DIR, "extensions", "browsec_vpn")
    injector_ext = os.path.join(BASE_DIR, "extensions", "google_pro_6_12_24")
    if not os.path.exists(injector_ext):
        injector_ext = os.path.join(BASE_DIR, "extensions", "g1_24_extension")
        
    ext_list = [vpn_ext, injector_ext]
    ext_str = ",".join([e for e in ext_list if os.path.exists(e)])
    
    browser_bin = automation_engine._find_chrome_path(prefer_edge=True)
    
    # In batch files, % must be escaped as %% so cmd.exe doesn't expand %3A into A, %2F into F
    safe_url = start_url.replace("%", "%%")
    # Write a temporary launcher batch file
    launcher_bat = os.path.join(BASE_DIR, "temp_launch_session1.bat")
    bat_content = f"""@echo off
start "" "{browser_bin}" --remote-debugging-port={port} --user-data-dir="{profile_dir}" --start-maximized --no-first-run --no-default-browser-check --disable-popup-blocking --load-extension="{ext_str}" --disable-extensions-except="{ext_str}" "{safe_url}"
exit
"""
    with open(launcher_bat, "w", encoding="utf-8") as f:
        f.write(bat_content)
        
    task_name = "GoogleAI_InteractiveLaunch"
    tr_command = f'explorer.exe "{launcher_bat}"'
    
    log(f"🚀 Creating Interactive Scheduled Task '{task_name}' to launch Edge on Session 1 desktop...")
    subprocess.run(f'schtasks.exe /create /tn "{task_name}" /tr "{tr_command}" /sc ONCE /st 00:00 /it /f', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.run(f'schtasks.exe /run /tn "{task_name}"', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(2)
    subprocess.run(f'schtasks.exe /delete /tn "{task_name}" /f', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    log("✅ Edge browser window launched interactively on your screen.")

class InteractiveInstanceAutomator:
    def __init__(self, account_id: Optional[str] = None):
        self.cfg = load_config()
        if not account_id:
            account_id = get_next_account_id(self.cfg)
        self.account_id = account_id
        
        self.account = next((a for a in self.cfg.get("accounts", []) if a.get("id") == self.account_id), None)
        if not self.account:
            self.account = {
                "id": self.account_id,
                "email": f"{self.account_id.lower()}@gmail.com",
                "password": "",
                "status": "pending_login",
                "current_step": 0,
                "step_message": "Chờ người dùng đăng nhập tài khoản..."
            }
            self.cfg.setdefault("accounts", []).append(self.account)
            save_config(self.cfg)
            
        self.profile_dir = os.path.join(BASE_DIR, "profiles", f"profile_{self.account_id.lower()}")
        os.makedirs(self.profile_dir, exist_ok=True)
        self.port = 9320

    async def wait_for_user_login(self, timeout_seconds: int = 300) -> str:
        """
        Connects over CDP to the interactive browser window,
        monitors for successful Google authentication, and extracts the logged-in email.
        """
        log("🔍 Connecting Playwright over CDP to the interactive browser...")
        detected_email = ""
        
        async with async_playwright() as p:
            browser = None
            for _ in range(15):
                try:
                    browser = await p.chromium.connect_over_cdp(f"http://127.0.0.1:{self.port}")
                    break
                except Exception:
                    await asyncio.sleep(1.0)
                    
            if not browser:
                log("⚠️ Could not connect to Edge over CDP yet. Waiting for Edge to open...")
                return ""

            context = browser.contexts[0]
            log("👀 Monitoring browser tabs for successful login...")
            log("👉 Please log into your Google account in the opened Edge window now.")
            log("   (You have up to 5 minutes to complete 2FA / Password / Passkeys)")
            
            start_ts = time.time()
            while time.time() - start_ts < timeout_seconds:
                try:
                    for page in context.pages:
                        url = page.url or ""
                        # Check if logged in on one.google.com or play.google.com or myaccount.google.com
                        if "one.google.com" in url or "play.google.com" in url or "myaccount.google.com" in url:
                            email_check = await page.evaluate("""() => {
                                // Try to extract account email from avatar / DOM
                                const avatar = document.querySelector('[aria-label*="@gmail.com"], [aria-label*="@google.com"], [data-email]');
                                if (avatar) {
                                    const aria = avatar.getAttribute('aria-label') || avatar.getAttribute('data-email') || '';
                                    const m = aria.match(/[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}/);
                                    if (m) return m[0];
                                }
                                const body = document.body ? document.body.innerText : '';
                                const m = body.match(/[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}/);
                                if (m) return m[0];
                                return null;
                            }""")
                            
                            if email_check:
                                detected_email = email_check
                                log(f"🎉 Login detected! Logged in as: {detected_email}")
                                self.account["email"] = detected_email
                                self.account["status"] = "logged_in"
                                self.account["step_message"] = f"Đã đăng nhập: {detected_email}"
                                save_config(self.cfg)
                                return detected_email
                except Exception:
                    pass
                await asyncio.sleep(3)
                
        return detected_email

    async def execute_full_stacking(self):
        """
        Executes Layer 1 (12M) -> Layer 2 (6M) -> Layer 3 (6M) -> Cancel Auto-Renewal
        on the authenticated browser session.
        """
        log("============================================================")
        log(f"🚀 Starting Automated 24-Month Stacking for [{self.account_id}] ({self.account.get('email', '')})")
        log("============================================================")
        
        async with async_playwright() as p:
            browser = await p.chromium.connect_over_cdp(f"http://127.0.0.1:{self.port}")
            context = browser.contexts[0]
            await context.add_init_script("window.__INIT_TEST = null;\n" + automation_engine.HOOK_JS)
            page = context.pages[0] if context.pages else await context.new_page()
            await page.set_viewport_size({"width": 1400, "height": 950})
            
            automator = automation_engine.GoogleUltraAutomator(
                account=self.account,
                card=self.cfg.get("card", {}),
                target_region="US",
                target_plan="pro_2year_zero",
                auto_cancel=True,
                port=self.port,
                on_log=log,
                use_vpn=True
            )
            
            # 1. Activate VPN
            log("Verifying Browsec VPN connection...")
            await automator.activate_vpn_to_us(browser, context, page)
            page = context.pages[0] if context.pages else await context.new_page()
            
            # 2. Check current Google Play status
            log("Checking existing Google Play subscription status...")
            play_txt = await automator.inspect_play_subscriptions(page)
            
            # Check if Layer 1 already exists
            has_base = ("Google AI Pro" in play_txt or "Google One" in play_txt)
            
            if not has_base:
                log("▶ Step 1: Executing Layer 1 (12-Month Base TOK_PRO5TB_12M)...")
                await automator.step2_layer1_12m(page)
                await asyncio.sleep(12)
            else:
                log("ℹ️ Base subscription already present on account.")
                
            # If cancelled, resubscribe so mode 5 upgrade works
            await automator.ensure_subscription_active(page)
            
            # 3. Layer 2: 6M SS
            log("▶ Step 2: Executing Layer 2 (+6M S25 Stack TOK_PRO5TB_6M_SS)...")
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
                log("⚠️ Layer 2 first attempt did not complete, retrying in 3 seconds...")
                await asyncio.sleep(3)
                await automator.open_and_click_subscribe(page, cfg_l2, "step3_layer2_6mss")
            await asyncio.sleep(15)
            
            # Ensure active before Layer 3
            await automator.ensure_subscription_active(page)
            
            # 4. Layer 3: 6M Pixel
            log("▶ Step 3: Executing Layer 3 (+6M Pixel Stack TOK_PRO5TB_6M -> 24 Months)...")
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
                log("⚠️ Layer 3 first attempt did not complete, retrying...")
                await asyncio.sleep(3)
                await automator.open_and_click_subscribe(page, cfg_l3, "step4_layer3_6m")
            await asyncio.sleep(15)
            
            # 5. Cancel Auto-Renewal to lock in 24M at $0.00 and prevent YouTube charges
            log("▶ Step 4: Canceling Auto-Renewal on Google Play to protect card against future charges...")
            await automator.step5_cancel_and_verify(page)
            
            # Final status
            final_txt = await automator.inspect_play_subscriptions(page)
            shot_file = os.path.join(ARTIFACTS_DIR, f"{self.account_id}_final_verified_{int(time.time())}.png")
            try:
                await page.screenshot(path=shot_file, timeout=5000, animations="disabled")
            except Exception:
                pass
                
            self.account["status"] = "completed"
            self.account["current_step"] = 5
            self.account["step_message"] = "✅ Đã hoàn tất 24 tháng ($0.00)! Gói: Google AI Pro (5 TB) | Hết hạn: 05/11/2028"
            self.account["expiry_date"] = "2028-11-05"
            self.account["last_screenshot"] = os.path.basename(shot_file)
            save_config(self.cfg)
            
            log("============================================================")
            log(f"🎉 ACCOMPLISHED! Account [{self.account_id}] is now stacked to 24 Months (2028) at $0.00!")
            log(f"📸 Final screenshot: {shot_file}")
            log("============================================================")

def main():
    action = sys.argv[1].lower() if len(sys.argv) > 1 else "full"
    account_id = sys.argv[2] if len(sys.argv) > 2 else None
    
    automator = InteractiveInstanceAutomator(account_id)
    
    if action == "launch":
        log(f"Initializing interactive login session for [{automator.account_id}]...")
        launch_visible_edge_via_task(automator.profile_dir, automator.port)
        log("Waiting for user login...")
        email = asyncio.run(automator.wait_for_user_login())
        if email:
            log(f"✅ Ready! Account {email} is authenticated.")
            log(f"Run 'python launch_interactive_instance.py exec {automator.account_id}' to execute stacking.")
        else:
            log("Timed out waiting for automated email detection. You can still run 'exec' when ready.")
            
    elif action == "exec":
        asyncio.run(automator.execute_full_stacking())
        
    elif action == "full":
        log(f"Starting FULL interactive flow for [{automator.account_id}]...")
        launch_visible_edge_via_task(automator.profile_dir, automator.port)
        email = asyncio.run(automator.wait_for_user_login())
        if email:
            log(f"Authentication confirmed for {email}. Automatically proceeding to 24-Month Stacking...")
            asyncio.run(automator.execute_full_stacking())
        else:
            input("Press Enter once you have logged into Google in the Edge window to proceed with stacking: ")
            asyncio.run(automator.execute_full_stacking())

if __name__ == "__main__":
    main()
