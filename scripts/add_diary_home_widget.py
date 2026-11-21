#!/usr/bin/env python3
"""Add the configurable native My Diary Home Screen widget and Me settings."""
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path("diary-project")
APP = ROOT / "app"
HTML_PATH = APP / "src/main/assets/index.html"
KOTLIN_PATH = APP / "src/main/java/com/muazzin/diary/MainActivity.kt"
MANIFEST_PATH = APP / "src/main/AndroidManifest.xml"

def require_once(source: str, anchor: str, replacement: str, label: str) -> str:
    count = source.count(anchor)
    if count == 0 and replacement in source:
        return source
    if count != 1:
        raise SystemExit(f"BLOCKED: expected one safe insertion point for {label}; found {count}")
    return source.replace(anchor, replacement, 1)

# 1) Add a real Widget Settings screen inside the existing Me menu.
html = HTML_PATH.read_text(encoding="utf-8")
share_anchor = "  shareAppBtn.addEventListener('click',function(e){e.preventDefault();e.stopPropagation();if(window.DiaryAppActions&&DiaryAppActions.shareApp){DiaryAppActions.shareApp();}});"
widget_ui = r"""
  var widgetSettingsBtn=el('button',{id:'diaryHomeWidgetSettingsBtn',type:'button',class:'diary-me-feature-btn'},'🏠 Home Screen Widget Settings');
  mePanel.appendChild(widgetSettingsBtn);
  var widgetSettingsModal=el('section',{id:'diaryHomeWidgetSettingsModal',hidden:'hidden','aria-modal':'true','role':'dialog'});
  var widgetSettingsHead=el('div',{class:'diary-home-widget-head'});
  var widgetSettingsTitle=el('strong',{},'🏠 Home Screen Widget Settings');
  var widgetSettingsClose=el('button',{type:'button',class:'diary-home-widget-close'},'✕');
  widgetSettingsHead.append(widgetSettingsTitle,widgetSettingsClose);
  var widgetSettingsHint=el('p',{},'Widget ka actual size Home Screen par long-press karke resize karein. Yahan text size aur dikhne wale shortcuts chunein.');
  var widgetSettingsOptions=el('div',{class:'diary-home-widget-options'});
  function makeWidgetOption(id,label,checked){
   var row=el('label',{class:'diary-home-widget-option'});
   var input=el('input',{id:id,type:'checkbox'});input.checked=checked;
   row.append(input,document.createTextNode(label));widgetSettingsOptions.appendChild(row);return input;
  }
  var widgetShowDate=makeWidgetOption('diaryWidgetShowDate','📅 Aaj ki Tareekh dikhayein',true);
  var widgetShowDiary=makeWidgetOption('diaryWidgetShowDiary','📒 My Diary kholen',true);
  var widgetShowCalendar=makeWidgetOption('diaryWidgetShowCalendar','📅 Personal Calendar kholen',true);
  var widgetShowReminder=makeWidgetOption('diaryWidgetShowReminder','⏰ Smart Reminder kholen',true);
  var widgetShowKharcha=makeWidgetOption('diaryWidgetShowKharcha','💰 My Kharcha kholen',false);
  var widgetShowDocuments=makeWidgetOption('diaryWidgetShowDocuments','📁 My Documents kholen',false);
  var widgetShowMemories=makeWidgetOption('diaryWidgetShowMemories','📒 My Memories kholen',false);
  var widgetShowPrivateLocker=makeWidgetOption('diaryWidgetShowPrivateLocker','🔐 Private Locker kholen',false);
  var widgetShowFavouriteNotes=makeWidgetOption('diaryWidgetShowFavouriteNotes','⭐ Favourite Notes kholen',false);
  var widgetShowWorldClock=makeWidgetOption('diaryWidgetShowWorldClock','🌍 World Clock kholen',false);
  var widgetShowSmartSearch=makeWidgetOption('diaryWidgetShowSmartSearch','🔍 Smart Search kholen',false);
  var widgetSizeLabel=el('label',{class:'diary-home-widget-size-label'},'Widget Text Size');
  var widgetSize=el('select',{id:'diaryWidgetSize'});
  [['compact','Chhota'],['standard','Normal'],['large','Bada']].forEach(function(item){widgetSize.appendChild(el('option',{value:item[0]},item[1]));});
  widgetSettingsOptions.append(widgetSizeLabel,widgetSize);
  var widgetSettingsStatus=el('p',{class:'diary-home-widget-status','aria-live':'polite'},'');
  var widgetSettingsSave=el('button',{type:'button',class:'diary-home-widget-action'},'💾 Settings Save Karein');
  var widgetSettingsPin=el('button',{type:'button',class:'diary-home-widget-action diary-home-widget-pin'},'➕ Home Screen par Lagayein');
  widgetSettingsModal.append(widgetSettingsHead,widgetSettingsHint,widgetSettingsOptions,widgetSettingsSave,widgetSettingsPin,widgetSettingsStatus);
  ov.appendChild(widgetSettingsModal);
  function widgetSettingsValue(){
   return {showDate:!!widgetShowDate.checked,showDiary:!!widgetShowDiary.checked,showCalendar:!!widgetShowCalendar.checked,showReminder:!!widgetShowReminder.checked,showKharcha:!!widgetShowKharcha.checked,showDocuments:!!widgetShowDocuments.checked,showMemories:!!widgetShowMemories.checked,showPrivateLocker:!!widgetShowPrivateLocker.checked,showFavouriteNotes:!!widgetShowFavouriteNotes.checked,showWorldClock:!!widgetShowWorldClock.checked,showSmartSearch:!!widgetShowSmartSearch.checked,size:String(widgetSize.value||'standard')};
  }
  function widgetApplySettings(value){
   value=value||{};
   widgetShowDate.checked=value.showDate!==false;
   widgetShowDiary.checked=value.showDiary!==false;
   widgetShowCalendar.checked=value.showCalendar!==false;
   widgetShowReminder.checked=value.showReminder!==false;
   widgetShowKharcha.checked=!!value.showKharcha;
   widgetShowDocuments.checked=!!value.showDocuments;
   widgetShowMemories.checked=!!value.showMemories;
   widgetShowPrivateLocker.checked=!!value.showPrivateLocker;
   widgetShowFavouriteNotes.checked=!!value.showFavouriteNotes;
   widgetShowWorldClock.checked=!!value.showWorldClock;
   widgetShowSmartSearch.checked=!!value.showSmartSearch;
   widgetSize.value=['compact','standard','large'].indexOf(value.size)>=0?value.size:'standard';
  }
  function widgetSaveSettings(showMessage){
   if(!window.DiaryAppActions||typeof DiaryAppActions.saveHomeWidgetSettings!=='function'){
    widgetSettingsStatus.textContent='Widget Settings ke liye My Diary ka installed Android app kholein.';return false;
   }
   var value=widgetSettingsValue();
   if(!value.showDiary&&!value.showCalendar&&!value.showReminder&&!value.showKharcha&&!value.showDocuments&&!value.showMemories&&!value.showPrivateLocker&&!value.showFavouriteNotes&&!value.showWorldClock&&!value.showSmartSearch){widgetSettingsStatus.textContent='Kam se kam ek shortcut select karein.';return false;}
   try{
    var saved=DiaryAppActions.saveHomeWidgetSettings(JSON.stringify(value));
    widgetSettingsStatus.textContent=saved?'Widget Settings save ho gayi.':'Settings save nahi ho sakin.';
    return !!saved;
   }catch(error){widgetSettingsStatus.textContent='Settings save nahi ho sakin.';return false;}
  }
  function widgetOpenSettings(){
   if(window.DiaryAppActions&&typeof DiaryAppActions.getHomeWidgetSettings==='function'){
    try{widgetApplySettings(JSON.parse(DiaryAppActions.getHomeWidgetSettings()||'{}'));}catch(error){widgetApplySettings({});}
   }else{widgetApplySettings({});}
   widgetSettingsStatus.textContent='';
   widgetSettingsModal.hidden=false;
  }
  widgetSettingsBtn.addEventListener('click',function(e){e.preventDefault();e.stopPropagation();widgetOpenSettings();});
  widgetSettingsClose.addEventListener('click',function(){widgetSettingsModal.hidden=true;});
  widgetSettingsSave.addEventListener('click',function(){widgetSaveSettings(true);});
  widgetSettingsPin.addEventListener('click',function(){
   if(!widgetSaveSettings(false))return;
   if(!window.DiaryAppActions||typeof DiaryAppActions.requestHomeWidgetPin!=='function'){
    widgetSettingsStatus.textContent='Home Screen Widget ke liye installed Android app zaroori hai.';return;
   }
   try{
    var requested=DiaryAppActions.requestHomeWidgetPin();
    widgetSettingsStatus.textContent=requested?'Android ka Add Widget prompt khul gaya.':'Is Android version/launcher mein direct Add supported nahi. Home Screen par long-press karke Widgets mein My Diary chunein.';
   }catch(error){widgetSettingsStatus.textContent='Widget add nahi ho saka. Home Screen par long-press karke Widgets mein My Diary chunein.';}
  });
"""
if "diaryHomeWidgetSettingsBtn" not in html:
    html = require_once(html, share_anchor, share_anchor + "\n" + widget_ui, "Me > Widget Settings button")
