from pathlib import Path
import re
import xml.etree.ElementTree as ET

base=Path("diary-project/app")
kt=base/"src/main/java/com/muazzin/diary/MainActivity.kt"
s=kt.read_text(encoding="utf-8")
if "class DiaryNativeActions" in s: raise SystemExit("Already patched")
s=s.replace("import android.content.Intent\n","import android.content.Intent\nimport android.app.AlertDialog\nimport android.webkit.JavascriptInterface\nimport android.widget.Toast\nimport java.net.HttpURLConnection\nimport java.net.URL\n",1)
s=s.replace("        if (WebViewFeature.isFeatureSupported(WebViewFeature.WEB_MESSAGE_LISTENER)) {","        webView.addJavascriptInterface(DiaryNativeActions(), \"DiaryAppActions\")\n\n        if (WebViewFeature.isFeatureSupported(WebViewFeature.WEB_MESSAGE_LISTENER)) {",1)
native = r"""
    private inner class DiaryNativeActions {
        private fun metadata(): JSONObject {
            val metadataUrl=URL("https://raw.githubusercontent.com/amuazzinxyz-ops/My-Diary-Updates/main/latest.json?cacheBust="+System.currentTimeMillis())
            val c=metadataUrl.openConnection() as HttpURLConnection
            c.connectTimeout=20000;c.readTimeout=20000;c.useCaches=false
            c.setRequestProperty("Cache-Control","no-cache, no-store, max-age=0")
            c.setRequestProperty("Pragma","no-cache")
            return try {
                val response=c.responseCode
                if(response !in 200..299) throw java.io.IOException("Update feed HTTP $response")
                JSONObject(c.inputStream.bufferedReader().use{it.readText()})
            } finally { c.disconnect() }
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
                    val targetVersion=j.optInt("versionCode",0)
                    if(targetVersion<=currentVersion()) throw Exception("Already latest")
                    val link=j.optString("apkUrl")
                    val expected=j.optString("sha256").lowercase()
                    if(!link.startsWith("https://raw.githubusercontent.com/amuazzinxyz-ops/My-Diary-Updates/main/") || !expected.matches(Regex("[0-9a-f]{64}"))) throw Exception("Untrusted update")
                    runOnUiThread { Toast.makeText(this@MainActivity,"APK download aur SHA-256 verification shuru...",Toast.LENGTH_LONG).show() }
                    val updateDir=File(cacheDir,"diary-share")
                    if(!updateDir.exists() && !updateDir.mkdirs()) throw Exception("Cannot create update folder")
                    val apk=File(updateDir,"my-diary-update.apk")
                    val part=File(updateDir,"my-diary-update.apk.part")
                    var downloaded=false
                    var lastFailure:Exception?=null
                    for(attempt in 1..3) {
                        part.delete()
                        try {
                            val cacheBustedLink=link+(if(link.contains("?")) "&" else "?")+"cacheBust="+System.currentTimeMillis()+"-"+attempt
                            val c=URL(cacheBustedLink).openConnection() as HttpURLConnection
                            c.connectTimeout=30000
                            c.readTimeout=60000
                            c.useCaches=false
                            c.instanceFollowRedirects=true
                            c.setRequestProperty("Cache-Control","no-cache, no-store, max-age=0")
                            c.setRequestProperty("Pragma","no-cache")
                            c.setRequestProperty("User-Agent","MyDiaryUpdater/1.1")
                            c.setRequestProperty("Accept-Encoding","identity")
                            c.setRequestProperty("Accept","application/vnd.android.package-archive, application/octet-stream")
                            val digest=java.security.MessageDigest.getInstance("SHA-256")
                            try {
                                val response=c.responseCode
                                if(response !in 200..299) throw java.io.IOException("HTTP $response")
                                val finalUrl=c.url
                                if(finalUrl.protocol!="https" || !(finalUrl.host=="raw.githubusercontent.com" || finalUrl.host=="githubusercontent.com" || finalUrl.host.endsWith(".githubusercontent.com"))) throw Exception("Untrusted download redirect")
                                var received=0L
                                c.inputStream.use { input -> part.outputStream().use { output ->
                                    val buffer=ByteArray(16384)
                                    while(true) {
                                        val n=input.read(buffer)
                                        if(n<0) break
                                        digest.update(buffer,0,n)
                                        output.write(buffer,0,n)
                                        received+=n
                                    }
                                    output.flush()
                                }}
                                if(received<=0L) throw java.io.IOException("Empty download")
                            } finally { c.disconnect() }
                            val actual=digest.digest().joinToString("") { "%02x".format(it) }
                            if(actual!=expected) throw Exception("SHA-256 mismatch")
                            if(apk.exists() && !apk.delete()) throw Exception("Cannot replace old APK")
                            if(!part.renameTo(apk)) throw Exception("Cannot finalize downloaded APK")
                            val archive=packageManager.getPackageArchiveInfo(apk.absolutePath,0) ?: throw Exception("Downloaded file is not a valid APK")
                            if(archive.packageName!=packageName) throw Exception("APK package mismatch")
                            @Suppress("DEPRECATION")
                            val archiveVersion=if(android.os.Build.VERSION.SDK_INT>=28) archive.longVersionCode.toInt() else archive.versionCode
                            if(archiveVersion!=targetVersion || archiveVersion<=currentVersion()) throw Exception("APK version mismatch")
                            downloaded=true
                            break
                        } catch(e:Exception) {
                            lastFailure=e
                            part.delete()
                            if(attempt<3) Thread.sleep(1200L*attempt)
                        }
                    }
                    if(!downloaded) throw Exception("3 download attempts failed: " + (lastFailure?.message ?: "unknown error"))
                    val uri=FileProvider.getUriForFile(this@MainActivity,"$packageName.fileprovider",apk)
                    runOnUiThread {
                        if(android.os.Build.VERSION.SDK_INT>=26 && !packageManager.canRequestPackageInstalls()) {
                            Toast.makeText(this@MainActivity,"APK verify ho gaya. Install permission allow karke Update dobara dabayein.",Toast.LENGTH_LONG).show()
                            startActivity(Intent(android.provider.Settings.ACTION_MANAGE_UNKNOWN_APP_SOURCES,android.net.Uri.parse("package:$packageName")))
                        } else {
                            val install=Intent(Intent.ACTION_VIEW).apply {
                                setDataAndType(uri,"application/vnd.android.package-archive")
                                addFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION or Intent.FLAG_ACTIVITY_NEW_TASK)
                            }
                            startActivity(install)
                        }
                    }
                } catch(e:Exception) {
                    val reason=e.message?.take(180) ?: e.javaClass.simpleName
                    runOnUiThread {
                        AlertDialog.Builder(this@MainActivity)
                            .setTitle("My Diary update nahi ho saka")
                            .setMessage("Download/verification fail hua. Wajah: $reason\n\nAapka purana Diary data safe hai. Internet check karke dobara koshish karein.")
                            .setPositiveButton("Theek hai", null)
                            .show()
                    }
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

# Keep the app's ORIGINAL FileProvider resource. Diary sharing already writes to
# cacheDir/diary-share; the APK updater writes to that same directory. Reusing
# the existing XML avoids a second authority/resource mapping that can fail
# at runtime with "Failed to find configured root that contains...".
android_ns = "http://schemas.android.com/apk/res/android"
ET.register_namespace("android", android_ns)
tree = ET.parse(manifest)
root = tree.getroot()
app = root.find("application")
if app is None:
    raise SystemExit("AndroidManifest application element missing")
authority = "${applicationId}.fileprovider"
providers = app.findall("provider")
provider = next((node for node in providers if node.get("{" + android_ns + "}name") == "androidx.core.content.FileProvider"), None)
if provider is None:
    raise SystemExit("Original FileProvider missing; refusing to replace app sharing configuration")
provider.set("{" + android_ns + "}authorities", authority)
provider.set("{" + android_ns + "}exported", "false")
provider.set("{" + android_ns + "}grantUriPermissions", "true")
metadata = [node for node in provider.findall("meta-data")
            if node.get("{" + android_ns + "}name") == "android.support.FILE_PROVIDER_PATHS"]
if len(metadata) != 1:
    raise SystemExit("Expected the original single FileProvider paths metadata")
if metadata[0].get("{" + android_ns + "}resource") != "@xml/file_paths":
    raise SystemExit("Original FileProvider paths resource changed unexpectedly")
xml_dir = base / "src/main/res/xml"
paths_file = xml_dir / "file_paths.xml"
if not paths_file.is_file():
    raise SystemExit("Original FileProvider file_paths.xml is missing")
paths_tree = ET.parse(paths_file)
paths_root = paths_tree.getroot()
cache_path = next((node for node in list(paths_root)
                   if node.tag == "cache-path"
                   and node.get("name") == "diary_shared_files"), None)
if cache_path is None:
    cache_path = ET.SubElement(paths_root, "cache-path")
    cache_path.set("name", "diary_shared_files")
cache_path.set("path", "diary-share/")
ET.indent(paths_tree, space="    ")
paths_tree.write(paths_file, encoding="utf-8", xml_declaration=True)
ET.indent(tree, space="    ")
tree.write(manifest, encoding="utf-8", xml_declaration=True)
# Validate the exact original resource and directory used by both share and updater.
check_tree = ET.parse(manifest)
check_app = check_tree.getroot().find("application")
matching = [node for node in check_app.findall("provider")
            if node.get("{" + android_ns + "}authorities") == authority
            and node.get("{" + android_ns + "}name") == "androidx.core.content.FileProvider"]
if len(matching) != 1:
    raise SystemExit("FAIL: expected exactly one Diary FileProvider with the app authority")
check_meta = [node for node in matching[0].findall("meta-data")
              if node.get("{" + android_ns + "}name") == "android.support.FILE_PROVIDER_PATHS"]
if len(check_meta) != 1 or check_meta[0].get("{" + android_ns + "}resource") != "@xml/file_paths":
    raise SystemExit("FAIL: original FileProvider paths metadata was not preserved")
check_paths = ET.parse(paths_file).getroot()
if not any(node.tag == "cache-path"
           and node.get("name") == "diary_shared_files"
           and node.get("path") == "diary-share/" for node in list(check_paths)):
    raise SystemExit("FAIL: original FileProvider cache path does not match cacheDir/diary-share")
print("PASS: original FileProvider resource, authority, and shared updater cache directory verified.")

g=base/"build.gradle.kts"
t=g.read_text(encoding="utf-8")
t=re.sub(r"versionCode\s*=\s*\d+","versionCode = 97",t,count=1)
t=re.sub(r'versionName\s*=\s*"[^"]+"','versionName = "1.0.97"',t,count=1)
if "versionCode = 97" not in t: raise SystemExit("Version code patch failed")
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
  mePanel.appendChild(shareAppBtn);
  shareAppBtn.addEventListener('click',function(e){e.preventDefault();e.stopPropagation();if(window.DiaryAppActions&&DiaryAppActions.shareApp){DiaryAppActions.shareApp();}});
"""
h=h.replace(anchor,anchor+actions,1)
style = """
<style id="diary-me-app-actions-style">
#diaryShareAppBtn{display:block!important;width:100%!important;min-height:34px!important;height:34px!important;margin:7px 0 0!important;padding:0 10px!important;box-sizing:border-box!important;border:1px solid #b9d0bd!important;border-radius:9px!important;background:linear-gradient(145deg,#fff,#e5eee8)!important;color:#123d2a!important;font-size:10px!important;font-weight:1000!important;line-height:1.15!important;text-align:left!important;white-space:nowrap!important;box-shadow:0 2px 0 #c7d9c8!important;cursor:pointer!important}
#diaryShareAppBtn:active{transform:translateY(2px)!important;box-shadow:0 0 0 transparent!important}
</style>
"""
if "</head>" not in h:
    raise SystemExit("HTML head closing tag missing")
