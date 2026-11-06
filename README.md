# My Diary New

**Independent identity:** My Diary New is a separate app and update channel. It is not part of MUAZZIN.

## Repository purpose

This repository, `My-Diary-Updates`, is reserved only for distributing official **My Diary New** Android app updates.

## Separation from MUAZZIN

- Keep the existing MUAZZIN website, repository, hosting, files, branding, and behavior unchanged.
- Do not place MUAZZIN website files or MUAZZIN app releases here.
- Do not connect this repository to the MUAZZIN website deployment.
- Diary branding and app identity must be maintained independently.

## What belongs here

- Signed My Diary New APK release files
- Version and update-check metadata for My Diary New
- Release notes for My Diary New
- Diary-only build verification and handover records

## What does not belong here

- The app's private diary entries or user data
- Signing keystores, passwords, access tokens, or other secrets
- MUAZZIN files or files for any other app

## Release requirements

Before publishing an update, verify all of the following against the actual Diary app project and its previously trusted release:

1. Android application ID (must remain the Diary app's own ID)
2. Version name and monotonically increasing version code
3. Signing certificate (must match the trusted Diary release key)
4. APK SHA-256 checksum
5. Install/update test on an Android device

Never invent an application ID, signing identity, version, checksum, or release file. Do not publish an APK until the original Diary app project and signing setup are available and verified.

## Current verified release

- Version: **1.0.89** (Android versionCode **89**)
- Android application ID: `com.personal.diaryapp`
- Public APK: `My-Diary.apk`
- Update metadata: `latest.json`
- APK SHA-256: `c900a97da2cc5cad275d9f176f61a8ebde81b44643a7ca8c72d655c84249d415`
- Signed build workflow: successful; signing certificate check passed.
- Native updater: included in v1.0.89. It checks for a newer release when the app opens, verifies the downloaded APK checksum, and hands installation to Android.
- Device installation/update test: **not yet performed**.

The first installation of v1.0.89 must be done manually because older installed versions do not contain the updater. Later releases can be detected from inside the app. Android still requires its own user confirmation to install.

## Share and update options audit

The current evidence and remaining source/device-test requirements for **Share App** and **Check for Updates** are recorded in [docs/SHARE_AND_UPDATE_OPTIONS_AUDIT_2026-11-06.md](docs/SHARE_AND_UPDATE_OPTIONS_AUDIT_2026-11-06.md). Do not treat the temporary candidate APK as proof of the updater until the repository's published APK is independently checked.

## Build archive / handover

The latest separately verified signed-build artifact and its APK checksum, certificate fingerprint, artifact IDs, expiry, and testing cautions are recorded in [docs/SIGNED_BUILD_HANDOVER_2026-11-06.md](docs/SIGNED_BUILD_HANDOVER_2026-11-06.md). This handover is an archive pointer, not a claim that the newer APK has already been published or phone-tested.
