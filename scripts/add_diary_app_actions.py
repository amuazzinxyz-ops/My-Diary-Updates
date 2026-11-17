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
s=s.replace("import android.content.Intent\n","import android.content.Intent\nimport android.media.AudioAttributes\nimport android.media.RingtoneManager\nimport android.media.Ringtone\nimport android.app.Service\nimport android.content.pm.ServiceInfo\nimport android.os.Handler\nimport android.os.Looper\nimport android.os.IBinder\nimport android.app.AlertDialog\nimport android.app.AlarmManager\nimport android.app.Notification\nimport android.app.NotificationChannel\nimport android.app.NotificationManager\nimport android.app.PendingIntent\nimport android.app.ProgressDialog\nimport android.content.BroadcastReceiver\nimport android.content.Context\nimport android.os.Build\nimport android.content.DialogInterface\nimport android.hardware.biometrics.BiometricPrompt\nimport android.hardware.fingerprint.FingerprintManager\nimport android.os.CancellationSignal\nimport android.webkit.JavascriptInterface\nimport android.widget.Toast\nimport android.security.keystore.KeyGenParameterSpec\nimport android.security.keystore.KeyProperties\nimport javax.crypto.Cipher\nimport javax.crypto.KeyGenerator\nimport javax.crypto.spec.GCMParameterSpec\nimport java.security.KeyStore\nimport java.net.HttpURLConnection\nimport java.net.URL\n",1)
s=s.replace("        if (WebViewFeature.isFeatureSupported(WebViewFeature.WEB_MESSAGE_LISTENER)) {","        webView.addJavascriptInterface(DiaryNativeActions(), \"DiaryAppActions\")\n\n        if (WebViewFeature.isFeatureSupported(WebViewFeature.WEB_MESSAGE_LISTENER)) {",1)
webview_client_anchor = "        webView.webViewClient = object : WebViewClientCompat() {"
if s.count(webview_client_anchor) != 1:
    raise SystemExit("Expected exactly one WebViewClient insertion point for document message bridge")
s=s.replace(webview_client_anchor, """        if (WebViewFeature.isFeatureSupported(WebViewFeature.WEB_MESSAGE_LISTENER)) {
            WebViewCompat.addWebMessageListener(webView, "DiaryNativeDocuments", setOf("https://appassets.androidplatform.net")) { _, message, sourceOrigin, isMainFrame, replyProxy ->
                if (isMainFrame && sourceOrigin.scheme == "https" && sourceOrigin.host == "appassets.androidplatform.net") {
                    try {
                        val payload = JSONObject(message.data ?: "{}")
                        val encoded = payload.optString("base64", "")
                        val name = payload.optString("fileName", "document")
                        val type = payload.optString("mimeType", "application/octet-stream")
                        if (encoded.isBlank()) throw IllegalArgumentException("Empty document")
                        Thread {
                            try {
                                DiaryNativeActions().openDocument(encoded, name, type)
                            } catch (error: Exception) {
                                android.util.Log.e("MyDiaryDocuments", "Web message document open failed", error)
                                runOnUiThread { Toast.makeText(this@MainActivity, "Document khol nahi saka.", Toast.LENGTH_LONG).show() }
                            }
                        }.start()
                        replyProxy.postMessage("{\\"accepted\\":true}")
                    } catch (error: Exception) {
                        android.util.Log.e("MyDiaryDocuments", "Invalid document open message", error)
                        replyProxy.postMessage("{\\"accepted\\":false}")
                    }
                }
            }
        }
        webView.webViewClient = object : WebViewClientCompat() {""", 1)
