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

## Last independently verified published release

- Version: **1.0.89** (Android versionCode **89**)
- Android application ID: `com.personal.diaryapp`
- APK filename: `My-Diary.apk`
- APK SHA-256: `c900a97da2cc5cad275d9f176f61a8ebde81b44643a7ca8c72d655c84249d415`
- The retained v1.0.89 build record reports a successful signing-certificate check.
- Device installation/update test: **not yet performed**.

This is the last release whose published APK identity is independently recorded in the repository's earlier audit. Do not assume that it is the current installed phone version.

## Current update-feed metadata — not yet cleared for release

The current committed `latest.json` declares:

- Version: **1.0.90** (versionCode **90**)
- Package: `com.personal.diaryapp`
- APK URL: `https://raw.githubusercontent.com/amuazzinxyz-ops/My-Diary-Updates/main/My-Diary.apk.apk`
- Declared SHA-256: `3850b28ceb48794f6712f8a003b7be5ae7c1d257b08c703f22bc684a0c2546d5`

The 1.0.90 signed candidate build and its certificate fingerprint are recorded in [docs/SIGNED_BUILD_HANDOVER_2026-11-06.md](docs/SIGNED_BUILD_HANDOVER_2026-11-06.md). However, the feed is **not cleared for release**: the metadata URL uses the accidental double-extension filename `My-Diary.apk.apk`, while the existing publication workflow validates the canonical URL ending in `My-Diary.apk`. The APK binary at the current metadata URL has not been independently downloaded and re-hashed in this repository, and device install/update behavior has not been tested.

**Do not use “Check for Updates” as a release test, do not install a candidate over the current app, and do not change or delete either APK until the APK file, metadata URL/hash, signing identity, and update path have all been reconciled and verified.** Do not publish a debug APK.

## Share and update options audit

The current evidence and remaining source/device-test requirements for **Share App** and **Check for Updates** are recorded in [docs/SHARE_AND_UPDATE_OPTIONS_AUDIT_2026-11-06.md](docs/SHARE_AND_UPDATE_OPTIONS_AUDIT_2026-11-06.md). The audit is not proof of a successful live Android share-sheet or updater test.

## Build archive / handover

The separately verified signed-build artifact, APK checksum, certificate fingerprint, artifact IDs, expiry, and testing cautions are recorded in [docs/SIGNED_BUILD_HANDOVER_2026-11-06.md](docs/SIGNED_BUILD_HANDOVER_2026-11-06.md). This is a build-evidence record, not proof that the 1.0.90 candidate has been safely published or phone-tested.
