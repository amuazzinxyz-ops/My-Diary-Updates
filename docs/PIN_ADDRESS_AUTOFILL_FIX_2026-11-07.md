# My Diary PIN address-autofill correction — 2026-11-07

## Scope
- Repository: `amuazzinxyz-ops/My-Diary-Updates`, branch `main`.
- Only the Diary PIN-entry experience was changed. MUAZZIN repositories and files were not used or modified.
- The original Android source archive remains unchanged in the repository.

## Correction
- Diary note PIN input now uses a dedicated field name, numeric pattern, and `autocomplete="new-password"` rather than `autocomplete="off"`, with password-manager/address-autofill suppression hints.
- The Diary master-lock PIN input receives the same protections.
- Android WebView JavaScript prompts whose message identifies a PIN now use a native numeric password dialog with a four-digit limit and Android autofill disabled (API 26+). Non-PIN prompts continue through the normal WebChromeClient behavior.
- PIN validation, hashing, local storage keys, saved note records, recovery behavior, and existing note data were not intentionally changed.

## Build verification
- Commit containing the correction: `bcd1143326cec2ebf7400cd24d842a066b43dac3`.
- Follow-up build-script import correction: `67e6fc1feba4f6d29eb37d2894ca3c13b701403c`.
- Successful GitHub Actions run: [42362033620](https://github.com/amuazzinxyz-ops/My-Diary-Updates/actions/runs/42362033620).
- Debug APK artifact ID: `13570445416`; artifact name: `My-Diary-debug-APK`.
- Downloaded debug APK SHA-256: `e96366804a6390f4f36d6cdec925f887386936371c6c549a22f24b3df8f395b9`.
- APK archive inspection confirmed the packaged HTML contains the updated `new-password` attributes and unique Diary PIN field names.
- Android compilation and debug APK packaging succeeded.

## Not yet completed
- The signed Release build and publication steps were skipped because the dedicated My-Diary-Updates repository workflow did not have the Diary keystore secret available (`HAS_KEYSTORE: false`).
- No production APK was published and `latest.json` was not changed.
- No real-device autofill test has been performed. The debug APK is not a safe in-place update for users of the release-signed app; do not ask users to uninstall their current Diary app or install the debug APK as a replacement.
- A release-signed build using the already trusted Diary signing certificate, followed by device testing and update-feed publication, remains required before all users can receive this fix.

## Preservation
The source ZIP, existing APK files, update metadata, app identity, signing register, and unrelated Diary features were left unchanged by this PIN correction.
