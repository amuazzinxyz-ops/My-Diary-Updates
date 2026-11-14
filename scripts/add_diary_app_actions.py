from pathlib import Path
# Camera safe-area repair: transparent Android status bar is applied below.
import re
import xml.etree.ElementTree as ET

base=Path("diary-project/app")
kt=base/"src/main/java/com/muazzin/diary/MainActivity.kt"
s=kt.read_text(encoding="utf-8")
# Make the Android status bar/camera safe area transparent so the Diary page
# background continues behind it. The HTML already reserves the safe inset
# with env(safe-area-inset-top), keeping the title below camera/status icons.
status_old = "        window.decorView.systemUiVisibility = View.SYSTEM_UI_FLAG_LAYOUT_STABLE"
status_new = """        window.statusBarColor = android.graphics.Color.TRANSPARENT
        window.decorView.systemUiVisibility = View.SYSTEM_UI_FLAG_LAYOUT_STABLE or View.SYSTEM_UI_FLAG_LAYOUT_FULLSCREEN or View.SYSTEM_UI_FLAG_LIGHT_STATUS_BAR"""
if status_old in s:
    s = s.replace(status_old, status_new, 1)
elif status_new not in s:
    raise SystemExit("Expected original Diary status-bar setup was not found; refusing unsafe patch")
# Wake and reveal the Diary only when Android launches it for a reminder full-screen intent.
wake_insertion = """        if (intent?.getStringExtra("diary_reminder_id") != null) {
            if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O_MR1) {
                setShowWhenLocked(true)
                setTurnScreenOn(true)
            } else {
                @Suppress("DEPRECATION")
                window.addFlags(android.view.WindowManager.LayoutParams.FLAG_SHOW_WHEN_LOCKED or android.view.WindowManager.LayoutParams.FLAG_TURN_SCREEN_ON)
            }
            window.addFlags(android.view.WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON)
        }"""
wake_anchor = "super.onCreate(savedInstanceState)"
if s.count(wake_anchor) != 1:
    raise SystemExit("Expected exactly one MainActivity onCreate super call; refusing unsafe screen-wake insertion")
s = s.replace(wake_anchor, wake_anchor + "\\n" + wake_insertion, 1)

back_old = """    @Deprecated("Deprecated in Android")
    override fun onBackPressed() {
        if (::webView.isInitialized && webView.canGoBack()) webView.goBack() else super.onBackPressed()
    }"""
back_new = """    private fun finishDiaryBackNavigation() {
        if (::webView.isInitialized && webView.canGoBack()) webView.goBack()
        else super.onBackPressed()
    }

    @Deprecated("Deprecated in Android")
    override fun onBackPressed() {
        if (!::webView.isInitialized) {
            super.onBackPressed()
            return
        }
        webView.evaluateJavascript(
            "(function(){try{return !!(window.__diaryCloseOverlayFromAndroid && window.__diaryCloseOverlayFromAndroid());}catch(e){return false;}})()"
        ) { result ->
            if (result == "true") {
                // The Diary is a single-page overlay. Clear its nested WebView history after closing it.
                webView.clearHistory()
            } else {
                finishDiaryBackNavigation()
            }
        }
    }"""
if s.count(back_old) != 1:
    raise SystemExit("Expected exactly one original Android Back handler; refusing unsafe patch")