elif "widgetSettingsPin.addEventListener" not in html:
    raise SystemExit("BLOCKED: partial Widget Settings UI found; refusing duplicate insertion")

feature_anchor = "  function openMeFeature(kind){if(meFeatureProtected(kind)&&meFeaturePinConfig(kind)){showMeFeaturePin(kind);return;}showMeFeaturePage(kind);}"
widget_target = r"""
  window.__diaryOpenWidgetTarget=function(target){
   if(['calendar','reminders','kharcha','documents','memories'].indexOf(target)>=0){openMeFeature(target);return;}
   if(target==='private-locker'){privateLockerOpen();return;}
   if(target==='world-clock'){worldClockBtn.click();return;}
   if(target==='favourite-notes'&&typeof window.__diaryShowFavouriteNotesFromWidget==='function'){window.__diaryShowFavouriteNotesFromWidget();return;}
   if(target==='smart-search'){var search=document.getElementById('diaryMyNotesSearch');if(search){search.value='';search.focus();}return;}
   if(target==='quick-note'||target==='new-note'){var note=document.getElementById('diaryMyNotesText');if(note){note.focus();}return;}
  };
"""
if "window.__diaryOpenWidgetTarget=function(target)" not in html:
    html = require_once(html, feature_anchor, feature_anchor + "\n" + widget_target, "native widget destination handler")

