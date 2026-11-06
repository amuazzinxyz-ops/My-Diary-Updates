#!/usr/bin/env python3
"""Apply a separate, Diary-only Android package identity to the extracted build copy."""
from pathlib import Path
import re
import shutil
import xml.etree.ElementTree as ET

root = Path("diary-project/app")
gradle = root / "build.gradle.kts"
manifest = root / "src/main/AndroidManifest.xml"
if not gradle.is_file() or not manifest.is_file():
    raise SystemExit("FAIL: Android app Gradle file or manifest missing")

g = gradle.read_text(encoding="utf-8")
if not re.search(r'applicationId[ ]*=[ ]*"[^"]+"', g):
    raise SystemExit("FAIL: applicationId declaration not found")
g = re.sub(r'(applicationId[ ]*=[ ]*)"[^"]+"', lambda m: m.group(1) + '"com.personal.diaryapp"', g, count=1)
gradle.write_text(g, encoding="utf-8")

ET.register_namespace("android", "http://schemas.android.com/apk/res/android")
tree = ET.parse(manifest)
app = tree.getroot().find("application")
if app is None:
    raise SystemExit("FAIL: application element missing")
android = "{http://schemas.android.com/apk/res/android}"
app.set(android + "label", "My Diary")
app.set(android + "icon", "@drawable/my_diary_icon")
if android + "roundIcon" in app.attrib:
    app.set(android + "roundIcon", "@drawable/my_diary_icon")
tree.write(manifest, encoding="utf-8", xml_declaration=True)

artwork = Path("assets/my-diary-icon.jpg")
if not artwork.is_file():
    raise SystemExit("FAIL: custom original My Diary artwork is missing")
drawable_nodpi = root / "src/main/res/drawable-nodpi"
drawable_nodpi.mkdir(parents=True, exist_ok=True)
shutil.copy2(artwork, drawable_nodpi / "my_diary_icon.jpg")

drawable = root / "src/main/res/drawable"
drawable.mkdir(parents=True, exist_ok=True)
icon = drawable / "ic_diary_launcher.xml"
icon.write_text("""<?xml version="1.0" encoding="utf-8"?>
<vector xmlns:android="http://schemas.android.com/apk/res/android"
    android:width="108dp" android:height="108dp" android:viewportWidth="108" android:viewportHeight="108">
    <path android:fillColor="#6330B8" android:pathData="M0,0h108v108h-108z"/>
    <path android:fillColor="#FFFDF8" android:pathData="M22,25 C22,20 26,17 32,17 H52 C57,17 61,20 61,25 V83 C58,78 54,76 49,76 H32 C26,76 22,80 22,85 Z"/>
    <path android:fillColor="#F7E9C2" android:pathData="M86,25 C86,20 82,17 76,17 H56 C51,17 47,20 47,25 V83 C50,78 54,76 59,76 H76 C82,76 86,80 86,85 Z"/>
    <path android:fillColor="#D4AF37" android:pathData="M51,23h6v62h-6z"/>
    <path android:fillColor="#9A7AC6" android:pathData="M29,31h17v3h-17z M29,40h17v3h-17z M29,49h17v3h-17z M62,31h17v3h-17z M62,40h17v3h-17z M62,49h17v3h-17z"/>
    <path android:fillColor="#D4AF37" android:pathData="M45,88h18v4h-18z"/>
</vector>
""", encoding="utf-8")

check = gradle.read_text(encoding="utf-8")
tree = ET.parse(manifest)
app = tree.getroot().find("application")
if 'applicationId = "com.personal.diaryapp"' not in check:
    raise SystemExit("FAIL: standalone Diary applicationId not applied")
if app.get(android + "label") != "My Diary" or app.get(android + "icon") != "@drawable/my_diary_icon":
    raise SystemExit("FAIL: standalone Diary app label/custom artwork icon not applied")
if not (drawable_nodpi / "my_diary_icon.jpg").is_file():
    raise SystemExit("FAIL: original custom Diary artwork was not copied into Android resources")
print("PASS: applicationId is com.personal.diaryapp")
print("PASS: launcher label is My Diary")
print("PASS: custom original My Diary artwork is configured as launcher icon")
