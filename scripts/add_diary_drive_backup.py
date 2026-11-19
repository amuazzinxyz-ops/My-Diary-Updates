#!/usr/bin/env python3
"""Apply only the isolated Google Drive crypto foundation to an extracted build copy."""
from pathlib import Path
import argparse
import re
import shutil

ROOT = Path(__file__).resolve().parent
parser = argparse.ArgumentParser()
parser.add_argument("--project", required=True, type=Path)
args = parser.parse_args()
project = args.project.resolve()
gradle = project / "app" / "build.gradle.kts"
if not gradle.is_file():
    raise SystemExit("BLOCKED: extracted Android app/build.gradle.kts is missing")

main_target = project / "app/src/main/java/com/muazzin/diary/backup/DiaryBackupCrypto.kt"
test_target = project / "app/src/test/java/com/muazzin/diary/backup/DiaryBackupCryptoTest.kt"
snapshot_target = project / "app/src/main/java/com/muazzin/diary/backup/DiaryBackupSnapshot.kt"
snapshot_test_target = project / "app/src/test/java/com/muazzin/diary/backup/DiaryBackupSnapshotTest.kt"
main_target.parent.mkdir(parents=True, exist_ok=True)
test_target.parent.mkdir(parents=True, exist_ok=True)
shutil.copyfile(ROOT / "drive_backup_src/DiaryBackupCrypto.kt", main_target)
shutil.copyfile(ROOT / "drive_backup_src/DiaryBackupCryptoTest.kt", test_target)
shutil.copyfile(ROOT / "drive_backup_src/DiaryBackupSnapshot.kt", snapshot_target)
shutil.copyfile(ROOT / "drive_backup_src/DiaryBackupSnapshotTest.kt", snapshot_test_target)

text = gradle.read_text(encoding="utf-8")
match = re.search(r"dependencies\s*\{([^}]*)\}", text, re.S)
if not match:
    raise SystemExit("BLOCKED: Gradle dependencies block not found")
body = match.group(1)
required = [
    'implementation("org.bouncycastle:bcprov-jdk18on:1.86")',
    'testImplementation("junit:junit:4.13.2")',
]
for dependency in required:
    if dependency not in body:
        body = body.rstrip() + "\n    " + dependency + "\n"
text = text[:match.start(1)] + body + text[match.end(1):]
gradle.write_text(text, encoding="utf-8")

check = gradle.read_text(encoding="utf-8")
if any(dep not in check for dep in required) or not all(p.is_file() for p in (main_target, test_target, snapshot_target, snapshot_test_target)):
    raise SystemExit("BLOCKED: Drive crypto foundation was not applied exactly")
print("PASS: isolated Argon2id/AES-GCM crypto and complete snapshot contract sources/tests applied to build copy")
