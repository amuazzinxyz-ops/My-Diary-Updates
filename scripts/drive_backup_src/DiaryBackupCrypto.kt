package com.muazzin.diary.backup

import org.bouncycastle.crypto.generators.Argon2BytesGenerator
import org.bouncycastle.crypto.params.Argon2Parameters
import org.json.JSONObject
import java.io.BufferedInputStream
import java.io.BufferedOutputStream
import java.io.DataInputStream
import java.io.DataOutputStream
import java.io.GZIPInputStream
import java.io.GZIPOutputStream
import java.io.InputStream
import java.io.OutputStream
import java.nio.charset.StandardCharsets
import java.security.SecureRandom
import android.util.Base64
import javax.crypto.AEADBadTagException
import javax.crypto.Cipher
import javax.crypto.CipherInputStream
import javax.crypto.CipherOutputStream
import javax.crypto.spec.GCMParameterSpec
import javax.crypto.spec.SecretKeySpec

/**
 * Portable, passphrase-recoverable encryption for My Diary cloud snapshots.
 *
 * The caller must write encrypted output to a temporary file and atomically
 * promote it only after encrypt() returns. Likewise, decrypt() output must be
 * staged and discarded unless the whole method returns successfully.
 *
 * No access token, passphrase, plaintext or attachment data is logged here.
 */
internal object DiaryBackupCrypto {
    private val MAGIC = "MYDIARYBKP1".toByteArray(StandardCharsets.US_ASCII)
    private const val FORMAT_VERSION = 1
    private const val SNAPSHOT_SCHEMA = 1
    private const val KDF_ID = "argon2id"
    private const val KDF_VERSION = 19 // Argon2 v1.3
    private const val MEMORY_KIB = 19_456
    private const val ITERATIONS = 2
    private const val PARALLELISM = 1
    private const val KEY_BYTES = 32
    private const val SALT_BYTES = 16
    private const val NONCE_BYTES = 12
    private const val GCM_TAG_BITS = 128
    private const val MAX_PASSPHRASE_CHARS = 1024
    private const val MAX_HEADER_BYTES = 16 * 1024
    private const val MAX_PLAINTEXT_BYTES = 512L * 1024L * 1024L
    private const val BUFFER_BYTES = 64 * 1024
    private val random = SecureRandom()

    fun encrypt(input: InputStream, output: OutputStream, passphrase: CharArray) {
        validatePassphrase(passphrase)
        val passwordCopy = passphrase.copyOf()
        val salt = ByteArray(SALT_BYTES).also(random::nextBytes)
        val wrapNonce = ByteArray(NONCE_BYTES).also(random::nextBytes)
        val payloadNonce = ByteArray(NONCE_BYTES).also(random::nextBytes)
        val dek = ByteArray(KEY_BYTES).also(random::nextBytes)
        var kek: ByteArray? = null
        try {
            val derivedKek = deriveKey(passwordCopy, salt)
            kek = derivedKek
            val wrappedDek = aesGcm(Cipher.ENCRYPT_MODE, derivedKek, wrapNonce, dek, wrapAad(salt, wrapNonce))
            val metadata = JSONObject()
                .put("format", "MY_DIARY_CLOUD_BACKUP")
                .put("formatVersion", FORMAT_VERSION)
                .put("snapshotSchema", SNAPSHOT_SCHEMA)
                .put("compression", "gzip")
                .put("payloadCipher", "AES-256-GCM")
                .put("kdf", KDF_ID)
                .put("kdfVersion", KDF_VERSION)
                .put("memoryKiB", MEMORY_KIB)
                .put("iterations", ITERATIONS)
                .put("parallelism", PARALLELISM)
                .put("salt", b64(salt))
                .put("wrapNonce", b64(wrapNonce))
                .put("wrappedDek", b64(wrappedDek))
                .put("payloadNonce", b64(payloadNonce))
            val header = metadata.toString().toByteArray(StandardCharsets.UTF_8)
            require(header.size in 1..MAX_HEADER_BYTES) { "Backup header is too large" }

            val data = DataOutputStream(BufferedOutputStream(output))
            data.write(MAGIC)
            data.writeInt(header.size)
            data.write(header)
            data.flush()

            val cipher = Cipher.getInstance("AES/GCM/NoPadding")
            cipher.init(Cipher.ENCRYPT_MODE, SecretKeySpec(dek, "AES"), GCMParameterSpec(GCM_TAG_BITS, payloadNonce))
            cipher.updateAAD(payloadAad(header))
            val cipherOut = CipherOutputStream(data, cipher)
            val gzipOut = GZIPOutputStream(BufferedOutputStream(cipherOut), BUFFER_BYTES)
            copyLimited(input, gzipOut, MAX_PLAINTEXT_BYTES)
            gzipOut.finish()
            gzipOut.close()
        } finally {
            passwordCopy.fill('\u0000')
            salt.fill(0)
            wrapNonce.fill(0)
            payloadNonce.fill(0)
            dek.fill(0)
            kek?.fill(0)
        }
    }

