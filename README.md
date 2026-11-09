# My Diary

Standalone Android diary app and its update repository. This project is separate from MUAZZIN.

## Start here

**Read the [My Diary Master Project Register](docs/PROJECT_MAP_AND_SECRETS_REGISTER.md) before every task.** It is the single current handover for project location, app identity, release state, language status, feature-preservation rules, and the required build/edit workflow.

## Current confirmed app state

- App package: `com.personal.diaryapp`
- Current published version: **1.0.105** (versionCode 105)
- Current APK: [My Diary 1.0.104 (signed APK)](https://raw.githubusercontent.com/amuazzinxyz-ops/My-Diary-Updates/main/My-Diary-1.0.105.apk)
- Update metadata: [latest.json](latest.json)
- Version 1.0.103 is the live signed update. Its updater includes cache-busting requests, retry handling, SHA-256/package/version checks, and a visible failure reason. The published 1.0.104 feed includes GitHub CDN redirect validation; the affected user's device-side download, verification, and in-place installation still require confirmation.

## Repository layout

- `Diary-Android-Project-v13 (6).zip` — existing Android source archive.
- `.github/workflows/build-diary-from-zip.yml` — Diary-only Android build workflow.
- `scripts/` — app-generation, identity, language, and build helper scripts.
- `assets/` — Diary assets.
- `docs/` — master register and dated historical audits/handover records.
- `latest.json` — current update-feed metadata.
- The signed 1.0.105 APK is published at the updater-compatible version-specific `/main/My-Diary-1.0.105.apk` URL. The release fixes APK download verification by relying on the complete response and SHA-256 rather than rejecting Content-Length differences.

## Non-negotiable safety rules

- Keep all My Diary work inside this repository. Never modify MUAZZIN files or workflows for a Diary task.
- Preserve the same Android package, trusted signing identity, local notes/photos, PIN locks, and unrelated features.
- Never publish a debug or unsigned APK as a production update.
- Never ask the user to uninstall the working app or clear its data as a routine step.
- Never expose or change signing secrets.
- Make only the requested change, back up first, test, and update the Master Project Register.

Older dated documents under `docs/` are retained as historical evidence. If an older document conflicts with the live repository or Master Register, inspect the current GitHub state and follow the Master Register.
