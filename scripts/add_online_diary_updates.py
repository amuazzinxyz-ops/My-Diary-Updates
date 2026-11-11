from pathlib import Path
import re

kt = Path("diary-project/app/src/main/java/com/muazzin/diary/MainActivity.kt")
s = kt.read_text(encoding="utf-8")
if "DiaryBundlePathHandler" in s:
    raise SystemExit("Online Diary bundle updater already patched")
if "class DiaryNativeActions" not in s:
    raise SystemExit("DiaryNativeActions missing; run add_diary_app_actions.py first")

old = '.addPathHandler("/assets/", WebViewAssetLoader.AssetsPathHandler(this))'
new = '.addPathHandler("/assets/", DiaryBundlePathHandler())'
if s.count(old) != 1:
    raise SystemExit("Expected exactly one WebView assets path handler")
s = s.replace(old, new, 1)

old_toast = 'if(latest>currentVersion()) runOnUiThread { downloadAndInstall() }\n                    else runOnUiThread { downloadWebBundleIfAvailable(j) }'
new_toast = 'if(latest>currentVersion()) runOnUiThread { downloadAndInstall() }\n                    else runOnUiThread { downloadWebBundleIfAvailable(j) }'
if s.count(old_toast) != 1:
    raise SystemExit("Could not safely locate existing APK latest-check branch")
s = s.replace(old_toast, new_toast, 1)