s = s.replace(back_old, back_new, 1)
if "class DiaryNativeActions" in s: raise SystemExit("Already patched")
if "override fun onActivityResult(" in s: raise SystemExit("Existing onActivityResult found; safe merge required")
s=s.replace("import android.content.Intent\n","import android.content.Intent\nimport android.app.AlertDialog\nimport android.app.AlarmManager\nimport android.app.Notification\nimport android.app.NotificationChannel\nimport android.app.NotificationManager\nimport android.app.PendingIntent\nimport android.app.ProgressDialog\nimport android.content.BroadcastReceiver\nimport android.content.Context\nimport android.os.Build\nimport android.webkit.JavascriptInterface\nimport android.widget.Toast\nimport java.net.HttpURLConnection\nimport java.net.URL\n",1)
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
        @JavascriptInterface fun saveBackup(content: String, suggestedName: String) {
            if (content.isEmpty()) return
            this@MainActivity.startDiaryBackupSave(content, suggestedName)
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
                    if(latest>currentVersion()) runOnUiThread { downloadAndInstall() }
                    else runOnUiThread { downloadWebBundleIfAvailable(j) }
                } catch (_:Exception) {
                    runOnUiThread { Toast.makeText(this@MainActivity,"Update check nahi ho saka. Internet check karein.",Toast.LENGTH_LONG).show() }
                }
            }.start()
        }
        @JavascriptInterface fun downloadAndInstall() {
            val progress = ProgressDialog(this@MainActivity).apply {
                setTitle("My Diary update")
                setMessage("APK download shuru ho raha hai...")
                setProgressStyle(ProgressDialog.STYLE_HORIZONTAL)
                max = 100
                setProgress(0)
                setCancelable(false)
                setCanceledOnTouchOutside(false)
            }
            progress.show()
            Thread {
                try {
                    val j=metadata()
                    if(j.optString("appName")!="My Diary" || j.optString("packageName")!=packageName) throw Exception("Wrong app")
                    val targetVersion=j.optInt("versionCode",0)
                    if(targetVersion<=currentVersion()) throw Exception("Already latest")
                    val link=j.optString("apkUrl")
                    val expected=j.optString("sha256").lowercase()
                    if(!link.startsWith("https://raw.githubusercontent.com/amuazzinxyz-ops/My-Diary-Updates/main/") || !expected.matches(Regex("[0-9a-f]{64}"))) throw Exception("Untrusted update")
                    runOnUiThread { if(progress.isShowing) progress.setMessage("APK download ho raha hai...") }
                    val updateDir=File(cacheDir,"diary-share")
                    if(!updateDir.exists() && !updateDir.mkdirs()) throw Exception("Cannot create update folder")
                    val apk=File(updateDir,"my-diary-update.apk")
                    val part=File(updateDir,"my-diary-update.apk.part")
                    var downloaded=false
                    var lastFailure:Exception?=null
                    for(attempt in 1..5) {
                        try {
                            // Resume a partial APK instead of discarding it after a dropped connection.
                            var existingBytes=if(part.isFile) part.length() else 0L
                            val cacheBustedLink=link+(if(link.contains("?")) "&" else "?")+"cacheBust="+System.currentTimeMillis()+"-"+attempt
                            val c=URL(cacheBustedLink).openConnection() as HttpURLConnection
                            c.connectTimeout=60000
                            c.readTimeout=180000
                            c.useCaches=false
                            c.instanceFollowRedirects=true
                            c.setRequestProperty("Cache-Control","no-cache, no-store, max-age=0")
                            c.setRequestProperty("Pragma","no-cache")
                            c.setRequestProperty("User-Agent","MyDiaryUpdater/1.2")
                            c.setRequestProperty("Accept-Encoding","identity")
                            c.setRequestProperty("Accept","application/vnd.android.package-archive, application/octet-stream")
                            if(existingBytes>0L) c.setRequestProperty("Range","bytes=$existingBytes-")
                            val digest=java.security.MessageDigest.getInstance("SHA-256")
                            try {
                                val response=c.responseCode
                                if(response!=200 && response!=206) throw java.io.IOException("HTTP $response")
                                val append=response==206 && existingBytes>0L
                                if(append) {
                                    val contentRange=c.getHeaderField("Content-Range") ?: throw java.io.IOException("Missing Content-Range")
                                    if(!contentRange.startsWith("bytes $existingBytes-")) throw java.io.IOException("Invalid Content-Range")
                                } else {
                                    existingBytes=0L
                                    if(part.exists() && !part.delete()) throw java.io.IOException("Cannot reset partial download")
                                }
                                if(append) part.inputStream().use { oldInput ->
                                    val oldBuffer=ByteArray(65536)
                                    while(true) {
                                        val oldN=oldInput.read(oldBuffer)
                                        if(oldN<0) break
                                        digest.update(oldBuffer,0,oldN)
                                    }
                                }
                                val responseBytes=c.contentLength.toLong()
                                val rangeTotal=if(append) c.getHeaderField("Content-Range")?.substringAfterLast("/")?.toLongOrNull() ?: -1L else -1L
                                val totalBytes=if(rangeTotal>0L) rangeTotal else if(responseBytes>0L) existingBytes+responseBytes else -1L
                                var lastUiUpdate=existingBytes
                                val finalUrl=c.url
                                if(finalUrl.protocol!="https" || !(finalUrl.host=="raw.githubusercontent.com" || finalUrl.host=="githubusercontent.com" || finalUrl.host.endsWith(".githubusercontent.com"))) throw Exception("Untrusted download redirect")
                                var received=existingBytes
                                c.inputStream.use { input -> java.io.FileOutputStream(part,append).use { output ->
                                    val buffer=ByteArray(65536)
                                    while(true) {
                                        val n=input.read(buffer)
                                        if(n<0) break
                                        digest.update(buffer,0,n)
                                        output.write(buffer,0,n)
                                        received+=n
                                        if(received-lastUiUpdate>=65536L || (totalBytes>0L && received>=totalBytes)) {
                                            val percent=if(totalBytes>0L) ((received*100L)/totalBytes).toInt().coerceIn(0,100) else 0
                                            runOnUiThread {
                                                if(progress.isShowing) {
                                                    progress.isIndeterminate=totalBytes<=0L
                                                    if(totalBytes>0L) {
                                                        progress.progress=percent
                                                        progress.setMessage("APK download ho raha hai: $percent%")
                                                    } else {
                                                        progress.setMessage("APK download ho raha hai...")
                                                    }
                                                }
                                            }
                                            lastUiUpdate=received
                                        }
                                    }
                                    output.flush()
                                }}
                                if(received<=0L) throw java.io.IOException("Empty download")
                                // Content-Length is only a progress hint; GitHub/CDN may report a different size.\n                                // The complete body is accepted only after SHA-256, APK package, and version checks.
                            } finally { c.disconnect() }
                            runOnUiThread {
                                if(progress.isShowing) {
                                    progress.isIndeterminate=true
                                    progress.setMessage("Download poora. SHA-256 verification ho raha hai...")
                                }
                            }
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
                            runOnUiThread {
                                if(progress.isShowing) {
                                    progress.isIndeterminate=true
                                    progress.setMessage("APK verify ho gaya. Installer khul raha hai...")
                                }
                            }
                            break
                        } catch(e:Exception) {
                            lastFailure=e
                            part.delete()
                            if(e.message?.contains("SHA-256 mismatch")==true || e.message?.contains("HTTP 416")==true) part.delete()
                            if(attempt<5) {
                                runOnUiThread {
                                    if(progress.isShowing) {
                                        progress.progress=0
                                        progress.isIndeterminate=true
                                        progress.setMessage("Download dobara koshish ho raha hai ($attempt/3)...")
                                    }
                                }
                                Thread.sleep(1500L*attempt)
                            }
                        }
                    }
                    if(!downloaded) throw Exception("5 download attempts failed: " + (lastFailure?.message ?: "unknown error"))
                    val uri=FileProvider.getUriForFile(this@MainActivity,"$packageName.fileprovider",apk)
                    runOnUiThread {
                        if(progress.isShowing) progress.dismiss()
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
                        if(progress.isShowing) progress.dismiss()
                        AlertDialog.Builder(this@MainActivity)
                            .setTitle("My Diary update nahi ho saka")
                            .setMessage("Download/verification fail hua. Wajah: $reason\n\nAapka purana Diary data safe hai. Internet check karke dobara koshish karein.")
                            .setPositiveButton("Theek hai", null)
                            .show()
                    }
                }
            }.start()
        }

        @JavascriptInterface fun hasReminderNotificationPermission(): Boolean {
            return android.os.Build.VERSION.SDK_INT < 33 ||
                checkSelfPermission(android.Manifest.permission.POST_NOTIFICATIONS) == android.content.pm.PackageManager.PERMISSION_GRANTED
        }
        @JavascriptInterface fun requestReminderNotificationPermission() {
            runOnUiThread {
                if (android.os.Build.VERSION.SDK_INT >= 33 &&
                    checkSelfPermission(android.Manifest.permission.POST_NOTIFICATIONS) != android.content.pm.PackageManager.PERMISSION_GRANTED) {
                    requestPermissions(arrayOf(android.Manifest.permission.POST_NOTIFICATIONS), 7321)
                }
            }
        }
        @JavascriptInterface fun hasExactAlarmPermission(): Boolean {
            return android.os.Build.VERSION.SDK_INT < 31 ||
                (getSystemService(android.content.Context.ALARM_SERVICE) as android.app.AlarmManager).canScheduleExactAlarms()
        }

        @JavascriptInterface fun hasFullScreenIntentPermission(): Boolean {
            return android.os.Build.VERSION.SDK_INT < 34 ||
                (getSystemService(android.content.Context.NOTIFICATION_SERVICE) as android.app.NotificationManager).canUseFullScreenIntent()
        }
        @JavascriptInterface fun requestFullScreenIntentPermission() {
            runOnUiThread {
                if (android.os.Build.VERSION.SDK_INT >= 34 && !hasFullScreenIntentPermission()) {
                    try {
                        startActivity(Intent(android.provider.Settings.ACTION_MANAGE_APP_USE_FULL_SCREEN_INTENT, android.net.Uri.parse("package:$packageName")))
                    } catch (_: Exception) {
                        Toast.makeText(this@MainActivity, "Full-screen alarm permission settings nahi khul sake.", Toast.LENGTH_LONG).show()
                    }
                }
            }
        }
        @JavascriptInterface fun requestExactAlarmPermission() {
            runOnUiThread {
                if (android.os.Build.VERSION.SDK_INT >= 31 && !hasExactAlarmPermission()) {
                    try {
                        startActivity(Intent(android.provider.Settings.ACTION_REQUEST_SCHEDULE_EXACT_ALARM, android.net.Uri.parse("package:$packageName")))
                    } catch (_: Exception) {
                        Toast.makeText(this@MainActivity, "Alarms & reminders permission settings nahi khul sake.", Toast.LENGTH_LONG).show()
                    }
                }
            }
        }
        @JavascriptInterface fun scheduleReminder(id: String, title: String, details: String, atMillis: Long): Boolean {
            if (id.isBlank() || title.isBlank() || atMillis <= System.currentTimeMillis()) return false
            if (!hasReminderNotificationPermission()) {
                requestReminderNotificationPermission()
                return false
            }
            if (!hasExactAlarmPermission()) {
                requestExactAlarmPermission()
                return false
            }
            if (!hasFullScreenIntentPermission()) {
                requestFullScreenIntentPermission()
                return false
            }
            return try {
                DiaryReminderScheduler.schedule(this@MainActivity, id, title, details, atMillis)
                true
            } catch (e: Exception) {
                false
            }
        }
        @JavascriptInterface fun cancelReminder(id: String): Boolean {
            if (id.isBlank()) return false
            return try {
                DiaryReminderScheduler.cancel(this@MainActivity, id)
                true
            } catch (e: Exception) {
                false
            }
        }

    }
