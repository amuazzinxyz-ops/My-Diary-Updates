#!/usr/bin/env python3
"""Apply least-privilege Google AuthorizationClient and encrypted Drive upload bridge."""
from pathlib import Path
import argparse, re
p=argparse.ArgumentParser()
p.add_argument("--project",required=True,type=Path)
project=p.parse_args().project.resolve()
main=project/"app/src/main/java/com/muazzin/diary/MainActivity.kt"
gradle=project/"app/build.gradle.kts"
if not main.is_file() or not gradle.is_file(): raise SystemExit("BLOCKED: Android project files missing")
s=main.read_text(encoding="utf-8")
anchor="import android.content.Intent\n"
imports=[
"import com.google.android.gms.auth.api.identity.AuthorizationRequest",
"import com.google.android.gms.auth.api.identity.Identity",
"import com.google.android.gms.common.api.Scope",
]
if anchor not in s: raise SystemExit("BLOCKED: Intent import anchor missing")
for item in imports:
    if item not in s: s=s.replace(anchor,anchor+item+"\n",1)
bridge_anchor="        @JavascriptInterface fun saveBackup(content: String, suggestedName: String) {"
bridge="""        @JavascriptInterface fun uploadEncryptedDiaryBackup(fileName: String) {
            this@MainActivity.beginGoogleDriveBackup(fileName)
        }
"""
if bridge_anchor not in s: raise SystemExit("BLOCKED: native bridge insertion anchor missing")
if "fun uploadEncryptedDiaryBackup(fileName: String)" not in s: s=s.replace(bridge_anchor,bridge+"\n"+bridge_anchor,1)
field="    private var pendingDiaryBackupContent: String? = null"
if field not in s: raise SystemExit("BLOCKED: backup state field missing")
if "pendingGoogleBackupFileName" not in s: s=s.replace(field,field+"\n    private var pendingGoogleBackupFileName: String? = null",1)
req="    private val DIARY_REMINDER_SOUND_FILE_REQUEST_CODE = 7321"
if req not in s: raise SystemExit("BLOCKED: request-code anchor missing")
if "DIARY_GOOGLE_AUTH_REQUEST_CODE" not in s: s=s.replace(req,req+"\n    private val DIARY_GOOGLE_AUTH_REQUEST_CODE = 7322",1)
outer_anchor="    private fun startDiaryBackupSave(content: String, suggestedName: String) {"
outer=r"""
    private fun notifyGoogleDriveBackupResult(ok: Boolean, message: String) {
        runOnUiThread {
            val payload = JSONObject().put("ok", ok).put("message", message)
            webView.evaluateJavascript("window.__diaryDriveBackupResult && window.__diaryDriveBackupResult(" + payload.toString() + ");", null)
        }
    }

    private fun beginGoogleDriveBackup(fileName: String) {
        runOnUiThread {
            if (pendingGoogleBackupFileName != null) {
                notifyGoogleDriveBackupResult(false, "Google Drive backup pehle se chal raha hai.")
                return@runOnUiThread
            }
            if (!fileName.matches(Regex("my-diary-backup-[0-9]{10,17}\\.mydbk"))) {
                notifyGoogleDriveBackupResult(false, "Encrypted backup file name invalid hai.")
                return@runOnUiThread
            }
            val folder = File(cacheDir, "diary-cloud-backup").canonicalFile
            val file = File(folder, fileName).canonicalFile
            if (file.parentFile != folder || !file.isFile || file.length() <= 0L || file.length() > 80L * 1024L * 1024L) {
                notifyGoogleDriveBackupResult(false, "Encrypted backup file missing ya size limit se badi hai.")
                return@runOnUiThread
            }
            pendingGoogleBackupFileName = fileName
            val request = AuthorizationRequest.builder()
                .setRequestedScopes(listOf(Scope("https://www.googleapis.com/auth/drive.appdata")))
                .build()
            Identity.getAuthorizationClient(this@MainActivity).authorize(request)
                .addOnSuccessListener { authorization ->
                    if (authorization.hasResolution()) {
                        try {
                            val pending = authorization.pendingIntent ?: throw IllegalStateException("Google consent intent missing")
                            startIntentSenderForResult(pending.intentSender, DIARY_GOOGLE_AUTH_REQUEST_CODE, null, 0, 0, 0)
                        } catch (_: Exception) {
                            pendingGoogleBackupFileName = null
                            notifyGoogleDriveBackupResult(false, "Google permission window nahi khul saka.")
                        }
                    } else uploadEncryptedDiaryBackupNow(authorization.accessToken)
                }
                .addOnFailureListener {
                    pendingGoogleBackupFileName = null
                    notifyGoogleDriveBackupResult(false, "Google Drive permission nahi mil saki. Dobara Connect karein.")
                }
        }
    }

    private fun finishGoogleDriveAuthorization(data: Intent?) {
        try {
            val authorization = Identity.getAuthorizationClient(this@MainActivity).getAuthorizationResultFromIntent(data)
            uploadEncryptedDiaryBackupNow(authorization.accessToken)
        } catch (_: Exception) {
            pendingGoogleBackupFileName = null
            notifyGoogleDriveBackupResult(false, "Google Drive permission cancel ya fail hui.")
        }
    }

    private fun uploadEncryptedDiaryBackupNow(accessToken: String?) {
        val token = accessToken?.takeIf { it.isNotBlank() }
        val fileName = pendingGoogleBackupFileName
        if (token == null || fileName.isNullOrBlank()) {
            pendingGoogleBackupFileName = null
            notifyGoogleDriveBackupResult(false, "Google Drive access token nahi mila. Dobara Connect karein.")
            return
        }
        Thread({
            var ok = false
            try {
                val folder = File(cacheDir, "diary-cloud-backup").canonicalFile
                val file = File(folder, fileName).canonicalFile
                if (file.parentFile != folder || !file.isFile || file.length() <= 0L || file.length() > 80L * 1024L * 1024L) {
                    throw java.io.IOException("Encrypted staging file invalid.")
                }
                val driveName = "My Diary Encrypted Backup.mydbk"
                val query = "name = '$driveName' and 'appDataFolder' in parents and trashed = false"
                val listUrl = URL("https://www.googleapis.com/drive/v3/files?q=" +
                    java.net.URLEncoder.encode(query, "UTF-8") + "&spaces=appDataFolder&fields=files(id,name)&pageSize=10")
                val list = listUrl.openConnection() as HttpURLConnection
                list.requestMethod = "GET"
                list.connectTimeout = 20000
                list.readTimeout = 30000
                list.setRequestProperty("Authorization", "Bearer " + token)
                val existingId = try {
                    if (list.responseCode !in 200..299) throw java.io.IOException("Drive lookup HTTP " + list.responseCode)
                    val files = JSONObject(list.inputStream.bufferedReader().use { it.readText() }).optJSONArray("files")
                    if (files != null && files.length() > 0) files.optJSONObject(0)?.optString("id")?.takeIf { it.isNotBlank() } else null
                } finally { list.disconnect() }

                if (existingId != null) {
                    val updateUrl = URL("https://www.googleapis.com/upload/drive/v3/files/" +
                        java.net.URLEncoder.encode(existingId, "UTF-8") + "?uploadType=media")
                    val update = updateUrl.openConnection() as HttpURLConnection
                    update.requestMethod = "PATCH"
                    update.doOutput = true
                    update.connectTimeout = 20000
                    update.readTimeout = 90000
                    update.setRequestProperty("Authorization", "Bearer " + token)
                    update.setRequestProperty("Content-Type", "application/octet-stream")
                    update.setFixedLengthStreamingMode(file.length())
                    try {
                        update.outputStream.use { output -> file.inputStream().use { input -> input.copyTo(output, 64 * 1024) } }
                        if (update.responseCode !in 200..299) throw java.io.IOException("Drive update HTTP " + update.responseCode)
                    } finally { update.disconnect() }
                } else {
                    val boundary = "MyDiaryBackup" + java.util.UUID.randomUUID().toString().replace("-", "")
                    val createUrl = URL("https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart&fields=id,name")
                    val create = createUrl.openConnection() as HttpURLConnection
                    create.requestMethod = "POST"
                    create.doOutput = true
                    create.connectTimeout = 20000
                    create.readTimeout = 90000
                    create.setRequestProperty("Authorization", "Bearer " + token)
                    create.setRequestProperty("Content-Type", "multipart/related; boundary=" + boundary)
                    create.setChunkedStreamingMode(64 * 1024)
                    try {
                        create.outputStream.use { output ->
                            val metadata = JSONObject().put("name", driveName)
                                .put("mimeType", "application/octet-stream")
                                .put("parents", org.json.JSONArray().put("appDataFolder"))
                            val prefix = "--" + boundary + "\r\nContent-Type: application/json; charset=UTF-8\r\n\r\n" +
                                metadata.toString() + "\r\n--" + boundary + "\r\nContent-Type: application/octet-stream\r\n\r\n"
                            output.write(prefix.toByteArray(Charsets.UTF_8))
                            file.inputStream().use { input -> input.copyTo(output, 64 * 1024) }
                            output.write(("\r\n--" + boundary + "--\r\n").toByteArray(Charsets.UTF_8))
                        }
                        if (create.responseCode !in 200..299) throw java.io.IOException("Drive create HTTP " + create.responseCode)
                    } finally { create.disconnect() }
                }

                val verify = listUrl.openConnection() as HttpURLConnection
                verify.requestMethod = "GET"
                verify.connectTimeout = 20000
                verify.readTimeout = 30000
                verify.setRequestProperty("Authorization", "Bearer " + token)
                try {
                    if (verify.responseCode !in 200..299) throw java.io.IOException("Drive verification HTTP " + verify.responseCode)
                    val files = JSONObject(verify.inputStream.bufferedReader().use { it.readText() }).optJSONArray("files")
                    if (files == null || files.length() == 0) throw java.io.IOException("Drive backup not visible after upload.")
                } finally { verify.disconnect() }
                if (!file.delete()) throw java.io.IOException("Uploaded backup staging cleanup failed.")
                getSharedPreferences("diary_cloud_backup_status_v1", Context.MODE_PRIVATE)
                    .edit().putLong("last_successful_backup_at", System.currentTimeMillis()).commit()
                ok = true
            } catch (_: Exception) {
                // Keep the encrypted staged file for retry. Never log tokens or Diary content.
            } finally {
                pendingGoogleBackupFileName = null
                notifyGoogleDriveBackupResult(ok, if (ok)
                    "Encrypted Diary backup Google Drive ke private folder mein save ho gaya."
                else "Encrypted upload verify nahi hua. Encrypted copy device par retry ke liye rakhi hai.")
            }
        }, "DiaryGoogleDriveUpload").start()
    }

"""
if outer_anchor not in s: raise SystemExit("BLOCKED: MainActivity outer-method insertion point missing")
if "private fun beginGoogleDriveBackup(" not in s: s=s.replace(outer_anchor,outer+"\n"+outer_anchor,1)
activity="        if (requestCode == DIARY_REMINDER_SOUND_RINGTONE_REQUEST_CODE) {"
handler=r"""
        if (requestCode == DIARY_GOOGLE_AUTH_REQUEST_CODE) {
            if (resultCode == Activity.RESULT_OK && data != null) finishGoogleDriveAuthorization(data)
            else {
                pendingGoogleBackupFileName = null
                notifyGoogleDriveBackupResult(false, "Google Drive permission cancel hui.")
            }
            return
        }
"""
if activity not in s: raise SystemExit("BLOCKED: onActivityResult insertion point missing")
if "finishGoogleDriveAuthorization(data)" not in s: s=s.replace(activity,handler+"\n"+activity,1)

g=gradle.read_text(encoding="utf-8")
m=re.search(r"dependencies\s*\{([^}]*)\}",g,re.S)
if not m: raise SystemExit("BLOCKED: Gradle dependencies block missing")
body=m.group(1)
dep='implementation("com.google.android.gms:play-services-auth:21.2.0")'
if dep not in body: body=body.rstrip()+"\n    "+dep+"\n"
g=g[:m.start(1)]+body+g[m.end(1):]
main.write_text(s,encoding="utf-8")
gradle.write_text(g,encoding="utf-8")
if "https://www.googleapis.com/auth/drive.appdata" not in s: raise SystemExit("BLOCKED: least-privilege scope missing")
if "drive.file" in s or "drive.readonly" in s or '\"https://www.googleapis.com/auth/drive\"' in s: raise SystemExit("BLOCKED: broad Drive scope detected")
if dep not in g or "uploadEncryptedDiaryBackup(fileName: String)" not in s: raise SystemExit("BLOCKED: Drive bridge/dependency incomplete")
if "play-services-auth:21.2.0" not in g: raise SystemExit("BLOCKED: auth dependency must remain compatible with minSdk 23")
print("PASS: AuthorizationClient drive.appdata and encrypted appDataFolder create/update/verify bridge staged.")
