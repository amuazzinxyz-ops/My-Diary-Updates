from pathlib import Path
import re

base=Path("diary-project/app")
kt=base/"src/main/java/com/muazzin/diary/MainActivity.kt"
s=kt.read_text(encoding="utf-8")
if "class DiaryNativeActions" in s: raise SystemExit("Already patched")
s=s.replace("import android.content.Intent\n","import android.content.Intent\nimport android.app.AlertDialog\nimport android.webkit.JavascriptInterface\nimport android.widget.Toast\nimport java.net.HttpURLConnection\nimport java.net.URL\n",1)
s=s.replace("        if (WebViewFeature.isFeatureSupported(WebViewFeature.WEB_MESSAGE_LISTENER)) {","        webView.addJavascriptInterface(DiaryNativeActions(), \"DiaryAppActions\")\n\n        if (WebViewFeature.isFeatureSupported(WebViewFeature.WEB_MESSAGE_LISTENER)) {",1)
native = r"""
    private inner class DiaryNativeActions {
        private fun metadata(): JSONObject {
            val c=URL("https://raw.githubusercontent.com/amuazzinxyz-ops/My-Diary-Updates/main/latest.json").openConnection() as HttpURLConnection
            c.connectTimeout=15000;c.readTimeout=15000
            return try { JSONObject(c.inputStream.bufferedReader().use{it.readText()}) } finally { c.disconnect() }
        }
        private fun currentVersion(): Int {
            val info=packageManager.getPackageInfo(packageName,0)
            @Suppress("DEPRECATION")
            return if(android.os.Build.VERSION.SDK_INT>=28) info.longVersionCode.toInt() else info.versionCode
        }
        @JavascriptInterface fun shareApp() {
            val share = Intent(Intent.ACTION_SEND).apply {
                type = "text/plain"
                putExtra(Intent.EXTRA_SUBJECT, "My Diary")
                putExtra(Intent.EXTRA_TEXT, "📒 My Diary app\nDownload: https://raw.githubusercontent.com/amuazzinxyz-ops/My-Diary-Updates/main/My-Diary.apk")
            }
            startActivity(Intent.createChooser(share, "Share My Diary"))
        }
        @JavascriptInterface fun checkForUpdates() {
            Thread {
                try {
                    val j=metadata()
                    if(j.optString("appName")!="My Diary" || j.optString("packageName")!=packageName) throw Exception("Wrong app")
                    val latest=j.optInt("versionCode",0)
                    if(latest<=currentVersion()) runOnUiThread { Toast.makeText(this@MainActivity,"My Diary pehle se latest hai.",Toast.LENGTH_LONG).show() }
                    else runOnUiThread { AlertDialog.Builder(this@MainActivity).setTitle("My Diary update available").setMessage("Naya version " + j.optString("versionName") + " available hai. Kya aap APK download karke install karna chahte hain?").setPositiveButton("Download & Install") { _, _ -> downloadAndInstall() }.setNegativeButton("Baad mein", null).show() }
                } catch (_:Exception) {
                    runOnUiThread { Toast.makeText(this@MainActivity,"Update check nahi ho saka. Internet check karein.",Toast.LENGTH_LONG).show() }
                }
            }.start()
        }
        @JavascriptInterface fun downloadAndInstall() {
            Thread {
                try {
                    val j=metadata()
                    if(j.optString("appName")!="My Diary" || j.optString("packageName")!=packageName) throw Exception("Wrong app")
                    if(j.optInt("versionCode",0)<=currentVersion()) throw Exception("Already latest")
                    val link=j.optString("apkUrl")
                    val expected=j.optString("sha256").lowercase()
                    if(!link.startsWith("https://raw.githubusercontent.com/amuazzinxyz-ops/My-Diary-Updates/main/") || !expected.matches(Regex("[0-9a-f]{64}"))) throw Exception("Untrusted update")
                    runOnUiThread { Toast.makeText(this@MainActivity,"APK download aur SHA-256 verification shuru...",Toast.LENGTH_LONG).show() }
                    val c=URL(link).openConnection() as HttpURLConnection
                    c.connectTimeout=20000;c.readTimeout=30000;c.instanceFollowRedirects=false
                    val apk=File(cacheDir,"my-diary-update.apk")
                    val digest=java.security.MessageDigest.getInstance("SHA-256")
                    try {
                        c.inputStream.use { input -> apk.outputStream().use { output ->
                            val buffer=ByteArray(8192)
                            while(true){val n=input.read(buffer);if(n<0)break;digest.update(buffer,0,n);output.write(buffer,0,n)}
                        }}
                    } finally { c.disconnect() }
                    val actual=digest.digest().joinToString("") { "%02x".format(it) }
                    if(actual!=expected){apk.delete();throw Exception("SHA-256 mismatch")}
                    val uri=FileProvider.getUriForFile(this@MainActivity,"$packageName.fileprovider",apk)
                    runOnUiThread {
                        val install=Intent(Intent.ACTION_VIEW).apply {
                            setDataAndType(uri,"application/vnd.android.package-archive")
                            addFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION or Intent.FLAG_ACTIVITY_NEW_TASK)
                        }
                        startActivity(install)
                    }
                } catch (_:Exception) {
                    runOnUiThread { Toast.makeText(this@MainActivity,"Download/verification nahi hua. Update abhi install nahi kiya gaya.",Toast.LENGTH_LONG).show() }
                }
            }.start()
        }
    }
"""
i=s.rfind("\n}")
if i<0: raise SystemExit("Class end missing")
s=s[:i]+native+s[i:]
kt.write_text(s,encoding="utf-8")

