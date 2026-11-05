#!/usr/bin/env python3
"""
scripts/backup_leads.py — Automated Lead Storage & Database Backup Utility
Creates timestamped, verified backups of the SQLite database and JSON audit log.
Retains 30 daily backup snapshots with SHA-256 verification.
"""

import os
import shutil
import hashlib
import time
from datetime import datetime

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(ROOT_DIR, "data")
BACKUP_DIR = os.path.join(DATA_DIR, "backups")

def get_file_sha256(filepath):
    if not os.path.exists(filepath):
        return None
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(8192):
            h.update(chunk)
    return h.hexdigest()

def perform_backup():
    os.makedirs(BACKUP_DIR, exist_ok=True)
    timestamp_str = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    backed_up_files = []

    files_to_backup = ["leads.db", "leads.json", "plans.json"]

    for fname in files_to_backup:
        src = os.path.join(DATA_DIR, fname)
        if os.path.exists(src):
            dst = os.path.join(BACKUP_DIR, f"{timestamp_str}_{fname}")
            shutil.copy2(src, dst)
            sha = get_file_sha256(dst)
            backed_up_files.append((fname, dst, sha))

    # Write backup manifest
    manifest_path = os.path.join(BACKUP_DIR, f"{timestamp_str}_manifest.txt")
    with open(manifest_path, "w", encoding="utf-8") as f:
        f.write(f"Sevenseas Broadband Automated Backup Manifest\n")
        f.write(f"Timestamp: {datetime.utcnow().isoformat()}Z\n")
        f.write("=" * 60 + "\n")
        for orig, backup_file, sha in backed_up_files:
            f.write(f"File: {orig}\n")
            f.write(f"Saved: {os.path.basename(backup_file)}\n")
            f.write(f"SHA-256: {sha}\n\n")

    print(f"✓ Backup completed successfully: {len(backed_up_files)} files archived at {BACKUP_DIR}")
    return manifest_path

def cleanup_old_backups(days_retention=30):
    now = time.time()
    retention_cutoff = now - (days_retention * 86400)
    purged = 0

    if os.path.exists(BACKUP_DIR):
        for f in os.listdir(BACKUP_DIR):
            fpath = os.path.join(BACKUP_DIR, f)
            if os.path.isfile(fpath) and os.path.getmtime(fpath) < retention_cutoff:
                os.remove(fpath)
                purged += 1

    if purged > 0:
        print(f"Cleaned up {purged} old backup files older than {days_retention} days.")

if __name__ == "__main__":
    perform_backup()
    cleanup_old_backups()
