(function () {
  "use strict";
  var MAX_BYTES = 64 * 1024 * 1024;
  var buttonId = "diaryGoogleDriveBackupBtn";
  var modalId = "diaryGoogleDriveBackupModal";

  function make(tag, attrs, text) {
    var node = document.createElement(tag);
    Object.keys(attrs || {}).forEach(function (key) {
      if (key === "style") Object.assign(node.style, attrs[key]);
      else node.setAttribute(key, attrs[key]);
    });
    if (text !== undefined) node.textContent = text;
    return node;
  }

  function install() {
    var panel = document.getElementById("diaryDiaryMePanel");
    if (!panel || document.getElementById(buttonId)) return;
    var button = make("button", {
      id: buttonId, type: "button",
      style: { display: "block", width: "100%", marginTop: "12px", padding: "13px 16px",
        borderRadius: "14px", border: "2px solid #c5a34a", background: "linear-gradient(145deg,#fff8df,#f0d58b)",
        color: "#39280a", fontWeight: "900", fontSize: "16px", boxShadow: "0 4px 0 #98772e,0 7px 14px rgba(0,0,0,.16)" }
    }, "☁️ Google Drive Backup");
    panel.appendChild(button);
    button.addEventListener("click", function (event) {
      event.preventDefault();
      event.stopPropagation();
      showModal();
    });
  }

  function showModal() {
    var existing = document.getElementById(modalId);
    if (existing) { existing.style.display = "flex"; return; }
    var overlay = make("div", { id: modalId, role: "presentation", style: {
      position: "fixed", inset: "0", zIndex: "2147483647", display: "flex",
      alignItems: "center", justifyContent: "center", padding: "18px",
      background: "rgba(0,0,0,.72)", boxSizing: "border-box"
    }});
    var box = make("section", { role: "dialog", "aria-modal": "true", "aria-labelledby": "diaryDriveTitle",
      style: { width: "100%", maxWidth: "440px", maxHeight: "90vh", overflowY: "auto",
        background: "#fff", color: "#211a2c", borderRadius: "18px", padding: "20px",
        boxSizing: "border-box", boxShadow: "0 12px 40px rgba(0,0,0,.35)" }});
    var title = make("h2", { id: "diaryDriveTitle", style: { margin: "0 0 10px", fontSize: "21px" }}, "☁️ Google Drive Encrypted Backup");
    var explain = make("p", { style: { lineHeight: "1.5", fontSize: "14px" }},
      "Aapki Diary pehle phone par encrypt hogi, phir Google Drive ke private app folder mein upload hogi. Passphrase Google ya My Diary mein save nahi hogi. Ise bhool gaye to backup restore nahi ho sakega. Kam se kam 12 characters ka passphrase yaad rakhein.");
    var pass = make("input", { type: "password", id: "diaryDrivePassphrase", autocomplete: "new-password",
      placeholder: "Naya backup passphrase", minlength: "12", required: "required",
      style: { display: "block", width: "100%", boxSizing: "border-box", padding: "13px",
        border: "1px solid #9b91a8", borderRadius: "10px", margin: "12px 0", fontSize: "16px" }});
    var confirm = make("input", { type: "password", id: "diaryDrivePassphraseConfirm", autocomplete: "new-password",
      placeholder: "Passphrase dobara likhein", minlength: "12", required: "required",
      style: { display: "block", width: "100%", boxSizing: "border-box", padding: "13px",
        border: "1px solid #9b91a8", borderRadius: "10px", margin: "12px 0", fontSize: "16px" }});
    var status = make("p", { role: "status", "aria-live": "polite",
      style: { minHeight: "42px", lineHeight: "1.4", fontSize: "14px", fontWeight: "700" }}, "");
    var actions = make("div", { style: { display: "flex", gap: "10px", marginTop: "12px" }});
    var cancel = make("button", { type: "button", style: { flex: "1", padding: "12px",
      border: "1px solid #aaa", borderRadius: "10px", background: "#f3f1f5", fontWeight: "800" }}, "Cancel");
    var submit = make("button", { type: "button", style: { flex: "1", padding: "12px",
      border: "0", borderRadius: "10px", background: "#315d3c", color: "#fff", fontWeight: "900" }}, "Encrypt & Backup");
    actions.append(cancel, submit);
    box.append(title, explain, pass, confirm, status, actions);
    overlay.appendChild(box);
    overlay.addEventListener("click", function (e) { if (e.target === overlay && !submit.disabled) overlay.remove(); });
    cancel.addEventListener("click", function () { if (!submit.disabled) overlay.remove(); });
    submit.addEventListener("click", async function () {
      var password = pass.value;
      if (password.length < 12) { status.textContent = "Passphrase kam se kam 12 characters ka rakhein."; return; }
      if (password !== confirm.value) { status.textContent = "Dono passphrase ek jaise nahi hain."; return; }
      var bridge = window.DiaryAppActions;
      if (!bridge || typeof bridge.encryptDiaryBackupSnapshot !== "function" ||
          typeof bridge.uploadEncryptedDiaryBackup !== "function") {
        status.textContent = "Is feature ke liye My Diary ka naya Android app version chahiye.";
        return;
      }
      if (!window.MyDiaryCloudBackup || typeof window.MyDiaryCloudBackup.collectSnapshot !== "function") {
        status.textContent = "Backup collector load nahi hua. App ko dobara kholkar koshish karein.";
        return;
      }
      submit.disabled = true; cancel.disabled = true;
      status.textContent = "Diary data check aur backup taiyaar ho raha hai…";
      try {
        var snapshot = await window.MyDiaryCloudBackup.collectSnapshot();
        if (!snapshot || !snapshot.serialized || snapshot.byteLength < 1 || snapshot.byteLength > MAX_BYTES) {
          throw new Error("Backup size 64 MiB ki current limit se zyada hai.");
        }
        status.textContent = "Phone par encrypted backup ban raha hai…";
        var encrypted = JSON.parse(bridge.encryptDiaryBackupSnapshot(snapshot.serialized, password, snapshot.byteLength));
        password = "";
        pass.value = ""; confirm.value = "";
        snapshot.serialized = ""; snapshot.snapshot = null;
        if (!encrypted || encrypted.ok !== true || typeof encrypted.fileName !== "string") {
          throw new Error(encrypted && encrypted.message ? encrypted.message : "Encryption fail hui.");
        }
        status.textContent = "Google account permission khul rahi hai…";
        window.__diaryDriveBackupResult = function (result) {
          var success = !!(result && result.ok);
          status.textContent = result && result.message ? result.message : (success ? "Backup save ho gaya." : "Backup upload nahi hua.");
          submit.disabled = false; cancel.disabled = false;
          submit.textContent = success ? "Backup Complete" : "Dobara Koshish";
        };
        bridge.uploadEncryptedDiaryBackup(encrypted.fileName);
      } catch (error) {
        password = ""; pass.value = ""; confirm.value = "";
        status.textContent = "Backup nahi bana: " + String(error && error.message || error);
        submit.disabled = false; cancel.disabled = false;
      }
    });
    document.body.appendChild(overlay);
    pass.focus();
  }

  function boot() {
    install();
    if (window.MutationObserver && document.body) {
      var observer = new MutationObserver(install);
      observer.observe(document.body, { childList: true, subtree: true });
    }
    window.addEventListener("diary-language-change", install);
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot);
  else boot();
})();