overlay_anchor = r""" function openOverlay(){
  if(!diaryStorageReady){prepareDiaryStorage().then(function(){openOverlay()});return;}
  var masterPin=localStorage.getItem(DIARY_MASTER_PIN_KEY)||'';
  if(masterPin){showDiaryUnlock();return;}
  openDiaryPanel();
 }
 function openDiaryPanel(){"""
widget_launcher = r"""
 window.__diaryOpenWidgetTargetFromAndroid=function(target){
  try{
   if(localStorage.getItem(DIARY_MASTER_PIN_KEY)){openOverlay();return;}
   openOverlay();
   if(['calendar','reminders','kharcha','documents','memories','private-locker','favourite-notes','world-clock','smart-search','quick-note','new-note'].indexOf(target)>=0){
    var tries=0;
    (function waitForDiaryOverlay(){
     if(typeof window.__diaryOpenWidgetTarget==='function'){window.__diaryOpenWidgetTarget(target);return;}
     if(tries++<20)window.setTimeout(waitForDiaryOverlay,200);
    })();
   }
  }catch(error){try{openOverlay();}catch(ignore){}}
 };
"""
if "window.__diaryOpenWidgetTargetFromAndroid=function(target)" not in html:
    if overlay_anchor not in html:
        raise SystemExit("BLOCKED: page-level openOverlay widget insertion point missing")
    html = html.replace(overlay_anchor, overlay_anchor.replace(" function openDiaryPanel(){", widget_launcher + " function openDiaryPanel(){"), 1)

widget_style = r"""
<style id="diary-home-widget-settings-style">
#diaryHomeWidgetSettingsBtn{display:flex!important;align-items:center!important;justify-content:flex-start!important;width:100%!important;min-height:40px!important;margin:7px 0 0!important;padding:7px 10px!important;box-sizing:border-box!important;border:2px solid #d4af37!important;border-radius:10px!important;background:linear-gradient(145deg,#c4a2ff,#6330b8)!important;color:#fff!important;font-size:14px!important;font-weight:1000!important;text-align:left!important;box-shadow:inset 0 2px 0 #ffffff88,0 3px 0 #54258f,0 6px 10px #3a19694a!important}
#diaryHomeWidgetSettingsModal{position:fixed!important;inset:0!important;z-index:100020!important;display:flex!important;flex-direction:column!important;gap:12px!important;overflow:auto!important;box-sizing:border-box!important;padding:calc(18px + env(safe-area-inset-top,0px)) 14px calc(24px + env(safe-area-inset-bottom,0px))!important;background:linear-gradient(145deg,#fffdf8,#eee4ff)!important;color:#2e2044!important}
#diaryHomeWidgetSettingsModal[hidden]{display:none!important}
.diary-home-widget-head{display:flex;align-items:center;justify-content:space-between;gap:10px;padding:10px;border:2px solid #d4af37;border-radius:14px;background:linear-gradient(145deg,#fff,#f2eaff);box-shadow:0 3px 0 #9b7415}
.diary-home-widget-head strong{font-size:18px;font-weight:1000;color:#4b267c}
.diary-home-widget-close{width:38px;min-width:38px;height:38px;border:1px solid #b99bdc;border-radius:10px;background:linear-gradient(145deg,#fff,#eadbff);color:#4b267c;font-size:22px;font-weight:1000}
#diaryHomeWidgetSettingsModal p{margin:0;font-size:14px;line-height:1.5;font-weight:800}
.diary-home-widget-options{display:flex;flex-direction:column;gap:9px;padding:12px;border:2px solid #b99bdc;border-radius:14px;background:#fff;box-shadow:0 3px 0 #8e68b8}
.diary-home-widget-option{display:flex;align-items:center;gap:10px;min-height:42px;padding:7px 9px;border:1px solid #d5c3eb;border-radius:9px;background:#f8f3ff;font-size:15px;font-weight:900}
.diary-home-widget-option input{width:22px;height:22px;accent-color:#6330b8;flex:0 0 auto}
.diary-home-widget-size-label{font-size:15px;font-weight:1000;color:#43256b}
#diaryWidgetSize{width:100%;min-height:42px;border:1px solid #b99bdc;border-radius:9px;padding:7px 10px;background:#fff;color:#2e2044;font-size:15px;font-weight:900}
.diary-home-widget-action{width:100%;min-height:46px;border:2px solid #d4af37;border-radius:11px;background:linear-gradient(145deg,#c4a2ff,#6330b8);color:#fff;font-size:15px;font-weight:1000;box-shadow:inset 0 2px 0 #ffffff77,0 3px 0 #54258f,0 6px 10px #3a196933}
.diary-home-widget-pin{background:linear-gradient(145deg,#fff1b9,#d4a72e);color:#382700}
.diary-home-widget-status{min-height:24px;padding:8px;border-radius:9px;background:#fff;font-size:14px!important;font-weight:900!important;color:#43256b}
</style>
"""
if "diary-home-widget-settings-style" not in html:
    if html.count("</head>") != 1:
        raise SystemExit("BLOCKED: expected one HTML head closing tag for Widget Settings styling")
    html = html.replace("</head>", widget_style + "\n</head>", 1)
