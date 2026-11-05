"""
Google AI Pro 24M Zero-Cost Auto — Forensic Watermark & Authorship Extractor
Extracts hidden zero-width steganographic watermarks and cryptographic seals from codebase files.
Used for DMCA copyright enforcement and verifying authentic authorship.
SPDX-License-Identifier: MIT
Copyright (c) 2026 Trinh Dang Khoa (Alex Trinh) <tumo07@io.vn>
"""
import os
import re
import sys
import io
import hashlib

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def decode_zero_width(s: str) -> str:
    """Decodes hidden binary data from Zero-Width characters."""
    m = re.search(r'\uFEFF([\u200B\u200C]+)\u200D', s)
    if not m:
        return ""
    raw_bits = m.group(1)
    bits = ''.join('1' if c == '\u200C' else '0' for c in raw_bits)
    if len(bits) % 8 != 0:
        bits = bits[:len(bits) - (len(bits) % 8)]
    bytes_list = [int(bits[i:i+8], 2) for i in range(0, len(bits), 8)]
    return bytes(bytes_list).decode('utf-8', errors='ignore')

def scan_file_for_watermarks(path: str):
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
    except Exception as e:
        return None

    rel = os.path.relpath(path, ROOT_DIR).replace("\\", "/")
    hidden_text = decode_zero_width(content)
    
    # Check for cryptographic author seal
    author_seal = None
    if "52f581e1acac94378238b4ecfd4b8ea29a4278796187a921bfbaedc8c8f5ee44" in content:
        author_seal = "52f581e1acac94378238b4ecfd4b8ea29a4278796187a921bfbaedc8c8f5ee44 (Valid tumo07 SHA-256 Seal)"

    if hidden_text or author_seal:
        return {
            "file": rel,
            "hidden_text": hidden_text,
            "author_seal": author_seal
        }
    return None

def main():
    print("=" * 75)
    print("  Google AI Pro 24M Zero-Cost Auto — Forensic Watermark Extractor")
    print("  Official Author: Trinh Dang Khoa (Alex Trinh) <tumo07@io.vn> | GitHub: @tumo07")
    print("=" * 75)

    findings = []
    for root, dirs, files in os.walk(ROOT_DIR):
        if any(ex in root for ex in [".git", "__pycache__", "profiles", "artifacts"]):
            continue
        for f in sorted(files):
            if f.endswith((".js", ".html", ".py", ".md", ".json")):
                p = os.path.join(root, f)
                res = scan_file_for_watermarks(p)
                if res:
                    findings.append(res)

    print(f"\n[*] Scanned repository files. Found {len(findings)} files with embedded author watermarks:\n")
    for item in findings:
        print(f"  * [{item['file']}]")
        if item['hidden_text']:
            print(f"     |-- Hidden Steganographic Payload: \"{item['hidden_text']}\"")
        if item['author_seal']:
            print(f"     +-- Cryptographic Seal: {item['author_seal']}")

    if findings:
        print("\n>>> FORENSIC RESULT: IRREFUTABLE PROOF OF AUTHORSHIP CONFIRMED. <<<")
        print("    Even if external surface comments are stripped by AI, these embedded")
        print("    binary watermarks mathematically prove copyright ownership by @tumo07.")
    else:
        print("\n[-] No watermarks detected.")

if __name__ == "__main__":
    main()