manifest=base/"src/main/AndroidManifest.xml"
ms=manifest.read_text(encoding="utf-8")
permission='    <uses-permission android:name="android.permission.REQUEST_INSTALL_PACKAGES" />'
if "android.permission.REQUEST_INSTALL_PACKAGES" not in ms:
    ms=ms.replace("<manifest", "<manifest", 1)
    p=ms.find(">", ms.find("<manifest"))
    if p<0: raise SystemExit("Manifest root tag missing")
    ms=ms[:p+1]+"\\n"+permission+ms[p+1:]
    manifest.write_text(ms,encoding="utf-8")

g=base/"build.gradle.kts"
t=g.read_text(encoding="utf-8")
t=re.sub(r"versionCode\s*=\s*\d+","versionCode = 90",t,count=1)
t=re.sub(r'versionName\s*=\s*"[^"]+"','versionName = "1.0.90"',t,count=1)
if "versionCode = 90" not in t: raise SystemExit("Version code patch failed")
g.write_text(t,encoding="utf-8")

m=base/"src/main/assets/index.html"
h=m.read_text(encoding="utf-8")
anchor="mePanel.appendChild(diaryPinBtn);mePanel.appendChild(lockDiaryBtn);mePanel.appendChild(unlockDiaryBtn);"
if "diaryShareAppBtn" in h or "diaryCheckUpdatesBtn" in h:
    raise SystemExit("Diary Me actions already exist; refusing duplicate insertion")
if anchor not in h:
    raise SystemExit("Diary Me menu insertion point missing")
actions = """
  var shareAppBtn=el('button',{id:'diaryShareAppBtn',type:'button'},'📤 Share App');
  var checkUpdatesBtn=el('button',{id:'diaryCheckUpdatesBtn',type:'button'},'🔄 Check for Updates');
  mePanel.appendChild(shareAppBtn);
  mePanel.appendChild(checkUpdatesBtn);
  shareAppBtn.addEventListener('click',function(e){e.preventDefault();e.stopPropagation();if(window.DiaryAppActions&&DiaryAppActions.shareApp){DiaryAppActions.shareApp();}});
  checkUpdatesBtn.addEventListener('click',function(e){e.preventDefault();e.stopPropagation();if(window.DiaryAppActions&&DiaryAppActions.checkForUpdates){DiaryAppActions.checkForUpdates();}});
"""
h=h.replace(anchor,anchor+actions,1)
style = """
<style id="diary-me-app-actions-style">
#diaryShareAppBtn,#diaryCheckUpdatesBtn{display:block!important;width:100%!important;min-height:34px!important;height:34px!important;margin:7px 0 0!important;padding:0 10px!important;box-sizing:border-box!important;border:1px solid #b9d0bd!important;border-radius:9px!important;background:linear-gradient(145deg,#fff,#e5eee8)!important;color:#123d2a!important;font-size:10px!important;font-weight:1000!important;line-height:1.15!important;text-align:left!important;white-space:nowrap!important;box-shadow:0 2px 0 #c7d9c8!important;cursor:pointer!important}
#diaryShareAppBtn:active,#diaryCheckUpdatesBtn:active{transform:translateY(2px)!important;box-shadow:0 0 0 transparent!important}
</style>
"""
if "</head>" not in h:
    raise SystemExit("HTML head closing tag missing")
h=h.replace("</head>",style+"\\n</head>",1)
if "diary-app-actions" in h or "diaryDownloadInstall" in h:
    raise SystemExit("External/floating app action controls detected; refusing build")
m.write_text(h,encoding="utf-8")
print("PASS: Share App and Check for Updates are inside Diary > Me; no external action bar.")


# Keep Android autofill/password managers from inserting a saved street or postal
# address into Diary PIN fields. Also render JS PIN prompts as numeric native dialogs.
html_path = Path("diary-project/app/src/main/assets/index.html")
html = html_path.read_text(encoding="utf-8")
pin_replacements = [
    (
        "var entered=window.prompt(t('recoveryCodePrompt'));if(entered===null)return;",
        "var entered=window.prompt(t('pinPrompt'));if(entered===null)return;"
    ),
    (
        "var pinInput=el('input',{type:'password',inputmode:'numeric',maxlength:'4',autocomplete:'off','aria-label':t('pinPrompt')});",
        "var pinInput=el('input',{type:'password',name:'diary-note-pin',inputmode:'numeric',pattern:'[0-9]*',maxlength:'4',autocomplete:'new-password',autocapitalize:'off',autocorrect:'off',spellcheck:'false','aria-autocomplete':'none','data-lpignore':'true','data-1p-ignore':'true','aria-label':t('pinPrompt')});"
    ),
    (
        "var input=el('input',{type:'password',inputmode:'numeric',maxlength:'4',autocomplete:'off'});input.placeholder=t('pinPrompt');",
        "var input=el('input',{type:'password',name:'diary-master-pin',inputmode:'numeric',pattern:'[0-9]*',maxlength:'4',autocomplete:'new-password',autocapitalize:'off',autocorrect:'off',spellcheck:'false','aria-autocomplete':'none','data-lpignore':'true','data-1p-ignore':'true'});input.placeholder=t('pinPrompt');"
    ),
]
for old, new in pin_replacements:
    count = html.count(old)
    if count != 1:
        raise SystemExit(f"Expected exactly one Diary PIN input anchor, found {count}: {old[:90]}")
    html = html.replace(old, new, 1)