HTML_PATH.write_text(html, encoding="utf-8")
print("PASS: Me > Widget Settings UI, selectable shortcuts/size, and native widget launch routing added.")

# 2) Add native bridge methods to the existing DiaryNativeActions class.
kotlin = KOTLIN_PATH.read_text(encoding="utf-8")
bridge_anchor = "        @JavascriptInterface fun shareApp() {"
bridge_methods = r"""
        @JavascriptInterface fun getHomeWidgetSettings(): String {
            val prefs = getSharedPreferences("diary_home_widget_prefs", Context.MODE_PRIVATE)
            return JSONObject()
                .put("showDate", prefs.getBoolean("showDate", true))
                .put("showDiary", prefs.getBoolean("showDiary", true))
                .put("showCalendar", prefs.getBoolean("showCalendar", true))
                .put("showReminder", prefs.getBoolean("showReminder", true))
                .put("showKharcha", prefs.getBoolean("showKharcha", false))
                .put("showDocuments", prefs.getBoolean("showDocuments", false))
                .put("showMemories", prefs.getBoolean("showMemories", false))
                .put("showPrivateLocker", prefs.getBoolean("showPrivateLocker", false))
                .put("showFavouriteNotes", prefs.getBoolean("showFavouriteNotes", false))
                .put("showWorldClock", prefs.getBoolean("showWorldClock", false))
                .put("showSmartSearch", prefs.getBoolean("showSmartSearch", false))
                .put("size", prefs.getString("size", "standard"))
                .toString()
        }

        @JavascriptInterface fun saveHomeWidgetSettings(json: String): Boolean {
            return try {
                val value = JSONObject(json)
                val prefs = getSharedPreferences("diary_home_widget_prefs", Context.MODE_PRIVATE)
                prefs.edit()
                    .putBoolean("showDate", value.optBoolean("showDate", true))
                    .putBoolean("showDiary", value.optBoolean("showDiary", true))
                    .putBoolean("showCalendar", value.optBoolean("showCalendar", true))
                    .putBoolean("showReminder", value.optBoolean("showReminder", true))
                    .putBoolean("showKharcha", value.optBoolean("showKharcha", false))
                    .putBoolean("showDocuments", value.optBoolean("showDocuments", false))
                    .putBoolean("showMemories", value.optBoolean("showMemories", false))
                    .putBoolean("showPrivateLocker", value.optBoolean("showPrivateLocker", false))
                    .putBoolean("showFavouriteNotes", value.optBoolean("showFavouriteNotes", false))
                    .putBoolean("showWorldClock", value.optBoolean("showWorldClock", false))
                    .putBoolean("showSmartSearch", value.optBoolean("showSmartSearch", false))
                    .putString("size", value.optString("size", "standard").takeIf { it in setOf("compact", "standard", "large") } ?: "standard")
                    .apply()
                runOnUiThread { DiaryHomeWidgetProvider.updateAll(this@MainActivity) }
                true
            } catch (error: Exception) {
                android.util.Log.e("MyDiaryWidget", "Widget settings save failed", error)
                false
            }
        }

        @JavascriptInterface fun requestHomeWidgetPin(): Boolean {
            if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
                val manager = android.appwidget.AppWidgetManager.getInstance(this@MainActivity)
                if (manager.isRequestPinAppWidgetSupported) {
                    return manager.requestPinAppWidget(
                        android.content.ComponentName(this@MainActivity, DiaryHomeWidgetProvider::class.java),
                        null,
                        null
                    )
                }
            }
            runOnUiThread {
                Toast.makeText(this@MainActivity, "Home Screen par long-press karein, Widgets kholein aur My Diary chunein.", Toast.LENGTH_LONG).show()
            }
            return false
        }
"""
if "getHomeWidgetSettings()" not in kotlin:
    kotlin = require_once(kotlin, bridge_anchor, bridge_methods + "\n" + bridge_anchor, "native Widget Settings bridge")
