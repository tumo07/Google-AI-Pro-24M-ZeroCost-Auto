"""
Google AI Pro 24M Zero-Cost Auto — v2.0.0 Android 27-Month CLI Runner
Usage:
  python run_android_27m.py --check
  python run_android_27m.py --list
  python run_android_27m.py --stack --password "YourGooglePassword"
  python run_android_27m.py --plan pro12 --stack

SPDX-License-Identifier: MIT
Copyright (c) 2026 Trinh Dang Khoa (Alex Trinh) <tumo07@io.vn>
"""
import argparse
import sys
from android_engine import AndroidBillingEngine


def main() -> int:
    ap = argparse.ArgumentParser(description="Google AI Pro 27-Month Android Play Billing Automator (v2.0.0)")
    ap.add_argument("--serial", default=None, help="ADB device serial (e.g. 127.0.0.1:16384)")
    ap.add_argument("--check", action="store_true", help="Check ADB, root, frida-server, and Billing module")
    ap.add_argument("--list", action="store_true", help="List available Google One free trial offers")
    ap.add_argument("--stack", action="store_true", help="Run full 27-month sequence: pro3 -> pro12 -> pro6 -> pro6b")
    ap.add_argument("--plan", choices=["pro3", "pro12", "pro6", "pro6b", "pro6c"], help="Run a single plan")
    ap.add_argument("--upgrade", action="store_true", help="Use SubscriptionUpdateParams (with --plan)")
    ap.add_argument("--cancel", action="store_true", help="Cancel auto-renewal on Google Play and verify")
    ap.add_argument("--no-cancel", action="store_true", help="Skip auto-cancel after --stack")
    ap.add_argument("--password", default="", help="Google password if Play Billing prompts Verify")
    args = ap.parse_args()

    eng = AndroidBillingEngine(serial=args.serial)

    if args.check:
        eng.connect_device()
        eng.ensure_root_and_frida()
        st = eng.read_subscription_state()
        print(f"[OK] Device ready: {eng.serial}")
        if st:
            print(f"[*] Current sub: {st['account']} | {st['doc_id']} | auto_renew={st['auto_renewing']}")
        return 0

    if args.list:
        offers = eng.list_offers()
        if not offers:
            print("[-] No offers returned. Ensure Google One and Play Store are signed in.")
            return 1
        print(f"\n=== Available Offers ({len(offers)}) ===")
        for o in offers:
            tag = "FREE" if str(o.get("micros")) == "0" else f"{o.get('micros')} micros"
            print(f"  {o.get('product'):<26} offerId={o.get('id'):<24} {o.get('period'):<5} [{tag}]")
        return 0

    if args.cancel:
        return 0 if eng.cancel_auto_renewal() else 1

    if args.plan:
        ok = eng.apply_plan(args.plan, stack=args.upgrade, password=args.password)
        return 0 if ok else 1

    if args.stack:
        ok = eng.run_27m_stack(password=args.password, auto_cancel=not args.no_cancel)
        return 0 if ok else 1

    ap.print_help()
    return 1


if __name__ == "__main__":
    sys.exit(main())
