from pathlib import Path
import re

base=Path("diary-project/app")
kt=base/"src/main/java/com/muazzin/diary/MainActivity.kt"
s=kt.read_text(encoding="utf-8")
if "class DiaryNativeActions" in s: raise SystemExit("Already patched")
s=s.replace("import android.content.Intent\n","import android.content.Intent\nimport android.webkit.JavascriptInterface\nimport android.widget.Toast\nimport java.net.HttpURLConnection\nimport java.net.URL\n",1)
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
        @JavascriptInterface fun checkForUpdates() {
            Thread {
                try {
                    val j=metadata()
                    if(j.optString("appName")!="My Diary" || j.optString("packageName")!=packageName) throw Exception("Wrong app")
                    val latest=j.optInt("versionCode",0)
                    if(latest<=currentVersion()) runOnUiThread { Toast.makeText(this@MainActivity,"My Diary pehle se latest hai.",Toast.LENGTH_LONG).show() }
                    else runOnUiThread { Toast.makeText(this@MainActivity,"Naya update " + j.optString("versionName") + " available hai. Download & Install dabayein.",Toast.LENGTH_LONG).show() }
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
marker="</main>\n<div id=\"diaryHomeEntryHost\""
if "diary-app-actions" in h: raise SystemExit("Already inserted")
if marker not in h: raise SystemExit("Diary home marker missing")
ui='''<div class="diary-app-actions"><button id="diaryCheckUpdates">🔄 Check for Updates</button><button id="diaryDownloadInstall">⬇️ Download &amp; Install</button></div>
<style>.diary-app-actions{position:fixed;z-index:2147483000;top:env(safe-area-inset-top,0px);left:0;right:0;display:flex;gap:8px;justify-content:center;padding:7px 10px;background:#faf7ff;border-bottom:1px solid #d4af37}.diary-app-actions button{flex:1;max-width:230px;min-height:40px;border:1px solid #b99bdf;border-radius:10px;background:linear-gradient(145deg,#fff,#eee5ff);color:#45256f;font-weight:800;font-size:13px}</style>
<script>(function(){var u=document.getElementById('diaryCheckUpdates'),d=document.getElementById('diaryDownloadInstall'),l=document.getElementById('diaryLanguageSelect');var names={roman:['🔄 Update Check Karein','⬇️ Download aur Install'],english:['🔄 Check for Updates','⬇️ Download & Install'],hindi:['🔄 अपडेट जाँचें','⬇️ डाउनलोड और इंस्टॉल']};function labels(){var a=names[l&&names[l.value]?l.value:'roman'];u.textContent=a[0];d.textContent=a[1]}u.onclick=function(){if(window.DiaryAppActions)DiaryAppActions.checkForUpdates()};d.onclick=function(){if(window.DiaryAppActions)DiaryAppActions.downloadAndInstall()};if(l)l.addEventListener('change',labels);labels()})();</script>
'''
h=h.replace(marker,"</main>\n"+ui+"<div id=\"diaryHomeEntryHost\"",1)
m.write_text(h,encoding="utf-8")
print("PASS: Update checker and SHA-256 verified APK download/install controls added; version set to 1.0.90")