elif "requestHomeWidgetPin()" not in kotlin:
    raise SystemExit("BLOCKED: incomplete native Widget Settings bridge found")
# Route a widget tap to the already-open WebView without creating another Diary activity.
field_anchor = "    private lateinit var webView: WebView\n"
if "private var pendingWidgetTarget: String?" not in kotlin:
    kotlin = require_once(kotlin, field_anchor, field_anchor + "    private var pendingWidgetTarget: String? = null\n", "pending Home Screen widget target")
create_anchor = "    override fun onCreate(savedInstanceState: Bundle?) {\n        super.onCreate(savedInstanceState)\n"
if "pendingWidgetTarget = intent?.getStringExtra(\"diary_widget_target\")" not in kotlin:
    kotlin = require_once(kotlin, create_anchor, create_anchor + "        pendingWidgetTarget = intent?.getStringExtra(\"diary_widget_target\")\n", "initial widget launch target")
page_anchor = "                super.onPageFinished(view, url)\n"
page_replacement = page_anchor + "                if (url.startsWith(\"https://appassets.androidplatform.net/assets/index.html\")) consumePendingWidgetTarget()\n"
if "consumePendingWidgetTarget()" not in kotlin:
    kotlin = require_once(kotlin, page_anchor, page_replacement, "WebView widget launch dispatch")
on_save_anchor = "    override fun onSaveInstanceState(outState: Bundle) {\n"
widget_activity_methods = r"""
    private fun consumePendingWidgetTarget() {
        val target = pendingWidgetTarget ?: return
        if (!::webView.isInitialized) return
        webView.evaluateJavascript("(typeof window.__diaryOpenWidgetTargetFromAndroid === 'function')") { ready ->
            if (ready == "true" && pendingWidgetTarget == target) {
                pendingWidgetTarget = null
                webView.evaluateJavascript("window.__diaryOpenWidgetTargetFromAndroid(" + JSONObject.quote(target) + ");", null)
            }
        }
    }

    override fun onNewIntent(intent: Intent) {
        super.onNewIntent(intent)
        setIntent(intent)
        pendingWidgetTarget = intent.getStringExtra("diary_widget_target")
        if (pendingWidgetTarget != null && ::webView.isInitialized) {
            webView.post { consumePendingWidgetTarget() }
        }
    }

"""
if "override fun onNewIntent(intent: Intent)" not in kotlin:
    kotlin = require_once(kotlin, on_save_anchor, widget_activity_methods + on_save_anchor, "singleTop widget activity routing")
load_anchor = '        if (savedInstanceState != null) webView.restoreState(savedInstanceState)\n        else webView.loadUrl("https://appassets.androidplatform.net/assets/index.html")'
load_replacement = '        if (savedInstanceState != null && pendingWidgetTarget == null) webView.restoreState(savedInstanceState)\n        else webView.loadUrl("https://appassets.androidplatform.net/assets/index.html" + if (pendingWidgetTarget != null) "?diary_widget_launch=1" else "")'
kotlin = require_once(kotlin, load_anchor, load_replacement, "cold widget launch marker URL")
KOTLIN_PATH.write_text(kotlin, encoding="utf-8")
print("PASS: Android WebView bridge saves settings and routes widget taps into the existing app.")