h=h.replace("</head>",style+"\n</head>",1)
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
html = html.replace("</head>", close_alignment_style + "\n</head>", 1)
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
                        dialog.dismiss()
                        android.os.Handler(android.os.Looper.getMainLooper()).postDelayed({ result?.confirm(pinValue) }, 300)
                    }
                }
                dialog.show()
                return true
            }
"""
# Lock Off confirmation must use a native dialog; do not show the WebView page URL.
native_confirm_prompt = r"""
            override fun onJsConfirm(view: WebView?, url: String?, message: String?, result: JsResult?): Boolean {
                val dialog = AlertDialog.Builder(this@MainActivity)
                    .setTitle("My Diary")
                    .setMessage(message.orEmpty())
                    .setPositiveButton("Yes") { _, _ -> result?.confirm() }
                    .setNegativeButton("No") { _, _ -> result?.cancel() }
                    .create()
                dialog.setOnCancelListener { result?.cancel() }
                dialog.show()
                return true
            }
"""
if "override fun onJsConfirm(" not in kotlin:
    if kotlin.count(anchor) != 1:
        raise SystemExit("Cannot safely locate the single WebChromeClient confirmation insertion point")
    kotlin = kotlin.replace(anchor, anchor + native_confirm_prompt, 1)
if "override fun onJsPrompt(" not in kotlin:
    if kotlin.count(anchor) != 1:
        raise SystemExit("Cannot safely locate the single WebChromeClient PIN prompt insertion point")
    kotlin = kotlin.replace(anchor, anchor + native_pin_prompt, 1)
kotlin_path.write_text(kotlin, encoding="utf-8")
print("PASS: Diary PIN fields disable address autofill and native PIN prompts use numeric password input.")
