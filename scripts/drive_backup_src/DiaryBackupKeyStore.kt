package com.muazzin.diary.backup

import android.content.Context
import android.security.keystore.KeyGenParameterSpec
import android.security.keystore.KeyProperties
import java.security.KeyStore
import javax.crypto.Cipher
import javax.crypto.KeyGenerator
import javax.crypto.spec.GCMParameterSpec
import javax.crypto.spec.SecretKeySpec

/**
 * Device-local cache for the random backup DEK.
 * Only AES-GCM ciphertext is persisted in SharedPreferences; the wrapping key
 * remains non-exportable in Android Keystore. Portable recovery still uses the
 * passphrase-wrapped DEK in the cloud envelope.
 */
internal object DiaryBackupKeyStore {
    private const val ALIAS = "my_diary_cloud_backup_dek_v1"
    private const val PREFS = "diary_cloud_backup_keys_v1"
    private const val IV = "dek_iv"
    private const val CIPHER_TEXT = "dek_cipher"
    private const val KEYSTORE = "AndroidKeyStore"

    @Synchronized
    fun cacheDataKey(context: Context, dataKey: ByteArray) {
        require(dataKey.size == 32) { "Invalid backup data key." }
        val store = KeyStore.getInstance(KEYSTORE).apply { load(null) }
        val key = if (store.containsAlias(ALIAS)) {
            store.getKey(ALIAS, null) ?: throw IllegalStateException("Backup key is unavailable.")
        } else {
            val generator = KeyGenerator.getInstance(KeyProperties.KEY_ALGORITHM_AES, KEYSTORE)
            generator.init(
                KeyGenParameterSpec.Builder(
                    ALIAS,
                    KeyProperties.PURPOSE_ENCRYPT or KeyProperties.PURPOSE_DECRYPT
                )
                    .setBlockModes(KeyProperties.BLOCK_MODE_GCM)
                    .setEncryptionPaddings(KeyProperties.ENCRYPTION_PADDING_NONE)
                    .setRandomizedEncryptionRequired(true)
                    .setUserAuthenticationRequired(false)
                    .build()
            )
            generator.generateKey()
        }
        val cipher = Cipher.getInstance("AES/GCM/NoPadding")
        cipher.init(Cipher.ENCRYPT_MODE, key)
        val encrypted = cipher.doFinal(dataKey)
        val saved = context.getSharedPreferences(PREFS, Context.MODE_PRIVATE).edit()
            .putString(IV, android.util.Base64.encodeToString(cipher.iv, android.util.Base64.NO_WRAP))
            .putString(CIPHER_TEXT, android.util.Base64.encodeToString(encrypted, android.util.Base64.NO_WRAP))
            .commit()
        encrypted.fill(0)
        if (!saved) throw IllegalStateException("Backup key cache could not be saved.")
    }

    @Synchronized
    fun loadDataKey(context: Context): ByteArray {
        val prefs = context.getSharedPreferences(PREFS, Context.MODE_PRIVATE)
        val ivText = prefs.getString(IV, null) ?: throw IllegalStateException("No local backup key is cached.")
        val cipherText = prefs.getString(CIPHER_TEXT, null) ?: throw IllegalStateException("Local backup key cache is incomplete.")
        val store = KeyStore.getInstance(KEYSTORE).apply { load(null) }
        val key = store.getKey(ALIAS, null) ?: throw IllegalStateException("This device's backup key is unavailable.")
        val iv = android.util.Base64.decode(ivText, android.util.Base64.NO_WRAP)
        val encrypted = android.util.Base64.decode(cipherText, android.util.Base64.NO_WRAP)
        try {
            val cipher = Cipher.getInstance("AES/GCM/NoPadding")
            cipher.init(Cipher.DECRYPT_MODE, key, GCMParameterSpec(128, iv))
            return cipher.doFinal(encrypted).also {
                if (it.size != 32) {
                    it.fill(0)
                    throw SecurityException("Cached backup key is invalid.")
                }
            }
        } finally {
            iv.fill(0)
            encrypted.fill(0)
        }
    }

    @Synchronized
    fun clear(context: Context) {
        context.getSharedPreferences(PREFS, Context.MODE_PRIVATE).edit().clear().commit()
        val store = KeyStore.getInstance(KEYSTORE).apply { load(null) }
        if (store.containsAlias(ALIAS)) store.deleteEntry(ALIAS)
    }
}