    fun decrypt(input: InputStream, output: OutputStream, passphrase: CharArray) {
        validatePassphrase(passphrase)
        val passwordCopy = passphrase.copyOf()
        var salt: ByteArray? = null
        var wrapNonce: ByteArray? = null
        var payloadNonce: ByteArray? = null
        var wrappedDek: ByteArray? = null
        var dek: ByteArray? = null
        var kek: ByteArray? = null
        try {
            val data = DataInputStream(BufferedInputStream(input))
            val magic = ByteArray(MAGIC.size)
            data.readFully(magic)
            if (!magic.contentEquals(MAGIC)) throw SecurityException("This is not a My Diary encrypted backup.")
            val headerSize = data.readInt()
            if (headerSize !in 1..MAX_HEADER_BYTES) throw SecurityException("Backup header is invalid.")
            val header = ByteArray(headerSize)
            data.readFully(header)
            val metadata = JSONObject(String(header, StandardCharsets.UTF_8))
            if (metadata.optString("format") != "MY_DIARY_CLOUD_BACKUP" ||
                metadata.optInt("formatVersion", -1) != FORMAT_VERSION ||
                metadata.optInt("snapshotSchema", -1) != SNAPSHOT_SCHEMA ||
                metadata.optString("compression") != "gzip" ||
                metadata.optString("payloadCipher") != "AES-256-GCM" ||
                metadata.optString("kdf") != KDF_ID ||
                metadata.optInt("kdfVersion", -1) != KDF_VERSION ||
                metadata.optInt("memoryKiB", -1) != MEMORY_KIB ||
                metadata.optInt("iterations", -1) != ITERATIONS ||
                metadata.optInt("parallelism", -1) != PARALLELISM
            ) throw SecurityException("Backup format or security parameters are not supported.")

            val saltBytes = decodeB64(metadata.getString("salt"), SALT_BYTES)
            salt = saltBytes
            val wrapNonceBytes = decodeB64(metadata.getString("wrapNonce"), NONCE_BYTES)
            wrapNonce = wrapNonceBytes
            val wrappedDekBytes = decodeB64(metadata.getString("wrappedDek"), KEY_BYTES + 16)
            wrappedDek = wrappedDekBytes
            val payloadNonceBytes = decodeB64(metadata.getString("payloadNonce"), NONCE_BYTES)
            payloadNonce = payloadNonceBytes
            val derivedKek = deriveKey(passwordCopy, saltBytes)
            kek = derivedKek
            val unwrappedDek = try {
                aesGcm(Cipher.DECRYPT_MODE, derivedKek, wrapNonceBytes, wrappedDekBytes, wrapAad(saltBytes, wrapNonceBytes))
            } catch (_: AEADBadTagException) {
                throw SecurityException("Recovery passphrase galat hai ya backup damaged hai.")
            }
            dek = unwrappedDek
            if (unwrappedDek.size != KEY_BYTES) throw SecurityException("Backup encryption key is invalid.")

            val cipher = Cipher.getInstance("AES/GCM/NoPadding")
            cipher.init(Cipher.DECRYPT_MODE, SecretKeySpec(unwrappedDek, "AES"), GCMParameterSpec(GCM_TAG_BITS, payloadNonceBytes))
            cipher.updateAAD(payloadAad(header))
            val cipherIn = CipherInputStream(data, cipher)
            GZIPInputStream(BufferedInputStream(cipherIn), BUFFER_BYTES).use { gzipIn ->
                copyLimited(gzipIn, output, MAX_PLAINTEXT_BYTES)
            }
            output.flush()
        } catch (error: SecurityException) {
            throw error
        } catch (error: Exception) {
            throw SecurityException("Backup verify/decrypt nahi ho saka. Current Diary data ko change na karein.", error)
        } finally {
            passwordCopy.fill('\u0000')
            salt?.fill(0)
            wrapNonce?.fill(0)
            payloadNonce?.fill(0)
            wrappedDek?.fill(0)
            dek?.fill(0)
            kek?.fill(0)
        }
    }

