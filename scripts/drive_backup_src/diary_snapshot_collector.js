(function (global) {
  "use strict";
  const MAX_BYTES = 64 * 1024 * 1024;
  const LOCAL_KEYS = new Set([
    "diary_personal_notes_v1", "diary_personal_notes_trash_v1",
    "diary_diary_master_pin_v1", "diary_diary_master_pattern_v1",
    "diary_diary_recovery_name_salt_v1", "diary_diary_recovery_name_hash_v1",
    "diaryDiaryMustChooseNewPinAfterRecovery", "diary_diary_note_font_v1",
    "diary_language_v204", "diary_interface_theme_v1",
    "diary_interface_custom_colour_v1", "diaryWorldClockCities",
    "diaryWorldClockFavourites"
  ]);
  const DYNAMIC_KEY = /^diary_me_section_(?:pin|recovery)_v1_(?:calendar|kharcha|documents|memories)$/;
  const DATABASES = {
    diary_me_features_v1: ["records"],
    diary_private_locker_v1: ["entries", "meta"],
    diary_diary_safety_v1: ["snapshots"]
  };

  function requestResult(request) {
    return new Promise((resolve, reject) => {
      request.onsuccess = () => resolve(request.result);
      request.onerror = () => reject(request.error || new Error("IndexedDB request failed"));
    });
  }
  function openDatabase(name) {
    return new Promise((resolve, reject) => {
      // Known v1 only: abort on upgrade so a missing DB is never silently created.
      const request = indexedDB.open(name, 1);
      request.onsuccess = () => resolve(request.result);
      request.onerror = () => reject(request.error || new Error("IndexedDB open failed: " + name));
      request.onblocked = () => reject(new Error("IndexedDB is blocked: " + name));
      request.onupgradeneeded = () => {
        try { if (request.transaction) request.transaction.abort(); } catch (_) {}
        reject(new Error("Required Diary database is missing or has an unexpected schema: " + name));
      };
    });
  }
  async function blobValue(blob) {
    const bytes = new Uint8Array(await blob.arrayBuffer());
    let binary = "";
    const chunk = 0x8000;
    for (let i = 0; i < bytes.length; i += chunk) {
      binary += String.fromCharCode.apply(null, bytes.subarray(i, i + chunk));
    }
    const result = { __diaryBackupType: "Blob", mimeType: blob.type || "application/octet-stream", base64: btoa(binary) };
    if (typeof File !== "undefined" && blob instanceof File) {
      result.fileName = blob.name;
      result.lastModified = blob.lastModified;
    }
    return result;
  }
  async function portable(value, depth) {
    if (depth > 32) throw new Error("Backup data nesting is too deep.");
    if (value instanceof Blob) return blobValue(value);
    if (Array.isArray(value)) {
      const out = [];
      for (const item of value) out.push(await portable(item, depth + 1));
      return out;
    }
    if (value && typeof value === "object") {
      const out = {};
      for (const key of Object.keys(value)) out[key] = await portable(value[key], depth + 1);
      return out;
    }
    if (value === null || ["string", "number", "boolean"].includes(typeof value)) return value;
    throw new Error("Unsupported data type in Diary backup.");
  }
  async function readStore(db, storeName) {
    if (!db.objectStoreNames.contains(storeName)) throw new Error("Backup store missing: " + storeName);
    const tx = db.transaction(storeName, "readonly");
    const result = await requestResult(tx.objectStore(storeName).getAll());
    return portable(result, 0);
  }
  async function collectSnapshot() {
    const localStorageData = {};
    for (const key of LOCAL_KEYS) localStorageData[key] = localStorage.getItem(key);
    for (let i = 0; i < localStorage.length; i++) {
      const key = localStorage.key(i);
      if (DYNAMIC_KEY.test(key)) localStorageData[key] = localStorage.getItem(key);
    }

    if (typeof indexedDB.databases !== "function") {
      throw new Error("This Android WebView cannot safely inspect existing Diary databases.");
    }
    const existingDatabases = await indexedDB.databases();
    const existingNames = new Set(existingDatabases.map(item => item.name));
    for (const dbName of Object.keys(DATABASES)) {
      if (!existingNames.has(dbName)) throw new Error("Required Diary database is missing: " + dbName);
    }

    const indexedDb = {};
    for (const [dbName, stores] of Object.entries(DATABASES)) {
      const db = await openDatabase(dbName);
      try {
        const data = {};
        for (const storeName of stores) data[storeName] = await readStore(db, storeName);
        indexedDb[dbName] = data;
      } finally {
        db.close();
      }
    }

    const bridge = global.DiaryAppActions;
    if (!bridge || typeof bridge.readNativeBackupPreferences !== "function") {
      throw new Error("Native reminder backup bridge is unavailable.");
    }
    const nativePrefs = JSON.parse(bridge.readNativeBackupPreferences());
    const snapshot = {
      schemaVersion: 1,
      createdAt: Date.now(),
      localStorage: localStorageData,
      indexedDb,
      nativePreferences: { diary_reminders_native_v1: nativePrefs }
    };
    const serialized = JSON.stringify(snapshot);
    const byteLength = new TextEncoder().encode(serialized).byteLength;
    if (byteLength > MAX_BYTES) throw new Error("Backup is larger than the current safe 64 MiB limit.");
    return { snapshot, serialized, byteLength };
  }

  global.MyDiaryCloudBackup = Object.freeze({ collectSnapshot });
})(window);
