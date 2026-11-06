#!/usr/bin/env python3
"""Build a clean standalone Diary HTML from the isolated notes module in the source bundle."""
from pathlib import Path
import re
import sys

if len(sys.argv) != 2:
    raise SystemExit("usage: build_standalone_diary.py <source-index.html>")

target = Path(sys.argv[1])
source = target.read_text(encoding="utf-8")

styles = []
for match in re.finditer(r"<style\b([^>]*)>(.*?)</style>", source, re.I | re.S):
    attrs, css = match.group(1), match.group(2)
    if re.search(r"muazzinMyNotes|muazzin-my-note|muazzinDiary|my-note-card|diary-", css, re.I):
        styles.append(match.group(0))

start = source.find('<script id="muazzin-my-notes-js">')
if start < 0:
    raise SystemExit("FAIL: isolated Diary/Notes module script was not found")
end = source.find("</script>", start)
if end < 0:
    raise SystemExit("FAIL: Diary module script is incomplete")
module = source[start:end + len("</script>")]

if not styles:
    raise SystemExit("FAIL: Diary styles were not found")

content = "\n".join(styles + [module])
content = content.replace("deleteForever:'Permanently Delete'", "deleteForever:'Hamesha ke liye mitaayein'")
content = content.replace("emptyTrash:'Recently Deleted mein koi note nahi hai.'", "emptyTrash:'Haal hi mein hataaye gaye notes mein koi note nahi hai.'")
content = content.replace("remove:'Delete Note'", "remove:'Note Hataayein'")
content = content.replace("category:'Category'", "category:'Kism'")
content = content.replace("allCategories:'Sab Categories'", "allCategories:'Sabhi Kismein'")
content = content.replace("forgotPin:'❓ Forgot PIN?'", "forgotPin:'❓ PIN Bhool Gaye?'")
content = content.replace("lockOff:'🔓 Lock Off'", "lockOff:'🔓 Lock Band Karein'")
content = content.replace("unlockSubmit:'Unlock'", "unlockSubmit:'Kholein'")
content = content.replace("pinPrompt:'4-digit PIN daalein'", "pinPrompt:'4 ankon ka PIN daalein'")
content = content.replace("pinUnavailable:'Is browser mein PIN lock available nahi hai.'", "pinUnavailable:'Is browser mein PIN lock ki suvidha nahi hai.'")
content = content.replace("deeni:'Deeni',work:'Work'", "deeni:'Religious',work:'Work'")
content = content.replace("kind==='cover'?'Naam ka design':'Text ka design'", "kind==='cover'?t('formatCoverHeading'):t('formatTextHeading')")
content = content.replace("'aria-label':'Font size'", "'aria-label':t('fontSizeLabel')")
content = content.replace("'aria-label':'Font family'", "'aria-label':t('fontFamilyLabel')")
content = content.replace("'aria-label':'Bold'", "'aria-label':t('boldLabel')")
content = content.replace("'aria-label':'Italic'", "'aria-label':t('italicLabel')")
content = content.replace("'aria-label':'Underline'", "'aria-label':t('underlineLabel')")
content = content.replace("'aria-label':'Text colour'", "'aria-label':t('textColourLabel')")
content = content.replace("'Delete selected ('+count+')'", "t('deleteSelected')+' ('+count+')'")
content = content.replace("'Attached diary photo'", "t('attachedPhoto')")
content = content.replace("roman:{button:'Meri Diary',", """roman:{formatCoverHeading:'Naam ka design',formatTextHeading:'Likhai ka design',fontSizeLabel:'Likhai ka size',fontFamilyLabel:'Likhai ka font',boldLabel:'Mota',italicLabel:'Tirchha',underlineLabel:'Neeche lakeer',textColourLabel:'Likhai ka rang',deleteSelected:'Chune hue hataayein',attachedPhoto:'Diary ki lagi hui photo',button:'Meri Diary',""")
content = content.replace("english:{button:'My Diary',", "english:{cancelSelection:'Cancel',formatCoverHeading:'Cover design',formatTextHeading:'Text design',fontSizeLabel:'Font size',fontFamilyLabel:'Font family',boldLabel:'Bold',italicLabel:'Italic',underlineLabel:'Underline',textColourLabel:'Text colour',deleteSelected:'Delete selected',attachedPhoto:'Attached diary photo',button:'My Diary',")
content = content.replace("hindi:{button:'मेरी डायरी',", """hindi:{formatCoverHeading:'कवर का डिज़ाइन',formatTextHeading:'लिखावट का डिज़ाइन',fontSizeLabel:'लिखावट का आकार',fontFamilyLabel:'लिखावट का फ़ॉन्ट',boldLabel:'मोटा',italicLabel:'तिरछा',underlineLabel:'रेखांकित',textColourLabel:'लिखावट का रंग',deleteSelected:'चुने हुए नोट हटाएँ',attachedPhoto:'डायरी में लगी फोटो',button:'मेरी डायरी',""")
content = content.replace("english:{button:'My Diary',", "english:{cancelSelection:'Cancel',formatCoverHeading:'Cover design',formatTextHeading:'Text design',fontSizeLabel:'Font size',fontFamilyLabel:'Font family',boldLabel:'Bold',italicLabel:'Italic',underlineLabel:'Underline',textColourLabel:'Text colour',deleteSelected:'Delete selected',attachedPhoto:'Attached diary photo',button:'My Diary',")
content = content.replace("deleteForever:'Permanently Delete'", "deleteForever:'Hamesha ke liye mitaayein'")
content = content.replace("catDeeni:'Deeni'", "catDeeni:'Religious'")
content = content.replace("cancelSelection=el('button',{type:'button',class:'diary-note-cancel-selection'},'Cancel')", "cancelSelection=el('button',{type:'button',class:'diary-note-cancel-selection'},t('cancelSelection'))")
content = content.replace("alt:'Diary photo attachment'", "alt:t('attachedPhoto')")
content = content.replace("roman:{formatCoverHeading:", "roman:{cancelSelection:'Chune se bahar',formatCoverHeading:")
content = content.replace("english:{formatCoverHeading:", "english:{cancelSelection:'Cancel',formatCoverHeading:")
content = content.replace("hindi:{formatCoverHeading:", "hindi:{cancelSelection:'चयन रद्द करें',formatCoverHeading:")
content = content.replace("diary-note-cancel-selection'},'Cancel')", "diary-note-cancel-selection'},t('cancelSelection'))")
content = content.replace("english:{formatCoverHeading:", "english:{formatCoverHeading:")
content = content.replace("remove:'Note Hataayein'", "remove:'Note Hataayein'")
content = content.replace("category:'Kism'", "category:'Category'")
content = content.replace("forgotPin:'❓ PIN Bhool Gaye?'", "forgotPin:'❓ Forgot PIN?'")
content = content.replace("lockOff:'🔓 Lock Band Karein'", "lockOff:'🔓 Turn Off Lock'")
content = content.replace("unlockSubmit:'Kholein'", "unlockSubmit:'Unlock'")
content = content.replace("categoryLabel:'Note Category'", "categoryLabel:'Note Category'")

