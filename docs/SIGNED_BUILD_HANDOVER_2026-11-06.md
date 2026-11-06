# My Diary signed build handover — 2026-11-06

This record keeps the previously verified signed Diary APK build easy to locate from the dedicated `My-Diary-Updates` repository.

## Signed APK build

- App: My Diary New
- Android application ID: `com.personal.diaryapp` (repository's established ID; device install/update still needs testing)
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
- Build log explicitly confirmed: release APK certificate matches the previously supplied trusted fingerprint.
- Artifact expiry shown by GitHub: **2026-12-06 01:42 UTC**.

## Important limitations

- This is a successful signed build artifact, not proof of a successful install/update on the user's phone.
- Do not uninstall the currently installed Diary app. Before any migration, preserve/export Diary data and confirm whether the installed build's signing certificate matches this release.
- The artifact link above is temporary and expires. This record preserves the IDs and checksums, but the APK binary has **not yet been permanently copied into this repository**.
- The build version name/versionCode for this artifact were not independently confirmed in the retained artifact listing; verify from the APK before publishing it as an update.
- Do not put keystores, passwords, tokens, private diary entries, or user data in this repository.
- Keep all Diary source, builds, release metadata, and future update work in `amuazzinxyz-ops/My-Diary-Updates`. Keep MUAZZIN code, settings, hosting, and release workflow separate and unchanged.

## Related build artifacts

- Debug APK artifact ID: `13470440224` (not suitable as a production update unless signing compatibility is confirmed).
- Interface text audit artifact ID: `13469559136`.
- Both are temporary GitHub Actions artifacts from the same build run; do not treat them as permanent release files.


## Latest updated-menu signed build — 2026-11-06

- Workflow run: [42166826100](https://github.com/amuazzinxyz-ops/Muazzin-New/actions/runs/42166826100) (run #93; successful)
- Isolated build branch: `diary-release-build-20261106`
- Build commit: `f0516b48d3dbe0b849b1ee0ab8611df610991588`
- Includes the current `scripts/add_diary_app_actions.py` step in the Diary build workflow, so the Share App / Check for Updates menu changes are included in this build.
- Signed release artifact: [My-Diary-signed-Release-APK](https://github.com/amuazzinxyz-ops/Muazzin-New/actions/runs/42166826100/artifacts/13479477068)
- Artifact ID: `13479477068`; ZIP size: 1,885,140 bytes; ZIP SHA-256: `b1054e18b73cf3bea63566f2871a3bcd6628e1f40f65535cfee8179c1d110014`
- Extracted APK: `app-release.apk`; size: 1,941,678 bytes; SHA-256: `3850b28ceb48794f6712f8a003b7be5ae7c1d257b08c703f22bc684a0c2546d5`
- GitHub Actions completed all steps successfully, including the release signing step and the upload of the signed APK. The workflow's signing step explicitly compares the APK certificate SHA-256 with the trusted fingerprint `23A4E93F3C7911DCE18389EA583548700C6AD6A3759707F1CD222D07E2408B5A`; a successful step means that check passed.
- Artifact expiry: 2026-12-06 05:14 UTC.
- The build uses the standalone Diary package identity `com.personal.diaryapp` and launcher label `My Diary` as set by the identity script.
- APK manifest was inspected from the downloaded artifact: package `com.personal.diaryapp`, versionCode `90`, versionName `1.0.90`.
- The retained prior publication APK from `my-diary-update-publication-v89.zip` was independently inspected: package `com.personal.diaryapp`, versionCode `89`, versionName `1.0.89`, and the same signing certificate SHA-256. Therefore this new APK is a valid higher-version signing/package match for that v89 APK. This still cannot prove which exact version is currently installed on the user's phone.

### Still not verified / next actions

- The APK has not been installed on the user's phone. Do not uninstall the existing app.
- The installed app's package ID and signing certificate have not yet been independently checked against this APK on-device; do not promise in-place update until that comparison is done.
- The APK binary is still a temporary Actions artifact in the isolated Diary build branch of `Muazzin-New`; it has not yet been permanently copied into `My-Diary-Updates`. The dedicated repository's Actions secrets are not configured, and the artifact cannot be promoted there with the available repository-file actions alone. Do not describe the consolidation as complete.
- The artifact is a signed release APK, not a debug APK. The debug artifact is not the one to install.

- **Updater feed is not live yet:** the currently committed `latest.json` still points to version 1.0.89 and its old APK checksum/URL. Do not use “Check for Updates” in 1.0.90 until the 1.0.90 APK has been permanently hosted at the exact URL in `latest.json` and the JSON version/checksum have been updated together. This build contains the updater code, but the new release has not been published to its feed.