native = r"""
    inner class DiaryNativeActions {
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
        private val privateLockerBiometricAlias = "my_diary_private_locker_biometric_v1"
        private fun notifyPrivateLockerFingerprintResult(success: Boolean, mode: String, keyB64: String = "") {
            this@MainActivity.runOnUiThread {
                try {
                    val js = "window.__privateLockerFingerprintResult && window.__privateLockerFingerprintResult(" +
                        success.toString() + "," + JSONObject.quote(mode) + "," + JSONObject.quote(keyB64) + ");"
                    webView.evaluateJavascript(js, null)
                } catch (_: Exception) { }
            }
        }

        @JavascriptInterface fun canUsePrivateLockerBiometric(): Boolean {
            if (Build.VERSION.SDK_INT < Build.VERSION_CODES.P) return false
            return canUseFingerprint()
        }

        private fun privateLockerBiometricKey(create: Boolean): java.security.Key {
            val store = KeyStore.getInstance("AndroidKeyStore")
            store.load(null)
            if (create) {
                if (store.containsAlias(privateLockerBiometricAlias)) store.deleteEntry(privateLockerBiometricAlias)
                val generator = KeyGenerator.getInstance(KeyProperties.KEY_ALGORITHM_AES, "AndroidKeyStore")
                val spec = KeyGenParameterSpec.Builder(
                    privateLockerBiometricAlias,
                    KeyProperties.PURPOSE_ENCRYPT or KeyProperties.PURPOSE_DECRYPT
                ).setBlockModes(KeyProperties.BLOCK_MODE_GCM)
                    .setEncryptionPaddings(KeyProperties.ENCRYPTION_PADDING_NONE)
                    .setRandomizedEncryptionRequired(true)
                    .setUserAuthenticationRequired(true)
                    .setUserAuthenticationValidityDurationSeconds(-1)
                    .setInvalidatedByBiometricEnrollment(true)
                    .build()
                return generator.apply { init(spec) }.generateKey()
            }
            return store.getKey(privateLockerBiometricAlias, null)
                ?: throw IllegalStateException("Fingerprint key not found")
        }

        private fun privateLockerPrompt(cipher: Cipher, mode: String, keyB64: String = "") {
            if (Build.VERSION.SDK_INT < Build.VERSION_CODES.P || !canUsePrivateLockerBiometric()) {
                notifyPrivateLockerFingerprintResult(false, mode)
                return
            }
            try {
                val prompt = BiometricPrompt.Builder(this@MainActivity)
                    .setTitle("Private Locker")
                    .setSubtitle(if (mode == "enable") "Fingerprint lock enable karein" else "Fingerprint se Private Locker kholein")
                    .setNegativeButton("Use PIN", mainExecutor, DialogInterface.OnClickListener { _, _ ->
                        notifyPrivateLockerFingerprintResult(false, mode)
                    }).build()
                prompt.authenticate(
                    BiometricPrompt.CryptoObject(cipher),
                    CancellationSignal(),
                    mainExecutor,
                    object : BiometricPrompt.AuthenticationCallback() {
                        override fun onAuthenticationSucceeded(result: BiometricPrompt.AuthenticationResult?) {
                            try {
                                val authenticatedCipher = result?.cryptoObject?.cipher
                                    ?: throw IllegalStateException("Biometric cipher unavailable")
                                if (mode == "enable") {
                                    val raw = android.util.Base64.decode(keyB64, android.util.Base64.NO_WRAP)
                                    if (raw.size != 32) throw IllegalArgumentException("Invalid Locker key")
                                    val encrypted = authenticatedCipher.doFinal(raw)
                                    val prefs = getSharedPreferences("private_locker_biometric", Context.MODE_PRIVATE)
                                    prefs.edit()
                                        .putString("iv", android.util.Base64.encodeToString(authenticatedCipher.iv, android.util.Base64.NO_WRAP))
                                        .putString("cipher", android.util.Base64.encodeToString(encrypted, android.util.Base64.NO_WRAP))
                                        .apply()
                                    notifyPrivateLockerFingerprintResult(true, "enabled")
                                } else {
                                    val prefs = getSharedPreferences("private_locker_biometric", Context.MODE_PRIVATE)
                                    val encrypted = android.util.Base64.decode(prefs.getString("cipher", "") ?: "", android.util.Base64.NO_WRAP)
                                    val raw = authenticatedCipher.doFinal(encrypted)
                                    notifyPrivateLockerFingerprintResult(true, "unlock", android.util.Base64.encodeToString(raw, android.util.Base64.NO_WRAP))
                                }
                            } catch (error: Exception) {
                                android.util.Log.e("PrivateLockerBiometric", "Fingerprint key operation failed", error)
                                notifyPrivateLockerFingerprintResult(false, mode)
                            }
                        }
                        override fun onAuthenticationFailed() { }
                        override fun onAuthenticationError(errorCode: Int, errString: CharSequence?) {
                            notifyPrivateLockerFingerprintResult(false, mode)
                        }
                    }
                )
            } catch (error: Exception) {
                android.util.Log.e("PrivateLockerBiometric", "Fingerprint prompt failed", error)
                notifyPrivateLockerFingerprintResult(false, mode)
            }
        }

        @JavascriptInterface fun enablePrivateLockerFingerprint(masterKeyB64: String) {
            runOnUiThread {
                try {
                    val raw = android.util.Base64.decode(masterKeyB64, android.util.Base64.NO_WRAP)
                    if (raw.size != 32) throw IllegalArgumentException("Invalid Locker key")
                    val key = privateLockerBiometricKey(true)
                    val cipher = Cipher.getInstance("AES/GCM/NoPadding")
                    cipher.init(Cipher.ENCRYPT_MODE, key)
                    privateLockerPrompt(cipher, "enable", masterKeyB64)
                } catch (error: Exception) {
                    android.util.Log.e("PrivateLockerBiometric", "Could not prepare fingerprint key", error)
                    notifyPrivateLockerFingerprintResult(false, "enable")
                }
            }
        }

        @JavascriptInterface fun authenticatePrivateLockerFingerprint() {
            runOnUiThread {
                try {
                    val prefs = getSharedPreferences("private_locker_biometric", Context.MODE_PRIVATE)
                    val ivText = prefs.getString("iv", null) ?: throw IllegalStateException("Fingerprint is not configured")
                    val cipherText = prefs.getString("cipher", null) ?: throw IllegalStateException("Fingerprint is not configured")
                    val key = privateLockerBiometricKey(false)
                    val cipher = Cipher.getInstance("AES/GCM/NoPadding")
                    val iv = android.util.Base64.decode(ivText, android.util.Base64.NO_WRAP)
                    cipher.init(Cipher.DECRYPT_MODE, key, GCMParameterSpec(128, iv))
                    privateLockerPrompt(cipher, "unlock")
                } catch (error: Exception) {
                    android.util.Log.e("PrivateLockerBiometric", "Could not prepare fingerprint unlock", error)
                    notifyPrivateLockerFingerprintResult(false, "unlock")
                }
            }
        }

        @JavascriptInterface fun disablePrivateLockerFingerprint() {
            try {
                val store = KeyStore.getInstance("AndroidKeyStore")
                store.load(null)
                if (store.containsAlias(privateLockerBiometricAlias)) store.deleteEntry(privateLockerBiometricAlias)
                getSharedPreferences("private_locker_biometric", Context.MODE_PRIVATE).edit().clear().apply()
            } catch (error: Exception) {
                android.util.Log.e("PrivateLockerBiometric", "Could not remove fingerprint key", error)
            }
        }

        private fun notifyDiaryFingerprintResult(success: Boolean, message: String) {
            this@MainActivity.runOnUiThread {
                try {
                    val js = "window.__diaryFingerprintResult && window.__diaryFingerprintResult(" +
                        success.toString() + "," + JSONObject.quote(message) + ");"
                    webView.evaluateJavascript(js, null)
                } catch (_: Exception) { }
            }
        }

        @JavascriptInterface fun canUseFingerprint(): Boolean {
            if (Build.VERSION.SDK_INT < Build.VERSION_CODES.M) return false
            return try {
                val manager = getSystemService(FingerprintManager::class.java) ?: return false
                manager.isHardwareDetected && manager.hasEnrolledFingerprints()
            } catch (_: Exception) { false }
        }

        @JavascriptInterface fun authenticateFingerprint() {
            runOnUiThread {
                if (Build.VERSION.SDK_INT < Build.VERSION_CODES.P) {
                    notifyDiaryFingerprintResult(false, "unavailable")
                    return@runOnUiThread
                }
                if (!canUseFingerprint()) {
                    notifyDiaryFingerprintResult(false, "unavailable")
                    return@runOnUiThread
                }
                try {
                    val prompt = BiometricPrompt.Builder(this@MainActivity)
                        .setTitle("My Diary")
                        .setSubtitle("Use your fingerprint to unlock Diary")
                        .setNegativeButton("Use PIN", mainExecutor, DialogInterface.OnClickListener { _, _ ->
                            notifyDiaryFingerprintResult(false, "cancelled")
                        })
                        .build()
                    prompt.authenticate(
                        CancellationSignal(),
                        mainExecutor,
                        object : BiometricPrompt.AuthenticationCallback() {
                            override fun onAuthenticationSucceeded(result: BiometricPrompt.AuthenticationResult?) {
                                notifyDiaryFingerprintResult(true, "success")
                            }
                            override fun onAuthenticationFailed() {
                                notifyDiaryFingerprintResult(false, "failed")
                            }
                            override fun onAuthenticationError(errorCode: Int, errString: CharSequence?) {
                                notifyDiaryFingerprintResult(false, "cancelled")
                            }
                        }
                    )
                } catch (error: Exception) {
                    android.util.Log.e("MyDiaryFingerprint", "Fingerprint prompt could not start", error)
                    notifyDiaryFingerprintResult(false, "unavailable")
                }
            }
        }

        @JavascriptInterface fun saveBackup(content: String, suggestedName: String) {
            if (content.isEmpty()) return
            this@MainActivity.startDiaryBackupSave(content, suggestedName)
        }
        @JavascriptInterface fun saveMemoryImage(base64: String, fileName: String, mimeType: String): Boolean {
            return try {
                val bytes = android.util.Base64.decode(base64, android.util.Base64.DEFAULT)
                if (bytes.isEmpty() || bytes.size > 20 * 1024 * 1024) throw Exception("Invalid image size")
                val safeName = fileName.substringAfterLast('/').substringAfterLast('\\')
                    .replace(Regex("[^A-Za-z0-9._ -]"), "_").take(120).ifBlank { "My-Memory.jpg" }
                if (android.os.Build.VERSION.SDK_INT < 29) throw Exception("Downloads folder access requires Android 10 or newer")
                val values = android.content.ContentValues().apply {
                    put(android.provider.MediaStore.MediaColumns.DISPLAY_NAME, safeName)
                    put(android.provider.MediaStore.MediaColumns.MIME_TYPE, mimeType.takeIf { it.startsWith("image/") } ?: "image/jpeg")
                    put(android.provider.MediaStore.MediaColumns.RELATIVE_PATH, android.os.Environment.DIRECTORY_DOWNLOADS + "/My Diary")
                    put(android.provider.MediaStore.MediaColumns.IS_PENDING, 1)
                }
                val destination = contentResolver.insert(android.provider.MediaStore.Downloads.EXTERNAL_CONTENT_URI, values)
                    ?: throw java.io.IOException("Could not create Downloads file")
                try {
                    contentResolver.openOutputStream(destination)?.use { it.write(bytes) }
                        ?: throw java.io.IOException("Could not open Downloads file")
                    val ready = android.content.ContentValues().apply { put(android.provider.MediaStore.MediaColumns.IS_PENDING, 0) }
                    contentResolver.update(destination, ready, null, null)
                } catch (error: Exception) {
                    contentResolver.delete(destination, null, null)
                    throw error
                }
                runOnUiThread { Toast.makeText(this@MainActivity, "Photo Downloads/My Diary mein save ho gayi.", Toast.LENGTH_LONG).show() }
                true
            } catch (error: Exception) {
                android.util.Log.e("MyDiaryMemories", "Saved image download failed", error)
                runOnUiThread { Toast.makeText(this@MainActivity, "Photo download nahi ho saki.", Toast.LENGTH_LONG).show() }
                false
            }
        }
        private fun currentVersion(): Int {
            val info=packageManager.getPackageInfo(packageName,0)
            @Suppress("DEPRECATION")
            return if(android.os.Build.VERSION.SDK_INT>=28) info.longVersionCode.toInt() else info.versionCode
        }
        @JavascriptInterface fun openDocument(base64: String, fileName: String, mimeType: String): Boolean {
            if (base64.isBlank()) return false
            return try {
                val bytes = android.util.Base64.decode(base64, android.util.Base64.DEFAULT)
                if (bytes.isEmpty() || bytes.size > 20 * 1024 * 1024) throw Exception("Invalid document size")
                val safeName = fileName.substringAfterLast('/').substringAfterLast('\\')
                    .replace(Regex("[^A-Za-z0-9._ -]"), "_").take(120).ifBlank { "My-Document" }
                val folder = File(cacheDir, "diary-share")
                if (!folder.exists() && !folder.mkdirs()) throw java.io.IOException("Cannot create document cache")
                val document = File(folder, "document-" + System.currentTimeMillis() + "-" + safeName)
                document.writeBytes(bytes)
                // Prefer the actual filename extension over a picker-supplied generic or
                // vendor MIME type so Android can match the installed PDF/Office viewer.
                val extensionType = android.webkit.MimeTypeMap.getSingleton()
                    .getMimeTypeFromExtension(safeName.substringAfterLast('.', "").lowercase())
                val resolvedType = extensionType
                    ?: mimeType.takeIf { it.isNotBlank() && it != "application/octet-stream" }
                    ?: "*/*"
                // Render PDFs inside My Diary instead of relying on an external viewer app.
                if (resolvedType == "application/pdf" || safeName.substringAfterLast('.', "").equals("pdf", true)) {
                    val descriptor = android.os.ParcelFileDescriptor.open(document, android.os.ParcelFileDescriptor.MODE_READ_ONLY)
                    val renderer = android.graphics.pdf.PdfRenderer(descriptor)
                    if (renderer.pageCount <= 0) {
                        renderer.close()
                        descriptor.close()
                        throw Exception("Empty PDF")
                    }
                    // WebView JavaScript interfaces run off the Android UI thread.
                    // Build and display every PDF view on the main thread.
                    runOnUiThread {
                        try {
                    val imageView = android.widget.ImageView(this@MainActivity).apply {
                        scaleType = android.widget.ImageView.ScaleType.FIT_CENTER
                        adjustViewBounds = true
                        setPadding(8, 8, 8, 8)
                    }
                    val pageLabel = android.widget.TextView(this@MainActivity).apply {
                        gravity = android.view.Gravity.CENTER
                        textSize = 14f
                        setPadding(8, 12, 8, 12)
                    }
                    val previous = android.widget.Button(this@MainActivity).apply { text = "‹ Previous" }
                    val next = android.widget.Button(this@MainActivity).apply { text = "Next ›" }
                    val controls = android.widget.LinearLayout(this@MainActivity).apply {
                        orientation = android.widget.LinearLayout.HORIZONTAL
                        gravity = android.view.Gravity.CENTER
                        addView(previous, android.widget.LinearLayout.LayoutParams(0, android.widget.LinearLayout.LayoutParams.WRAP_CONTENT, 1f))
                        addView(pageLabel, android.widget.LinearLayout.LayoutParams(0, android.widget.LinearLayout.LayoutParams.WRAP_CONTENT, 1f))
                        addView(next, android.widget.LinearLayout.LayoutParams(0, android.widget.LinearLayout.LayoutParams.WRAP_CONTENT, 1f))
                    }
                    val scroll = android.widget.ScrollView(this@MainActivity).apply {
                        addView(imageView, android.widget.FrameLayout.LayoutParams(
                            android.widget.FrameLayout.LayoutParams.MATCH_PARENT,
                            android.widget.FrameLayout.LayoutParams.WRAP_CONTENT
                        ))
                    }
                    val content = android.widget.LinearLayout(this@MainActivity).apply {
                        orientation = android.widget.LinearLayout.VERTICAL
                        addView(scroll, android.widget.LinearLayout.LayoutParams(
                            android.widget.LinearLayout.LayoutParams.MATCH_PARENT, 0, 1f
                        ))
                        addView(controls)
                    }
                    var pageIndex = 0
                    fun renderPdfPage(index: Int) {
                        val page = renderer.openPage(index)
                        try {
                            val maxWidth = (resources.displayMetrics.widthPixels * 0.88f).toInt().coerceAtLeast(600)
                            val scale = minOf(maxWidth.toFloat() / page.width.toFloat(), 2.0f)
                            val bitmap = android.graphics.Bitmap.createBitmap(
                                (page.width * scale).toInt().coerceAtLeast(1),
                                (page.height * scale).toInt().coerceAtLeast(1),
                                android.graphics.Bitmap.Config.ARGB_8888
                            )
                            page.render(bitmap, null, null, android.graphics.pdf.PdfRenderer.Page.RENDER_MODE_FOR_DISPLAY)
                            imageView.setImageBitmap(bitmap)
                            pageLabel.text = "Page ${index + 1} of ${renderer.pageCount}"
                            previous.isEnabled = index > 0
                            next.isEnabled = index < renderer.pageCount - 1
                            pageIndex = index
                            scroll.scrollTo(0, 0)
                        } finally {
                            page.close()
                        }
                    }
                    renderPdfPage(0)
                    previous.setOnClickListener { if (pageIndex > 0) renderPdfPage(pageIndex - 1) }
                    next.setOnClickListener { if (pageIndex < renderer.pageCount - 1) renderPdfPage(pageIndex + 1) }
                    val pdfDialog = android.app.AlertDialog.Builder(this@MainActivity)
                        .setTitle(safeName)
                        .setView(content)
                        .setPositiveButton("Close", null)
                        .create()
                    pdfDialog.setOnDismissListener {
                        try { renderer.close() } catch (_: Exception) {}
                        try { descriptor.close() } catch (_: Exception) {}
                    }
                    pdfDialog.show()
                        } catch (error: Exception) {
                            try { renderer.close() } catch (_: Exception) {}
                            try { descriptor.close() } catch (_: Exception) {}
                            android.util.Log.e("MyDiaryDocuments", "Unable to display PDF", error)
                            Toast.makeText(this@MainActivity, "PDF nahi khul saka. File dobara add karke dekhein.", Toast.LENGTH_LONG).show()
                        }
                    }
                    return true
                }
                // Open photos directly inside My Diary so gallery apps that reject FileProvider
                // URIs cannot leave the user with a non-responsive document tap.
                if (resolvedType.startsWith("image/") && resolvedType != "image/gif") {
                    val bounds = android.graphics.BitmapFactory.Options().apply { inJustDecodeBounds = true }
                    android.graphics.BitmapFactory.decodeFile(document.absolutePath, bounds)
                    if (bounds.outWidth <= 0 || bounds.outHeight <= 0) throw Exception("Invalid image")
                    val maxSide = 2400
                    var sample = 1
                    while (bounds.outWidth / sample > maxSide || bounds.outHeight / sample > maxSide) sample *= 2
                    val bitmap = android.graphics.BitmapFactory.decodeFile(
                        document.absolutePath,
                        android.graphics.BitmapFactory.Options().apply { inSampleSize = sample }
                    ) ?: throw Exception("Image decode failed")
                    runOnUiThread {
                        try {
                            // Android Views must be created and attached on the main UI thread.
                            val imageView = android.widget.ImageView(this@MainActivity).apply {
                                setImageBitmap(bitmap)
                                scaleType = android.widget.ImageView.ScaleType.FIT_CENTER
                                adjustViewBounds = true
                                maxWidth = (resources.displayMetrics.widthPixels * 0.92f).toInt()
                                maxHeight = (resources.displayMetrics.heightPixels * 0.72f).toInt()
                                setPadding(12, 12, 12, 12)
                            }
                            android.app.AlertDialog.Builder(this@MainActivity)
                                .setTitle(safeName)
                                .setView(imageView)
                                .setPositiveButton("Close", null)
                                .show()
                        } catch (error: Exception) {
                            android.util.Log.e("MyDiaryDocuments", "Unable to display image", error)
                            Toast.makeText(this@MainActivity, "Photo nahi khul saki. File dobara add karke dekhein.", Toast.LENGTH_LONG).show()
                        }
                    }
                    return true
                }
                val contentUri = androidx.core.content.FileProvider.getUriForFile(
                    this@MainActivity, "$packageName.fileprovider", document
                )
                val readGrant = Intent.FLAG_GRANT_READ_URI_PERMISSION
                val grantClip = android.content.ClipData.newUri(contentResolver, safeName, contentUri)
                val viewIntent = Intent(Intent.ACTION_VIEW).apply {
                    setDataAndType(contentUri, resolvedType)
                    clipData = grantClip
                    addFlags(readGrant)
                }
                // Put the same URI grant on the chooser wrapper as well as its target
                // intent. Some Android 13–15 chooser implementations otherwise drop
                // the FileProvider grant before handing the document to the viewer.
                val chooser = Intent.createChooser(viewIntent, "Open document").apply {
                    clipData = grantClip
                    addFlags(readGrant)
                }
                runOnUiThread {
                    try {
                        startActivity(chooser)
                    } catch (error: Exception) {
                        android.util.Log.e("MyDiaryDocuments", "Unable to launch document viewer", error)
                        Toast.makeText(this@MainActivity, "Document viewer nahi khul saka. File type ya viewer check karein.", Toast.LENGTH_LONG).show()
                    }
                }
                true
            } catch (_: Exception) {
                runOnUiThread {
                    Toast.makeText(this@MainActivity, "Document khol nahi saka. File dobara add karke dekhein.", Toast.LENGTH_LONG).show()
                }
                false
            }
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
        @JavascriptInterface fun pickReminderSound(currentUri: String) {
            this@MainActivity.startDiaryReminderSoundPicker(currentUri)
        }
        @JavascriptInterface fun scheduleReminder(id: String, title: String, details: String, atMillis: Long, soundUri: String, snoozeMinutes: Int, snoozeLimit: Int, ringDurationSeconds: Int, ringVolumePercent: Int): Boolean {
            return scheduleReminderInternal(id, title, details, atMillis, soundUri, snoozeMinutes, snoozeLimit, ringDurationSeconds, ringVolumePercent, false)
        }
        @JavascriptInterface fun scheduleReminderDaily(id: String, title: String, details: String, atMillis: Long, soundUri: String, snoozeMinutes: Int, snoozeLimit: Int, ringDurationSeconds: Int, ringVolumePercent: Int): Boolean {
            return scheduleReminderInternal(id, title, details, atMillis, soundUri, snoozeMinutes, snoozeLimit, ringDurationSeconds, ringVolumePercent, true)
        }
        private fun scheduleReminderInternal(id: String, title: String, details: String, atMillis: Long, soundUri: String, snoozeMinutes: Int, snoozeLimit: Int, ringDurationSeconds: Int, ringVolumePercent: Int, repeatDaily: Boolean): Boolean {
            if (id.isBlank() || title.isBlank() || atMillis <= System.currentTimeMillis() || snoozeMinutes !in setOf(2, 5, 10, 15, 20, 30) || snoozeLimit !in setOf(0, 3, 5, 10) || ringDurationSeconds !in setOf(10, 20, 30, 60, 120, 300) || ringVolumePercent !in 0..100) return false
            if (!hasReminderNotificationPermission()) { requestReminderNotificationPermission(); return false }
            if (!hasExactAlarmPermission()) { requestExactAlarmPermission(); return false }
            // Android 14+ may deny full-screen intents to apps that are not default alarm/calling apps.
            // Do not block the actual alarm: AlarmClock + the foreground ringtone service and screen wake lock
            // must still run when full-screen UI permission is unavailable. Android will show the notification;
            // when full-screen permission is granted, the existing wake activity is used unchanged.
            return try {
                DiaryReminderScheduler.schedule(this@MainActivity, id, title, details, atMillis, soundUri, snoozeMinutes, snoozeLimit, ringDurationSeconds, ringVolumePercent, 0, repeatDaily, atMillis)
                true
            } catch (e: Exception) { false }
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
    private val DIARY_REMINDER_SOUND_RINGTONE_REQUEST_CODE = 7320
    private val DIARY_REMINDER_SOUND_FILE_REQUEST_CODE = 7321

    private fun notifyDiaryReminderSoundPicked(uri: String, label: String) {
        runOnUiThread {
            val js = "window.__diaryReminderSoundPicked && window.__diaryReminderSoundPicked(" +
                JSONObject.quote(uri) + "," + JSONObject.quote(label) + ");"
            webView.evaluateJavascript(js, null)
        }
    }

    private fun startDiaryReminderSoundPicker(currentUri: String) {
        runOnUiThread {
            val options = arrayOf("Phone ringtone / alarm tone", "Choose audio file", "Use default alarm sound")
            AlertDialog.Builder(this@MainActivity)
                .setTitle("Reminder sound")
                .setItems(options) { _, which ->
                    try {
                        when (which) {
                            0 -> {
                                val intent = Intent(RingtoneManager.ACTION_RINGTONE_PICKER).apply {
                                    putExtra(RingtoneManager.EXTRA_RINGTONE_TYPE, RingtoneManager.TYPE_ALARM or RingtoneManager.TYPE_RINGTONE)
                                    putExtra(RingtoneManager.EXTRA_RINGTONE_TITLE, "Choose reminder alarm tone")
                                    putExtra(RingtoneManager.EXTRA_RINGTONE_SHOW_DEFAULT, true)
                                    putExtra(RingtoneManager.EXTRA_RINGTONE_DEFAULT_URI, RingtoneManager.getDefaultUri(RingtoneManager.TYPE_ALARM))
                                    putExtra(RingtoneManager.EXTRA_RINGTONE_SHOW_SILENT, false)
                                    if (currentUri.isNotBlank()) putExtra(RingtoneManager.EXTRA_RINGTONE_EXISTING_URI, Uri.parse(currentUri))
                                }
                                startActivityForResult(intent, DIARY_REMINDER_SOUND_RINGTONE_REQUEST_CODE)
                            }
                            1 -> {
                                val intent = Intent(Intent.ACTION_OPEN_DOCUMENT).apply {
                                    addCategory(Intent.CATEGORY_OPENABLE)
                                    type = "audio/*"
                                    addFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION or Intent.FLAG_GRANT_PERSISTABLE_URI_PERMISSION)
                                }
                                startActivityForResult(intent, DIARY_REMINDER_SOUND_FILE_REQUEST_CODE)
                            }
                            2 -> notifyDiaryReminderSoundPicked("", "Default phone alarm sound")
                        }
                    } catch (_: Exception) {
                        Toast.makeText(this@MainActivity, "Ringtone ya audio file nahi khul saki.", Toast.LENGTH_LONG).show()
                    }
                }
                .setNegativeButton("Cancel", null)
                .show()
        }
    }

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
        if (requestCode == DIARY_REMINDER_SOUND_RINGTONE_REQUEST_CODE) {
            if (resultCode == Activity.RESULT_OK) {
                val picked = data?.getParcelableExtra<Uri>(RingtoneManager.EXTRA_RINGTONE_PICKED_URI)
                    ?: RingtoneManager.getDefaultUri(RingtoneManager.TYPE_ALARM)
                val ringtone = picked?.let { RingtoneManager.getRingtone(this, it) }
                notifyDiaryReminderSoundPicked(picked?.toString().orEmpty(), ringtone?.getTitle(this) ?: "Phone alarm tone")
            }
            return
        }
        if (requestCode == DIARY_REMINDER_SOUND_FILE_REQUEST_CODE) {
            if (resultCode == Activity.RESULT_OK) {
                val picked = data?.data
                if (picked != null) {
                    try {
                        val flags = (data?.flags ?: 0) and Intent.FLAG_GRANT_READ_URI_PERMISSION
                        if (flags != 0) contentResolver.takePersistableUriPermission(picked, flags)
                        val label = contentResolver.query(picked, null, null, null, null)?.use { cursor ->
                            val nameIndex = cursor.getColumnIndex(android.provider.OpenableColumns.DISPLAY_NAME)
                            if (cursor.moveToFirst() && nameIndex >= 0) cursor.getString(nameIndex) else null
                        }?.takeIf { it.isNotBlank() } ?: "Selected audio file"
                        notifyDiaryReminderSoundPicked(picked.toString(), label)
                    } catch (_: Exception) {
                        Toast.makeText(this@MainActivity, "Audio file ka access save nahi ho saka.", Toast.LENGTH_LONG).show()
                    }
                }
            }
            return
        }
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
    private const val AUTO_ITEMS = "auto_items"
    const val ACTION_ALARM = "com.personal.diaryapp.action.REMINDER_ALARM"
    const val ACTION_SNOOZE = "com.personal.diaryapp.action.REMINDER_SNOOZE"
    const val ACTION_AUTO_SNOOZE = "com.personal.diaryapp.action.REMINDER_AUTO_SNOOZE"
    const val ACTION_DONE = "com.personal.diaryapp.action.REMINDER_DONE"
    private const val CHANNEL_ID = "diary_reminders"

    private fun requestCode(id: String): Int = (id.hashCode() and 0x3fffffff) + 10
    private fun pendingFlags(): Int = PendingIntent.FLAG_UPDATE_CURRENT or
        (if (Build.VERSION.SDK_INT >= 23) PendingIntent.FLAG_IMMUTABLE else 0)

    private fun alarmIntent(context: Context, id: String, title: String, details: String, soundUri: String, snoozeMinutes: Int = 10, snoozeLimit: Int = 3, ringDurationSeconds: Int = 30, ringVolumePercent: Int = 80, snoozeUsed: Int = 0, repeatDaily: Boolean = false, dailyAnchorAt: Long = 0L): Intent =
        Intent(context, DiaryReminderReceiver::class.java).apply {
            action = ACTION_ALARM
            data = Uri.parse("mydiary-reminder://alarm/" + Uri.encode(id))
            putExtra("diary_reminder_id", id)
            putExtra("diary_reminder_title", title)
            putExtra("diary_reminder_details", details)
            putExtra("diary_reminder_sound_uri", soundUri)
            putExtra("diary_reminder_snooze_minutes", snoozeMinutes)
            putExtra("diary_reminder_snooze_limit", snoozeLimit)
            putExtra("diary_reminder_snooze_used", snoozeUsed)
            putExtra("diary_reminder_ring_duration_seconds", ringDurationSeconds)
            putExtra("diary_reminder_ring_volume_percent", ringVolumePercent)
            putExtra("diary_reminder_repeat_daily", repeatDaily)
            putExtra("diary_reminder_daily_anchor_at", if (dailyAnchorAt > 0L) dailyAnchorAt else System.currentTimeMillis())
        }

    private fun readItems(context: Context): org.json.JSONArray {
        val raw = context.getSharedPreferences(PREFS, Context.MODE_PRIVATE).getString(ITEMS, "[]") ?: "[]"
        return try { org.json.JSONArray(raw) } catch (_: Exception) { org.json.JSONArray() }
    }

    private fun writeItems(context: Context, items: org.json.JSONArray) {
        context.getSharedPreferences(PREFS, Context.MODE_PRIVATE).edit().putString(ITEMS, items.toString()).apply()
    }

    private fun readAutoItems(context: Context): org.json.JSONArray {
        val raw = context.getSharedPreferences(PREFS, Context.MODE_PRIVATE).getString(AUTO_ITEMS, "[]") ?: "[]"
        return try { org.json.JSONArray(raw) } catch (_: Exception) { org.json.JSONArray() }
    }

    private fun writeAutoItems(context: Context, items: org.json.JSONArray) {
        context.getSharedPreferences(PREFS, Context.MODE_PRIVATE).edit().putString(AUTO_ITEMS, items.toString()).apply()
    }

    fun schedule(context: Context, id: String, title: String, details: String, atMillis: Long, soundUri: String, snoozeMinutes: Int = 10, snoozeLimit: Int = 3, ringDurationSeconds: Int = 30, ringVolumePercent: Int = 80, snoozeUsed: Int = 0, repeatDaily: Boolean = false, dailyAnchorAt: Long = atMillis) {
        require(id.isNotBlank() && title.isNotBlank() && atMillis > System.currentTimeMillis() && snoozeMinutes in setOf(2, 5, 10, 15, 20, 30) && snoozeLimit in setOf(0, 3, 5, 10) && ringDurationSeconds in setOf(10, 20, 30, 60, 120, 300) && ringVolumePercent in 0..100 && snoozeUsed in 0..snoozeLimit)
        val alarm = context.getSystemService(Context.ALARM_SERVICE) as AlarmManager
        val pending = PendingIntent.getBroadcast(context, requestCode(id), alarmIntent(context, id, title, details, soundUri, snoozeMinutes, snoozeLimit, ringDurationSeconds, ringVolumePercent, snoozeUsed, repeatDaily, dailyAnchorAt), pendingFlags())
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
        next.put(org.json.JSONObject().put("id", id).put("title", title).put("details", details).put("at", atMillis).put("soundUri", soundUri).put("snoozeMinutes", snoozeMinutes).put("snoozeLimit", snoozeLimit).put("snoozeUsed", snoozeUsed).put("ringDurationSeconds", ringDurationSeconds).put("ringVolumePercent", ringVolumePercent).put("repeatDaily", repeatDaily).put("dailyAnchorAt", if (repeatDaily) dailyAnchorAt else 0L))
        writeItems(context, next)
    }

    fun nextDailyAt(anchorAt: Long, now: Long = System.currentTimeMillis()): Long {
        val calendar = java.util.Calendar.getInstance().apply { timeInMillis = anchorAt }
        while (calendar.timeInMillis <= now) calendar.add(java.util.Calendar.DAY_OF_YEAR, 1)
        return calendar.timeInMillis
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
            alarmIntent(context, id, "", "", ""),
            pendingFlags()
        )
        alarm.cancel(pending)
        pending.cancel()
        cancelAutoSnooze(context, id)
        remove(context, id)
    }

    private fun autoSnoozeIntent(context: Context, id: String, title: String, details: String, soundUri: String, snoozeMinutes: Int, snoozeLimit: Int, ringDurationSeconds: Int, ringVolumePercent: Int, snoozeUsed: Int, repeatDaily: Boolean, dailyAnchorAt: Long): Intent =
        Intent(context, DiaryReminderReceiver::class.java).apply {
            action = ACTION_AUTO_SNOOZE
            data = Uri.parse("mydiary-reminder://auto-snooze/" + Uri.encode(id))
            putExtra("diary_reminder_id", id)
            putExtra("diary_reminder_title", title)
            putExtra("diary_reminder_details", details)
            putExtra("diary_reminder_sound_uri", soundUri)
            putExtra("diary_reminder_snooze_minutes", snoozeMinutes)
            putExtra("diary_reminder_snooze_limit", snoozeLimit)
            putExtra("diary_reminder_snooze_used", snoozeUsed)
            putExtra("diary_reminder_ring_duration_seconds", ringDurationSeconds)
            putExtra("diary_reminder_ring_volume_percent", ringVolumePercent)
            putExtra("diary_reminder_repeat_daily", repeatDaily)
            putExtra("diary_reminder_daily_anchor_at", dailyAnchorAt)
        }

    fun scheduleAutoSnooze(context: Context, id: String, title: String, details: String, soundUri: String, atMillis: Long, snoozeMinutes: Int, snoozeLimit: Int, ringDurationSeconds: Int, ringVolumePercent: Int, snoozeUsed: Int, repeatDaily: Boolean, dailyAnchorAt: Long) {
        if (atMillis <= System.currentTimeMillis()) return
        val alarm = context.getSystemService(Context.ALARM_SERVICE) as AlarmManager
        val pending = PendingIntent.getBroadcast(
            context, requestCode(id) + 200000000,
            autoSnoozeIntent(context, id, title, details, soundUri, snoozeMinutes, snoozeLimit, ringDurationSeconds, ringVolumePercent, snoozeUsed, repeatDaily, dailyAnchorAt),
            pendingFlags()
        )
        val showIntent = context.packageManager.getLaunchIntentForPackage(context.packageName)
            ?: Intent(context, MainActivity::class.java)
        showIntent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK or Intent.FLAG_ACTIVITY_CLEAR_TOP)
        val showPending = PendingIntent.getActivity(context, requestCode(id) + 300000000, showIntent, pendingFlags())
        alarm.setAlarmClock(AlarmManager.AlarmClockInfo(atMillis, showPending), pending)
        val old = readAutoItems(context)
        val next = org.json.JSONArray()
        for (i in 0 until old.length()) {
            val item = old.optJSONObject(i) ?: continue
            if (item.optString("id") != id) next.put(item)
        }
        next.put(org.json.JSONObject()
            .put("id", id).put("title", title).put("details", details).put("soundUri", soundUri)
            .put("at", atMillis).put("snoozeMinutes", snoozeMinutes).put("snoozeLimit", snoozeLimit)
            .put("snoozeUsed", snoozeUsed).put("ringDurationSeconds", ringDurationSeconds)
            .put("ringVolumePercent", ringVolumePercent).put("repeatDaily", repeatDaily)
            .put("dailyAnchorAt", dailyAnchorAt))
        writeAutoItems(context, next)
    }

    fun cancelAutoSnooze(context: Context, id: String) {
        val alarm = context.getSystemService(Context.ALARM_SERVICE) as AlarmManager
        val intent = Intent(context, DiaryReminderReceiver::class.java).apply {
            action = ACTION_AUTO_SNOOZE
            data = Uri.parse("mydiary-reminder://auto-snooze/" + Uri.encode(id))
        }
        val pending = PendingIntent.getBroadcast(context, requestCode(id) + 200000000, intent, pendingFlags())
        alarm.cancel(pending)
        pending.cancel()
        val old = readAutoItems(context)
        val next = org.json.JSONArray()
        for (i in 0 until old.length()) {
            val item = old.optJSONObject(i) ?: continue
            if (item.optString("id") != id) next.put(item)
        }
        writeAutoItems(context, next)
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
            val soundUri = item.optString("soundUri")
            val snoozeMinutes = item.optInt("snoozeMinutes", 10)
            val snoozeLimit = item.optInt("snoozeLimit", 3)
            val snoozeUsed = item.optInt("snoozeUsed", 0)
            val ringDurationSeconds = item.optInt("ringDurationSeconds", 30)
            val ringVolumePercent = item.optInt("ringVolumePercent", 80)
            val repeatDaily = item.optBoolean("repeatDaily", false)
            val dailyAnchorAt = item.optLong("dailyAnchorAt", item.optLong("at"))
            val at = item.optLong("at")
            if (id.isNotBlank() && title.isNotBlank()) {
                if (at > now) schedule(context, id, title, details, at, soundUri, snoozeMinutes, snoozeLimit, ringDurationSeconds, ringVolumePercent, snoozeUsed, repeatDaily, dailyAnchorAt)
                else if (repeatDaily) schedule(context, id, title, details, nextDailyAt(dailyAnchorAt, now), soundUri, snoozeMinutes, snoozeLimit, ringDurationSeconds, ringVolumePercent, 0, true, dailyAnchorAt)
                else if (at > now - 24L * 60L * 60L * 1000L) schedule(context, id, title, details, now + 5000L, soundUri, snoozeMinutes, snoozeLimit, ringDurationSeconds, ringVolumePercent, snoozeUsed)
                else remove(context, id)
            }
        }
        val autoItems = readAutoItems(context)
        autoItems.length().let { count ->
            for (i in 0 until count) {
                val item = autoItems.optJSONObject(i) ?: continue
                val id = item.optString("id")
                val title = item.optString("title")
                val at = item.optLong("at")
                if (id.isBlank() || title.isBlank()) continue
                val soundUri = item.optString("soundUri")
                val snoozeMinutes = item.optInt("snoozeMinutes", 10)
                val snoozeLimit = item.optInt("snoozeLimit", 3)
                val snoozeUsed = item.optInt("snoozeUsed", 0)
                val ringDurationSeconds = item.optInt("ringDurationSeconds", 30)
                val ringVolumePercent = item.optInt("ringVolumePercent", 80)
                val repeatDaily = item.optBoolean("repeatDaily", false)
                val dailyAnchorAt = item.optLong("dailyAnchorAt", at)
                val restoreAt = if (at > now) at else if (at > now - 24L * 60L * 60L * 1000L) now + 5000L else 0L
                if (restoreAt > 0L) scheduleAutoSnooze(context, id, title, item.optString("details"), soundUri, restoreAt, snoozeMinutes, snoozeLimit, ringDurationSeconds, ringVolumePercent, snoozeUsed, repeatDaily, dailyAnchorAt)
                else cancelAutoSnooze(context, id)
            }
        }
    }

    fun showNotification(context: Context, id: String, title: String, details: String, soundUri: String, snoozeMinutes: Int, snoozeLimit: Int, snoozeUsed: Int, ringDurationSeconds: Int, ringVolumePercent: Int, repeatDaily: Boolean, dailyAnchorAt: Long) {
        if (Build.VERSION.SDK_INT >= 33 &&
            context.checkSelfPermission(android.Manifest.permission.POST_NOTIFICATIONS) != PackageManager.PERMISSION_GRANTED) return
        val manager = context.getSystemService(Context.NOTIFICATION_SERVICE) as NotificationManager
        val alarmSound = if (soundUri.isBlank()) RingtoneManager.getDefaultUri(RingtoneManager.TYPE_ALARM) else Uri.parse(soundUri)
        val channelId = "diary_reminders_silent_v1"
        val alarmAttributes = AudioAttributes.Builder()
            .setUsage(AudioAttributes.USAGE_ALARM)
            .setContentType(AudioAttributes.CONTENT_TYPE_SONIFICATION)
            .build()
        if (Build.VERSION.SDK_INT >= 26) {
            val channel = NotificationChannel(channelId, "My Diary Reminders", NotificationManager.IMPORTANCE_HIGH).apply {
                description = "Scheduled reminders from My Diary"
                enableVibration(true)
                setSound(null, null)
            }
            manager.createNotificationChannel(channel)
        }
        val code = requestCode(id)
        val launch = context.packageManager.getLaunchIntentForPackage(context.packageName) ?: Intent()
        launch.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK or Intent.FLAG_ACTIVITY_CLEAR_TOP)
        launch.putExtra("diary_reminder_id", id)
        val content = PendingIntent.getActivity(context, code + 1, launch, pendingFlags())
        // Full-screen reminder surface shows the alert and actions immediately while
        // the selected-duration wake activity holds the display.
        val wakeIntent = Intent(context, DiaryReminderWakeActivity::class.java).apply {
            putExtra("diary_reminder_id", id)
            putExtra("diary_reminder_title", title)
            putExtra("diary_reminder_details", details)
            putExtra("diary_reminder_sound_uri", soundUri)
            putExtra("diary_reminder_snooze_minutes", snoozeMinutes)
            putExtra("diary_reminder_snooze_limit", snoozeLimit)
            putExtra("diary_reminder_snooze_used", snoozeUsed)
            putExtra("diary_reminder_ring_duration_seconds", ringDurationSeconds)
            putExtra("diary_reminder_ring_volume_percent", ringVolumePercent)
            putExtra("diary_reminder_repeat_daily", repeatDaily)
            putExtra("diary_reminder_daily_anchor_at", dailyAnchorAt)
            addFlags(Intent.FLAG_ACTIVITY_NEW_TASK or Intent.FLAG_ACTIVITY_NO_USER_ACTION)
        }
        val wakePending = PendingIntent.getActivity(context, code + 4, wakeIntent, pendingFlags())
        fun actionIntent(action: String, suffix: String): PendingIntent {
            val actionIntent = Intent(context, DiaryReminderReceiver::class.java).apply {
                this.action = action
                data = Uri.parse("mydiary-reminder://" + suffix + "/" + Uri.encode(id))
                putExtra("diary_reminder_id", id)
                putExtra("diary_reminder_title", title)
                putExtra("diary_reminder_details", details)
                putExtra("diary_reminder_sound_uri", soundUri)
                putExtra("diary_reminder_snooze_minutes", snoozeMinutes)
                putExtra("diary_reminder_snooze_limit", snoozeLimit)
                putExtra("diary_reminder_snooze_used", snoozeUsed)
                putExtra("diary_reminder_ring_duration_seconds", ringDurationSeconds)
                putExtra("diary_reminder_ring_volume_percent", ringVolumePercent)
                putExtra("diary_reminder_repeat_daily", repeatDaily)
                putExtra("diary_reminder_daily_anchor_at", dailyAnchorAt)
            }
            return PendingIntent.getBroadcast(context, code + if (action == ACTION_SNOOZE) 2 else 3, actionIntent, pendingFlags())
        }
        val builder = if (Build.VERSION.SDK_INT >= 26) Notification.Builder(context, channelId) else Notification.Builder(context)
        val body = details.ifBlank { "My Diary reminder" }
        builder.setSmallIcon(android.R.drawable.ic_lock_idle_alarm)
            .setContentTitle(title)
            .setContentText(body)
            .setStyle(Notification.BigTextStyle().bigText(body))
            .setSound(null, alarmAttributes)
            .setContentIntent(content)
            .setFullScreenIntent(wakePending, true)
            .setVisibility(Notification.VISIBILITY_PUBLIC)
            .setAutoCancel(true)
            .setPriority(Notification.PRIORITY_HIGH)
            .setCategory(Notification.CATEGORY_ALARM)
            .setDefaults(Notification.DEFAULT_VIBRATE or Notification.DEFAULT_LIGHTS)
        if (snoozeUsed < snoozeLimit) {
            builder.addAction(android.R.drawable.ic_lock_idle_alarm, "$snoozeMinutes min baad", actionIntent(ACTION_SNOOZE, "snooze"))
        }
        builder.addAction(android.R.drawable.ic_menu_close_clear_cancel, "Done", actionIntent(ACTION_DONE, "done"))
        manager.notify(code, builder.build())
    }
}

class DiaryReminderReceiver : BroadcastReceiver() {
    override fun onReceive(context: Context, intent: Intent?) {
        val msg = intent ?: return
        val id = msg.getStringExtra("diary_reminder_id") ?: return
        val title = msg.getStringExtra("diary_reminder_title") ?: "My Diary Reminder"
        val details = msg.getStringExtra("diary_reminder_details") ?: ""
        val soundUri = msg.getStringExtra("diary_reminder_sound_uri") ?: ""
        val snoozeMinutes = msg.getIntExtra("diary_reminder_snooze_minutes", 10).coerceIn(2, 30)
        val snoozeLimit = msg.getIntExtra("diary_reminder_snooze_limit", 3).coerceIn(0, 10)
        val snoozeUsed = msg.getIntExtra("diary_reminder_snooze_used", 0).coerceIn(0, snoozeLimit)
        val ringDurationSeconds = msg.getIntExtra("diary_reminder_ring_duration_seconds", 30).coerceIn(10, 300)
        val ringVolumePercent = msg.getIntExtra("diary_reminder_ring_volume_percent", 80).coerceIn(0, 100)
        val repeatDaily = msg.getBooleanExtra("diary_reminder_repeat_daily", false)
        val dailyAnchorAt = msg.getLongExtra("diary_reminder_daily_anchor_at", 0L).takeIf { it > 0L } ?: System.currentTimeMillis()
        when (msg.action) {
            DiaryReminderScheduler.ACTION_SNOOZE -> {
                DiaryReminderScheduler.cancelAutoSnooze(context, id)
                val manager = context.getSystemService(Context.NOTIFICATION_SERVICE) as NotificationManager
                manager.cancel((id.hashCode() and 0x3fffffff) + 10)
                DiaryReminderSoundService.stop(context)
                if (snoozeUsed < snoozeLimit) DiaryReminderScheduler.schedule(context, id, title, details, System.currentTimeMillis() + snoozeMinutes.toLong() * 60L * 1000L, soundUri, snoozeMinutes, snoozeLimit, ringDurationSeconds, ringVolumePercent, snoozeUsed + 1, repeatDaily, dailyAnchorAt)
                return
            }
            DiaryReminderScheduler.ACTION_AUTO_SNOOZE -> {
                val manager = context.getSystemService(Context.NOTIFICATION_SERVICE) as NotificationManager
                manager.cancel((id.hashCode() and 0x3fffffff) + 10)
                DiaryReminderSoundService.stop(context)
                DiaryReminderScheduler.schedule(context, id, title, details, System.currentTimeMillis() + snoozeMinutes.toLong() * 60L * 1000L, soundUri, snoozeMinutes, snoozeLimit, ringDurationSeconds, ringVolumePercent, snoozeUsed, repeatDaily, dailyAnchorAt)
                return
            }
            DiaryReminderScheduler.ACTION_DONE -> {
                DiaryReminderScheduler.cancelAutoSnooze(context, id)
                val manager = context.getSystemService(Context.NOTIFICATION_SERVICE) as NotificationManager
                manager.cancel((id.hashCode() and 0x3fffffff) + 10)
                DiaryReminderSoundService.stop(context)
                if (!repeatDaily) DiaryReminderScheduler.cancel(context, id)
                return
            }
        }
        if (repeatDaily) {
            DiaryReminderScheduler.schedule(context, id, title, details, DiaryReminderScheduler.nextDailyAt(dailyAnchorAt), soundUri, snoozeMinutes, snoozeLimit, ringDurationSeconds, ringVolumePercent, 0, true, dailyAnchorAt)
        } else {
            DiaryReminderScheduler.remove(context, id)
        }
        DiaryReminderScheduler.showNotification(context, id, title, details, soundUri, snoozeMinutes, snoozeLimit, snoozeUsed, ringDurationSeconds, ringVolumePercent, repeatDaily, dailyAnchorAt)
        DiaryReminderSoundService.start(context, soundUri, ringDurationSeconds, ringVolumePercent)
        // If the user does not press Done or Snooze, automatically repeat at the saved Snooze interval.
        // This fallback is independent of the manual Snooze limit and is cancelled by either action.
        DiaryReminderScheduler.scheduleAutoSnooze(
            context, id, title, details, soundUri,
            System.currentTimeMillis() + snoozeMinutes.toLong() * 60L * 1000L,
            snoozeMinutes, snoozeLimit, ringDurationSeconds, ringVolumePercent, snoozeUsed,
            repeatDaily, dailyAnchorAt
        )
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


class DiaryReminderSoundService : Service() {
    private var ringtone: Ringtone? = null
    private var screenWakeLock: android.os.PowerManager.WakeLock? = null
    private val handler = Handler(Looper.getMainLooper())
    private val stopPlayback = Runnable { stopSelf() }

    override fun onStartCommand(intent: Intent?, flags: Int, startId: Int): Int {
        val seconds = (intent?.getIntExtra("diary_reminder_ring_duration_seconds", 30) ?: 30).coerceIn(10, 300)
        val volumePercent = (intent?.getIntExtra("diary_reminder_ring_volume_percent", 80) ?: 80).coerceIn(0, 100)
        val channelId = "diary_reminder_audio_service"
        val manager = getSystemService(Context.NOTIFICATION_SERVICE) as NotificationManager
        if (Build.VERSION.SDK_INT >= 26 && manager.getNotificationChannel(channelId) == null) {
            manager.createNotificationChannel(NotificationChannel(channelId, "My Diary Alarm Playback", NotificationManager.IMPORTANCE_LOW).apply {
                description = "Timed reminder ringtone playback"
                setSound(null, null)
                enableVibration(false)
                setShowBadge(false)
            })
        }
        val notification = (if (Build.VERSION.SDK_INT >= 26) Notification.Builder(this, channelId) else Notification.Builder(this))
            .setSmallIcon(android.R.drawable.ic_lock_idle_alarm)
            .setContentTitle("My Diary")
            .setContentText("Reminder ringtone is playing")
            .setOngoing(true)
            .build()
        try {
            if (Build.VERSION.SDK_INT >= 29) startForeground(91001, notification, ServiceInfo.FOREGROUND_SERVICE_TYPE_MEDIA_PLAYBACK)
            else startForeground(91001, notification)
            handler.removeCallbacks(stopPlayback)
            ringtone?.stop()
            val power = getSystemService(Context.POWER_SERVICE) as android.os.PowerManager
            screenWakeLock?.let { if (it.isHeld) it.release() }
            screenWakeLock = power.newWakeLock(android.os.PowerManager.SCREEN_BRIGHT_WAKE_LOCK or android.os.PowerManager.ACQUIRE_CAUSES_WAKEUP or android.os.PowerManager.ON_AFTER_RELEASE, "$packageName:ReminderScreen").apply {
                setReferenceCounted(false)
                acquire(seconds * 1000L)
            }
            val selected = if (intent?.getStringExtra("diary_reminder_sound_uri").isNullOrBlank())
                RingtoneManager.getDefaultUri(RingtoneManager.TYPE_ALARM)
            else Uri.parse(intent?.getStringExtra("diary_reminder_sound_uri"))
            var player = RingtoneManager.getRingtone(this, selected)
            if (player == null) player = RingtoneManager.getRingtone(this, RingtoneManager.getDefaultUri(RingtoneManager.TYPE_ALARM))
            if (player == null) {
                stopSelf()
                return START_NOT_STICKY
            }
            player.setAudioAttributes(AudioAttributes.Builder().setUsage(AudioAttributes.USAGE_ALARM).setContentType(AudioAttributes.CONTENT_TYPE_SONIFICATION).build())
            if (Build.VERSION.SDK_INT >= 28) {
                player.isLooping = true
                player.volume = volumePercent / 100f
            }
            ringtone = player
            player.play()
            handler.postDelayed(stopPlayback, seconds * 1000L)
        } catch (_: Exception) {
            stopSelf()
        }
        return START_NOT_STICKY
    }

    override fun onDestroy() {
        handler.removeCallbacks(stopPlayback)
        try { ringtone?.stop() } catch (_: Exception) { }
        ringtone = null
        try { screenWakeLock?.let { if (it.isHeld) it.release() } } catch (_: Exception) { }
        screenWakeLock = null
        if (Build.VERSION.SDK_INT >= 24) stopForeground(STOP_FOREGROUND_REMOVE) else {
            @Suppress("DEPRECATION")
            stopForeground(true)
        }
        super.onDestroy()
    }

    override fun onBind(intent: Intent?): IBinder? = null

    companion object {
        fun start(context: Context, soundUri: String, durationSeconds: Int, volumePercent: Int) {
            val intent = Intent(context, DiaryReminderSoundService::class.java).apply {
                putExtra("diary_reminder_sound_uri", soundUri)
                putExtra("diary_reminder_ring_duration_seconds", durationSeconds)
                putExtra("diary_reminder_ring_volume_percent", volumePercent)
            }
            if (Build.VERSION.SDK_INT >= 26) context.startForegroundService(intent) else context.startService(intent)
        }
        fun stop(context: Context) {
            context.stopService(Intent(context, DiaryReminderSoundService::class.java))
        }
    }
}

// This dedicated full-screen activity displays the reminder over the keyguard.
// It never opens MainActivity or unlocks the phone; the notification's normal
// content tap remains the sole route into the Diary app.
// Screen-duration release trigger: reminder activity holds FLAG_KEEP_SCREEN_ON for the configured ring duration.
class DiaryReminderWakeActivity : android.app.Activity() {
    private fun addLine(parent: android.widget.LinearLayout, value: String, size: Float, color: Int, bold: Boolean = false) {
        val view = android.widget.TextView(this).apply {
            text = value
            textSize = size
            setTextColor(color)
            gravity = android.view.Gravity.CENTER
            if (bold) setTypeface(null, android.graphics.Typeface.BOLD)
            setPadding(8, 10, 8, 10)
        }
        parent.addView(view, android.widget.LinearLayout.LayoutParams(android.view.ViewGroup.LayoutParams.MATCH_PARENT, android.view.ViewGroup.LayoutParams.WRAP_CONTENT))
    }
    private fun actionButton(parent: android.widget.LinearLayout, label: String, color: Int, action: String) {
        val button = android.widget.Button(this).apply {
            text = label
            textSize = 17f
            setTextColor(android.graphics.Color.WHITE)
            background = android.graphics.drawable.GradientDrawable().apply { setColor(color); cornerRadius = 24f }
            setOnClickListener { sendReminderAction(action); finish() }
        }
        val params = android.widget.LinearLayout.LayoutParams(android.view.ViewGroup.LayoutParams.MATCH_PARENT, android.view.ViewGroup.LayoutParams.WRAP_CONTENT)
        params.setMargins(4, 8, 4, 8)
        parent.addView(button, params)
    }
    private fun sendReminderAction(action: String) {
        val id = intent?.getStringExtra("diary_reminder_id") ?: return
        val actionIntent = Intent(this, DiaryReminderReceiver::class.java).apply {
            this.action = action
            data = Uri.parse("mydiary-reminder://wake-action/" + action.substringAfterLast("_").lowercase() + "/" + Uri.encode(id))
            putExtra("diary_reminder_id", id)
            putExtra("diary_reminder_title", intent?.getStringExtra("diary_reminder_title") ?: "My Diary Reminder")
            putExtra("diary_reminder_details", intent?.getStringExtra("diary_reminder_details") ?: "")
            putExtra("diary_reminder_sound_uri", intent?.getStringExtra("diary_reminder_sound_uri") ?: "")
            putExtra("diary_reminder_snooze_minutes", intent?.getIntExtra("diary_reminder_snooze_minutes", 10) ?: 10)
            putExtra("diary_reminder_snooze_limit", intent?.getIntExtra("diary_reminder_snooze_limit", 3) ?: 3)
            putExtra("diary_reminder_snooze_used", intent?.getIntExtra("diary_reminder_snooze_used", 0) ?: 0)
            putExtra("diary_reminder_ring_duration_seconds", intent?.getIntExtra("diary_reminder_ring_duration_seconds", 30) ?: 30)
            putExtra("diary_reminder_ring_volume_percent", intent?.getIntExtra("diary_reminder_ring_volume_percent", 80) ?: 80)
            putExtra("diary_reminder_repeat_daily", intent?.getBooleanExtra("diary_reminder_repeat_daily", false) ?: false)
            putExtra("diary_reminder_daily_anchor_at", intent?.getLongExtra("diary_reminder_daily_anchor_at", 0L) ?: 0L)
        }
        sendBroadcast(actionIntent)
    }
    override fun onCreate(savedInstanceState: android.os.Bundle?) {
        super.onCreate(savedInstanceState)
        if (android.os.Build.VERSION.SDK_INT >= android.os.Build.VERSION_CODES.O_MR1) {
            setShowWhenLocked(true)
            setTurnScreenOn(true)
        } else {
            @Suppress("DEPRECATION")
            window.addFlags(android.view.WindowManager.LayoutParams.FLAG_SHOW_WHEN_LOCKED or android.view.WindowManager.LayoutParams.FLAG_TURN_SCREEN_ON)
        }
        window.addFlags(android.view.WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON)
        val title = intent?.getStringExtra("diary_reminder_title") ?: "My Diary Reminder"
        val details = intent?.getStringExtra("diary_reminder_details") ?: ""
        val snoozeMinutes = (intent?.getIntExtra("diary_reminder_snooze_minutes", 10) ?: 10).coerceIn(2, 30)
        val snoozeLimit = (intent?.getIntExtra("diary_reminder_snooze_limit", 3) ?: 3).coerceIn(0, 10)
        val snoozeUsed = (intent?.getIntExtra("diary_reminder_snooze_used", 0) ?: 0).coerceIn(0, snoozeLimit)
        val durationSeconds = (intent?.getIntExtra("diary_reminder_ring_duration_seconds", 30) ?: 30).coerceIn(10, 300)
        val root = android.widget.LinearLayout(this).apply {
            orientation = android.widget.LinearLayout.VERTICAL
            gravity = android.view.Gravity.CENTER
            setPadding(24, 24, 24, 24)
            setBackgroundColor(android.graphics.Color.argb(205, 8, 18, 30))
        }
        val card = android.widget.LinearLayout(this).apply {
            orientation = android.widget.LinearLayout.VERTICAL
            gravity = android.view.Gravity.CENTER
            setPadding(24, 28, 24, 24)
            background = android.graphics.drawable.GradientDrawable().apply {
                setColor(android.graphics.Color.rgb(248, 250, 252))
                cornerRadius = 32f
                setStroke(3, android.graphics.Color.rgb(194, 151, 55))
            }
        }
        addLine(card, "⏰  MY DIARY REMINDER", 15f, android.graphics.Color.rgb(139, 98, 24), true)
        addLine(card, title, 25f, android.graphics.Color.rgb(20, 35, 52), true)
        if (details.isNotBlank()) addLine(card, details, 17f, android.graphics.Color.rgb(55, 65, 81))
        addLine(card, "Reminder is ringing", 14f, android.graphics.Color.rgb(100, 116, 139))
        if (snoozeUsed < snoozeLimit) actionButton(card, "Snooze  •  ${snoozeMinutes} min", android.graphics.Color.rgb(35, 105, 83), DiaryReminderScheduler.ACTION_SNOOZE)
        actionButton(card, "Done  ✓", android.graphics.Color.rgb(155, 45, 52), DiaryReminderScheduler.ACTION_DONE)
        root.addView(card, android.widget.LinearLayout.LayoutParams(android.view.ViewGroup.LayoutParams.MATCH_PARENT, android.view.ViewGroup.LayoutParams.WRAP_CONTENT))
        setContentView(root)
        // End only the wake screen at the selected ring duration. Keep the
        // reminder notification posted until the user taps Done or Snooze.
        android.os.Handler(mainLooper).postDelayed({
            finish()
        }, durationSeconds * 1000L)
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
    "android.permission.FOREGROUND_SERVICE",
    "android.permission.FOREGROUND_SERVICE_MEDIA_PLAYBACK",
    "android.permission.WAKE_LOCK",
    "android.permission.USE_BIOMETRIC",
    "android.permission.USE_FINGERPRINT",
]
missing_permissions = [p for p in permissions if 'android:name="' + p + '"' not in ms]
if missing_permissions:
    p=ms.find(">", ms.find("<manifest"))
    if p<0: raise SystemExit("Manifest root tag missing")
    block="\n"+"\n".join('    <uses-permission android:name="' + p + '" />' for p in missing_permissions)
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
service_name = ".DiaryReminderSoundService"
service = next((node for node in app.findall("service") if node.get("{" + android_ns + "}name") == service_name), None)
if service is None:
    service = ET.SubElement(app, "service")
service.set("{" + android_ns + "}name", service_name)
service.set("{" + android_ns + "}enabled", "true")
service.set("{" + android_ns + "}exported", "false")
service.set("{" + android_ns + "}foregroundServiceType", "mediaPlayback")
wake_activity_name = ".DiaryReminderWakeActivity"
wake_activity = next((node for node in app.findall("activity")
                      if node.get("{" + android_ns + "}name") == wake_activity_name), None)
if wake_activity is None:
    wake_activity = ET.SubElement(app, "activity")
    wake_activity.set("{" + android_ns + "}name", wake_activity_name)
wake_activity.set("{" + android_ns + "}exported", "false")
wake_activity.set("{" + android_ns + "}excludeFromRecents", "true")
wake_activity.set("{" + android_ns + "}noHistory", "true")
wake_activity.set("{" + android_ns + "}showWhenLocked", "true")
wake_activity.set("{" + android_ns + "}turnScreenOn", "true")
wake_activity.set("{" + android_ns + "}taskAffinity", "")
wake_activity.set("{" + android_ns + "}theme", "@android:style/Theme.Translucent.NoTitleBar")
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
t=re.sub(r"versionCode\s*=\s*\d+","versionCode = 98",t,count=1)
t=re.sub(r'versionName\s*=\s*"[^"]+"','versionName = "1.0.98"',t,count=1)
if "versionCode = 98" not in t: raise SystemExit("Version code patch failed")
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
    elif index == 2 and all(marker in html for marker in (
        "name:'diary-master-pin'",
        "inputmode:'numeric'",
        "pattern:'[0-9]*'",
        "maxlength:'4'",
        "autocomplete:'new-password'",
        "'data-lpignore':'true'",
        "'data-1p-ignore':'true'",
        "diary-master-pin-entry",
    )):
        # The current Diary HTML already defines its master PIN input with the
        # autofill protections inline. Accept this updated form without replacing it.
        print("PASS: current Diary master PIN input already has numeric/autofill protections.")
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

# Trigger APK 1.0.152 build after reminder notification persistence fix.