"""
i=s.rfind("\n}")
if i<0: raise SystemExit("Class end missing")
s=s[:i]+native+s[i:]
outer = r"""
    private var pendingDiaryBackupContent: String? = null
    private val DIARY_BACKUP_REQUEST_CODE = 7319

    private fun startDiaryBackupSave(content: String, suggestedName: String) {
        runOnUiThread {
            if (pendingDiaryBackupContent != null) {
                Toast.makeText(this@MainActivity, "Backup save window pehle se khula hai.", Toast.LENGTH_LONG).show()
                return@runOnUiThread
            }
            pendingDiaryBackupContent = content
            val safeName = suggestedName.substringAfterLast('/').take(120).ifBlank { "Diary-My-Notes-Backup.json" }
            val createDocument = Intent(Intent.ACTION_CREATE_DOCUMENT).apply {
                addCategory(Intent.CATEGORY_OPENABLE)
                type = "application/json"
                putExtra(Intent.EXTRA_TITLE, safeName)
            }
            try { startActivityForResult(createDocument, DIARY_BACKUP_REQUEST_CODE) }
            catch (e: Exception) {
                pendingDiaryBackupContent = null
                notifyDiaryBackupResult(false)
                Toast.makeText(this@MainActivity, "Backup save window nahi khul saka.", Toast.LENGTH_LONG).show()
            }
        }
    }

    private fun notifyDiaryBackupResult(saved: Boolean) {
        runOnUiThread {
            webView.evaluateJavascript("window.diaryBackupSaveResult && window.diaryBackupSaveResult($saved);", null)
        }
    }

    override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
        super.onActivityResult(requestCode, resultCode, data)
        if (requestCode != DIARY_BACKUP_REQUEST_CODE) return
        val content = pendingDiaryBackupContent
        pendingDiaryBackupContent = null
        val destination = data?.data
        if (resultCode == Activity.RESULT_OK && destination != null && content != null) {
            try {
                val output = contentResolver.openOutputStream(destination) ?: throw java.io.IOException("Save location open nahi hui")
                output.bufferedWriter(Charsets.UTF_8).use { it.write(content) }
                notifyDiaryBackupResult(true)
                Toast.makeText(this@MainActivity, "Backup save ho gaya.", Toast.LENGTH_LONG).show()
            } catch (e: Exception) {
                notifyDiaryBackupResult(false)
                Toast.makeText(this@MainActivity, "Backup save nahi ho saka. Doosri location chunein.", Toast.LENGTH_LONG).show()
            }
        } else {
            notifyDiaryBackupResult(false)
            Toast.makeText(this@MainActivity, "Backup save cancel hua.", Toast.LENGTH_SHORT).show()
        }
    }
