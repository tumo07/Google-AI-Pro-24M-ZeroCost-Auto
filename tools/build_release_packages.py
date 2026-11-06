import os
import sys
import shutil
import zipfile

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RELEASE_OUT = os.path.join(BASE_DIR, "release_assets")
os.makedirs(RELEASE_OUT, exist_ok=True)

print(f"Building release assets from: {BASE_DIR}")

def add_file_with_unix_perms(zf, file_path, arc_path, is_exec=False):
    with open(file_path, "rb") as f:
        data = f.read()
    zinfo = zipfile.ZipInfo(arc_path)
    zinfo.date_time = (2026, 11, 6, 10, 0, 0)
    zinfo.compress_type = zipfile.ZIP_DEFLATED
    zinfo.create_system = 3  # UNIX
    if is_exec:
        zinfo.external_attr = 0o100755 << 16  # rwxr-xr-x
    else:
        zinfo.external_attr = 0o100644 << 16  # rw-r--r--
    zf.writestr(zinfo, data)

# 1. Package macOS Universal Bundle
print("Preparing macOS Universal bundle with POSIX 0755 permissions...")
mac_zip_path = os.path.join(RELEASE_OUT, "Google-AI-Pro-Automator-v1.2.0-macOS-Universal.zip")

mac_files = [
    "gui_app.py", "engine_stacker.py", "automation_engine.py", "launch_interactive_instance.py",
    "Google_AI_Pro_Automator.command", "setup_macos.sh", "run_gui.sh", "run_stacker.sh",
    "custom_stacking_flow.py", "run_account.py", "run_layer2_layer3_step5.py", "stack_layers_now.py",
    "config.example.json", "config.json", "requirements.txt",
    "README.md", "HUONG_DAN_CHI_TIET.md", "CHANGELOG.md", "LICENSE"
]

with zipfile.ZipFile(mac_zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
    prefix = "Google-AI-Pro-Automator-macOS"
    
    # Add files
    for fname in mac_files:
        fpath = os.path.join(BASE_DIR, fname)
        if os.path.exists(fpath):
            arc = f"{prefix}/{fname}"
            is_exec = fname.endswith((".command", ".sh"))
            add_file_with_unix_perms(zf, fpath, arc, is_exec=is_exec)
            
    # Add tools directory (check_dependencies, etc.)
    tools_dir = os.path.join(BASE_DIR, "tools")
    if os.path.exists(tools_dir):
        for root, dirs, files in os.walk(tools_dir):
            for file in files:
                if file.endswith((".py", ".sh", ".bat")):
                    full_p = os.path.join(root, file)
                    rel_p = os.path.relpath(full_p, BASE_DIR).replace("\\", "/")
                    arc = f"{prefix}/{rel_p}"
                    is_exec = file.endswith((".sh", ".command", ".bat"))
                    add_file_with_unix_perms(zf, full_p, arc, is_exec=is_exec)

    # Add Google AI Pro Automator.app bundle
    app_dir = os.path.join(BASE_DIR, "Google AI Pro Automator.app")
    if os.path.exists(app_dir):
        for root, dirs, files in os.walk(app_dir):
            for file in files:
                full_p = os.path.join(root, file)
                rel_p = os.path.relpath(full_p, BASE_DIR).replace("\\", "/")
                arc = f"{prefix}/{rel_p}"
                is_exec = (file == "launcher" or file.endswith((".sh", ".command")))
                add_file_with_unix_perms(zf, full_p, arc, is_exec=is_exec)
                
    # Add extensions directory
    ext_dir = os.path.join(BASE_DIR, "extensions")
    if os.path.exists(ext_dir):
        for root, dirs, files in os.walk(ext_dir):
            for file in files:
                full_p = os.path.join(root, file)
                rel_p = os.path.relpath(full_p, BASE_DIR).replace("\\", "/")
                arc = f"{prefix}/{rel_p}"
                add_file_with_unix_perms(zf, full_p, arc, is_exec=False)

print(f"[OK] Created: {mac_zip_path} ({os.path.getsize(mac_zip_path) / 1024:.2f} KB)")

# 2. Package Windows Portable Python Bundle
print("Preparing Windows Portable Python bundle with automated bootstrap...")
win_zip_path = os.path.join(RELEASE_OUT, "Google-AI-Pro-Automator-v1.2.0-Windows-Portable.zip")

win_files = [
    "gui_app.py", "engine_stacker.py", "automation_engine.py", "launch_interactive_instance.py",
    "start_gui.bat", "Google_AI_Pro_Tool.bat", "3_Chay_Custom_Flow.bat", "4_Dang_Nhap_Account_Moi.bat",
    "5_Chay_Nang_Cap_24T.bat", "6_Tu_Dong_A_Den_Z_Moi_Acc.bat", "launch_visible_automation.bat",
    "custom_stacking_flow.py", "run_account.py", "run_layer2_layer3_step5.py", "stack_layers_now.py",
    "config.example.json", "config.json", "requirements.txt",
    "README.md", "HUONG_DAN_CHI_TIET.md", "CHANGELOG.md", "LICENSE"
]

with zipfile.ZipFile(win_zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
    prefix = "Google-AI-Pro-Automator-Windows-Portable"
    
    for fname in win_files:
        fpath = os.path.join(BASE_DIR, fname)
        if os.path.exists(fpath):
            arc = f"{prefix}/{fname}"
            zf.write(fpath, arc)
            
    # Add tools
    tools_dir = os.path.join(BASE_DIR, "tools")
    if os.path.exists(tools_dir):
        for root, dirs, files in os.walk(tools_dir):
            for file in files:
                if file.endswith((".py", ".bat")):
                    full_p = os.path.join(root, file)
                    rel_p = os.path.relpath(full_p, BASE_DIR).replace("\\", "/")
                    arc = f"{prefix}/{rel_p}"
                    zf.write(full_p, arc)
                    
    # Add extensions
    ext_dir = os.path.join(BASE_DIR, "extensions")
    if os.path.exists(ext_dir):
        for root, dirs, files in os.walk(ext_dir):
            for file in files:
                full_p = os.path.join(root, file)
                rel_p = os.path.relpath(full_p, BASE_DIR).replace("\\", "/")
                arc = f"{prefix}/{rel_p}"
                zf.write(full_p, arc)

print(f"[OK] Created: {win_zip_path} ({os.path.getsize(win_zip_path) / 1024:.2f} KB)")
print("All distribution packages created successfully!")
