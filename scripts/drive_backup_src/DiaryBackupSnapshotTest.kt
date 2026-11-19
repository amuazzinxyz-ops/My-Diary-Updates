package com.muazzin.diary.backup

import org.junit.Assert.assertEquals
import org.junit.Assert.fail
import org.junit.Test

class DiaryBackupSnapshotTest {
    private fun validSnapshot(): Map<String, Any?> = mapOf(
        "schemaVersion" to 1,
        "createdAt" to 1_800_000_000_000L,
        "localStorage" to mapOf(
            "diary_personal_notes_v1" to "[]",
            "diary_personal_notes_trash_v1" to "[]",
            "diary_me_section_pin_v1_kharcha" to "protected"
        ),
        "indexedDb" to mapOf(
            "diary_me_features_v1" to mapOf("records" to listOf(mapOf("id" to "1", "kind" to "kharcha"))),
            "diary_private_locker_v1" to mapOf("entries" to emptyList<Any>(), "meta" to emptyList<Any>()),
            "diary_diary_safety_v1" to mapOf("snapshots" to emptyList<Any>())
        ),
        "nativePreferences" to mapOf(
            "diary_reminders_native_v1" to mapOf("items" to "[]", "auto_items" to "[]")
        )
    )

    @Test
    fun acceptsCompleteInventoriedSnapshot() {
        val report = DiaryBackupSnapshot.validate(validSnapshot())
        assertEquals(1, report.records)
    }

    @Test
    fun rejectsMissingDatabaseOrStore() {
        val broken = validSnapshot().toMutableMap()
        broken["indexedDb"] = mapOf("diary_me_features_v1" to mapOf("records" to emptyList<Any>()))
        try {
            DiaryBackupSnapshot.validate(broken)
            fail("Incomplete store inventory must be rejected")
        } catch (_: IllegalArgumentException) { }
    }

    @Test
    fun rejectsDeviceBoundOrOAuthMaterial() {
        val broken = validSnapshot().toMutableMap()
        broken["localStorage"] = mapOf("diary_fingerprint_unlock_enabled_v1" to "true")
        try {
            DiaryBackupSnapshot.validate(broken)
            fail("Device-bound fingerprint state must not be portable")
        } catch (_: IllegalArgumentException) { }

        val withToken = validSnapshot().toMutableMap()
        withToken["indexedDb"] = mapOf(
            "diary_me_features_v1" to mapOf("records" to listOf(mapOf("access_token" to "secret"))),
            "diary_private_locker_v1" to mapOf("entries" to emptyList<Any>(), "meta" to emptyList<Any>()),
            "diary_diary_safety_v1" to mapOf("snapshots" to emptyList<Any>())
        )
        try {
            DiaryBackupSnapshot.validate(withToken)
            fail("OAuth material must not enter a backup")
        } catch (_: IllegalArgumentException) { }
    }

    @Test
    fun rejectsNonStringInventoryKeys() {
        val broken = validSnapshot().toMutableMap()
        broken["indexedDb"] = mapOf(
            "diary_me_features_v1" to mapOf("records" to emptyList<Any>(), 7 to "unexpected"),
            "diary_private_locker_v1" to mapOf("entries" to emptyList<Any>(), "meta" to emptyList<Any>()),
            "diary_diary_safety_v1" to mapOf("snapshots" to emptyList<Any>())
        )
        try {
            DiaryBackupSnapshot.validate(broken)
            fail("Non-string inventory keys must be rejected")
        } catch (_: IllegalArgumentException) { }
    }

    @Test
    fun rejectsCamelCaseOAuthAndDeviceCredentials() {
        val forbiddenKeys = listOf("accessToken", "refreshToken", "deviceId", "fingerprintKey")
        for (key in forbiddenKeys) {
            val broken = validSnapshot().toMutableMap()
            broken["indexedDb"] = mapOf(
                "diary_me_features_v1" to mapOf("records" to listOf(mapOf(key to "must-not-export"))),
                "diary_private_locker_v1" to mapOf("entries" to emptyList<Any>(), "meta" to emptyList<Any>()),
                "diary_diary_safety_v1" to mapOf("snapshots" to emptyList<Any>())
            )
            try {
                DiaryBackupSnapshot.validate(broken)
                fail("$key must not enter a portable backup")
            } catch (_: IllegalArgumentException) { }
        }
    }

    @Test
    fun rejectsExcessiveNesting() {
        var nested: Any = "x"
        repeat(DiaryBackupSnapshot.MAX_DEPTH + 2) { nested = listOf(nested) }
        val broken = validSnapshot().toMutableMap()
        broken["indexedDb"] = mapOf(
            "diary_me_features_v1" to mapOf("records" to listOf(mapOf("data" to nested))),
            "diary_private_locker_v1" to mapOf("entries" to emptyList<Any>(), "meta" to emptyList<Any>()),
            "diary_diary_safety_v1" to mapOf("snapshots" to emptyList<Any>())
        )
        try {
            DiaryBackupSnapshot.validate(broken)
            fail("Excessive nesting must be rejected")
        } catch (_: IllegalArgumentException) { }
    }
}
