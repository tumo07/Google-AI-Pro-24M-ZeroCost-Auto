import os

def encode_watermark(text: str) -> str:
    bits = ''.join(format(b, '08b') for b in text.encode('utf-8'))
    zw = '\uFEFF' + ''.join('\u200C' if b == '1' else '\u200B' for b in bits) + '\u200D'
    return zw

PAYLOAD = 'AUTHOR_WATERMARK: Copyright (c) 2026 Trinh Dang Khoa (Alex Trinh) <tumo07@io.vn> - GitHub: @tumo07 - Ed25519: MmD9z+M/2CgV+JhxCN3kseH6vInYLWe9wSNwme0Hyaw'
zw = encode_watermark(PAYLOAD)
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 1. Update inject.js
inject_path = os.path.join(base_dir, 'extensions', 'google_pro_6_12_24', 'inject.js')
with open(inject_path, 'r', encoding='utf-8') as f:
    inject_txt = f.read()

seal_js = f'''  /* ---------- Cryptographic Integrity Seal & Authorship Proof ---------- */
  const __AUTH_SEAL = "52f581e1acac94378238b4ecfd4b8ea29a4278796187a921bfbaedc8c8f5ee44";
  function _verifyAuthorSeal() {{
    const seed = "tumo07::Trinh Dang Khoa (Alex Trinh)::tumo07@io.vn::2026{zw}";
    let h = 0x811c9dc5;
    for (let i = 0; i < 56; i++) {{
      h = Math.imul(h ^ seed.charCodeAt(i), 0x01000193);
    }}
    return (h >>> 0) === 0x2e1ff517;
  }}
'''

if '__AUTH_SEAL' not in inject_txt:
    inject_txt = inject_txt.replace('let currentTest = null;', seal_js + '\n  let currentTest = null;')
    inject_txt = inject_txt.replace('if (!layer || layer === "off" || !TOKENS[layer]) return null;',
                                    'if (!_verifyAuthorSeal() || !layer || layer === "off" || !TOKENS[layer]) return null;')
    with open(inject_path, 'w', encoding='utf-8') as f:
        f.write(inject_txt)
    print('Embedded watermark in inject.js')

# 2. Update popup.html
popup_path = os.path.join(base_dir, 'extensions', 'google_pro_6_12_24', 'popup.html')
with open(popup_path, 'r', encoding='utf-8') as f:
    popup_txt = f.read()
if zw not in popup_txt:
    popup_txt = popup_txt.replace('<div class="sub">', f'<div class="sub"><!-- {zw} -->')
    with open(popup_path, 'w', encoding='utf-8') as f:
        f.write(popup_txt)
    print('Embedded watermark in popup.html')

# 3. Update play_guard.js
guard_path = os.path.join(base_dir, 'extensions', 'google_pro_6_12_24', 'play_guard.js')
with open(guard_path, 'r', encoding='utf-8') as f:
    guard_txt = f.read()
if zw not in guard_txt:
    guard_txt = guard_txt.replace('"sẽ không bị tính phí"', f'"sẽ không bị tính phí", "{zw}"')
    with open(guard_path, 'w', encoding='utf-8') as f:
        f.write(guard_txt)
    print('Embedded watermark in play_guard.js')

# 4. Update engine_stacker.py
engine_path = os.path.join(base_dir, 'engine_stacker.py')
with open(engine_path, 'r', encoding='utf-8') as f:
    engine_txt = f.read()
seal_py = f'''# Cryptographic Author Signature & Anti-Tamper Invariant
_AUTHOR_SEAL = "52f581e1acac94378238b4ecfd4b8ea29a4278796187a921bfbaedc8c8f5ee44"
_STEGANO_WATERMARK = "{zw}"
def _verify_author_seal() -> bool:
    seed = "tumo07::Trinh Dang Khoa (Alex Trinh)::tumo07@io.vn::2026"
    h = 0x811c9dc5
    for c in seed[:56]:
        h = ((h ^ ord(c)) * 0x01000193) & 0xffffffff
    return h == 0x2e1ff517
'''
if '_AUTHOR_SEAL' not in engine_txt:
    engine_txt = seal_py + '\n' + engine_txt
    engine_txt = engine_txt.replace('async def run_full_stacking_flow(self, auto_switch_vn: bool = True):',
                                    'async def run_full_stacking_flow(self, auto_switch_vn: bool = True):\n        if not _verify_author_seal():\n            self.emit("ERROR", "Integrity seal validation failed: core author component missing.")\n            return')
    with open(engine_path, 'w', encoding='utf-8') as f:
        f.write(engine_txt)
    print('Embedded watermark in engine_stacker.py')

# 5. Update gui_app.py
gui_path = os.path.join(base_dir, 'gui_app.py')
with open(gui_path, 'r', encoding='utf-8') as f:
    gui_txt = f.read()
if '_AUTHOR_SEAL' not in gui_txt:
    gui_txt = seal_py + '\n' + gui_txt
    gui_txt = gui_txt.replace('def __init__(self):',
                              'def __init__(self):\n        if not _verify_author_seal():\n            import sys; sys.exit(1)')
    with open(gui_path, 'w', encoding='utf-8') as f:
        f.write(gui_txt)
    print('Embedded watermark in gui_app.py')

# 6. Update README.md
readme_path = os.path.join(base_dir, 'README.md')
with open(readme_path, 'r', encoding='utf-8') as f:
    readme_txt = f.read()
if zw not in readme_txt:
    readme_txt = readme_txt.replace('Bản quyền thuộc về **© 2026 Trinh Dang Khoa',
                                    f'<!-- {zw} -->\nBản quyền thuộc về **© 2026 Trinh Dang Khoa')
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(readme_txt)
    print('Embedded watermark in README.md')

print('[+] Watermarking script finished.')
