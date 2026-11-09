# MY DIARY — MASTER PROJECT REGISTER

**Single source of truth. Last updated: 2026-11-09 (1.0.105 remains the signed APK; temporary web-bundle bootstrap is active for older updater clients; affected-user device test pending).**

This file replaces the old project register. Read it first at the start of every My Diary task, then inspect the live repository and current source before editing. Older dated audit and handover files in `docs/` are historical evidence only; when they conflict with this register or current GitHub state, do not treat them as current instructions.

## 1. Project identity and boundary

- App: **My Diary** — a standalone Android app, separate from MUAZZIN.
- Repository: `amuazzinxyz-ops/My-Diary-Updates`
- Branch: `main`
- Android package: `com.personal.diaryapp`
- Latest signed APK: **1.0.105**, versionCode **105**. Published in commit `31d2249c6129c850e9dd16818ceb3a4a059842c6`. The live `latest.json` versionCode is temporarily set to **1** (versionName remains 1.0.105) solely to trigger the existing web-bundle updater in older installed apps; restore versionCode 105 after the affected user confirms the browser-fallback button has appeared.
- Latest update feed: `latest.json`.
- Current source archive: `Diary-Android-Project-v13 (6).zip`.
- Build workflow: `.github/workflows/build-diary-from-zip.yml`.
- Helper scripts and language data: `scripts/`.
- Project evidence and dated records: `docs/`.

**Hard boundary:** all future My Diary source, app, build, release, update, and documentation work belongs only in this repository. Do not use or modify the MUAZZIN website/repository/workflows for Diary work. Do not merge the two apps or create a second project/workflow/archive when the existing one can be reused.

## 2. Current published release — confirmed by live feed, build, and APK artifact

- Version: **1.0.105** / versionCode **105**.
- Package: `com.personal.diaryapp`.
- Published APK: `My-Diary-1.0.105.apk` (also copied to legacy `My-Diary.apk`).
- Update URL in live `latest.json`: `https://raw.githubusercontent.com/amuazzinxyz-ops/My-Diary-Updates/main/My-Diary-1.0.105.apk`.
- SHA-256 in live feed: `c94b0d682bd86cd0a2c0f344cc0158bcd9346453ede4b0f4eb447b67681ea7cf`.
- Published release commit: [31d2249](https://github.com/amuazzinxyz-ops/My-Diary-Updates/commit/31d2249c6129c850e9dd16818ceb3a4a059842c6).
- Build run `42656590333` completed successfully. The workflow validated the existing signing certificate fingerprint `23A4E93F3C7911DCE18389EA583548700C6AD6A3759707F1CD222D07E2408B5A` before publishing.
- Downloaded signed-release artifact and independently calculated the APK SHA-256; it exactly matches the live feed value above. The versioned APK exists in the main-branch publish commit.
- The 1.0.103 APK contains an allow-list for the repository's raw GitHub URL prefix (not an exact `My-Diary.apk` filename), so the new version-specific APK path remains within that approved prefix. This supports compatibility for older updater clients.
- The affected user's actual web-bundle bootstrap, browser download, and APK installation on a different user's phone remain **not device-verified**. Successful build/publication and matching checksum do not prove that the user's device has completed installation.
- The 1.0.105 updater sends `Accept-Encoding: identity` to avoid compressed-transfer Content-Length discrepancies with strict download-length checks. Older installed clients retain their previous native downloader. To bridge them, `web-source/index.html` and `diary-web/index.html` were updated to webVersion 10 with a browser-download fallback button. The live feed temporarily advertises versionCode 1 so 1.0.103 and older clients that already contain the web-bundle updater can fetch this HTML without entering the failing APK downloader. This is a bootstrap workaround, not yet device-verified; it requires the affected user to tap Check for Updates once, then use the new Browser download button to download/install the signed 1.0.105 APK. Restore feed versionCode 105 only after that bootstrap step is confirmed.

## 3. Updater reliability — included in published 1.0.95

- Reversible backup branch created: `backup/pre-updater-reliability-1.0.93`.
- Updater source: `scripts/add_diary_app_actions.py`.
- New downloader retries up to three times, uses a temporary partial file, checks content length when supplied, verifies SHA-256, validates APK package and version against the feed, and opens Android's unknown-app install permission settings when needed.
- 2026-11-09 user reported that tapping Download & Install shows the APK download/SHA-256 start message and then immediately reports download/verification failure. The signed APK remains 1.0.105; live latest.json is temporarily in legacy web-bundle bootstrap mode (versionCode 1, webVersion 10). The current updater requests uncached metadata and APK URLs, retries three times, checks HTTP response/content length/SHA-256/package/version, follows HTTPS GitHub CDN redirects only to approved GitHub content hosts, and displays the actual failure reason. The user's quoted older generic message does not reveal which check failed; the affected phone must still be tested with the published 1.0.104 build. A successful publication does not prove device-side download/install success.
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