"""
class_end=s.rfind("\n}")
if class_end < 0: raise SystemExit("MainActivity closing brace missing")
s=s[:class_end]+"\n"+outer+s[class_end:]
reminder_native = r"""
private object DiaryReminderScheduler {
    private const val PREFS = "diary_reminders_native_v1"
    private const val ITEMS = "items"
    const val ACTION_ALARM = "com.personal.diaryapp.action.REMINDER_ALARM"
    const val ACTION_SNOOZE = "com.personal.diaryapp.action.REMINDER_SNOOZE"
    const val ACTION_DONE = "com.personal.diaryapp.action.REMINDER_DONE"
    private const val CHANNEL_ID = "diary_reminders"

    private fun requestCode(id: String): Int = (id.hashCode() and 0x3fffffff) + 10
    private fun pendingFlags(): Int = PendingIntent.FLAG_UPDATE_CURRENT or
        (if (Build.VERSION.SDK_INT >= 23) PendingIntent.FLAG_IMMUTABLE else 0)

    private fun alarmIntent(context: Context, id: String, title: String, details: String): Intent =
        Intent(context, DiaryReminderReceiver::class.java).apply {
            action = ACTION_ALARM
            data = Uri.parse("mydiary-reminder://alarm/" + Uri.encode(id))
            putExtra("diary_reminder_id", id)
            putExtra("diary_reminder_title", title)
            putExtra("diary_reminder_details", details)
        }

