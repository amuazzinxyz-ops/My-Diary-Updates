# My Diary Project Register (Permanent Handover)

Last reviewed: 2026-11-26

## Current release state — 2026-11-26

- Latest published web version: **478**. Web 478 resets header-button Move Mode to OFF whenever the Me menu closes, including outside taps and navigation into Calendar notes, Private Locker, and feature pages. It preserves saved button positions and sizes. Phone test pending.
- Web 478 source and mirror are byte-identical. SHA-256: `04374ed939422483b0b832f95e442ddba530b90aa5bc7501460c515d11dd7530`; `latest.json` declares `webVersion: 478` with the same SHA-256.
- Web 477 remains the previous known-good release and rollback target. **Phone Test PASS — Web Update 477 confirmed by the user on 2026-11-26.** The “Button Set Karein” label is now vertically centered; 16px bold size and left alignment remain correct.
- Web 476 history: increased the label from 15px to 16px, retaining bold weight 950 and left alignment. Phone test pending.
- Web 476 source and mirror were byte-identical. SHA-256: `ef234ad7e8b1182bf2368c332e506b3e87c89571e2d92c5010f0261b7900938e`.
- Web 475 history: the label was 15px, left-aligned, with bold weight 950; phone test pending.
- Web 475 source and mirror were byte-identical. Published Web 475 SHA-256: `070d762968501ae0f3a2fd8a57ef0cd7bee7eedb0fbfc3192e8018b1314a4fb0`; its release metadata was published before Web 476.
- **Phone Test PASS — Web Update 473 confirmed by the user on 2026-11-26.** Web 473 removed only the Move Mode instruction text inside Button Set Karein and changed its inner close button label from “Band Karein” to “Band”.
- Web 472 rollback and its user-confirmed Phone Test PASS remain in release history. Web 472 rolled back the Web 471 saved-position reload change and restored the exact Web 470 source content.
- Web 469 added **Button Set Karein** inside the existing Me menu. Web 470 only shortened its move-button label to “Position badalne ke liye”. Web 471's saved-position reload change was rolled back in Web 472; Web 472 used the exact Web 470 source content.
- Recently Deleted fullscreen layout remains isolated: its × button retains the original top-right position and default 36px size even when a custom heading-button layout is saved.
- APK remains unchanged: `versionName: 1.0.220`, `versionCode: 219`, SHA-256 `7515fee36d815d2238797eab3ecac830f8eee969eaf37ded85d23abe40730f30`. No APK was requested or published.

## APK 1.0.220 to 1.0.221 included-work audit — 2026-11-26

- Compared the exact 1.0.220 publication commit `f8e59e4501` (baseline metadata: Web 466) against the 1.0.221 build/publication. The 1.0.221 workflow embeds the exact current `web-source/index.html` advertised by live `latest.json`: Web 478, not the older Web 466 bundle.
- Therefore the cumulative, retained Web changes after the 1.0.220 baseline are present in 1.0.221: Web 467 Calendar/Smart Reminder saved-entry AM/PM display; Web 468 header-button position/size controls; Web 469 Button Set Karein integration and independent Recently Deleted close-button behavior; Web 470 move-label wording; Web 472's verified rollback to Web 470 behavior; Web 473 move-hint/close-label cleanup; Web 474–477 Button Set Karein label sizing, boldness, alignment and vertical centering; and Web 478 resetting Move Mode OFF when the Me menu closes while preserving saved positions/sizes.
- Important exclusions: the Web 471 saved-position auto-restore behavior was explicitly rolled back by Web 472 and is not included. The temporary My Documents back-arrow alignment experiments before the rollback to Web 467 were also not retained in the final Web 478 source. These are not silently counted as included features.
- Native updater comparison: the only post-1.0.220 Android updater code change in this release is the Web downloader's explicit `Accept-Encoding: identity` header to prevent compressed-transfer bytes from causing SHA-256 mismatch. The existing native updater behavior, including keeping the Me menu open after Update Check refresh, was already present before the 1.0.220 baseline.
- Result: **all retained/published Check for Updates work after APK 1.0.220 is included in APK 1.0.221's Web 478 bundle**, plus the native SHA transport fix. Rolled-back experiments are excluded. This is a source/build audit, not a user phone-test PASS.

## Web 478 SHA mismatch investigation — 2026-11-26

