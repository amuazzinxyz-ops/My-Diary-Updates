# My Diary

Standalone Android diary app and its update repository. This project is separate from MUAZZIN.

## Start here

**Read the [My Diary Master Project Register](docs/PROJECT_MAP_AND_SECRETS_REGISTER.md) before every task.** It is the single current handover for project location, app identity, release state, language status, feature-preservation rules, and the required build/edit workflow.

## Current confirmed app state

- App package: `com.personal.diaryapp`
- Current published version: **1.0.113** (versionCode 112)
- Current APK: [My Diary 1.0.113 (signed APK)](https://raw.githubusercontent.com/amuazzinxyz-ops/My-Diary-Updates/main/My-Diary-1.0.113.apk)
- Update metadata: [latest.json](latest.json)
- The updater downloads the complete APK response and validates it using SHA-256, package name, and versionCode; it does not reject a valid download solely because the HTTP Content-Length differs.
- The user confirmed on 10 Nov 2026 that Check for Updates now updates successfully on both their own phone and another user's phone.
- Version 1.0.112 set Check for Updates, Refresh, and Share App button heights to 40px. Version 1.0.113 adds the Interface Colours palette to the Me menu (Original, Blue, Green, Rose), saves the selected theme on the device, and preserves existing Diary data. Successful signed build/publish run: [42774333846](https://github.com/amuazzinxyz-ops/My-Diary-Updates/actions/runs/42774333846). The release APK SHA-256 is 4db6f8e7bf5fea511a133a8750e56060f165d8d0653739a5cddbfba62a5c48cc.
## Repository layout

- `Diary-Android-Project-v13 (6).zip` — existing Android source archive.
- `.github/workflows/build-diary-from-zip.yml` — Diary-only Android build workflow.
- `scripts/` — app-generation, identity, language, and build helper scripts.
- `assets/` — Diary assets.
- `docs/` — master register and dated historical audits/handover records.
- `latest.json` — current update-feed metadata.
- The signed 1.0.113 APK is published at the updater-compatible version-specific `/main/My-Diary-1.0.113.apk` URL. The updater verifies the complete download using SHA-256, package name, and versionCode.

## Non-negotiable safety rules

- Keep all My Diary work inside this repository. Never modify MUAZZIN files or workflows for a Diary task.
- Preserve the same Android package, trusted signing identity, local notes/photos, PIN locks, and unrelated features.
- Never publish a debug or unsigned APK as a production update.
- Never ask the user to uninstall the working app or clear its data as a routine step.
- Never expose or change signing secrets.
- Make only the requested change, back up first, test, and update the Master Project Register.

Older dated documents under `docs/` are retained as historical evidence. If an older document conflicts with the live repository or Master Register, inspect the current GitHub state and follow the Master Register.
