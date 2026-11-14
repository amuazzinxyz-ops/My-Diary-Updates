# MY DIARY — MANDATORY SAFE-WORK PROTOCOL (READ FIRST EVERY TASK)

**Status checked against live `latest.json` on 2026-11-14:** APK `1.0.143` / versionCode `142`; webVersion `201`; package `com.personal.diaryapp`. Live APK SHA-256 `4eccf17f61389bbb112a1daf910eb88d11315c19c22efa2d9e71171115688961`; web SHA-256 `5d0f47cca0424f0d9c31ce94e85a280caf38633ec53252f89951b85fb9f50686`.

**Project/repository:** `amuazzinxyz-ops/My-Diary-Updates`  
**This register:** `docs/PROJECT_MAP_AND_SECRETS_REGISTER.md`  
**Scope:** My Diary only. Never edit or inspect the separate MUAZZIN project for a My Diary task.

## A. Mandatory start gate — do not edit until complete

1. Read this register from the live default branch, including the newest entries and relevant historical notes.
2. Fetch the live `latest.json`; record APK version/versionCode, webVersion, APK URL and hashes. Do not rely on stale version numbers elsewhere in this document.
3. Inspect the current repository tree, recent commits, workflow status and the exact files/functions involved. Identify the latest successful/known-good state for the requested feature. If the live files, register, feed, or history disagree, STOP and reconcile before editing.
4. Confirm whether the request is web-only, native Android, build/workflow, or mixed. Do not change the wrong layer.
5. Write a short scope list: files/functions allowed to change, related dependencies to inspect, and features/files explicitly out of scope.
6. Create a timestamped backup of every file that will be edited, plus the live feed and this register when applicable. Verify the backup exists and is readable before editing. Never overwrite the only known-good backup.

## B. Change rules — preserve existing behaviour

1. Make only the user's explicitly requested change. Prefer the smallest isolated patch; do not refactor, redesign, rename, reorder, or clean up unrelated code.
2. Do not delete, replace, disable, or materially alter an existing feature, button, menu, updater path, data format, storage key, permission, package identity, signing identity, or recovery flow without explicit user approval.
3. Treat shared functions, global CSS, common event handlers, translations, storage and update code as high-impact dependencies. Inspect their callers and effects before changing them.
4. Preserve backward compatibility with existing notes, photos, backups, PIN/recovery records and stored user data. Never clear app data, uninstall the app, or change storage keys as a troubleshooting shortcut.
5. Do not bundle unrelated fixes into one release. If a new request reveals a separate issue, record it and ask/handle it as a separate task.
6. If a test fails or an unexpected difference appears, stop. Do not stack another speculative fix on top. Compare with the backup, isolate the cause, and restore the last known-good state when needed.

## C. Required verification before any publish

1. Review the complete diff against the pre-edit backup. Every changed line must be explainable by the user's request.
2. Run applicable checks: syntax/parse checks, HTML structure checks, targeted function checks, translation checks, data/storage compatibility checks, and automated tests/builds. Also inspect nearby features that share the changed code.
3. For web releases, fetch the final source and published mirror again and prove they are byte-identical. Independently calculate SHA-256 from the exact UTF-8 source bytes and verify it equals `latest.json.webSha256`. Do not copy a guessed or previously used hash.
4. For APK releases, verify debug and signed Release builds, package name, versionName/versionCode, APK SHA-256, live feed URL/hash, and the existing trusted signing-certificate fingerprint. Never regenerate, replace, expose, or modify signing secrets to make a build pass.
5. Verify the update workflow completed successfully and the feed points to the exact artifact that was checked. A queued, failed, cancelled, or partially completed workflow is NOT a published release.
6. Re-fetch every changed live file after writing. Confirm the expected commit/blob SHA, source/mirror/feed consistency, version metadata and backup paths.
7. Do not publish if any required check is missing, contradictory, or failing. Fix the cause or roll back first.

## D. Phone verification — report honestly

1. Automated checks and GitHub success do not prove that the app works on the user's phone.
2. Provide a short, relevant phone test list using the existing in-app route (normally **Me → Check for Updates**). Do not send the user to manual APK links when the in-app updater is the intended route.
3. Clearly separate: **code checked**, **build/workflow checked**, **live release checked**, and **physical-device test pending/confirmed**.
4. Never say “all fixed”, “100% working”, or “phone tested” unless the corresponding evidence exists. Record the user's actual phone-test result in the next register entry.

## E. Rollback and recovery

1. Keep the pre-change backup and last known-good commit/reference. Record exact paths and commit IDs.
2. If the update breaks an existing feature, stop further changes and compare the live code with the pre-change snapshot. Restore only the affected files from the verified last-known-good state; do not roll back unrelated good work.
3. After rollback, re-check source/mirror/feed/hash/version and test the recovery path. Do not claim recovery until verified.
4. Never delete backups, historical register entries, or signing records as part of routine cleanup.

## F. Register and release record

**MANDATORY SUCCESS-ENTRY RULE:** Whenever any requested work is completed successfully, immediately append a dated entry to this Master Register before reporting the work as complete. This applies to every successful task—not only published releases—including small UI fixes, code changes, translations, investigations that resolve an issue, configuration changes, and confirmed user/device test results. Record what was requested, what was actually completed, the evidence/checks, exact files or areas changed (or explicitly state no files changed), what was left untouched, and any pending limitations. If a task is not successful or remains incomplete, record its status honestly as pending/blocked/failed where useful; never write an unverified success claim. Do not rely on chat history as a substitute for the Register entry.

For every task, append a dated entry containing: user request; starting commit/version; exact files changed; exact behaviour changed; files/features deliberately untouched; backup paths; tests and results; workflow/run and commit IDs; source/mirror blob identity; independently verified SHA-256; feed values; APK/signing checks if applicable; rollback reference; and phone-test status. Mark unknown or untested items as **pending**, never as passed.

Keep historical entries as history. If an old entry contains stale version information, do not silently rewrite history; clearly identify the current live values near the top and state that `latest.json` is authoritative.

## G. Reusable task checklist — complete every time

- [ ] Correct project and repository confirmed (My Diary only)
- [ ] Master Register and live latest.json read
- [ ] Latest known-good commit/version identified
- [ ] Scope and dependencies inspected
- [ ] Pre-edit backups created and verified
- [ ] Only requested minimal change made
- [ ] Full diff reviewed; unrelated features preserved
- [ ] Relevant regression/syntax/data/build checks passed
- [ ] Source and mirror byte-identical (web change)
- [ ] Exact SHA-256 matches live feed (web change)
- [ ] APK version/hash/signing fingerprint verified (APK change)
- [ ] Workflow completed successfully
- [ ] Changed files re-fetched and live metadata verified
- [ ] **Successful work has a dated Master Register entry before completion is reported**
- [ ] Register updated with evidence and backup paths
- [ ] Phone-test status clearly marked; no unsupported success claim

**STOP RULE:** If any item required for the type of release cannot be verified, do not publish and do not describe the task as complete. Tell the user exactly what is blocked and preserve the last known-good version.


---

# Web Update 153 — Independent adjustment for each image (2026-11-13)

- User reported that adjusting one image prevented another image from being adjusted. Root cause: shared `diaryFingerAdjustKind` gated all document-level Pointer/Touch handlers, so only the most recently activated image kind could receive gestures.
- Starting state: Web Update 152; APK 1.0.136 / versionCode 135; package `com.personal.diaryapp`; prior source/mirror blob SHA `4ea139d2ca9ee04b72a31b1a9cbc712a3d87ca41`; prior feed SHA-256 `b3916ea90ea9f46a633a6e11fb47e89540f9ba2a17db7e7993f9cb2529ccef84`.
- Changed only `web-source/index.html`, source commit `5b591b65deb262efc0fd988c3530ce60948a5efe`. Removed the global active-kind gate from pointer and touch gesture handlers; each bound image now accepts gestures only when the pointer is inside its own bounds / belongs to its own tracked pointer IDs. Starting adjustment no longer disables the previously selected image. Photo preview is always gesture-enabled when present. Clearing/resetting a note removes adjustment styling from all active image targets. Existing per-image colour/position/zoom state and zoom limits remain unchanged.
- Pre-edit backup branch: `backup/pre-independent-image-adjustment-2026-11-13`; verified exact readable backups:
  - `backups/web-source-before-independent-image-adjustment-2026-11-13.html`
  - `backups/diary-web-before-independent-image-adjustment-2026-11-13.html`
  - `backups/latest-before-independent-image-adjustment-2026-11-13.json`
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-independent-image-adjustment-2026-11-13.md`
- Diff contained only the shared gesture activation/gating and Photo preview active styling. Both inline JavaScript blocks parsed successfully. Targeted checks confirmed all four Pointer/Touch global-kind gates removed, independent per-target pointer tracking retained, and reset clears all active targets.
- Publisher output commit: `de42b4b796738149e0dfe7c0ffbdbcc38fb9ee9a` (“Publish My Diary web bundle update”). Feed advanced to Web Update 153. Live source and mirror are byte-identical; both blob SHA `aa9a115ce37c1e3cad115046f13dcf3f7f63a75e`. Live feed web SHA-256: `d43796f0c2e4998cbeda3bc1f16dfe7019c44076d9574e9ef5e0f64dbdf0b145`. Publisher commit updated `diary-web/index.html` and `latest.json` with matching source patch and release metadata.
- APK unchanged: 1.0.136 / versionCode 135 / SHA-256 `6fc74ca82888fed4121cc352c1846ec8c6a7063e2d2a33fbe032726f7a244348`; no APK rebuild or signing changes.
- Physical-device verification pending. Ask user to use **Me → Check for Updates**, then test adjustment separately on Cover, Detail and Photo, switching between them in both directions. Do not claim phone-side success until user confirms.
- Rollback: exact pre-edit files on `backup/pre-independent-image-adjustment-2026-11-13`; preserve all diary data and settings.


# Web Update 152 — Automatic finger adjustment after image selection (2026-11-13)

- User requested removal of the separate “Ungli se Adjust Karein” button and automatic image adjustment as soon as an image is selected.
- Starting live state: Web Update 151; APK 1.0.136 / versionCode 135; package `com.personal.diaryapp`; source/mirror blob SHA `99785ad58c1a0a03f0b90b5dc3bd5fe3de9b6077`; feed SHA-256 `4043dc99f56adba90e65d54869f711bc7f05d3c54c3974e1f17108d7be05bfc8`.
- Changed only `web-source/index.html` in source commit `acc35a9b44f44cacffe8ddf610c142ea2dfecea2`. Removed the manual adjustment button and hint from the Cover, Detail and Photo image-design menu. Added automatic adjustment activation after successful image selection for Cover, Detail and attached Photo. Existing pointer/touch gesture engine, one-finger drag, two-finger pinch, zoom range 0.8–4, rendering and saved position/zoom state remain in place. No other feature, translation values, storage/data keys, note/photo records, PIN/recovery, native Android source, APK, package identity or signing data changed.
- Pre-edit backup branch: `backup/pre-auto-finger-adjust-no-button-2026-11-13`. Verified readable exact backups:
  - `backups/web-source-before-auto-finger-adjust-no-button-2026-11-13.html`
  - `backups/diary-web-before-auto-finger-adjust-no-button-2026-11-13.html`
  - `backups/latest-before-auto-finger-adjust-no-button-2026-11-13.json`
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-auto-finger-adjust-no-button-2026-11-13.md`
- Source diff reviewed; only the requested adjustment UI/activation logic changed. Both inline JavaScript blocks parsed successfully. No remaining `diary-finger-adjust-button` references in the updated source; the automatic activation function is called from all three image-selection handlers.
- Publisher output commit: `23fe1494f9f5efa4b2681feef048e08060195b2c` (GitHub Actions bot, “Publish My Diary web bundle update”). Live feed advanced to Web Update 152. Re-fetched source and mirror are byte-identical; both Git blob SHA `4ea139d2ca9ee04b72a31b1a9cbc712a3d87ca41`. Independently computed UTF-8 SHA-256 `b3916ea90ea9f46a633a6e11fb47e89540f9ba2a17db7e7993f9cb2529ccef84` matches live `latest.json.webSha256`. Source/mirror/feed checks passed. The workflow-run listing/status endpoint did not expose a run ID or conclusion in this session; publisher bot output commit and updated feed/mirror were verified.
- APK remains 1.0.136 / versionCode 135; APK SHA-256 remains `6fc74ca82888fed4121cc352c1846ec8c6a7063e2d2a33fbe032726f7a244348`. No APK rebuild or signing operation.
- Physical-device verification is **pending**. User should install Web Update 152 using the existing **Me → Check for Updates** path, then confirm image selection automatically enables drag and pinch zoom in Cover, Detail and Photo. Do not claim phone-side success until the user confirms.
- Rollback: use exact pre-edit files on `backup/pre-auto-finger-adjust-no-button-2026-11-13`; preserve notes, photos, PIN data and app data.


# Web Update 132 — Keep the Diary Me button label as “Me” in every language (2026-11-12)

- User request: restore the Me button to its previous literal label, “Me”, in every supported language; make no other changes.
- Starting live state: Web Update 131; APK 1.0.135 / versionCode 134; package `com.personal.diaryapp`. Source commit before this task: `ccf1cdc0d8e56f001b71f67676bab6017a1fa310`.
- Scope: web-only; changed only the nine non-English `words[language]["me"]` values (Roman English, Hindi, Urdu, Arabic, Bengali, Gujarati, Marathi, Tamil, Telugu) to the literal `Me`. English was already `Me`. All ten language dictionaries now return exactly `Me` for this button.
- No other translation keys, button labels, layouts, menus, feature logic, notes, photos, storage, PIN/recovery flows, native Android source, APK, package identity, or signing data were changed.
- Pre-edit backup branch: `backup/pre-me-button-label-all-languages-2026-11-12`. Readable verified backups on that branch:
  - `backups/web-source-before-me-button-label-all-languages-2026-11-12.html`
  - `backups/diary-web-before-me-button-label-all-languages-2026-11-12.html`
  - `backups/latest-before-me-button-label-all-languages-2026-11-12.json`
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-me-button-label-all-languages-2026-11-12.md`
- Exact source change commit: `0ca75c82322828981b509952baebf78d53ba7788`; publisher commit: `e638557b24da1a8f5ae0b4b44c45e4266662260c`. Web-only workflow run `43269118234` completed with **success**.
- Post-publish verification: `web-source/index.html` and `diary-web/index.html` are byte-identical; both Git blob SHA `9f654af4acfd0e24e48268214cfd0fc9068b7774`. Independently computed UTF-8 SHA-256 `ef03b5fc97252aa133b46339ef6bff59add404283584f96091e2412d61ba6707` matches live `latest.json.webSha256`; live `webVersion=132`.
- APK remains `1.0.135` / versionCode `134`; package `com.personal.diaryapp`; APK URL and SHA-256 remain unchanged (`c3e312ec7cd8504bab68c12f9df996c8d10018670d0d1ccef9373408d4ddba4d`). No APK rebuild or signing operation.
- Source diff review: exactly one file changed in the source commit, with 9 additions and 9 deletions; each line is one requested Me-label value.
- Automated language-value check: all ten language keys resolve to exactly `Me`. Workflow and source/mirror/feed checks passed. Physical-device verification remains **pending**; use the existing in-app **Me → Check for Updates** path and confirm the button says “Me” after update.
- Rollback: use the verified backup branch and the exact pre-edit backup files above; preserve the existing last-known-good state.



---

# Web Update 113 — Note Lock Forgot PIN uses Diary-style in-app dialogs (2026-11-12)

- User reported that the Android WebView page address still appeared during Note Lock → Forgot PIN. Re-inspection found remaining native `window.alert()` calls in the Note Lock recovery path, including Copy PIN failure and PIN/storage/crypto error branches; Web Update 112 covered only the wrong temporary-PIN message.
- Updated the Note Lock Forgot PIN path and its new-PIN creation/confirmation path to use the same custom in-app message popup as Diary Lock. The temporary PIN popup, custom four-digit input, wrong-PIN retry, PIN hashing/storage sequence, and new PIN creation flow remain intact.
- Backups: `backups/web112-before-note-forgot-pin-inapp-dialogs-2026-11-12.html`, `backups/diary-web112-before-note-forgot-pin-inapp-dialogs-2026-11-12.html`, `backups/latest-before-web113-note-forgot-pin-inapp-dialogs-2026-11-12.json`, and `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-web113-note-forgot-pin-inapp-dialogs-2026-11-12.md`.
- Web Update 113 SHA-256: `dcbcfce3eeb54d17ac6766dcb703d46e994cbbdc8acea36e6881f8931caea27d`. Source and mirror were written from the same exact HTML content. APK remains 1.0.135; no APK rebuild or app-data change.
- Static verification: no native `window.alert()` / `window.prompt()` remains in the Note Lock Forgot PIN and new-PIN confirmation paths. Physical-device verification is pending; use Me → Check for Updates and test Copy PIN, wrong temporary PIN, and PIN mismatch.

---

# Web Update 112 — In-app Note Lock wrong PIN message (2026-11-12)

- Replaced the native WebView `window.alert` for a wrong temporary PIN in Note Lock → Forgot PIN with a custom in-app message popup.
- The popup shows only the localized Diary message **“Diary PIN galat hai.”** and a close button; the Android page-address heading is no longer shown for this error.
- Closing the message retries the temporary PIN prompt. PIN comparison and recovery logic are unchanged.
- Backup: `backups/web111-before-custom-note-pin-error-2026-11-12.html`
- Feed backup: `backups/latest-before-web112-custom-note-pin-error-2026-11-12.json`
- Master Register backup: `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-web112-custom-note-pin-error-2026-11-12.md`
- Source SHA-256: `28b0fca7bd482c728827bd4b47073adeb3d4a2387de8f6e42db14543dbf89e3a`; source/mirror sync is being verified.
- Web Update 112 only; APK remains `1.0.135` and is not rebuilt. Device-side test pending.

---

# Web Update 111 — Note Lock wrong temporary PIN message (2026-11-12)

- User-requested wording only: when the temporary PIN entered during Note Lock → Forgot PIN is wrong, the message now uses the existing Diary Lock wording: **“Diary PIN galat hai.”**
- Implemented only in the temporary-PIN verification branch by calling the existing `diaryPinWrong` message. The separate legacy recovery-code error text remains unchanged.
- The retry flow, temporary PIN generation, PIN verification, stored lock data, new PIN creation/confirmation, notes, photos, Diary Lock, APK and unrelated features were not changed.
- Backup before change: `backups/web110-before-note-forgot-pin-error-wording-2026-11-12.html`
- Update-feed backup: `backups/latest-before-web111-note-pin-error-2026-11-12.json`
- Master Register backup: `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-web111-note-pin-error-2026-11-12.md`
- Source and mirror were verified byte-identical; SHA-256: `bbb84e19d76f69333ad7e95b8fa6cf5bbd279264f6fba0e47349bd19910fa317`.
- Web Update 111 published in `latest.json`; APK version and APK URL remain unchanged.
- Device-side verification is still pending; user should use **Me → Check for Updates** and test a deliberately wrong temporary PIN.

---

# Web Update 110 — exact UTF-8 SHA-256 correction (2026-11-12)

- User reported that Check for Updates failed with “Diary update SHA-256 match nahi hua”.
- Root cause confirmed: `latest.json` contained an incorrect `webSha256` value (`fa4d6f6a66b835542cd56bcc5246f954b5d41ae33a73a072c323db708512df7f`) for the current `web-source/index.html` bytes.
- Backed up the live feed to `backups/latest-before-web110-sha256-correction-2026-11-12.json` and backed up this register before editing.
- Recomputed SHA-256 over the exact UTF-8 HTML bytes using a SHA-256 implementation verified against the standard `abc` test vector. Correct digest: `163f14796d8a84867ad68e17833991e01bbf4f0d1baa5c1f4696c2362805bf78`.
- Updated only `latest.json` metadata: `webVersion=110`, corrected `webSha256`, and checksum-repair release note. The HTML source, published mirror, APK URL/hash/version, package identity, signing identity, notes/photos/PIN storage, and all app features were not changed.
- Re-fetched the source, mirror, and feed after publishing. Source and mirror are byte-identical and have matching Git blob SHA `3c53a0c8af11d0341d8a9839be3bd12ae5b54ca2`; the independently recalculated source SHA-256 exactly matches the live feed.
- This is a metadata-only web update. Device-side Check for Updates success still requires the user's test; do not claim phone-side verification.

---

# My Diary recovery — restore last-known-good 11:00 AM state (2026-11-12)

- User reported that My Diary worked correctly until approximately 11:00 AM IST on 2026-11-12 and became unstable after later changes.
- Read the Master Register and inspected the live repository history. The last coherent web state at the requested cutoff is **Web Update 98**, recorded at approximately 10:54 AM IST. Subsequent changes altered Note Lock Forgot PIN recovery (manual recovery-PIN verification was replaced by a Copy PIN flow, then repeatedly changed/restored), and later web updates 101–104 plus repeated checksum corrections.
- Created a full pre-repair Git backup branch: `backup/pre-web98-restore-2026-11-12` from pre-repair main head `e90785349d0f9e906798cfd05dd329c1b4edc324`.
- Restored `web-source/index.html` byte-for-byte from the Web Update 98 snapshot at commit `1ace3bd50656ac2e55640e8f198d3f3880e66814`; synchronized `diary-web/index.html` to the same content. Restored source and mirror Git blob SHA: `af8e3bc167b6f3410569663831f7aded9727319d` (225,579 characters each).
- Published **Web Update 105** in `latest.json`, retaining APK identity/version **1.0.135 / versionCode 134**, package `com.personal.diaryapp`, APK URL and APK SHA-256 unchanged. The Web 98 checksum was restored from the matching Web 98 feed: `4545038ad06640840613940e67645eb66b1dc2e655185a53665b8cf4e23843c7`.
- This is a web-content rollback/recovery only. No user data, notes, photos, local storage, PIN/recovery records, package identity, keystore secrets, or signing identity were changed. No new APK was built because the existing 1.0.135 updater can deliver the restored web bundle through **Me → Check for Updates**; do not uninstall or clear data.
- Device-side update and feature behavior still require the user's Check for Updates test. This register entry supersedes the older stale Web Update 85 / APK 1.0.131 note below.

---

# SHA-256 update-feed repair — 2026-11-12

- User again reported the installed app's web-update error: `Diary update SHA-256 match nahi hua`.
- Re-inspected the actual Android updater path. This message is raised only when the downloaded HTML bundle's bytes do not match `latest.json.webSha256`; the APK downloader uses a different error message.
- Verified the signed APK build artifact from workflow run **43089651168** independently: SHA-256 `04a9863ff35f13ca2beccecceaffc49c2e41d6bb8e72bac1df4d4501238b04a2`, matching the APK hash already in `latest.json`. No APK rebuild or APK metadata change was needed.
- Created pre-repair backups:
  - `backups/web-source-index-before-sha-publish-repair-2026-11-12.html`
  - `backups/diary-web-index-before-sha-publish-repair-2026-11-12.html`
  - `backups/latest-before-sha-publish-repair-2026-11-12.json`
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-sha-publish-repair-2026-11-12.md`
- Re-published the exact same Diary HTML with only a non-visible HTML comment added to trigger a fresh release record. No interface, layout, button, feature, or app logic changed.
- Synchronized `diary-web/index.html` byte-for-byte with `web-source/index.html`; both now have Git blob SHA `a211e05028c20bd029c7d00560c9a558576a084e`.
- Independently computed UTF-8 SHA-256 for the exact current HTML and checked the implementation against the standard SHA-256 test vector `abc`. Current HTML SHA-256: `9085dade0a1a84ec2938488e434d89cf825b00d266f2da9542b9db5992775697`.
- Updated `latest.json` to **Web Update 85** with that exact `webSha256`. Re-fetched all three files after commits and verified source/mirror blob SHAs match and feed checksum equals the independently calculated HTML checksum.
- APK remains **1.0.131 / versionCode 130**; signed APK checksum, package name, and signing identity were not changed. Notes, photos, PIN/recovery data and app data were not touched.
- GitHub Actions web-publisher run **43095216483** was triggered by the source change but remained queued during this repair; direct source/mirror/feed synchronization and hash verification were completed independently. Device-side download/install still requires the user's Check for Updates test.

---

# Latest correction — Camera/status-bar background made transparent (2026-11-11)

- User asked to remove the separate background strip above the phone's front camera while keeping the Diary title and content below the camera/status icons.
- Retrieved the exact original Android source from the successful 1.0.126 build artifact; no ZIP upload from the user was needed.
- Updated only the native status-bar setup generated by `scripts/add_diary_app_actions.py`: transparent status bar, edge-to-edge layout behind the system bar, and dark status icons. The current published Diary HTML already includes `viewport-fit=cover` and `env(safe-area-inset-top)` top padding, so the page background extends behind the status bar while the welcome panel stays below the camera/status icons.
- Kept the Diary HTML, panel border/design, buttons, data storage, notes/photos/PIN, package name, and signing identity unchanged.
- Prepared APK **1.0.127 / versionCode 126**, based on installed **1.0.126 / versionCode 125**. Workflow release guard and APK filename/feed update were advanced together. Publish only if debug and signed Release builds, certificate fingerprint, APK checksum, and feed checks all pass.
- Phone appearance remains unverified until the user installs the update through **Me → Check for Updates**.

## APK publish guard alignment — 2026-11-11

- Debug APK and signed Release APK build succeeded in run 43050047044; existing signing certificate fingerprint matched.
- The final publish step correctly refused to publish because a second stale baseline check still expected 1.0.124/123, while the live feed is 1.0.125/124. Updated that final guard to the actual installed baseline. No APK or live feed was changed by the blocked publish.
- This workflow-only correction triggers a fresh signed build. Publish only if all checks pass.

## Backup Save As build correction 2 — 2026-11-11

- Second APK workflow attempt 43049587648 passed source checks and the native patch script, then Kotlin compilation found a duplicate `android.app.Activity` import because the original Android project already imports Activity.
- Removed only the redundant import insertion. The existing Activity import is retained and used by the Save As result handler. No app feature or data change.
- A fresh APK build is triggered by this commit. Publish only after debug and signed Release builds, signing fingerprint, APK checksum and feed all pass.

## Backup Save As build correction — 2026-11-11

- First APK workflow attempt 43049271326 stopped in the patch script before compilation. The exact failure was a generated Python string searching for a literal backslash-n instead of the MainActivity closing-line newline.
- Corrected the generator's class-end search and insertion newline. The Activity-level Save As result handler remains outside the inner JavaScript bridge class, as required.
- The next push triggers a fresh full build; do not publish or install until it passes all source, debug, signed Release, certificate, checksum and feed checks.

# Latest correction — Android Backup opens Save As and confirms only after saving (2026-11-11)

- Backup button root cause: export used a hidden download anchor and displayed success immediately without letting Android choose a folder or filename.
- Web export now calls the Android native bridge in the installed app; regular browser download fallback remains.
- Android bridge uses ACTION_CREATE_DOCUMENT with suggested filename `Diary-My-Notes-Backup.json`. User can choose folder and change filename. JSON is written to selected URI. Success is shown only after stream write completes; cancel/failure clears success status.
- Existing backup JSON structure, restore, notes/photos/PIN data, local storage, styling and app identity are preserved.
- Pre-edit backups stored at `backups/*-before-native-backup-save-dialog-2026-11-11.bak` for edited files.
- Prepared next APK **1.0.126 / versionCode 125**, based on installed **1.0.125 / versionCode 124**. Web Update 79. Workflow builds from tracked Android project ZIP, applies updated native bridge script, and verifies signing identity before publishing.
- Device-side Save As flow remains unverified until installed and tested on Android.

# Latest correction — Inner Diary panel moved down a further 2px (2026-11-11)

- User asked for a very small additional downward adjustment after Web Update 77.
- Inspected the current project register, main web source, published mirror, and update feed. Source and mirror matched before editing; Web Update 77 had the panel at 6px down.
- Changed only the opened inner Diary panel offset from 6px to 8px total using a later, narrowly scoped CSS override. No other layout, controls, features, APK, or user data changed.
- Backups created before editing: `backups/web-source-index-before-inner-diary-downshift-8px-2026-11-11.html`, `backups/diary-web-index-before-inner-diary-downshift-8px-2026-11-11.html`, `backups/latest-before-inner-diary-downshift-8px-2026-11-11.json`, `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-inner-diary-downshift-8px-2026-11-11.md`.
- Published Web Update 78; HTML SHA-256: `98ce041e2b32c238072b23d73ba12a0f2652526e18031ccea3afa9e0dfdf7740`. APK remains 1.0.125 / versionCode 124; no APK rebuild.
- Source/mirror/feed/register will be checked after write. Actual phone appearance awaits user confirmation.

# Latest correction — Opened inner Diary panel moved slightly lower (2026-11-11)

- User asked for the Diary panel that opens inside the app to sit a little lower, matching the recent top-spacing adjustment.
- Inspected the current main web source and published mirror; they were byte-identical before editing. The opened Diary panel is centered inside `#diaryMyNotesOverlay` and already has its own 3D perspective transform.
- Narrow web-only CSS adjustment: added `position:relative; top:6px` to `#diaryMyNotesPanel`. This shifts only the opened inner Diary panel down by 6px while preserving its existing centering, perspective transform, purple outer border, camera safe-area spacing, and Diary behavior.
- Backups created before editing: `backups/web-source-index-before-inner-diary-downshift-2026-11-11.html`, `backups/diary-web-index-before-inner-diary-downshift-2026-11-11.html`, `backups/latest-before-inner-diary-downshift-2026-11-11.json`, and `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-inner-diary-downshift-2026-11-11.md`.
- Published Web Update 77; HTML SHA-256: `49904d23be30b44a0dbfb3714fe84fae907e361efb0b247bb26384e4da39cfba`. APK remains 1.0.125 / versionCode 124; no APK rebuild or app-data changes.
- Static source, mirror, and feed verification completed after publishing. Physical-phone appearance remains pending user confirmation.

# Latest correction — Diary header starts below the camera/status-bar safe area (2026-11-11)

- User clarified that the existing purple 3D border should begin below the phone's front-camera / status-bar area, not behind or beside notification icons.
- Inspected the current published HTML: it uses `viewport-fit=cover` but the page body had a fixed `14px` top padding and did not account for `env(safe-area-inset-top)`.
- Narrow web-only correction: body top padding now uses `calc(14px + env(safe-area-inset-top, 0px))`. This moves the existing Diary content and purple header border below the reported safe area while preserving the existing horizontal/bottom spacing, border design, buttons, and all Diary behaviour.
- Backups created before editing: `backups/web-source-index-before-camera-safe-area-spacing-2026-11-11.html`, `backups/diary-web-index-before-camera-safe-area-spacing-2026-11-11.html`, `backups/latest-before-camera-safe-area-spacing-2026-11-11.json`, and `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-camera-safe-area-spacing-2026-11-11.md`.
- Published Web Update 76; feed records HTML SHA-256 `69daf44646cbaa878b1626a43549b1b073be92457ec6805123be0dcc4110357f`. Source and mirror are byte-identical (Git blob SHA `3bfd3ae6418f008e704e850e048fec4ae0b15271`). APK remains 1.0.125 / versionCode 124; no APK rebuild, signing change, notes/photos/PIN changes, or unrelated feature changes.
- Static source/feed checks passed. Physical-phone appearance remains pending user confirmation after **Me → Check for Updates**.

# Latest correction — Android status bar no longer overlays the Diary page (2026-11-11)

- User showed that Android notification icons (for example Vi and WhatsApp) appeared over the top of the My Diary welcome screen because the native Activity enabled `SYSTEM_UI_FLAG_LAYOUT_STABLE`, allowing the WebView content to draw behind the transparent status bar.
- Updated `scripts/add_diary_app_actions.py` to remove that layout-behind-status-bar flag, set an opaque pale lavender status-bar background (`#FAF7FF`), and enable dark status-bar icons. The status bar now occupies its own area; time, network, battery, and notification icons remain visible, but no longer overlay the Diary content.
- Pre-edit backups: `backups/add_diary_app_actions-before-statusbar-separation-2026-11-11.py`, `backups/build-diary-from-zip-before-statusbar-separation-2026-11-11.yml`, and `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-statusbar-separation-2026-11-11.md`.
- Signed APK **1.0.124 / versionCode 123** built and published successfully by workflow run **43033906461**. Debug build, signed Release build, signing-certificate fingerprint verification, publish, and artifact upload all succeeded. Live `latest.json` now points to `My-Diary-1.0.124.apk` with SHA-256 `391f08f3cdd00cef316668b0cf2111a3fef6bebe0e82946fcb30ff92cb0a1ecb`. Web bundle remains Web Update **74**; its hash and content were not changed.
- No Diary HTML redesign, local notes/photos, PIN/recovery data, package identity, signing identity, or unrelated app features were changed. Physical-device appearance is pending user confirmation after installing 1.0.124 via **Me → Check for Updates**.

# MY DIARY — MASTER PROJECT REGISTER

**Single source of truth. Last updated: 2026-11-11 (published APK 1.0.122 / versionCode 121; Web Update 58).**

## Latest correction — Check for Updates starts APK download directly (2026-11-11)

- User requires the installed app's **Me → Check for Updates** control itself to carry out the update; do not substitute a manually supplied APK link.
- Root cause in the generated native updater: when a newer APK was found, the button opened an extra confirmation dialog with a separate **Download & Install** button. This interrupted the requested one-button update flow.
- Narrow repair in `scripts/add_diary_app_actions.py`: when the feed reports a newer APK, the existing button now immediately calls the existing `downloadAndInstall()` routine. That routine retains the progress display, retries, SHA-256 verification, package/version validation, and Android's system installer handoff. Android's own final install confirmation cannot be bypassed.
- Kept the second generator, `scripts/add_online_diary_updates.py`, compatible with the new branch. It now validates/preserves the direct APK-download branch while retaining the existing web-bundle update path when the installed APK is already current.
- When the installed APK is already current, the existing web-bundle hash-check/update path remains in place. Notes, photos, PIN/recovery data, package identity, signing identity, UI, and other features are unchanged.
- Pre-edit backups: `backups/add_diary_app_actions-before-one-tap-check-update-2026-11-11.py`, `backups/build-diary-from-zip-before-one-tap-check-update-2026-11-11.yml`, and `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-one-tap-check-update-2026-11-11.md`, and `backups/add_online_diary_updates-before-one-tap-check-update-2026-11-11.py`.
- Preparing signed APK **1.0.122 / versionCode 121** from live feed baseline **1.0.121 / versionCode 120**. Do not report this repair as complete until the signed build, signature fingerprint, APK checksum, and live feed are verified. Device-side download/install remains pending user confirmation.


**Single source of truth. Last updated: 2026-11-11 (signed APK 1.0.119 / versionCode 118; Web Update 56 keeps Recently Deleted action labels on one line).

## Latest correction — Check for Updates refreshes the verified current web page (2026-11-11)

- User reported that **Me → Check for Updates** said Diary was already updated while the screen still showed the old interface.
- Root cause in the native updater: when the installed HTML SHA-256 already matched the published web bundle, it returned “already latest” without reloading the WebView. The on-disk HTML could be current while the currently displayed page remained alive in WebView memory.
- Narrow repair in `scripts/add_online_diary_updates.py`: when the installed hash matches, reload the existing `https://appassets.androidplatform.net/assets/index.html` URL through the existing verified local-file path handler, then show a refresh-confirmation message. No data, notes, photos, PINs, or package identity are changed.
- A new signed APK **1.0.120 / versionCode 119** is being prepared from the existing 1.0.119 / versionCode 118 baseline. Published web bundle remains **Web Update 56**; no web-source redesign or new web content is required.
- Pre-edit backups: `backups/add_online_diary_updates-before-force-webview-reload-2026-11-11.py`, `backups/build-diary-from-zip-before-force-webview-reload-2026-11-11.yml`, and `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-force-webview-reload-2026-11-11.md`.
- Device-side confirmation is pending. Do not claim the fix works on a phone until the user installs 1.0.120 and tests **Me → Check for Updates**.

## Latest correction — Recently Deleted buttons stay one line (2026-11-11)

- User clarified that **Hamesha ke liye mitaayein** must remain on one line, not wrap to two lines.
- Updated both Recently Deleted action buttons to fixed 40px height, one-line non-wrapping labels, centered text, and responsive smaller font/compact horizontal padding so the full phrase fits within the full-width button on mobile. Restore/delete handlers remain unchanged.
- New pre-edit backups: `backups/web-source-index-before-trash-button-one-line-2026-11-11.html`, `backups/diary-web-index-before-trash-button-one-line-2026-11-11.html`, `backups/latest-before-trash-button-one-line-2026-11-11.json`, and `backups/docs-register-before-trash-button-one-line-2026-11-11.md`.
- Web Update **56**; source and mirror synchronized, SHA-256 `44886700f7382f1f1d5c4c2ec35d602429ce19bf0ac92cea472365e8230872eb`. APK remains **1.0.119 / versionCode 118**. Web-only CSS correction; no note/photo data or PIN changes. Live static checks passed; visual confirmation on physical phone is pending.

## Latest change — Recently Deleted action-button fit (2026-11-11)

- User reported that the **Hamesha ke liye mitaayein** label appeared below/outside the **Mitaayein** button instead of fitting within the complete button.
- Added a dedicated class to the existing Recently Deleted action row and scoped CSS so **Wapas Laayein** and **Hamesha ke liye mitaayein** use equal full-width stacked buttons. Labels can wrap inside the button; height grows naturally when a translated label needs another line. Existing click handlers, confirmation prompts, restore/delete behavior, and trash data are unchanged.
- Backups created before editing: `backups/web-source-index-before-trash-delete-button-fit-2026-11-11.html`, `backups/diary-web-index-before-trash-delete-button-fit-2026-11-11.html`, `backups/latest-before-trash-delete-button-fit-2026-11-11.json`, and `backups/docs-PROJECT_MAP_AND_SECRETS_REGISTER-before-trash-delete-button-fit-2026-11-11.md`.
- Source and mirror are synchronized at blob SHA `a3bec7494f034f558b0c144c28675b05c4f73ac7`. Published feed is Web Update **55**, source length 203,260 characters, SHA-256 `9d3c5d035d5cc94c998cd7392451a7729a6d70c2fea1a9d36c6ae805d2600575`.
- APK remains **1.0.119 / versionCode 118**. This is a web-only layout correction; no APK rebuild, signing change, note/photo data change, PIN change, or MUAZZIN change was made. Static publication checks completed; physical phone appearance still needs user confirmation.


This file replaces the old project register. Read it first at the start of every My Diary task, then inspect the live repository and current source before editing. Older dated audit and handover files in `docs/` are historical evidence only; when they conflict with this register or current GitHub state, do not treat them as current instructions.

## Latest change — Recently Deleted mobile visibility (2026-11-11)

- User reported that opening Me → Haal hi mein delete kiye gaye placed the deleted-note list too far down, hiding its actions on mobile.
- Root cause: the list is moved into the absolutely positioned Me menu, but the menu had no height limit or internal scrolling. Added a mobile-safe maximum height and vertical scrolling to the visible Me menu, with touch scrolling enabled; opening the trash list resets its scroll position to the top.
- The existing deleted-note cards, Restore and Delete Forever actions, trash storage, note data, PINs, and APK/signing identity were not changed.
- Published web source and mirror are synchronized (same blob SHA 9a30a3edec4eafd64ed42ec63ab91f4d08f951ac). Web Update 54 is recorded in latest.json; UTF-8 source length 234,669 bytes and SHA-256 fb177a134365b9cd3b57e792babf3567d913f49dcbf070c84d78cd31d2dd0ab8.
- Backups: backups/web-source-index-before-trash-menu-mobile-scroll-fix-2026-11-11.html, backups/diary-web-index-before-trash-menu-mobile-scroll-fix-2026-11-11.html, backups/latest-before-trash-menu-mobile-scroll-fix-2026-11-11.json, and backups/docs-PROJECT_MAP_AND_SECRETS_REGISTER-before-trash-menu-mobile-scroll-fix-2026-11-11.md.
- APK remains 1.0.119 / versionCode 118; no APK rebuild or signing change was made. Static source/feed checks completed; physical mobile scrolling still needs user confirmation after Me → Check for Updates.

## 0. Current verified release and web-update state — 2026-11-11

- Signed APK **1.0.119 / versionCode 118** was built and published by workflow run **42860862628**. Source validation, debug build, signed Release build, publish, signed APK upload, and artifact upload all completed successfully.
- Live `latest.json` points to `My-Diary-1.0.119.apk`, package `com.personal.diaryapp`, versionCode 118, versionName 1.0.119, and APK SHA-256 `b98e8902f9896971e1dccf634a4d4d0349066f1885a9dee0125a303bf4d57a63`. The main-branch Git tree confirms the versioned APK exists (1,955,249 bytes).
- The 1.0.119 updater repairs false “already latest” reports for the web UI: it compares the installed `filesDir/diary-web/index.html` SHA-256 with feed `webSha256`; only an exact match is treated as current. If not, it downloads the trusted published HTML, verifies SHA-256, then replaces the app-private bundle.
- APK publishing no longer overwrites `web-source/index.html` or `diary-web/index.html` from the older ZIP-generated HTML. The published web UI is preserved when future APK releases are built.
- Current web bundle is **Web Update 52**, restored to the interface from before Calendar View and Note Colours. `web-source/index.html` and `diary-web/index.html` have the same Git blob SHA `48b08d0899aba36093094db3832281e133590c2d`; the exact UTF-8 payload is 234,165 bytes and SHA-256 is `224bb72fce7055f07ea97334c7958a72d4f344987bef603784d56c01e6f081d3`. The live `latest.json.webSha256` now matches this value.
- The Content-Length false rejection was removed from the APK downloader; complete APK downloads are validated by SHA-256, package name, and version.
- Follow-up incident 2026-11-11: users on 1.0.119 saw `Diary update SHA-256 match nahi hua`. Root cause was the published `latest.json.webSha256` value, not the downloaded HTML: it contained an incorrect checksum. Recomputed SHA-256 from the actual raw.githubusercontent.com response bytes (234,165 bytes), corrected `latest.json` to `224bb72fce7055f07ea97334c7958a72d4f344987bef603784d56c01e6f081d3`, and independently re-fetched/re-hashed the raw HTML; exact match confirmed. A later feed edit had reintroduced a stale `webSha256` (`5a018c...`) while the published HTML remained unchanged. On 2026-11-11 this was repaired again after backing up the exact current feed and Master Register; the current feed hash was verified against the 234,165-byte UTF-8 source fetched from GitHub. No APK rebuild required; version remains 1.0.119 / code 118 and webVersion 52.
- Backup files for the updater/workflow repair are `backups/add_online_diary_updates-before-hash-repair-2026-11-10.py` and `backups/build-diary-workflow-before-preserve-web-source-2026-11-10.yml`. The web source backup remains `backups/web-source-index-before-restore-android-back-2026-11-10.html`.
- **Other phones have not been physically tested.** They must install the 1.0.119 APK for the hash-based repair to take effect; then Me → Check for Updates should compare and update the web bundle. Do not claim secondary-phone success until confirmed.
- Do not change local notes, photos, PIN/recovery data, package identity, signing identity, or unrelated features.

## 1. Project identity and boundary

- App: **My Diary** — a standalone Android app, separate from MUAZZIN.
- Repository: `amuazzinxyz-ops/My-Diary-Updates`
- Branch: `main`
- Android package: `com.personal.diaryapp`
- Latest APK currently served by the update feed: **1.0.119**, versionCode **118**. The signed APK is served at https://raw.githubusercontent.com/amuazzinxyz-ops/My-Diary-Updates/main/My-Diary-1.0.119.apk. The current web bundle is served from web-source/index.html and recorded in latest.json as webVersion **52**. Feed SHA-256 for the web bundle: `224bb72fce7055f07ea97334c7958a72d4f344987bef603784d56c01e6f081d3`.
- Latest update feed: `latest.json`.
- Current source archive: `Diary-Android-Project-v13 (6).zip`.
- Build workflow: `.github/workflows/build-diary-from-zip.yml`.
- Helper scripts and language data: `scripts/`.
- Project evidence and dated records: `docs/`.

**Hard boundary:** all future My Diary source, app, build, release, update, and documentation work belongs only in this repository. Do not use or modify the MUAZZIN website/repository/workflows for Diary work. Do not merge the two apps or create a second project/workflow/archive when the existing one can be reused.

## 2. Previously published 1.0.105 release — historical evidence (superseded by the 1.0.104 rollback below)

- Version: **1.0.105** / versionCode **105**.
- Package: `com.personal.diaryapp`.
- Published APK: `My-Diary-1.0.105.apk` (also copied to legacy `My-Diary.apk`).
- Update URL in live `latest.json`: `https://raw.githubusercontent.com/amuazzinxyz-ops/My-Diary-Updates/main/My-Diary-1.0.105.apk`.
- SHA-256 in live feed: `c94b0d682bd86cd0a2c0f344cc0158bcd9346453ede4b0f4eb447b67681ea7cf`.
- Published release commit: [31d2249](https://github.com/amuazzinxyz-ops/My-Diary-Updates/commit/31d2249c6129c850e9dd16818ceb3a4a059842c6).
- Build run `42656590333` completed successfully. The workflow validated the existing signing certificate fingerprint `23A4E93F3C7911DCE18389EA583548700C6AD6A3759707F1CD222D07E2408B5A` before publishing.
- Downloaded signed-release artifact and independently calculated the APK SHA-256; it exactly matches the live feed value above. The versioned APK exists in the main-branch publish commit.
- The 1.0.103 APK contains an allow-list for the repository's raw GitHub URL prefix (not an exact `My-Diary.apk` filename), so the new version-specific APK path remains within that approved prefix. This supports compatibility for older updater clients.
- The affected user's actual in-app download, verification, and installation on another phone remain **not device-verified**. Successful build/publication and matching checksum do not prove that the user's device has completed installation.
- The 1.0.105 updater sends `Accept-Encoding: identity`, but older installed clients cannot benefit from that change until they install a newer APK. The 1.0.106 source fix removes the strict Content-Length equality requirement: the downloader reads the complete response and relies on SHA-256, APK package, and version verification to reject incomplete or incorrect files. The live feed remains at 1.0.105 until the signed 1.0.106 build passes workflow checks and is published. The affected phone's download and installation remain unverified.

## 3. Updater reliability — included in published 1.0.95

- Reversible backup branch created: `backup/pre-updater-reliability-1.0.93`.
- Updater source: `scripts/add_diary_app_actions.py`.
- New downloader retries up to three times, uses a temporary partial file, checks content length when supplied, verifies SHA-256, validates APK package and version against the feed, and opens Android's unknown-app install permission settings when needed.
- 2026-11-09 user reported that tapping Download & Install shows the APK download/SHA-256 start message and then immediately reports download/verification failure. The signed APK and live latest.json remain 1.0.105 / versionCode 105 while the next release is prepared. The current updater requests uncached metadata and APK URLs, retries three times, checks HTTP response/content length/SHA-256/package/version, follows HTTPS GitHub CDN redirects only to approved GitHub content hosts, and displays the actual failure reason. The user's earlier generic message did not reveal which check failed; the proposed 1.0.106 change addresses the strict Content-Length failure path, but the affected phone must still be tested. A successful publication does not prove device-side download/install success.
- Uses the existing raw.githubusercontent.com APK URL so older 1.0.92 clients' URL allow-list is not changed.
- The 1.0.103 release was built against the approved transition from feed baseline 1.0.102/102 and published only after package/version and trusted signing checks passed.
- Relevant updater/workflow commits: `60d19813d1b9e2ab4361238c829dda17acf401bf` (updater compatibility), `460ddfd6fe7035c893e1b71790288c408fc57650` (1.0.94 version gate), `1b7c87a51bf97232081e34f80731b6e15b77be0f` and `9f6a4d5e4120bc6b8aa9ff1175a225d52f2f91a1` (serialized, safe publishing), and `fd25e3dd44ca16f594a14076a9a7904a6dcd4694` (removed a redundant publish-stage version parser).
- The successful release workflow run `42634599963` published the verified signed 1.0.103 APK and feed after signing, package, version, and SHA-256 checks passed.

Before a later release:
1. Read live `latest.json` and current Gradle/workflow version gates.
2. Advance the next version from the actual feed, not from memory.
3. Keep fail-closed package, baseline, next-version, signing, and metadata checks.
4. Never publish a debug or unsigned APK as an app update.

## 4. Language status and next language work

The current translation expansion includes these 10 app language options:
1. Roman English
2. English
3. Hindi
4. Urdu
5. Arabic
6. Bengali
7. Gujarati
8. Marathi
9. Tamil
10. Telugu

Arabic was added in the 1.0.92 source change (133 translation keys matching the Urdu schema); Kannada was replaced by Arabic in that change. Arabic is RTL. Treat wording quality as needing language review where appropriate; key-count matching alone does not prove perfect translation.

**User's next language goal:** expand from 10 to 20 languages. Complete the remaining 10 language options before starting automatic language detection. Before adding each language, inspect the current translation schema and generated UI text audit, avoid duplicate or partial dictionaries, and test coverage/RTL behavior where relevant. Do not claim 20 languages are complete until all 20 options and their interface strings have been checked.

## 5. Diary feature map and preservation requirements

This is the standalone My Diary app, not the Diary panel inside MUAZZIN. The existing project/archive and generated Diary HTML are the source to inspect. The following are user requirements and known feature areas; **verify their exact current implementation in the source before editing rather than assuming every requested detail is already complete**.

### Existing feature areas to preserve
- Notes and Diary entries, including saved local records.
- Note lock and the existing PIN protection.
- Diary PIN lock and its recovery/forgot-code flow.
- Photos and attachments.
- Share note / share content.
- Pin Note, Favourite, Smart Search.
- Multi-select notes and delete controls.
- Note editor formatting and existing text/name fields.
- App language selector and translation dictionaries.
- Android app identity, local storage, update behavior, and navigation.

### Specific user requirements — do not regress
- Never change or remove the existing **Note lock** while making unrelated changes.
- Preserve existing diary entries, photos, local storage keys, PIN hashes, and recovery behavior.
- For Diary lock recovery, after a forgotten-code recovery/unlock, require a newly created code before the same old recovery path can be reused, as previously requested; inspect current source to see whether this is implemented before changing it.
- Note editor should retain its two existing fields: optional name (`Note ka naam (optional)`) and note text (`Yahan apni baat likhein…`). Do not add separate duplicate image boxes.
- An image selected near the name belongs within the name field/design; an image selected near the note text belongs within the text field/design. Preserve image/text placement when sharing; do not shift all text to the left or duplicate title/name text.
- Font-size controls must change actual text size (not merely box dimensions); font family and bold controls should work on the intended text.
- Preserve existing layout, buttons, colors, behavior, and all unrelated functions unless the user explicitly asks for a change.

## 6. Signing, app identity, and data safety

- Keep package `com.personal.diaryapp` unchanged.
- Keep using the existing trusted signing setup and same signing identity for in-place updates. Never generate a new keystore or signing key.
- The four expected GitHub Actions secret names are:
  - `DIARY_KEYSTORE_BASE64`
  - `DIARY_KEY_ALIAS`
  - `DIARY_KEY_PASSWORD`
  - `DIARY_STORE_PASSWORD`
- Their values are secret: never print, request in chat, commit, or place in documentation. Do not delete, rename, regenerate, or change them.
- The 1.0.92 workflow run successfully passed its signing readiness/keystore validation and published the signed release; the user's phone then accepted it as an update.
- Never ask the user to uninstall the working app, clear app data, or delete local notes/photos as a routine troubleshooting step.
- Never replace the release APK with a debug or unsigned APK.

## 7. Required workflow for every new request

When the user says **“new kaam”**, **“sudhar”**, **“aage”**, or gives a feature request:

1. Read this Master Register first.
2. Inspect the live repository head, latest commit, current APK/feed version, source archive, relevant source/script, and build workflow. Do not rely on old chat snippets or historical audit notes alone.
3. Identify the exact existing section/function and check whether the requested feature already exists.
4. Start directly if the request is clear. Do not ask the user to upload files or repeat information already in this repository/register.
5. Ask only one concise question if an essential detail is genuinely missing or a change could risk data, security, app identity, or an irreversible behavior.
6. Before editing, preserve the original source/archive and create a clear backup or reversible commit. Change only what the user requested.
7. Preserve all unrelated features and existing user data. Do not refactor or redesign unrelated screens.
8. Run the relevant static checks, syntax checks, translation coverage checks, Android build, and release verification as applicable.
9. For a production update, verify package, monotonically increasing versionCode, versionName, trusted signing identity, APK SHA-256, exact feed URL, and publish workflow. A successful build alone is not proof of a successful phone update.
10. Report what changed, exact files/commit, tests passed/failed, and what remains untested. Never claim a device test unless the user confirms it or there is actual device evidence.
11. Update this register after each important source, feature, language, version, workflow, or release change. Keep dated audit files as historical evidence, not competing master registers.

## 8. Current update failure status (2026-11-09)

- User clarified that their own phone updates successfully; the failure affects other users who are on 1.0.103 or older and see: “Download/verification nahi hua. Update abhi install nahi kiya gaya”.
- 1.0.105 is now published with a unique version-specific APK URL to avoid stale CDN content associated with overwriting the same APK filename. The signed APK artifact's independently calculated SHA-256 matches the live feed exactly; build, trusted signing-certificate check, and publish all succeeded.
- The older 1.0.103 client's approved raw-GitHub URL prefix accepts the new versioned APK path. The 1.0.105 updater adds `Accept-Encoding: identity` for strict Content-Length checks, but this cannot retroactively change downloader code on already-installed older clients.
- The actual affected user's in-app download, verification, and installation are still **not device-verified**. Do not say the issue is fully fixed until an affected user confirms a successful in-app update.
- Do not create a new signing key, publish a debug APK, uninstall the existing app, clear app data, or alter local notes/photos/PIN data. Preserve the existing signing identity.

## 9. User's current known next goal

- Continue completing the remaining 10 languages to reach 20 total.
- Only after all 20 languages are complete and checked, work on automatic language detection.
- For any new feature or correction the user specifies before that, prioritize the exact request and preserve the rest of the app.

## 10. Short request format (optional)

The user can simply say what they want in Roman Hindi. No special template, file upload, or explanation is required when the existing project contains what is needed.


- Historical publish validation note: the earlier redundant version-parser failure was corrected before the verified 1.0.94 release. That 1.0.94 parser failure is historical; the current live feed and 1.0.95 release evidence above are authoritative.

## 11. User-requested version rollback — 2026-11-09

- User explicitly confirmed restoring **My Diary 1.0.104 / versionCode 104** and removing the later 1.0.105, 1.0.106, and 1.0.107 release files from the active main-branch distribution.
- Live `latest.json` now serves versionCode 104 / versionName 1.0.104 with the original recorded SHA-256 `f14e75d502d9263e29ab81250f781925f034afe63296a7444abd4cc8c65c7544`.
- APK URL is pinned to immutable historical commit `89219d4e9e553f606b5323a85723705e9ca3ed44`, path `My-Diary.apk`; the historical APK path and matching old metadata were confirmed present.
- Web bundle metadata is also restored to the 1.0.104-era webVersion 8 and pinned to the same immutable commit.
- Removed from the main branch: `My-Diary-1.0.105.apk`, `My-Diary-1.0.106.apk`, `My-Diary-1.0.107.apk`, and the main-branch `My-Diary.apk` alias that pointed to 1.0.107. Their historical Git objects/commits remain recoverable; this was not a destructive history rewrite.
- The separate legacy file `My-Diary.apk.apk` was not touched because it is not one of the 1.0.105–1.0.107 files targeted by the user's instruction.
- This restores the distribution feed and release assets only. It does not install or downgrade the app on any phone. The affected-device in-app update still needs a real phone-side test; do not claim it is fixed until confirmed.


## 12. Updater-compatible APK URL repair — 2026-11-09

- Root cause: `latest.json` had been changed to an immutable commit URL. The installed updater only accepts APK URLs under `https://raw.githubusercontent.com/amuazzinxyz-ops/My-Diary-Updates/main/`; therefore it rejected the commit-pinned APK as an untrusted URL before installation.
- Restored the exact original signed 1.0.104 APK blob (`ff244e050b348a8e92e3871375db838521a5b259`, 1,950,182 bytes) at `main/My-Diary.apk` without rebuilding or resigning it.
- Restored `latest.json.apkUrl` to the updater-compatible `/main/My-Diary.apk` path. Version remains 1.0.104 / versionCode 104; APK SHA-256 remains `f14e75d502d9263e29ab81250f781925f034afe63296a7444abd4cc8c65c7544`.
- Verified the 1.0.104 signed release artifact independently: SHA-256 matches the feed; successful workflow run `42648457972` confirms the trusted signing certificate fingerprint `23A4E93F3C7911DCE18389EA583548700C6AD6A3759707F1CD222D07E2408B5A`.
- New repair commit: `58652250ae0d390c28bbe7ebe522b5aaf8ec1b5b`.
- The phone-side in-app download/install is not yet device-verified. Do not claim completion until an affected 1.0.103-or-older device confirms installation.


## 13. APK download verification repair and signed release — 2026-11-09

- Confirmed the signed 1.0.104 updater still compared the received byte count against the HTTP `Content-Length` header. GitHub/CDN transfer behavior can make that header differ from the bytes delivered to the Android client, causing valid APK downloads to be rejected before installation.
- The current updater source now sends `Accept-Encoding: identity`, reads the full response body, and verifies the completed APK using SHA-256, package name, and versionCode; it does not reject a valid file solely because `Content-Length` differs.
- Repaired the release workflow's stale hardcoded version gates to build **1.0.105 / versionCode 105** from the live **1.0.104 / versionCode 104** feed baseline.
- Signed release workflow run `42668393009` passed source validation, debug build, signed release build, signing checks, publish, and artifact upload. Published feed points to `My-Diary-1.0.105.apk` and records SHA-256 `32a8d90f991cab12b1e3ad462e8a4b82135b11d3bc783be54e7f5280749864a2`.
- Live `latest.json` release notes were corrected to describe the updater fix. The phone-side in-place installation and update behavior still require confirmation on a device; do not claim device verification until the user confirms it.
- No app data, notes, photos, or PIN storage was cleared or migrated by this release task.
## 14. My Diary 1.0.112 — confirmed update workflow and current handover (2026-11-10)

- Current published release: **1.0.112**, versionCode **111**, package `com.personal.diaryapp`.
- Current APK: `My-Diary-1.0.112.apk`; feed URL: `https://raw.githubusercontent.com/amuazzinxyz-ops/My-Diary-Updates/main/My-Diary-1.0.112.apk`.
- Current APK SHA-256 from live `latest.json`: `040740f50feb19447ce9dc0aaeb69c2190539d3ff02737ec15247e51ee43bba2`.
- Successful signed build/publish workflow run: `42688075014` — **success**.
- This release sets all three Diary action buttons to **40px height**: **Check for Updates**, **Refresh**, and **Share App**.
- **User-confirmed device result (2026-11-10):** the user reports that updates now work correctly on their own mobile and on the other user's mobile using **Check for Updates**. Treat this as the current successful real-device confirmation, replacing the older “device-side update pending” status in historical sections above. Do not continue describing the current update flow as unverified.
- Current stopping point: the update/download/verification/install flow is working as confirmed by the user. No further updater changes are needed unless a new reproducible problem is reported.
- For the next task, first read this register and inspect the live `main` branch, `latest.json`, current source archive, relevant script, and workflow. Continue in the same narrow, backup-first, test-before-release manner.
- Preserve package `com.personal.diaryapp`, the existing trusted signing identity/secrets, all diary notes/photos, PIN Lock and recovery, and every unrelated feature. Never uninstall the working app or clear its data as a routine step. Do not modify MUAZZIN.
- For future releases, derive the next version from the live feed (currently versionCode **112**); do not reuse or guess a version. Verify build, signing, APK SHA-256, feed URL, and release publication. Report phone-side behavior only as confirmed by the user or actual device evidence.


## 15. Me menu button height update — 2026-11-10

- User requested that every button inside the My Diary **Me** menu be exactly **40px** high.
- Added a narrowly scoped CSS rule to `web-source/index.html` targeting buttons and button-role/input button controls inside `#diaryDiaryMePanel` only. It sets `height`, `min-height`, and `max-height` to 40px with `!important`; controls and buttons outside the Me menu are not targeted.
- Preserved the pre-edit HTML at `backups/web-source-index-before-me-buttons-40px-2026-11-10.html`.
- Updated `latest.json` web bundle metadata to webVersion 18 and SHA-256 `1fef5d5719bb402408db38d3454127eb68dc0382ed68d6677c133a22ce17aeb2`.
- Static verification: the new scoped CSS rule is present in the live source; the backup file is present. No Android APK rebuild or physical-device visual test was performed for this CSS-only web bundle change.

## 16. My Diary 1.0.113 — Interface Colours in Me menu (2026-11-10)

- Current published release: **1.0.113**, versionCode **112**, package com.personal.diaryapp.
- Signed APK: My-Diary-1.0.113.apk; feed URL: https://raw.githubusercontent.com/amuazzinxyz-ops/My-Diary-Updates/main/My-Diary-1.0.113.apk.
- APK SHA-256 from live latest.json: 4db6f8e7bf5fea511a133a8750e56060f165d8d0653739a5cddbfba62a5c48cc.
- Successful signed build/publish workflow run: 42774333846. Debug build and signed Release build succeeded; the release certificate SHA-256 matched the previously trusted signing fingerprint 23A4E93F3C7911DCE18389EA583548700C6AD6A3759707F1CD222D07E2408B5A.
- Added 🎨 Interface Colours inside the existing Me menu. It offers Original, Blue, Green, and Rose themes. The selected theme is saved locally using the separate key diary_interface_theme_v1 and restored when the Diary opens.
- Added translations for the new button and palette labels in all 10 existing language options.
- Updated only the Diary generation/language scripts and the Diary-only APK workflow version gate. The workflow publishes the generated Diary web bundle and signed APK; no MUAZZIN repository or workflow was used.
- Backups created before editing:
  - backups/add_diary_refresh_button-before-interface-colours-2026-11-10.py
  - backups/expand_diary_languages-before-interface-colours-2026-11-10.py
  - backups/build-diary-from-zip-before-interface-colours-2026-11-10.yml
  - backups/web-source-index-before-interface-colours-2026-11-10.html
  - backups/README-before-interface-colours-release-2026-11-10.md
  - backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-interface-colours-release-2026-11-10.md
  - backups/latest-before-interface-colours-release-2026-11-10.json
- Static verification: Diary project validation passed; generated HTML/JavaScript syntax check passed; translation audit passed; debug build passed; signed Release build passed; signing certificate and publish checks passed. The published web source contains the Interface Colours button, theme persistence, palette CSS, and all 10 localized labels.
- Not yet verified on a physical phone: visual appearance and in-place installation of 1.0.113. Do not claim a device test until the user confirms it. Existing notes, photos, PIN Lock/recovery, package identity, and signing identity were preserved.
- Current version baseline for the next release: versionCode **112** / versionName **1.0.113**. Derive the next version from the live feed and keep all existing data and features intact.


## 17. My Diary 1.0.114 — updater download progress and verification visibility (2026-11-10)

- Current published release: **1.0.114**, versionCode **113**, package **com.personal.diaryapp**.
- Signed APK URL: https://raw.githubusercontent.com/amuazzinxyz-ops/My-Diary-Updates/main/My-Diary-1.0.114.apk.
- APK SHA-256: `223a0a8397764e289c1a95fae6aa674ff3272c55b1db2d6b340bf96ec98802c0`. The downloaded signed workflow artifact APK was independently hashed locally and matched the live `latest.json` checksum exactly.
- Successful signed build/publish workflow run: **42786868649**. Debug build, signed Release build, publication, and artifact upload succeeded. The signing certificate was verified against the previously trusted SHA-256 fingerprint `23A4E93F3C7911DCE18389EA583548700C6AD6A3759707F1CD222D07E2408B5A`.
- User-reported symptom prompting this change: APK download appears to stop after about 10–20 seconds. Static inspection showed the updater only displayed a short Toast and had no persistent progress UI; that made it impossible to tell whether bytes were still downloading, a retry was happening, or the transfer had failed.
- Kept the existing HTTPS download, three-attempt retry, SHA-256 verification, package/version validation, and Android installer flow. Added a persistent native progress dialog with percentage when the server provides a content length, indeterminate progress otherwise, visible retry status, verification status, and dismissal before installer launch or failure details. This is a narrow updater-only change.
- Updated the build workflow to versionCode 113 / versionName 1.0.114 and the matching APK filename/path. The workflow's baseline guard required the live 1.0.113 / 112 feed before publishing.
- Backups created before editing:
  - `backups/add_diary_app_actions-before-download-progress-2026-11-10.py`
  - `backups/build-diary-from-zip-before-download-progress-2026-11-10.yml`
- Verification: source generation and JS syntax audit passed; Android debug build passed; signed Release build passed; APK signature fingerprint passed; live metadata SHA-256 matched the signed APK bytes. No physical-device installation or real network download test has yet been performed, so do not claim the original 10–20-second symptom is fully resolved until the user confirms the 1.0.114 update behavior. The new persistent progress/error display will show the actual stage and failure reason if it recurs.
- Preserved Diary notes, photos, PIN settings, package identity, signing identity, existing Check for Updates entry point, Refresh, and unrelated app features. Do not change the download mechanism again without a reproducible reason.

## 18. My Diary web-only update 29 — Interface Colours label fit (2026-11-10)

- User reported that the final “s” in “Interface Colours” was clipped and the in-app Check for Updates message said Diary was latest.
- Confirmed the existing Android updater source already compares the independent `webVersion` field after confirming the APK is current. The Android build workflow runs `scripts/add_online_diary_updates.py`; that code downloads the trusted web bundle, validates SHA-256 and HTML, stores it separately under app files, and reloads the WebView without replacing the APK or touching Diary data.
- Created backup: `backups/web-source-index-before-interface-colours-label-fit-2026-11-10.html`.
- Corrected the Interface Colours button label fit while keeping its height exactly 40px: font size 16px, reduced horizontal padding, and no clipping overflow. Removed the duplicate 🎨 prefix from the button label in the preceding web-only commit.
- Web-only publish workflow run **42795407894** (run 11) completed successfully.
- Verified live `latest.json` reports **webVersion 29** and SHA-256 `84ec629260635c86badc2081c0e63232f8a1009ae1d1c0f1f765af1c67c1beab`; published `diary-web/index.html` contains the updated 16px label rule and overflow-visible rule.
- APK remains **1.0.115 / versionCode 114**; no APK rebuild, signing change, or local Diary data change was made.
- Phone-side application of webVersion 29 and the final visual appearance still require user confirmation. Ask the user to tap **Me → Check for Updates** again; if the installed app already has webVersion 29, it will correctly report latest.

## 19. My Diary 1.0.116 — native PDF Save and Android Back handling (2026-11-10)

- Current published APK: **1.0.116**, versionCode **115**, package **com.personal.diaryapp**.
- Signed APK URL: https://raw.githubusercontent.com/amuazzinxyz-ops/My-Diary-Updates/main/My-Diary-1.0.116.apk.
- APK SHA-256: `0b4d5b60bdf8e77688a434ae1ce4c09cbd699fcee4877d362690b1fb3354488f`. The signed Release APK workflow artifact was downloaded and independently hashed; it exactly matches the published `latest.json` checksum.
- Current online web bundle: **webVersion 43**; web bundle SHA-256: `eeac50f1b19f2a1c2903cbbeae4d9f284dbfb9437ca565642e0d2dbf7a32c381`.
- Successful signed build and publish workflow run: **42842056052**. Diary generation, translation audit, JavaScript syntax check, Android debug build, signed Release build, publish, and artifact upload passed. The release certificate SHA-256 matched the previously trusted fingerprint `23A4E93F3C7911DCE18389EA583548700C6AD6A3759707F1CD222D07E2408B5A`.
- PDF Save now uses a dedicated `DiaryPdfActions.printDiaryPdf` Android JavaScript bridge and native Android `PrintManager` / `WebView.createPrintDocumentAdapter`. The note is saved first; Android's print sheet then offers **Save as PDF**. The ordinary browser popup/print path remains as a fallback outside the native app.
- Android Back now asks the WebView whether the Diary overlay is open. If it is open, Back is consumed and the Diary remains visible; the user closes it using the existing visible × button. When the overlay is not open, normal WebView history / Activity back behavior continues.
- The current online web bundle was used as the APK's embedded Diary HTML so the 1.0.116 APK retains the latest web-only features instead of reverting to the older generated base.
- Backups created before this change:
  - `backups/add_diary_app_actions-before-native-pdf-back-2026-11-10.py`
  - `backups/build-diary-from-zip-before-native-pdf-back-2026-11-10.yml`
  - `backups/web-source-index-before-native-pdf-back-2026-11-10.html`
- Existing notes, photos, local storage, PIN Lock/recovery, package identity, signing identity, updater, and unrelated Diary features were not intentionally changed. No keystore or signing secret was regenerated or altered.
- Static/build verification is complete, but **physical-device behavior has not yet been confirmed**. Ask the user to install **1.0.116** using **Me → Check for Updates**, then test PDF Save (choose Save as PDF in Android's print sheet) and Android Back while the Diary editor is open. Do not claim either behavior is device-verified until the user confirms it.
- This section supersedes the older version baseline and webVersion notes in sections 17–18. Current next-release baseline: **versionCode 115 / versionName 1.0.116 / webVersion 43**. Derive the next version from the live feed.

## 19. My Diary 1.0.116 — native PDF Save and Android Back handling (2026-11-10)

- Current published APK: **1.0.116**, versionCode **115**, package **com.personal.diaryapp**.
- Signed APK URL: https://raw.githubusercontent.com/amuazzinxyz-ops/My-Diary-Updates/main/My-Diary-1.0.116.apk.
- APK SHA-256: `0b4d5b60bdf8e77688a434ae1ce4c09cbd699fcee4877d362690b1fb3354488f`. The signed Release APK workflow artifact was downloaded and independently hashed; it exactly matches the published `latest.json` checksum.
- Current online web bundle: **webVersion 43**; web bundle SHA-256: `eeac50f1b19f2a1c2903cbbeae4d9f284dbfb9437ca565642e0d2dbf7a32c381`.
- Successful signed build and publish workflow run: **42842056052**. Diary generation, translation audit, JavaScript syntax check, Android debug build, signed Release build, publish, and artifact upload passed. The release certificate SHA-256 matched the previously trusted fingerprint `23A4E93F3C7911DCE18389EA583548700C6AD6A3759707F1CD222D07E2408B5A`.
- PDF Save now uses a dedicated `DiaryPdfActions.printDiaryPdf` Android JavaScript bridge and native Android `PrintManager` / `WebView.createPrintDocumentAdapter`. The note is saved first; Android's print sheet then offers **Save as PDF**. The ordinary browser popup/print path remains as a fallback outside the native app.
- Android Back now asks the WebView whether the Diary overlay is open. If it is open, Back is consumed and the Diary remains visible; the user closes it using the existing visible × button. When the overlay is not open, normal WebView history / Activity back behavior continues.
- The current online web bundle was used as the APK's embedded Diary HTML so the 1.0.116 APK retains the latest web-only features instead of reverting to the older generated base.
- Backups created before this change:
  - `backups/add_diary_app_actions-before-native-pdf-back-2026-11-10.py`
  - `backups/build-diary-from-zip-before-native-pdf-back-2026-11-10.yml`
  - `backups/web-source-index-before-native-pdf-back-2026-11-10.html`
- Existing notes, photos, local storage, PIN Lock/recovery, package identity, signing identity, updater, and unrelated Diary features were not intentionally changed. No keystore or signing secret was regenerated or altered.
- Static/build verification is complete, but **physical-device behavior has not yet been confirmed**. Ask the user to install **1.0.116** using **Me → Check for Updates**, then test PDF Save (choose Save as PDF in Android's print sheet) and Android Back while the Diary editor is open. Do not claim either behavior is device-verified until the user confirms it.
- This section supersedes the older version baseline and webVersion notes in sections 17–18. Current next-release baseline: **versionCode 115 / versionName 1.0.116 / webVersion 43**. Derive the next version from the live feed.


## 20. My Diary web-only update 50 — Calendar View and per-note colours (2026-11-11)

- User requested two additions to the existing My Diary project: **Calendar View** (select a saved date and see notes from that day) and **Note Colours** (choose a background colour for each note).
- Added a month calendar with previous/next month navigation, note counts on dates, and date selection to filter the note list by the note's original `created` date. The All Notes control clears the selected date filter.
- Added a per-note colour selector with Original/default plus Yellow, Green, Blue, Pink, Purple, and Peach. The selected `noteColor` is stored within that note's existing JSON record, restored when editing, applied to its note card, and retained by JSON backup/export/import. Existing notes without this property remain unchanged and use the original background.
- Added Roman English, English, Hindi, Urdu, Arabic, Bengali, Gujarati, Marathi, Tamil, and Telugu labels for both features and colour choices.
- Created pre-edit source backup: `backups/web-source-index-before-calendar-and-note-colours-2026-11-11.html`.
- Source commit: `ee74f5df8b9deac8cc570acc49a040e7e8a43110`. The existing web-only publishing workflow completed its publish action: live `latest.json` now reports **webVersion 50** and SHA-256 `a5e8350fe48595f114f6b8a9344d2144e79788e7f2f22ad2128bbd3d8fa5e3c8`. Re-fetched source and published mirror both contain the features and have the same Git blob SHA `c050f46b75cae959a70eeb6ad18c5a1c45261fdd`.
- Static validation: both inline JavaScript blocks in the modified HTML parsed successfully; the publish workflow accepted the HTML and updated the feed/mirror. No APK rebuild was required; APK remains **1.0.119 / versionCode 118**. No app data, notes, photos, PIN/recovery, package identity, or signing settings were intentionally modified.
- Physical phone appearance and use of the new Calendar View/colour selector have **not yet been confirmed**. Ask the user to use **Me → Check for Updates** to receive Web Update 50, then verify both features on the phone. Do not claim device-side testing until the user confirms it.

## 21. Recently Deleted note display repair — 2026-11-11

- User reported that notes inside **🗑️ Haal hi mein delete kiye gaye** no longer opened/displayed as before.
- Root cause: the trash-note expand handler removed the hidden flag from its details container, but did not add the existing expanded class to its note card. The existing Diary CSS intentionally hides .diary-note-full previews until the card has .expanded; as a result, the note content stayed invisible even after tapping its title.
- Narrow fix: the trash-note title toggle now toggles card.classList.toggle('expanded', opening) alongside the details visibility and aria-expanded state. This reuses the existing note-card design and CSS; no redesign or storage-key change.
- Backups before edit: backups/web-source-index-before-recently-deleted-display-fix-2026-11-11.html, backups/diary-web-index-before-recently-deleted-display-fix-2026-11-11.html, backups/latest-before-recently-deleted-display-fix-2026-11-11.json, and backups/docs-PROJECT_MAP_AND_SECRETS_REGISTER-before-recently-deleted-display-fix-2026-11-11.md.
- Source fix commit: 7447af3c120d91649983c0400118240812788f3e; published mirror sync commit: 905c0edeae6bf98c3a8f0a7148f498d81ccfc080.
- Live update feed reports webVersion 53 and SHA-256 17d56cee11f46d5be90e4a274150cccab48d6f190099f64054d411fd05c337d3 for the 234,207-byte HTML bundle. The source and mirror must be confirmed identical before closing this repair. APK remains 1.0.119 / versionCode 118; this is a web-only correction, so no APK rebuild or signing change.
- Static check: the trash title handler toggles the same .expanded class required by the existing CSS rule that reveals .diary-note-full. Actual display on the user's phone is not device-tested; receive Web Update 53 via Me → Check for Updates.


## 22. Recently Deleted panel design refresh — 2026-11-11

- User requested a modest design improvement inside the panel opened by **Me → 🗑️ Haal hi mein delete kiye gaye**. This change is limited to the appearance of the deleted-note cards and their expanded details.
- Added scoped CSS only: softly rounded individual note cards, a subtle green accent and light background, clearer tap-to-expand title surface, a softly framed note-preview area, and a compact expiry label. The existing Restore and Delete Forever buttons retain their current layout, 40px height, one-line labels, and existing click handlers.
- No HTML structure, JavaScript handlers, trash storage key/data, note content, photo data, PIN Lock/recovery, package identity, APK, or signing files were changed. No MUAZZIN files or repository were accessed for edits.
- Pre-edit backups:
  - `backups/web-source-index-before-trash-panel-design-2026-11-11.html`
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-trash-panel-design-2026-11-11.md`
- Source commit: `01d797e8681d182f26c3ca0c86a17e1d5219cf4a`. Web-only publish workflow run **42968535389** completed successfully.
- Published **Web Update 57**. Live feed SHA-256: `84ae2034860516397ceaa6077c7033a30735da6b6560ad897ea2031791fbe590`. Source and published mirror have identical blob SHA `9c0bda40dcdaf11622fa393cbb5f13772435ab53`; both are 205,602 bytes.
- APK remains **1.0.122 / versionCode 121** (SHA-256 `62a7f7687777b9f2caa548ee9c96c327b75eefa2630828b159e42052f0251aa9`). No APK rebuild was needed because this is a web-only styling change; no signing operation was performed.
- GitHub Actions HTML/feed publication checks passed. The panel's visual appearance on a physical phone has not been device-confirmed; use **Me → Check for Updates** to receive Web Update 57, then open Recently Deleted to inspect it.


## 23. Me menu touch scrolling repair — 2026-11-11

- User reported that the buttons inside the Diary **Me** menu appeared fixed and could not be scrolled to reach the lower options.
- Root cause: the dropdown is absolutely positioned inside the Diary header, while the containing `#diaryMyNotesPanel` has `overflow:hidden`; the parent clipped the dropdown below its boundary even though the dropdown had an earlier max-height/overflow rule.
- Narrow fix: when the Me menu opens, add `diary-me-menu-open` to the Diary panel so the panel/header allow the dropdown to extend beyond the frame; give the menu an explicit touch-friendly vertical scroll area (`overflow-y:auto`, `-webkit-overflow-scrolling:touch`, `touch-action:pan-y`, contained overscroll, and a viewport-safe max-height). Reset scroll to the top when opening. Remove the open class when the user taps outside or closes the Diary. The Recently Deleted entry path also activates the same menu-open state.
- Existing menu button order, button sizes, click handlers, translations, note/trash data, photo data, PIN Lock/recovery, and all unrelated features are unchanged.
- Backups:
  - `backups/web-source-index-before-me-menu-scroll-fix-2026-11-11.html`
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-me-menu-scroll-fix-2026-11-11.md`
- Source commit: `2c66f2ab531adfbed4a026fe6516628afd95ff3f`. Web-only publish workflow run **43010831372** completed successfully.
- Published **Web Update 58**. Feed SHA-256: `a79d757830530671cc5715046dbd0bf49a259116a15152a95a059639c9232802`. Source and published mirror have identical blob SHA `f16f50d419d48efd852cb89c1682516ae75d77b3`.
- APK remains **1.0.122 / versionCode 121**; no APK rebuild or signing operation was needed. No MUAZZIN project was changed.
- Automated GitHub web publication checks passed. Physical-device touch scrolling still needs the user to confirm after **Me → Check for Updates** receives Web Update 58.

## 24. Me dropdown overlay and Note Pin separation — 2026-11-11

- User reported that after tapping **Me**, Note Pin (📌) and underlying Diary card content appeared mixed into the Me menu instead of the Me options opening as a distinct dropdown.
- Code inspection confirmed that the Note Pin control is generated only as part of each saved note card, not as a Me-menu option. The Me dropdown CSS had a transparent background and no visible panel surface; after the scroll repair allowed it to extend beyond the Diary frame, the underlying note cards could show through the dropdown area. This made their Pin controls appear to be part of Me.
- Narrow CSS-only repair: made the open Me dropdown an opaque, bounded, raised panel with its own stacking context; preserved the existing menu position, order, 40px controls, scrolling and click handlers. Added a defensive rule to hide any .diary-note-pin only if it is ever rendered inside the Me menu. Note Pin controls remain on their own note cards.
- Backups created before the edit:
  - backups/web-source-index-before-me-menu-overlay-fix-2026-11-11.html
  - backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-me-menu-overlay-fix-2026-11-11.md
- Source commit: 3a2a083738162736153e0f5c56adff123a402c04. Web-only publish workflow run **43012733041** completed successfully.
- Published **Web Update 59**. Live feed SHA-256: 63e85562878fcc65e04e05fdca00718c41e99b948003294a94e925f3e0fbed0a. Source and published mirror have identical blob SHA 7f0ce0ac10c84f8e6786a770b1faab75d2b870f9.
- APK remains **1.0.122 / versionCode 121**; no APK rebuild or signing operation was performed. Notes, photos, PIN Lock/recovery, package identity, and existing button handlers were not intentionally changed.
- GitHub publication checks passed. Physical phone appearance has not yet been device-confirmed. On the phone, use **Me → Check for Updates** to receive Web Update 59, then open Me and confirm that only the Me menu options appear on an opaque panel, with Note Pin remaining on each note card.



## 25. WebView stale-page cache repair — Diary 1.0.123 preparation (2026-11-11)

- User reported that the **Diary ka Asal Rang** label still appeared as the previous Roman wording on the installed Android app, even though the live HTML source and web bundle already contained the requested new wording.
- Inspection confirmed the current Roman dictionary entry is exactly `Diary ka Asal Rang`; the obsolete wording is absent from the current `web-source/index.html`. The live update feed is webVersion **60** and its SHA-256 matches the published bundle.
- Root cause identified in the Android update path: the native `DiaryBundlePathHandler` returned the same `appassets.androidplatform.net/assets/index.html` URL without explicit no-cache response headers. A WebView could reuse an older cached response after the verified on-disk HTML bundle was replaced.
- Narrow native updater repair in `scripts/add_online_diary_updates.py`: both post-update reload paths now append a unique `diaryRefresh` query value; the asset path handler sends `Cache-Control: no-store, no-cache, must-revalidate, max-age=0`, `Pragma: no-cache`, and `Expires: 0`. The hash-verified download, local bundle backup, bundled-asset fallback, app origin, notes/photos/PIN storage, and signing identity remain unchanged.
- Backups before the repair:
  - `backups/add_online_diary_updates-before-webview-no-cache-2026-11-11.py`
  - `backups/build-diary-from-zip-before-webview-no-cache-2026-11-11.yml`
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-webview-no-cache-2026-11-11.md`
- Source commits: updater repair `65e3776e0c30f9533e004298ab6a64c8bfd0115e`; workflow version bump `256bf955ab711ee9a231e2dab17ecce273124375`; cleanup `99e0f38b079645ead7ca13d9e3d6d2b6995f6d2e`; final publish-guard alignment `ff28c27277423d888fd0da8bf85e251d2230581e`.
- The existing release workflow is prepared to build **1.0.123 / versionCode 122** from the exact latest published HTML, using the existing package name and existing trusted signing key. Live APK remains **1.0.122 / versionCode 121** until the signed build and publish workflow succeeds.
- This is a native WebView cache-delivery repair, so a new APK is required for installed apps to receive the stronger no-cache handling. No APK has been declared published until the workflow completes and the signed artifact/feed checks pass. Phone-side display must still be confirmed after installing the update.


---

# Web Update 114 — Diary subtitle tap instruction wording (2026-11-12)

- User-requested exact Roman-language subtitle change under **Meri Diary**: `Apne notes likhein aur search karein` → `Apne notes likhein aur search karne Yaha Tap Kare`.
- Changed exactly one occurrence in `web-source/index.html`; synchronized `diary-web/index.html` to the same exact content. No other language strings, Diary features, buttons, search logic, storage, notes/photos, PIN/recovery flow, APK, package identity, or signing data were changed.
- Backups: `backups/web113-before-diary-subtitle-tap-wording-2026-11-12.html`, `backups/diary-web113-before-diary-subtitle-tap-wording-2026-11-12.html`, `backups/latest-before-web114-diary-subtitle-tap-wording-2026-11-12.json`, and `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-web114-diary-subtitle-tap-wording-2026-11-12.md`; all four were re-fetched and verified readable before editing.
- Source update commit: `6896c4bfc4160c897c744a2f3cd08c87d4073a18`; mirror update commit: `28b229f13464138d79abf3e9047a3fc9b5e5eee7`. Both files have identical Git blob SHA `9ebf5d526731bc57f6ce5b823c5d9d4b5f0aa07b` and 227,890 characters. Post-write re-fetch confirmed exact source/mirror equality and exactly one occurrence of the new phrase.
- Independently computed UTF-8 SHA-256: `ca3f160566a10c62e571689678f84ec55096afa5564bfc9745acbe2300e4aa52`; the SHA implementation passed the standard `abc` test vector. `latest.json` advanced to webVersion `114` with this exact digest. APK remains `1.0.135` / versionCode `134`; no APK rebuild.
- Backup reference / rollback: restore the two HTML files from the matching Web 113 backups and restore `latest.json` from its Web 114 pre-change backup; retain the Register backup as the pre-change record.
- Automated static checks: source/mirror byte identity, exact text count, backup readability, and feed checksum value recorded. GitHub Actions run `43241660297` (run 103) was checked and **failed** at its push step because its checkout was behind the concurrent manual mirror/feed/Register commits (`non-fast-forward`, `fetch first`). The workflow had independently recomputed the same SHA-256 and prepared Web 114 before the push rejection. The final source, mirror, and `latest.json` were then re-fetched and verified consistent; the workflow itself is not marked successful. Physical-device **Me → Check for Updates** test remains pending; do not claim phone verification.


---

# Web Update 115 — Correct Diary subtitle in all supported languages (2026-11-12)

- User corrected the intended wording and asked that the subtitle follow each language already supported by the Diary. The live language dictionary contains exactly three entries: `roman`, `english`, and `hindi`.
- Updated only the `sub` string for those three entries:
  - Roman: `Apne Notes Likhne Aur Search Karne Yaha Tap Kare`
  - English: `Tap here to write and search your notes`
  - Hindi: `अपने नोट्स लिखने और खोजने के लिए यहाँ टैप करें`
- Backups created and re-fetched successfully: `backups/web114-before-diary-subtitle-all-languages-2026-11-12.html`, `backups/diary-web114-before-diary-subtitle-all-languages-2026-11-12.html`, `backups/latest-before-web115-diary-subtitle-all-languages-2026-11-12.json`, and `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-web115-diary-subtitle-all-languages-2026-11-12.md`.
- Source commit: `3a429816e40ab89f0ab5b025829f553a585fae22`. GitHub Actions web-only publish run `43243273460` completed with **success**. Workflow generated/synchronized the mirror and update feed.
- Final re-fetch verified source and `diary-web/index.html` are byte-identical. Verified the three exact language strings above. `latest.json` reports webVersion `115` and web SHA-256 `7ff566dcec4eb114dfbc323cc72aceebf6285d367203e1066866759d2a050cdb`. APK remains `1.0.135` / versionCode `134`; no APK rebuild.
- Scope was limited to the three subtitle strings. No other Diary features, saved notes/photos, PIN/recovery, storage, APK identity, or signing data were changed. Phone-side **Me → Check for Updates** verification is still pending.


---

# Web Update 116 — Localize Diary home screen in all 10 supported languages (2026-11-12)

- User requested that the Diary landing screen follow the selected app language. The screen previously hard-coded My Diary, Private notes, memories and personal writing, and Language / Zaban, even though the app offers 10 languages.
- Added one isolated applyDiaryHomeLanguage() function in web-source/index.html. It translates those three landing-screen strings for Roman English, English, Hindi, Urdu, Arabic, Bengali, Gujarati, Marathi, Tamil, and Telugu. It runs at startup and whenever the language selector or existing language-change/storage events run. Existing language options, app dictionaries, Diary entry button, and direction handling remain intact.
- No Diary feature, button, note/photo data, storage key, PIN/recovery logic, APK, package identity, or signing data was changed.
- Backups created and re-fetched/readable before editing:
  - backups/web115-before-diary-home-language-screen-2026-11-12.html
  - backups/diary-web115-before-diary-home-language-screen-2026-11-12.html
  - backups/latest-before-web116-diary-home-language-screen-2026-11-12.json
  - backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-web116-diary-home-language-screen-2026-11-12.md
- Source commit: 7d545f38a66f4bb2b3d3def4ef29a94f3ec50164. Web-only workflow run 43244545952 completed with success; its publish job and all steps passed.
- Final re-fetch: source and diary-web/index.html are byte-identical, Git blob SHA 00c5dda6f514bf92d39cf81cf0e2c51f47021513. Independently recalculated UTF-8 SHA-256 9899c9df540ca5f845344c151b2f2303c16204c68796752fcbd558eda47515fb; matched the live latest.json value. Live webVersion is 116.
- APK remains 1.0.135 / versionCode 134; no APK rebuild. The 10-language string coverage and workflow/feed integrity were checked. Physical-device language switching is still pending: use Me → Check for Updates, then select each language and confirm the heading, subtitle, and language label change together.


# Web Update 117 — Diary home subtitle wording and bold 3D finish (2026-11-12)

- User requested replacing the Roman home subtitle with the exact wording `Notes, Yadein Aur Apni Baate Likhne Ki Diary`, translating the replacement according to the selected language, and making the subtitle bold with a raised 3D text effect.
- Changed only the localized `subtitle` value in the existing `applyDiaryHomeLanguage()` home-screen copy for the 10 already-supported languages (Roman English, English, Hindi, Urdu, Arabic, Bengali, Gujarati, Marathi, Tamil, Telugu). Added one isolated `diary-home-subtitle-bold-3d` CSS rule targeting only `.diary-home p`; no layout dimensions, language selector, app dictionaries, Diary entry button, notes/photos, storage, PIN/recovery, APK, package identity, or signing files were changed.
- Backups created before editing and re-fetched byte-for-byte/readable:
  - `backups/web-source-index-before-home-subtitle-bold-3d-2026-11-12.html`
  - `backups/diary-web-index-before-home-subtitle-bold-3d-2026-11-12.html`
  - `backups/latest-before-home-subtitle-bold-3d-2026-11-12.json`
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-home-subtitle-bold-3d-2026-11-12.md`
- Source update commit: `15e157562e88e23f49a20b2e7106cc191c753017`. GitHub Actions web-only publish run `43247148040` (run 106) completed with success; the publish job and all listed steps passed. Publisher commit: `91a39248e9478e2765d7a98adab46831673e8c9d`.
- Post-publish re-fetch: `web-source/index.html` and `diary-web/index.html` are byte-identical, Git blob SHA `35cd6fd9c4405bf8fefe2c7ee11490d0e036460e`, UTF-8 size 263,162 bytes. Independently calculated SHA-256 `e30a576cb937251039081d048179f3b6c3cc7a493feae2165463c0e318c495da` matches live `latest.json` `webSha256`; live webVersion is `117`.
- APK remains `1.0.135` / versionCode `134`, package `com.personal.diaryapp`; no APK rebuild. Workflow's web-only HTML/feed verification and JSON validation passed. Static inspection confirmed all 10 subtitle dictionary entries were changed once and the isolated 3D CSS rule appears once. Physical-device visual/language verification is pending; use **Me → Check for Updates**, then check the welcome subtitle in the selected languages. Do not claim phone testing until user confirms.
- Rollback: restore `web-source/index.html` and `diary-web/index.html` from the two Web 116 HTML backups above, and restore `latest.json` from `backups/latest-before-home-subtitle-bold-3d-2026-11-12.json`; retain this Register backup as the pre-entry record.



# Web Update 118 — Bold 3D styling for the Diary entry button (2026-11-12)

- User asked to make the three visible elements of the Diary entry button bold with a 3D effect: 📒 icon, localized “Meri Diary” title, and localized “Apne Notes Likhne Aur Search Karne Yaha Tap Kare” subtitle.
- Before editing, re-fetched and read the Master Register, latest.json, source, and mirror. Source and mirror were identical at Web 117. Created and re-fetched byte-identical backups:
  - `backups/web-source-index-before-diary-entry-bold-3d-2026-11-12.html`
  - `backups/diary-web-index-before-diary-entry-bold-3d-2026-11-12.html`
  - `backups/latest-before-diary-entry-bold-3d-2026-11-12.json`
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-diary-entry-bold-3d-2026-11-12.md`
- Added one isolated CSS block `diary-entry-button-bold-3d` scoped only to `#diaryMyNotesEntry` title, subtitle, and icon. The same selectors apply to all localized text as the existing `installEntry()` replaces title/subtitle according to the selected language. No wording, language dictionary, button dimensions, click handler, note/photo data, storage, PIN/recovery, APK, package identity, or signing files were changed.
- Source commit: `4501656ae40a62cb14c32b06e810f36a4557c352`. GitHub Actions web-only publish run `43248392917` (run 107) completed with **success**; publish job and all steps passed.
- Post-publish re-fetch verified source and `diary-web/index.html` are byte-identical; Git blob SHA `fb2075878ef553b80e4ea05c8e651a8e4d658167`. Live `latest.json` reports webVersion `118` and web SHA-256 `73c38c4b50c32dc6a0cb4a51395fdfe4362cd4345efe85dced274cffb4b20c00`; the successful publish workflow generated the mirror and feed hash after validating the HTML and JSON. APK remains `1.0.135` / versionCode `134`; no APK rebuild.
- Physical phone visual check remains pending. User should open **Me → Check for Updates** and inspect the Diary entry button. Do not claim phone verification.
- Rollback: restore `web-source/index.html` and `diary-web/index.html` from the two HTML backups above and `latest.json` from its backup; this Register backup is the pre-entry record.


# Web Update 119 — Animated tap indicator for the Diary entry (2026-11-12)

- User approved adding a clear tap sign beside the localized **Meri Diary** title. Added one isolated CSS pseudo-element after the title: a small pointing-hand emoji (👆) with a gentle tap/bounce motion. The cue automatically follows the existing localized title in all supported languages; reduced-motion accessibility preference disables the animation.
- No title/subtitle wording, language dictionaries, icon, button size/layout, click handler, notes/photos, storage, PIN/recovery, APK, package identity, or signing data was changed.
- Pre-edit backups created and re-fetched/readable:
  - `backups/web-source-index-before-tap-indicator-2026-11-12.html`
  - `backups/diary-web-index-before-tap-indicator-2026-11-12.html`
  - `backups/latest-before-tap-indicator-2026-11-12.json`
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-tap-indicator-2026-11-12.md`
- Source commit: `fd4b22d01165d747d7545a473f3fd2113b12ad1c`. Web-only publish workflow run `43249661987` (run 108) completed with **success**; all publish job steps passed.
- Post-publish re-fetch verified `web-source/index.html` and `diary-web/index.html` are byte-identical with Git blob SHA `6bedf161736ab417291a560ab683fa7c613b621e`. Independently calculated UTF-8 SHA-256 `01bc624e78f33f8fd8f3596e26f159651bcee9003ca6dea190fb4af3c5372f55` passed the standard `abc` test vector and matches live `latest.json`. Live webVersion is `119`.
- APK remains `1.0.135` / versionCode `134`, package `com.personal.diaryapp`; no APK rebuild or signing operation. Phone-side visual confirmation is pending; use **Me → Check for Updates**, then check that the pointing-hand cue appears beside Meri Diary and gently moves.
- Rollback: restore both HTML files from the two pre-edit HTML backups above and restore `latest.json` from `backups/latest-before-tap-indicator-2026-11-12.json`; retain the Register backup as the pre-change record.


# Web Update 121 — Larger directional tap indicator for the Diary entry (2026-11-12)

- User asked to make the pointing hand larger and aim it toward the localized **Meri Diary** title. Updated the existing isolated tap cue from a small hand after the title to a larger right-pointing hand before the title, with a gentle horizontal nudge animation. For right-to-left title direction, the cue switches to a left-pointing hand so it still points toward the title. Reduced-motion accessibility preference still disables the animation.
- Change is limited to the Diary entry title pseudo-element CSS. No wording, language dictionaries, icon, layout dimensions, button/click behavior, notes/photos, storage, PIN/recovery, APK, package identity, or signing data changed.
- Pre-edit backups created and re-fetched byte-for-byte:
  - `backups/web-source-index-before-larger-right-pointing-cue-2026-11-12.html`
  - `backups/diary-web-index-before-larger-right-pointing-cue-2026-11-12.html`
  - `backups/latest-before-larger-right-pointing-cue-2026-11-12.json`
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-larger-right-pointing-cue-2026-11-12.md`
- Final source commit: `31a5f1cd14dbdce054097ad0ad9e244ec03a7df3`. Final web-only publish workflow run `43250593694` (run 110) completed with **success**; all publish steps passed.
- Post-publish re-fetch: source and `diary-web/index.html` are byte-identical, Git blob SHA `2e24d7aeef5a3bb481686d24c6831a4f2fefdb3e`. Independently calculated UTF-8 SHA-256 `9625b8563152a1883ac934411f3e260c3b07a62ccbf5bf1e492112fbab169648` matches live `latest.json` `webSha256`; live webVersion is `121`.
- APK remains `1.0.135` / versionCode `134`, package `com.personal.diaryapp`; no APK rebuild or signing changes. Physical phone visual confirmation remains pending. Use **Me → Check for Updates** and verify that the larger hand points toward the Diary title in both left-to-right and right-to-left language layouts.
- Rollback: restore both HTML files from the two pre-edit HTML backups above and `latest.json` from `backups/latest-before-larger-right-pointing-cue-2026-11-12.json`; retain the Register backup as the pre-edit record.


# Web Update 122 — Center Diary title directly beneath its icon (2026-11-12)

- User asked to place the localized **Meri Diary** title properly directly under the 📒 icon.
- Added one isolated CSS rule block, `diary-home-icon-title-alignment`, to center the icon and heading on the same vertical axis and reduce the gap between them. The heading remains directly below the icon for all supported languages. No wording, subtitle, language selection, entry button, tap indicator, click behaviour, notes/photos, storage, PIN/recovery, APK, package identity, or signing data changed.
- Backups created before editing and re-fetched/readable: `backups/web-source-index-before-icon-title-alignment-2026-11-12.html`, `backups/diary-web-index-before-icon-title-alignment-2026-11-12.html`, `backups/latest-before-icon-title-alignment-2026-11-12.json`, and `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-icon-title-alignment-2026-11-12.md`.
- Source commit: `34238ca9912be8da672aaac5b03bd09ec2737cd2`. Web-only publish workflow run `43251898462` completed with **success**; checkout, publish verification and final job steps passed.
- Post-publish source and `diary-web/index.html` were re-fetched and verified byte-identical, Git blob SHA `0696ac1c98e44babe1097de5e1119dc85fbd1e10`. Independently computed UTF-8 SHA-256 `1e640d2394f472e18ba1b091b3fc70f0eb3d27f259d361917332ec56f374ebe1` passed the standard `abc` test vector and matches live `latest.json`. Live webVersion is `122`.
- APK remains `1.0.135` / versionCode `134`, package `com.personal.diaryapp`; no APK rebuild or signing operation. Physical-device visual verification is pending: use **Me → Check for Updates** and confirm 📒 and Meri Diary are centered, with the title immediately below the icon.
- Rollback: restore both HTML files from the two pre-edit HTML backups above and `latest.json` from `backups/latest-before-icon-title-alignment-2026-11-12.json`; retain the Register backup as the pre-edit record.


# Web Update 123 — Correct Diary entry button vertical stacking (2026-11-12)

- User reported that Web Update 122 had not changed the visible layout. Inspection confirmed the mistake: the previous CSS targeted the unrelated `.diary-home h1`, while the visible three-line Diary entry is dynamically built inside `#diaryMyNotesEntry` using `.diary-more-icon`, `#diaryMyNotesEntryTitle`, and `#diaryMyNotesEntrySub`.
- Corrected only those actual button children: force the icon, localized Diary title, and subtitle into three separate centered block rows in that exact order, with a small consistent vertical gap. Existing title pointer cue, typography, button dimensions/design, click handler, language translations, notes/photos, storage, PIN/recovery, APK and package identity remain unchanged.
- Before-edit backups were created and verified readable: `backups/web-source-index-before-entry-button-stack-fix-2026-11-12.html`, `backups/diary-web-index-before-entry-button-stack-fix-2026-11-12.html`, `backups/latest-before-entry-button-stack-fix-2026-11-12.json`, and `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-entry-button-stack-fix-2026-11-12.md`.
- Source commit: `c4bd996653d26bb8af2a034f35d74d6c94e72081`. Web-only publish workflow run `43252894674` (run 112) completed with **success**; checkout, publish verification, and final job steps passed.
- Post-publish source and `diary-web/index.html` were re-fetched and verified byte-identical, Git blob SHA `6d73e0464b9e245237afa2cfd574b9be5938f89d`. Independently computed UTF-8 SHA-256 `64e6aac4bf792d777fcd33bba009bc7314a167aa8fc7a628b8b29ce4ab6bf12e` matches live `latest.json`. Live webVersion is `123`.
- APK remains `1.0.135` / versionCode `134`, package `com.personal.diaryapp`; no APK rebuild or signing operation. Physical-device visual verification is still pending. Use **Me → Check for Updates** and confirm the visible button reads icon, title, subtitle vertically.
- Rollback: restore both HTML files from the two pre-edit HTML backups above and `latest.json` from `backups/latest-before-entry-button-stack-fix-2026-11-12.json`; retain the Register backup as the pre-edit record.



# Web Update 124 — Center Diary title beneath icon; move tap cue after title (2026-11-12)

- User reported that the Diary title still did not sit directly below the 📒 icon and specified the intended arrangement: icon on its own top row, localized Diary title centered directly below it, left-pointing 👈 cue after the title on the same line, then the subtitle.
- Inspection confirmed the entry is dynamically built with the icon, title span, and subtitle as direct children of `#diaryMyNotesEntry`. The prior cue was a `::before` inline element, which was included in the centered title line and could visually shift the title away from the icon's center.
- Replaced only the tap-indicator CSS: title now uses its content width and is centered as a flex child directly beneath the centered icon; the old leading hand is suppressed; a left-pointing hand is positioned after the title without participating in title centering. The cue animation and reduced-motion support remain. Subtitle, button dimensions/design, click handler, language text, notes/photos, storage, PIN/recovery, APK, package identity, and signing data are unchanged.
- Before-edit backups were created and verified readable: `backups/web-source-index-before-title-left-hand-after-2026-11-12.html`, `backups/diary-web-index-before-title-left-hand-after-2026-11-12.html`, `backups/latest-before-title-left-hand-after-2026-11-12.json`, and `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-title-left-hand-after-2026-11-12.md`.
- Source commit: `ead8e5976478ecc57964b36280e721d62bb6050b`. Web-only publish workflow run `43254476583` (run 113) completed with **success**.
- Post-publish source and `diary-web/index.html` were re-fetched and verified byte-identical, Git blob SHA `629e5689b7f699469062fe2a7b4d0f238d52bb96`. Live `latest.json` reports webVersion `124` and webSha256 `4ec6b2af000a8fda0377470b9c01d9cc5a9e376bb6bb152d37f58879cda7faee`.
- APK remains `1.0.135` / versionCode `134`, package `com.personal.diaryapp`; no APK rebuild or signing changes. Physical-phone visual confirmation remains pending.
- Rollback: restore both HTML files from the two pre-edit HTML backups above and `latest.json` from `backups/latest-before-title-left-hand-after-2026-11-12.json`; retain the Register backup as the pre-edit record.


# Web Update 125 — Correct Urdu and Arabic Diary tap cue direction and position (2026-11-12)

- User reported that the pointing-hand cue appeared in the wrong place for Urdu and Arabic. Inspection confirmed applyDiaryTextDirection() already sets the document root to dir="rtl" for both languages, but the existing cue always displayed 👈 and used only the LTR placement/animation.
- Added one narrowly scoped RTL CSS override: when the document root is RTL, the cue changes to 👉, moves to the visual left of the title (the end of the RTL title line), and animates rightward toward the title. Roman English, English, Hindi and other LTR layouts retain the existing 👈 cue on the title's right side. The language-direction logic itself was not changed.
- Pre-edit backups were created and re-fetched/readable:
  - backups/web-source-index-before-rtl-tap-cue-fix-2026-11-12.html
  - backups/diary-web-index-before-rtl-tap-cue-fix-2026-11-12.html
  - backups/latest-before-rtl-tap-cue-fix-2026-11-12.json
  - backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-rtl-tap-cue-fix-2026-11-12.md
- Source commit: 795ee75670a96e6ae500fb791121d43f53c1febb. Web-only publish workflow run 43255529653 (run 114) completed with success; checkout, HTML/feed publish, and final job steps passed.
- Post-publish re-fetch verified web-source/index.html and diary-web/index.html are byte-identical, Git blob SHA 6fd73ae538b8c96f7c95935e451a4bbb2d9fe007. Live latest.json reports webVersion 125 and web SHA-256 e138bcde5c96a1fbd4c12baa836999df87b6dec314abb391032a37606c7d3d16. APK remains 1.0.135 / versionCode 134; no APK rebuild.
- No Diary wording, language dictionaries, button click behaviour, notes/photos, storage, PIN/recovery, APK, package identity, or signing data changed. Physical-device visual confirmation remains pending; apply via Me → Check for Updates, then check Urdu and Arabic separately.
- Rollback: restore both HTML files from the two pre-edit HTML backups above and latest.json from backups/latest-before-rtl-tap-cue-fix-2026-11-12.json; retain the Register backup as the pre-edit record.


# Web Update 126 — Anchor Urdu and Arabic hand directly to the title's physical left (2026-11-12)

- User reported that the Urdu/Arabic pointing hand was still in the wrong position and clarified it should sit immediately to the left of the Diary title.
- Inspected the prior RTL rule: using logical inset-inline-end with a positive 100% offset resolved to the wrong physical side in this absolutely positioned pseudo-element. Corrected only the RTL override to use an explicit physical right offset (right: calc(100% + 8px)), anchoring the 👉 hand directly outside the title's left edge. LTR placement remains unchanged.
- Pre-edit source, mirror, feed and register backups were created and re-fetched/readable:
  - backups/web-source-index-before-rtl-cue-left-anchor-fix-2026-11-12.html
  - backups/diary-web-index-before-rtl-cue-left-anchor-fix-2026-11-12.html
  - backups/latest-before-rtl-cue-left-anchor-fix-2026-11-12.json
  - backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-rtl-cue-left-anchor-fix-2026-11-12.md
- Source commit: c41950c79c918f608c0dfd8cbe7a9d9789aa587c. Web-only workflow run 43256323665 (run 115) completed successfully; publish/verification job succeeded.
- Post-publish source and mirror re-fetched with identical Git blob SHA 74c047fec88eba94f0f1a241a94a3910f4fbe1a3. Live feed reports webVersion 126 and webSha256 5478676b8ed740838567af953c7a503183bf8b5edd74379a010001e9ed4bca7d. APK remains 1.0.135 / versionCode 134; no APK rebuild.
- Only the RTL cue anchor was changed. No language text, LTR cue, click handler, notes/photos, storage, PIN/recovery, package identity, APK or signing data changed. Physical-device visual confirmation remains pending; apply via Me → Check for Updates.
- Rollback: restore both HTML files from the two pre-edit HTML backups above and latest.json from backups/latest-before-rtl-cue-left-anchor-fix-2026-11-12.json; retain the Register backup as the pre-edit record.


# Web Update 127 — complete translation coverage audit across all 10 Diary languages (2026-11-12)

- User requested checking every language so all visible Diary wording matches its selected language, and completing any remaining translation work.
- Read the live Register and latest.json. The Register header still showed stale 126/126 values; the live feed was authoritative and showed APK 1.0.135 / versionCode 134 and webVersion 127. Corrected the header above and recorded the discrepancy here.
- Audited the translation dictionaries in web-source/index.html: Roman English, English, Hindi, Urdu, Arabic, Bengali, Gujarati, Marathi, Tamil and Telugu. The shared English dictionary contains 129 translation keys. All 10 language dictionaries now explicitly cover all 129 keys; no base translation keys are missing.
- The only remaining inherited-English strings found in the seven non-Latin-script dictionaries were recoveryPinPrompt and recoveryVerify. Added localized wording for these two recovery prompts in Urdu, Arabic, Bengali, Gujarati, Marathi, Tamil and Telugu. PIN remains as the technical acronym where appropriate. Existing translated wording and the other 127 labels/messages were left unchanged.
- Pre-edit backups were created and verified readable:
  - backups/web-source-index-before-all-language-audit-fix-2026-11-12.html
  - backups/diary-web-index-before-all-language-audit-fix-2026-11-12.html
  - backups/latest-before-all-language-audit-fix-2026-11-12.json
  - backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-all-language-audit-fix-2026-11-12.md
- Translation source commit: c3965cf497bacc66a255570f3d6864f621fef363. Web publish workflow run 43262992695 completed successfully; all publish job steps passed. The workflow published webVersion 127 and did not rebuild the APK.
- Post-publish source and diary-web/index.html were re-fetched and are byte-identical; both Git blob SHA: ffd03bfece972a5f51ea1b9a6179d9858076b541. Independently computed UTF-8 SHA-256: 7340af8197aca28e59dc20d3f75d4b0901fea18d518edea94a174cae2e1bd8e3, exactly matching live latest.json webSha256.
- Live feed remains APK 1.0.135 / versionCode 134, package com.personal.diaryapp; APK URL and APK SHA-256 unchanged. No APK rebuild, signing change, storage/data change, PIN/recovery logic change, or feature/UI redesign.
- Physical-device verification remains pending. User should install Web Update 127 through Me → Check for Updates, then select each of the 10 languages and review the Diary home screen, note editor, search, buttons, PIN/recovery prompts and recently-deleted messages. Do not claim phone-side verification until the user confirms.
- Rollback: restore both HTML files from the two pre-edit HTML backups above and latest.json from backups/latest-before-all-language-audit-fix-2026-11-12.json; retain the Register backup as the pre-edit record.


# Web Update 131 — full My Diary UI language audit and localization pass (2026-11-12)

- User requested a detailed check of the entire Diary so every visible section and message follows the selected language, and any remaining work be completed.
- Starting live state: Web Update 127; APK 1.0.135 / versionCode 134; package com.personal.diaryapp. Scope was web-only localization. No APK, Android native source, package identity, signing, storage keys, note/photo data, PIN/recovery logic, or feature behaviour was changed.
- Created and verified readable pre-edit backups:
  - backups/web-source-before-full-language-audit-2026-11-12.html
  - backups/diary-web-before-full-language-audit-2026-11-12.html
  - backups/latest-before-full-language-audit-2026-11-12.json
  - backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-full-language-audit-2026-11-12.md
- Re-audited all 10 language dictionaries and all 129 shared base translation keys. The seven non-Latin-script dictionaries had no remaining exact English-value fallbacks in the audited base strings; PIN remains an intentional technical acronym and My Diary remains the app name.
- The full-screen scan found additional UI strings outside the main dictionary that had remained in English/Roman text. Added 15 localized labels/messages to all 10 languages: Me menu, Check for Updates, Refresh, refresh success/failure, update-unavailable message, Share App, Calendar, Calendar accessibility label, previous/next month, empty-day message, note-count text, 4-digit PIN placeholder, and Open Diary accessibility label.
- Matched the welcome-screen subtitle in every language to that language's actual Diary entry-button subtitle. Restored the user's requested Roman wording exactly: “Apne Notes Likhne Aur Search Karne Yaha Tap Kare”.
- Calendar month, weekday names, selected date, note dates, calendar day numbers and note counts now use the selected app language/locale, including localized numerals where supported. The calendar's note-empty message and month navigation labels are localized.
- Improved 17 Roman-English labels that were still English-only (including pin/unpin, share, cover/detail photo, edit/delete, backup/restore, copy, lock/unlock, forgot PIN and PIN copy). Also localized Roman font-size/category/recovery/storage wording. Corrected the English dictionary's Remove Note and Category labels so English no longer displays Roman wording.
- Scanned remaining direct UI text assignments and common hardcoded labels. Remaining literal strings found by the scan are language-neutral formatting controls/symbols (B/I/U, px, ×), blank status resets, and the language names in the language selector; no further user-facing hardcoded English button, calendar, or error strings were found in the audited paths.
- Source commits in this localization pass: 8ab020948f9fc343a70865d18668c4a643821be5, b477d41c0205ab3e846358490e9c2c94d4d532ad, 65279bbb2192781689f65d2563ab3519521d3d08, and final source commit 78f84a9f97bbe645c012eb78b156c6e5801047a6. Final web-only publish workflow run 43267249602 completed successfully; all job steps passed.
- Post-publish verification: web-source/index.html and diary-web/index.html are byte-identical, Git blob SHA 02dc650f334c14197d2ec36c6418928f365722bb. Independently computed exact UTF-8 SHA-256 29139113be913ace26d740a77572617d52b48e9f35d96b1eae56eb52941173c matches live latest.json.webSha256. Live feed reports webVersion 131.
- APK remains 1.0.135 / versionCode 134, package com.personal.diaryapp; APK URL and APK SHA-256 c3e312ec7cd8504bab68c12f9df996c8d10018670d0d1ccef9373408d4ddba4d are unchanged. No APK rebuild or signing operation occurred.
- Automated/source audit and publishing are complete; physical-device visual and native-speaker wording review remain pending. User should apply Web Update 131 using Me → Check for Updates and inspect all 10 language selections, including Diary home, note editor, search, Me menu, Calendar, Recently Deleted, note lock, Diary PIN/recovery, backup/restore, and error messages. Do not claim phone-side testing until user confirms.
- Rollback: restore web-source/index.html and diary-web/index.html from the two pre-edit HTML backups above and latest.json from backups/latest-before-full-language-audit-2026-11-12.json; retain the Register backup as the pre-edit record.


---

# My Diary 1.0.136 / Web Update 133 — One-press Android Back exits the whole Diary (2026-11-12)

- User request: from any nested Diary section, one Android Back press must close the complete Diary and return to the screen underneath; users should not have to press Back repeatedly to unwind Diary navigation.
- Starting live state: APK **1.0.135 / versionCode 134**, webVersion **132**, package `com.personal.diaryapp`; starting main commit `2effcdd79bc4375a5f018afac014b88c13e3d8ff`.
- Scope: only the Diary overlay close callback, native Android Activity Back handling generated by `scripts/add_diary_app_actions.py`, and the APK build workflow/version metadata. The supplied Android project ZIP, unrelated screens, note editor, note data/storage, photos, PIN/recovery records, permissions, package identity and signing identity were not changed.
- Behaviour change:
  - `web-source/index.html` exposes `window.__diaryCloseOverlayFromAndroid`; when the Diary overlay is open, it calls the existing `closeOverlay(true)` path to close the whole overlay directly without stepping backward through nested in-Diary history.
  - `scripts/add_diary_app_actions.py` updates the native `onBackPressed()` handler to ask that callback first. If the Diary is open, it closes the complete overlay and clears the single-page WebView's nested history. If the Diary is not open, the existing WebView history / Activity Back behaviour is retained.
- Verified pre-edit backups on branch `backup/pre-one-press-diary-exit-2026-11-12`:
  - `backups/web-source-before-one-press-diary-exit-2026-11-12.html`
  - `backups/add_diary_app_actions-before-one-press-diary-exit-2026-11-12.py`
  - `backups/build-diary-from-zip-before-one-press-diary-exit-2026-11-12.yml`
  - `backups/latest-before-one-press-diary-exit-2026-11-12.json`
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-one-press-diary-exit-2026-11-12.md`
- Web publication: Web Update **133**, workflow run **43276059809**, completed successfully. Source and published mirror are byte-identical; both Git blob SHA `81c75f34835dd7d51cac6da32b7e6729f6380aaf`. Independently recalculated UTF-8 SHA-256 `3cb78b3dc27621fa277323b4c5eec729fe60a1adc80921290795be17268116bd` matches live `latest.json.webSha256`.
- APK publication: workflow run **43276194581**, completed successfully. Debug build, signed Release build, certificate check, publish step and artifact uploads all passed. The release certificate matched the previously trusted SHA-256 fingerprint `23A4E93F3C7911DCE18389EA583548700C6AD6A3759707F1CD222D07E2408B5A`.
- Live feed now reports APK **1.0.136 / versionCode 135**, webVersion **133**, package `com.personal.diaryapp`, APK URL `https://raw.githubusercontent.com/amuazzinxyz-ops/My-Diary-Updates/main/My-Diary-1.0.136.apk`, APK SHA-256 `6fc74ca82888fed4121cc352c1846ec8c6a7063e2d2a33fbe032726f7a244348`. The signed workflow artifact was downloaded and independently hashed; it exactly matches the live feed checksum.
- Post-publish checks: source and mirror re-fetched and confirmed identical; feed package/version/URL/hash checked; backup files re-fetched and confirmed readable. No APK signing secret or keystore was changed.
- Phone verification remains **pending**. User should apply APK **1.0.136** through the existing **Me → Check for Updates** path, then open Diary, enter nested sections such as note editor / Me / Recently Deleted, and press Android Back once. Confirm that the entire Diary closes immediately and returns to the underlying screen. Do not claim physical-device testing until user confirms.
- Rollback reference: backup branch above; pre-change main commit `2effcdd79bc4375a5f018afac014b88c13e3d8ff`; pre-change web feed backup listed above. Preserve all user data; do not clear app data or uninstall as a rollback shortcut.


---

# Web Update 136 — Add colour choices inside all three existing image buttons (2026-11-13)

- User request: keep the existing Image Select buttons (no separate Colour Select button); when tapped, each existing button should offer both image selection and colour selection.
- Starting live state: APK **1.0.136 / versionCode 135**, webVersion **133**, package `com.personal.diaryapp`. Live `latest.json` was read before editing.
- Scope: web-only Diary editor, saved-note rendering, import compatibility and share-image rendering. No native Android source, APK, package identity, signing identity, storage keys, PIN/recovery logic, updater logic, or unrelated screens were changed.
- Added the same in-button chooser to all three existing controls: **Note Cover Photo**, **Details Image**, and **Photo Lagayein**. Each offers **Choose Image**, **Solid Colour**, or **Gradient Colour** (two independently selectable colours). No separate top-level colour button was added.
- Selected cover/detail colours are layered over the chosen image (without replacing it), or used as a background when no image is selected. The attached-photo colour is shown as a frame around the photo. Colour settings are saved with each note, restored when editing, retained in note backup import/export, shown on saved notes, and included in the composed share image.
- Added localized chooser labels for all 10 supported languages: Roman English, English, Hindi, Urdu, Arabic, Bengali, Gujarati, Marathi, Tamil and Telugu.
- Backups were created and re-fetched/readable on branch `backup/pre-image-button-colour-options-2026-11-13`:
  - `backups/web-source-before-image-button-colour-options-2026-11-13.html`
  - `backups/diary-web-before-image-button-colour-options-2026-11-13.html`
  - `backups/latest-before-image-button-colour-options-2026-11-13.json`
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-image-button-colour-options-2026-11-13.md`
- Final source commit: `ccfafe5425b5765e47d1ce96270e70a99586c0a7`. Web-only publisher workflow run **43366404020** (run 126) completed with **success**. An intermediate syntax issue in an earlier attempt was corrected before the final successful run; the final embedded scripts both parse successfully.
- Post-publish verification: `web-source/index.html` and `diary-web/index.html` are byte-identical; both Git blob SHA `c150cb5c0777f1b2e84c0fac96ee477c5b5b782f`. Independently computed UTF-8 SHA-256 `cce2170ace3f45721a5ddd8ebc79b1908d5119fce636941256c8f24be2903c93` matches live `latest.json.webSha256`. Live webVersion is **136**.
- APK remains **1.0.136 / versionCode 135**, package `com.personal.diaryapp`; APK URL, checksum, certificate and signing identity are unchanged. No APK rebuild or signing operation occurred.
- Static checks passed: both inline scripts parse; SHA-256 implementation passed the standard `abc` test vector; all 10 language dictionaries contain the new chooser labels; source/mirror/feed checks passed. Actual Android phone interaction and visual verification remain **pending**.
- Phone test: use **Me → Check for Updates**. In a new note, tap each of the three existing image buttons. Confirm its menu offers image, solid colour and gradient; choose colours, attach images, save, reopen/edit, and share the note. Also check an older note to confirm its existing images still display normally. Do not claim phone-side testing until the user confirms.
- Rollback: use the backup branch and the exact pre-change HTML, feed and Register files listed above; preserve all local notes and app data.


---

# Web Update 137 — Purpose-specific design panels inside the three image buttons (2026-11-13)

- User clarified that the three existing image buttons should open attractive, clearly explained panels, with the image and colour choices visible inside each panel.
- Starting live state: APK **1.0.136 / versionCode 135**, webVersion **136**, package `com.personal.diaryapp`. Read the live feed and Master Register before editing.
- Scope: web-only Diary image-picker panel UI, localized labels/descriptions and related CSS. No native Android source, APK, package/signing identity, updater logic, note storage keys, PIN/recovery logic, or unrelated features were changed.
- All three existing controls now open a purpose-specific premium-style panel:
  1. **Note Cover Photo** — explains that it decorates the note-name/title box.
  2. **Details Image** — explains that it decorates the writing/details box.
  3. **Photo Lagayein / Attach Photo** — explains that it attaches a separate photo to the note and styles its frame.
- Each panel displays **Choose Image**, **Solid Colour**, and **Gradient Colour** choices within the same panel. No separate Colour button or extra image button was added. Existing colour selection and persistence logic from Web Update 136 remains in place.
- Added panel headings and explanatory descriptions for all 10 supported languages: Roman English, English, Hindi, Urdu, Arabic, Bengali, Gujarati, Marathi, Tamil and Telugu.
- Verified pre-edit backups on branch `backup/pre-image-button-pamphlet-panels-2026-11-13`:
  - `backups/web-source-before-image-button-pamphlet-panels-2026-11-13.html`
  - `backups/diary-web-before-image-button-pamphlet-panels-2026-11-13.html`
  - `backups/latest-before-image-button-pamphlet-panels-2026-11-13.json`
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-image-button-pamphlet-panels-2026-11-13.md`
- Source change commit: `7e042007a60e0db45d140cbf117430fbe0bb34c5`. Web-only workflow run **43367264608** (run 127) completed successfully.
- Post-publish verification: source and mirror are byte-identical; both Git blob SHA `fe20d5c8e6f15e6790cdfd75a86b81026b5aa461`. Independently calculated UTF-8 SHA-256 `113d77a5e1aa74d0358f978dfa71583bfdf806128b15ff16fdb9b6cbd419ad9d` exactly matches live `latest.json.webSha256`; live webVersion **137**.
- Both inline scripts parse successfully. All 10 language dictionaries contain the seven panel heading/description labels.
- APK remains **1.0.136 / versionCode 135**, SHA-256 `6fc74ca82888fed4121cc352c1846ec8c6a7063e2d2a33fbe032726f7a244348`; no APK rebuild or signing operation occurred.
- Phone-side visual and interaction testing remains **pending**. Use **Me → Check for Updates**, tap each of the three existing buttons, and confirm the correct purpose panel and its three choices appear. Test image selection and colour selection in each panel.
- Rollback: use the verified backup branch and exact pre-change files listed above. Preserve all local notes, photos and app data.


---

# Web Update 138 — Separate ready-made pamphlet chooser in all three Diary image panels (2026-11-13)

- User clarified that the requested pamphlet choice must be a **separate option**, not merely the existing image/colour controls. User approved proceeding.
- Starting live state: APK **1.0.136 / versionCode 135**, webVersion **137**, package `com.personal.diaryapp`. Live `latest.json` and Master Register were read before editing.
- Scope: web-only `web-source/index.html`; the existing publisher synchronizes `diary-web/index.html` and updates `latest.json`. No native Android source, APK, package/signing identity, updater logic, note storage keys, PIN/recovery logic, or unrelated features changed.
- Added a distinct **Pamphlet Chunein / Choose Pamphlet** option inside each of the three existing image panels: Note ka Cover Photo, Details Image, and Photo Lagayein. The option opens a separate ready-made design gallery with four selectable presets: Royal Gold, Purple Bloom, Emerald Garden and Ocean Blue. Selecting a preset applies its two-colour gradient to the relevant existing cover field, details field, or attached-photo frame.
- Existing **Choose Image**, **Solid Colour**, and **Gradient Colour** options remain available and unchanged. No new top-level editor button was added; the pamphlet option is inside each existing panel. All six new labels were translated in all 10 supported languages.
- Pre-edit backup branch: `backup/pre-pamphlet-chooser-2026-11-13`. Verified readable backup files:
  - `backups/web-source-before-pamphlet-chooser-2026-11-13.html`
  - `backups/diary-web-before-pamphlet-chooser-2026-11-13.html`
  - `backups/latest-before-pamphlet-chooser-2026-11-13.json`
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-pamphlet-chooser-2026-11-13.md`
- Source commit: `2ad2a044f7fd7bce0b44164b4fa24fc823ac73e1`. Web-only publisher workflow run **43368466848** (run 128) completed successfully.
- Post-publish verification: source and published mirror were re-fetched and have identical Git blob SHA `5cb65a2706d3e9165c05da43bbb8d75d8126ddc5`. Independently calculated SHA-256 over the exact UTF-8 source bytes: `01804fe61c88983e57833809fbcad705c2da75fc3ee88a948184c59420e064c3`, matching live `latest.json.webSha256`. Live webVersion **138**.
- Both inline scripts parse successfully. Each of the six new translation keys is present in all 10 language dictionaries. SHA-256 implementation was checked against the standard `abc` test vector. APK remains **1.0.136 / versionCode 135**, APK hash and package identity unchanged; no APK rebuild or signing operation.
- Physical-device visual and interaction verification remains **pending**. Use **Me → Check for Updates**, then open each of the three image panels, tap **Pamphlet Chunein**, choose each preset, and confirm it styles the intended field/photo frame. Also confirm the existing image, solid-colour and gradient-colour choices still work.
- Rollback: use the verified backup branch and exact pre-change files listed above. Preserve all local notes, photos and app data.


---

# Web Update 140 — Actual decorative ready-made pamphlet templates (2026-11-13)

- User clarified that “pamphlet” means fully designed, ready-made decorative templates commonly offered in other apps, not simple colour swatches or two-colour gradients. Replaced the previous four gradient swatches with real visual template previews and selectable designs.
- Starting feed before this task: APK **1.0.136 / versionCode 135**, webVersion **138**, package `com.personal.diaryapp`. This live Register, feed and current source were read before editing.
- Scope: web-only `web-source/index.html`; publisher synchronizes `diary-web/index.html` and updates `latest.json`. No native Android source, APK, package/signing identity, updater logic, note storage keys, PIN/recovery logic, or unrelated screens were changed.
- Each existing image button retains its own separate `Pamphlet Chunein` option and its own purpose-specific ready-made gallery:
  - **Note ka Cover Photo:** Floral, Islamic, Classic and Nature title-cover designs.
  - **Details Image:** Paper, lined writing page, Islamic and Nature writing-area designs.
  - **Photo Lagayein:** Polaroid, Royal, Floral and Modern photo-frame designs.
- Each gallery displays a miniature decorated layout preview, ornamentation, border and sample typography—not just a colour tile. Selecting a template applies the decorative background/frame to its matching editor field or attached photo.
- Template IDs are safely whitelisted and retained by the existing `cleanDiaryColour` normalization. Therefore selected template styling is saved with the note, restored when editing, carried through the existing note backup import/export path, applied to saved-note previews and reflected in the composed share artwork. Existing Choose Image, Solid Colour and Gradient Colour controls remain available.
- Added localized template chooser headings and four style labels in all 10 supported languages: Roman English, English, Hindi, Urdu, Arabic, Bengali, Gujarati, Marathi, Tamil and Telugu.
- Backups were created and readable on branch `backup/pre-real-pamphlet-templates-2026-11-13`:
  - `backups/web-source-before-real-pamphlet-templates-2026-11-13.html`
  - `backups/diary-web-before-real-pamphlet-templates-2026-11-13.html`
  - `backups/latest-before-real-pamphlet-templates-2026-11-13.json`
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-real-pamphlet-templates-2026-11-13.md`
- Final source commit: `85711d1aee91d364fce973dda0e4f02f0be27c0f`. Final web-only publishing workflow run **43369439756** (run 130) completed successfully. An earlier publish for the same task was superseded by a small canvas-rendering correction; run 130 is the final source version.
- Post-publish verification: source and mirror were re-fetched and have identical Git blob SHA `330c27bf9d12f50dcf06cab8be828e038a2ca20f`. Both inline JavaScript scripts parse successfully. Each of the six new chooser/label translation keys is present in all 10 language dictionaries. There are 12 distinct purpose-specific template choices across the three galleries.
- Independently computed SHA-256 over exact UTF-8 source bytes: `8188d5d65d9dd04393e49c0e85b400a0b18904f9c4c0b38ec091c1018f8050d6`, matching live `latest.json.webSha256`. Live webVersion **140**.
- APK remains **1.0.136 / versionCode 135**, checksum, URL and package unchanged; no APK rebuild or signing operation.
- Physical-device visual/interaction testing remains **pending**. User should use **Me → Check for Updates**, then open each of the three existing image buttons and inspect its distinct gallery, select a template, save/reopen the note, and test the existing image/solid/gradient options. Do not claim phone-side testing until user confirms.
- Rollback: use the backup branch and exact pre-change files listed above. Preserve all local notes, photos and app data.


---

# Web Update 142 — Finger drag and pinch-to-zoom image adjustment (2026-11-13)

- User approved touch adjustment for all three existing Diary image areas: Note Cover Photo, Details Image and attached Photo.
- Starting live state: APK **1.0.136 / versionCode 135**, webVersion **140**, package `com.personal.diaryapp`. Read the live source, feed and Master Register before editing.
- Scope: web-only Diary editor and note preview/share rendering in `web-source/index.html`; the publisher synchronized `diary-web/index.html` and updated `latest.json`. No APK, native Android code, package/signing identity, PIN/recovery logic, updater logic, or unrelated feature was changed.
- Added a separate **Ungli se Adjust Karein / Adjust with Finger** control inside each of the three existing image panels. When enabled, one finger drags the image to reposition it and two fingers pinch to zoom (up to 3×). Tap the control again to finish. The editor remains normally editable when adjustment mode is off.
- The crop position and zoom values are stored in the existing per-note cover/detail/photo colour settings, normalized safely for older notes, and restored when a note is reopened. The same crop is used in saved-note previews and the composed share image. Existing decorative pamphlet templates, image selection, solid colour and gradient colour choices remain in place.
- Added the adjustment button and usage hint in all 10 supported languages: Roman English, English, Hindi, Urdu, Arabic, Bengali, Gujarati, Marathi, Tamil and Telugu.
- Verified pre-edit backups on branch `backup/pre-finger-adjustment-2026-11-13`:
  - `backups/web-source-before-finger-adjustment-2026-11-13.html`
  - `backups/diary-web-before-finger-adjustment-2026-11-13.html`
  - `backups/latest-before-finger-adjustment-2026-11-13.json`
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-finger-adjustment-2026-11-13.md`
- Source commits: `b633b0967e98c6832afe031b1dafa05705560533` and final refinement `2d78e2b27e31c0f4d73bd273e744de62c75696a6`. Final web-only publisher workflow run **43372607691** completed successfully; all publish job steps passed. The preceding publish run **43372558034** also completed successfully; final source is the later commit above.
- Post-publish verification: `web-source/index.html` and `diary-web/index.html` are byte-identical; Git blob SHA `b9a7a01e1f226de50d01741ba8c5efa8eaa47663`. Both embedded JavaScript scripts parse successfully. All 10 language dictionaries contain the adjustment button text. Checks confirm the pointer drag/pinch handlers, saved crop data, new-note reset and all 12 existing pamphlet templates remain present.
- Live feed reports webVersion **142** and web SHA-256 `6d7ba9eaa51e60642d1176abc7278d46a58aaa76d1e7105446405c356d835101`. APK remains **1.0.136 / versionCode 135**, URL, SHA-256 and package unchanged; no APK rebuild or signing operation.
- Physical-device touch/visual testing remains **pending**. Use **Me → Check for Updates**, open each of the three image panels, choose an image or pamphlet, tap **Ungli se Adjust Karein**, drag with one finger and pinch with two fingers. Save and reopen the note and verify the crop remains. Do not claim phone-side testing until the user confirms.
- Rollback: use the backup branch and exact pre-change files listed above. Preserve all local notes, photos and app data.


---

# Web Update 143 — Android touch drag and pinch adjustment repair (2026-11-13)

- User reported that the finger-adjust button activated and the image appeared, but the image stayed fixed and could not be moved by touch.
- Starting live state: APK 1.0.136 / versionCode 135; webVersion 142; source commit `4b8e2829e4f374881d0ba6b47615a40acd2befee`. Live `latest.json` was authoritative; the stale status line above previously said webVersion 140 and has now been corrected to 143.
- Scope: web-only; changed only `bindDiaryFingerAdjust(target,kind)` in `web-source/index.html`. Added native Touch Events for Android touch dragging and two-finger pinch zoom; retained mouse/pen Pointer Events. Touch movement is handled at document level so dragging continues if the finger moves beyond the image/input boundary. Existing position/zoom state and paint functions remain in use.
- Explicitly untouched: pamphlet designs/chooser, image selection, editor layout, notes/photos data, save format, PIN/lock/recovery, language dictionaries, native Android source, APK, package identity, signing data and all other features.
- Pre-edit backup branch: `backup/pre-finger-drag-fix-2026-11-13`. Verified backup files:
  - `backups/web-source-before-finger-drag-fix-2026-11-13.html`
  - `backups/diary-web-before-finger-drag-fix-2026-11-13.html`
  - `backups/latest-before-finger-drag-fix-2026-11-13.json`
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-finger-drag-fix-2026-11-13.md`
- Source change commit: `20376daa52c530163f1085a648d4a4b54b146f7b`. Web publisher workflow run `43378304747` (run 133) completed with **success**.
- Post-publish verification: source and published mirror are byte-identical, both Git blob SHA `98d759b0b8b7637058affbba9307701bfd45d2ed`; independently calculated UTF-8 SHA-256 `745d8e5fb5d794fac62f613d0783b6f20bf208a8c22e0060b86d231f531bd7c1` matches live `latest.json.webSha256`; live webVersion is 143.
- APK remains `1.0.136` / versionCode `135`; no APK rebuild or signing operation. Phone-side drag/zoom test is **pending**; do not claim device testing until user confirms.
- Rollback: restore the verified pre-edit files from `backup/pre-finger-drag-fix-2026-11-13` if phone testing identifies a regression.


---

# Web Update 144 — Multi-finger pinch zoom repair (2026-11-13)

- User confirmed one-finger image dragging worked after Web Update 143, but two-/three-finger pinch zoom and zoom-out did not work.
- Starting live state: APK 1.0.136 / versionCode 135; webVersion 143; starting source commit `ddd716f1ba3d8e88b1ee911f8bc4bd4c8d79afd6`.
- Scope: web-only; replaced only `bindDiaryFingerAdjust(target,kind)` in `web-source/index.html`. Android touch-capable Pointer Events now handle each active pointer ID; legacy Touch Events remain as fallback. Pinch span is calculated from all active fingers around their centre, so two or three fingers can scale the image. Gesture baselines reset when fingers are added/removed to avoid jumps; one-finger drag is retained.
- Explicitly untouched: pamphlet designs/chooser, image selection, layout, note/photo storage, save format, PIN/lock/recovery, language dictionaries, native Android code, APK, package/signing identity, and unrelated features.
- Pre-edit backup branch: `backup/pre-pinch-zoom-fix-2026-11-13`. Verified readable backups:
  - `backups/web-source-before-pinch-zoom-fix-2026-11-13.html`
  - `backups/diary-web-before-pinch-zoom-fix-2026-11-13.html`
  - `backups/latest-before-pinch-zoom-fix-2026-11-13.json`
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-pinch-zoom-fix-2026-11-13.md`
- Source commit: `0d576d9fe53c580416febbfcee3eaac4349b0316`. Web publisher workflow run `43378989369` (run 134) completed successfully.
- Post-publish: source and mirror byte-identical; blob SHA `0f7b9e3fb63b974b0906ab92344060ec0463029b`; independently calculated UTF-8 SHA-256 `375ee8fd55eb2ce15e9d5065638e5b70f451df7a0fd7827cf9aaeaa1ee7240d2` matches live feed. Live webVersion `144`.
- APK remains `1.0.136` / versionCode `135`; no APK build/signing change. Physical phone pinch test is **pending**; do not claim device confirmation until user tests.
- Rollback: restore the exact pre-edit files from `backup/pre-pinch-zoom-fix-2026-11-13` if testing reveals regression.

---

# Web Update 145 — Two-axis image movement and Android multi-touch repair (2026-11-13)

- User reported after Update 144 that an image could move only vertically; horizontal movement and pinch zoom/zoom-out still did not work.
- Starting live state: APK 1.0.136 / versionCode 135; webVersion 144; source blob 0f7b9e3fb63b974b0906ab92344060ec0463029b. Re-read the live register, feed, source and mirror before editing.
- Scope: web-only. Changed the finger-adjust image painting/gesture functions, image background sizing in the existing field-image renderer, the existing zoom-value clamp, and the existing pamphlet-template CSS override in web-source/index.html. No other Diary feature was changed.
- Repair details: Android now uses native Touch Events for one-, two- and three-finger gestures even on browsers that also support Pointer Events; mouse/pen Pointer Events remain. Uploaded field images are sized with overflow on both axes so horizontal and vertical repositioning are possible. Background position and size are applied with CSS priority so the template rule cannot override image adjustment. Pinch zoom range now allows zoom-out to 0.8 and zoom-in up to 4×. Image dimensions are cached for adjustment rather than reloaded on every move.
- Pre-edit backup branch: backup/pre-two-axis-adjust-fix-2026-11-13. Backups created and readable:
  - backups/web-source-before-two-axis-adjust-fix-2026-11-13.html
  - backups/diary-web-before-two-axis-adjust-fix-2026-11-13.html
  - backups/latest-before-two-axis-adjust-fix-2026-11-13.json
  - backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-two-axis-adjust-fix-2026-11-13.md
- Source commit: 28cbd549a61bd92c9417b125e4a41f14691f726a. Web publisher workflow run 43379560399 (run 135) completed with success; publish job and all listed steps succeeded.
- Post-publish verification: web-source/index.html and diary-web/index.html are byte-identical; both Git blob SHA c1417ddb7b940f922b98b034dee9a226da7926ba. Live feed reports webVersion 145 and web SHA-256 bc3fb24aecf6af0abe06fa1b27ff90042fb1eac769d798e568630d71fa9fb165. The live feed was re-fetched after publishing.
- APK remains 1.0.136 / versionCode 135; APK URL, SHA-256 and package identity unchanged. No APK rebuild or signing operation.
- Physical-device testing is pending. The user must install Web Update 145 through Me → Check for Updates, then test horizontal and vertical drag, two-finger pinch-in/zoom-out and pinch-out/zoom-in on a Cover image, Details image and attached Photo. Do not claim phone-side confirmation until the user reports the results.
- Rollback: restore the exact pre-edit files from backup/pre-two-axis-adjust-fix-2026-11-13. Preserve all local notes, photos, PIN data and app data.
---

# Web Update 146 — Horizontal drag and multi-touch capture repair (2026-11-13)

- User reported the same failure after Web Update 145: image moved only vertically; horizontal drag and pinch zoom/zoom-out did not work. Do not treat the user's phone-side test as passed.
- Re-read the current live register, latest.json, source and mirror before editing. Starting live state: webVersion 145; APK 1.0.136 / versionCode 135.
- Changed only bindDiaryFingerAdjust in web-source/index.html. The new handler captures touchstart at document capture phase and registers additional fingers by checking whether their coordinates are within the active image/field bounds. This avoids relying on the second finger's event target matching the first finger's target. Pinch span is recalculated when finger count changes.
- Horizontal and vertical drag now convert pointer pixel movement into CSS background-position percentage using the actual image overflow dimensions, rather than scaling by the full field width/height. This addresses the very small horizontal shift when the image only overflows the field slightly. Attached Photo transform drag is retained.
- Pre-edit backup branch: backup/pre-horizontal-drag-pinch-repair-2026-11-13. Backups created and readable:
  - backups/web-source-before-horizontal-drag-pinch-repair-2026-11-13.html
  - backups/diary-web-before-horizontal-drag-pinch-repair-2026-11-13.html
  - backups/latest-before-horizontal-drag-pinch-repair-2026-11-13.json
  - backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-horizontal-drag-pinch-repair-2026-11-13.md
- Source commit: 08819ff9c8fd2285c7fdc0f450409a875ee13610. Publisher workflow run 43379986888 (run 136) completed with success.
- Post-publish verification: source and mirror are byte-identical; both Git blob SHA 6cc67040b3c3ecc20440b457a4eca7c9e4103d6f. Live feed reports webVersion 146 and web SHA-256 9c3aacda52194dc8d1ebe25b3cdbb1b043c7ef48fce78768ae15d5ab80d83471.
- APK unchanged at 1.0.136 / versionCode 135; no APK rebuild or signing operation.
- Physical-device testing remains pending. Ask user to install Web Update 146 through Me → Check for Updates and test left/right drag, up/down drag, two-finger pinch-in and pinch-out. Do not claim phone-side success until user confirms.
- Rollback: restore exact pre-edit files from backup/pre-horizontal-drag-pinch-repair-2026-11-13. Preserve all local notes, photos, PIN data and app data.

---

# Web Update 148 — Correct layered background image adjustment (2026-11-13)

- User reported that after Web Update 146, the image still moved only vertically; horizontal drag and two-finger zoom in/out did not work. The “Diary pehle se update hai” message was traced to the installed HTML SHA matching the live web bundle, not to the APK version.
- Re-inspected the current live Master Register, latest.json, web source and published mirror. Starting state: APK 1.0.136 / versionCode 135; webVersion 146; source/mirror blob SHA 6cc67040b3c3ecc20440b457a4eca7c9e4103d6f.
- Root cause found in the actual field-image renderer: each field photo is painted as multiple CSS background layers (optional tint, dark overlay, and the photo). The adjustment code was not explicitly separating the fixed overlay layers from the movable/zoomable photo layer. The repair now computes matching per-layer background-position, background-size, and background-repeat lists: overlays stay fitted to the field while only the actual photo layer receives its saved position and zoom. The same helper is used by initial image rendering and live finger adjustment.
- Scope: web-only; changed only web-source/index.html in two sequential commits: d6826be5e4eedd123f33938190bb93e23c3e81fe (initial layer separation) and 517faeb7a2671a8e165346944d52afd4e7e368c4 (per-layer repeat alignment). No APK rebuild, native Android change, data/storage key change, note/photo/PIN change, or unrelated UI change.
- Pre-edit backup branch: backup/pre-layered-background-adjust-repair-2026-11-13. Verified readable backups:
  - backups/web-source-before-layered-background-adjust-repair-2026-11-13.html
  - backups/diary-web-before-layered-background-adjust-repair-2026-11-13.html
  - backups/latest-before-layered-background-adjust-repair-2026-11-13.json
  - backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-layered-background-adjust-repair-2026-11-13.md
- Publisher workflows: run 43380705300 (run 137) and final run 43380881224 (run 138) both completed successfully; final run 138 publish job and all steps succeeded.
- Post-publish verification: web-source/index.html and diary-web/index.html are byte-identical; both Git blob SHA 962a0d43fc18dcbd8494cae4ec0ae603228c450d. Independently calculated UTF-8 SHA-256 0380cfa8045407eef7e58803514bfc4a1f0a5f3425286cebd0d247064e184ea0 matches live latest.json.webSha256. Live webVersion is 148.
- JavaScript parse check: both inline script blocks parsed successfully. Source/mirror/feed and backup checks passed.
- APK remains 1.0.136 / versionCode 135; APK SHA-256 remains 6fc74ca82888fed4121cc352c1846ec8c6a7063e2d2a33fbe032726f7a244348. No APK rebuild or signing operation.
- Physical-device verification is **pending**. Do not claim horizontal drag or pinch zoom works until the user tests it on the phone after receiving Web Update 148.
- Rollback: use the exact pre-edit files on backup/pre-layered-background-adjust-repair-2026-11-13. Preserve all local notes, photos, PIN data and app data.


# Web Update 149 — Smooth two-axis image adjustment for Cover, Detail and Photo (2026-11-13)

- User reported Web Update 148 still moved images only vertically, with excessively fast movement; horizontal drag and pinch zoom in/out were not working. User requested the same working adjustment across all three image areas: Cover, Detail and attached Photo.
- Re-read the live Master Register, latest.json, source and mirror before editing. Starting live state: webVersion 148; APK 1.0.136 / versionCode 135; source/mirror blob SHA 962a0d43fc18dcbd8494cae4ec0ae603228c450d.
- Root causes found in the actual adjustment math:
  - Cover/Detail drag used Math.max(1, containerSize - imageSize). Because imageSize exceeds containerSize, the negative overflow denominator was replaced with 1, making even a tiny finger movement jump rapidly and hit position limits. The new calculation uses the positive overflow magnitude with the correct sign on both axes.
  - The previous 1.25 image scale combined with the minimum saved zoom of 0.8 produced an effective scale of exactly 1.0, so one axis could have no overflow and could not be dragged. The base image scale is now 1.6, retaining overflow on both axes at the default zoom while keeping zoom-in/out range unchanged.
  - Attached Photo stored its neutral position as 50/50 but applied those values as direct CSS translate percentages, causing an offset from the centre. Translation now uses (position - 50), so 50/50 is the neutral centre.
- Changed only web-source/index.html. No APK rebuild, native Android change, storage/data key change, note/photo/PIN logic change, or unrelated UI change.
- Pre-edit backup branch: backup/pre-smooth-two-axis-photo-adjust-2026-11-13. Verified backup files:
  - backups/web-source-before-smooth-two-axis-photo-adjust-2026-11-13.html
  - backups/diary-web-before-smooth-two-axis-photo-adjust-2026-11-13.html
  - backups/latest-before-smooth-two-axis-photo-adjust-2026-11-13.json
  - backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-smooth-two-axis-photo-adjust-2026-11-13.md
- Source commit: 0c9935262b0bc7329f32cc2f3e0b926a2fbd5754. Web publisher workflow run 43382216940 (run 139) completed successfully; publish job and all listed steps succeeded.
- Post-publish verification: web-source/index.html and diary-web/index.html are byte-identical; both Git blob SHA b965dfa16278ab1b6ca8e5a80596e25367fdf9fb. Live latest.json reports webVersion 149 and web SHA-256 53f635184494a5da270f55e4e1732e833c10ad928037beb4db3e74263cd9d228. Final publisher commit on main: 0a9320e6697e6727c6671c987319d4847194e3cb.
- JavaScript parse check: both inline script blocks parsed successfully. Publisher workflow, source/mirror equality and live feed checks passed.
- APK remains 1.0.136 / versionCode 135; APK SHA-256 remains 6fc74ca82888fed4121cc352c1846ec8c6a7063e2d2a33fbe032726f7a244348. No APK rebuild or signing operation.
- Physical-device verification is **pending**. Do not claim smooth horizontal/vertical drag or pinch zoom works until the user tests all three image areas on the phone after receiving Web Update 149.
- Rollback: use the exact pre-edit files on backup/pre-smooth-two-axis-photo-adjust-2026-11-13. Preserve all local notes, photos, PIN data and app data.


# Web Update 150 — Reliable multi-pointer pinch zoom (2026-11-13)

- User confirmed Web Update 149 fixed equal left/right and up/down dragging in all three image targets (Cover, Detail, Photo), but pinch zoom-in and zoom-out still did not work.
- Re-read the live Master Register, latest.json, source and mirror. Starting state: webVersion 149; APK 1.0.136 / versionCode 135; source/mirror blob SHA b965dfa16278ab1b6ca8e5a80596e25367fdf9fb.
- Pinch zoom diagnosis: the existing gesture engine relied on document Touch Events while also installing Pointer Events but explicitly ignored touch pointers. Replaced this with Pointer Events as the primary Android/WebView gesture path: every finger is tracked by its independent pointerId; pointer capture keeps each contact associated with the selected image field; pointer move updates both points before calculating pinch distance; pointer up/cancel/lost capture rebase the remaining contact. Legacy Touch Events remain as fallback when PointerEvent is unavailable.
- The existing shared pinch ratio, zoom range 0.8–4, position state, rendering, and drag math are retained. No changes to notes, local storage/data keys, photo content, PIN, editor UI, or APK.
- Changed only web-source/index.html. Pre-edit backup branch: backup/pre-pointer-pinch-zoom-repair-2026-11-13. Verified backups:
  - backups/web-source-before-pointer-pinch-zoom-repair-2026-11-13.html
  - backups/diary-web-before-pointer-pinch-zoom-repair-2026-11-13.html
  - backups/latest-before-pointer-pinch-zoom-repair-2026-11-13.json
  - backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-pointer-pinch-zoom-repair-2026-11-13.md
- Source commit: 760c573af312bc4bbf70f2125f311609aa41836e. Web publisher workflow run 43383223582 (run 140) completed successfully; publish job and all listed steps succeeded.
- Post-publish verification: web-source/index.html and diary-web/index.html are byte-identical; both Git blob SHA fd1d38dc9d73bdabb5a074ef1449a2360712ff51. Live latest.json reports webVersion 150 and web SHA-256 ab6b55d80e6f157b77be6d8a82f8ae198b95284b66fb9a436487fd04104c176e. Both inline JavaScript blocks parse successfully.
- APK remains 1.0.136 / versionCode 135. No APK rebuild or signing operation.
- Physical-device verification is **pending**. Do not claim pinch zoom works until the user tests Cover, Detail and Photo on the phone after receiving Web Update 150. Drag was already confirmed by the user on Update 149; this change was limited to pointer gesture tracking.
- Rollback: use the exact pre-edit files on backup/pre-pointer-pinch-zoom-repair-2026-11-13. Preserve all local notes, photos, PIN data and app data.


# Web Update 151 — Detect both fingers across the selected image box (2026-11-13)

- User tested Web Update 150 and reported that pinch zoom-in and zoom-out still did not work. Existing left/right and up/down drag in Cover, Detail and Photo had been confirmed working and must be preserved.
- Re-read the live Master Register, latest.json, source and published mirror before editing. Starting state: webVersion 150; APK 1.0.136 / versionCode 135; source/mirror blob SHA fd1d38dc9d73bdabb5a074ef1449a2360712ff51.
- Diagnosis: Pointer Events registered pointerdown only on the selected image element and used pointer capture. A second finger landing on another part of the image box/frame or a child element could fail to enter the tracked pointer set. The pinch calculation itself and zoom bounds were retained.
- Changed only bindDiaryFingerAdjust(target,kind) in web-source/index.html: pointerdown is now captured at document level and each contact is registered when its coordinates fall inside the selected target's bounding rectangle. Removed explicit pointer capture and the related lost-capture handler; document-level pointermove/up/cancel continue tracking active contacts. Existing one-finger drag calculations, pinch ratio, zoom range 0.8–4, image painting, Touch Events fallback and stored state remain unchanged.
- Explicitly untouched: pamphlet chooser/designs, image selection, editor layout, note/photo data and storage keys, save format, PIN/lock/recovery, translations, native Android source, APK, package identity, signing data and unrelated Diary features.
- Pre-edit backup branch: backup/pre-document-pointerdown-pinch-repair-2026-11-13. Verified readable backups:
  - backups/web-source-before-document-pointerdown-pinch-repair-2026-11-13.html
  - backups/diary-web-before-document-pointerdown-pinch-repair-2026-11-13.html
  - backups/latest-before-document-pointerdown-pinch-repair-2026-11-13.json
  - backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-document-pointerdown-pinch-repair-2026-11-13.md
- Source commit: 28d24528fdef97ef86b385f07e30f922f0a42c0c. Publisher commit: 998923d92b31dd1155e65ad843c3ae6fa2b39acb. Live feed advanced to webVersion 151; publisher commit synchronized the published mirror and feed.
- Post-publish verification: source and mirror are byte-identical; both Git blob SHA 99785ad58c1a0a03f0b90b5dc3bd5fe3de9b6077. Independently calculated UTF-8 SHA-256 4043dc99f56adba90e65d54869f711bc7f05d3c54c3974e1f17108d7be05bfc8 matches live latest.json.webSha256. Both inline JavaScript blocks parsed successfully. Source, mirror and feed were re-fetched after publishing.
- APK remains 1.0.136 / versionCode 135; no APK rebuild or signing operation. Notes, photos, PIN data, app data, and package/signing identity were not changed.
- Physical-device verification is **pending**. User must install Web Update 151 through Me → Check for Updates and test pinch-in and pinch-out separately on Cover, Detail and Photo. Existing drag was already confirmed on Web Update 149; do not claim pinch zoom works until the user confirms it on the phone.
- Rollback: use the exact pre-edit files on backup/pre-document-pointerdown-pinch-repair-2026-11-13; preserve all local notes, photos, PIN data and app data.


# Web Update 154 — Clear change-image control after image selection (2026-11-13)

- User request: make it clear how to replace a selected image when it is not liked. A selected Cover, Detail or attached Photo now changes its picker button label to the localized **Change Image** wording. Tapping the same button opens the existing image-design chooser, where **Choose Image** opens the gallery; selecting a new image replaces only that image target.
- Changed only `web-source/index.html`, source commit `9e3a180a7b6abd70f24a586e45abe3832de83a09`. Added localized `changeImage` wording for all 10 supported languages. Cover and Detail labels follow whether their respective image data exists; Photo label follows attached-photo state. Language switching refreshes all three labels. Existing image picker, colour/pamphlet chooser, crop/drag/pinch state, text, note records, storage keys, PIN/recovery, native Android source, APK, package identity and signing data were not changed.
- Starting live state: Web Update 153; APK 1.0.136 / versionCode 135; source/mirror blob SHA `aa9a115ce37c1e3cad115046f13dcf3f7f63a75e`.
- Pre-edit backup branch: `backup/pre-image-replacement-control-2026-11-13`. Verified readable backups:
  - `backups/web-source-before-image-replacement-control-2026-11-13.html` (blob SHA `aa9a115ce37c1e3cad115046f13dcf3f7f63a75e`)
  - `backups/latest-before-image-replacement-control-2026-11-13.json` (blob SHA `e5d475d13a82f5816060a05e83f83cce549310ad`)
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-image-replacement-control-2026-11-13.md` (blob SHA `4e58ae3fb839bec284cfa74f63bc1ea65b624076`)
- Static checks: all 10 language entries and Cover/Detail/Photo label-state logic were found in the final source; language-refresh logic for all three controls was verified. The source commit changed only `web-source/index.html`. A JavaScript parser run and independent SHA-256 calculation were not available in this session; do not describe those checks as passed.
- Publisher output commit: `4b53d41fe9bd51225c46aa6286ec930bbb15b653` (“Publish My Diary web bundle update”). Live feed advanced to Web Update 154. Re-fetched source and published mirror are byte-identical; both Git blob SHA `e145f56506ea6aef721a8673fecbb3fc859c76f9`. Live `latest.json.webSha256` is `dcfcf5244c66e2b46dbf8e33189344408754af9abd5cb45a4f5621e3f582ce0b` (publisher/feed value; independent calculation not performed). Workflow run ID/conclusion was not exposed by the available status lookup; the publisher output commit, mirrored file and advanced feed were verified.
- APK unchanged: 1.0.136 / versionCode 135 / SHA-256 `6fc74ca82888fed4121cc352c1846ec8c6a7063e2d2a33fbe032726f7a244348`; no APK rebuild or signing changes.
- Physical-device verification pending. User should install Web Update 154 using **Me → Check for Updates**, then test changing Cover, Detail and Photo individually; confirm the existing text and the other images remain unchanged.
- Rollback: use the exact pre-edit files on `backup/pre-image-replacement-control-2026-11-13`; preserve local notes, photos, PIN data and app data.


# Web Update 155 — Change Image opens gallery directly (2026-11-13)

- User clarification: tapping **🔄 Image Badlein / Change Image** should open image selection directly, not open the image-design chooser first.
- Changed only `web-source/index.html`, source commit `f0f9430a9b8791a7875697ce8b8ad31cc4c12770`. In the shared Cover/Detail/Photo image chooser button handler, when that target already has an image, the button closes the chooser if needed and directly invokes its existing file input (`file.click()`). When no image is selected yet, the original chooser remains available so users can still choose an image, colour, gradient or pamphlet design. This keeps the requested direct-replace path while preserving first-time design choices.
- Pre-edit backup branch: `backup/direct-image-picker-2026-11-13`. Verified readable backups:
  - `backups/web-source-before-direct-image-picker-2026-11-13.html` (blob SHA `e145f56506ea6aef721a8673fecbb3fc859c76f9`)
  - `backups/latest-before-direct-image-picker-2026-11-13.json` (blob SHA `28c8b747f2db2372a51cb92e8ef788e4029bc174`)
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-direct-image-picker-2026-11-13.md` (blob SHA `c98cde2e17003b314ec1efa0e94f4aef9f72e964`)
- Static source review confirmed the one shared handler tests the selected-image state separately for Cover, Detail and Photo, and calls the existing file input directly for each selected image. Existing initial image chooser, pamphlet/colour options, image compression, image-position/zoom adjustment, text, notes, local storage, PIN/recovery, Android source, package identity and signing data were not changed. No JavaScript parser or independent SHA-256 calculation was run in this session.
- Publisher workflow run `43390587303` (run 145, `.github/workflows/publish-diary-web-update.yml`) completed successfully. Its `publish` job and all steps succeeded. Publisher output commit was verified by live files: source and `diary-web/index.html` are byte-identical with Git blob SHA `82dd680c76336782cfeb9d1bcc67ec2f02ade1b5`. Live feed advanced to Web Update 155; `latest.json.webSha256=81813e198d9435ef84c66b5e7964d3c1ef72e41c349d78797e7859eada9cc88e`.
- APK unchanged: 1.0.136 / versionCode 135 / SHA-256 `6fc74ca82888fed4121cc352c1846ec8c6a7063e2d2a33fbe032726f7a244348`; publisher workflow explicitly ran without rebuilding APK.
- Physical-device verification pending. User should use **Me → Check for Updates** to install Web Update 155, then tap Change Image for Cover, Detail and Photo and confirm Gallery opens directly; select a replacement and check other images/text remain unchanged.
- Rollback: use the exact pre-edit files on `backup/direct-image-picker-2026-11-13`; preserve local notes, photos, PIN data and app data.


# Web Update 156 — Restore writing by tapping an image field (2026-11-13)

- User reported that tapping the image no longer opened the writing option/keyboard. Inspection found the automatic image-adjustment Pointer/Touch handlers were calling `preventDefault()` and `stopPropagation()` on every initial press, including taps on the Cover title input and Detail text area.
- Starting live state: Web Update 155; APK 1.0.136 / versionCode 135; package `com.personal.diaryapp`; source/mirror blob SHA `82dd680c76336782cfeb9d1bcc67ec2f02ade1b5`; feed SHA-256 `81813e198d9435ef84c66b5e7964d3c1ef72e41c349d78797e7859eada9cc88e`.
- Changed only `web-source/index.html`, source commit `c30e4a2aa010383ca5fa8149d7e7174dc5c83793`. Single taps now pass through to the input/textarea so the keyboard can open. Drag/pinch adjustment takes over only after movement reaches 6 pixels; the Touch Events fallback follows the same threshold. Existing zoom range, per-image positions, saved image/text data, and Web Update 155 direct Gallery replacement behavior remain unchanged.
- Pre-edit backup branch: `backup/pre-image-tap-writing-fix-2026-11-13`; exact readable backups verified:
  - `backups/web-source-before-image-tap-writing-fix-2026-11-13.html` (blob SHA `82dd680c76336782cfeb9d1bcc67ec2f02ade1b5`)
  - `backups/latest-before-image-tap-writing-fix-2026-11-13.json` (blob SHA `0705bc5580afd5b96f16bd7dc4866c705dbe7aa4`)
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-image-tap-writing-fix-2026-11-13.md` (blob SHA `c80f161897a4928b0ffae5faf1e114ed511de5d9`)
- Source diff reviewed: only the shared image gesture handler changed. Both inline JavaScript blocks parsed successfully. Static checks confirm tap events are no longer cancelled at pointer/touch start and both drag handlers use the 6-pixel movement threshold.
- Web-only workflow run `43395054248` (run 146) completed with conclusion `success`; publish job `131783845220` succeeded. Publisher output advanced the live feed to Web Update 156.
- Post-publish: source and `diary-web/index.html` are byte-identical; both Git blob SHA `3a9439731ca5965b381b938b86c5189b657c4999`. Independently computed UTF-8 SHA-256 `7404440c4db966789b67529d0f156191a715769b3d2513a9da13be8c4de92aef` matches live `latest.json.webSha256`; webVersion is 156.
- APK unchanged: 1.0.136 / versionCode 135 / SHA-256 `6fc74ca82888fed4121cc352c1846ec8c6a7063e2d2a33fbe032726f7a244348`; no APK rebuild or signing changes.
- Physical-device verification **pending**. User should use **Me → Check for Updates**, then tap the Cover image field and Detail image field to confirm the writing keyboard opens; also verify one-finger drag and two-finger zoom still work. Tap **Image Badlein** on an existing image to confirm it still opens Gallery directly.
- Rollback: verified pre-edit files on `backup/pre-image-tap-writing-fix-2026-11-13`; preserve all diary notes, photos, PIN data and app identity.


# Web Update 158 — Fix Note Share on mobile (2026-11-13)

- User reported that 📤 Note Share Karein did not work. Root cause: the composed PNG was created asynchronously (Image loading and canvas.toBlob) and only then passed to navigator.share(). On mobile browsers the transient user activation from the tap can expire before this asynchronous work completes, so the native share sheet is blocked.
- Starting live state: Web Update 156; APK 1.0.136 / versionCode 135; package com.personal.diaryapp; source/mirror blob SHA 3a9439731ca5965b381b938b86c5189b657c4999; feed SHA-256 7404440c4db966789b67529d0f156191a715769b3d2513a9da13be8c4de92aef.
- Changed only web-source/index.html. When a note is expanded and unlocked, the app now prepares the same combined Diary PNG (cover image + title text + detail image + note text + attached photo) in advance. The Share button remains disabled until that PNG is ready, then its click calls navigator.share({files:[file]}) immediately within the user's tap. If file sharing is unsupported, the existing composed-image download fallback remains. Preparation is cached per note ID, update timestamp and selected language. Note content, image layout, formatting, notes storage, photos, PIN/recovery, app identity and Android source were not changed.
- Pre-edit backup branch: backup/pre-note-share-fix-2026-11-13; verified exact backups:
  - backups/web-source-before-note-share-fix-2026-11-13.html (blob SHA 3a9439731ca5965b381b938b86c5189b657c4999)
  - backups/latest-before-note-share-fix-2026-11-13.json (blob SHA 3b8f1fd35cf7921e83932274897f8a017b778414)
  - backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-note-share-fix-2026-11-13.md (blob SHA 75db3e09d122642bc6a6cc5fbf20ddf2dad99be1)
- Source commits: initial implementation b401fed740e8397dd578f5ccf5520502fed687c8; final refinement 7d367e562ed1d682c769980d89919fb4f1083abb. Final diff reviewed and both inline JavaScript blocks parsed successfully. Static checks verified pre-generation on expanded notes, disabled-until-ready behavior, cached PNG, and synchronous share invocation on tap.
- Publisher workflow runs 147 (43396317069) and 148 (43396414393) both completed successfully; each publish job succeeded. The final publisher output is Web Update 158 (run 148). Live feed confirms webVersion=158 and webSha256=bcb655b79f33742f44e6de283bd2af5286acb7d8f5bf70cd90f55d521e866f16.
- Post-publish: source and diary-web/index.html are byte-identical; both Git blob SHA 131469afbb2aa47b0132c07f7210b45e0eba0b6a.
- APK unchanged: 1.0.136 / versionCode 135 / SHA-256 6fc74ca82888fed4121cc352c1846ec8c6a7063e2d2a33fbe032726f7a244348; web-only workflow did not rebuild APK.
- Physical-device verification pending. User should install via Me → Check for Updates, open/unlock a note, wait until 📤 Note Share Karein becomes enabled, then tap it and confirm Android's share sheet appears with the combined Diary PNG. If no compatible share target exists, the existing image-download fallback should run.
- Rollback: exact pre-edit files are preserved on backup/pre-note-share-fix-2026-11-13; preserve all local notes, photos, PIN data and app identity.


# Web Update 159 — Prevent Note Share tap from collapsing the note (2026-11-13)

- User tested Web Update 158 and reported that tapping 📤 Note Share Karein only shifted/collapsed the page.
- Inspection found the share button was deliberately disabled until the asynchronous PNG preparation completed. Because a disabled button does not dispatch its click event, the event could bubble to the parent note card, whose click handler collapses the expanded note. This explains the reported page movement.
- Starting live state: Web Update 158; APK 1.0.136 / versionCode 135; source/mirror blob SHA 131469afbb2aa47b0132c07f7210b45e0eba0b6a.
- Changed only web-source/index.html, source commit a67edf176d17d185fe4b56936152d563b85d2a08. The Share button is no longer disabled while the combined PNG is being prepared. Its click handler now always prevents default and stops propagation first, so tapping cannot trigger the parent note-card collapse. If the PNG is not ready yet, it displays a short “still preparing, tap again” message and ensures preparation is running. Once cached, the same button opens the native share sheet directly from the tap. Existing combined-image layout and download fallback remain. No note records, local photos, PIN/recovery, Android source, app identity or APK were changed.
- Pre-edit backup branch backup/pre-note-share-button-tap-fix-2026-11-13; exact backups verified:
  - backups/web-source-before-note-share-button-tap-fix-2026-11-13.html (blob SHA 131469afbb2aa47b0132c07f7210b45e0eba0b6)
  - backups/latest-before-note-share-button-tap-fix-2026-11-13.json (blob SHA 4fd67f1313bc3586352f2768497b7c619aba7054)
  - backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-note-share-button-tap-fix-2026-11-13.md (blob SHA 0abe02d7ca27b6c83564b781d147a16f20789d0b)
- Both inline JavaScript blocks parsed successfully. Static checks confirm the button is never disabled, stops event propagation on every tap, retries image preparation when necessary, and calls share only after a composed PNG is cached.
- Publisher workflow run 43397309941 (run 149) completed successfully. Publisher job succeeded. Live feed advanced to Web Update 159 with webSha256 bcb655b79f33742f44e6de283bd2af5286acb7d8f5bf70cd90f55d521e866f16.
- Post-publish: web-source/index.html and diary-web/index.html are byte-identical; both blob SHA 9b5372c80a3f63c8e8f69fc8fa31324b2e4e1a81.
- APK unchanged: 1.0.136 / versionCode 135 / SHA-256 6fc74ca82888fed4121cc352c1846ec8c6a7063e2d2a33fbe032726f7a244348.
- Physical-device verification pending. User should install Web Update 159 using Me → Check for Updates, open/unlock a note, tap Share once (if still preparing, wait briefly and tap again), and confirm the note stays expanded and Android's share sheet opens.
- Rollback: exact pre-edit files are preserved on backup/pre-note-share-button-tap-fix-2026-11-13; preserve local notes, photos, PIN data and app identity.


# Web Update 160 — Restore the known-good one-tap Note Share handler (2026-11-13)

- User reported Note Share remained nonfunctional after Web Update 159 and explicitly required evidence-based checking, not guesswork.
- Starting live state: Web Update 159; APK 1.0.136 / versionCode 135; package `com.personal.diaryapp`; source/mirror blob SHA `9b5372c80a3f63c8e8f69fc8fa31324b2e4e1a81`; feed SHA-256 `bcb655b79f33742f44e6de283bd2af5286acb7d8f5bf70cd90f55d521e866f16`.
- Historical comparison: fetched the actual Web Update 157 source at publisher commit `4705d62cb2222a677c2a438717116a48c0306cda`, then compared the Note Share function and button handler against Web Updates 158 and 159. Web 157's button handler calls `shareNote(n)` immediately from the tap. Web 158 introduced a disabled-until-ready state; Web 159 removed disabled state but added a cache-miss early return, so a tap while image preparation was pending did not invoke the known-good Share flow. This was the exact behavioral regression.
- Scope: changed only the Note Share button's click handler in `web-source/index.html`. Restored the exact Web 157 handler behavior: prevent default, stop propagation, then call `shareNote(n)` immediately. Existing asynchronous pre-generation, cache, combined PNG composition, text/image placement, native share call, and download fallback remain. No other functions, UI, notes, photos, storage, PIN/recovery, Android source, package identity, APK or signing data changed.
- Pre-edit backup branch: `backup/pre-share-single-tap-restore-2026-11-13`; verified readable exact backups:
  - `backups/web-source-before-share-single-tap-restore-2026-11-13.html` (blob SHA `9b5372c80a3f63c8e8f69fc8fa31324b2e4e1a81`)
  - `backups/diary-web-before-share-single-tap-restore-2026-11-13.html` (blob SHA `9b5372c80a3f63c8e8f69fc8fa31324b2e4e1a81`)
  - `backups/latest-before-share-single-tap-restore-2026-11-13.json` (blob SHA `90ffff65ff474fe5b964de4244a13e520dc8e975`)
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-share-single-tap-restore-2026-11-13.md` (blob SHA `b290aecd5a204392285ad1b52bb50da5b81b33f6`)
- Source change commit: `e648772ad8924e7fade1f58ef0b57b26ea158a34`; publisher output commit: `6e21edb1f4a89dd55601db21cd9b2596b268019b`. The exact branch diff was verified to equal one replacement of the Share click handler only.
- Verification: both inline JavaScript blocks parsed successfully. Static checks confirmed the restored handler exists once, stops parent-card propagation, leaves pre-generation enabled, and preserves the composed PNG/native-share code. Re-fetched source and mirror are byte-identical; both Git blob SHA `8cd55c74c81a77232b53d22ff3da27d564617d37`. Independently calculated UTF-8 SHA-256 `9e62a60bfad90c5374d02ebad6e39d6138c5c217bffcb22c03ab3c8a1a31be1f` matches live feed `latest.json.webSha256`; live webVersion is 160. Publisher output commit and live mirror/feed update are verified; direct workflow run ID/conclusion was not available through the current read endpoint and is recorded as not independently retrieved.
- APK unchanged: 1.0.136 / versionCode 135 / SHA-256 `6fc74ca82888fed4121cc352c1846ec8c6a7063e2d2a33fbe032726f7a244348`; no APK rebuild or signing changes.
- Physical-device verification **pending**. User should use **Me → Check for Updates**, open/unlock a note, and tap **Share** once. Confirm the note stays expanded and the Android share sheet opens. Do not claim phone-side success until the user confirms.
- Rollback: exact pre-edit files on `backup/pre-share-single-tap-restore-2026-11-13`; preserve all local notes, photos, PIN data and app identity.


# Web Update 161 — Keep Note Share unavailable until the composed image is ready (2026-11-13)

- User reported that `📤 Note Share Karein` still did not open Share and asked for the fix to work in both the Android APK and Chrome.
- Starting live state: Web Update 160; APK 1.0.136 / versionCode 135; package `com.personal.diaryapp`; source/mirror blob SHA `8cd55c74c81a77232b53d22ff3da27d564617d37`; feed SHA-256 `9e62a60bfad90c5374d02ebad6e39d6138c5c217bffcb22c03ab3c8a1a31be1f`.
- Audited the complete live `shareNote` function and the expanded-note rendering/click handlers. Confirmed that a cache-miss Share tap fell through to asynchronous image loading, canvas rendering and `toBlob`, then called `navigator.share` only after those asynchronous steps. That loses the transient browser user activation in Chrome. Also confirmed the Android project has a native `DiaryNativeShare` WebMessageListener and a `navigator.share` shim; it converts selected files to Base64 and invokes Android's FileProvider share intent.
- Changed only `web-source/index.html`: the Share button now stays disabled until the composed PNG cache is ready, and its preparation callback enables the button only after the cached image exists. The parent note-card click handler now ignores taps originating from buttons/inputs/selects, preventing a not-yet-ready Share button tap from collapsing the expanded note. Once enabled, the button calls the existing `shareNote(n)` synchronously from the tap. Combined PNG artwork, image/text positioning, native Android share bridge, browser Web Share API, download fallback, notes, photos, storage, PIN/recovery and APK were not changed.
- Pre-edit backup branch: `backup/pre-note-share-ready-gate-2026-11-13`; verified backup files:
  - `backups/web-source-before-note-share-ready-gate-2026-11-13.html`
  - `backups/latest-before-note-share-ready-gate-2026-11-13.json`
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-note-share-ready-gate-2026-11-13.md`
- Source change commit: `a5647aa33116ed4e30914911ba64da16e66cc474`; source blob SHA `893bb0524cbf409289784ff616fff453b2efd262`.
- Web-only publisher workflow run `43406545302` (run 151) completed with conclusion `success`; publish job `131822149788` succeeded. Live source and `diary-web/index.html` are byte-identical; both blob SHA `893bb0524cbf409289784ff616fff453b2efd262`. Live feed advanced to Web Update 161 and reports `webSha256=72d57d63844f68f125c49f7bfb90fd62c38a060bd8804fd9dc129eb7561e3ccb`. The publisher workflow computed this SHA and wrote it to the feed; an independent local recomputation is still pending.
- Static verification after publication confirmed the readiness gate, preparation callback, synchronous Share call after readiness, and parent-card control-target guard are all present in the published source. JavaScript parse/build validation for this exact web bundle is pending; no claim of complete automated syntax validation is made.
- APK unchanged: 1.0.136 / versionCode 135 / SHA-256 `6fc74ca82888fed4121cc352c1846ec8c6a7063e2d2a33fbe032726f7a244348`; no APK rebuild or signing change.
- Physical-device/browser verification pending. User should use **Me → Check for Updates**, open and unlock a note, wait for the Share button to become enabled, then tap it once. Confirm the note stays expanded and the Android/Chrome share sheet opens with the single composed Diary image. Do not claim phone-side success until confirmed.
- Rollback: exact pre-edit files are preserved on `backup/pre-note-share-ready-gate-2026-11-13`; preserve local notes, photos, PIN data and app identity.


# Web Update 162 — Note Share canvas fallback and failure-safe readiness (2026-11-13)

- User reported that Web Update 161 still did not make Note Share work. Re-audited the full share function and found a definite failure-path defect: when `canvas.toBlob` returned null or image preparation rejected, the code still called the readiness callback with no success value. The Share button then became enabled despite no cached image; the next tap rebuilt the image asynchronously and could lose the user activation again.
- Created pre-edit backup branch `backup/pre-note-share-canvas-fallback-2026-11-13` with:
  - `backups/web-source-before-note-share-canvas-fallback-2026-11-13.html`
  - `backups/latest-before-note-share-canvas-fallback-2026-11-13.json`
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-note-share-canvas-fallback-2026-11-13.md`
- Changed only `web-source/index.html`: canvas PNG creation now uses `canvas.toBlob` when available and falls back to `canvas.toDataURL` -> Blob if `toBlob` is unavailable or returns null. Preparation callbacks now receive explicit success/failure; Share is enabled only after a successful cached PNG, and remains disabled on failure with an accessible error title/status. Existing composed layout, native Android bridge, browser share, download fallback, notes/photos/storage/PIN and app identity are unchanged.
- Source commit `9949f2de30084cbfa64d5465aa959f8aad6b7054`; source blob `50420b05d0bd25d893b44d5e1c94c53f8c4b9975`.
- Web-only publisher run `43407161971` (run 152) completed `success`; publish job `131824200908` completed `success`. Workflow's verification/publish step succeeded, including its bundle validation.
- Post-publish source and `diary-web/index.html` are byte-identical; both blob SHA `50420b05d0bd25d893b44d5e1c94c53f8c4b9975`. Feed reports Web Update `162`, SHA-256 `39d789052f285fb29abc4292f6e4e802382adc03ca3d876de3907c474cba7dcf`. Static post-publish checks confirmed fallback function, explicit true/false callback paths, and success-only enable logic.
- APK unchanged at 1.0.136 / versionCode 135; no APK rebuild or signing change. Physical device/browser share-sheet test remains pending. Do not claim complete success until user confirms the actual share sheet opens and the composed image is attached.
- User test path: Me → Check for Updates; open/unlock note; wait until Share button becomes enabled; tap once. If it stays disabled, report the visible status rather than tapping repeatedly.


# Web Update 163 — Keep Note Share tappable and isolate touch events (2026-11-13)

- User reported that tapping **📤 Note Share Karein** only moved the note page. Inspection of the live Web Update 162 source identified the exact cause: the Share button was set to `disabled` until its composed PNG cache was ready. A disabled HTML button does not dispatch the normal click event; on touch, the tap can be retargeted to the parent note card. The note card's pointer/scroll handling then receives the gesture instead of Share. This was not a new Android bridge failure.
- Starting state: Web Update 162; APK 1.0.136 / versionCode 135; source and mirror blob SHA `50420b05d0bd25d893b44d5e1c94c53f8c4b9975`; feed SHA-256 `39d789052f285fb29abc4292f6e4e802382adc03ca3d876de3907c474cba7dcf`.
- Pre-edit backups were created and re-fetched successfully on branch `backup/note-share-disabled-tap-event-2026-11-13`:
  - `backups/web-source-before-note-share-disabled-tap-event-2026-11-13.html` (blob SHA `50420b05d0bd25d893b44d5e1c94c53f8c4b9975`)
  - `backups/diary-web-before-note-share-disabled-tap-event-2026-11-13.html` (blob SHA `50420b05d0bd25d893b44d5e1c94c53f8c4b9975`)
  - `backups/latest-before-note-share-disabled-tap-event-2026-11-13.json` (blob SHA `18df90e0cfb8819b9fc57ac0357c4624f0c85022`)
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-note-share-disabled-tap-event-2026-11-13.md` (blob SHA `a26cc24aa128fe63291c2806c65564147e7487c4`)
- Changed only the Share-button creation/handler line in `web-source/index.html` (source commit `ebec0098ec2e7ef89a7e24d9bb87eff6b6ac3acd`). Share remains enabled while the PNG is preparing; pointerdown and touchstart stop propagation; click prevents default and stops propagation. If the image is not ready, the user sees a preparing message and preparation can be retried; when cached, the existing `shareNote(n)` is called synchronously from the tap. Existing composed-image artwork, layout, image/text placement, native Android bridge, browser share, download fallback, notes/photos/storage/PIN/recovery and APK were not changed.
- Both inline JavaScript blocks in the updated source parsed successfully. The source/mirror publisher output commit is `6101336f899cf133706cc52ead800200af53efd5` (“Publish My Diary web bundle update”), which updated only `diary-web/index.html` and `latest.json`. The publisher workflow run ID was not independently exposed by the available read endpoint; the publisher bot output commit and live feed were verified.
- Post-publish source and mirror are byte-identical; both blob SHA `5a75e86dce0a444af482ba20325963570d94f301`. Live feed reports webVersion `163` and `webSha256=5170a6cba592960dbb2ff7b0b3773c6b38da1d6b16c99999029228ccfcdfdc37`. Independently calculated SHA-256 from the exact UTF-8 source bytes matches the feed.
- APK unchanged: 1.0.136 / versionCode 135 / SHA-256 `6fc74ca82888fed4121cc352c1846ec8c6a7063e2d2a33fbe032726f7a244348`; no APK rebuild or signing changes.
- Physical-device verification pending. User should use **Me → Check for Updates**, open/unlock a note, and tap **📤 Note Share Karein**. First confirm the note page no longer moves; then wait for the image-ready state and tap Share again if the preparation message appears. Confirm the actual Android/Chrome share sheet opens and contains the combined note image before claiming the feature fully works.
- Rollback: exact pre-edit files are preserved on `backup/note-share-disabled-tap-event-2026-11-13`; preserve local notes, photos, PIN data and app identity.


# Pending source patch — stop note-card press animation on Share (2026-11-13)

- User reports Share tap still only moves the whole note card. Inspection found the explicit parent-card press animation: `.diary-my-note:active{transform:scale(.99)}`. The Share button is inside this article card, so the card itself visibly shifts during a Share press.
- A minimal source-only patch was committed as `ba5d085f1846856f8b05f82fc755530556efd802`: the Share button now has the additional class `diary-note-share`, and `.diary-my-note:has(.diary-note-share:active){transform:none!important;}` suppresses only the parent card's active movement while Share is pressed. Existing Share handler and other note actions remain unchanged.
- Pre-edit backups were created and verified on `backup/note-card-share-motion-fix-2026-11-13`: source and mirror blob SHA `5a75e86dce0a444af482ba20325963570d94f301`, feed blob SHA `0d262443629d9216d3bbbe1ce78c9a5f798dfe28`, register blob SHA `85020077f83f7e451e55415567d34cab8a5e872f`.
- **Not published.** After the source commit, the mirror remains at `5a75e86dce0a444af482ba20325963570d94f301`, while source is `fc2beb9cd8b4fecd2372273b635cecdf77a5705b`; feed remains webVersion `163` with SHA-256 `5170a6cba592960dbb2ff7b0b3773c6b38da1d6b16c99999029228ccfcdfdc37`. No publisher workflow run was returned for the source commit. Therefore do not tell the user to check for updates or claim the fix is live. Resume only after the established publisher workflow can be run and verified, then mirror, feed hash, and register must all be verified.


# Completed publication — Note Share card motion fix (Web Update 164, 2026-11-13)

- The source patch from commit `ba5d085f1846856f8b05f82fc755530556efd802` was published by the verified GitHub Actions workflow run **43408313086**, workflow **Publish My Diary web-only update**, run 154; status `completed`, conclusion `success`, head SHA matches the source patch.
- Publisher output commit: `2b77b47b379e61d8d6e929fe2272e013f0c705db`. It changed only `diary-web/index.html` and `latest.json`.
- Live `latest.json` reports webVersion `164`, webSha256 `0645f735400d037eac30dcca5c043317bd67f2c0f5982eefdef6269fa60522ae`; APK remains `1.0.136`, versionCode `135`, APK SHA-256 unchanged at `6fc74ca82888fed4121cc352c1846ec8c6a7063e2d2a33fbe032726f7a244348`.
- Live source and published mirror were fetched independently; both are byte-identical and share blob SHA `fc2beb9cd8b4fecd2372273b635cecdf77a5705b`. This verifies mirror equality. The feed's published SHA-256 is recorded above; this runtime did not independently recompute the SHA-256 digest.
- Minimal change: add class `diary-note-share` to the Share button and CSS `.diary-my-note:has(.diary-note-share:active){transform:none!important;}` to prevent the enclosing note card's active scale animation only while Share is pressed. Existing Share logic and other controls are unchanged.
- Earlier section “Pending source patch — stop note-card press animation on Share” is superseded by this completed publication record. Physical-device confirmation is still pending: user must verify that the share sheet opens and contains the composed note image. Do not claim the actual Share operation is confirmed until the user tests it.
- Register pre-edit backup was saved and verified on branch `backup/note-share-motion-published-2026-11-13` at `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-note-share-motion-published-2026-11-13.md`.


# Note Share readiness fix — Web Update 165 (2026-11-13)

- User's repeated report: tapping **📤 Note Share Karein** only moved the note card and did not open Share. Inspection of the live Web Update 164 source found that the Share button was appended immediately while its composed PNG was still being generated. The click handler explicitly returned early while the cache was empty, so that tap never called `navigator.share`; it only displayed a preparation message. The enclosing note card also had active transform rules, which visually moved the card during the press.
- Pre-edit backups were created and re-fetched successfully on branch `backup/share-ready-gate-2026-11-13`:
  - `backups/web-source-before-share-ready-gate-2026-11-13.html` (blob SHA `fc2beb9cd8b4fecd2372273b635cecdf77a5705b`)
  - `backups/diary-web-before-share-ready-gate-2026-11-13.html` (same blob SHA)
  - `backups/latest-before-share-ready-gate-2026-11-13.json` (blob SHA `e6b4d223e9f3f44b2cf7523f5faca6344d1378b7`)
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-share-ready-gate-2026-11-13.md` (blob SHA `fc982c76464abd1a9261a22eecf5050cdd9c5f9a`)
- Source-only patch commit: `2fba229b2959117bbfc999d1c7bfbbccbe3c43bf`; source blob SHA `3e585702b5560f9a7785c54895ad4e3769380bd4`. The Share button is now created only after the composed PNG cache is ready. While preparing, a visible status replaces the premature Share button; if image preparation fails, that status can be tapped to retry. Once ready, a single Share-button tap calls the existing `shareNote(n)` path directly. Both active note-card transform rules were neutralized to prevent the card from shifting on press. No image composition, notes, photos, storage, PIN, or native bridge code was changed.
- Both inline JavaScript blocks passed syntax parsing after the patch. Targeted source checks confirmed the premature button/click path was removed, the ready-gated button is present, and the card active transforms are neutralized.
- Publisher workflow run **43409526224**, run 155, head SHA `2fba229b2959117bbfc999d1c7bfbbccbe3c43bf`, completed successfully. Publisher output commit `f7b4c82ec2dbdd61d98101f27d9728db4bda4eff` changed only `diary-web/index.html` and `latest.json`.
- Live feed reports webVersion `165` and SHA-256 `ba25e5c8d46931e8e50848a2cd118b0051c4d370a61e1fff1135c75f7f017e64`; this exact digest was printed by the successful publisher workflow. Independently fetched source and mirror are byte-identical, both blob SHA `3e585702b5560f9a7785c54895ad4e3769380bd4`.
- APK remains unchanged: `1.0.136`, versionCode `135`, SHA-256 `6fc74ca82888fed4121cc352c1846ec8c6a7063e2d2a33fbe032726f7a244348`.
- Physical-device verification is still pending. Do not claim Share sheet operation is confirmed until user tests that the Share button appears after preparation and opens the share sheet with the composed note image. If the button does not appear, report that as a distinct image-preparation failure rather than asking the user to keep tapping.
- This section supersedes the earlier pending/partial Share notes and the Web Update 164 card-motion-only fix for current live status.


# Note Share native bridge routing — Web Update 166 (2026-11-13)

- User reported that Check for Updates showed “Diary Pehle Se Update Hai” and Note Share still needed repair. Re-inspection found a concrete integration issue: the updater reloads the verified HTML with a cache-busting query parameter (?diaryRefresh=...), while the Android onPageFinished hook in the inspected Android source archive injects the navigator.share shim only when the URL exactly equals the bare /assets/index.html URL. On the query-string refresh URL, that shim is skipped even though the DiaryNativeShare WebMessageListener is available. This explains why the updated HTML can display Share but the WebView navigator.share path may be absent.
- Pre-edit backup branch: backup/native-share-bridge-query-fix-2026-11-13. Exact files were created, re-fetched, and verified byte-identical:
  - backups/web-source-before-native-share-bridge-query-fix-2026-11-13.html — blob SHA 3e585702b5560f9a7785c54895ad4e3769380bd4
  - backups/diary-web-before-native-share-bridge-query-fix-2026-11-13.html — same blob SHA
  - backups/latest-before-native-share-bridge-query-fix-2026-11-13.json — blob SHA 49cc95f5dc16c4061c8cea988867f638fe26b8a1
  - backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-native-share-bridge-query-fix-2026-11-13.md — blob SHA 6f6d335fdd616c59ac89155324f3bd78e225f4c8
- Changed only web-source/index.html in source commit 73eb6df12d880121cc54b3c0d2664577ca990065, blob SHA ab23175252a017f0d19f5064969685a02d5044a9. Added a direct DiaryNativeShare bridge path for the already-composed PNG, before the Web Share API fallback. It reads the PNG as a data URL, sends the base64 image through the existing native bridge, and displays the native bridge success/error response. The same helper also covers the existing direct canvas-share fallback path. Browser Chrome continues to use the existing navigator.share path when the Android bridge is absent. No note composition, images, storage, PIN, native source, APK, or app identity was changed.
- Both inline JavaScript blocks in the patched source passed new Function syntax parsing. Targeted checks confirmed the native bridge helper and both call sites exist.
- Publisher workflow Publish My Diary web-only update, run 43410604332, run 156, head SHA 73eb6df12d880121cc54b3c0d2664577ca990065, completed with conclusion success; publish job 131835762093 succeeded. Publisher output commit 134cd248d3995b1a2926e7e084fe5498addf721b changed only diary-web/index.html and latest.json.
- Live feed reports webVersion 166, web SHA-256 1f9f4bb9707eb562f696f752d11868724a277a5c122edcff9531d5f32d6c89b9; the exact digest was emitted by the successful publisher workflow. Re-fetched source and mirror are byte-identical; both blob SHA ab23175252a017f0d19f5064969685a02d5044a9, both 289,637 characters.
- APK remains unchanged at 1.0.136, versionCode 135, SHA-256 6fc74ca82888fed4121cc352c1846ec8c6a7063e2d2a33fbe032726f7a244348. This is a web-only patch; no APK rebuild or signing change.
- Physical phone verification remains pending. User should run Me → Check for Updates, open an unlocked note, wait for the Share button to appear, and tap it once. Do not claim success until the Android share sheet actually opens with the composed Diary PNG attached. If it fails, capture the visible status/error; do not repeatedly tap or assume a device-side success.
- Rollback: exact pre-edit files are preserved on backup/native-share-bridge-query-fix-2026-11-13. Preserve local notes, photos, PIN data, and app identity.


---

# Web Update 167 — Mobile Diary left/right border fit (2026-11-13)

- User reported that the left and right border lines of the opened Diary panel are slightly clipped on mobile. The CSS sizing was the cause: the panel had `width:min(760px,100%)` with a 2px border but no mobile `border-box`, allowing the border to extend beyond the overlay's available width.
- Changed only `web-source/index.html`: added the isolated `diary-mobile-border-fit` CSS rule for screens up to 420px, setting `#diaryMyNotesPanel` to `box-sizing:border-box`, `width:100%`, and `max-width:100%`. This keeps the existing left/right border lines inside the mobile panel width. No vertical positioning, border style/colour, panel content, gesture behaviour, note/share code, translations, data/storage, PIN/recovery, native Android source, APK, package identity, or signing data changed.
- Starting live state: feed Web Update 166; APK 1.0.136 / versionCode 135; package `com.personal.diaryapp`. Source/mirror prior blob SHA `ab23175252a017f0d19f5064969685a02d5044a9`; prior feed SHA-256 `1f9f4bb9707eb562f696f752d11868724a277a5c122edcff9531d5f32d6c89b9`.
- Reconciled the stale status line at the top of this register: it incorrectly said Web Update 163 while the live feed was 166. The live feed was treated as authoritative. Current header now reflects Web Update 167 and its exact feed SHA-256.
- Pre-edit backup branch: `backup/pre-mobile-diary-border-fit-2026-11-13`. Exact backups created and re-fetched byte-identically:
  - `backups/web-source-before-mobile-diary-border-fit-2026-11-13.html` — blob `ab23175252a017f0d19f5064969685a02d5044a9`
  - `backups/diary-web-before-mobile-diary-border-fit-2026-11-13.html` — blob `ab23175252a017f0d19f5064969685a02d5044a9`
  - `backups/latest-before-mobile-diary-border-fit-2026-11-13.json` — blob `bc7fdc05e1e83f548b1e7b1d67a26a9e2bee502c`
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-mobile-diary-border-fit-2026-11-13.md` — blob `643101011d6490c9ac60c2ab851f3655735f9d6f`
- Source patch commit: `c1f1723c44c2f7e86710561903ee32459abfa4a2`; source blob `00737e4bfe34a875dd1099555d9d6ff67381b472`. Both inline JavaScript blocks parsed successfully; the added CSS braces are balanced and the mobile-only selector was confirmed in the final source.
- Publisher output commit: `dede972e9c906579a59dd12fd4fa57eb852fd6b2` (“Publish My Diary web bundle update”), changing only `diary-web/index.html` and `latest.json`. Live source and mirror were re-fetched and are byte-identical, both blob SHA `00737e4bfe34a875dd1099555d9d6ff67381b472`. Independently computed UTF-8 SHA-256 `87a7d661f06322370dfe5ac87a7aef555eeaeb6844c82ffe302465c9f3b53751` matches `latest.json.webSha256`; live feed is Web Update 167.
- APK unchanged: 1.0.136 / versionCode 135; APK SHA-256 `6fc74ca82888fed4121cc352c1846ec8c6a7063e2d2a33fbe032726f7a244348`. No APK rebuild or signing changes.
- Physical-device verification pending. User should use the existing **Me → Check for Updates** path and confirm that both vertical border lines are now fully visible on the mobile screen. Do not claim phone-side success until the user confirms.
- Rollback: restore the exact pre-edit HTML files from `backup/pre-mobile-diary-border-fit-2026-11-13`; preserve all notes, photos, settings, and PIN data.


---

# Web Update 168 — Reduce mobile Diary panel width by 10px total (2026-11-13)

- User confirmed the previous border fit was still clipped and specified: reduce the total panel width by 10px. Applied exactly 10 CSS pixels total, equivalent to 5px on each side, on screens up to 420px.
- Starting live state: Web Update 167; APK 1.0.136 / versionCode 135; package `com.personal.diaryapp`. Source/mirror prior blob SHA `00737e4bfe34a875dd1099555d9d6ff67381b472`; prior feed SHA-256 `87a7d661f06322370dfe5ac87a7aef555eeaeb6844c82ffe302465c9f3b53751`.
- Changed only `web-source/index.html`, in the existing `diary-mobile-border-fit` CSS block: `width:calc(100% - 10px)`, matching `max-width`, and auto left/right margins. The existing `box-sizing:border-box` and 420px mobile breakpoint remain. No height, vertical position, border thickness/colour/style, panel content, feature logic, gestures, Share, translations, notes/photos, storage, PIN/recovery, native Android source, APK, package identity or signing data changed.
- Pre-edit backup branch: `backup/pre-mobile-diary-border-10px-2026-11-13`. Exact backups created, re-fetched and verified byte-identical:
  - `backups/web-source-before-mobile-diary-border-10px-2026-11-13.html` — blob `00737e4bfe34a875dd1099555d9d6ff67381b472`
  - `backups/diary-web-before-mobile-diary-border-10px-2026-11-13.html` — same blob
  - `backups/latest-before-mobile-diary-border-10px-2026-11-13.json` — blob `77fa17c622e285ad4073dd4f9fe84d838a42b34f`
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-mobile-diary-border-10px-2026-11-13.md` — blob `461ee2c49201bee05fbaf0588e3cd9dab19b10bd`
- Source patch commit `c2c795b47b55a17ce9c0fbb521d57b4305c6b650`; final source blob `d1b173fa83ee5cb85ffdc780d14205a0ee1a0402`. Both inline JavaScript blocks parsed successfully; mobile CSS braces balanced; targeted checks confirmed 10px total width reduction, horizontal centering, and no height/top/bottom changes.
- Publisher workflow run `43413910094`, run 158, completed successfully; publish job `131846909543` succeeded. Publisher output commit `0071dba5a93091b6cea858a33b112a53f93c9a40` updated the published mirror and feed. Re-fetched source and mirror are byte-identical, both blob SHA `d1b173fa83ee5cb85ffdc780d14205a0ee1a0402`.
- Live feed advanced to Web Update 168. Independently calculated UTF-8 SHA-256 `e6d08089a138d3fc2026eceff7db1fcd5f247eda92ed4f616ca54b60e70d8b09`, matching `latest.json.webSha256`.
- APK unchanged: 1.0.136 / versionCode 135; SHA-256 `6fc74ca82888fed4121cc352c1846ec8c6a7063e2d2a33fbe032726f7a244348`. Web-only update; no APK rebuild or signing changes.
- Physical-device verification pending. User should use **Me → Check for Updates** and inspect only the left/right border lines. Do not claim the phone-side clipping is fixed until the user confirms.
- Rollback: exact pre-edit files are preserved on `backup/pre-mobile-diary-border-10px-2026-11-13`; restore only the affected HTML if required. Preserve notes, photos, settings and PIN data.


---

# Web Update 169 — Fix mobile Diary left/right border clipping (2026-11-13)

- User reported that the left/right border lines were still clipped after Web Update 168 and asked to correct them. Re-inspection found that the Diary panel is a flex item inside `#diaryMyNotesOverlay`; its default `min-width:auto` can prevent the panel from shrinking below its automatic content minimum. The overlay also already has 10px horizontal padding.
- Starting live state: Web Update 168; APK 1.0.136 / versionCode 135; package `com.personal.diaryapp`. Prior source/mirror blob SHA `d1b173fa83ee5cb85ffdc780d14205a0ee1a0402`; prior feed SHA-256 `e6d08089a138d3fc2026eceff7db1fcd5f247eda92ed4f616ca54b60e70d8b09`.
- Changed only the existing `diary-mobile-border-fit` block in `web-source/index.html`, source commit `f8bc9dbc4d85fc0f892bfe86533fd81bcf662549`: added `min-width:0` and `flex:0 1 auto` so the flex item can shrink; increased the panel width reduction from 10px to 20px total (`width` and `max-width:calc(100% - 20px)`), keeping auto horizontal margins, border-box sizing and the existing 420px breakpoint. This creates an additional 10px of total clearance compared with Web Update 168. No vertical position/height, border thickness/colour/style, panel content, features, gestures, Share, translations, notes/photos, storage, PIN/recovery, native Android source, APK, package identity or signing data changed.
- Pre-edit backup branch: `backup/pre-border-clip-followup-2026-11-13`. Exact readable backups re-fetched and verified byte-identical:
  - `backups/web-source-before-border-clip-followup-2026-11-13.html` — blob `d1b173fa83ee5cb85ffdc780d14205a0ee1a0402`
  - `backups/diary-web-before-border-clip-followup-2026-11-13.html` — same blob
  - `backups/latest-before-border-clip-followup-2026-11-13.json` — blob `dc0794b352f5532034b0bf62ff37c7b62984eb54`
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-border-clip-followup-2026-11-13.md` — blob `50a36e60e4ae52233c19f943e1a29322e2ee3241`
- Diff was limited to the single existing mobile CSS block. The CSS block braces are balanced; targeted checks confirmed the new shrink allowance, 20px total panel width reduction, centering, unchanged 420px breakpoint and unchanged vertical rules. JavaScript and application logic were not modified.
- Web-only publisher workflow run `43415645933`, run 159, completed with **success**; publish job `131852720937` succeeded. Publisher output commit: `6755760a81ca382438f620c4dcac151d4dbe8b78`. Live source and published mirror are byte-identical; both blob SHA `5dddf6c526402e6300ddb1028f746c45fd6c5c6a`. Independently calculated UTF-8 SHA-256 `3aa66bec80991551df39d9de3807552ae76b15cab47eb8d5dd9bc3b6bdff0a94` matches live `latest.json.webSha256`; live `webVersion=169`.
- APK unchanged: 1.0.136 / versionCode 135; SHA-256 `6fc74ca82888fed4121cc352c1846ec8c6a7063e2d2a33fbe032726f7a244348`. No APK rebuild or signing changes.
- Physical-device verification **pending**. User should use **Me → Check for Updates**, then inspect the left/right border lines. Do not claim phone-side success until user confirms.
- Rollback: restore only the pre-edit HTML from the verified backup branch if needed; preserve notes, photos, settings and PIN data.


---

# Web Update 170 — Further mobile Diary border clearance (2026-11-13)

- User reported that the left/right Diary panel border remained clipped after Web Update 169. Checked the actual native update path in the generated Android project script: the “Diary pehle se update hai” response is shown when the installed `filesDir/diary-web/index.html` SHA-256 already matches the current feed hash; it then clears WebView cache and reloads the verified local file. Therefore this message did not mean the new CSS was skipped; it meant the current Web Update 169 HTML was already installed.
- Rechecked the exact mobile CSS and confirmed Web Update 169 had the panel at `calc(100% - 20px)`, with `box-sizing:border-box`, `min-width:0`, flex shrink, and centered auto margins. The overlay itself has 10px padding, and the Diary panel has raised 3D edge/shadow styling. To provide additional visible clearance without changing vertical layout or 3D border styling, increased only the panel's mobile total width reduction by a further 10px: `width` and `max-width:calc(100% - 30px)`, i.e. 15px each side. Existing 420px breakpoint, flex shrink, min-width, box sizing, and centering remain.
- Starting state: Web Update 169; APK 1.0.136 / versionCode 135; package `com.personal.diaryapp`. Source/mirror prior blob SHA `5dddf6c526402e6300ddb1028f746c45fd6c5c6a`; feed hash `3aa66bec80991551df39d9de3807552ae76b15cab47eb8d5dd9bc3b6bdff0a94`.
- Changed only the existing `diary-mobile-border-fit` CSS block in `web-source/index.html`, source commit `4b56f17247c5a962d601fe0446f57770694c3a9a`, final source blob `06dc67027578c3a9ce8dfc6922f8aef0cca114e4`. No height, top/bottom position, border thickness/colour/style, panel content, application logic, translations, notes/photos, storage, PIN/recovery, native Android source, APK, package identity or signing data changed.
- Pre-edit backup branch: `backup/pre-mobile-border-fit-30px-2026-11-13`. Exact backups re-fetched and verified identical:
  - `backups/web-source-before-mobile-border-fit-30px-2026-11-13.html` — blob `5dddf6c526402e6300ddb1028f746c45fd6c5c6a`
  - `backups/diary-web-before-mobile-border-fit-30px-2026-11-13.html` — same blob
  - `backups/latest-before-mobile-border-fit-30px-2026-11-13.json` — blob `7511095bbdbf8b20386507f532acb06199eaad3a`
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-mobile-border-fit-30px-2026-11-13.md` — blob `048b0800312cd866d45c0a9c53389589e0990154`
- Diff limited to the one existing mobile CSS block; exact selector and declarations checked; braces balanced. Web-only publisher workflow run `43416391968`, run 160, completed successfully; publish job `131855257914` succeeded. Live source and published mirror are byte-identical, blob SHA `06dc67027578c3a9ce8dfc6922f8aef0cca114e4`. Independently calculated UTF-8 SHA-256 `ff55b50443518dc79d7384e6bcb6131d4bed7b957c1bab416150b44e91ac742e` matches live `latest.json.webSha256`; live `webVersion=170`.
- APK unchanged: 1.0.136 / versionCode 135; SHA-256 `6fc74ca82888fed4121cc352c1846ec8c6a7063e2d2a33fbe032726f7a244348`. No APK rebuild or signing changes.
- Physical-device verification pending. User should tap **Me → Check for Updates**; if the checker again reports already updated, it indicates the installed HTML hash is current. Then inspect the left/right outer border. Do not claim phone-side success until the user confirms.
- Rollback: exact pre-edit files preserved on `backup/pre-mobile-border-fit-30px-2026-11-13`; preserve all notes, photos, settings and PIN data.


---

# Web Update 171 — Center Diary panel to equal mobile screen gutters (2026-11-13)

- User reported that the Diary page did not appear evenly fitted to the mobile screen: moving the page left or right caused one side to move inward while the other remained clipped. The earlier mobile rule subtracted a second percentage from a flex overlay that already had 10px horizontal padding, making panel width depend on the padded content box rather than directly using the available screen width.
- Starting state: Web Update 170; APK 1.0.136 / versionCode 135; package `com.personal.diaryapp`. Starting source/mirror blob SHA `06dc67027578c3a9ce8dfc6922f8aef0cca114e4`; feed SHA-256 `ff55b50443518dc79d7384e6bcb6131d4bed7b957c1bab416150b44e91ac742e`.
- Changed only the existing `diary-mobile-border-fit` CSS block in `web-source/index.html`, source commit `b46f11410de693e98bd61ba6f710348c7f3ab2a7`. Removed the `calc(100% - 30px)` width rule. The overlay now supplies symmetric left/right gutters using `max(12px, env(safe-area-inset-left/right, 0px))`; the Diary panel uses `width:100%`, `max-width:760px`, `min-width:0`, a shrinkable flex basis, and auto side margins. This makes the panel fit the overlay's actual available width and keeps it centered without independent left/right nudging.
- No panel height, vertical position, border thickness/colour, 3D border/shadow, Diary content, translations, notes/photos, storage keys, PIN/recovery, native Android source, APK, package identity or signing data changed. Full source commit diff reviewed: only the one existing CSS block changed.
- Pre-edit backup branch: `backup/pre-centered-mobile-diary-panel-2026-11-13`. Verified readable exact backups:
  - `backups/web-source-before-centered-mobile-diary-panel-2026-11-13.html` — blob `06dc67027578c3a9ce8dfc6922f8aef0cca114e4`
  - `backups/diary-web-before-centered-mobile-diary-panel-2026-11-13.html` — same blob
  - `backups/latest-before-centered-mobile-diary-panel-2026-11-13.json` — blob `2d846ca0573d03840885a5ccc3629996dbd1da69`
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-centered-mobile-diary-panel-2026-11-13.md` — blob `f409ccea7adaef3d6d90c6d4cb060142594db751`
- Web-only publisher workflow run `43417578157`, run 161, completed with **success**; publish job `131859266460` succeeded. Publisher advanced live feed to webVersion `171`. Re-fetched source and published mirror are byte-identical; both Git blob SHA `a47e48aa1eb74cd5f44ec655764ece6ce97ad532`. Independently calculated UTF-8 SHA-256 `51bb5ed38c96f360fa9de1ddb75faea159805f4a19e45c5844912f9d1598ad42` matches live `latest.json.webSha256`.
- APK unchanged: 1.0.136 / versionCode 135; SHA-256 `6fc74ca82888fed4121cc352c1846ec8c6a7063e2d2a33fbe032726f7a244348`. No APK rebuild or signing changes.
- Physical-device verification **pending**. User should use **Me → Check for Updates**, then inspect whether the left and right outer borders have equal space and both remain fully visible. Do not claim the phone-side issue is fixed until the user confirms.
- Rollback: exact pre-edit files preserved on `backup/pre-centered-mobile-diary-panel-2026-11-13`; preserve all Diary notes, photos, settings and PIN data.


---

# Web Update 172 — Fit locked Note card and PIN controls on mobile (2026-11-13)

- User clarified that the left/right clipping is noticed specifically when a Note is locked, not on the general Diary page. Starting state: Web Update 171; APK 1.0.136 / versionCode 135; package `com.personal.diaryapp`; starting source blob `a47e48aa1eb74cd5f44ec655764ece6ce97ad532`; starting feed SHA-256 `51bb5ed38c96f360fa9de1ddb75faea159805f4a19e45c5844912f9d1598ad42`.
- Changed only a new CSS block `diary-note-lock-mobile-fit` in `web-source/index.html`. It targets the expanded locked Note card containing the `diary-note-pin` input, constrains that card to the available list width with border-box sizing and zero minimum width, and keeps the PIN field and its content within the card. No Note Lock/Unlock logic or PIN/recovery data was changed.
- The general Diary panel sizing CSS from Web Update 171 was left untouched. No notes, photos, settings, translations, storage keys, PIN/recovery logic, native Android source, APK, package identity or signing data changed.
- Pre-edit backup branch: `backup/pre-note-lock-mobile-fit-2026-11-13`. Backups preserved:
  - `backups/web-source-before-note-lock-mobile-fit-2026-11-13.html` — pre-edit source blob `a47e48aa1eb74cd5f44ec655764ece6ce97ad532`
  - `backups/diary-web-before-note-lock-mobile-fit-2026-11-13.html` — exact pre-edit published mirror
  - `backups/latest-before-note-lock-mobile-fit-2026-11-13.json`
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-note-lock-mobile-fit-2026-11-13.md`
- Source commit `72d68e7b9cb8f69bc9adfb24d5c341dc1cdfff58`. Web-only publisher workflow run `43418912556`, run 162, completed successfully. Live feed advanced to webVersion `172`; live `webSha256=3c17afe300473dd43e98201423961390ef431c1b01fca408795489559f71a7e2`. Source and published mirror are byte-identical; both blob SHA `34a031dedbdc94d50a861abb40b32a4dbb310125`.
- APK unchanged: 1.0.136 / versionCode 135; SHA-256 `6fc74ca82888fed4121cc352c1846ec8c6a7063e2d2a33fbe032726f7a244348`. No APK rebuild or signing changes.
- Physical-device verification **pending**. Ask the user to use **Me → Check for Updates**, then lock a Note and check whether the locked Note card and both side borders fit evenly inside the mobile screen. Do not claim the phone-side issue is fixed until the user confirms.
- Rollback: exact pre-edit files preserved on `backup/pre-note-lock-mobile-fit-2026-11-13`; preserve all Diary notes, photos, settings and PIN data.


---

# Web Update 173 — Stack and enlarge locked Note PIN action buttons (2026-11-13)

- User reported that the text on the locked Note actions “❓ PIN Bhool Gaye?” and “🔓 Tala Band Karein” overflowed their buttons while the buttons were side-by-side. User requested larger buttons arranged vertically.
- Starting state: Web Update 172; APK 1.0.136 / versionCode 135; package `com.personal.diaryapp`; starting source/mirror blob SHA `34a031dedbdc94d50a861abb40b32a4dbb310125`; prior feed SHA-256 `3c17afe300473dd43e98201423961390ef431c1b01fca408795489559f71a7e2`.
- Changed only the locked Note PIN action controls in `web-source/index.html`: their wrapper now uses a vertical flex column with full width and spacing; each button is full width, minimum 46px high, larger 14px bold text, increased padding, and wrapping enabled so localized labels stay inside. Button event handlers and PIN/lock behaviour remain unchanged.
- No other Note cards, general Diary layout, languages/translations, notes/photos/storage, PIN/recovery data or logic, native Android source, APK, package identity or signing data changed.
- Pre-edit backup branch: `backup/pre-note-lock-action-buttons-stack-2026-11-13`. Exact pre-edit source, published mirror, `latest.json`, and this Master Register were backed up under `backups/*-before-note-lock-action-buttons-stack-2026-11-13.*` on that branch.
- Source commit `34a9cc0804793fd7c3d4e6c16c1aea411d06ce54`; final source/mirror blob SHA `09a97742b81d4ba6794fc59bd3054b34f08d6fd0`. Publisher workflow run `43419663486`, run 163, completed successfully; publish job `131866187842` succeeded. Live feed advanced to webVersion `173`; live `webSha256=73175c989ab35b7f72f5358336c056cc39e4112b036d71232f6b5c0b1fdc1d6f`. Re-fetched source and published mirror are byte-identical.
- APK unchanged: 1.0.136 / versionCode 135; SHA-256 `6fc74ca82888fed4121cc352c1846ec8c6a7063e2d2a33fbe032726f7a244348`. Web-only update; no APK rebuild or signing changes.
- Physical-device verification **pending**. User should use **Me → Check for Updates**, open a locked Note, and confirm the two action buttons appear one above the other with all text inside. Do not claim phone-side success until user confirms.
- Rollback: restore the exact pre-edit HTML from `backup/pre-note-lock-action-buttons-stack-2026-11-13`; preserve notes, photos, settings and PIN data.


---

# Web Update 174 — Confirm discard when closing an unsaved New Note (2026-11-13)

- User requested an × close control flow while writing a new Note: ask before removing the unfinished writing.
- Starting live state: Web Update 173; APK 1.0.136 / versionCode 135; package `com.personal.diaryapp`; starting source/mirror blob SHA `09a97742b81d4ba6794fc59bd3054b34f08d6fd0`; previous feed SHA-256 `73175c989ab35b7f72f5358336c056cc39e4112b036d71232f6b5c0b1fdc1d6f`.
- Changed only the × button click handler and the three existing language dictionaries (Roman English, English, Hindi). When a new unsaved draft contains text, a cover/details/photo attachment, or a selected image colour, × asks for confirmation. Confirming resets only the in-memory new draft using the existing `newNote()` reset routine and closes the Diary. Choosing Cancel leaves the draft and editor open. Closing an existing saved Note does not ask and does not alter it. The overlay backdrop and Escape/Android Back paths were not changed.
- Existing save flow, note storage format/keys, saved Notes, photos already saved, PIN/lock/recovery, search, editor layout, native Android code, APK, package identity and signing data were not changed.
- Pre-edit backup branch: `backup/pre-new-note-close-discard-2026-11-13`. Exact pre-edit files were saved and re-fetched:
  - `backups/web-source-before-new-note-close-discard-2026-11-13.html` — blob `09a97742b81d4ba6794fc59bd3054b34f08d6fd0`
  - `backups/diary-web-before-new-note-close-discard-2026-11-13.html` — same blob
  - `backups/latest-before-new-note-close-discard-2026-11-13.json` — blob `b1a5ed98412646aead746ce24b3e314d6d63887e`
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-new-note-close-discard-2026-11-13.md` — blob `23d0d6defa08ff15569be16d7c98b348a9ac034b`
- Source commit `572f82fa2fd35bbe7212813fb47ad3df83499491`; final source blob `ca8b9420b1c8ef58312d4fe627f6bffeaf312239`. The web-only publisher workflow run `43426737220`, run 164, completed successfully; publish job `131889866019` succeeded. Live feed advanced to webVersion `174`; live `webSha256=c3ed3642eea1d28e18bdb1705939466ef4aa623ed0260879f9209b3273246bd5`. Re-fetched source and published mirror are byte-identical (same blob SHA).
- APK unchanged: 1.0.136 / versionCode 135; SHA-256 `6fc74ca82888fed4121cc352c1846ec8c6a7063e2d2a33fbe032726f7a244348`. Web-only release; no APK rebuild or signing changes.
- Physical-device verification **pending**. User should use **Me → Check for Updates**, open **＋ New Note**, type a short test, and tap ×. Confirm should discard and close; Cancel should keep the text and editor open. Also verify an empty New Note closes without a confirmation. Do not claim phone-side success until the user confirms.
- Rollback: restore the exact pre-edit HTML from `backup/pre-new-note-close-discard-2026-11-13`; preserve all notes, photos, settings and PIN data.

## Web Update 175 — New Note page par alag × se sirf draft clear (2026-11-13)
- User clarified the intended behavior: New Note editor visible rahe; uske apne × par tap karne se typed title/body aur added draft images/content clear ho, editor band na ho.
- Added a separate × control at the top of `diaryMyNotesEditor`. It calls the existing `newNote()` reset routine, so draft text, draft photo/image data and draft formatting reset while the writing pad stays visible. No extra confirmation dialog is shown.
- The separate editor × is shown for a new unsaved note and hidden while editing an existing saved note.
- Restored the main Diary overlay close button to its original direct `closeOverlay` behavior. It no longer contains the earlier mistaken draft-discard logic.
- No changes to saved Notes, storage format, existing Note lock/PIN/recovery, share, search, APK/native code, package identity or signing.
- Source commit: `131794e2f32a58a62fa85b33bbf0504202caa3db`; source/mirror blob SHA: `39e326970ad28dc3462c50e92edb4fbe6b396c96`. `web-source/index.html` and `diary-web/index.html` were re-fetched and verified byte-identical.
- Publisher workflow run `43427869229` (run 165), publish job completed successfully. Live `latest.json` reports webVersion `175`, webSha256 `8785bf67609495c847d21a6248fa9b9cdf886852788fd38959760e58d57b0b19`.
- Physical-device test pending. User should use **Me → Check for Updates**, open **＋ New Note**, type something and add a photo, then tap the new ×. Confirm the text/photo clear and the writing pad remains open. Do not claim phone-side verification until user confirms.

## Web Update 176 — New Note × sirf draft par visible (2026-11-13)
- User confirmed: × should remain hidden while New Note is empty, appear only after text is typed or an image is added, and disappear again when tapped to clear the draft.
- Implemented live visibility updates for title/body typing and the existing photo, cover-image and detail-image preview completion paths. The button is shown only for an unsaved New Note with draft content. Tapping it calls the existing `newNote()` reset routine; it clears draft text/images and leaves the writing pad open.
- No change to saved-note editing behavior, main Diary close button, saved notes/storage, Note lock/PIN/recovery, APK/native code, package identity or signing.
- Source commit: `993551bb9455f12b028d0b2df97c24e2997ec653`; source and published mirror were re-fetched and verified byte-identical, blob SHA `098ec07a4f0ef8205a7b42367304c1b033b4d665`.
- Publisher workflow run `43428578542`, run 166, and publish job completed successfully. Live `latest.json` reports webVersion `176`, webSha256 `19d6828ff323f044df54e8c1bac450da63a0f3e0ca72505672994119a95cb01b`.
- Physical-device verification pending. User should use **Me → Check for Updates**, then test: empty New Note has no ×; typing or adding an image shows ×; tapping × clears the draft and hides × while keeping the pad open. Do not claim phone-side verification until user confirms.

## Web Update 177 — New Note × hide/show CSS correction (2026-11-13)
- User reported the clear × remained visible after tapping it to clear the draft.
- Re-inspection found the button's CSS explicitly set `display:block`, which could override the browser's built-in `hidden` behavior. Removed that display declaration and switched the visibility function to the button's `hidden` property. The click handler now also refreshes visibility after the existing `newNote()` reset.
- Source commit: `2f5bc69a2dbf38774df5c3092306912e0d597d80`; source and published mirror re-fetched and verified byte-identical, blob SHA `bdd72933f3c238957a893bc3cfcb1e0d61143823`.
- Publisher workflow run `43428899194`, run 167, publish job completed successfully. Live `latest.json` reports webVersion `177`, webSha256 `8c22fecf2a7112996490b66417fea86ced92161a925ae1a9dbb201d5f432305d`.
- Physical-device verification pending. Test after **Me → Check for Updates**: empty New Note hides ×; text/image makes it appear; tapping × clears the draft and hides ×.


## Web Update 178 — New Note clear × right side restored (2026-11-13)
- User clarified that only the separate × on the New Note writing pad had shifted to the left; it must return to the right. Kept the editor, title/body fields, images, visibility behavior, clear action, main Diary close button, saved notes, and all other functions unchanged.
- Root cause: the clear × is a button (inline-block by default), so its auto left margin did not reliably align it to the right. Changed only its visible-state CSS selector to `#diaryMyNotesDraftClearX:not([hidden])` and set `display:block`; retained the existing right-aligning auto margin. Using the `:not([hidden])` selector preserves native hidden behavior when the draft is empty or after clearing.
- Exact pre-edit files backed up on branch `backup/new-note-clear-x-right-2026-11-13`: `backups/web-source-before-new-note-clear-x-right-2026-11-13.html`, `backups/diary-web-before-new-note-clear-x-right-2026-11-13.html`, `backups/latest-before-new-note-clear-x-right-2026-11-13.json`, and `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-new-note-clear-x-right-2026-11-13.md`.
- Source commit: `5efa345f140541b0055aa1135b4100257ddbe4d9`; source blob `7046e907a57068ad8f07f7707d4d69ed3cfe7dc7`. Web publisher workflow run `43429955889` completed successfully. Live webVersion is `178` with webSha256 `df38b4c0af55507788b9187f0ff05c6bdb1d21c7af2594765bb6ae61c8d9aaa7`.
- Re-fetched source and published mirror are byte-identical (blob SHA `7046e907a57068ad8f07f7707d4d69ed3cfe7dc7`). APK remains unchanged at 1.0.136 / versionCode 135; no APK rebuild or signing changes.
- Physical-device verification pending. Use **Me → Check for Updates**, open **＋ New Note**, type a short test, and confirm the × appears on the right. Tap it and confirm the draft clears, the × disappears, and the writing pad remains open. Empty New Note should keep × hidden.


---

# Web Update 180 — Show and support clear × while editing saved Notes (2026-11-13)

- User request: while editing an existing saved Note, show the same editor-page × clear control used for a New Note and make it clear the current editor content in the same way.
- Starting live state: Web Update 179; APK 1.0.136 / versionCode 135; package com.personal.diaryapp; source/mirror blob SHA 4996fe1441e649f29c772c058f06bbcf9470e500; prior feed SHA-256 14a3ef144df495d1919fc2a5f4b93f35ddda0a76b69adcec4b81ac43ab9749af.
- Web-only scope: changed only web-source/index.html. The clear × is now visible in saved-note edit mode whenever the editor contains a title, body, attached photo, cover/detail image, or cover/detail text. Tapping it uses the existing New Note reset routine to clear the in-memory editor fields and image data, then restores the current saved note ID, category and Delete button so the user remains in Edit mode. The existing note is not written to storage or deleted by ×; any subsequent save continues to target that same note. The existing non-empty save validation remains unchanged.
- The clear × visibility refreshes when an existing Note is opened. New Note visibility and behavior remain unchanged. The existing Note close button, save logic, note data format/storage keys, photos in saved records, PIN/lock/recovery, translations, updater, pamphlet-template backward compatibility, native Android source, APK, package identity and signing data were not changed.
- Pre-edit backup branch: backup/edit-note-clear-x-2026-11-13. Four files were created and re-fetched readable:
  - backups/web-source-before-edit-note-clear-x-2026-11-13.html — pre-edit source blob 4996fe1441e649f29c772c058f06bbcf9470e500
  - backups/diary-web-before-edit-note-clear-x-2026-11-13.html — exact pre-edit published mirror
  - backups/latest-before-edit-note-clear-x-2026-11-13.json — pre-edit feed
  - backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-edit-note-clear-x-2026-11-13.md — pre-edit register
- Source commit: 2abb20b5d958f61703d8a594f1d236c64dee8a67. The full diff was reviewed and contains only the clear × click routing, visibility gate, edit-draft reset helper, and openNote visibility refresh. Both inline JavaScript blocks parsed successfully. Targeted static checks confirmed the × routes New Note to its original reset and saved-note Edit to the new edit-preserving reset; the edit reset restores the active note ID/category and Delete control; openNote refreshes × visibility.
- Web publisher workflow run 43432343803 (run 170) completed with **success**; publish job and all steps succeeded. Publisher commit: 4801bcdda217afe4ad4335c21fcaca7937dfd17e. Live source and published mirror are byte-identical; both blob SHA b612bde3339702f5c80feb63d5189531613bf504. Independently computed UTF-8 SHA-256 ddf7e372e7eaa03b294069059fb75f6b6894fc201ccd0fe583feb6cd2b4dc4a9 matches live latest.json webSha256. Live webVersion is 180.
- APK unchanged: 1.0.136 / versionCode 135 / SHA-256 6fc74ca82888fed4121cc352c1846ec8c6a7063e2d2a33fbe032726f7a244348. No APK rebuild or signing changes.
- Physical-device verification pending. User should use Me → Check for Updates, open a saved Note with existing text/photo, confirm × appears, tap × and confirm text/images clear while the same Note remains in Edit mode; then type replacement text and confirm Save updates that same Note. Also confirm New Note × behavior remains unchanged. Do not claim phone-side verification until user confirms.
- Rollback: exact pre-edit source, mirror, feed and register are preserved on backup/edit-note-clear-x-2026-11-13. Restore only the affected HTML if a regression is found; preserve saved notes, photos, settings and PIN data.


# Web Update 179 — Remove Pamphlet Chunein button (2026-11-13)

- User requested removal of the **🪄 Pamphlet Chunein** button.
- Starting live state: APK `1.0.136` / versionCode `135`; webVersion `178`; package `com.personal.diaryapp`; source/mirror blob SHA `7046e907a57068ad8f07f7707d4d69ed3cfe7dc7`; prior feed SHA-256 `df38b4c0af55507788b9187f0ff05c6bdb1d21c7af2594765bb6ae61c8d9aaa7`.
- Scope: web-only, only `attachDiaryColourChooser(kind)` in `web-source/index.html`. Removed creation and event handling of the Pamphlet Chunein button and its chooser gallery from the three existing image controls (Cover, Details, attached Photo). The existing Choose Image, Solid Colour and Gradient Colour controls remain.
- Preserved backward compatibility: existing saved notes that already contain a pamphlet template ID still render with their stored design. `cleanDiaryColour`, `diaryPamphletStyle`, saved-note preview, image rendering and share artwork template support were not removed. Existing notes, photos, storage, PIN/recovery, translations, updater, native Android source, APK, package identity and signing data were not changed.
- Pre-edit backup branch: `backup/pre-remove-pamphlet-button-2026-11-13`. Four exact files were created and re-fetched byte-identically:
  - `backups/web-source-before-remove-pamphlet-button-2026-11-13.html` — blob `7046e907a57068ad8f07f7707d4d69ed3cfe7dc7`
  - `backups/diary-web-before-remove-pamphlet-button-2026-11-13.html` — same blob
  - `backups/latest-before-remove-pamphlet-button-2026-11-13.json` — blob `c171744f7da41c477014fe93846afea12f91f15f`
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-remove-pamphlet-button-2026-11-13.md` — blob `4eda91076b66ee4a08a745cdf6a38e2f609d0479`
- Source change commit: `1acb4e1ec1d369cce8b6c2b25f8b34ee81202eb7`; source blob SHA `4996fe1441e649f29c772c058f06bbcf9470e500`. The exact source diff was reviewed: it deletes only the pamphlet button/gallery construction and removes the button/gallery from the image chooser menu assembly.
- Both inline JavaScript blocks parsed successfully. Targeted checks confirm no runtime pamphlet button/gallery construction or handler remains; image selection, solid colour, gradient colour and the existing saved-template renderer remain.
- Publisher output commit: `230a8a0b31d314569d7d49d7afd1869779406055` (GitHub Actions bot, “Publish My Diary web bundle update”). It changed only `diary-web/index.html` and `latest.json`. Live source and mirror were re-fetched and are byte-identical; both blob SHA `4996fe1441e649f29c772c058f06bbcf9470e500`. Live feed reports webVersion `179` and `webSha256=14a3ef144df495d1919fc2a5f4b93f35ddda0a76b69adcec4b81ac43ab9749af`. The workflow run ID/conclusion was not independently exposed by the available GitHub read endpoint; publisher bot commit and matching live feed/mirror confirm publication, but do not substitute for a separately observed workflow conclusion.
- APK unchanged: `1.0.136` / versionCode `135`; APK SHA-256 `6fc74ca82888fed4121cc352c1846ec8c6a7063e2d2a33fbe032726f7a244348`. No APK rebuild or signing changes.
- Physical-device verification pending. User should use **Me → Check for Updates**, then open each of the three image controls and confirm **Pamphlet Chunein** is absent while **Choose Image**, **Solid Colour**, and **Gradient Colour** remain. Also open an older note that already used a pamphlet design and confirm its saved appearance remains. Do not claim phone-side verification until user confirms.
- Rollback: exact pre-edit source, mirror, feed and register are preserved on `backup/pre-remove-pamphlet-button-2026-11-13`; restore the exact HTML if testing reveals a regression. Preserve notes, photos, settings and PIN data.


---

# Register Policy Update — Mandatory entry for every successful task (2026-11-13)

- User instruction: always add a Master Register entry for work that is completed successfully, and add a standing rule requiring this for all future successful work.
- Added the **MANDATORY SUCCESS-ENTRY RULE** to Section F and a matching mandatory item to the reusable task checklist in Section G. The rule covers all successful work, including small fixes and non-release tasks, and requires evidence plus honest pending/blocked status; chat history is not a substitute for a Register entry.
- The existing **Web Update 180** entry already records the saved-Note clear × implementation, backup, checks, publishing workflow, source/mirror/feed verification, and pending physical-device test. No new code or release was made in this policy-only task.
- Backup: `backup/register-success-entry-rule-2026-11-13` → `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-success-entry-rule-2026-11-13.md`; backup commit `945ca910ee7f2e59af6275197dec0c163096ec10`.
- Scope: only `docs/PROJECT_MAP_AND_SECRETS_REGISTER.md` changed on the default branch. No app source, mirror, latest.json, APK, signing data, notes, photos, settings, or PIN/recovery data changed.
- Verification: live register was fetched before editing; pre-edit register backup was created on a separate backup branch. Post-edit re-fetch and content/section verification are required before reporting completion.


---

# Me Button — Four new independent tools (Web Update 182, 2026-11-13)

- User selected and approved four new Me Button tools in this order: **Personal Calendar**, **My Kharcha**, **My Documents**, **My Memories**. Existing Diary Notes, existing saved-Notes Calendar, Note Lock, Diary Lock/PIN/recovery, updater and existing data must remain untouched.
- Starting live state: Web Update 180; APK 1.0.136 / versionCode 135; package `com.personal.diaryapp`; source/mirror blob `b612bde3339702f5c80feb63d5189531613bf504`; starting feed blob `aa8fadea5b34cd8959410b371b3c86ec06b0abda`.
- Scope: web-only, `web-source/index.html`. Added four separate purple/gold 3D-style buttons under Me, opening an independent feature page:
  - **Personal Calendar:** add and list dated birthday, anniversary and important-day entries.
  - **My Kharcha:** add income/expense entries with date, amount in INR, optional category/details, and running totals/balance.
  - **My Documents:** save and open local image/PDF files with a title.
  - **My Memories:** save dated text memories with an optional photo.
- All four features use a new, separate IndexedDB database `diary_me_features_v1` and object store `records`; they do not reuse or modify the existing Notes storage keys or the Diary safety-copy database. Attachments are stored as local Blob data; file-size limit is 20 MB. User data remains on the device; no cloud upload was added.
- A follow-up correction made optional form fields genuinely optional (the initial version mistakenly emitted a false-valued HTML boolean `required` attribute). Final source includes this correction.
- Explicit limitations for this first version: no edit/search/export-import or integration with the existing Notes backup yet; Personal Calendar currently stores and lists dates but does not send reminders or auto-repeat birthdays/anniversaries. The new database is separate and is **not encrypted by the existing Diary PIN**, so device/app PIN must not be assumed to protect these new records. Physical-device verification is pending; use dummy/test entries only until storage backup and privacy protection are added and tested.
- Pre-edit backup branch: `backup/me-four-features-before-implementation-2026-11-13`. Four exact, readable backups re-fetched successfully:
  - `backups/web-source-before-me-four-features-2026-11-13.html` — original blob `b612bde3339702f5c80feb63d5189531613bf504`
  - `backups/diary-web-before-me-four-features-2026-11-13.html` — same original blob
  - `backups/latest-before-me-four-features-2026-11-13.json` — blob `aa8fadea5b34cd8959410b371b3c86ec06b0abda`
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-me-four-features-2026-11-13.md` — blob `63942493cc15dda564fd9f01961ae47d02137c6c`
- Source commits: initial implementation `23ec8cb253456ecfda775c243a31da1591cd012f`; optional-field correction `524629c81c3c937ea9b1d2fe7996348eb86cf366`.
- Web-only publisher workflow runs: `43435266550` (run 171) and `43435584101` (run 172); both completed **successfully**, including all publish-job steps. Final live webVersion: **182**.
- Final source and published mirror were re-fetched and are byte-identical; both Git blob SHA `2797094230b8a7864d531988d65f33798f44e759`. Independently calculated UTF-8 SHA-256 `436873076a491bd9d8759e7b6506e517469a89fc57c9893b18708f69354c2dd1` matches live `latest.json.webSha256`.
- Both inline JavaScript blocks passed syntax parsing. Static checks confirmed the new feature database, four feature labels/buttons, and optional-field correction. No live-device runtime test was available.
- APK unchanged: 1.0.136 / versionCode 135 / SHA-256 `6fc74ca82888fed4121cc352c1846ec8c6a7063e2d2a33fbe032726f7a244348`. No APK rebuild, native Android, package identity or signing changes.
- Deliberately untouched: existing Notes and their storage, existing saved-Notes Calendar, photos already attached to Notes, Note Lock, Diary Lock/PIN/recovery, translations outside the new feature labels, updater, app sharing, theme controls, and all MUAZZIN project files.
- Phone test pending. Ask the user to use **Me → Check for Updates**, install Web Update 182, then test each feature with dummy data: add/delete one date, one income and one expense, one sample PDF/image document, and one text/photo memory; close and reopen each page to confirm data persists. Do not claim phone-side success until the user confirms.
- Rollback: restore only `web-source/index.html` from the verified pre-edit backup branch if regression is found; then re-run source/mirror/feed/hash checks. Preserve all user data and PIN records.


---

# Web Update 183 — Make My Kharcha amount entry obvious and visible (2026-11-13)

- User reported that the **My Kharcha** page did not show a clear box for entering how much was spent. Live code inspection found the numeric amount input was generated, but its generic label was only “Raqam (₹)” / “Amount (₹)”; the user-facing amount field needed a more explicit label and stronger visual distinction. No assumption was made that the phone had been tested.
- Starting live state: Web Update 182; APK 1.0.136 / versionCode 135; package `com.personal.diaryapp`; source/mirror blob `2797094230b8a7864d531988d65f33798f44e759`; feed blob `e196d0e94dcdf02566474b20d24f19aab5095ac1`; starting web SHA-256 `436873076a491bd9d8759e7b6506e517469a89fc57c9893b18708f69354c2dd1`.
- Web-only scope: changed only `web-source/index.html`. The amount field label is now **“Kitna Kharcha Hua (₹)”** in Roman English, with matching English and Hindi labels. Added a clear example placeholder (“Yahan rakam likhein, jaise 500” / translated equivalents), decimal numeric keyboard hint, accessible label, and a dedicated high-contrast purple/gold input style with explicit visible/display sizing. The existing amount input, positive-number validation, expense/income selector, save operation, and totals/balance calculations remain in place.
- No other feature, form, database, stored record, existing Notes, Personal Calendar, My Documents, My Memories, existing Note/Diary locks or PIN/recovery, updater, native Android source, APK, package identity, or signing data was changed.
- Pre-edit backup branch: `backup/my-kharcha-amount-field-2026-11-13`. All four backups were re-fetched and confirmed readable:
  - `backups/web-source-index-before-my-kharcha-amount-field-2026-11-13.html` — original blob `2797094230b8a7864d531988d65f33798f44e759`
  - `backups/diary-web-index-before-my-kharcha-amount-field-2026-11-13.html` — same original blob
  - `backups/latest-before-my-kharcha-amount-field-2026-11-13.json` — blob `e196d0e94dcdf02566474b20d24f19aab5095ac1`
  - `backups/docs-PROJECT_MAP_AND_SECRETS_REGISTER-before-my-kharcha-amount-field-2026-11-13.md` — original register blob `dc411328b84f5d4ff29aab09fbabf5e674bbbff1`
- Source change commit: `f201ec571857f94fe9ea3c8142e36e916aa0d5e7`. Diff reviewed: only the three language labels/placeholders, amount input accessibility/input-mode/class assignment, and dedicated amount-field CSS changed. Both inline JavaScript blocks passed syntax parsing. Static checks confirmed the new label/placeholder/style and the existing `record.amount=Number(amount.value)` save binding remains.
- Publisher workflow run `43437336597` (run 173) completed with **success**; publish job `131925734864` completed successfully. Publisher commit: `f217904abf4cd9fd0afba22b792ef27112daf6b6`. Live webVersion: **183**.
- Final live source and published mirror were re-fetched and are byte-identical; both blob SHA `c7ce6c6fd0456c416204e6ad3c37422cd21d6d32`. Independently calculated UTF-8 SHA-256 `bb4c5985646ffc89c4ef0e9db6725e98ef6e9fa6c54fb07c75c73caf3d61efa3` matches live `latest.json.webSha256`.
- APK unchanged: 1.0.136 / versionCode 135 / SHA-256 `6fc74ca82888fed4121cc352c1846ec8c6a7063e2d2a33fbe032726f7a244348`; no APK rebuild or signing changes.
- Physical-device verification pending. User should use **Me → Check for Updates**, install Web Update 183, open **💰 My Kharcha**, and confirm the prominent **Kitna Kharcha Hua (₹)** box appears, accepts a test amount (e.g. 500), saves, and contributes to the expense total. Do not claim phone-side verification until user confirms.
- Rollback: exact pre-edit source, published mirror, feed and register are preserved on `backup/my-kharcha-amount-field-2026-11-13`; restore only the affected HTML if testing reveals a regression. Preserve all saved data.

---

# Web Update 184 — Separate My Kharcha amount and expense inputs (2026-11-13)

- User clarified that My Kharcha needs two separate numeric boxes: Raqam (₹) for the available/received amount (example ₹5,000) and Kharcha (₹) for the spent amount (example ₹2,000). The totals below must show total Raqam/Income ₹5,000, total Kharcha ₹2,000, and remaining balance ₹3,000.
- Starting live state: Web Update 183; APK 1.0.136 / versionCode 135; source/mirror blob c7ce6c6fd0456c416204e6ad3c37422cd21d6d32; feed blob d10c4a80337ba3d45706020b4583b8038659c3a6; starting web SHA-256 bb4c5985646ffc89c4ef0e9db6725e98ef6e9fa6c54fb07c75c73caf3d61efa3.
- Web-only scope: web-source/index.html. Replaced the single amount-plus-income/expense selector with two clearly labelled, separate decimal inputs. Roman English, English and Hindi labels/placeholders are supplied. Optional expense item/category and details remain available. Each saved record stores the two values separately; the live summary adds the Raqam to income, adds Kharcha to expenses, and calculates the remaining balance. Existing historical records using the previous amount + flow structure are still included in totals and remain displayable.
- Validation: both inline JavaScript blocks passed new Function syntax parsing. Static checks confirmed both inputs, the two-value save logic, updated labels in all three languages, old-record compatibility, and the new total/balance calculation. Arithmetic example verified: ₹5,000 − ₹2,000 = ₹3,000. No database schema migration or deletion was made.
- Pre-edit backup branch: backup/my-kharcha-two-amount-boxes-2026-11-13. The exact live source, published mirror, latest feed and Master Register were backed up as backups/web-source-before-two-amount-boxes-2026-11-13.html, backups/diary-web-before-two-amount-boxes-2026-11-13.html, backups/latest-before-two-amount-boxes-2026-11-13.json, and backups/register-before-two-amount-boxes-2026-11-13.md. All four backup files were successfully created on the backup branch before editing.
- Source commit: df2ae309cc419deda28342723a36bcf4b305c20b. Publisher commit: b956660f14adec6ebd330c966ad5ed401fb8fce8. Published Web Update: 184. Live source and mirror are byte-identical; both Git blob SHA 243e5842a9efafab356fb2842450ab1f6c96d0f2. Independently calculated UTF-8 SHA-256 97baad776de526da1ab8ad2a24b8f7242247ab3088583299289a4401f2b71b34 matches latest.json webSha256.
- APK unchanged: 1.0.136 / versionCode 135 / SHA-256 6fc74ca82888fed4121cc352c1846ec8c6a7063e2d2a33fbe032726f7a244348; no APK rebuild, native Android, package identity or signing changes.
- Physical-device verification remains pending. User should use Me → Check for Updates, install Web Update 184, then enter Raqam 5000 and Kharcha 2000 in separate boxes and save; confirm the summary shows Raqam ₹5,000.00, Kharcha ₹2,000.00 and Baqi ₹3,000.00. Do not claim phone-side success until user confirms.
- Rollback: restore web-source/index.html from the verified pre-edit backup branch; republish and recheck source/mirror/feed/hash. Preserve all user data and the existing Notes/PIN records.
---

# Web Update 185 — Edit saved My Kharcha entries (2026-11-13)

- User asked to be able to edit a My Kharcha entry after adding it. Added an Edit button to each saved Kharcha record (Roman English, English and Hindi labels). Selecting Edit fills the existing form with that record's date, Raqam, Kharcha, expense name and details.
- Saving an edited entry reuses the original record ID and created timestamp, updating the existing IndexedDB record instead of creating a duplicate. The form returns to Add mode after a successful save. Delete behavior remains unchanged. Old-format Kharcha entries remain editable with compatible value prefill.
- Scope: web-source/index.html only. Pre-edit backup branch: backup/my-kharcha-edit-entry-2026-11-13. Backups: backups/web-source-before-kharcha-edit-2026-11-13.html, backups/diary-web-before-kharcha-edit-2026-11-13.html, backups/latest-before-kharcha-edit-2026-11-13.json, backups/register-before-kharcha-edit-2026-11-13.md.
- Source commit: 6e23e88fd5110ee2f556d40dda3da84b488c8f08. Published Web Update: 185. Source and published mirror are byte-identical; both blob SHA 746947562a558bcf5db02e4a65e797f534355962. latest.json webSha256: 9481d9d50d3258548ae73cf37bbf12027969f7762d45f682473ab00c868b61f8.
- Both inline JavaScript blocks passed syntax parsing before commit. Static checks verified all three edit labels, the Edit button, record prefill, original ID preservation, save-mode reset and old-record compatibility. No APK rebuild; APK remains 1.0.136 / versionCode 135.
- Physical-device verification is pending. After Me → Check for Updates installs Web Update 185, test adding Raqam 5000 / Kharcha 2000, editing one value, saving, and confirming the same entry updates without duplication and the totals/balance recalculate. Do not claim phone-side testing until user confirms.
- Rollback: restore web-source/index.html from the verified pre-edit backup branch, republish, and verify mirror/feed. Preserve user records and all existing Diary/Notes/PIN features.

---

# Web Update 186 — My Kharcha categories, reports, separate section PIN locks and Smart Search (2026-11-13)

- User approved four additions to the existing Me tools: expense categories with separate totals; PDF reports for My Kharcha and Personal Calendar; separate locks for My Kharcha, My Documents and My Memories; and Smart Search.
- Starting live state: Web Update 185; APK 1.0.136 / versionCode 135; package com.personal.diaryapp. Starting source/mirror blob SHA 746947562a558bcf5db02e4a65e797f534355962; starting feed webSha256 9481d9d50d3258548ae73cf37bbf12027969f7762d45f682473ab00c868b61f8.
- Scope: web-only, changed only web-source/index.html in source commit d7e80e91be2145686b5ef4fcb08a2cc4ddc05299. The publisher workflow mirrored the exact source into diary-web/index.html and advanced latest.json to Web Update 186.
- My Kharcha category entry retains a free-text field and adds suggestions for Khana/Food, Safar/Travel, Shopping, Bill/Bills, Ghar/Home, Sehat/Health, Taleem/Education and Other. The summary now displays expense totals grouped by the category text; the category filter narrows the visible records without changing saved data or the all-record totals.
- Smart Search is available within each Me feature list. It searches names/titles, dates, amounts, category, details, event type and document filename as applicable. Existing record IDs and stored record shapes remain intact.
- PDF Report buttons are available in My Kharcha and Personal Calendar. They prepare a clean report in a separate browser tab/window; the user chooses the browser's Print / Save as PDF action. This is a browser-generated print-to-PDF flow, not a direct background PDF download. Popup permission may be required.
- Separate PIN gates are added for My Kharcha, My Documents and My Memories. Each section creates its own 4–8 digit PIN on first access; salted PBKDF2-SHA-256 hashes are stored, not the raw PIN. Leaving the section returns to Me and requires the PIN again on next entry. **Important security limitation:** this is an app-screen access lock only. The existing IndexedDB records and attached files are not encrypted at rest, so this does not protect data from someone with direct access to browser/device storage. The UI explicitly tells the user this; do not describe it as file encryption or strong device-level protection. There is no in-app forgot/reset PIN recovery flow in this release, so the user must keep each PIN safe.
- Existing Kharcha data (including historical amount/flow records), Personal Calendar entries, documents, memories, photos, record IDs and IndexedDB database remain untouched; no migration or deletion was performed. Existing Notes storage, Note Lock, Diary Lock/PIN/recovery, native Android code, APK, package identity and signing data were not changed.
- Pre-edit backup branch: backup/me-kharcha-category-pdf-lock-smart-search-2026-11-13. Exact readable backups, each re-fetched and compared with the pre-edit live content:
  - backups/web-source-before-kharcha-category-pdf-lock-search-2026-11-13.html — blob 746947562a558bcf5db02e4a65e797f534355962
  - backups/diary-web-before-kharcha-category-pdf-lock-search-2026-11-13.html — same source blob
  - backups/latest-before-kharcha-category-pdf-lock-search-2026-11-13.json — blob eb3a05d2b9c98de601982efe662feab9c8b87aae
  - backups/register-before-kharcha-category-pdf-lock-search-2026-11-13.md — blob a518c750d5fb7c9d4ed4491a0ba0fbcad4179be0
- Diff review: the source commit changed only web-source/index.html (67 additions, 14 deletions). Both inline JavaScript blocks passed syntax parsing. Static checks confirmed the category suggestions and grouped totals, search controls and matching logic, report generation/print action, PBKDF2 PIN setup/check and all three language dictionaries (Roman English, English and Hindi).
- Publisher workflow run 43458317453 (run 176) completed with conclusion success; its only publish job and every step completed successfully. Publisher commit: bbc32c1f4fdc855b6dbab7d086704d06af4a09a7.
- Final live source and published mirror are byte-identical; both Git blob SHA 46c320b0597e54fbdca3371516a2c693bd06cb54. Independently computed UTF-8 SHA-256 4fa7cfc3c0366aa36e9fc0c4137907bebff544e270873e31b094a8c50770f5ea matches live latest.json.webSha256. Live webVersion is 186.
- APK unchanged: 1.0.136 / versionCode 135 / SHA-256 6fc74ca82888fed4121cc352c1846ec8c6a7063e2d2a33fbe032726f7a244348. No APK rebuild, native Android, package identity or signing changes.
- Physical-device verification pending. User should use Me → Check for Updates, install Web Update 186, then test category suggestions and per-category totals, Smart Search in each section, PDF report creation for Kharcha and Calendar, and first-time PIN setup/re-entry for Kharcha, Documents and Memories. Use dummy/test records initially; the PIN gate is not at-rest encryption. Do not claim phone-side success until user confirms.
- Rollback: restore web-source/index.html from the verified pre-edit backup branch, republish and re-check source/mirror/feed/hash. Preserve all user data and all existing Notes/PIN records.


---

# Web Update 187 — Manage and recover separate Me-section PIN locks (2026-11-13)

- User approved adding three independent PIN-management options to **My Kharcha**, **My Documents** and **My Memories**: remove a lock, change its PIN, and recover a forgotten PIN.
- Starting live state: Web Update 186; APK 1.0.136 / versionCode 135 / package `com.personal.diaryapp`; source/mirror blob `46c320b0597e54fbdca3371516a2c693bd06cb54`; starting feed SHA-256 `4fa7cfc3c0366aa36e9fc0c4137907bebff544e270873e31b094a8c50770f5ea`.
- Web-only scope: changed only `web-source/index.html`; publisher mirrored it to `diary-web/index.html` and advanced the web feed to Update 187. No native Android source, APK, package identity, signing material, existing Notes, Note Lock, Diary Lock, or unrelated feature was changed.
- Each protected section now has a **🔑 PIN** management control after it is unlocked. Changing PIN requires the current PIN and entering the new 4–8 digit PIN twice. Removing a lock requires the current PIN plus confirmation; it removes only that section's PIN/recovery configuration and does not delete its Kharcha/Documents/Memories records or attachments.
- New PIN setup creates a random 20-character hexadecimal recovery code. The user must save it outside the app and re-enter it to confirm. Only a salted PBKDF2-SHA-256 hash is stored in localStorage; the plaintext recovery code is shown during setup, not persisted. Forgot PIN accepts this code, lets the user set a new PIN, then generates and requires confirmation of a replacement recovery code (one-time rotation).
- Existing Update 186 PINs remain compatible and are not overwritten. Because those earlier PINs had no recovery code, the first successful unlock after this update prompts the user to create one. **If an existing PIN was already forgotten before a recovery code was created, this update cannot recover it retroactively.** The user must know the current PIN once to establish recovery.
- All three UI language dictionaries (Roman English, English, Hindi) include the new PIN/recovery labels and messages. Existing PIN storage keys `diary_me_section_pin_v1_<kind>`, 4–8 digit PIN validation, PBKDF2-SHA-256 with 120,000 iterations, and protected-section mapping remain unchanged. New recovery hashes use separate keys `diary_me_section_recovery_v1_<kind>`.
- Pre-edit backup branch: `backup/section-pin-management-recovery-2026-11-13`. Verified exact readable backups:
  - `backups/web-source-before-section-pin-management-recovery-2026-11-13.html` — blob `46c320b0597e54fbdca3371516a2c693bd06cb54`
  - `backups/diary-web-before-section-pin-management-recovery-2026-11-13.html` — same blob
  - `backups/latest-before-section-pin-management-recovery-2026-11-13.json` — blob `6d1761e207a305e87dbf87443b60f0707be537a2`
  - `backups/register-before-section-pin-management-recovery-2026-11-13.md` — blob `87506eb56fe9256f6ab69c8fa7f5411c9162b5a7`
- Source commit: `7c90390050d2d270a6de986b335af087f6d16884`. The source diff is confined to the Me-feature language labels, protected-section PIN/recovery functions, and the PIN-management header control. Both inline JavaScript blocks passed syntax parsing. Static checks confirmed the three protected section IDs, original PIN storage key and digest parameters are preserved, and the new recovery/change/remove handlers are present.
- Publisher workflow run `43460652702` completed with **success**; publish job `132006363405` and all five steps completed successfully. Publisher commit: `6014f03538c73a0a29d03727a3da77a89879f324`.
- Final live source and published mirror are byte-identical; both Git blob SHA `9ff42b600813d36073b813ff8a5554a70f67771d`. Independently calculated UTF-8 SHA-256 `391951ff6ca63e24728c8f2f67d374cbcaf7aa0260cf7732a7669d06a9414137` matches live `latest.json.webSha256`. Live webVersion: **187**.
- APK unchanged: 1.0.136 / versionCode 135 / SHA-256 `6fc74ca82888fed4121cc352c1846ec8c6a7063e2d2a33fbe032726f7a244348`; no APK rebuild or signing changes.
- Physical-device verification is **pending**. Test each of the three sections separately: first unlock an existing PIN and save the displayed recovery code; change PIN using old PIN and verify the new PIN; leave/re-enter and unlock; use Forgot PIN with the recovery code and save the replacement code; finally remove the lock using the current PIN and confirm saved records remain. Do not claim phone-side testing until the user confirms.
- Rollback: restore `web-source/index.html` from the verified backup branch, republish, and re-check source/mirror/feed/hash. Preserve all user data.


---

# Web Update 191 — Match all three Me-section locks to Note Lock (2026-11-13)

- User requested that the separate locks for **My Kharcha**, **My Documents** and **My Memories** work the same way as the existing Note Lock.
- Starting live state: Web Update 187; APK 1.0.136 / versionCode 135; source/mirror blob `9ff42b600813d36073b813ff8a5554a70f67771d`; starting web SHA-256 `391951ff6ca63e24728c8f2f67d374cbcaf7aa0260cf7732a7669d06a9414137`.
- Scope: only `web-source/index.html` was changed. The publisher mirrored it to `diary-web/index.html`. No Android source, APK, package identity, signing files, existing Note Lock, Diary Lock, notes, photos, or Me-section records/attachments were modified.
- All three protected sections now use the Note Lock's **4-digit numeric PIN** flow:
  - First setup asks for a new 4-digit PIN and confirmation, using the same style of on-screen PIN popup.
  - Unlock accepts the current PIN. Four-digit PINs auto-submit as in Note Lock.
  - **Forgot PIN** shows a newly generated temporary 4-digit PIN with a Copy button; after the user re-enters it correctly, the app asks them to create and confirm a new 4-digit PIN.
  - **Change PIN** verifies the current PIN first, then asks for a new 4-digit PIN twice.
  - **Remove Lock** verifies the current PIN before removing only the PIN setting for that section. The section's saved records and attachments remain.
- Compatibility for PINs created in Update 186/187: existing 4-digit PINs remain valid and are marked as 4-digit after their first successful unlock. If an existing PIN is 5–8 digits, the user must enter it once successfully, then create a new 4-digit PIN. This avoids silently losing access to older PIN-protected sections.
- Previous section-specific recovery-code setup is replaced by the Note Lock-style generated temporary PIN recovery flow. Any old section recovery hash is discarded when a new PIN is saved. **Security limitation:** like the existing Note Lock forgot-PIN flow, the temporary recovery PIN is displayed by the app to whoever can reach that section's lock screen; it is not an independent identity check. The lock remains an app access gate, not encryption of data at rest.
- Roman English, English and Hindi labels were updated for 4-digit PIN instructions and temporary PIN verification. Existing Notes and Note Lock code was not changed.
- Pre-edit backup branch: `backup/note-style-section-lock-2026-11-13`. Exact pre-edit backups were fetched back and compared:
  - `backups/web-source-before-note-style-section-lock-2026-11-13.html` — blob `9ff42b600813d36073b813ff8a5554a70f67771d`
  - `backups/diary-web-before-note-style-section-lock-2026-11-13.html` — same blob
  - `backups/latest-before-note-style-section-lock-2026-11-13.json` — blob `7a0b4394d314b5e46450bde8cd366fd5c1fa8ae3`
  - `backups/register-before-note-style-section-lock-2026-11-13.md` — blob `a1d7cda1780cc79dc264ec75660743d08cbd10a0`
- Source changes were reviewed. Both inline JavaScript blocks passed syntax parsing. Static checks confirmed the Note-style four-digit setup/dialog, generated temporary PIN and copy flow, verification before changing/removing locks, legacy 5–8 digit PIN migration, all three language dictionaries, and unchanged section PIN storage key family.
- Final source commit: `9e9fd3ce3ea4c6fd04762e802318cd7189fe5f59`. Final source and mirror are byte-identical; both Git blob SHA `5d13b32a95121f0933a28042df334c1416f69f5f`. Independently calculated UTF-8 SHA-256 `ad920b3597dc3f57ff06eeb8dfcbf2615807928d8417797b0f92275778a14ce5` matches live `latest.json.webSha256`. Live webVersion: **191**.
- Publisher workflow run `43464715352` completed with **success**; publish job `132020633376` and all steps completed successfully.
- APK unchanged: 1.0.136 / versionCode 135 / SHA-256 `6fc74ca82888fed4121cc352c1846ec8c6a7063e2d2a33fbe032726f7a244348`. No APK rebuild or signing changes.
- Physical-device testing is pending. Test each section independently: unlock with the old PIN; if it was 5–8 digits, complete the one-time migration to a 4-digit PIN; test a normal unlock; use Forgot PIN, copy and re-enter the temporary PIN, then set a new PIN; test Change PIN and Remove Lock; confirm records and attachments remain. Do not claim phone-side testing until user confirms.
- Rollback: restore the verified pre-edit `web-source/index.html` from the backup branch, republish, and re-check source/mirror/feed/hash. Preserve all user data.


---

# Web Update 192 — Require explicit recovery PIN verification for all three Me locks (2026-11-13)

- User reported that after tapping **Forgot PIN**, a new PIN could be created without entering the temporary recovery PIN. User confirmed this affected all three protected sections: **My Kharcha**, **My Documents**, and **My Memories**.
- Starting live state: Web Update 191; APK 1.0.136 / versionCode 135; source/mirror blob `5d13b32a95121f0933a28042df334c1416f69f5f`; feed blob `ce97d78d4310c042d11f6958ba8f40e4554bc2d4`.
- Scope: changed only `web-source/index.html`; publisher mirrored it to `diary-web/index.html` and advanced the live web feed to Update 192. No APK, Android source, Note Lock, Diary Lock, protected records, attachments, or other features were intentionally changed.
- Recovery flow hardening applied to the shared Me-section lock handler used by all three sections:
  - Copying the displayed temporary PIN no longer closes the popup or advances the flow.
  - A separate **Unlock / Continue** button is required to open the recovery-PIN entry dialog.
  - Recovery-PIN entry no longer auto-submits after four digits. The user must explicitly tap **Unlock** (or press Enter) in that dialog.
  - Only an exact match with the temporary PIN reaches `meFeatureAskNewPin`. A wrong PIN returns to verification; closing the dialog cancels recovery. Thus copying, closing, or entering an incorrect value cannot reach new-PIN creation.
  - The existing new-PIN creation and confirmation, four-digit PIN storage, and section data are unchanged.
- Pre-edit backup branch: `backup/section-recovery-verify-fix-2026-11-13`. Verified pre-edit source and mirror backups both have blob `5d13b32a95121f0933a28042df334c1416f69f5f`. Additional exact backup files: `backups/latest-before-section-recovery-verify-fix-2026-11-13.json` and `backups/register-before-section-recovery-verify-fix-2026-11-13.md`.
- Source commit: `94798828f4c9c7f009842035cba5761a20c28da1`. Publisher commit: `4c7138c81d557def46cdf1dee087f28caa70fcde` (Publish My Diary web bundle update). Publisher diff confirms the source changes were mirrored and the feed was advanced.
- Final live source and mirror are byte-identical; both Git blob SHA `7bf375b9d2345509f2b2f9307b05961cd84fae70`. Live `latest.json.webVersion`: **192**; `webSha256`: `a881d44a7ae85c7adb55374cd30b0cb1d29eeba0dfe2db46f25623e9569cb811`. Feed and published mirror were fetched after publishing.
- APK unchanged: 1.0.136 / versionCode 135 / SHA-256 `6fc74ca82888fed4121cc352c1846ec8c6a7063e2d2a33fbe032726f7a244348`; no APK rebuild or signing changes.
- Physical-device verification is pending. User should install web update 192 through **Me → Check for Updates**, then test Forgot PIN independently in all three sections: copy the temporary PIN, verify that copy alone does not advance, tap Unlock, enter a wrong PIN and confirm no new-PIN screen appears, then enter the correct temporary PIN and confirm only then that new PIN setup opens. Also confirm existing records and attachments remain. Do not claim phone-side testing until the user confirms.
- Rollback: restore the verified pre-edit `web-source/index.html` from the backup branch, republish, and re-check source/mirror/feed. Preserve all user data.


---

# Web Update 193 — Match Me-section recovery PIN steps to Note Lock (2026-11-13)

- User confirmed the exact recovery behavior to align: after copying the temporary PIN, the popup should advance directly to PIN entry; entering four digits should automatically verify; a wrong PIN should show the Note Lock-style error popup and allow retry; only the correct temporary PIN may proceed to new PIN setup and confirmation.
- Starting live state: Web Update 192; APK 1.0.136 / versionCode 135; source/mirror blob `7bf375b9d2345509f2b2f9307b05961cd84fae70`; starting web SHA-256 `a881d44a7ae85c7adb55374cd30b0cb1d29eeba0dfe2db46f25623e9569cb811`.
- Scope: changed only the Me-section PIN recovery UI/flow in `web-source/index.html`. The shared handler covers My Kharcha, My Documents and My Memories. Existing PIN setup, PIN confirmation, current-PIN verification for Change/Remove, PBKDF2 PIN storage, section data and attachments remain unchanged. Note Lock and Diary Lock were not edited.
- Recovery flow now follows Note Lock's sequence:
  - The temporary-PIN popup has a Copy button only; successful copy closes it and opens the recovery PIN entry dialog.
  - The recovery dialog auto-verifies as soon as four numeric digits are entered (Enter also works); there is no extra Unlock/Continue button.
  - A wrong recovery PIN shows the same purple Note Lock-style error popup; closing that popup retries recovery PIN entry.
  - A correct recovery PIN alone opens the existing new-PIN setup and confirmation flow. Closing recovery entry cancels without creating a new PIN.
  - Clipboard failure leaves the temporary-PIN popup open and shows the localized failure label.
- Pre-edit backup branch: `backup/me-lock-note-recovery-flow-2026-11-13`. Verified exact backups:
  - `backups/web-source-before-me-lock-note-recovery-flow-2026-11-13.html` — blob `7bf375b9d2345509f2b2f9307b05961cd84fae70`
  - `backups/diary-web-before-me-lock-note-recovery-flow-2026-11-13.html` — same blob
  - `backups/latest-before-me-lock-note-recovery-flow-2026-11-13.json` — blob `1cbbbe0045c654c3e3fec06f0449caaa421fb21c`
  - `backups/register-before-me-lock-note-recovery-flow-2026-11-13.md` — blob `b6571b82044ad07e8093873d87839f6f9fe6461e`
- Source commit: `d6c5d64a39c1be9371311ca3073f79fa1accceae`. Diff review shows only `web-source/index.html` changed (11 additions, 5 deletions). Both inline JavaScript blocks passed syntax parsing. Static checks confirmed successful-copy advance, automatic four-digit recovery verification, wrong-PIN retry popup, and shared application to all three protected sections.
- Publisher workflow run `43469878386` completed successfully, including the web-only publish step. Publisher/main commit: `1a6c34f83e052c9fc969e0618c7f62cc4661c644`. Published source and mirror are byte-identical; both blob SHA `6bbbb9d59cd4796673a4b7c0337809dfd13a9e02`. Live `latest.json.webVersion`: **193**; `webSha256`: `7a10ed398939bdc688e66e4be5a7afc789e97ce0b4658ac8eac7c952a1b56246`.
- APK unchanged: 1.0.136 / versionCode 135 / SHA-256 `6fc74ca82888fed4121cc352c1846ec8c6a7063e2d2a33fbe032726f7a244348`; no APK rebuild, Android source change or signing change.
- Physical-device verification is pending. Install web update 193 through **Me → Check for Updates** and test Forgot PIN separately in all three sections: copy temporary PIN, confirm recovery entry opens; enter a wrong four-digit PIN and confirm the error popup then retry; enter the correct temporary PIN and confirm only then that new PIN setup and confirmation open. Also verify Change PIN, Remove Lock and saved records/attachments remain intact. Do not claim phone-side testing until user confirms.
- Rollback: restore `web-source/index.html` from the verified pre-edit backup branch, republish, and re-check source/mirror/feed. Preserve all user data.


---

# Web Update 195 + APK 1.0.137 — Smart Follow-up Reminder (2026-11-13)

- User requested the Smart Follow-up Reminder idea. Added a fifth independent ⏰ Smart Reminder tool under Me.
- Starting live state: APK 1.0.136 / versionCode 135, Web Update 193, source/mirror blob 6bbbb9d59cd4796673a4b7c0337809dfd13a9e02, web SHA-256 7a10ed398939bdc688e66e4be5a7afc789e97ce0b4658ac8eac7c952a1b56246.
- Web behavior:
  - Create a reminder with title, date, time and optional details.
  - Optionally link it to an existing Note; choosing a linked Note fills an empty reminder title.
  - Reject past date/time values.
  - List, Smart Search (including time), edit and delete reminders. Editing reschedules the same reminder ID; deleting cancels its native alarm.
  - Notifications provide 10-minute Snooze and Done actions.
  - Reminder form labels, validation messages and permission prompts are translated for Roman, English, Hindi, Urdu, Arabic, Bengali, Gujarati, Marathi, Tamil and Telugu. Android notification action labels currently display “10 min baad” and “Done”.
  - A browser-only HTML session without the native Android bridge does not claim to schedule alerts; it asks the user to use the latest installed My Diary app.
- Android scheduling:
  - Added native JavaScript bridge methods to schedule/cancel reminders and check/request notification and exact-alarm permissions.
  - Uses Android AlarmManager with exact alarms where the user grants Alarms & reminders special access; Android 13+ also requires Notifications permission.
  - Pending reminders are stored in app-private SharedPreferences and restored after device reboot or app package replacement through dedicated receivers.
  - If exact-alarm access is not available, native scheduling has an inexact fallback, but the UI requests exact-alarm access before saving for the intended punctual behavior.
  - Notification title/details may be visible on the phone lock screen. Reminder records are local to the device; no cloud upload or sync was added.
- Storage and preservation:
  - Reminder records reuse the existing diary_me_features_v1 IndexedDB database and records object store; no database version/schema migration.
  - Existing Notes database/storage, Note Lock, Diary Lock, PIN/recovery data, old Notes, photos, attachments, existing Calendar, My Kharcha, My Documents and My Memories were not intentionally changed.
  - The Me-feature IndexedDB data is not encrypted by the existing section PIN; do not assume the reminder content is encrypted at rest.
- Files changed for this feature:
  - web-source/index.html — Smart Reminder UI, translations, form validation, link-to-Note, search/edit/delete and native bridge calls.
  - scripts/add_diary_app_actions.py — Android bridge, AlarmManager scheduler, notification actions, notification/boot permissions and receivers.
  - scripts/add_online_diary_updates.py — keep the existing DiaryBundlePathHandler inside MainActivity when top-level reminder receiver classes are appended.
  - .github/workflows/build-diary-from-zip.yml — next signed APK version advanced to 1.0.137 / versionCode 136; release guard, APK URL/name and release notes updated.
  - Publisher workflows generated diary-web/index.html, latest.json, My-Diary.apk and My-Diary-1.0.137.apk.
- Verified pre-edit backup branch: backup/pre-smart-follow-up-reminder-2026-11-13. All six backups were re-fetched and byte-identically verified:
  - backups/web-source-before-smart-follow-up-reminder-2026-11-13.html — original blob 6bbbb9d59cd4796673a4b7c0337809dfd13a9e02
  - backups/diary-web-before-smart-follow-up-reminder-2026-11-13.html — same original blob
  - backups/latest-before-smart-follow-up-reminder-2026-11-13.json — blob d52cc10a33aa118efc84f9b65977103e875c7177
  - backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-smart-follow-up-reminder-2026-11-13.md — blob 0c231f8a6161f18e0791fb8036fb081444079f3b
  - backups/add_diary_app_actions-before-smart-follow-up-reminder-2026-11-13.py — blob 067a6cdaf5ac53cdd497894f8a6436f5cbe7a447
  - backups/build-diary-from-zip-before-smart-follow-up-reminder-2026-11-13.yml — blob f6467078153e112b4b56e5d515c67a0b47d0a3be
- Source and integration commits:
  - Smart Reminder UI: 518a52f61b0314a288d000223009f969775cc760
  - Native reminder scheduler/bridge: 620730aba25a9105556a843a41b01dcd4f14ca8a
  - Exact-alarm permission methods: 5c1a25cc24a73b9dafff1913e69524859d806403
  - Boot receiver manifest correction: 3bd7e6d91368789718714169b4e1b9a67e678505
  - Duplicate-import correction: 9875e15d31c1f556602632d052d02c540c4a687c
  - Existing online updater insertion-point correction: d709eabeae544992025c4d7053007cd06b12254b
  - APK workflow version bump: c4ef435b7767bdd7a4e9048ea41b854ff182cf60
  - Exact-alarm UI prompt: 29265136fe01efe1515533a52d70e28b7a5581be
- Web publishing:
  - Web Update 194 publisher run 43473902236 completed successfully.
  - Web Update 195 publisher run 43474487869 completed successfully; publisher commit 2d94faf8b887f5b867fa980b96b3fbd64cb8792e.
  - Final web-source/index.html and diary-web/index.html are byte-identical; both Git blob SHA a45b5803031a6e521e696c3169632e84a515c92d.
  - Independently computed SHA-256 of the exact final UTF-8 source: b0c386146062439091df8c47645202d90678b548f7b7127a40933b976891ebdc. The implementation was checked against the standard SHA-256 abc test vector; the digest matches live latest.json webSha256.
- APK publishing:
  - Build/publish workflow run 43474419797 completed successfully.
  - Debug and signed Release APK builds passed; Android Kotlin compilation passed; JavaScript module node --check passed; Android identity, FileProvider and translation audit checks passed.
  - The existing signing certificate fingerprint was verified unchanged: 23A4E93F3C7911DCE18389EA583548700C6AD6A3759707F1CD222D07E2408B5A.
  - Publisher commit: 628375728d79e88e7d0aa1baf1e1713f8e1db15b.
  - Live latest.json: APK 1.0.137 / versionCode 136; URL https://raw.githubusercontent.com/amuazzinxyz-ops/My-Diary-Updates/main/My-Diary-1.0.137.apk; APK SHA-256 38439e536479d7adea7c50031b59873d8a898b0c103f845018cfa8b8e8b805bf; webVersion 195; web SHA-256 b0c386146062439091df8c47645202d90678b548f7b7127a40933b976891ebdc.
  - The APK build used the immediately previous web bundle (Web Update 194); the live feed is Web Update 195. After installing APK 1.0.137, run Me → Check for Updates again if needed so the native updater applies web bundle 195.
  - Two intermediate build attempts failed during integration (duplicate Android imports and the online updater class insertion point); these were corrected. The final build run above completed successfully. No failed/intermediate APK was published.
- Physical-device verification is pending. User should update to APK 1.0.137, then use Me → Check for Updates again to apply Web Update 195 if it is still offered. In Me → Smart Reminder, create a test reminder 2–3 minutes ahead, allow Android Notifications and Alarms & reminders permissions, return to the form and tap Save again. Confirm the notification arrives with screen off/app closed, then test Snooze and Done. Also test after a device restart. Do not claim device-side testing until the user confirms.
- Rollback: restore the exact web source, native integration scripts, build workflow and feed from backup/pre-smart-follow-up-reminder-2026-11-13. For any APK rollback after installation, preserve package identity/signing and publish a newer versionCode; never ask the user to uninstall or clear app data. Preserve all notes, photos, attachments, PIN/recovery data and user records.


---

# Web Update 196 — Keep the Me menu open after returning from a Me feature (2026-11-13)

- User request: when opening any of the five Me features — Personal Calendar, Smart Reminder, My Kharcha, My Documents or My Memories — and then pressing **Back**, return to the five-option Me menu without closing/collapsing the Me button.
- Starting live state: APK 1.0.137 / versionCode 136; Web Update 195; package `com.personal.diaryapp`. Starting source/mirror blob SHA `a45b5803031a6e521e696c3169632e84a515c92d`; starting feed blob `f25723a6d43952a4cea54de2b2d2189ff1bbb28d`; starting register blob `8f20ca672817a86112dac6ebe176f33f8b5d2a3a`. The immediately preceding main commit was `1eeedad3ad0e30059698e8e7bea0fcc47236393d` (register-only clarification).
- Root cause: the Me feature modal's click event bubbled to the Diary overlay's outside-click handler. The Back/Close handler first reopened `mePanel`, then the same click bubbled to the overlay, which treated the click as outside the Me menu and hid it again.
- Scope: web-only; changed exactly one event-handler line in `web-source/index.html`. The modal click handler now calls `e.stopPropagation()` before handling a backdrop click. This keeps Back/Close clicks from reaching the overlay outside-click handler; the existing backdrop-close behavior is retained. The five feature buttons, feature pages, PIN gates, records, attachments, database/storage keys, translations, native Android source, APK, package identity and signing data were not changed.
- Pre-edit backup branch: `backup/me-feature-back-retain-menu-2026-11-13`. Exact readable backups were fetched back and compared byte-for-byte:
  - `backups/web-source-before-me-feature-back-retain-menu-2026-11-13.html` — original blob `a45b5803031a6e521e696c3169632e84a515c92d`
  - `backups/latest-before-me-feature-back-retain-menu-2026-11-13.json` — original blob `f25723a6d43952a4cea54de2b2d2189ff1bbb28d`
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-me-feature-back-retain-menu-2026-11-13.md` — original blob `8f20ca672817a86112dac6ebe176f33f8b5d2a3a`
- Source commit: `ec2065157ac25cefb8a15d70232192c09afb4ae1`. Commit diff was reviewed and contains only the single requested event-handler change. Publisher commit: `37eb3c42df30c112c16d04bc2a0fc456d77ed2f9` (“Publish My Diary web bundle update”).
- Published verification: `web-source/index.html` and `diary-web/index.html` were re-fetched and are byte-identical; both blob SHA `fd585bed757ddb961098b3a8f9c7059d59543622`. Independently computed SHA-256 of the exact UTF-8 source bytes: `f55cb80a22ad6237d108d07c246a2ba9b0d03c33e3603f4f38e7cdcdd52eb43b`, matching live `latest.json.webSha256`. Live `webVersion=196`.
- APK unchanged: `1.0.137` / versionCode `136`; APK SHA-256 remains `38439e536479d7adea7c50031b59873d8a898b0c103f845018cfa8b8e8b805bf`. No APK rebuild, native source change, or signing operation. Publisher workflow run ID/conclusion was not exposed by the available workflow-run lookup in this session; the publisher bot commit and live source/mirror/feed were verified.
- Physical-device verification is **pending**. User should open **Me → Smart Reminder** (and preferably each of the other four features), tap **Back**, and confirm the five-option Me menu remains visible. Also test the feature Close (×) button and backdrop close; confirm tapping the Me button itself still opens/closes the menu normally. Do not claim phone-side success until the user confirms.
- Rollback: restore the exact pre-edit `web-source/index.html` from `backup/me-feature-back-retain-menu-2026-11-13`, republish, and re-check source/mirror/feed/hash. Preserve all user records and app data.


---

# Web Update 197 — Hide the redundant Lock button in My Kharcha (2026-11-13)

- User request: after opening **💰 My Kharcha**, remove the visible `🔒 Lock` header button. This is a UI-only removal; keep My Kharcha's section PIN protection and lock/recovery system unchanged.
- Starting live state: APK 1.0.137 / versionCode 136; Web Update 196; package `com.personal.diaryapp`. Starting source/mirror blob `fd585bed757ddb961098b3a8f9c7059d59543622`; feed blob `f4e3717e47aa72a426cad0bd844374083ba24063d`; register blob `e1e94bd23661b650099fd06c02485d89e6a242f7`.
- Scope: changed exactly one line in `web-source/index.html`. The header `🔒 Lock` button is now hidden for `kharcha`; it remains governed as before for Documents and Memories. Existing `meFeatureProtected(kind)` still includes `kharcha`, `documents` and `memories`; the PIN gate, PIN/recovery storage keys, dialogs, records and other features were not changed. No APK/native source, data schema or translations changed.
- Pre-edit backup branch: `backup/remove-kharcha-header-lock-button-2026-11-13`. Three backups were re-fetched; the HTML backup blob `fd585bed757ddb961098b3a8f9c7059d59543622` matches the exact pre-edit source.
- Source commit: `deb0d2b582e22a800d547300e99f1589c6d29b43`. Reviewed diff contains only the one requested visibility change. Publisher commit: `c6f52a0f548621af8a1dc2dd0461e8ebe0bd7584` (“Publish My Diary web bundle update”).
- Published verification: `web-source/index.html` and `diary-web/index.html` are byte-identical; blob SHA `58db1f74729e21bff7139b068aad202fe58b537d`. Independently computed SHA-256 of exact UTF-8 source: `4452235be464d6acb8622430f71e4f0a76b416579e41ad91207d52a4d256852e`, matching live `latest.json.webSha256`. Live `webVersion=197`.
- APK unchanged: 1.0.137 / versionCode 136; APK SHA-256 `38439e536479d7adea7c50031b59873d8a898b0c103f845018cfa8b8e8b805bf`. No APK rebuild or signing change.
- Physical-device verification is pending. User should apply **Me → Check for Updates** and open My Kharcha: confirm the header `🔒 Lock` button is absent, while the section PIN still prompts on entry and the records, add/edit/delete, PDF report and other tools still work. Also confirm Documents and Memories are unchanged. Do not claim phone-side testing until user confirms.
- Rollback: restore exact pre-edit `web-source/index.html` from `backup/remove-kharcha-header-lock-button-2026-11-13`, republish, and verify source/mirror/feed/hash. Preserve all local records and PIN/recovery data.


---

# APK 1.0.138 — Keep Smart Reminder alarms exact while screen is off (2026-11-14)

- User reported that Smart Reminder notifications and ringtone arrive while the phone screen is ON, but neither arrives while the screen is OFF. User confirmed they are using the installed APK.
- Live starting state: My Diary APK 1.0.137 / versionCode 136; Web Update 197; package `com.personal.diaryapp`. Starting native integration script blob `d8d18d417d266819248a38119d99ab892f39dece`; build workflow blob `a5fe450702a58e33acd5e4b9242062da18c945e0`; feed blob `07c94c3a2760c52ec2e423e483800ba115a02027`; web source blob `58db1f74729e21bff7139b068aad202fe58b537d`.
- Root cause identified in the Android alarm scheduler: if `setExactAndAllowWhileIdle` threw `SecurityException`, the code silently fell back to `setAndAllowWhileIdle`. That is an inexact alarm and Android Doze can defer it while the screen is off. This fallback could therefore produce the exact symptom reported. The UI already checks exact-alarm permission, but the native bridge did not independently enforce it.
- Scope: native scheduling reliability only. The bridge now rechecks exact-alarm permission immediately before scheduling and opens the exact-alarm permission settings if access is missing. The scheduler verifies `canScheduleExactAlarms()` on Android 12+ and refuses to claim success without access. The inexact fallback has been removed; Android 6+ uses `RTC_WAKEUP` + `setExactAndAllowWhileIdle`, and older Android uses `setExact`.
- No reminder record schema, IndexedDB storage, reminder UI/translations, web HTML, Notes, photos, attachments, Calendar, Kharcha, Documents, Memories, PIN/recovery data, package identity, or user data was intentionally changed. The web bundle remains Web Update 197.
- Pre-edit backup branch: `backup/reminder-screen-off-exact-alarm-2026-11-14`. Five backup files were fetched back and verified byte-identical to the live pre-edit files:
  - `backups/add_diary_app_actions-before-reminder-screen-off-exact-alarm-2026-11-14.py` — original blob `d8d18d417d266819248a38119d99ab892f39dece`
  - `backups/build-diary-from-zip-before-reminder-screen-off-exact-alarm-2026-11-14.yml` — original blob `a5fe450702a58e33acd5e4b9242062da18c945e0`
  - `backups/web-source-before-reminder-screen-off-exact-alarm-2026-11-14.html` — original blob `58db1f74729e21bff7139b068aad202fe58b537d`
  - `backups/latest-before-reminder-screen-off-exact-alarm-2026-11-14.json` — original blob `07c94c3a2760c52ec2e423e483800ba115a02027`
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-reminder-screen-off-exact-alarm-2026-11-14.md` — original blob `4dd82a996744a990502e7952ee14ad21e97a86d5`
- Reviewed native diff: removed the catch-and-downgrade to `setAndAllowWhileIdle`; added native exact-alarm permission recheck before calling the scheduler. Confirmed the final native script contains no `setAndAllowWhileIdle` fallback and retains one `setExactAndAllowWhileIdle` call.
- Source PR: [#1](https://github.com/amuazzinxyz-ops/My-Diary-Updates/pull/1), merged successfully as commit `b30e39f09a06c7404141e37370e81b6d22467b78` (squash merge). Build workflow run `43594988709` completed with conclusion `success`: debug build, Kotlin compilation, signed Release build, package checks, signature checks and APK publication passed. The existing signing certificate fingerprint was verified unchanged: `23A4E93F3C7911DCE18389EA583548700C6AD6A3759707F1CD222D07E2408B5A`.
- Published APK: `1.0.138` / versionCode `137`; live `latest.json` blob `425f295230b22b6814335d61d9c0b01feb8f138c`; APK SHA-256 `59b95893e6e412a1ed44a6f3880fd486ea3b6cf70ee484ceef4102ed7bef4b38`; APK file and versioned APK are byte-identical (same Git blob `d3597926cd910e7ae0ba96fb0ba1bcb5dd1230e5`). WebVersion remains `197` and web SHA-256 remains `4452235be464d6acb8622430f71e4f0a76b416579e41ad91207d52a4d256852e`.
- Physical-device verification is pending; do not claim the phone-side screen-off symptom is fixed until the user confirms. After installing APK 1.0.138 via **Me → Check for Updates**, create a short test reminder, lock the screen and verify both notification and ringtone arrive at the scheduled time. Also test with the app closed and after device restart. If exact-alarm access is missing, the app must request it rather than silently schedule an inexact alarm. If the alarm still does not fire despite exact access, investigate the device manufacturer's background/autostart restrictions separately.
- Rollback: restore the native integration script and build workflow from the verified backup branch above, then publish a newer versionCode while preserving app identity/signing. Do not uninstall the app, clear app data, or delete reminders/notes/photos/PIN data.


---

# APK 1.0.139 — Use Android AlarmClock events for Smart Reminder screen-off delivery (2026-11-14)

- User tested APK 1.0.138 and confirmed that both reminder notification and ringtone still arrived only while the screen was ON; neither arrived while the screen was OFF. User also confirmed all relevant phone/app settings were already ON. Do not send the user through the same settings checklist again.
- Live starting state: APK 1.0.138 / versionCode 137; Web Update 197; package `com.personal.diaryapp`. Starting native integration script blob `76e6f18d94507b4df4c29c7dda1c0ed238043266`; workflow blob `4a29b4c8e435fdbfd39b9c5cd0b1d584deb09dec`; feed blob `425f295230b22b6814335d61d9c0b01feb8f138c`; register blob `c0eeff18ee2b27d49e218d96c530c01b1f72c4d1`.
- Additional source inspection: the original Android project manifest contained no reminder-specific permission or receiver declarations. The native integration script adds `POST_NOTIFICATIONS`, `RECEIVE_BOOT_COMPLETED`, `SCHEDULE_EXACT_ALARM`, `.DiaryReminderReceiver`, and `.DiaryReminderBootReceiver` with BOOT_COMPLETED and MY_PACKAGE_REPLACED actions. The previous build had no fail-closed assertion that these generated declarations were actually present.
- Scope: native reminder delivery only. Replaced ordinary `setExactAndAllowWhileIdle(RTC_WAKEUP,...)` scheduling with `AlarmManager.setAlarmClock(AlarmClockInfo(atMillis, showPending), pending)`. This registers each reminder with Android as an alarm-clock event, supplies the app launch PendingIntent as the system's alarm-show action, and uses the system wake-up alarm path. The notification is also categorized as `Notification.CATEGORY_ALARM`. Existing exact-alarm permission checks, reminder storage, cancellation, snooze, boot/package-replacement restoration, and notification actions remain in place.
- Build workflow now fails closed unless the generated manifest parses and contains notification/exact-alarm/boot permissions, both reminder receivers, and boot/update restoration actions; it also checks the generated Kotlin source uses AlarmClock scheduling and has no old inexact/ordinary exact scheduler fallback.
- Preservation: no web HTML, reminder record schema, notes, photos, attachments, Calendar, Kharcha, Documents, Memories, PIN/recovery data, app package identity, signing configuration, or user data intentionally changed. Web bundle remains Web Update 197. No user data clearing or app uninstall is required.
- Pre-edit backup branch: `backup/reminder-screen-off-alarmclock-2026-11-14`. Backup files were committed and their blobs match the exact pre-edit live files:
  - `backups/add_diary_app_actions-before-reminder-alarmclock-2026-11-14.py` — original blob `76e6f18d94507b4df4c29c7dda1c0ed238043266`
  - `backups/build-diary-from-zip-before-reminder-alarmclock-2026-11-14.yml` — original blob `4a29b4c8e435fdbfd39b9c5cd0b1d584deb09dec`
  - `backups/latest-before-reminder-alarmclock-2026-11-14.json` — original blob `425f295230b22b6814335d61d9c0b01feb8f138c`
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-reminder-alarmclock-2026-11-14.md` — original blob `c0eeff18ee2b27d49e218d96c530c01b1f72c4d1`
- Source PR: [#2](https://github.com/amuazzinxyz-ops/My-Diary-Updates/pull/2), squash-merged as commit `93c0e89d3194c8c61385cc794310e9e33e5277cf`. Build workflow run [43597330789](https://github.com/amuazzinxyz-ops/My-Diary-Updates/actions/runs/43597330789) completed successfully. The manifest/receiver/permission audit passed; debug Kotlin/Android build passed; signed Release APK build and publication passed. The release signer SHA-256 fingerprint was verified unchanged: `23A4E93F3C7911DCE18389EA583548700C6AD6A3759707F1CD222D07E2408B5A`.
- Published APK: `1.0.139` / versionCode `138`; live feed blob `c794626b4ed9e71b657641895dc0f116bd42c296`; APK SHA-256 `04588ba0971f5d68817e3133ae88b0370b1c4ffe8c2b47c9063d656c575b6004`. The signed Release APK artifact was downloaded and independently hashed; its SHA-256 matches the live feed. `My-Diary.apk` and `My-Diary-1.0.139.apk` have the same Git blob `f10ad2b40e330fa7a7ad881de08e77fc3c08b5f2`. Web source and mirror remain byte-identical at blob `58db1f74729e21bff7139b068aad202fe58b537d`; WebVersion remains `197`, web SHA-256 remains `4452235be464d6acb8622430f71e4f0a76b416579e41ad91207d52a4d256852e`.
- Physical-device verification is pending. User must install/update to APK 1.0.139, create a test Smart Reminder a few minutes ahead, lock the screen, and confirm both notification and ringtone arrive with the screen OFF. Also test with My Diary closed and after device restart. The assistant has not tested the user's Vivo device and must not claim this symptom is fixed until user confirms. Android may show its normal next-alarm indicator because reminders are now registered as alarm-clock events.
- Rollback: restore the native integration script and workflow from the verified backup branch above, then publish a newer versionCode while preserving package identity/signing. Never uninstall the app, clear app data, or delete reminders, notes, photos, attachments, PIN/recovery data, or user records.


---

# APK 1.0.140 — Wake the screen for Smart Reminders (2026-11-14)

- User clarified after APK 1.0.139 that, with the phone screen OFF, reminder notification and ringtone now arrive, but the display does not turn ON. User asked to fix only screen wake; notification timing, ringtone, reminder content and all other Diary features must remain unchanged.
- Live starting state: APK 1.0.139 / versionCode 138; Web Update 197; package `com.personal.diaryapp`. Starting native integration script blob `c9a2794e46a2915dd3d041f1de88966e9a39951a`; build workflow blob `d71558b4fdc6eb35c252ff1c6c9eb5ae332958a6`; feed blob `c794626b4ed9e71b657641895dc0f116bd42c296`; register blob `3bd4845a4189a64fbe6f95df3874a017117fbe7e`.
- Root cause: the existing alarm notification was categorized as an alarm and used AlarmManager.setAlarmClock, but it did not set a notification full-screen intent. Android therefore delivered the notification and ringtone without being asked to launch an activity and wake the display.
- Scope: native Smart Reminder screen wake only. The generated MainActivity now calls setShowWhenLocked(true) and setTurnScreenOn(true) when launched with a reminder ID; older Android versions use the corresponding window flags. The alarm notification now sets the existing reminder content PendingIntent as its full-screen intent. On Android 14+, the native bridge checks NotificationManager.canUseFullScreenIntent(); if access is missing, it opens Android's special full-screen-intent access settings and does not report the reminder as successfully scheduled until access is granted and the reminder is saved again. Added `android.permission.USE_FULL_SCREEN_INTENT` to the generated manifest.
- Build workflow now fails closed unless the generated manifest includes USE_FULL_SCREEN_INTENT and the generated Kotlin includes the full-screen notification intent, lock-screen wake calls, and Android 14+ permission check/request.
- Preservation: no web HTML, reminder record schema, IndexedDB storage, ringtone, notification channel, reminder labels/translations, notes, photos, attachments, Calendar, Kharcha, Documents, Memories, PIN/recovery data, package identity, signing configuration, or user data was intentionally changed. Existing AlarmClock scheduling, exact-alarm permission, notification actions, snooze, cancellation, and boot/package-replacement restoration remain in place.
- Pre-edit backup branch: `backup/reminder-screen-wake-fullscreen-2026-11-14`. The exact pre-edit files were fetched back and verified byte-identical:
  - `backups/add_diary_app_actions-before-reminder-screen-wake-fullscreen-2026-11-14.py` — original blob `c9a2794e46a2915dd3d041f1de88966e9a39951a`
  - `backups/build-diary-from-zip-before-reminder-screen-wake-fullscreen-2026-11-14.yml` — original blob `d71558b4fdc6eb35c252ff1c6c9eb5ae332958a6`
  - `backups/latest-before-reminder-screen-wake-fullscreen-2026-11-14.json` — original blob `c794626b4ed9e71b657641895dc0f116bd42c296`
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-reminder-screen-wake-fullscreen-2026-11-14.md` — original blob `3bd4845a4189a64fbe6f95df3874a017117fbe7e`
- Source PR [#3](https://github.com/amuazzinxyz-ops/My-Diary-Updates/pull/3) was squash-merged as commit `4a00783bb539720ade7e980febc3cb1b67e17a6e`. Build workflow run [43598484763](https://github.com/amuazzinxyz-ops/My-Diary-Updates/actions/runs/43598484763) completed with conclusion `success`. The generated manifest/Kotlin checks passed; debug and signed Release APK builds passed; APK publication and artifact uploads passed. The existing signing certificate fingerprint was independently checked and remains `23A4E93F3C7911DCE18389EA583548700C6AD6A3759707F1CD222D07E2408B5A`.
- Published APK: `1.0.140` / versionCode `139`; live feed blob `be9086e97cecde0f4f7c4d2e6152c6350cf540da`; APK SHA-256 `2936ddae0c7b8672bbfcccf1dccf344f4bc5aa4a21f6fc0fd1214a5cb559c588`. The signed APK was downloaded from the workflow artifact and independently hashed; it matches live latest.json. `My-Diary.apk` and `My-Diary-1.0.140.apk` have identical Git blob `f0385aec830257526527da69e63da421271a4ad8`. Web source and mirror remain byte-identical at blob `58db1f74729e21bff7139b068aad202fe58b537d`; WebVersion remains `197`, web SHA-256 remains `4452235be464d6acb8622430f71e4f0a76b416579e41ad91207d52a4d256852e`.
- Physical-device verification is **pending**. User should install via **Me → Check for Updates**, then create/save a short test reminder. If Android opens the full-screen-intent special access page, enable My Diary's full-screen notifications/alarm access, return to My Diary, and save the reminder again. Lock the phone before the reminder time and confirm that the display turns ON while notification and ringtone still arrive. Do not claim screen wake is fixed until the user confirms on their Vivo phone.
- Rollback: use the verified backup branch above; if needed, restore only the native integration script and workflow, then publish a higher versionCode while preserving package identity/signing. Never uninstall the app, clear app data, or delete reminders, notes, photos, attachments, PIN/recovery data, or user records.


# APK 1.0.141 — Keep Smart Reminder notification without auto-opening My Diary (2026-11-14)

- User confirmed the intended behavior: when the phone is locked/screen is off, the Smart Reminder notification and ringtone should still arrive, but My Diary must not open automatically and the phone should remain locked.
- Starting live state: APK 1.0.140 / versionCode 139; Web Update 197; package `com.personal.diaryapp`. Starting feed blob `be9086e97cecde0f4f7c4d2e6152c6350cf540da`; APK SHA-256 `2936ddae0c7b8672bbfcccf1dccf344f4bc5aa4a21f6fc0fd1214a5cb559c588`.
- Scope: native reminder presentation only. Removed the reminder notification's full-screen Activity intent, the reminder-only screen-wake flags in MainActivity, the Android 14+ full-screen-intent permission check/request, and `USE_FULL_SCREEN_INTENT`. Preserved `AlarmManager.setAlarmClock`, exact-alarm permission enforcement, regular notification content tap action, alarm category, notification defaults/sound, snooze/Done actions, reminder scheduling/cancellation, boot/package-replacement restoration, reminder storage and all user data.
- Changed only `scripts/add_diary_app_actions.py` and `.github/workflows/build-diary-from-zip.yml`. Web HTML and Web Update 197 are unchanged. The build workflow now fails closed if full-screen reminder launch or screen-wake code is reintroduced, and checks the normal notification tap action.
- Pre-edit backup branch: `backup/no-auto-open-reminder-2026-11-14`. Verified exact readable backups:
  - `backups/native-script-py-before-no-auto-open-reminder-2026-11-14` — original blob `c16f8927522ce55dfb5018f445f10c7970dc27ff`
  - `backups/build-workflow-yml-before-no-auto-open-reminder-2026-11-14` — original blob `ea4402a0f573b49fbe5f017f83b129eae40129ac`
  - `backups/latest-json-before-no-auto-open-reminder-2026-11-14` — original blob `be9086e97cecde0f4f7c4d2e6152c6350cf540da`
  - `backups/master-register-md-before-no-auto-open-reminder-2026-11-14` — original blob `bf067f5a7f76d3d11d3bbff900323424ecea366c`
- Source PR [#4](https://github.com/amuazzinxyz-ops/My-Diary-Updates/pull/4) was squash-merged as commit `80d5a5fd9b2b94049e7baaae965850798b6c9782`. Merged source script blob is `edca39d3a861eedf87dcabee84776261152ca93b`; workflow blob is `a8781272363673bb2155b44fa1634cbedb3d3280`. Re-fetched main-branch script contains no full-screen intent, screen-wake flags, or full-screen permission; AlarmClock scheduler and ordinary notification content intent remain present.
- Next APK target: `1.0.141` / versionCode `140`; build/publish verification is **pending**. At this register update, live `latest.json` still points to APK 1.0.140 / code 139, so do not install or describe 1.0.141 as published yet. Existing signing certificate must remain `23A4E93F3C7911DCE18389EA583548700C6AD6A3759707F1CD222D07E2408B5A`.
- Physical Vivo V2420 / Android 15 verification is **pending**. After a successful in-app update via **Me → Check for Updates**, create a short test reminder, lock the screen, and confirm notification + ringtone arrive while My Diary stays closed and the phone remains locked. Then test a reminder with the screen ON and confirm tapping its notification still opens the reminder normally. Never claim phone-side success until the user confirms.
- Rollback: use the verified pre-edit files on `backup/no-auto-open-reminder-2026-11-14`; if needed, restore only the native integration script and workflow and publish a higher versionCode. Never uninstall, clear app data, or remove reminders/notes/photos/PIN data.

---

# APK 1.0.141 — Correct reminder notification tap-action build guard (2026-11-14)

- Follow-up to the Smart Reminder no-auto-open repair. The first trigger run `43599842119` failed at the generated-Kotlin static assertion because the workflow expected the text `builder.setContentIntent(content)`, while the actual generated notification builder uses the chained call `.setContentIntent(content)`. This was a false-negative verification check; it did not indicate a runtime reminder-code failure.
- Changed only `.github/workflows/build-diary-from-zip.yml`: the guard now requires exactly one `.setContentIntent(content)` occurrence. No Android runtime source, web HTML, reminder storage, notes, photos, PIN/recovery data, package identity, or signing configuration was changed in this correction.
- Before-edit backups committed and readable in PR #5 branch:
  - `backups/build-workflow-before-reminder-tap-check-2026-11-14.yml`
  - `backups/latest-before-reminder-tap-check-2026-11-14.json`
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-reminder-tap-check-2026-11-14.md`
- PR [#5](https://github.com/amuazzinxyz-ops/My-Diary-Updates/pull/5) merged as commit `66adb151bc31167fa48dfa73fe604ffe137aed65`. Final workflow blob: `8f31523f90f9852e8aa4b3d64bcff07f3a463a41`. Reviewed PR diff: one workflow guard correction plus the three exact backups.
- Corrected build workflow run `43600109747` was started and passed project verification, published HTML/hash checks, translation audit, identity checks, release version guard, and generated-source guard. At the time of this entry the Android debug APK build is still **in progress**; signed release build, APK publication, live feed update, APK hash and signing fingerprint verification are **pending**. Do not call APK 1.0.141 published until every release check passes and `latest.json` points to the verified artifact.
- Live update feed at the start of this correction remains APK `1.0.140` / versionCode `139`, Web Update `197`; latest.json remains authoritative.
- Phone verification on Vivo V2420 / Android 15 is pending. After a verified release is available, use **Me → Check for Updates**, then test screen-off notification + ringtone with My Diary staying closed and phone locked; separately verify tapping the notification opens the reminder normally.
- Rollback for this workflow-only correction: restore the exact workflow from `backups/build-workflow-before-reminder-tap-check-2026-11-14.yml`; preserve all user data and the existing signing identity.

## Final publication verification — APK 1.0.141 (2026-11-14)

- Corrected workflow run `43600109747` completed with conclusion `success`; build job `132462842753` also completed successfully.
- All release-critical steps passed: project/source validation, published HTML/hash checks, translation audit, app identity validation, target version `1.0.141` / versionCode `140`, debug build, signed Release configuration, publish verification, signed APK upload, and APK upload.
- `latest.json` was re-fetched from `main` and now advertises APK `1.0.141`, versionCode `140`, URL `https://raw.githubusercontent.com/amuazzinxyz-ops/My-Diary-Updates/main/My-Diary-1.0.141.apk`, SHA-256 `aaaa7c49a76ed0fc0caef4f78b37cdf695ce22d5d2d0705d3ea275fecfaf959e`. Web Update remains `197` with unchanged SHA-256 `4452235be464d6acb8622430f71e4f0a76b416579e41ad91207d52a4d256852e`.
- GitHub Actions run contains the non-expired `My-Diary-signed-Release-APK` artifact (1,949,061 bytes), and `My-Diary-debug-APK` (2,617,001 bytes). Signed release upload and publish steps report success.
- The workflow's signing-readiness and keystore/alias validation steps passed. Preserve the established signing certificate fingerprint `23A4E93F3C7911DCE18389EA583548700C6AD6A3759707F1CD222D07E2408B5A`.
- The app update is now published. Remaining verification is physical-device behavior only: user must install via **Me → Check for Updates** on Vivo V2420 / Android 15 and confirm notification + ringtone arrive with screen off while My Diary remains closed and the phone locked; then tap the notification to confirm it opens normally. Do not claim device-side confirmation until the user reports it.
- User data remains untouched by this build; do not uninstall or clear app data.


---


## Final publication verification — APK 1.0.142 (2026-11-14)

- Corrected workflow run `43601017474` completed with conclusion **success**; build job `132465753714` completed successfully. Debug APK, signed Release APK, publish, artifact upload and APK upload steps passed. Translation audit artifact was also uploaded.
- Live `latest.json` re-fetched from `main`: APK `1.0.142`, versionCode `141`, package `com.personal.diaryapp`, URL `https://raw.githubusercontent.com/amuazzinxyz-ops/My-Diary-Updates/main/My-Diary-1.0.142.apk`, SHA-256 `9a538b5baa4a6ecf97158502e5b564473b158144c3bc324f41e1f8c83081a9d3`. Downloaded signed Release APK artifact independently hashed; exact SHA-256 matches live feed.
- Workflow signing verification reports v1/JAR and v2 APK signatures valid. Signer certificate SHA-256 matches the existing trusted fingerprint `23A4E93F3C7911DCE18389EA583548700C6AD6A3759707F1CD222D07E2408B5A`. Package/version identity checks passed in workflow. Web Update remains `197`, with unchanged web SHA-256 `4452235be464d6acb8622430f71e4f0a76b416579e41ad91207d52a4d256852e`.
- Release change is limited to the native Smart Reminder presentation: screen wake is routed to transparent `DiaryReminderWakeActivity`, not MainActivity; normal notification tap still targets MainActivity. Existing reminder scheduling, sound, Snooze/Done, restoration, storage and all Diary content/data remain preserved. No web HTML or user data changed.
- Backups: branch `backup/pre-wake-screen-no-app-open-2026-11-14`; files `backups/native-script-py-before-wake-screen-no-app-open-2026-11-14.py`, `backups/build-workflow-yml-before-wake-screen-no-app-open-2026-11-14.yml`, `backups/latest-json-before-wake-screen-no-app-open-2026-11-14.json`, `backups/master-register-md-before-wake-screen-no-app-open-2026-11-14.md`.
- Phone verification is **pending**. User may now install through **Me → Check for Updates**. Test with screen off: screen should wake to lock screen, notification and ringtone should arrive, and My Diary must not open by itself. Tapping the notification should open My Diary normally. Do not claim device-side success until user confirms. Never uninstall or clear app data.


---

# APK 1.0.142 — Restore missing versioned download file (2026-11-14)

- User reported **Me → Check for Updates** failed with HTTP 404. Investigation confirmed live `latest.json` advertised APK 1.0.142 / versionCode 141 and SHA-256 `9a538b5baa4a6ecf97158502e5b564473b158144c3bc324f41e1f8c83081a9d3`, but the versioned path `My-Diary-1.0.142.apk` was missing from the repository. Root cause was a filename mismatch in the previous workflow's git-add list; this task did not alter that workflow.
- Verified the signed Release APK from workflow artifact run `43601017474`: size 2,005,532 bytes; independently computed SHA-256 exactly matches the live feed. Independently computed Git blob SHA-1 is `4d09815ab977bacebfe27a0ea78373e78d72a4e1`, matching the existing `My-Diary.apk` blob exactly. Therefore the already-verified signed APK bytes were reused without rebuilding, re-signing, or changing the feed.
- Minimal repair: added repository path `My-Diary-1.0.142.apk` as an additional tree entry pointing to that exact existing blob. No existing file was overwritten. Commit: `0a3251fc93458bc340b36e81a9b4a041e82b48fc`. Added path re-fetched successfully; its blob SHA is `4d09815ab977bacebfe27a0ea78373e78d72a4e1`. Live `latest.json` re-fetched and remains unchanged at APK 1.0.142 / code 141 / SHA-256 above; Web Update 197 and its hash remain unchanged.
- Pre-repair backup branch: `backup/pre-missing-142-apk-2026-11-14`, created at exact prior main commit `2159ad732a3d536a8803042be56e1ab74c0677d8`. No workflow, native source, web source, app data, notes, photos, reminders, PIN/recovery data, package identity, or signing configuration changed. MUAZZIN was not touched.
- Verification status: missing versioned path now exists in the live main branch and references the byte-identical, previously hash-verified APK. The updater should now be retried via **Me → Check for Updates**. Physical-device download/install test and reminder behavior remain **pending** until the user confirms.


---

# APK 1.0.143 / Web Update 198 — Per-reminder ringtone and audio-file selection (2026-11-14)

- User request: allow a Smart Reminder to use a phone ringtone/alarm tone or an audio file selected from the device. Design decision: choose a sound separately for each reminder, with a default phone alarm option.
- Starting live state: APK 1.0.142 / versionCode 141; Web Update 197; package `com.personal.diaryapp`; main starting commit `89abdd32a130d9d4b82b68e298a0f930da61561e`.
- Scope: native Android reminder sound selection and the existing Smart Reminder form only. Changed `scripts/add_diary_app_actions.py`, `.github/workflows/build-diary-from-zip.yml`, and `web-source/index.html`. The web publisher generated matching `diary-web/index.html` and updated `latest.json`. No unrelated web feature was changed.
- UI: each reminder form now offers three choices: phone ringtone/alarm tone (Android Ringtone Picker), audio file (Android Storage Access Framework / File Manager, `audio/*`), or default phone alarm. Button and default label were added to all 10 supported language dictionaries. The chosen sound label appears in the reminder list and is restored when editing.
- Native behavior: the selected URI is stored with the reminder in the existing reminder record, passed through the alarm PendingIntent, and used to create a sound-specific notification channel with alarm audio attributes. The selected sound is preserved through Snooze and boot/package-replacement restoration. File-picker read permission is persisted for future alarm delivery. Existing reminders without a stored sound URI continue using the default phone alarm.
- Preserved: exact AlarmClock scheduling and permissions, lock-screen wake-only activity, normal notification tap into My Diary, notification category/priority, vibration/lights, Snooze, Done, reminder IDs, existing stored reminders, notes, photos, PIN/recovery data, app package identity, and signing identity. No new storage keys for notes or PIN and no app-data reset. MUAZZIN project untouched.
- Pre-edit backups created and re-fetched successfully on branch `backup/pre-custom-reminder-ringtones-2026-11-14`:
  - `backups/native-script-py-before-custom-reminder-ringtones-2026-11-14.py` (source blob `316b599d5f279747cadd49bc8bc259ea434fe6e5`)
  - `backups/build-workflow-yml-before-custom-reminder-ringtones-2026-11-14.yml` (source blob `bde2fd57bf5d2e8df2a687280fda5469fac22ae2`)
  - `backups/web-source-html-before-custom-reminder-ringtones-2026-11-14.html` and `backups/diary-web-html-before-custom-reminder-ringtones-2026-11-14.html` (both source blob `58db1f74729e21bff7139b068aad202fe58b537d`)
  - `backups/latest-json-before-custom-reminder-ringtones-2026-11-14.json` (source blob `c4b1e86a0a47d05ea4a1235b1267a86935ab6240`)
  - `backups/master-register-md-before-custom-reminder-ringtones-2026-11-14.md` (source blob `f1b8b4e442f52a7dc424f7b16ae7efee9523acf6`)
- Source PR #6 merged as `70604735d4985957add81c0b0c3d950433736f4f`. PR #7 then added a null-safe read of the optional audio-picker result flags in the source script, merged as `c4f3d41fe477b554a35fb08775595d80121f46fb`; this follow-up is source-side defensive handling and does not change normal selected-file behavior.
- Web publisher run `43604761824` completed successfully. Web Update advanced to `198`; `web-source/index.html` and `diary-web/index.html` were re-fetched byte-identical (both Git blob SHA `bc0f12816af112c155c53c1bd611e0d3d2003286`, 353,698 UTF-16 code units). Independently calculated SHA-256 of the exact HTML embedded in the signed APK is `23543bb8712b99de25da4d27accf56bad86376a47f0ceca154c4cf2dc5f5ca74`, matching live `latest.json.webSha256`.
- APK workflow run `43604761859` completed with conclusion `success`: project checks, translation audit, version guard, debug build, signed Release build, signing verification, publication and APK upload all passed. Live `latest.json`: APK `1.0.143`, versionCode `142`, URL `https://raw.githubusercontent.com/amuazzinxyz-ops/My-Diary-Updates/main/My-Diary-1.0.143.apk`, SHA-256 `4eccf17f61389bbb112a1daf910eb88d11315c19c22efa2d9e71171115688961`; Web Update `198` and web SHA-256 above. Versioned APK path exists in the main tree (Git blob SHA `7efc7d32fc297c8937f26e632f7799c4af633740`, 2,008,245 bytes).
- Downloaded the signed Release APK artifact `14117363203` and independently calculated SHA-256 `4eccf17f61389bbb112a1daf910eb88d11315c19c22efa2d9e71171115688961`, matching both the live feed and APK tree blob. Independently inspected signer certificate SHA-256 `23A4E93F3C7911DCE18389EA583548700C6AD6A3759707F1CD222D07E2408B5A`, matching the established signing identity. Workflow's apksigner verification passed.
- A follow-up build workflow run `43604849915` was triggered by PR #7 after the first APK had already published; see the follow-up workflow note below.
- Physical-device test of the new ringtone selector is **pending**. User should install using **Me → Check for Updates**, then create one test reminder with a phone ringtone, another with an audio file, and one with default sound. Confirm each plays when due; test Snooze retains the selected sound and Done still dismisses it. Existing reminders should continue with default phone alarm unless edited. Do not claim device-side success until user confirms.
- Rollback: preserve all backups above and the last known-good APK 1.0.142. If a regression occurs, restore only the affected source/workflow/web files from the verified backup branch and publish a higher versionCode; never uninstall, clear app data, or remove notes/photos/PIN/recovery data.


## Follow-up workflow note — run 43604849915 (2026-11-14)

- This second run was triggered by PR #7's null-safe source-script follow-up after APK 1.0.143 had already been successfully published by run 43604761859.
- Its project checks and debug build passed, and signed Release build configuration completed. The publish step correctly failed closed because the live feed had already advanced to APK 1.0.143 / versionCode 142, while this duplicate run was still approved only for the prior baseline 1.0.142 / code 141.
- APK upload steps were skipped; no duplicate APK or feed overwrite occurred. Re-fetched latest.json remains at 1.0.143 / code 142, SHA-256 4eccf17f61389bbb112a1daf910eb88d11315c19c22efa2d9e71171115688961. The successful publication remains run 43604761859.


---

# Web Update 199 — Personal Calendar completion (2026-11-14)

- User request: complete all remaining Personal Calendar work and verify it carefully. Starting live state: APK 1.0.143 / versionCode 142; Web Update 198; package `com.personal.diaryapp`; source/mirror blob SHA `bc0f12816af112c155c53c1bd611e0d3d2003286`; starting main commit `170a557277fa4261a2b8c52cf81b32500c1e8012`.
- Scope: web-only Personal Calendar and its integration with the existing Diary month view. Changed `web-source/index.html`; the web publisher generated matching `diary-web/index.html` and updated `latest.json`. No native Android source, build workflow, APK, Smart Reminder implementation, notes, photos, storage database version, package identity, or signing data changed.
- Personal Calendar now stores optional event time and details; supports non-repeating, daily, weekly, monthly and yearly recurrence; provides optional event-time reminders using the existing Android AlarmClock/notification bridge with separate `cal-` reminder IDs; supports edit/delete with cancellation/restoration of its own alarms; and includes time/details/repeat fields in Smart Search and PDF report output. Existing Personal Calendar records remain readable; the additional fields are optional and no IndexedDB schema/version migration was made.
- The Diary main month view now merges Personal Calendar event occurrences with existing Notes, marks event days, and displays Hijri day/month labels using `Intl.DateTimeFormat` with an Islamic-calendar fallback. Calendar has a separate section PIN gate/configuration using the existing Me-section PIN/recovery mechanism and its own `calendar` key. New Calendar interface strings were added for all 10 supported languages.
- Recurrence alarm behavior is intentionally bounded and transparent: future one-shot Android alarms are pre-scheduled for up to 30 daily, 52 weekly, 24 monthly, or 10 yearly occurrences, then replenished whenever Personal Calendar is opened. This uses the existing Android AlarmClock scheduler, so scheduled alarms retain the existing screen-off/boot restoration behavior; it is **not** an unbounded native repeating alarm if the user never opens Calendar again after the scheduled horizon. Calendar alerts use the existing default phone alarm channel. Phone-side delivery remains pending verification.
- Pre-edit backup branch: `backup/pre-personal-calendar-completion-2026-11-14` (initial backup set), and work branch `work/personal-calendar-completion-2026-11-14`. Six exact backups were created on the work branch and fetched back readable before editing:
  - `backups/web-source-before-personal-calendar-work-2026-11-14.html` — blob SHA `bc0f12816af112c155c53c1bd611e0d3d2003286`
  - `backups/diary-web-before-personal-calendar-work-2026-11-14.html` — blob SHA `bc0f12816af112c155c53c1bd611e0d3d2003286`
  - `backups/latest-before-personal-calendar-work-2026-11-14.json` — blob SHA `3d5c4909a73736b777bc855006482184d1d3ac26`
  - `backups/master-register-before-personal-calendar-work-2026-11-14.md` — blob SHA `a73b2709787c015436b897c770921cdb9d175c11`
  - `backups/native-script-before-personal-calendar-work-2026-11-14.py` — blob SHA `865303b946368f79f0366407ae49138dc2907bb5`
  - `backups/build-workflow-before-personal-calendar-work-2026-11-14.yml` — blob SHA `b313f11797f093b36ca38a11b7165bb796d6ed84`
- Source changes were committed on work branch `work/personal-calendar-completion-2026-11-14`; PR #9 merged by squash as commit `76bae63175d332f35b90ac2b54c87b3b2ef6c3ad`. Web publisher run `43607476077` completed with conclusion **success**. Publisher commit: `5959ca3916e1a336f0e3a935b5c6d19fcaab7066`.
- Verification: both inline JavaScript blocks passed V8 parse checks. Targeted recurrence checks passed for one-off, monthly 31st-to-short-month clamping, daily 30-occurrence horizon, weekly 52-occurrence horizon, and yearly 10-occurrence horizon. All 8 new Calendar translation keys were confirmed present in all 10 language dictionaries. Targeted static checks confirmed event time/details, recurrence selector, optional event reminder, separate Calendar PIN, Hijri rendering, main month-view event integration, full-screen alarm permission check, and cancellation on deletion.
- Live post-publish verification: `web-source/index.html` and `diary-web/index.html` were re-fetched and are byte-identical; both Git blob SHA `17e6e63fa9faf0074205b2cd5bfad3880cc6a0d9`, length 367,387 characters. Independently computed UTF-8 SHA-256 `529b3e39e1a7e26d85b235b17ada0f2a17b2cfdc85dee3940ac7a5b88bc93018` matches live `latest.json.webSha256`; live webVersion is 199. APK remains 1.0.143 / versionCode 142 with unchanged SHA-256 `4eccf17f61389bbb112a1daf910eb88d11315c19c22efa2d9e71171115688961`; no APK rebuild or signing action.
- Phone verification is **pending**. User should install Web Update 199 through **Me → Check for Updates**, then test: Personal Calendar opens with its own PIN gate; create/edit/delete an event with date/time/details; check daily/weekly/monthly/yearly display in the main month view; verify Hijri labels in different languages; test one-time and recurring event alerts with screen off and after reboot; confirm Snooze/Done affect only that event occurrence and Smart Reminder continues unchanged. Do not claim physical-device success until user confirms.
- Rollback: use the exact backups above on `work/personal-calendar-completion-2026-11-14`; restore only `web-source/index.html` if needed and publish a higher webVersion. Do not roll back or alter APK/native files, and never clear app data or delete Calendar records.


---

# Web Update 200 — Remove Personal Calendar inner lock button (2026-11-14)

- User asked to remove the extra Lock button shown inside Personal Calendar. Confirmed the intended scope by inspecting the live implementation: this was the modal-header `meFeatureLock` control, whose click simply closes the feature and returns to Me. The actual Calendar PIN gate is a separate flow.
- Minimal change to `web-source/index.html` only: hide `meFeatureLock` when `kind==='calendar'`. Preserve the PIN gate, PIN verify/create/forgot/recovery/manager functions, Calendar records, reminder alarms, and all other feature behavior. The existing button visibility for Documents and Memories remains unchanged; Kharcha remains unchanged.
- Before editing, fetched the live Master Register, source/mirror, feed, native script and Android build workflow. Created branch `work/remove-calendar-inner-lock-button-2026-11-14`. Six backups were created and fetched back readable with exact pre-edit lengths:
  - `backups/web-source-before-calendar-lock-button-removal-2026-11-14.html`
  - `backups/diary-web-before-calendar-lock-button-removal-2026-11-14.html`
  - `backups/latest-before-calendar-lock-button-removal-2026-11-14.json`
  - `backups/master-register-before-calendar-lock-button-removal-2026-11-14.md`
  - `backups/native-script-before-calendar-lock-button-removal-2026-11-14.py`
  - `backups/build-workflow-before-calendar-lock-button-removal-2026-11-14.yml`
- Both inline JavaScript blocks passed V8 syntax parsing. PR #10 merged by squash as commit `c6fe40c215883b9981d4973c295d7c068fe92c4e`.
- Web publisher run `43610280385` completed with conclusion **success**. Live `webVersion=200`; `web-source/index.html` and `diary-web/index.html` were re-fetched and are byte-identical, both Git blob SHA `7d42a5aa280f0a9ed3217dabe81ad931a7156032`, 367,387 characters. Live feed `webSha256=eac11a930eb722e49ccf6b4146555d34868405f0b144d8ad1f9e060d65b61c48`.
- APK remains unchanged at `1.0.143` / versionCode `142`, SHA-256 `4eccf17f61389bbb112a1daf910eb88d11315c19c22efa2d9e71171115688961`. No APK rebuild, native Android source change, data migration or signing action.
- Phone check: install the web change through **Me → Check for Updates**. Confirm the extra inner Lock button is gone from Personal Calendar and the PIN gate still appears when reopening it. No user-device test has yet been reported.


---

# Web Update 201 — Smart Reminder ringtone choices in Personal Calendar (2026-11-14)

- User request: Personal Calendar event reminders should have the same ringtone/sound selection options as Smart Reminder.
- Starting live state: APK 1.0.143 / versionCode 142; Web Update 200; package `com.personal.diaryapp`; starting source/mirror blob SHA `7d42a5aa280f0a9ed3217dabe81ad931a7156032`; starting main commit `2dc10f24f36aacf265aa302bf5b9fe6386fd52ba`.
- Scope: web-only change to `web-source/index.html`; publisher regenerated `diary-web/index.html` and `latest.json`. No native Android source, Android build workflow, APK, package/signing identity, Smart Reminder code, Calendar PIN/recovery, recurrence rules/horizons, records database, or other Diary feature was changed.
- Calendar form now reuses the exact existing Android Smart Reminder picker and bridge: choose a phone ringtone/alarm tone, choose an audio file from the device, or use the default phone alarm. It uses the existing localized `reminderSound` and `reminderSoundDefault` labels across all 10 supported languages.
- Selected sound URI and label are saved with the Calendar event; the URI is passed to every scheduled Calendar occurrence, including recurring occurrences. Editing an existing event restores its previous sound selection. The event card shows the selected sound label when its reminder is enabled. Existing Calendar records without a saved sound continue to use the default phone alarm.
- No native changes were needed: the existing Android `pickReminderSound` and `scheduleReminder(..., soundUri)` bridge already supports the same picker and sound URI for the separate `cal-` alarm IDs.
- Pre-edit backup branch: `work/calendar-reminder-ringtone-2026-11-14`. Exact backups were created and fetched back readable before editing:
  - `backups/web-source-before-calendar-reminder-ringtone-2026-11-14.html` — blob SHA `7d42a5aa280f0a9ed3217dabe81ad931a7156032`
  - `backups/diary-web-before-calendar-reminder-ringtone-2026-11-14.html` — blob SHA `7d42a5aa280f0a9ed3217dabe81ad931a7156032`
  - `backups/latest-before-calendar-reminder-ringtone-2026-11-14.json` — blob SHA `7362ea002629f1841d2fee7c72da3d6aaa0dbe9f`
  - `backups/master-register-before-calendar-reminder-ringtone-2026-11-14.md` — blob SHA `836302ec91d79c334c32ff737bad10e47db0f648`
- Source PR #11 merged by squash as commit `a54d578d1c162b8bd0af4e447807bde17cdce265`. Web publisher commit `d14dd75c5ec7e25eed852ad0399fc5da13a96c27` published Web Update 201. The publisher workflow run ID/conclusion was not exposed by the available run/status listing; publication itself was verified from the live source, mirror and feed.
- Post-publish verification: live `web-source/index.html` and `diary-web/index.html` were re-fetched byte-identical; both Git blob SHA `2275664443613a817d12aaf42a3cf56889185a90`, length 369,123 characters. Independently calculated UTF-8 SHA-256 `5d0f47cca0424f0d9c31ce94e85a280caf38633ec53252f89951b85fb9f50686` matches live `latest.json.webSha256`; live webVersion is 201.
- Targeted source checks confirmed the Calendar form calls the existing sound picker, stores/restores the selected URI and label, and passes the URI to each `cal-` scheduled alarm. Existing records fall back to empty URI/default alarm. APK remains 1.0.143 / versionCode 142 with unchanged SHA-256 `4eccf17f61389bbb112a1daf910eb88d11315c19c22efa2d9e71171115688961`; no APK rebuild or signing operation.
- Physical-device verification is **pending**. User should install Web Update 201 through **Me → Check for Updates**, then create a Calendar event with reminder enabled and test all three sound choices; edit the event to confirm the choice is retained; test one recurring event occurrence. Do not claim phone-side success until the user confirms.
- Rollback: use the exact pre-edit backups above and restore only `web-source/index.html` if required; publish a higher webVersion. Never clear app data or alter Calendar records, PIN/recovery data, notes, photos, or APK/signing files.


---

# Web Update 202 — Remove inner Lock buttons from My Documents and My Memories (2026-11-14)

- User request: remove only the extra header Lock button from **My Documents** and **My Memories**.
- Starting live state: APK 1.0.143 / versionCode 142; Web Update 201; package `com.personal.diaryapp`; starting source/mirror Git blob SHA `2275664443613a817d12aaf42a3cf56889185a90`; starting main commit `6c49082e013babf782d7cfd6ed9971542102eacb`.
- Scope: one-line web-only change in `web-source/index.html`: changed the modal-header Lock button visibility assignment to `meFeatureLock.hidden=true;`. This removes the extra button from the two requested sections. No other feature UI or behavior was changed.
- Explicitly preserved: the separate Documents and Memories PIN protection gate (`meFeatureProtected` still includes both kinds), PIN create/verify, Forgot PIN and recovery configuration, PIN Manager, document and memory record storage, attached files/photos, and all other Diary features. No PIN or user-data storage key was modified or deleted. Calendar and Kharcha security logic remains unchanged.
- Pre-edit backups were created on branch `backup/pre-documents-memories-lock-removal-2026-11-14` and fetched back readable with matching original Git blob SHAs:
  - `backups/web-source-before-documents-memories-lock-removal-2026-11-14.html` — `2275664443613a817d12aaf42a3cf56889185a90`
  - `backups/diary-web-before-documents-memories-lock-removal-2026-11-14.html` — `2275664443613a817d12aaf42a3cf56889185a90`
  - `backups/latest-before-documents-memories-lock-removal-2026-11-14.json` — `83a86d6dbdcbbaa30bdb8d906ecbdf2afda27b86`
  - `backups/master-register-before-documents-memories-lock-removal-2026-11-14.md` — `c9775ab431a8ff8479d7eae40e27af8572a06437`
  - `backups/native-script-before-documents-memories-lock-removal-2026-11-14.py` — `865303b946368f79f0366407ae49138dc2907bb5`
  - `backups/build-workflow-before-documents-memories-lock-removal-2026-11-14.yml` — `b313f11797f093b36ca38a11b7165bb796d6ed84`
- Work branch: `work/remove-documents-memories-lock-buttons-2026-11-14`. PR #12 merged by squash as commit `e21f7ff03d0db75cd059b8c6beb4a3e0c352960a`. PR changed exactly one file with 1 insertion and 1 deletion.
- Pre-merge validation: both inline JavaScript blocks passed V8 syntax parsing. Static checks confirmed the PIN protection gate, PIN configuration/recovery helpers, PIN Manager handler, and document/memory data paths remain present.
- Web publisher automatically created commit `cfae818f2f343158c8f1a0ea3c191aa2daf521b6` (`Publish My Diary web bundle update`). Live `latest.json` advanced to Web Update 202 and reports web SHA-256 `7b7c2bee7ac1d575748734521cd5602e17bab12b718ed7f9606e41aadb857a0d`. Live `web-source/index.html` and `diary-web/index.html` were re-fetched and are identical; both Git blob SHA `1ee54525c9a6dcbfe8f2cd9ca2c94ddffbcd7e10`, length 369071 characters.
- APK remains unchanged at 1.0.143 / versionCode 142 with SHA-256 `4eccf17f61389bbb112a1daf910eb88d11315c19c22efa2d9e71171115688961`. This was a web-only update; no APK rebuild, native Android source change, signing action, package identity change, or app-data migration.
- Physical-device verification is **pending**. Install Web Update 202 through **Me → Check for Updates**. Confirm the extra Lock button is absent from both My Documents and My Memories, and separately verify that opening each still presents its PIN gate and Forgot PIN/recovery remains available. Do not claim phone-side success until the user confirms.
- Rollback: use the exact pre-edit backups above and restore only `web-source/index.html` if needed, then publish a higher webVersion. Never clear app data or delete/modify documents, memories, PIN/recovery data, notes, photos, or APK/signing files.
