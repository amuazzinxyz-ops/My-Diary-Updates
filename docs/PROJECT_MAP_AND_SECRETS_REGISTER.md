# MY DIARY — MASTER PROJECT REGISTER

**Single source of truth. Last updated: 2026-11-09 (My Diary 1.0.94 release verified).**

This file replaces the old project register. Read it first at the start of every My Diary task, then inspect the live repository and current source before editing. Older dated audit and handover files in `docs/` are historical evidence only; when they conflict with this register or current GitHub state, do not treat them as current instructions.

## 1. Project identity and boundary

- App: **My Diary** — a standalone Android app, separate from MUAZZIN.
- Repository: `amuazzinxyz-ops/My-Diary-Updates`
- Branch: `main`
- Android package: `com.personal.diaryapp`
- Latest published feed: **1.0.94**, versionCode **94**. The owner's phone had previously updated successfully from an older build; the other affected user's device-side update remains untested.
- Latest update feed: `latest.json`.
- Current source archive: `Diary-Android-Project-v13 (6).zip`.
- Build workflow: `.github/workflows/build-diary-from-zip.yml`.
- Helper scripts and language data: `scripts/`.
- Project evidence and dated records: `docs/`.

**Hard boundary:** all future My Diary source, app, build, release, update, and documentation work belongs only in this repository. Do not use or modify the MUAZZIN website/repository/workflows for Diary work. Do not merge the two apps or create a second project/workflow/archive when the existing one can be reused.

## 2. Current published release — confirmed by live feed and successful release workflow

- Version: **1.0.94** / versionCode **94**.
- Package: `com.personal.diaryapp`.
- Published APK: `My-Diary.apk`.
- Update URL: `https://raw.githubusercontent.com/amuazzinxyz-ops/My-Diary-Updates/main/My-Diary.apk`.
- SHA-256 in live `latest.json`: `61e5d915ff2ec6d62833e4cff8427a11be60592a1bad998a91ccdb33d5b133e9`.
- Release workflow run: [42510516768](https://github.com/amuazzinxyz-ops/My-Diary-Updates/actions/runs/42510516768), completed successfully. The workflow calculated the SHA-256 from the signed Release APK, wrote that value into `latest.json`, and committed the APK and feed together in commit `426d7d16528ae609ffd483dbf6f6cfe8569cb37b`.
- Signing certificate SHA-256 fingerprint verified against the previously trusted identity: `23A4E93F3C7911DCE18389EA583548700C6AD6A3759707F1CD222D07E2408B5A`.
- A duplicate queued run [42510711957](https://github.com/amuazzinxyz-ops/My-Diary-Updates/actions/runs/42510711957) failed closed because 1.0.94 had already been published; its guard correctly refused to overwrite the live 1.0.94 feed. This does not invalidate the successful 1.0.94 release run.
- The separate affected user's actual phone installation remains untested; no device-side success is claimed.

## 3. Updater reliability — included in published 1.0.94

- Reversible backup branch created: `backup/pre-updater-reliability-1.0.93`.
- Updater source: `scripts/add_diary_app_actions.py`.
- New downloader now retries up to three times, uses a temporary partial file, checks content length when supplied, verifies SHA-256, validates APK package and version against the feed, and opens Android's unknown-app install permission settings when needed.
- Uses the existing raw.githubusercontent.com APK URL so older 1.0.92 clients' URL allow-list is not changed.
- Workflow next-version gate is 1.0.94 / code 94 and feed baseline is 1.0.93 / code 93.
- Latest source/workflow commits: `60d19813d1b9e2ab4361238c829dda17acf401bf` (updater compatibility) and `460ddfd6fe7035c893e1b71790288c408fc57650` (workflow version gate). The 1.0.94 release has **not yet been confirmed published**; do not claim it is available until live feed, build, signing fingerprint, and APK SHA are verified.
- Publishing conflict fix: workflow now serializes release runs, fetches current `origin/main` immediately before publishing, refuses to overwrite unless the live feed is still exactly 1.0.93/93, then commits only the verified APK and feed using a normal fast-forward push. Workflow commits: `1b7c87a51bf97232081e34f80731b6e15b77be0f` and syntax-escape correction `9f6a4d5e4120bc6b8aa9ff1175a225d52f2f91a1`. Latest build run `42510516768` is pending at last check; run `42510479638` is also in progress. Live feed remains 1.0.93 until verified publication.

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

## 8. User's current known next goal

- Continue completing the remaining 10 languages to reach 20 total.
- Only after all 20 languages are complete and checked, work on automatic language detection.
- For any new feature or correction the user specifies before that, prioritize the exact request and preserve the rest of the app.

## 9. Short request format (optional)

The user can simply say what they want in Roman Hindi. No special template, file upload, or explanation is required when the existing project contains what is needed.


- Follow-up publish validation finding: run `42510479638` built the debug APK successfully and the signed Release APK passed the previously registered certificate fingerprint check, but publish stopped at a redundant Gradle-version regex check. The earlier fail-closed source/feed gate had already validated version 1.0.94/94; the second check was brittle and blocked publication. Workflow commit `fd25e3dd44ca16f594a14076a9a7904a6dcd4694` removes that duplicate parsing and carries the already-approved fixed release metadata into the publish step. New run `42510711957` is pending. Live feed remains 1.0.93/93; no 1.0.94 release is claimed yet.