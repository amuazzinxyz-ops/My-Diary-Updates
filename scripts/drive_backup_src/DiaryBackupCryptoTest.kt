package com.muazzin.diary.backup

import org.junit.Assert.assertArrayEquals
import org.junit.Assert.assertFalse
import org.junit.Assert.fail
import org.junit.Test
import java.io.ByteArrayInputStream
import java.io.ByteArrayOutputStream
import java.nio.charset.StandardCharsets

class DiaryBackupCryptoTest {
    private val passphrase = "correct horse battery staple".toCharArray()

    @Test
    fun encryptedSnapshotRoundTripsAndDoesNotExposePlaintext() {
        val original = ("My Diary private sample — notes, Kharcha, photos and reminders\n".repeat(2000))
            .toByteArray(StandardCharsets.UTF_8)
        val encrypted = ByteArrayOutputStream()
        DiaryBackupCrypto.encrypt(ByteArrayInputStream(original), encrypted, passphrase)
        val bytes = encrypted.toByteArray()
        assertFalse(String(bytes, StandardCharsets.ISO_8859_1).contains("My Diary private sample"))
        val restored = ByteArrayOutputStream()
        DiaryBackupCrypto.decrypt(ByteArrayInputStream(bytes), restored, passphrase)
        assertArrayEquals(original, restored.toByteArray())
    }

    @Test
    fun wrongPassphraseIsRejected() {
        val encrypted = ByteArrayOutputStream()
        DiaryBackupCrypto.encrypt(ByteArrayInputStream("secret".toByteArray()), encrypted, passphrase)
        try {
            DiaryBackupCrypto.decrypt(
                ByteArrayInputStream(encrypted.toByteArray()),
                ByteArrayOutputStream(),
                "another incorrect passphrase".toCharArray()
            )
            fail("Wrong passphrase must not decrypt the backup")
        } catch (_: SecurityException) {
            // Expected.
        }
    }

    @Test
    fun tamperedCiphertextIsRejected() {
        val encrypted = ByteArrayOutputStream()
        DiaryBackupCrypto.encrypt(ByteArrayInputStream("tamper test".toByteArray()), encrypted, passphrase)
        val bytes = encrypted.toByteArray()
        bytes[bytes.lastIndex] = (bytes.last().toInt() xor 1).toByte()
        try {
            DiaryBackupCrypto.decrypt(ByteArrayInputStream(bytes), ByteArrayOutputStream(), passphrase)
            fail("Modified ciphertext must fail authentication")
        } catch (_: SecurityException) {
            // Expected.
        } catch (_: java.io.IOException) {
            // CipherInputStream may surface an authentication failure as IOException.
        }
    }
}