content = content.replace("categoryLabel:'Note Category'", "categoryLabel:'Note ki Kism'")
content = content.replace("category:'Kism'", "category:'Kism'")

# Final explicit language pass: target the dictionary and control in the extracted module.
english_labels = "cancelSelection:'Cancel',formatCoverHeading:'Cover design',formatTextHeading:'Text design',fontSizeLabel:'Font size',fontFamilyLabel:'Font family',boldLabel:'Bold',italicLabel:'Italic',underlineLabel:'Underline',textColourLabel:'Text colour',deleteSelected:'Delete selected',attachedPhoto:'Attached diary photo',"
content, english_count = re.subn(r"english:\{(?=button:)", "english:{" + english_labels, content, count=1)
if english_count != 1:
    raise SystemExit("FAIL: English dictionary insertion point not found")
content = content.replace("diary-note-cancel-selection'},'Cancel');", "diary-note-cancel-selection'},t('cancelSelection'));")
if "diary-note-cancel-selection'},'Cancel');" in content:
    raise SystemExit("FAIL: Cancel-selection control was not localized")


for old, new in (
    ("MUAZZIN", "DIARY"),
    ("Muazzin", "Diary"),
    ("muazzin", "diary"),
    ("My Notes", "My Diary"),
    ("my-notes", "my-diary"),
    ("v11MoreView", "diaryHomeEntryHost"),
    ("v184LanguageSelect", "diaryLanguageSelect"),
    ("muazzin-language-change", "diary-language-change"),
    ("Diary Saheb  •  Personal Diary", "My Diary"),
    ("Diary-My-Diary-Backup.json", "My-Diary-Backup.json"),
):
    content = content.replace(old, new)

page = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="theme-color" content="#6330b8">
<title>My Diary</title>
<style>
:root{color-scheme:light;font-family:Arial,"Noto Sans",sans-serif;background:#f4efff;color:#2e2044}
*{box-sizing:border-box}
body{margin:0;min-height:100vh;background:linear-gradient(145deg,#fbf8ff,#eee4ff);padding:14px 12px 28px}
.diary-home{max-width:760px;margin:0 auto;text-align:center;padding:18px 14px 14px;border:2px solid #d4af37;border-radius:22px;background:linear-gradient(145deg,#fffdf8,#f0e8ff);box-shadow:0 4px 0 #9b7415,0 9px 20px #35204b22}
.diary-mark{font-size:48px;line-height:1.1}
.diary-home h1{margin:7px 0 4px;font-size:27px;color:#4b267c}
.diary-home p{margin:0 0 12px;color:#5e4a78;font-size:13px}
.diary-language{display:flex;justify-content:center;align-items:center;gap:8px;flex-wrap:wrap;margin:8px auto 0}
.diary-language label{font-size:12px;font-weight:800;color:#50317b}
.diary-language select{min-height:38px;border:1px solid #bda7dc;border-radius:9px;background:#fff;padding:6px 10px;font-weight:700;color:#39235b}
#diaryHomeEntryHost{display:flex;justify-content:center;max-width:760px;margin:14px auto}
#diaryMyNotesEntry{max-width:460px;width:100%;min-height:74px!important;font-size:16px!important;border:2px solid #d4af37!important;box-shadow:0 3px 0 #9b7415,0 7px 15px #39204b22!important}
</style>
</head>
<body>
<main class="diary-home">
 <div class="diary-mark">📒</div>
 <h1>My Diary</h1>
 <p>Private notes, memories and personal writing</p>
 <div class="diary-language">
  <label for="diaryLanguageSelect">Language / Zaban</label>
  <select id="diaryLanguageSelect">
   <option value="roman" selected>Roman English</option>
   <option value="english">English</option>
   <option value="hindi">हिन्दी</option>
  </select>
 </div>
</main>
<div id="diaryHomeEntryHost" aria-label="Open Diary"></div>
""" + content + """
<script>
window.addEventListener('load',function(){
 setTimeout(function(){
  var button=document.getElementById('diaryMyNotesEntry');
  if(button)button.click();
 },350);
});
</script>
</body>
</html>
"""

page = page.replace("diary-note-cancel-selection'},'Cancel')", "diary-note-cancel-selection'},t('cancelSelection'))")
if "diary-note-cancel-selection'},'Cancel')" in page:
    raise SystemExit("FAIL: final Cancel button localization failed")

for forbidden in ("muazzin", "azan", "azaan", "namaz", "quran", "masjid", "zakat", "qibla", "nearby"):
    if re.search(forbidden, page, re.I):
        raise SystemExit("FAIL: non-Diary feature marker remains: " + forbidden)

if "diaryMyNotesOverlay" not in page or "diaryMyNotesPanel" not in page:
    raise SystemExit("FAIL: Diary editor/overlay identifiers are missing")
if "diary_personal_notes_v1" not in page:
    raise SystemExit("FAIL: Diary storage namespace was not separated")

target.write_text(page, encoding="utf-8")
print("PASS: generated standalone Diary HTML")
print("PASS: retained isolated Diary editor, PIN, backup/restore, photos and note management module")
print("PASS: removed Muazzin/namaz/Quran/masjid/zakat feature code and branding")
print("Output bytes:", target.stat().st_size)
