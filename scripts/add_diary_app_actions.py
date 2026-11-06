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