# 3) Create the native AppWidgetProvider and its RemoteViews resources.
provider_path = APP / "src/main/java/com/muazzin/diary/DiaryHomeWidgetProvider.kt"
provider_source = r'''package com.muazzin.diary

import android.app.PendingIntent
import android.appwidget.AppWidgetManager
import android.appwidget.AppWidgetProvider
import android.content.ComponentName
import android.content.Context
import android.content.Intent
import android.net.Uri
import android.widget.RemoteViews
import android.view.View
import android.util.TypedValue
import java.text.SimpleDateFormat
import java.util.Date
import java.util.Locale

class DiaryHomeWidgetProvider : AppWidgetProvider() {
    override fun onUpdate(context: Context, manager: AppWidgetManager, appWidgetIds: IntArray) {
        appWidgetIds.forEach { updateWidget(context, manager, it) }
    }

    override fun onAppWidgetOptionsChanged(context: Context, manager: AppWidgetManager, appWidgetId: Int, newOptions: android.os.Bundle) {
        updateWidget(context, manager, appWidgetId)
    }

    companion object {
        private const val PREFS = "diary_home_widget_prefs"

        fun updateAll(context: Context) {
            val manager = AppWidgetManager.getInstance(context)
            val component = ComponentName(context, DiaryHomeWidgetProvider::class.java)
            val ids = manager.getAppWidgetIds(component)
            if (ids.isNotEmpty()) ids.forEach { updateWidget(context, manager, it) }
        }

        private fun updateWidget(context: Context, manager: AppWidgetManager, widgetId: Int) {
            val prefs = context.getSharedPreferences(PREFS, Context.MODE_PRIVATE)
            val views = RemoteViews(context.packageName, R.layout.diary_home_widget)
            val options = manager.getAppWidgetOptions(widgetId)
            val availableWidth = options.getInt(AppWidgetManager.OPTION_APPWIDGET_MIN_WIDTH, 180)
            val availableHeight = options.getInt(AppWidgetManager.OPTION_APPWIDGET_MIN_HEIGHT, 280)
            val showDate = prefs.getBoolean("showDate", true) && availableHeight >= 280
            val shortcuts = listOf(
                Triple(R.id.widgetDiaryButtonHit, R.id.widgetDiaryButton, prefs.getBoolean("showDiary", true) to "diary"),
                Triple(R.id.widgetCalendarButtonHit, R.id.widgetCalendarButton, prefs.getBoolean("showCalendar", true) to "calendar"),
                Triple(R.id.widgetReminderButtonHit, R.id.widgetReminderButton, prefs.getBoolean("showReminder", true) to "reminders"),
                Triple(R.id.widgetKharchaButtonHit, R.id.widgetKharchaButton, prefs.getBoolean("showKharcha", false) to "kharcha"),
                Triple(R.id.widgetDocumentsButtonHit, R.id.widgetDocumentsButton, prefs.getBoolean("showDocuments", false) to "documents"),
                Triple(R.id.widgetMemoriesButtonHit, R.id.widgetMemoriesButton, prefs.getBoolean("showMemories", false) to "memories"),
                Triple(R.id.widgetPrivateLockerButtonHit, R.id.widgetPrivateLockerButton, prefs.getBoolean("showPrivateLocker", false) to "private-locker"),
                Triple(R.id.widgetFavouriteNotesButtonHit, R.id.widgetFavouriteNotesButton, prefs.getBoolean("showFavouriteNotes", false) to "favourite-notes"),
                Triple(R.id.widgetWorldClockButtonHit, R.id.widgetWorldClockButton, prefs.getBoolean("showWorldClock", false) to "world-clock"),
                Triple(R.id.widgetSmartSearchButtonHit, R.id.widgetSmartSearchButton, prefs.getBoolean("showSmartSearch", false) to "smart-search"),
            )
            val anyShortcutSelected = shortcuts.any { it.third.first }

            views.setTextViewText(R.id.widgetDate, SimpleDateFormat("EEE, dd MMM yyyy", Locale.getDefault()).format(Date()))
            views.setViewVisibility(R.id.widgetDate, if (showDate) View.VISIBLE else View.GONE)

            val size = prefs.getString("size", "standard") ?: "standard"
            val titleSize = when (size) { "compact" -> 15f; "large" -> 21f; else -> 18f }
            val bodySize = when (size) { "compact" -> 12f; "large" -> 17f; else -> 14f }
            // Keep the user's selected text size at every widget width; only outer padding adapts.
            val responsiveBodySize = bodySize
            views.setTextViewTextSize(R.id.widgetTitle, TypedValue.COMPLEX_UNIT_SP, titleSize)
            views.setTextViewTextSize(R.id.widgetDate, TypedValue.COMPLEX_UNIT_SP, responsiveBodySize)
            shortcuts.forEachIndexed { index, shortcut ->
                val (hitId, labelId, setting) = shortcut
                val visible = setting.first || (index == 0 && !anyShortcutSelected)
                views.setViewVisibility(hitId, if (visible) View.VISIBLE else View.GONE)
                views.setTextViewTextSize(labelId, TypedValue.COMPLEX_UNIT_SP, responsiveBodySize)
                setTarget(context, views, widgetId, hitId, index + 1, setting.second)
            }
            val density = context.resources.displayMetrics.density
            val horizontalPadding = (if (availableWidth < 180) 6 * density else 10 * density).toInt()
            val verticalPadding = (if (availableHeight < 280) 6 * density else 10 * density).toInt()
            views.setViewPadding(R.id.widgetRoot, horizontalPadding, verticalPadding, horizontalPadding, verticalPadding)

            manager.updateAppWidget(widgetId, views)
        }

        private fun setTarget(context: Context, views: RemoteViews, widgetId: Int, viewId: Int, slot: Int, target: String) {
            val intent = Intent(context, MainActivity::class.java).apply {
                action = "${context.packageName}.HOME_WIDGET_TARGET.$target"
                data = Uri.parse("mydiary-widget://$widgetId/$slot/$target")
                putExtra("diary_widget_target", target)
                putExtra("diary_widget_slot", slot)
                addFlags(Intent.FLAG_ACTIVITY_NEW_TASK or Intent.FLAG_ACTIVITY_CLEAR_TOP or Intent.FLAG_ACTIVITY_SINGLE_TOP)
            }
            val flags = PendingIntent.FLAG_UPDATE_CURRENT or PendingIntent.FLAG_IMMUTABLE
            val pending = PendingIntent.getActivity(context, widgetId * 10 + slot, intent, flags)
            views.setOnClickPendingIntent(viewId, pending)
        }
    }
}
'''
if not provider_path.exists():
    provider_path.write_text(provider_source, encoding="utf-8")
