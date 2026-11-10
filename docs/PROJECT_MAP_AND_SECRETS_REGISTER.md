# MY DIARY — MASTER PROJECT REGISTER

**Single source of truth. Last updated: 2026-11-11 (signed APK 1.0.119 / versionCode 118; Web Update 55 fixes Recently Deleted action-button label fit).
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