    private fun readItems(context: Context): org.json.JSONArray {
        val raw = context.getSharedPreferences(PREFS, Context.MODE_PRIVATE).getString(ITEMS, "[]") ?: "[]"
        return try { org.json.JSONArray(raw) } catch (_: Exception) { org.json.JSONArray() }
    }

    private fun writeItems(context: Context, items: org.json.JSONArray) {
        context.getSharedPreferences(PREFS, Context.MODE_PRIVATE).edit().putString(ITEMS, items.toString()).apply()
    }

    fun schedule(context: Context, id: String, title: String, details: String, atMillis: Long) {
        require(id.isNotBlank() && title.isNotBlank() && atMillis > System.currentTimeMillis())
        val alarm = context.getSystemService(Context.ALARM_SERVICE) as AlarmManager
        val pending = PendingIntent.getBroadcast(context, requestCode(id), alarmIntent(context, id, title, details), pendingFlags())
        if (Build.VERSION.SDK_INT >= 31 && !alarm.canScheduleExactAlarms()) {
            throw SecurityException("Exact alarm permission is required for reliable reminders")
        }
        // Treat diary reminders as real alarm-clock events. AlarmClockInfo uses a
        // wake-up alarm and is surfaced to Android as the user's next alarm, which
        // is the strongest AlarmManager delivery class for alarms during idle modes.
        val showIntent = context.packageManager.getLaunchIntentForPackage(context.packageName)
            ?: Intent(context, MainActivity::class.java)
        showIntent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK or Intent.FLAG_ACTIVITY_CLEAR_TOP)
        val showPending = PendingIntent.getActivity(
            context, requestCode(id) + 100000000, showIntent, pendingFlags()
        )
        val alarmClock = AlarmManager.AlarmClockInfo(atMillis, showPending)
        alarm.setAlarmClock(alarmClock, pending)
        val old = readItems(context)
        val next = org.json.JSONArray()
        for (i in 0 until old.length()) {
            val item = old.optJSONObject(i) ?: continue
            if (item.optString("id") != id) next.put(item)
        }
        next.put(org.json.JSONObject().put("id", id).put("title", title).put("details", details).put("at", atMillis))
        writeItems(context, next)
    }

    fun remove(context: Context, id: String) {
        val old = readItems(context)
        val next = org.json.JSONArray()
        for (i in 0 until old.length()) {
            val item = old.optJSONObject(i) ?: continue
            if (item.optString("id") != id) next.put(item)
        }
        writeItems(context, next)
    }

    fun cancel(context: Context, id: String) {
        val alarm = context.getSystemService(Context.ALARM_SERVICE) as AlarmManager
        val pending = PendingIntent.getBroadcast(
            context, requestCode(id),
            alarmIntent(context, id, "", ""),
            pendingFlags()
        )
        alarm.cancel(pending)
        pending.cancel()
        remove(context, id)
    }

    fun restore(context: Context) {
        val old = readItems(context)
        val pending = ArrayList<org.json.JSONObject>()
        for (i in 0 until old.length()) {
            val item = old.optJSONObject(i) ?: continue
            pending.add(item)
        }
        val now = System.currentTimeMillis()
        pending.forEach { item ->
            val id = item.optString("id")
            val title = item.optString("title")
            val details = item.optString("details")
            val at = item.optLong("at")
            if (id.isNotBlank() && title.isNotBlank()) {
                if (at > now) schedule(context, id, title, details, at)
                else if (at > now - 24L * 60L * 60L * 1000L) schedule(context, id, title, details, now + 5000L)
                else remove(context, id)
            }
        }
    }

    fun showNotification(context: Context, id: String, title: String, details: String) {
        if (Build.VERSION.SDK_INT >= 33 &&
            context.checkSelfPermission(android.Manifest.permission.POST_NOTIFICATIONS) != PackageManager.PERMISSION_GRANTED) return
        val manager = context.getSystemService(Context.NOTIFICATION_SERVICE) as NotificationManager
        if (Build.VERSION.SDK_INT >= 26) {
            val channel = NotificationChannel(CHANNEL_ID, "My Diary Reminders", NotificationManager.IMPORTANCE_HIGH).apply {
                description = "Scheduled reminders from My Diary"
                enableVibration(true)
            }
            manager.createNotificationChannel(channel)
        }
        val code = requestCode(id)
        val launch = context.packageManager.getLaunchIntentForPackage(context.packageName) ?: Intent()
        launch.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK or Intent.FLAG_ACTIVITY_CLEAR_TOP)
        launch.putExtra("diary_reminder_id", id)
        val content = PendingIntent.getActivity(context, code + 1, launch, pendingFlags())
        fun actionIntent(action: String, suffix: String): PendingIntent {
            val actionIntent = Intent(context, DiaryReminderReceiver::class.java).apply {
                this.action = action
                data = Uri.parse("mydiary-reminder://" + suffix + "/" + Uri.encode(id))
                putExtra("diary_reminder_id", id)
                putExtra("diary_reminder_title", title)
                putExtra("diary_reminder_details", details)
            }
            return PendingIntent.getBroadcast(context, code + if (action == ACTION_SNOOZE) 2 else 3, actionIntent, pendingFlags())
        }
        val builder = if (Build.VERSION.SDK_INT >= 26) Notification.Builder(context, CHANNEL_ID) else Notification.Builder(context)
        val body = details.ifBlank { "My Diary reminder" }
        builder.setSmallIcon(android.R.drawable.ic_lock_idle_alarm)
            .setContentTitle(title)
            .setContentText(body)
            .setStyle(Notification.BigTextStyle().bigText(body))
            .setContentIntent(content)
            // A full-screen alarm intent asks Android to show the alarm UI over the lock screen.
            .setFullScreenIntent(content, true)
            .setAutoCancel(true)
            .setPriority(Notification.PRIORITY_HIGH)
            .setCategory(Notification.CATEGORY_ALARM)
            .setDefaults(Notification.DEFAULT_ALL)
            .addAction(android.R.drawable.ic_lock_idle_alarm, "10 min baad", actionIntent(ACTION_SNOOZE, "snooze"))
            .addAction(android.R.drawable.ic_menu_close_clear_cancel, "Done", actionIntent(ACTION_DONE, "done"))
        manager.notify(code, builder.build())
    }
}

