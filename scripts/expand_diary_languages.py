#!/usr/bin/env python3
from pathlib import Path
import json, re, sys

html_path = Path(sys.argv[1])
source = html_path.read_text(encoding="utf-8")
translations = json.loads((Path(__file__).with_name("diary-full-translations.json")).read_text(encoding="utf-8"))
languages = ("urdu", "kannada", "bengali", "gujarati", "marathi", "tamil", "telugu")
required = set(translations["urdu"])
for lang in languages:
    if set(translations[lang]) != required:
        raise SystemExit(f"{lang}: translation keys do not match Urdu")
    if len(required) != 133 or any(not str(v).strip() for v in translations[lang].values()):
        raise SystemExit(f"{lang}: incomplete translation data")

# Preserve the existing Roman English, English and Hindi dictionaries verbatim.
insert = []
for lang in languages:
    values = json.dumps(translations[lang], ensure_ascii=False, separators=(",", ":"))
    insert.append(f" words[{json.dumps(lang)}]=Object.assign({{}},words.english,{values});")
insert.append(""" function applyDiaryTextDirection(){
  var l=language(),rtl=(l==='urdu');
  var codes={roman:'en',english:'en',hindi:'hi',urdu:'ur',kannada:'kn',bengali:'bn',gujarati:'gu',marathi:'mr',tamil:'ta',telugu:'te'};
  document.documentElement.dir=rtl?'rtl':'ltr';
  document.documentElement.lang=codes[l]||'en';
  document.body.dir=rtl?'rtl':'ltr';
 }""")
block = "\n" + "\n".join(insert) + "\n"
if 'words["urdu"]' not in source:
    if " function language(){" not in source:
        raise SystemExit("Could not locate Diary language() insertion point")
    source = source.replace(" function language(){", block + " function language(){", 1)

# Add all seven choices after the existing Hindi option.
option = '   <option value="hindi">हिन्दी</option>'
options = option + '''
   <option value="urdu">اردو</option>
   <option value="kannada">ಕನ್ನಡ</option>
   <option value="bengali">বাংলা</option>
   <option value="gujarati">ગુજરાતી</option>
   <option value="marathi">मराठी</option>
   <option value="tamil">தமிழ்</option>
   <option value="telugu">తెలుగు</option>'''
if 'value="urdu"' not in source:
    if option not in source:
        raise SystemExit("Could not locate Hindi language selector option")
    source = source.replace(option, options, 1)

# Apply language direction both at startup and whenever the selector changes.
source = source.replace(
    "setTimeout(function(){installEntry();refreshLabels()},0)",
    "setTimeout(function(){applyDiaryTextDirection();installEntry();refreshLabels()},0)"
)
source = source.replace(
    " function boot(){\n  prepareDiaryStorage();",
    " function boot(){\n  applyDiaryTextDirection();\n  prepareDiaryStorage();"
)
html_path.write_text(source, encoding="utf-8")
print("Added seven complete APK-sourced language dictionaries:", len(required), "keys each")