elif "class DiaryHomeWidgetProvider" not in provider_path.read_text(encoding="utf-8"):
    raise SystemExit("BLOCKED: existing DiaryHomeWidgetProvider file has unexpected content")

res = APP / "src/main/res"
(res / "layout").mkdir(parents=True, exist_ok=True)
(res / "drawable").mkdir(parents=True, exist_ok=True)
(res / "xml").mkdir(parents=True, exist_ok=True)
# Keep the visible widget panel compact: wrap only the selected shortcut rows.
layout = r'''<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:id="@+id/widgetRoot"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:orientation="vertical"
    android:clickable="false"
    android:focusable="false"
    android:padding="10dp"
    android:background="@drawable/diary_widget_bg">
    <TextView
        android:id="@+id/widgetTitle"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="📒 My Diary"
        android:textColor="#45236F"
        android:textStyle="bold"
        android:textSize="18sp"
        android:gravity="center"
        android:paddingBottom="3dp" />
    <TextView
        android:id="@+id/widgetDate"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="Today"
        android:textColor="#5B4B6E"
        android:textSize="14sp"
        android:gravity="center"
        android:paddingBottom="7dp" />'''
widget_button_specs = [
    ("Diary", "📒 My Diary"),
    ("Calendar", "📅 Personal Calendar"),
    ("Reminder", "⏰ Smart Reminder"),
    ("Kharcha", "💰 My Kharcha"),
    ("Documents", "📁 My Documents"),
    ("Memories", "📒 My Memories"),
    ("PrivateLocker", "🔐 Private Locker"),
    ("FavouriteNotes", "⭐ Favourite Notes"),
    ("WorldClock", "🌍 World Clock"),
    ("SmartSearch", "🔍 Smart Search"),
]
button_rows = "\n".join(
    f'''    <FrameLayout
        android:id="@+id/widget{key}ButtonHit"
        android:layout_width="match_parent"
        android:layout_height="48dp"
        android:layout_marginTop="4dp"
        android:clickable="true"
        android:focusable="true"
        android:longClickable="false"
        android:background="@drawable/diary_widget_button">
        <TextView
            android:id="@+id/widget{key}Button"
            android:layout_width="match_parent"
            android:layout_height="match_parent"
            android:gravity="center"
            android:text="{label}"
            android:textColor="#FFFFFF"
            android:textStyle="bold"
            android:clickable="false"
            android:focusable="false" />
    </FrameLayout>''' for key, label in widget_button_specs
)
layout = layout + "\n" + button_rows + "\n</LinearLayout>\n"
layout_path = res / "layout/diary_home_widget.xml"
layout_path.write_text(layout, encoding="utf-8")
bg = r'''<?xml version="1.0" encoding="utf-8"?>
<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="rectangle">
    <gradient android:startColor="#FFFDF8" android:endColor="#EEE4FF" android:angle="135" />
    <corners android:radius="18dp" />
    <stroke android:width="2dp" android:color="#D4AF37" />
</shape>
'''
(res / "drawable/diary_widget_bg.xml").write_text(bg, encoding="utf-8")
button_bg = r'''<?xml version="1.0" encoding="utf-8"?>
<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="rectangle">
    <gradient android:startColor="#A77BE0" android:endColor="#6330B8" android:angle="135" />
    <corners android:radius="9dp" />
    <stroke android:width="1dp" android:color="#D4AF37" />
</shape>
'''
(res / "drawable/diary_widget_button.xml").write_text(button_bg, encoding="utf-8")
# Fit the centered header and ten selectable 48dp shortcuts with minimal outer padding.
widget_info = r'''<?xml version="1.0" encoding="utf-8"?>
<appwidget-provider xmlns:android="http://schemas.android.com/apk/res/android"
    android:minWidth="180dp"
    android:minHeight="280dp"
    android:minResizeWidth="150dp"
    android:minResizeHeight="260dp"
    android:updatePeriodMillis="1800000"
    android:initialLayout="@layout/diary_home_widget"
    android:resizeMode="horizontal|vertical"
    android:widgetCategory="home_screen"
    android:label="My Diary" />
'''
(res / "xml/diary_home_widget_info.xml").write_text(widget_info, encoding="utf-8")

