package com.muazzin.diary.backup

/**
 * Canonical, versioned snapshot contract. The WebView collector must populate
 * every inventoried store; native-only biometric material and OAuth credentials
 * are deliberately outside this contract.
 */
internal object DiaryBackupSnapshot {
    const val SCHEMA_VERSION = 1
    const val MAX_RECORDS = 100_000
    const val MAX_DEPTH = 32
    const val MAX_ESTIMATED_BYTES = 512L * 1024L * 1024L

    private val localStorageKeys = setOf(
        "diary_personal_notes_v1",
        "diary_personal_notes_trash_v1",
        "diary_diary_master_pin_v1",
        "diary_diary_master_pattern_v1",
        "diary_diary_recovery_name_salt_v1",
        "diary_diary_recovery_name_hash_v1",
        "diaryDiaryMustChooseNewPinAfterRecovery",
        "diary_diary_note_font_v1",
        "diary_language_v204",
        "diary_interface_theme_v1",
        "diary_interface_custom_colour_v1",
        "diaryWorldClockCities",
        "diaryWorldClockFavourites"
    )
    private val indexedDbStores = mapOf(
        "diary_me_features_v1" to setOf("records"),
        "diary_private_locker_v1" to setOf("entries", "meta"),
        "diary_diary_safety_v1" to setOf("snapshots")
    )

    data class Report(val records: Int, val estimatedBytes: Long)

    /**
     * Validate a decoded JSON-like object before encryption or before any restore
     * staging. Accepted values are null, String, Boolean, Number, List and Map.
     */
    fun validate(root: Map<String, Any?>): Report {
        require(root.keys == setOf("schemaVersion", "createdAt", "localStorage", "indexedDb", "nativePreferences")) {
            "Backup snapshot fields are incomplete or unsupported."
        }
        require((root["schemaVersion"] as? Number)?.toInt() == SCHEMA_VERSION) {
            "Backup snapshot version is not supported."
        }
        require((root["createdAt"] as? Number)?.toLong()?.let { it > 0L } == true) {
            "Backup creation time is invalid."
        }

        val local = root["localStorage"] as? Map<*, *>
            ?: throw IllegalArgumentException("Backup localStorage section is missing.")
        for ((keyAny, value) in local) {
            val key = keyAny as? String ?: throw IllegalArgumentException("Invalid localStorage key.")
            val permitted = key in localStorageKeys ||
                key.matches(Regex("diary_me_section_(pin|recovery)_v1_(calendar|kharcha|documents|memories)"))
            require(permitted) { "Unsupported or device-bound localStorage key: $key" }
            require(value == null || value is String) { "localStorage values must remain strings." }
        }

        val dbs = root["indexedDb"] as? Map<*, *>
            ?: throw IllegalArgumentException("Backup IndexedDB section is missing.")
        require(dbs.keys.filterIsInstance<String>().toSet() == indexedDbStores.keys) {
            "Backup IndexedDB inventory is incomplete."
        }

        var recordCount = 0
        var estimatedBytes = 0L
        for ((dbName, expectedStores) in indexedDbStores) {
            val db = dbs[dbName] as? Map<*, *>
                ?: throw IllegalArgumentException("IndexedDB database $dbName is missing.")
            require(db.keys.filterIsInstance<String>().toSet() == expectedStores) {
                "IndexedDB store inventory is incomplete for $dbName."
            }
            for (storeName in expectedStores) {
                val records = db[storeName] as? List<*>
                    ?: throw IllegalArgumentException("IndexedDB store $storeName is invalid.")
                recordCount += records.size
                require(recordCount <= MAX_RECORDS) { "Backup contains too many records." }
                records.forEach { record ->
                    require(record is Map<*, *>) { "IndexedDB records must be objects." }
                    estimatedBytes += measure(record, 0)
                    require(estimatedBytes <= MAX_ESTIMATED_BYTES) { "Backup exceeds the safe size limit." }
                }
            }
        }

        val native = root["nativePreferences"] as? Map<*, *>
            ?: throw IllegalArgumentException("Native reminder state is missing.")
        require(native.keys.filterIsInstance<String>().toSet() == setOf("diary_reminders_native_v1")) {
            "Unsupported native preference section."
        }
        val reminders = native["diary_reminders_native_v1"] as? Map<*, *>
            ?: throw IllegalArgumentException("Native reminder state is invalid.")
        require(reminders.keys.filterIsInstance<String>().toSet() == setOf("items", "auto_items")) {
            "Native reminder scheduler state is incomplete."
        }
        reminders.values.forEach { value ->
            require(value == null || value is String) { "Native reminder values must remain strings." }
        }

        estimatedBytes += measure(local, 0) + measure(native, 0)
        require(estimatedBytes <= MAX_ESTIMATED_BYTES) { "Backup exceeds the safe size limit." }
        return Report(recordCount, estimatedBytes)
    }

    private fun measure(value: Any?, depth: Int): Long {
        require(depth <= MAX_DEPTH) { "Backup nesting is too deep." }
        return when (value) {
            null -> 4L
            is String -> value.toByteArray(Charsets.UTF_8).size.toLong()
            is Boolean, is Number -> 16L
            is ByteArray -> value.size.toLong()
            is List<*> -> value.sumOf { measure(it, depth + 1) }
            is Map<*, *> -> {
                var total = 0L
                for ((key, child) in value) {
                    val name = key as? String ?: throw IllegalArgumentException("Backup object key is invalid.")
                    val normalized = name.lowercase().replace("-", "_")
                    require(normalized !in setOf(
                        "access_token", "refresh_token", "authorization", "oauth",
                        "device_id", "fingerprint_key", "private_locker_biometric"
                    )) { "Device credentials cannot be included in a portable backup." }
                    total += name.toByteArray(Charsets.UTF_8).size + measure(child, depth + 1)
                    require(total <= MAX_ESTIMATED_BYTES) { "Backup exceeds the safe size limit." }
                }
                total
            }
            else -> throw IllegalArgumentException("Unsupported value in backup snapshot.")
        }
    }
}
