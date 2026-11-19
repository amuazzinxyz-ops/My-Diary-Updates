"use strict";
const fs = require("fs");
const vm = require("vm");
const source = fs.readFileSync(process.argv[2], "utf8");

function request(value) {
  const req = { result: value, error: null };
  Promise.resolve().then(() => { if (req.onsuccess) req.onsuccess(); });
  return req;
}
const storeData = {
  diary_me_features_v1: { records: [{ id: "note-1", kind: "documents", fileData: null }] },
  diary_private_locker_v1: { entries: [{ id: "locker-1", cipher: "ciphertext" }], meta: [{ id: "config", salt: "salt" }] },
  diary_diary_safety_v1: { snapshots: [{ notes: "[{\\\"id\\\":\\\"old\\\"}]", trash: "[]", savedAt: 123 }] }
};
const storeKeys = {
  diary_me_features_v1: { records: ["note-1"] },
  diary_private_locker_v1: { entries: ["locker-1"], meta: ["config"] },
  diary_diary_safety_v1: { snapshots: ["latest"] }
};
const fakeIndexedDB = {
  databases: async () => Object.keys(storeData).map(name => ({ name })),
  open(name, version) {
    const req = { result: null, error: null };
    Promise.resolve().then(() => {
      if (!storeData[name] || version !== 1) {
        req.error = new Error("unexpected database open");
        if (req.onerror) req.onerror();
        return;
      }
      req.result = {
        objectStoreNames: { contains: store => Object.prototype.hasOwnProperty.call(storeData[name], store) },
        transaction(storeName) {
          return { objectStore() {
            return {
              getAll: () => request(storeData[name][storeName]),
              getAllKeys: () => request(storeKeys[name][storeName])
            };
          }};
        },
        close() {}
      };
      if (req.onsuccess) req.onsuccess();
    });
    return req;
  }
};
const localValues = {
  diary_personal_notes_v1: "[]",
  diary_me_section_pin_v1_calendar: "protected"
};
const context = {
  window: {
    DiaryAppActions: {
      readNativeBackupPreferences() {
        return JSON.stringify({ items: "[]", auto_items: "[]" });
      }
    }
  },
  Set, Promise, Object, Array, String, Number, Error, TextEncoder, Uint8Array, Date, Blob,
  btoa: (value) => Buffer.from(value, "binary").toString("base64"),
  indexedDB: fakeIndexedDB,
  localStorage: {
    get length() { return Object.keys(localValues).length; },
    getItem(key) { return Object.prototype.hasOwnProperty.call(localValues, key) ? localValues[key] : null; },
    key(index) { return Object.keys(localValues)[index] || null; }
  },
};
vm.createContext(context);
vm.runInContext(source, context);
if (!context.window.MyDiaryCloudBackup || typeof context.window.MyDiaryCloudBackup.collectSnapshot !== "function") {
  throw new Error("Collector API was not registered");
}
if (!source.includes("indexedDB.databases()") || !source.includes('indexedDB.open(name, 1)') || !source.includes("onupgradeneeded")) {
  throw new Error("Collector must inspect existing databases and must not create missing ones");
}
if (!source.includes("store.getAllKeys()") ||
    !source.includes("__diaryBackupKey") ||
    !source.includes("__diaryBackupValue") ||
    !source.includes('dbName === "diary_diary_safety_v1"')) {
  throw new Error("Collector must preserve out-of-line Diary Safety record keys for restore");
}

(async function () {
  const collected = await context.window.MyDiaryCloudBackup.collectSnapshot();
  const safety = collected.snapshot.indexedDb.diary_diary_safety_v1.snapshots;
  if (safety.length !== 1 || safety[0].__diaryBackupKey !== "latest" ||
      !safety[0].__diaryBackupValue || safety[0].__diaryBackupValue.savedAt !== 123) {
    throw new Error("Diary Safety snapshot key/value pair was not preserved exactly");
  }
  const locker = collected.snapshot.indexedDb.diary_private_locker_v1;
  if (locker.entries[0].id !== "locker-1" || locker.meta[0].id !== "config") {
    throw new Error("Private Locker records were not collected");
  }
  if (collected.snapshot.localStorage.diary_me_section_pin_v1_calendar !== "protected") {
    throw new Error("Dynamic Me PIN/recovery localStorage key was not collected");
  }
  if (collected.snapshot.nativePreferences.diary_reminders_native_v1.items !== "[]") {
    throw new Error("Native reminder scheduler state was not collected");
  }
  console.log("PASS: collector preserves Diary Safety keys and collects Locker, dynamic localStorage, and native reminder state");
})().catch(error => { console.error(error); process.exitCode = 1; });
