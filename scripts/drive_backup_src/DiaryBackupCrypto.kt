package com.muazzin.diary.backup

import org.bouncycastle.crypto.generators.Argon2BytesGenerator
import org.bouncycastle.crypto.params.Argon2Parameters
import java.io.BufferedInputStream
import java.io.BufferedOutputStream
import java.io.DataInputStream
import java.io.DataOutputStream
import java.io.GZIPInputStream
import java.io.GZIPOutputStream
import java.io.InputStream
import java.io.OutputStream
import java.nio.ByteBuffer
import java.nio.ByteOrder
import java.nio.charset.StandardCharsets
import java.security.SecureRandom
import javax.crypto.AEADBadTagException
import javax.crypto.Cipher
import javax.crypto.CipherInputStream
import javax.crypto.CipherOutputStream
import javax.crypto.spec.GCMParameterSpec
import javax.crypto.spec.SecretKeySpec

/**
 * Portable, passphrase-recoverable encryption for My Diary cloud snapshots.
 *
 * Binary envelope: fixed authenticated header followed by AES-GCM ciphertext.
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
    private const val KDF_VERSION = 19 // Argon2 v1.3
    private const val MEMORY_KIB = 19_456
    private const val ITERATIONS = 2
    private const val PARALLELISM = 1
    private const val KEY_BYTES = 32
    private const val SALT_BYTES = 16
    private const val NONCE_BYTES = 12
    private const val GCM_TAG_BITS = 128
    private const val MAX_PASSPHRASE_CHARS = 1024
    private const val MAX_PLAINTEXT_BYTES = 512L * 1024L * 1024L
    private const val BUFFER_BYTES = 64 * 1024
    private val HEADER_BYTES = MAGIC.size + (6 * 4) + SALT_BYTES + NONCE_BYTES + (KEY_BYTES + 16) + NONCE_BYTES
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
            val header = ByteBuffer.allocate(HEADER_BYTES).order(ByteOrder.BIG_ENDIAN)
                .put(MAGIC)
                .putInt(FORMAT_VERSION)
                .putInt(SNAPSHOT_SCHEMA)
                .putInt(KDF_VERSION)
                .putInt(MEMORY_KIB)
                .putInt(ITERATIONS)
                .putInt(PARALLELISM)
                .put(salt)
                .put(wrapNonce)
                .put(wrappedDek)
                .put(payloadNonce)
                .array()

            val data = DataOutputStream(BufferedOutputStream(output))
            data.write(header)
            data.flush()

            val cipher = Cipher.getInstance("AES/GCM/NoPadding")
            cipher.init(Cipher.ENCRYPT_MODE, SecretKeySpec(dek, "AES"), GCMParameterSpec(GCM_TAG_BITS, payloadNonce))
            cipher.updateAAD(payloadAad(header))
            val cipherOut = CipherOutputStream(data, cipher)
            val gzipOut = GZIPOutputStream(BufferedOutputStream(cipherOut), BUFFER_BYTES)
            try {
                copyLimited(input, gzipOut, MAX_PLAINTEXT_BYTES)
                gzipOut.finish()
            } finally {
                gzipOut.close()
            }
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
            val header = ByteArray(HEADER_BYTES)
            data.readFully(header)
            val buffer = ByteBuffer.wrap(header).order(ByteOrder.BIG_ENDIAN)
            val magic = ByteArray(MAGIC.size)
            buffer.get(magic)
            if (!magic.contentEquals(MAGIC)) throw SecurityException("This is not a My Diary encrypted backup.")
            if (buffer.int != FORMAT_VERSION ||
                buffer.int != SNAPSHOT_SCHEMA ||
                buffer.int != KDF_VERSION ||
                buffer.int != MEMORY_KIB ||
                buffer.int != ITERATIONS ||
                buffer.int != PARALLELISM
            ) throw SecurityException("Backup format or security parameters are not supported.")

            val saltBytes = ByteArray(SALT_BYTES)
            buffer.get(saltBytes)
            salt = saltBytes
            val wrapNonceBytes = ByteArray(NONCE_BYTES)
            buffer.get(wrapNonceBytes)
            wrapNonce = wrapNonceBytes
            val wrappedDekBytes = ByteArray(KEY_BYTES + 16)
            buffer.get(wrappedDekBytes)
            wrappedDek = wrappedDekBytes
            val payloadNonceBytes = ByteArray(NONCE_BYTES)
            buffer.get(payloadNonceBytes)
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
            val cipherBuffer = BufferedInputStream(cipherIn)
            val gzipIn = GZIPInputStream(cipherBuffer, BUFFER_BYTES)
            try {
                copyLimited(gzipIn, output, MAX_PLAINTEXT_BYTES)
                // Force AES-GCM to reach its end-of-stream tag check. GZIP may
                // stop at its member trailer before consuming the cipher stream.
                val drain = ByteArray(BUFFER_BYTES)
                try {
                    while (cipherBuffer.read(drain) >= 0) { }
                } finally {
                    drain.fill(0)
                }
            } finally {
                gzipIn.close()
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
        "MyDiary|DEK-wrap|v1|argon2id|19|19456|2|1|".toByteArray(StandardCharsets.US_ASCII) + salt + nonce

    private fun payloadAad(header: ByteArray): ByteArray =
        MAGIC + "|payload|".toByteArray(StandardCharsets.US_ASCII) + header

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
