#!/usr/bin/env python3
"""Apply label-sized, individually pressed 3D styling to the native My Diary widget."""
from pathlib import Path
import xml.etree.ElementTree as ET

APP = Path("diary-project/app")
LAYOUT = APP / "src/main/res/layout/diary_home_widget.xml"
BUTTON_BG = APP / "src/main/res/drawable/diary_widget_button.xml"
INFO = APP / "src/main/res/xml/diary_home_widget_info.xml"
PROVIDER = APP / "src/main/java/com/muazzin/diary/DiaryHomeWidgetProvider.kt"
ANDROID = "{http://schemas.android.com/apk/res/android}"
ET.register_namespace("android", "http://schemas.android.com/apk/res/android")

BUTTONS = {
    "widgetDiaryButtonHit": "widgetDiaryButton",
    "widgetCalendarButtonHit": "widgetCalendarButton",
    "widgetReminderButtonHit": "widgetReminderButton",
    "widgetNewNoteButtonHit": "widgetNewNoteButton",
}

if not all(path.is_file() for path in (LAYOUT, INFO, PROVIDER)):
    raise SystemExit("BLOCKED: original native Home Screen widget layout/provider files are missing")

tree = ET.parse(LAYOUT)
root = tree.getroot()
if root.get(ANDROID + "id") != "@+id/widgetRoot":
    raise SystemExit("BLOCKED: unexpected widget root; refusing to restyle an unknown layout")
root.set(ANDROID + "clickable", "false")
root.set(ANDROID + "focusable", "false")

nodes = {}
for node in root.iter():
    node_id = node.get(ANDROID + "id", "")
    if node_id.startswith("@+id/"):
        nodes[node_id.rsplit("/", 1)[1]] = node

for hit_id, label_id in BUTTONS.items():
    wrapper = nodes.get(hit_id)
    label = nodes.get(label_id)
    if wrapper is None or label is None or label not in list(wrapper):
        raise SystemExit(f"BLOCKED: expected independent widget button and label: {hit_id}/{label_id}")
    wrapper.set(ANDROID + "layout_width", "160dp")
    wrapper.set(ANDROID + "layout_height", "48dp")
    wrapper.set(ANDROID + "layout_gravity", "center_horizontal")
    wrapper.set(ANDROID + "layout_marginTop", "4dp")
    wrapper.set(ANDROID + "background", "@drawable/diary_widget_button")
    wrapper.set(ANDROID + "clickable", "true")
    wrapper.set(ANDROID + "focusable", "true")
    wrapper.set(ANDROID + "longClickable", "false")
    label.set(ANDROID + "layout_width", "match_parent")
    label.set(ANDROID + "layout_height", "match_parent")
    label.set(ANDROID + "gravity", "center")
    label.set(ANDROID + "paddingLeft", "6dp")
    label.set(ANDROID + "paddingRight", "6dp")
    label.set(ANDROID + "clickable", "false")
    label.set(ANDROID + "focusable", "false")
    label.set(ANDROID + "textStyle", "bold")

ET.indent(tree, space="    ")
tree.write(LAYOUT, encoding="utf-8", xml_declaration=True)

button_selector = '''<?xml version="1.0" encoding="utf-8"?>
<selector xmlns:android="http://schemas.android.com/apk/res/android">
    <item android:state_pressed="true">
        <shape android:shape="rectangle">
            <gradient android:startColor="#5B2A9D" android:endColor="#3F176F" android:angle="135" />
            <corners android:radius="10dp" />
            <stroke android:width="1dp" android:color="#F0C95A" />
        </shape>
    </item>
    <item>
        <layer-list>
            <item>
                <shape android:shape="rectangle">
                    <solid android:color="#3F1B69" />
                    <corners android:radius="10dp" />
                </shape>
            </item>
            <item android:bottom="3dp">
                <shape android:shape="rectangle">
                    <gradient android:startColor="#B18BEA" android:endColor="#6330B8" android:angle="135" />
                    <corners android:radius="10dp" />
                    <stroke android:width="1dp" android:color="#E5C65B" />
                </shape>
            </item>
        </layer-list>
    </item>
</selector>
'''
BUTTON_BG.write_text(button_selector, encoding="utf-8")

info = ET.parse(INFO).getroot()
if info.get(ANDROID + "minHeight") != "280dp" or info.get(ANDROID + "minWidth") != "180dp":
    raise SystemExit("BLOCKED: required 180dp x 280dp widget minimum size changed unexpectedly")
provider = PROVIDER.read_text(encoding="utf-8")
for target in ('"diary"', '"calendar"', '"reminders"', '"new-note"'):
    if target not in provider:
        raise SystemExit("BLOCKED: missing independent widget destination " + target)
if provider.count("setOnClickPendingIntent(") != 1 or "widgetId * 10 + slot" not in provider:
    raise SystemExit("BLOCKED: independent per-button PendingIntent routing changed")

check = ET.parse(LAYOUT).getroot()
check_nodes = {n.get(ANDROID + "id", "").rsplit("/", 1)[-1]: n for n in check.iter() if n.get(ANDROID + "id", "").startswith("@+id/")}
for hit_id, label_id in BUTTONS.items():
    wrapper, label = check_nodes.get(hit_id), check_nodes.get(label_id)
    if wrapper is None or label is None or wrapper.get(ANDROID + "layout_width") != "160dp":
        raise SystemExit("FAIL: equal-width button layout not applied: " + hit_id)
    if wrapper.get(ANDROID + "layout_height") != "48dp" or wrapper.get(ANDROID + "layout_gravity") != "center_horizontal":
        raise SystemExit("FAIL: button hit area/centering changed: " + hit_id)
    if label.get(ANDROID + "layout_width") != "match_parent" or label.get(ANDROID + "clickable") != "false":
        raise SystemExit("FAIL: button label must fill its equal-width wrapper and remain non-clickable: " + label_id)
if check.get(ANDROID + "clickable") != "false" or check.get(ANDROID + "focusable") != "false":
    raise SystemExit("FAIL: widget container must remain non-clickable/non-focusable")
selector = ET.parse(BUTTON_BG).getroot()
if selector.tag != "selector" or not any(item.get(ANDROID + "state_pressed") == "true" for item in selector.findall("item")):
    raise SystemExit("FAIL: per-button pressed selector is missing")
if 'android:bottom="3dp"' not in BUTTON_BG.read_text(encoding="utf-8"):
    raise SystemExit("FAIL: raised 3D button shadow layer is missing")
for header_id in ("widgetTitle", "widgetDate"):
    header = check_nodes.get(header_id)
    if header is None or header.get(ANDROID + "gravity") != "center":
        raise SystemExit("FAIL: Diary title and date must be centered above the buttons: " + header_id)
if any(check_nodes[x].get(ANDROID + "layout_width") != "160dp" for x in BUTTONS):
    raise SystemExit("FAIL: all four buttons must have the same Personal Calendar-sized width")
print("PASS: four equal 160dp x 48dp buttons, centered Diary title/date, compact 180dp x 280dp widget, raised 3D face, isolated pressed state, and independent tap routing.")
