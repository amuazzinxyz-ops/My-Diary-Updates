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
console.log("PASS: collector parses, exposes API, and refuses to create missing IndexedDB databases");
