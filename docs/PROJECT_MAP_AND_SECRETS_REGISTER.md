# MY DIARY — MANDATORY SAFE-WORK PROTOCOL (READ FIRST EVERY TASK)

**Status checked against live `latest.json` on 2026-11-13:** APK `1.0.136` / versionCode `135`; webVersion `140`; package `com.personal.diaryapp`. The live feed is authoritative for current release values. Re-read it before every task; never assume these values remain current. (This line corrects the stale 126/126 figures recorded earlier.)

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
- [ ] Register updated with evidence and backup paths
- [ ] Phone-test status clearly marked; no unsupported success claim

**STOP RULE:** If any item required for the type of release cannot be verified, do not publish and do not describe the task as complete. Tell the user exactly what is blocked and preserve the last known-good version.


---

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
