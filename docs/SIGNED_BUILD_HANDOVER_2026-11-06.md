# My Diary signed build handover — 2026-11-06

This record preserves evidence for the separately built signed Diary APK candidate. It does not mean that the candidate has been published to the dedicated update feed or tested on a phone.

## Earlier signed APK build

- App: My Diary New
- Android application ID: `com.personal.diaryapp`
- Workflow run: [42145229060](https://github.com/amuazzinxyz-ops/Muazzin-New/actions/runs/42145229060)
- Build commit: `44c3212b097e5b1b0de9d54f0c6da73ec735c8f7`
- Build branch label at source: `diary-android`
- Signed APK artifact: [My-Diary-signed-Release-APK](https://github.com/amuazzinxyz-ops/Muazzin-New/actions/runs/42145229060/artifacts/13469174755)
- Artifact ID: `13469174755`
- Artifact ZIP size: 1,881,333 bytes
- Artifact ZIP SHA-256: `1ecc7a8c1555710badc4f29cb7ea6fdcb22780a43f260c8ef4ec02e2adeb74d6`
- Extracted APK filename: `app-release.apk`
- Extracted APK size: 1,937,690 bytes
- Extracted APK SHA-256: `a9a3a314d47fe482ad7236781310040c1d1c559162e93a714720901d3c57f7e4`
- Signing certificate SHA-256: `23A4E93F3C7911DCE18389EA583548700C6AD6A3759707F1CD222D07E2408B5A`
- The retained build log explicitly confirmed that the release APK certificate matched the trusted fingerprint.
- Artifact expiry shown by GitHub: **2026-12-06 01:42 UTC**.

## Latest updated-menu signed build — 2026-11-06

- Workflow run: [42166826100](https://github.com/amuazzinxyz-ops/Muazzin-New/actions/runs/42166826100) (run #93; successful)
- Isolated build branch label in the retained build record: `diary-release-build-20261106`
- Build commit: `f0516b48d3dbe0b849b1ee0ab8611df610991588`
- Signed release artifact: [My-Diary-signed-Release-APK](https://github.com/amuazzinxyz-ops/Muazzin-New/actions/runs/42166826100/artifacts/13479477068)
- Artifact ID: `13479477068`; ZIP size: 1,885,140 bytes; ZIP SHA-256: `b1054e18b73cf3bea63566f2871a3bcd6628e1f40f65535cfee8179c1d110014`
- Extracted APK: `app-release.apk`; size: 1,941,678 bytes; SHA-256: `3850b28ceb48794f6712f8a003b7be5ae7c1d257b08c703f22bc684a0c2546d5`
- Signing certificate SHA-256: `23A4E93F3C7911DCE18389EA583548700C6AD6A3759707F1CD222D07E2408B5A`
- The retained build log reports a successful signing step and trusted-certificate comparison.
- APK manifest inspection recorded package `com.personal.diaryapp`, versionCode `90`, versionName `1.0.90`.
- Artifact expiry shown by GitHub: **2026-12-06 05:14 UTC**.
- The retained comparison record says this candidate is a higher-version package/signing match against the v1.0.89 APK. This is not a phone install/update test.

## Current feed state checked — 2026-11-07

The dedicated repository's committed `latest.json` was inspected on 2026-11-07. It currently declares versionName `1.0.90`, versionCode `90`, and SHA-256 `3850b28ceb48794f6712f8a003b7be5ae7c1d257b08c703f22bc684a0c2546d5`. Its APK URL currently ends in `My-Diary.apk.apk`.

The existing `.github/workflows/publish-diary-update.yml` expects the canonical APK URL ending in `My-Diary.apk`. Therefore the current metadata URL and publication-workflow validation rule do not agree. The current repository copy at the double-extension URL has not been independently downloaded and re-hashed during this check. Treat version 1.0.90 as a signed build candidate recorded by the handover, **not as a safely verified published update**. The earlier statement in this document that the feed remained at v1.0.89 is superseded by this 2026-11-07 inspection.

## Important limitations and next safe steps

- The 1.0.90 candidate has not been installed on the user's phone. Do not uninstall the currently installed app.
- The installed app's package ID and signing certificate have not been independently checked on-device; do not promise in-place update until that comparison is done.
- The APK candidate has not been independently confirmed at the exact URL currently declared by `latest.json`.
- The dedicated Diary build workflow's debug build can succeed without the signing secrets, but its signed Release step is skipped when those secrets are absent from that repository's Actions context. The original project ZIP used by that workflow declares `versionCode = 1` and `versionName = "1.0"`; the current identity script changes applicationId/label/icon but not version, and the workflow's release metadata writer is hardcoded to versionCode 90 / versionName 1.0.90. Consequently, the ZIP workflow's debug APK is version 1 and cannot be treated as an update to the known v1.0.90 installation; Android will reject a version-code downgrade, and its debug signing identity is not the trusted release key. Do not install this debug APK over the user's existing app or publish it. A next release version must be chosen only after installed-app identity and version are checked on-device.
- The permanent project register records that the existing four Diary signing secrets must remain at their recorded location and must not be transferred, recreated, deleted, renamed, or changed. The project boundary also forbids doing Diary work in the MUAZZIN repository. Do not bypass these rules or expose secret values.
- Do not publish a debug APK, alter the trusted signing certificate, or modify `latest.json`/release APK files until the release binary, canonical URL, checksum, package/version, and update path are reconciled under the register's rules.
- Android phone visual testing, PIN autofill testing, share-sheet testing, and in-place update testing remain pending.

## Related earlier artifacts

- Earlier debug APK artifact ID: `13470440224` (not suitable as a production update unless signing compatibility is independently confirmed).
- Earlier interface text audit artifact ID: `13469559136`.
- GitHub Actions artifacts are temporary and expire; this record preserves evidence and identifiers, not a permanent APK binary.


## Release workflow guard added — 2026-11-07

The Diary ZIP build workflow now has a signed-release-only fail-closed version check. It compares the extracted Gradle package/versionCode/versionName with `latest.json`, requires the canonical `My-Diary.apk` URL, and requires versionCode greater than the last user-confirmed installed versionCode 90. The publish step derives its version fields from the checked Gradle source rather than hardcoding 1.0.90. Current source is still version 1.0 / code 1 while feed is 1.0.90 / code 90, so a signed release will be blocked until the source version and intended next release are deliberately reconciled. This change does not bump versions, modify release files or metadata, access signing secrets, trigger a build, or publish an APK. Commit: `c9fb687f9366b420b57b6f46bb3f470b51bbde80`.