# 4) Register the real Android home-screen widget without changing existing receivers/providers.
ANDROID_NS = "{http://schemas.android.com/apk/res/android}"
ET.register_namespace("android", "http://schemas.android.com/apk/res/android")
tree = ET.parse(MANIFEST_PATH)
root = tree.getroot()
app = root.find("application")
if app is None: raise SystemExit("BLOCKED: Android application manifest element missing")
main = next((node for node in app.findall("activity") if node.get(ANDROID_NS + "name") == ".MainActivity"), None)
if main is None: raise SystemExit("BLOCKED: MainActivity manifest declaration missing")
main.set(ANDROID_NS + "launchMode", "singleTop")
receiver = next((node for node in app.findall("receiver") if node.get(ANDROID_NS + "name") == ".DiaryHomeWidgetProvider"), None)
if receiver is None:
    receiver = ET.SubElement(app, "receiver")
    receiver.set(ANDROID_NS + "name", ".DiaryHomeWidgetProvider")
    receiver.set(ANDROID_NS + "exported", "true")
    intent_filter = ET.SubElement(receiver, "intent-filter")
    action = ET.SubElement(intent_filter, "action")
    action.set(ANDROID_NS + "name", "android.appwidget.action.APPWIDGET_UPDATE")
    metadata = ET.SubElement(receiver, "meta-data")
    metadata.set(ANDROID_NS + "name", "android.appwidget.provider")
    metadata.set(ANDROID_NS + "resource", "@xml/diary_home_widget_info")
else:
    metadata = next((node for node in receiver.findall("meta-data") if node.get(ANDROID_NS + "name") == "android.appwidget.provider"), None)
    if metadata is None:
        metadata = ET.SubElement(receiver, "meta-data")
        metadata.set(ANDROID_NS + "name", "android.appwidget.provider")
    metadata.set(ANDROID_NS + "resource", "@xml/diary_home_widget_info")
ET.indent(tree, space="    ")
tree.write(MANIFEST_PATH, encoding="utf-8", xml_declaration=True)

# Fail closed on missing widget wiring, manifest metadata, and the existing Diary bridge.
manifest_check = ET.parse(MANIFEST_PATH).getroot()
app_check = manifest_check.find("application")
widget_receivers = [node for node in app_check.findall("receiver") if node.get(ANDROID_NS + "name") == ".DiaryHomeWidgetProvider"]
if len(widget_receivers) != 1: raise SystemExit("FAIL: expected exactly one My Diary home-widget receiver")
if not any(node.get(ANDROID_NS + "resource") == "@xml/diary_home_widget_info" for node in widget_receivers[0].findall("meta-data")):
    raise SystemExit("FAIL: My Diary widget provider metadata missing")
if not (res / "layout/diary_home_widget.xml").is_file() or not provider_path.is_file():
    raise SystemExit("FAIL: My Diary widget layout/provider source missing")
if 'android:layout_height="wrap_content"' not in layout.split('android:id="@+id/widgetRoot"',1)[1].split('>',1)[0]:
    raise SystemExit("FAIL: widget visible content must wrap its selected buttons, not fill unused height")
if ('android:minHeight="280dp"' not in widget_info or 'android:minResizeWidth="150dp"' not in widget_info
        or 'android:minResizeHeight="260dp"' not in widget_info or 'android:resizeMode="horizontal|vertical"' not in widget_info):
    raise SystemExit("FAIL: two-axis widget resize dimensions are incomplete")
if "getHomeWidgetSettings()" not in KOTLIN_PATH.read_text(encoding="utf-8") or "window.__diaryOpenWidgetTargetFromAndroid=function(target)" not in HTML_PATH.read_text(encoding="utf-8"):
    raise SystemExit("FAIL: My Diary widget settings bridge or destination handler missing")
widget_html_check = HTML_PATH.read_text(encoding="utf-8")
for required in (
    "function diaryFinishPendingWidgetTarget()",
    "window.__diaryPendingWidgetTarget=(['calendar','reminders','kharcha','documents','memories','private-locker','favourite-notes','world-clock','smart-search','quick-note','diary','new-note'].indexOf(target)>=0)?target:null;",
    "if(typeof window.__diaryOpenWidgetTarget==='function')window.__diaryOpenWidgetTarget(target);",
):
    if required not in widget_html_check:
        raise SystemExit("FAIL: widget shortcut destination preservation missing: " + required)
if widget_html_check.count("diaryFinishPendingWidgetTarget();") != 5:
    raise SystemExit("FAIL: widget destination must resume after app open, PIN, Pattern, and Fingerprint unlock")
if ('android:minHeight="280dp"' not in widget_info or 'android:minResizeWidth="150dp"' not in widget_info
        or 'android:minResizeHeight="260dp"' not in widget_info or 'android:resizeMode="horizontal|vertical"' not in widget_info):
    raise SystemExit("FAIL: two-axis widget resize dimensions are incomplete")
for target in ('"diary"', '"calendar"', '"reminders"', '"new-note"', '"kharcha"', '"documents"', '"memories"', '"private-locker"', '"favourite-notes"', '"world-clock"', '"smart-search"', '"quick-note"'):
    if target not in provider_path.read_text(encoding="utf-8"):
        raise SystemExit("FAIL: missing native widget shortcut target " + target)
print("PASS: native AppWidgetProvider, manifest receiver, RemoteViews layout, selectable options, and tap destinations verified.")