- User reported that Web Update 478 repeatedly fails in Check for Updates with a SHA-256 mismatch. Do not mark Web 478 phone-test PASS until the user confirms successful installation and behavior.
- Verified current `web-source/index.html` and `diary-web/index.html` are now byte-identical; latest.json advertises Web 478 and the same source SHA-256.
- Found the prior Android build workflow was stale: it still required Web Update 466 and the old APK baseline, and a previous build attempt failed because the source/mirror were temporarily out of sync.
- Backups created before the updater/release-workflow change:
  - `backups/add_online_diary_updates-before-web-identity-1.0.221-2026-11-26.py`
  - `backups/build-diary-from-zip-before-web-identity-1.0.221-2026-11-26.yml`
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-web-identity-1.0.221-2026-11-26.md`
- Commit `e3b3e13dc82e795ad20896276c5426a155c7df0f` adds an explicit `Accept-Encoding: identity` request header to the Web bundle downloader and updates the guarded signed build pipeline for My Diary 1.0.221 / versionCode 220, based on installed 1.0.220 / code 219 and Web 478.
- GitHub Actions build run **45814673042** completed with **SUCCESS**. Signing keystore/alias validation, debug build, signed Release build, release verification/publication, signed APK upload, and APK upload all passed. The run published My Diary **1.0.221 / versionCode 220** to live latest.json with Web Update **478**. APK SHA-256: `20b3529674dc4a3375c480ca454b06113d67314f48f404d30bc6e7747591cf35`; Web HTML SHA-256: `04374ed939422483b0b832f95e442ddba530b90aa5bc7501460c515d11dd7530`. Update is available through the app's **Check for Updates**; no separate APK delivery. User phone test is still pending; do not mark Web 478 or APK 1.0.221 Phone Test PASS until user confirms.
- Delivery preference unchanged: publish only through the app's Check for Updates; do not send a separate APK file. Phone test remains pending.

## Project boundary — IMPORTANT

- This repository is the single home for **My Diary** project files, release automation, update metadata, and Diary documentation.
- Repository: `amuazzinxyz-ops/My-Diary-Updates`
- Branch: `main`
- Keep MUAZZIN website/app files, workflows, credentials, and deployments separate.
- Never create a second copy of an existing Diary workflow, project archive, signing key, or release setup without first checking this register and the actual repository.
- Before every future Diary task: read this register, then inspect the current files/workflows and latest commits. Update this register when anything moves or changes.

## Where Diary project items live

| Item | Repository location | Purpose / instruction |
|---|---|---|
| Android project archive | `Diary-Android-Project-v13 (6).zip` | Existing Diary Android project source archive. Inspect before creating or replacing a project. |
| Build from project ZIP workflow | `.github/workflows/build-diary-from-zip.yml` | Diary Android build workflow; expects the four signing secrets listed below for signed release builds. |
| Publish/update workflow | `.github/workflows/publish-diary-update.yml` | Diary release/update publishing automation. Inspect before changing release behavior. |
| APK release file (older filename) | `My-Diary.apk` | Existing APK file. Check version/signature before replacing. |
| APK release file (newer upload name) | `My-Diary.apk.apk` | Uploaded candidate for v1.0.90; double extension is accidental/undesirable. Do not delete until latest.json is safely corrected and release file is verified. |
| Update metadata | `latest.json` | App's update-check metadata. Its APK URL, version, and SHA-256 must match the actual published APK. |
| Project assets | `assets/` | Diary-only assets. Inspect before adding duplicates. |
| Build/helper scripts | `scripts/` | Diary-only helper scripts. Inspect before creating duplicates. |
| Project documentation | `docs/` | Audits and handover notes. Add future project maps, test reports, and release notes here. |
| Main repository instructions | `README.md` | Project boundary, release requirements, and links to handover docs. Keep it current. |

## Four Android signing secrets — repository Actions secrets

These are **GitHub repository secrets**, not folders and not files in the repository. Never put their values in a commit, README, issue, log, chat, or plain-text documentation.

Required names:

1. `DIARY_KEYSTORE_BASE64`
2. `DIARY_KEY_ALIAS`
3. `DIARY_KEY_PASSWORD`
4. `DIARY_STORE_PASSWORD`

Required final location:  
`amuazzinxyz-ops/My-Diary-Updates` → Settings → Secrets and variables → Actions.

Migration status at last check (2026-11-06):
- The My-Diary-Updates build workflow reported the signing secrets were missing; signed release steps were skipped.
- The four existing secrets were reported to be present in `Muazzin-New`.
- Therefore, **do not delete the four secrets from Muazzin-New yet**.
- Transfer the exact existing values into the four names above in My-Diary-Updates. Do not generate a new keystore or change alias/passwords.
- Then run a signed release build and verify that the signing certificate fingerprint matches the trusted existing Diary certificate:
  `23A4E93F3C7911DCE18389EA583548700C6AD6A3759707F1CD222D07E2408B5A`
- Only after the Diary repository has a successful signed build and the certificate match is verified may the four old secrets be deleted from Muazzin-New.
- The connected GitHub integration used for this work can inspect repository files/workflows but cannot read or write GitHub Secrets. Never claim the secret transfer is complete unless a verified workflow run proves it.

## Known app identity and release safety

- Android package: `com.personal.diaryapp`
- Last user-confirmed installed app: versionName `1.0.90`, versionCode `90`.
- Trusted signing certificate fingerprint: `23A4E93F3C7911DCE18389EA583548700C6AD6A3759707F1CD222D07E2408B5A`.
- Preserve the same signing certificate for all future in-place app updates. Never ask the user to uninstall the installed app as a routine update step.
- Never publish a release until package, version, signature, checksum, metadata URL, and install/update behavior are checked.

## Known release metadata caution

At the last inspection, `latest.json` pointed to `My-Diary.apk.apk` for version 1.0.90, while the repository also contained `My-Diary.apk` (older v1.0.89 file). The double extension and the metadata/file alignment need a deliberate cleanup. Do not delete either APK or change latest.json casually; first verify which exact APK is published and update the metadata consistently.

## Next actions, in safe order

1. Transfer the same four existing signing secret values into My-Diary-Updates Actions secrets.
2. Run the Diary build workflow and verify successful signed release + trusted certificate fingerprint.
3. Verify the release APK checksum and ensure latest.json points to the correct APK filename/version.
4. Test update detection/install on the user's Android device when a new release is available.
5. Only then remove the four Diary secrets and any Diary-only temporary workflow/branch from Muazzin-New, after confirming no Diary workflow there is still needed.
6. Keep MUAZZIN main website/app repository and deployment untouched.

## Rule for future assistants

The user has repeatedly requested strict separation: **MUAZZIN path separate; My Diary path separate.** Start by reading this register and inspecting the existing Diary repository. Reuse what is already here. Do not ask the user to re-upload or recreate something that already exists. Do not claim an action was completed unless the repository/workflow/device evidence confirms it.