class DiaryReminderReceiver : BroadcastReceiver() {
    override fun onReceive(context: Context, intent: Intent?) {
        val msg = intent ?: return
        val id = msg.getStringExtra("diary_reminder_id") ?: return
        val title = msg.getStringExtra("diary_reminder_title") ?: "My Diary Reminder"
        val details = msg.getStringExtra("diary_reminder_details") ?: ""
        when (msg.action) {
            DiaryReminderScheduler.ACTION_SNOOZE -> {
                val manager = context.getSystemService(Context.NOTIFICATION_SERVICE) as NotificationManager
                manager.cancel((id.hashCode() and 0x3fffffff) + 10)
                DiaryReminderScheduler.schedule(context, id, title, details, System.currentTimeMillis() + 10L * 60L * 1000L)
                return
            }
            DiaryReminderScheduler.ACTION_DONE -> {
                val manager = context.getSystemService(Context.NOTIFICATION_SERVICE) as NotificationManager
                manager.cancel((id.hashCode() and 0x3fffffff) + 10)
                DiaryReminderScheduler.cancel(context, id)
                return
            }
        }
        DiaryReminderScheduler.remove(context, id)
        DiaryReminderScheduler.showNotification(context, id, title, details)
    }
}

class DiaryReminderBootReceiver : BroadcastReceiver() {
    override fun onReceive(context: Context, intent: Intent?) {
        val action = intent?.action
        if (action == Intent.ACTION_BOOT_COMPLETED || action == Intent.ACTION_MY_PACKAGE_REPLACED) {
            DiaryReminderScheduler.restore(context)
        }
    }
}
"""
if "class DiaryReminderReceiver" in s or "object DiaryReminderScheduler" in s:
    raise SystemExit("Reminder native classes already exist in script; refusing duplicate insertion")
s += "\n" + reminder_native + "\n"
kt.write_text(s,encoding="utf-8")

manifest=base/"src/main/AndroidManifest.xml"
ms=manifest.read_text(encoding="utf-8")
permissions = [
    "android.permission.REQUEST_INSTALL_PACKAGES",
    "android.permission.POST_NOTIFICATIONS",
    "android.permission.RECEIVE_BOOT_COMPLETED",
    "android.permission.SCHEDULE_EXACT_ALARM",
    "android.permission.USE_FULL_SCREEN_INTENT",
]
missing_permissions = [p for p in permissions if 'android:name="' + p + '"' not in ms]
if missing_permissions:
    p=ms.find(">", ms.find("<manifest"))
    if p<0: raise SystemExit("Manifest root tag missing")
    block="\n"+"\\n".join('    <uses-permission android:name="' + p + '" />' for p in missing_permissions)
    ms=ms[:p+1]+block+ms[p+1:]
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
for receiver_name, actions in [
    (".DiaryReminderReceiver", []),
    (".DiaryReminderBootReceiver", ["android.intent.action.BOOT_COMPLETED", "android.intent.action.MY_PACKAGE_REPLACED"]),
]:
    existing = [node for node in app.findall("receiver") if node.get("{" + android_ns + "}name") == receiver_name]
    if not existing:
        receiver = ET.SubElement(app, "receiver")
        receiver.set("{" + android_ns + "}name", receiver_name)
        receiver.set("{" + android_ns + "}enabled", "true")
        receiver.set("{" + android_ns + "}exported", "true" if receiver_name == ".DiaryReminderBootReceiver" else "false")
        if actions:
            intent_filter = ET.SubElement(receiver, "intent-filter")
            for action_name in actions:
                action = ET.SubElement(intent_filter, "action")
                action.set("{" + android_ns + "}name", action_name)
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
if anchor not in h and "diaryShareAppBtn" not in h:
    raise SystemExit("Diary Me menu insertion point missing")
if "diaryShareAppBtn" not in h:
    actions = """
  var shareAppBtn=el('button',{id:'diaryShareAppBtn',type:'button'},'📤 Share App');
  mePanel.appendChild(shareAppBtn);
  shareAppBtn.addEventListener('click',function(e){e.preventDefault();e.stopPropagation();if(window.DiaryAppActions&&DiaryAppActions.shareApp){DiaryAppActions.shareApp();}});