close_alignment_style = """
<style id="diary-close-glyph-centering">
/* Center only the × glyph; keep the Close button's existing box and placement unchanged. */
#diaryMyNotesClose {
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    box-sizing: border-box !important;
    padding: 0 0 2px !important;
    line-height: 1 !important;
}
</style>
"""
if "diary-close-glyph-centering" in html:
    raise SystemExit("Close glyph centering patch already present; refusing duplicate")
if "</head>" not in html:
    raise SystemExit("Diary HTML head closing tag missing")
html = html.replace("</head>", close_alignment_style + "\\n</head>", 1)
html_path.write_text(html, encoding="utf-8")

kotlin_path = Path("diary-project/app/src/main/java/com/muazzin/diary/MainActivity.kt")
kotlin = kotlin_path.read_text(encoding="utf-8")
imports = [
    "import android.app.AlertDialog",
    "import android.text.InputFilter",
    "import android.text.InputType",
    "import android.text.method.DigitsKeyListener",
    "import android.view.WindowManager",
    "import android.widget.EditText",
]
for item in imports:
    if item not in kotlin:
        kotlin = kotlin.replace("import android.app.Activity", item + chr(10) + "import android.app.Activity", 1)
anchor = "        webView.webChromeClient = object : WebChromeClient() {"
native_pin_prompt = r"""
            override fun onJsPrompt(view: WebView?, url: String?, message: String?, defaultValue: String?, result: JsPromptResult?): Boolean {
                val prompt = message.orEmpty()
                val isPinPrompt = Regex("(?i)\\bPIN\\b|पिन|پن").containsMatchIn(prompt)
                if (!isPinPrompt) return super.onJsPrompt(view, url, message, defaultValue, result)

                val pinInput = EditText(this@MainActivity).apply {
                    inputType = InputType.TYPE_CLASS_NUMBER or InputType.TYPE_NUMBER_VARIATION_PASSWORD
                    keyListener = DigitsKeyListener.getInstance("0123456789")
                    filters = arrayOf(InputFilter.LengthFilter(4))
                    isSingleLine = true
                    hint = "4-digit PIN"
                    if (android.os.Build.VERSION.SDK_INT >= 26) {
                        importantForAutofill = View.IMPORTANT_FOR_AUTOFILL_NO_EXCLUDE_DESCENDANTS
                    }
                }
                val dialog = AlertDialog.Builder(this@MainActivity)
                    .setTitle(prompt)
                    .setView(pinInput)
                    .setPositiveButton("OK", null)
                    .setNegativeButton("Cancel") { _, _ -> result?.cancel() }
                    .create()
                dialog.setOnCancelListener { result?.cancel() }
                dialog.setOnShowListener {
                    dialog.window?.setSoftInputMode(WindowManager.LayoutParams.SOFT_INPUT_STATE_ALWAYS_VISIBLE)
                    pinInput.requestFocus()
                    pinInput.post {
                        val manager = getSystemService(android.content.Context.INPUT_METHOD_SERVICE) as android.view.inputmethod.InputMethodManager
                        manager.showSoftInput(pinInput, android.view.inputmethod.InputMethodManager.SHOW_IMPLICIT)
                    }
                    dialog.getButton(AlertDialog.BUTTON_POSITIVE).setOnClickListener {
                        val pinValue = pinInput.text.toString()
                        val manager = getSystemService(android.content.Context.INPUT_METHOD_SERVICE) as android.view.inputmethod.InputMethodManager
                        manager.hideSoftInputFromWindow(pinInput.windowToken, 0)
                        pinInput.clearFocus()
                        val dialogDecor = dialog.window?.decorView
                        dialog.dismiss()
                        if (dialogDecor != null) {
                            dialogDecor.postDelayed({ result?.confirm(pinValue) }, 300)
                        } else {
                            result?.confirm(pinValue)
                        }
                    }
                }
                dialog.show()
                return true
            }
"""
if "override fun onJsPrompt(" not in kotlin:
    if kotlin.count(anchor) != 1:
        raise SystemExit("Cannot safely locate the single WebChromeClient PIN prompt insertion point")
    kotlin = kotlin.replace(anchor, anchor + native_pin_prompt, 1)
kotlin_path.write_text(kotlin, encoding="utf-8")
print("PASS: Diary PIN fields disable address autofill and native PIN prompts use numeric password input.")
