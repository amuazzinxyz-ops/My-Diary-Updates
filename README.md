# My Diary

Standalone Android diary app and its update repository. This project is separate from MUAZZIN.

## Start here

**Read the [My Diary Master Project Register](docs/PROJECT_MAP_AND_SECRETS_REGISTER.md) before every task.** It is the single current handover for project location, app identity, release state, language status, feature-preservation rules, and the required build/edit workflow.

## Current confirmed app state

- App package: `com.personal.diaryapp`
- Current published version: **1.0.92** (versionCode 92)
- Current APK: [My-Diary.apk](My-Diary.apk)
- Update metadata: [latest.json](latest.json)
- User confirmed that version 1.0.92 installed over the previous app successfully, Arabic appeared, and the existing app continued to work.

## Repository layout

- `Diary-Android-Project-v13 (6).zip` — existing Android source archive.
- `.github/workflows/build-diary-from-zip.yml` — Diary-only Android build workflow.
- `scripts/` — app-generation, identity, language, and build helper scripts.
- `assets/` — Diary assets.
- `docs/` — master register and dated historical audits/handover records.
- `latest.json` — current update-feed metadata.
- `My-Diary.apk` — current published APK.

## Non-negotiable safety rules

- Keep all My Diary work inside this repository. Never modify MUAZZIN files or workflows for a Diary task.
- Preserve the same Android package, trusted signing identity, local notes/photos, PIN locks, and unrelated features.
- Never publish a debug or unsigned APK as a production update.
- Never ask the user to uninstall the working app or clear its data as a routine step.
- Never expose or change signing secrets.
- Make only the requested change, back up first, test, and update the Master Project Register.

Older dated documents under `docs/` are retained as historical evidence. If an older document conflicts with the live repository or Master Register, inspect the current GitHub state and follow the Master Register.
