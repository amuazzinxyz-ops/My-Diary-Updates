"use strict";
const fs = require("fs");
const vm = require("vm");
const source = fs.readFileSync(process.argv[2], "utf8");
const context = {
  window: {},
  Set, Promise, Object, Array, String, Number, Error, TextEncoder, Uint8Array,
  btoa: (s) => Buffer.from(s, "binary").toString("base64"),
  Blob,
  File: global.File,
  indexedDB: { open() { throw new Error("not used in static collector contract test"); } },
  localStorage: { length: 0, getItem() { return null; }, key() { return null; } },
  Date
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
console.log("PASS: collector parses, refuses to create missing databases, and preserves Diary Safety keys");
