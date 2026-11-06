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
        @JavascriptInterface fun shareApp() {
            runOnUiThread {
                try {
                    val dir=File(cacheDir,"diary-share").apply{mkdirs()}
                    val apk=File(dir,"My-Diary.apk")
                    File(applicationInfo.sourceDir).copyTo(apk,true)
                    val uri=FileProvider.getUriForFile(this@MainActivity,"$packageName.fileprovider",apk)
                    val send=Intent(Intent.ACTION_SEND).apply {
                        type="application/vnd.android.package-archive"
                        putExtra(Intent.EXTRA_STREAM,uri)
                        putExtra(Intent.EXTRA_SUBJECT,"My Diary App")
                        clipData=ClipData.newUri(contentResolver,"My Diary APK",uri)
                        addFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION)
                    }
                    startActivity(Intent.createChooser(send,"Share My Diary App"))
                } catch (_:Exception) { Toast.makeText(this@MainActivity,"App share nahi ho saka.",Toast.LENGTH_LONG).show() }
            }
        }
        @JavascriptInterface fun checkForUpdates() {
            Thread {
                try {
                    val c=URL("https://raw.githubusercontent.com/amuazzinxyz-ops/My-Diary-Updates/main/latest.json").openConnection() as HttpURLConnection
                    c.connectTimeout=15000;c.readTimeout=15000
                    val j=JSONObject(c.inputStream.bufferedReader().use{it.readText()});c.disconnect()
                    if(j.optString("appName")!="My Diary" || j.optString("packageName")!=packageName) throw Exception("Wrong app")
                    val info=packageManager.getPackageInfo(packageName,0)
                    @Suppress("DEPRECATION")
                    val current=if(android.os.Build.VERSION.SDK_INT>=28) info.longVersionCode.toInt() else info.versionCode
                    val latest=j.optInt("versionCode",0)
                    if(latest<=current){runOnUiThread{Toast.makeText(this@MainActivity,"My Diary pehle se latest hai.",Toast.LENGTH_LONG).show()};return@Thread}
                    val link=j.optString("apkUrl")
                    if(!link.startsWith("https://raw.githubusercontent.com/amuazzinxyz-ops/My-Diary-Updates/main/")) throw Exception("Untrusted APK link")
                    runOnUiThread {
                        Toast.makeText(this@MainActivity,"Naya update mil gaya. Download karke Android installer mein Update confirm karein.",Toast.LENGTH_LONG).show()
                        startActivity(Intent(Intent.ACTION_VIEW,Uri.parse(link)))
                    }
                } catch (_:Exception) {
                    runOnUiThread{Toast.makeText(this@MainActivity,"Update check nahi ho saka. Internet check karein.",Toast.LENGTH_LONG).show()}
                }
            }.start()
        }
    }
"""
i=s.rfind("\n}")
if i<0: raise SystemExit("Class end missing")
s=s[:i]+native+s[i:]
kt.write_text(s,encoding="utf-8")

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
ui='''<div class="diary-app-actions"><button id="diaryShareApp">📤 Share App</button><button id="diaryCheckUpdates">🔄 Check for Updates</button></div>
<style>.diary-app-actions{position:fixed;z-index:2147483000;top:env(safe-area-inset-top,0px);left:0;right:0;display:flex;gap:8px;justify-content:center;padding:7px 10px;background:#faf7ff;border-bottom:1px solid #d4af37}.diary-app-actions button{flex:1;max-width:230px;min-height:40px;border:1px solid #b99bdf;border-radius:10px;background:linear-gradient(145deg,#fff,#eee5ff);color:#45256f;font-weight:800;font-size:13px}</style>
<script>(function(){var s=document.getElementById('diaryShareApp'),u=document.getElementById('diaryCheckUpdates'),l=document.getElementById('diaryLanguageSelect');var names={roman:['📤 App Share Karein','🔄 Update Check Karein'],english:['📤 Share App','🔄 Check for Updates'],hindi:['📤 ऐप शेयर करें','🔄 अपडेट जाँचें']};function labels(){var a=names[l&&names[l.value]?l.value:'roman'];s.textContent=a[0];u.textContent=a[1]}s.onclick=function(){if(window.DiaryAppActions)DiaryAppActions.shareApp()};u.onclick=function(){if(window.DiaryAppActions)DiaryAppActions.checkForUpdates()};if(l)l.addEventListener('change',labels);labels()})();</script>
'''
h=h.replace(marker,"</main>\n"+ui+"<div id=\"diaryHomeEntryHost\"",1)
m.write_text(h,encoding="utf-8")
print("PASS: Native Share App and update-check controls added; version set to 1.0.90")