"""
    h=h.replace(anchor,anchor+actions,1)
if "diary-me-app-actions-style" not in h:
    style = """
<style id="diary-me-app-actions-style">
#diaryShareAppBtn{display:block!important;width:100%!important;min-height:40px!important;height:40px!important;margin:7px 0 0!important;padding:0 10px!important;box-sizing:border-box!important;border:1px solid #b9d0bd!important;border-radius:9px!important;background:linear-gradient(145deg,#fff,#e5eee8)!important;color:#123d2a!important;font-size:18px!important;font-weight:900!important;line-height:1.15!important;text-align:left!important;white-space:nowrap!important;box-shadow:0 2px 0 #c7d9c8!important;cursor:pointer!important}
#diaryShareAppBtn:active{transform:translateY(2px)!important;box-shadow:0 0 0 transparent!important}
</style>
"""
    if "</head>" not in h:
        raise SystemExit("HTML head closing tag missing")
    h=h.replace("</head>",style+"\n</head>",1)
# Preserve the existing Check for Updates button and its handler unchanged.
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
for index, (old, new) in enumerate(pin_replacements):
    count = html.count(old)
    if count == 1:
        html = html.replace(old, new, 1)
    elif new in html:
        continue
    elif index == 0:
        # The current published Diary has its own recovery-code flow; this legacy
        # window.prompt anchor belongs only to older HTML and is not required.
        print("PASS: legacy recovery prompt anchor is not used by the current Diary HTML.")
    else:
        raise SystemExit(f"Expected existing or already-updated Diary PIN input anchor: {old[:90]}")
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
if "diary-close-glyph-centering" not in html:
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
                    .setNegativeButton("Cancel") { _, _ -> result?.cancel() }
                    .create()
                var submitted = false
                fun submitPinAutomatically() {
                    if (submitted || pinInput.text?.length != 4) return
                    submitted = true
                    val pinValue = pinInput.text.toString()
                    val manager = getSystemService(android.content.Context.INPUT_METHOD_SERVICE) as android.view.inputmethod.InputMethodManager
                    manager.hideSoftInputFromWindow(pinInput.windowToken, 0)
                    pinInput.clearFocus()
                    dialog.dismiss()
                    android.os.Handler(android.os.Looper.getMainLooper()).postDelayed({ result?.confirm(pinValue) }, 300)
                }
                dialog.setOnCancelListener { if (!submitted) result?.cancel() }
                dialog.setOnShowListener {
                    dialog.window?.setSoftInputMode(WindowManager.LayoutParams.SOFT_INPUT_STATE_ALWAYS_VISIBLE)
                    pinInput.requestFocus()
                    pinInput.addTextChangedListener(object : android.text.TextWatcher {
                        override fun beforeTextChanged(s: CharSequence?, start: Int, count: Int, after: Int) {}
                        override fun onTextChanged(s: CharSequence?, start: Int, before: Int, count: Int) {
                            if (s?.length == 4) pinInput.post { submitPinAutomatically() }
                        }
                        override fun afterTextChanged(s: android.text.Editable?) {}
                    })
                    pinInput.post {
                        val manager = getSystemService(android.content.Context.INPUT_METHOD_SERVICE) as android.view.inputmethod.InputMethodManager
                        manager.showSoftInput(pinInput, android.view.inputmethod.InputMethodManager.SHOW_IMPLICIT)
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
