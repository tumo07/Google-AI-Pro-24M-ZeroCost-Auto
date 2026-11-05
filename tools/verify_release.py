"""
Google AI Pro 24M Zero-Cost Auto — Cryptographic Release Verifier
Verifies repository integrity and author authenticity using Ed25519 signatures.
SPDX-License-Identifier: MIT
Copyright (c) 2026 Trinh Dang Khoa (Alex Trinh) <tumo07@io.vn>
"""
import os
import sys
import hashlib
from cryptography.hazmat.primitives.asymmetric import ed25519
from cryptography.hazmat.primitives import serialization
from cryptography.exceptions import InvalidSignature

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KEY_PUB_PATH = os.path.join(ROOT_DIR, "RELEASE_AUTHOR_PUBLIC_KEY.pub")
CHECKSUMS_PATH = os.path.join(ROOT_DIR, "CHECKSUMS.sha256")
SIG_PATH = os.path.join(ROOT_DIR, "CHECKSUMS.sha256.sig")

def verify_release() -> bool:
    print("=" * 70)
    print("  Google AI Pro 24M Zero-Cost Auto — Authenticity Verification")
    print("  Author: Trinh Dang Khoa (Alex Trinh) <tumo07@io.vn> | GitHub: @tumo07")
    print("=" * 70)

    if not os.path.exists(KEY_PUB_PATH):
        print("[-] FAILED: Public key not found at", KEY_PUB_PATH)
        return False
    if not os.path.exists(CHECKSUMS_PATH):
        print("[-] FAILED: Checksums manifest not found at", CHECKSUMS_PATH)
        return False
    if not os.path.exists(SIG_PATH):
        print("[-] FAILED: Digital signature not found at", SIG_PATH)
        return False

    with open(KEY_PUB_PATH, "rb") as f:
        pub_key = serialization.load_pem_public_key(f.read())
    with open(CHECKSUMS_PATH, "rb") as f:
        manifest_data = f.read()
    with open(SIG_PATH, "rb") as f:
        signature = f.read()

    # 1. Verify digital signature
    try:
        pub_key.verify(signature, manifest_data)
        print("[+] [1/2] DIGITAL SIGNATURE VERIFIED: Authentic cryptographic signature from author (@tumo07).")
    except InvalidSignature:
        print("[-] [1/2] SIGNATURE MISMATCH: The signature is invalid! This release may be tampered or unauthorized.")
        return False

    # 2. Verify file hashes
    lines = manifest_data.decode("utf-8").splitlines()
    mismatches = []
    verified_count = 0

    for line in lines:
        if not line.strip():
            continue
        expected_hash, rel_path = line.split("  ", 1)
        full_path = os.path.join(ROOT_DIR, rel_path.replace("/", os.sep))
        if not os.path.exists(full_path):
            mismatches.append(f"Missing file: {rel_path}")
            continue
        with open(full_path, "rb") as fp:
            actual_hash = hashlib.sha256(fp.read()).hexdigest()
        if actual_hash != expected_hash:
            mismatches.append(f"Hash mismatch in: {rel_path}")
        else:
            verified_count += 1

    if mismatches:
        print(f"[-] [2/2] INTEGRITY CHECK FAILED: {len(mismatches)} files do not match manifest:")
        for m in mismatches[:10]:
            print("    *", m)
        return False

    print(f"[+] [2/2] INTEGRITY VERIFIED: All {verified_count} repository files match official SHA-256 hashes.")
    print("\n>>> VERIFICATION PASSED: Genuine, Untampered Open-Source Release. <<<")
    return True

if __name__ == "__main__":
    success = verify_release()
    sys.exit(0 if success else 1)
