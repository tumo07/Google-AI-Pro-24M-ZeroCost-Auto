"""
Google AI Pro 24M Zero-Cost Auto — Cryptographic Release Signer
Signs all codebase files using Ed25519 asymmetric cryptography.
SPDX-License-Identifier: MIT
Copyright (c) 2026 Trinh Dang Khoa (Alex Trinh) <tumo07@io.vn>
"""
import os
import hashlib
from cryptography.hazmat.primitives.asymmetric import ed25519
from cryptography.hazmat.primitives import serialization

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KEY_PRIV_PATH = os.path.join(ROOT_DIR, "release_key.priv")
KEY_PUB_PATH = os.path.join(ROOT_DIR, "RELEASE_AUTHOR_PUBLIC_KEY.pub")
CHECKSUMS_PATH = os.path.join(ROOT_DIR, "CHECKSUMS.sha256")
SIG_PATH = os.path.join(ROOT_DIR, "CHECKSUMS.sha256.sig")

EXCLUDE_PATTERNS = [
    ".git", "__pycache__", "profiles", "artifacts", "temp",
    "release_key.priv", "CHECKSUMS.sha256", "CHECKSUMS.sha256.sig",
    "config.local.json", ".png", ".log"
]

def should_hash(rel_path: str) -> bool:
    for pat in EXCLUDE_PATTERNS:
        if pat in rel_path.replace("\\", "/"):
            return False
    return True

def generate_or_load_keys():
    if os.path.exists(KEY_PRIV_PATH):
        with open(KEY_PRIV_PATH, "rb") as f:
            priv_key = serialization.load_pem_private_key(f.read(), password=None)
    else:
        priv_key = ed25519.Ed25519PrivateKey.generate()
        with open(KEY_PRIV_PATH, "wb") as f:
            f.write(priv_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.NoEncryption()
            ))
        print(f"[+] Generated new Ed25519 private key: {KEY_PRIV_PATH}")

    pub_key = priv_key.public_key()
    pub_bytes = pub_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    with open(KEY_PUB_PATH, "wb") as f:
        f.write(pub_bytes)
    print(f"[+] Exported official public key: {KEY_PUB_PATH}")
    return priv_key, pub_key

def compute_checksums():
    checksum_lines = []
    for root, dirs, files in os.walk(ROOT_DIR):
        for f in sorted(files):
            full_path = os.path.join(root, f)
            rel_path = os.path.relpath(full_path, ROOT_DIR).replace("\\", "/")
            if not should_hash(rel_path):
                continue
            with open(full_path, "rb") as fp:
                digest = hashlib.sha256(fp.read()).hexdigest()
            checksum_lines.append(f"{digest}  {rel_path}\n")

    manifest_data = "".join(checksum_lines).encode("utf-8")
    with open(CHECKSUMS_PATH, "wb") as f:
        f.write(manifest_data)
    print(f"[+] Hashed {len(checksum_lines)} repository files into {CHECKSUMS_PATH}")
    return manifest_data

def sign_manifest(priv_key: ed25519.Ed25519PrivateKey, manifest_data: bytes):
    sig = priv_key.sign(manifest_data)
    with open(SIG_PATH, "wb") as f:
        f.write(sig)
    print(f"[+] Cryptographically signed release with Ed25519: {SIG_PATH}")

if __name__ == "__main__":
    priv, pub = generate_or_load_keys()
    data = compute_checksums()
    sign_manifest(priv, data)
    print("[*] Release signing completed successfully!")
