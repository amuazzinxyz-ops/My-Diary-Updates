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
    fun cachedKeyCanEncryptMultipleBackupsWithPortablePassphraseEnvelope() {
        val originalOne = "first backup".toByteArray(StandardCharsets.UTF_8)
        val originalTwo = "second backup with newer diary data".toByteArray(StandardCharsets.UTF_8)
        var cachedKey: ByteArray? = null
        var salt: ByteArray? = null
        var wrapNonce: ByteArray? = null
        var wrappedDek: ByteArray? = null
        try {
            val first = ByteArrayOutputStream()
            DiaryBackupCrypto.encrypt(ByteArrayInputStream(originalOne), first, passphrase) { key, s, n, wrapped ->
                cachedKey = key; salt = s; wrapNonce = n; wrappedDek = wrapped
            }
            val second = ByteArrayOutputStream()
            DiaryBackupCrypto.encryptWithCachedDataKey(
                ByteArrayInputStream(originalTwo), second,
                cachedKey!!, salt!!, wrapNonce!!, wrappedDek!!
            )
            val restoredOne = ByteArrayOutputStream()
            DiaryBackupCrypto.decrypt(ByteArrayInputStream(first.toByteArray()), restoredOne, passphrase)
            val restoredTwo = ByteArrayOutputStream()
            DiaryBackupCrypto.decrypt(ByteArrayInputStream(second.toByteArray()), restoredTwo, passphrase)
            assertArrayEquals(originalOne, restoredOne.toByteArray())
            assertArrayEquals(originalTwo, restoredTwo.toByteArray())
            // Each backup must have a different payload nonce even though its DEK is reused.
            val nonceOffset = "MYDIARYBKP1".length + (6 * 4) + 16 + 12 + 48
            val firstNonce = first.toByteArray().copyOfRange(nonceOffset, nonceOffset + 12)
            val secondNonce = second.toByteArray().copyOfRange(nonceOffset, nonceOffset + 12)
            assertFalse(firstNonce.contentEquals(secondNonce))
        } finally {
            cachedKey?.fill(0); salt?.fill(0); wrapNonce?.fill(0); wrappedDek?.fill(0)
        }
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
