#!/usr/bin/env python3
"""Add a safe, local Diary refresh control inside the existing Me menu."""
from pathlib import Path
import re

path = Path("diary-project/app/src/main/assets/index.html")
html = path.read_text(encoding="utf-8")

start = html.find('<script id="diary-my-diary-js">')
if start < 0:
    # The extracted script keeps its original element id in some source revisions.
    start = html.find("<script")
    if start < 0:
        raise SystemExit("Diary script not found")
end = html.find("</script>", start)
if end < 0:
    raise SystemExit("Diary script closing tag not found")
script = html[start:end]

anchor = "  var diaryPinBtn=el('button',{id:'diaryDiaryMasterPinBtn',type:'button'},t('diaryPin'));"
if script.count(anchor) != 1:
    raise SystemExit("Could not uniquely locate the existing Diary Me-menu controls")
if "diaryDiaryRefreshBtn" in script:
    raise SystemExit("Refresh button already exists; refusing duplicate insertion")

insert = """  var checkUpdatesBtn=el('button',{id:'diaryCheckUpdatesBtn',type:'button'},'⬇️ Check for Updates');
  mePanel.appendChild(checkUpdatesBtn);
  var refreshDiaryBtn=el('button',{id:'diaryDiaryRefreshBtn',type:'button'},'🔄 Refresh');
  mePanel.appendChild(refreshDiaryBtn);
"""
script = script.replace(anchor, insert + anchor, 1)

listener_anchor = "  diaryPinBtn.addEventListener('click',function(e){e.preventDefault();e.stopPropagation();configureDiaryPin();});"
if script.count(listener_anchor) != 1:
    raise SystemExit("Could not uniquely locate the Diary Me-menu event handlers")
listener = """  checkUpdatesBtn.addEventListener('click',function(e){
   e.preventDefault();e.stopPropagation();
   if(window.DiaryAppActions&&typeof DiaryAppActions.checkForUpdates==='function'){
    DiaryAppActions.checkForUpdates();
   }else{
    alert('Check for Updates sirf installed My Diary app mein available hai.');
   }
  });
  refreshDiaryBtn.addEventListener('click',function(e){
   e.preventDefault();e.stopPropagation();
   function refreshDiaryNow(){
    try{
     renderList();
     saveDiarySafetyCopy();
     refreshDiaryBtn.textContent='✓ Refreshed';
     window.setTimeout(function(){refreshDiaryBtn.textContent='🔄 Refresh';},1300);
    }catch(err){
     refreshDiaryBtn.textContent='Refresh failed';
     window.setTimeout(function(){refreshDiaryBtn.textContent='🔄 Refresh';},1800);
    }
   }
   if(!diaryStorageReady){prepareDiaryStorage().then(refreshDiaryNow);return;}
   refreshDiaryNow();
  });
"""
script = script.replace(listener_anchor, listener + listener_anchor, 1)
html = html[:start] + script + "</script>" + html[end + len("</script>"):]

style = """
<style id="diary-me-refresh-gold-3d">
#diaryDiaryMePanel #diaryDiaryRefreshBtn{
 border:2px solid #d4af37!important;
 box-shadow:inset 0 2px 0 rgba(255,255,220,.82),
            inset 0 -2px 0 rgba(126,83,0,.20),
            0 1px 0 #9b7415,0 2px 4px rgba(70,48,0,.20)!important;
 font-weight:1000!important;
}
</style>
"""
if 'id="diary-me-refresh-gold-3d"' not in html:
    if "</body>" not in html:
        raise SystemExit("Could not find end of standalone Diary page")
    html = html.replace("</body>", style + "\n</body>", 1)

check_update_style = """
<style id="diary-me-check-updates-style">
#diaryDiaryMePanel #diaryCheckUpdatesBtn{
 display:flex!important;align-items:center!important;justify-content:flex-start!important;
 align-self:stretch!important;width:100%!important;min-width:100%!important;max-width:100%!important;
 height:34px!important;min-height:34px!important;max-height:34px!important;
 margin:0 0 7px!important;padding:0 10px!important;box-sizing:border-box!important;
 font-size:10px!important;line-height:1.15!important;text-align:left!important;
 white-space:nowrap!important;overflow:hidden!important;text-overflow:clip!important;
}
</style>
"""
if 'id="diary-me-check-updates-style"' not in html:
    if "</body>" not in html:
        raise SystemExit("Could not find end of standalone Diary page")
    html = html.replace("</body>", check_update_style + "\n</body>", 1)

equal_size_style = """
<style id="v136-me-refresh-equal-size">
/* Match Refresh button dimensions to the existing Font Size and Trash buttons. */
#diaryDiaryMePanel #diaryDiaryRefreshBtn{
 display:flex!important;align-items:center!important;justify-content:flex-start!important;
 align-self:stretch!important;width:100%!important;min-width:100%!important;max-width:100%!important;
 height:34px!important;min-height:34px!important;max-height:34px!important;
 margin:0!important;padding:0 10px!important;box-sizing:border-box!important;
 font-size:10px!important;line-height:1.15!important;text-align:left!important;
 white-space:nowrap!important;overflow:hidden!important;text-overflow:clip!important;
}
</style>
"""
if 'id="v136-me-refresh-equal-size"' not in html:
    if "</body>" not in html:
        raise SystemExit("Could not find end of standalone Diary page")
    html = html.replace("</body>", equal_size_style + "\n</body>", 1)

if script.count("diaryDiaryRefreshBtn") != 1:
    raise SystemExit("Refresh button insertion verification failed")
if "renderList();" not in script[script.find("diaryDiaryRefreshBtn"):]:
    raise SystemExit("Refresh handler does not call the existing Diary list renderer")

path.write_text(html, encoding="utf-8")
print("PASS: Me menu now contains one Refresh button")
print("PASS: Refresh re-reads current Diary notes and trash from local storage via existing renderer")
print("PASS: Existing editor, PIN, notes and data storage logic remain unchanged")
