#!/usr/bin/env python3
"""Inject the Google Drive encrypted-backup UI into the isolated Diary build copy."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PROJECT = Path("diary-project/app/src/main")
assets = PROJECT / "assets"
html_path = assets / "index.html"
source = ROOT / "drive_backup_src/diary_google_drive_ui.js"
target = assets / "diary_google_drive_ui.js"

if not html_path.is_file() or not source.is_file():
    raise SystemExit("BLOCKED: Diary HTML or Google Drive UI source is missing")
html = html_path.read_text(encoding="utf-8")
if "diaryDiaryMePanel" not in html:
    raise SystemExit("BLOCKED: expected Me panel is missing from Diary HTML")
if "diary_google_drive_ui.js" in html:
    raise SystemExit("BLOCKED: unexpected pre-existing Google Drive UI injection")
if "diary_snapshot_collector.js" not in html:
    raise SystemExit("BLOCKED: snapshot collector must be injected before Drive UI")
target.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")
marker = "</body>"
position = html.rfind(marker)
if position < 0:
    raise SystemExit("BLOCKED: final HTML body close is missing")
tag = '<script src="diary_google_drive_ui.js"></script>\n'
html = html[:position] + tag + html[position:]
html_path.write_text(html, encoding="utf-8")
if html.count('src="diary_google_drive_ui.js"') != 1:
    raise SystemExit("BLOCKED: Drive UI must be injected exactly once")
if not target.is_file() or target.stat().st_size < 1000:
    raise SystemExit("BLOCKED: Drive UI asset was not copied")
print("PASS: Google Drive encrypted-backup UI injected into Me panel build copy")
