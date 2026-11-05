import asyncio
import json
import os
import sys
import time

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

def load_config():
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def save_config(cfg):
    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
        json.dump(cfg, f, ensure_ascii=False, indent=2)

def log_msg(msg):
    ts = time.strftime("%H:%M:%S")
    line = f"[{ts}] {msg}"
    print(line, flush=True)
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(line + "\n")

def on_state_patch(patch):
    c = load_config()
    for acc in c.get("accounts", []):
        if acc["id"] == "Account_1":
            acc.update(patch)
            break
    save_config(c)

async def main():
    cfg = load_config()
    target_acc = next((a for a in cfg.get("accounts", []) if a["id"] == "Account_1"), None)
    if not target_acc:
        log_msg("❌ Account_1 not found in config.json")
        return

    log_msg(f"🚀 Starting automation for {target_acc['email']} (VPN: {cfg.get('use_vpn', False)})...")

    automator = automation_engine.GoogleUltraAutomator(
        account=target_acc,
        card=cfg.get("card", {}),
        target_region=cfg.get("target_region", "US"),
        target_plan=cfg.get("target_plan", "pro_2year_zero"),
        auto_cancel=cfg.get("auto_cancel", True),
        proxy_template=cfg.get("proxy_template", ""),
        port=9320,
        on_log=log_msg,
        on_state=on_state_patch,
        use_vpn=cfg.get("use_vpn", False),
    )

    start_step = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    await automator.run_pipeline(start_step=start_step)
    log_msg("🏁 run_pipeline completed.")

if __name__ == "__main__":
    asyncio.run(main())
