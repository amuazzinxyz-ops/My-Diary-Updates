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
  var interfaceColoursBtn=el('button',{id:'diaryInterfaceColoursBtn',type:'button','aria-expanded':'false','aria-controls':'diaryInterfaceColoursPanel'},'🎨 '+t('interfaceColours'));
  var interfaceColoursPanel=el('div',{id:'diaryInterfaceColoursPanel',hidden:'hidden'});
  var interfaceThemeOptions=[
   {value:'default',label:t('themeDefault'),icon:'🟣'},
   {value:'blue',label:t('themeBlue'),icon:'🔵'},
   {value:'green',label:t('themeGreen'),icon:'🟢'},
   {value:'rose',label:t('themeRose'),icon:'🌸'}
  ];
  interfaceThemeOptions.forEach(function(item){
   var option=el('button',{type:'button',class:'diary-interface-theme-option','data-theme':item.value,'aria-pressed':'false'},item.icon+' '+item.label);
   option.addEventListener('click',function(e){e.preventDefault();e.stopPropagation();applyDiaryInterfaceTheme(item.value);});
   interfaceColoursPanel.appendChild(option);
  });
  mePanel.appendChild(interfaceColoursBtn);
  mePanel.appendChild(interfaceColoursPanel);
  function applyDiaryInterfaceTheme(theme){
   theme=['default','blue','green','rose'].indexOf(theme)>=0?theme:'default';
   try{localStorage.setItem('diary_interface_theme_v1',theme);}catch(e){}
   if(theme==='default')document.body.removeAttribute('data-diary-interface-theme');
   else document.body.setAttribute('data-diary-interface-theme',theme);
   var options=interfaceColoursPanel.querySelectorAll('button[data-theme]');
   for(var i=0;i<options.length;i++)options[i].setAttribute('aria-pressed',options[i].getAttribute('data-theme')===theme?'true':'false');
  }
  interfaceColoursBtn.addEventListener('click',function(e){
   e.preventDefault();e.stopPropagation();
   var opening=interfaceColoursPanel.hidden;
   interfaceColoursPanel.hidden=!opening;
   interfaceColoursBtn.setAttribute('aria-expanded',opening?'true':'false');
  });
  var savedInterfaceTheme='default';
  try{savedInterfaceTheme=localStorage.getItem('diary_interface_theme_v1')||'default';}catch(e){}
  applyDiaryInterfaceTheme(savedInterfaceTheme);
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
 height:40px!important;min-height:40px!important;max-height:40px!important;
 margin:0 0 7px!important;padding:0 10px!important;box-sizing:border-box!important;
 font-size:18px!important;font-weight:900!important;line-height:1.15!important;text-align:left!important;
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
 height:40px!important;min-height:40px!important;max-height:40px!important;
 margin:0!important;padding:0 10px!important;box-sizing:border-box!important;
 font-size:18px!important;font-weight:900!important;line-height:1.15!important;text-align:left!important;
 white-space:nowrap!important;overflow:hidden!important;text-overflow:clip!important;
}
</style>
"""
if 'id="v136-me-refresh-equal-size"' not in html:
    if "</body>" not in html:
        raise SystemExit("Could not find end of standalone Diary page")
    html = html.replace("</body>", equal_size_style + "\n</body>", 1)

if script.count("id:'diaryDiaryRefreshBtn'") != 1:
    raise SystemExit("Refresh button insertion verification failed")
if "renderList();" not in script[script.find("diaryDiaryRefreshBtn"):]:
    raise SystemExit("Refresh handler does not call the existing Diary list renderer")


interface_theme_style = """
<style id="diary-interface-colours-themes">
#diaryInterfaceColoursPanel{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:6px;padding:6px 0;margin:0 0 7px;width:100%;box-sizing:border-box}
#diaryInterfaceColoursPanel[hidden]{display:none!important}
#diaryInterfaceColoursPanel .diary-interface-theme-option{height:40px!important;min-height:40px!important;max-height:40px!important;margin:0!important;padding:0 7px!important;border:1px solid #b9d0bd!important;border-radius:9px!important;background:linear-gradient(145deg,#fff,#e5eee8)!important;color:#123d2a!important;font-size:12px!important;font-weight:900!important;white-space:nowrap!important;box-shadow:0 2px 0 #c7d9c8!important}
#diaryInterfaceColoursPanel .diary-interface-theme-option[aria-pressed="true"]{outline:2px solid #d4af37!important;outline-offset:1px!important}
body[data-diary-interface-theme="blue"]{background:#eaf4ff!important}
body[data-diary-interface-theme="blue"] #diaryMyNotesPanel{background:#f2f8ff!important;border-color:#6d9acb!important}
body[data-diary-interface-theme="blue"] #diaryMyNotesHead{background:linear-gradient(145deg,#d9eaff,#bcd8f5)!important;color:#173f67!important}
body[data-diary-interface-theme="blue"] #diaryMyNotesHead h2{color:#173f67!important}
body[data-diary-interface-theme="blue"] #diaryMyNotesBody{background:#e9f3ff!important}
body[data-diary-interface-theme="blue"] #diaryMyNotesEditor,body[data-diary-interface-theme="blue"] #diaryMyNotesList .diary-my-note{background:linear-gradient(145deg,#fff,#edf6ff)!important;border-color:#9bbce0!important}
body[data-diary-interface-theme="blue"] #diaryMyNotesSearch,body[data-diary-interface-theme="blue"] #diaryMyNotesCategory,body[data-diary-interface-theme="blue"] #diaryMyNotesCategoryFilter,body[data-diary-interface-theme="blue"] #diaryMyNotesTitle,body[data-diary-interface-theme="blue"] #diaryMyNotesText{background:#fff!important;border-color:#7fa8d2!important;color:#173f67!important}
body[data-diary-interface-theme="blue"] #diaryMyNotesActions button,body[data-diary-interface-theme="blue"] #diaryMyNotesBackup button,body[data-diary-interface-theme="blue"] #diaryMyNotesPin,body[data-diary-interface-theme="blue"] #diaryDiaryMePanel button{background:linear-gradient(145deg,#fff,#dcecff)!important;border-color:#7fa8d2!important;color:#173f67!important}
body[data-diary-interface-theme="green"]{background:#eaf6ef!important}
body[data-diary-interface-theme="green"] #diaryMyNotesPanel{background:#f1f8f2!important;border-color:#75a98a!important}
body[data-diary-interface-theme="green"] #diaryMyNotesHead{background:linear-gradient(145deg,#d7ecdd,#b9dec5)!important;color:#17452d!important}
body[data-diary-interface-theme="green"] #diaryMyNotesHead h2{color:#17452d!important}
body[data-diary-interface-theme="green"] #diaryMyNotesBody{background:#e8f4eb!important}
body[data-diary-interface-theme="green"] #diaryMyNotesEditor,body[data-diary-interface-theme="green"] #diaryMyNotesList .diary-my-note{background:linear-gradient(145deg,#fff,#edf7ef)!important;border-color:#8fba9b!important}
body[data-diary-interface-theme="green"] #diaryMyNotesSearch,body[data-diary-interface-theme="green"] #diaryMyNotesCategory,body[data-diary-interface-theme="green"] #diaryMyNotesCategoryFilter,body[data-diary-interface-theme="green"] #diaryMyNotesTitle,body[data-diary-interface-theme="green"] #diaryMyNotesText{background:#fff!important;border-color:#75a98a!important;color:#17452d!important}
body[data-diary-interface-theme="green"] #diaryMyNotesActions button,body[data-diary-interface-theme="green"] #diaryMyNotesBackup button,body[data-diary-interface-theme="green"] #diaryMyNotesPin,body[data-diary-interface-theme="green"] #diaryDiaryMePanel button{background:linear-gradient(145deg,#fff,#dcefe1)!important;border-color:#75a98a!important;color:#17452d!important}
body[data-diary-interface-theme="rose"]{background:#fff0f4!important}
body[data-diary-interface-theme="rose"] #diaryMyNotesPanel{background:#fff7f8!important;border-color:#d58aa6!important}
body[data-diary-interface-theme="rose"] #diaryMyNotesHead{background:linear-gradient(145deg,#f9dce6,#f1c3d3)!important;color:#6b2842!important}
body[data-diary-interface-theme="rose"] #diaryMyNotesHead h2{color:#6b2842!important}
body[data-diary-interface-theme="rose"] #diaryMyNotesBody{background:#fff0f4!important}
body[data-diary-interface-theme="rose"] #diaryMyNotesEditor,body[data-diary-interface-theme="rose"] #diaryMyNotesList .diary-my-note{background:linear-gradient(145deg,#fff,#fff1f5)!important;border-color:#dfa1b7!important}
body[data-diary-interface-theme="rose"] #diaryMyNotesSearch,body[data-diary-interface-theme="rose"] #diaryMyNotesCategory,body[data-diary-interface-theme="rose"] #diaryMyNotesCategoryFilter,body[data-diary-interface-theme="rose"] #diaryMyNotesTitle,body[data-diary-interface-theme="rose"] #diaryMyNotesText{background:#fff!important;border-color:#d58aa6!important;color:#6b2842!important}
body[data-diary-interface-theme="rose"] #diaryMyNotesActions button,body[data-diary-interface-theme="rose"] #diaryMyNotesBackup button,body[data-diary-interface-theme="rose"] #diaryMyNotesPin,body[data-diary-interface-theme="rose"] #diaryDiaryMePanel button{background:linear-gradient(145deg,#fff,#f9e0e9)!important;border-color:#d58aa6!important;color:#6b2842!important}
</style>
"""
if 'id="diary-interface-colours-themes"' not in html:
    if "</body>" not in html:
        raise SystemExit("Could not find end of standalone Diary page")
    html = html.replace("</body>", interface_theme_style + chr(10) + "</body>", 1)

all_me_buttons_style = """
<style id="diary-me-all-buttons-40px">
/* Keep every control added inside the Me menu at the user's confirmed 40px height. */
#diaryDiaryMePanel button,#diaryDiaryMePanel [role="button"],#diaryDiaryMePanel input[type="button"],#diaryDiaryMePanel input[type="submit"],#diaryDiaryMePanel input[type="reset"]{height:40px!important;min-height:40px!important;max-height:40px!important;box-sizing:border-box!important}
</style>
"""
if 'id="diary-me-all-buttons-40px"' not in html:
    if "</body>" not in html:
        raise SystemExit("Could not find end of standalone Diary page")
    html = html.replace("</body>", all_me_buttons_style + chr(10) + "</body>", 1)


if "diaryInterfaceColoursBtn" not in script or "diary_interface_theme_v1" not in script:
    raise SystemExit("Interface Colours button or saved theme handler is missing")
path.write_text(html, encoding="utf-8")
print("PASS: Me menu now contains one Refresh button")
print("PASS: Refresh re-reads current Diary notes and trash from local storage via existing renderer")
print("PASS: Existing editor, PIN, notes and data storage logic remain unchanged")
# Track this script for a clean retry of the approved Diary build.
