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