    private fun validatePassphrase(passphrase: CharArray) {
        require(passphrase.size in 12..MAX_PASSPHRASE_CHARS) {
            "Recovery passphrase kam se kam 12 characters ki honi chahiye."
        }
    }

    private fun deriveKey(passphrase: CharArray, salt: ByteArray): ByteArray {
        val parameters = Argon2Parameters.Builder(Argon2Parameters.ARGON2_id)
            .withVersion(Argon2Parameters.ARGON2_VERSION_13)
            .withMemoryAsKB(MEMORY_KIB)
            .withIterations(ITERATIONS)
            .withParallelism(PARALLELISM)
            .withSalt(salt)
            .build()
        val generator = Argon2BytesGenerator()
        generator.init(parameters)
        return ByteArray(KEY_BYTES).also { generator.generateBytes(passphrase, it) }
    }

    private fun aesGcm(
        mode: Int,
        key: ByteArray,
        nonce: ByteArray,
        input: ByteArray,
        aad: ByteArray
    ): ByteArray {
        val cipher = Cipher.getInstance("AES/GCM/NoPadding")
        cipher.init(mode, SecretKeySpec(key, "AES"), GCMParameterSpec(GCM_TAG_BITS, nonce))
        cipher.updateAAD(aad)
        return cipher.doFinal(input)
    }

    private fun wrapAad(salt: ByteArray, nonce: ByteArray): ByteArray =
        ("MyDiary|DEK-wrap|v1|argon2id|19|19456|2|1|" + b64(salt) + "|" + b64(nonce))
            .toByteArray(StandardCharsets.UTF_8)

    private fun payloadAad(header: ByteArray): ByteArray =
        MAGIC + "|payload|".toByteArray(StandardCharsets.US_ASCII) + header

    private fun b64(bytes: ByteArray): String = Base64.encodeToString(bytes, Base64.NO_WRAP)

    private fun decodeB64(value: String, expectedBytes: Int): ByteArray {
        val decoded = try { Base64.decode(value, Base64.DEFAULT) }
        catch (error: IllegalArgumentException) { throw SecurityException("Backup metadata encoding is invalid.", error) }
        if (decoded.size != expectedBytes) {
            decoded.fill(0)
            throw SecurityException("Backup metadata size is invalid.")
        }
        return decoded
    }

    private fun copyLimited(input: InputStream, output: OutputStream, maximum: Long) {
        val buffer = ByteArray(BUFFER_BYTES)
        var total = 0L
        try {
            while (true) {
                val count = input.read(buffer)
                if (count < 0) break
                total += count
                if (total > maximum) throw SecurityException("Backup data exceeds the safe size limit.")
                output.write(buffer, 0, count)
            }
        } finally {
            buffer.fill(0)
        }
    }
}