method_anchor = '        @JavascriptInterface fun downloadAndInstall() {'
web_method = r"""
        private fun downloadWebBundleIfAvailable(j: JSONObject) {
            val target = j.optInt("webVersion", 0)
            val prefs = getSharedPreferences("diary_web_updates", MODE_PRIVATE)
            val expected = j.optString("webSha256").lowercase()
            val link = j.optString("webUrl")
            val trustedPrefix = "https://raw.githubusercontent.com/amuazzinxyz-ops/My-Diary-Updates/main/web-source/index.html"
            if (target < 1 || !expected.matches(Regex("[0-9a-f]{64}")) || !link.startsWith(trustedPrefix)) {
                runOnUiThread { Toast.makeText(this@MainActivity, "Diary update details sahi nahi hain.", Toast.LENGTH_LONG).show() }
                return
            }
            val installedFile = File(filesDir, "diary-web/index.html")
            val installedHash = if (installedFile.isFile) {
                try {
                    val md = java.security.MessageDigest.getInstance("SHA-256")
                    installedFile.inputStream().use { input ->
                        val buffer = ByteArray(16384)
                        while (true) {
                            val count = input.read(buffer)
                            if (count < 0) break
                            md.update(buffer, 0, count)
                        }
                    }
                    md.digest().joinToString("") { "%02x".format(it.toInt() and 0xff) }
                } catch (_: Exception) { "" }
            } else ""
            if (installedHash == expected) {
                prefs.edit().putInt("webVersion", target).apply()
                // The file is current, but the WebView may still be displaying an older page
                // kept alive in memory. Reload the same app-assets URL so the path handler
                // serves the verified on-disk HTML immediately.
                runOnUiThread {
                    webView.post {
                        // Force WebView to discard any stale in-memory/disk page before reloading
                        // the SHA-256-verified local Diary HTML bundle.
                        webView.stopLoading()
                        webView.clearCache(true)
                        webView.clearHistory()
                        webView.loadUrl("https://appassets.androidplatform.net/assets/index.html?diaryRefresh=" + System.currentTimeMillis())
                        Toast.makeText(this@MainActivity, "Diary pehle se update hai. Screen refresh kar di gayi hai.", Toast.LENGTH_LONG).show()
                    }
                }
                return
            }
            Thread {
                try {
                    runOnUiThread { Toast.makeText(this@MainActivity, "Diary ka naya update download ho raha hai...", Toast.LENGTH_LONG).show() }
                    val dir = File(filesDir, "diary-web")
                    if (!dir.exists() && !dir.mkdirs()) throw Exception("Update folder nahi bana")
                    val part = File(dir, "index.html.part")
                    val current = File(dir, "index.html")
                    val backup = File(dir, "index.html.previous")
                    val connection = URL(link + (if (link.contains("?")) "&" else "?") + "v=" + System.currentTimeMillis()).openConnection() as HttpURLConnection
                    connection.connectTimeout = 25000
                    connection.readTimeout = 90000
                    connection.useCaches = false
                    connection.instanceFollowRedirects = true
                    connection.setRequestProperty("Cache-Control", "no-cache, no-store")
                    connection.setRequestProperty("User-Agent", "MyDiaryWebUpdater/1.0")
                    val digest = java.security.MessageDigest.getInstance("SHA-256")
                    var total = 0L
                    try {
                        val response = connection.responseCode
                        if (response !in 200..299) throw java.io.IOException("HTTP $response")
                        val finalUrl = connection.url
                        if (finalUrl.protocol != "https" || !(finalUrl.host == "raw.githubusercontent.com" || finalUrl.host == "githubusercontent.com" || finalUrl.host.endsWith(".githubusercontent.com"))) throw Exception("Untrusted update redirect")
                        connection.inputStream.use { input ->
                            part.outputStream().use { output ->
                                val buffer = ByteArray(16384)
                                while (true) {
                                    val count = input.read(buffer)
                                    if (count < 0) break
                                    total += count
                                    if (total > 35L * 1024L * 1024L) throw Exception("Diary update file bahut bada hai")
                                    digest.update(buffer, 0, count)
                                    output.write(buffer, 0, count)
                                }
                                output.flush()
                            }
                        }
                    } finally { connection.disconnect() }
                    if (total < 1000L) throw Exception("Diary update file adhura hai")
                    val actual = digest.digest().joinToString("") { "%02x".format(it.toInt() and 0xff) }
                    if (actual != expected) throw Exception("Diary update SHA-256 match nahi hua")
                    val head = part.inputStream().use { input -> ByteArray(4096).also { input.read(it) }.toString(Charsets.UTF_8) }
                    if (!head.contains("<html", true) && !head.contains("<!doctype", true)) throw Exception("Downloaded Diary file valid HTML nahi hai")
                    if (backup.exists()) backup.delete()
                    if (current.exists() && !current.renameTo(backup)) throw Exception("Purana Diary version safe nahi ho saka")
                    if (!part.renameTo(current)) {
                        if (backup.exists()) backup.renameTo(current)
                        throw Exception("Naya Diary update apply nahi hua")
                    }
                    prefs.edit().putInt("webVersion", target).apply()
                    runOnUiThread {
                        Toast.makeText(this@MainActivity, "My Diary update lag gaya. App refresh ho rahi hai...", Toast.LENGTH_LONG).show()
                        webView.postDelayed({
                            webView.stopLoading()
                            webView.clearCache(true)
                            webView.clearHistory()
                            webView.loadUrl("https://appassets.androidplatform.net/assets/index.html?diaryRefresh=" + System.currentTimeMillis())
                        }, 700)
                    }
                } catch (e: Exception) {
                    File(filesDir, "diary-web/index.html.part").delete()
                    val reason = e.message?.take(160) ?: "Unknown error"
                    runOnUiThread {
                        AlertDialog.Builder(this@MainActivity)
                            .setTitle("Diary update nahi ho saka")
                            .setMessage("Wajah: $reason\nAapke notes, photos aur PIN data ko touch nahi kiya gaya.")
                            .setPositiveButton("Theek hai", null).show()
                    }
                }
            }.start()
        }
"""
if s.count(method_anchor) != 1:
    raise SystemExit("Could not safely locate native updater method insertion point")
s = s.replace(method_anchor, web_method + "\n" + method_anchor, 1)

handler = r"""
    private inner class DiaryBundlePathHandler : WebViewAssetLoader.PathHandler {
        override fun handle(path: String): WebResourceResponse? {
            return try {
                val updated = File(filesDir, "diary-web/index.html")
                val stream = if (path == "index.html" && updated.isFile) updated.inputStream() else assets.open(path)
                val mime = if (path.endsWith(".html", true)) "text/html" else android.webkit.MimeTypeMap.getSingleton().getMimeTypeFromExtension(path.substringAfterLast('.', "")) ?: "application/octet-stream"
                val noCacheHeaders = mapOf(
                    "Cache-Control" to "no-store, no-cache, must-revalidate, max-age=0",
                    "Pragma" to "no-cache",
                    "Expires" to "0"
                )
                WebResourceResponse(mime, "UTF-8", 200, "OK", noCacheHeaders, stream)
            } catch (_: Exception) {
                null
            }
        }
    }
"""
idx = s.rfind("\n}")
if idx < 0:
    raise SystemExit("MainActivity closing brace missing")
s = s[:idx] + "\n" + handler + s[idx:]
kt.write_text(s, encoding="utf-8")
print("PASS: secure hash-verified online HTML bundle updater added; same WebView origin and bundled fallback retained.")
