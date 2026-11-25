# Google AI Pro 24M Zero-Cost Automator v2.0.0

## Highlights
- **New Android Play Billing Engine (`android_engine.py` / `run_android_27m.py` / `Run_Android_27M.bat`):**
  - 27-month (~820 days) stacking sequence via **ADB + Frida 16.5.9** on MuMu Player 12 / rooted Android: `pro3` (`eft-3mo`) -> `pro12` (`12months-eft`) -> `pro6` (`6months-eft`) -> `pro6b` (`6months-eft-2`) using `SubscriptionUpdateParams` (`CHARGE_FULL_PRICE=5`).
  - Automatic ADB port discovery (`16384`, `16385`, `7555`, `16416`, `21503`, `62001`), `adb root`, `frida-server` setup, and Play Billing module deployment.
  - Strict `$0.00` Zero-Cost Gate via `uiautomator`, password verification prompt support, and Play Store auto-renewal cancellation verified against `library.db` (`subs_auto_renewing = 0`).
- **Updated GUI (`gui_app.py` v2.0.0):**
  - Added dedicated **Android Play Billing 27-Month** controls directly in the Wizard tab (`Check ADB`, `Scan Offers`, `Run 27M Stack`, `Cancel Auto-Renewal`).
- **Cryptographic Verification:**
  - Signed with Ed25519 (`CHECKSUMS.sha256` + `CHECKSUMS.sha256.sig`). Verify with `python tools/verify_release.py`.
