# My Diary Project Register (Permanent Handover)

Last reviewed: 2026-11-26

## Current release state — 2026-11-26

- Latest published web version: **484**. Web 484 restores the Diary heading **Me** button's existing size slider in **Button Set Karein**. The fixed 36px width, height, padding, and font-size constraints are removed only from the Me button so its original 75%–160% slider can resize it; existing slider JavaScript is unchanged. The × button, **Position badalne ke liye** control, saved positions, and all other functions are unchanged. **Phone Test pending.** Web 483 removes the **🌈 Do Rang (Gradient)** choice only from the **🖼️ Photo Lagayein** chooser; gradient choices in Note Cover Photo and Details Image remain available and unchanged. **Phone Test PASS — user confirmed on 2026-11-26.** Personal Calendar category/date/time badges remain compact and wrap only when needed. **Phone Test PASS — user confirmed on 2026-11-26.**
- Web 481 source and mirror are byte-identical. SHA-256: `a6dc79b385696dd24cd42767db10cffef7bfd733dfd87a9d0a6f92ddeec443c8`; `latest.json` declares `webVersion: 481` with the same SHA-256.
- Web 479 remains the previous known-good release. Its custom category option, save, and edit behavior are **Phone Test PASS — user confirmed on 2026-11-26**.
- Web 478 remains the previous known-good release. It resets header-button Move Mode to OFF whenever the Me menu closes while preserving saved button positions and sizes. **Phone Test PASS — user confirmed on 2026-11-26 after installing APK 1.0.221 over APK 1.0.220 and confirming Check for Updates PASS.**
- Web 477 remains the previous known-good release and rollback target. **Phone Test PASS — Web Update 477 confirmed by the user on 2026-11-26.** The “Button Set Karein” label is now vertically centered; 16px bold size and left alignment remain correct.
- Web 476 history: increased the label from 15px to 16px, retaining bold weight 950 and left alignment. Phone test pending.
- Web 476 source and mirror were byte-identical. SHA-256: `ef234ad7e8b1182bf2368c332e506b3e87c89571e2d92c5010f0261b7900938e`.
- Web 475 history: the label was 15px, left-aligned, with bold weight 950; phone test pending.
- Web 475 source and mirror were byte-identical. Published Web 475 SHA-256: `070d762968501ae0f3a2fd8a57ef0cd7bee7eedb0fbfc3192e8018b1314a4fb0`; its release metadata was published before Web 476.
- **Phone Test PASS — Web Update 473 confirmed by the user on 2026-11-26.** Web 473 removed only the Move Mode instruction text inside Button Set Karein and changed its inner close button label from “Band Karein” to “Band”.
- Web 472 rollback and its user-confirmed Phone Test PASS remain in release history. Web 472 rolled back the Web 471 saved-position reload change and restored the exact Web 470 source content.
- Web 469 added **Button Set Karein** inside the existing Me menu. Web 470 only shortened its move-button label to “Position badalne ke liye”. Web 471's saved-position reload change was rolled back in Web 472; Web 472 used the exact Web 470 source content.
- Recently Deleted fullscreen layout remains isolated: its × button retains the original top-right position and default 36px size even when a custom heading-button layout is saved.
- Latest APK: **versionName 1.0.221**, **versionCode 220**, SHA-256 `20b3529674dc4a3375c480ca454b06113d67314f48f404d30bc6e7747591cf35`. **Phone Test PASS — installed successfully as an update over APK 1.0.220; app Check for Updates also PASS, user-confirmed 2026-11-26.**

## Web Update 486 — resize the Me button itself, not its text — 2026-11-26

- Corrected the previous interpretation: the size slider must change the **actual Me button box**, not the text size. The Me label stays at its original 13px; the button width, height, min-width, max-width, min-height, and max-height now scale together from 75% to 160%.
- At 100%, the button remains the original 36×36px. Its existing appearance, label, colour, 3D styling, and action are retained. The × button, position behavior, and all other controls/functions were not changed.
- Updated `web-source/index.html` and `diary-web/index.html`; both are byte-identical with Git blob SHA `b1674e673f6ee9a5bb25028a197031a3ed82f6c8`.
- `latest.json` declares **webVersion 486** and Web SHA-256 `964ade81bf4d864ef480c052591c5b842b66a28d68d9b4bc9eb9cf842cc8fbf5`. APK remains **1.0.221 / versionCode 220**; no APK was built.
- Commits: source `7c455981ddf1fda5d71702f12252561f628d179f`; mirror `2b90462da541c25cc04f1c32e81dad6a238445ca`; metadata `7a4348ee858ec94a70083aa9d4c7e450d963b981`.
- Delivery is through Check for Updates. **Phone Test pending** until user confirmation.

## Web Update 485 — preserve Me button's original size and restore slider — 2026-11-26

- Corrected the Web 484 visual regression: the Diary Me button keeps its original **36×36px outer box at 100%**. The six 36px width/height declarations are restored as normal CSS declarations (not `!important`), so they preserve the default box without blocking the existing JavaScript size control.
- The existing Me-button slider code remains unchanged: it still adjusts the Me button's font size and padding from 75% to 160%. No change was made to any other button, control, position behavior, or feature.
- Updated `web-source/index.html` and `diary-web/index.html`; both now have identical Git blob SHA `baedd8d22fb0632866b5c21b78afed080943d8d9` (byte-identical).
- `latest.json` now declares **webVersion 485** and Web SHA-256 `b0a83f776187d4d58a6f0aecc40d093f633da3d3f5307e48770c7eaf6b6a3c36`. APK remains **1.0.221 / versionCode 220**; no APK was built or changed.
- Commits: source `12c82cf8e92f05aeb4b71e8dd69175a700d75326`; mirror `278c6e2a0f122088aab12bbee0ff936533629054`; metadata `406f92a7a222afb8d93701eb06c24ffa0479a079`.
- Repository and metadata updated for Check for Updates. **Phone Test pending**; do not mark PASS until the user confirms.

## Web Update 484 — restore Diary Me button size slider — 2026-11-26

- Confirmed the exact regression in live source: `diary-me-button-36px` CSS applied fixed `width`, `min/max-width`, `height`, `min/max-height`, `padding`, and `font-size` with `!important`. This overrode the existing `setupDiaryHeaderButtonLayout()` JavaScript that scales the Me button's font size and padding when the size slider changes.
- Removed only those fixed sizing declarations from the Me button CSS. Kept flex alignment, box sizing, line height, and nowrap styling. Existing slider logic and its 75%–160% range are unchanged. The × button logic and the **Position badalne ke liye** action are untouched.
- Source and mirror are byte-identical. Git blob SHA: `6da54f114619082b21ec0a905c849d204837848e`. Verified UTF-8 SHA-256: `4d0eb125e0e1314c571fba2949278574f496855939fc9bed86081cd2f99afafc`. `latest.json` declares `webVersion: 484` with the same SHA-256; APK metadata remains version 1.0.221 / versionCode 220, unchanged.
- Backups: `backups/2026-11-26-before-me-size-slider-fix-web-source-index.html`, `backups/2026-11-26-before-me-size-slider-fix-diary-web-index.html`, `backups/2026-11-26-before-me-size-slider-fix-docs-PROJECT_MAP_AND_SECRETS_REGISTER.md`, and `backups/2026-11-26-before-me-size-slider-fix-latest.json`.
- Source commit: `562e67d53de78f15388e5ec843b84bd8f15f925c`; mirror commit: `60346b206d112782b2d3957f6553a0c426a19112` (the source/mirror update is byte-identical); metadata commit: `a5a5a69acc98451fddb5611f37b34e2497ca51f3`.
- No APK created. Delivery is through the app's **Check for Updates**. Repository/metadata verification PASS; **Phone Test pending** until user confirms.

## Web Update 483 — remove Gradient option only from Photo Lagayein — 2026-11-26

- In `attachDiaryColourChooser`, the 🌈 Do Rang (Gradient) button is now appended only when `kind !== 'Photo'`. Therefore it is hidden only in the 🖼️ Photo Lagayein chooser.
- The Note Cover Photo and Details Image chooser paths still show the existing Gradient option. The Photo chooser's image-selection behavior and all other existing options/behavior are unchanged. No other screens, settings, saved data, or app functions were changed.
- Source and mirror are byte-identical; both Git blob SHA values: `cc979a16999f836ca66d54a27a80818c6b43bae5`. Verified Web 483 SHA-256: `ff59e34c068dc0481b594813c39a68a3ef4f0db157e1b9f04d09105126e387ec`. Live `latest.json` now declares `webVersion: 483` and the same SHA-256.
- Backups made before editing: `backups/web-source-before-photo-gradient-removal-2026-11-26.html` and `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-photo-gradient-removal-2026-11-26.md`.
- Source commit: `038f9ff5beb585e9c6d3b0bf95878ea5a4a59651`; mirror commit: `40eca9660de6e66dc2761f3f12acdc49b5141f17`; metadata commit: `bb3162f7f1f2d13a38109309b4b6e74c2a8af312`.
- No APK created. Delivery is through the app's Check for Updates. **Phone Test PASS — user confirmed on 2026-11-26.**

## APK 1.0.220 to 1.0.221 included-work audit — 2026-11-26

- Compared the exact 1.0.220 publication commit `f8e59e4501` (baseline metadata: Web 466) against the 1.0.221 build/publication. The 1.0.221 workflow embeds the exact current `web-source/index.html` advertised by live `latest.json`: Web 478, not the older Web 466 bundle.
- Therefore the cumulative, retained Web changes after the 1.0.220 baseline are present in 1.0.221: Web 467 Calendar/Smart Reminder saved-entry AM/PM display; Web 468 header-button position/size controls; Web 469 Button Set Karein integration and independent Recently Deleted close-button behavior; Web 470 move-label wording; Web 472's verified rollback to Web 470 behavior; Web 473 move-hint/close-label cleanup; Web 474–477 Button Set Karein label sizing, boldness, alignment and vertical centering; and Web 478 resetting Move Mode OFF when the Me menu closes while preserving saved positions/sizes.
- Important exclusions: the Web 471 saved-position auto-restore behavior was explicitly rolled back by Web 472 and is not included. The temporary My Documents back-arrow alignment experiments before the rollback to Web 467 were also not retained in the final Web 478 source. These are not silently counted as included features.
- Native updater comparison: the only post-1.0.220 Android updater code change in this release is the Web downloader's explicit `Accept-Encoding: identity` header to prevent compressed-transfer bytes from causing SHA-256 mismatch. The existing native updater behavior, including keeping the Me menu open after Update Check refresh, was already present before the 1.0.220 baseline.
- Result: **all retained/published Check for Updates work after APK 1.0.220 is included in APK 1.0.221's Web 478 bundle**, plus the native SHA transport fix. Rolled-back experiments are excluded. **User confirmed Phone Test PASS on 2026-11-26** after installing APK 1.0.221 over 1.0.220 and confirming Check for Updates PASS.

## Handover summary for next task — APK 1.0.221

- **Web Update 478 — Move Mode fix:** whenever the Me menu closes (outside tap or navigation to Calendar notes, Private Locker, Documents/Memories, or another feature page), header-button Move Mode resets to OFF. Saved button positions and sizes remain unchanged. **Phone Test PASS.**
- **Native updater SHA-256 fix:** Web bundle downloader requests `Accept-Encoding: identity` so the downloaded bytes match the published SHA-256. **Phone Test PASS** through successful Check for Updates.
- **APK 1.0.221 / versionCode 220:** installed over APK 1.0.220; Check for Updates PASS; both fixes above are included. **Phone Test PASS — user confirmed 2026-11-26.**
- Next task must be added below this completed release history; do not reopen or alter these PASS items unless a new issue is reported.

## Permanent release safety rule — SHA-256 verification (effective 2026-11-26)

For every future Web Update, complete these checks before publishing. Never type or reuse a guessed or stale checksum:

1. Read the current Master Register, live `latest.json`, actual source HTML, mirror HTML, and latest successful release before editing.
2. Make only the requested change and create a dated backup before risky edits.
3. Calculate SHA-256 directly from the exact final UTF-8 file bytes using a trusted SHA-256 implementation.
4. Confirm source HTML and mirror HTML are byte-identical, then independently calculate and compare both SHA-256 values.
5. Set `latest.json` `webVersion` and `webSha256` to the verified version and exact calculated hash. The metadata hash must equal both source and mirror hashes.
6. After committing, re-fetch the published source, mirror, and `latest.json` from `main`; recalculate/compare hashes and confirm live metadata matches the published files.
7. If any comparison fails, stop. Do not publish or report the update as ready; correct the mismatch first.
8. Record the verified version, hashes, backup, and commit in this register. Keep repository verification and phone testing separate; mark Phone Test PASS only after the user confirms the update on their device.

This is a mandatory release gate for every future web update. APK creation is not required for a web-only update unless the user explicitly asks.

## Web Update 482 — Diary Me button 36 × 36 px — 2026-11-26

- Set only `#diaryDiaryMeBtn` to a fixed 36 × 36 px border-box, matching the Diary heading × button's 36 × 36 px outer dimensions.
- Kept the “Me” label at 13 px, centered with no internal padding; its text is not reduced or hidden. Existing gold/purple 3D styling, position/move controls, and click behavior remain unchanged.
- No other UI, data, or app behavior changed. No APK created; delivery is through Check for Updates.
- Source and mirror are byte-identical. Web 482 SHA-256: `fa46ca5d31ac99632c5da07ebbc884915e86e816be94a12c5d4641aaffdb8453`; `latest.json` declares `webVersion: 482` with the same SHA-256.
- Backup: `backups/web-source-index-before-me-button-36px-2026-11-26.html`.
- **Phone Test PASS — user confirmed on 2026-11-26.**

- **Web 482 SHA-256 correction — 2026-11-26:** Repeated phone SHA mismatch was traced to stale/wrong `latest.json` checksum, not the APK downloader. Independently hashed the exact UTF-8 bytes from `web-source/index.html`; SHA-256 is `fa46ca5d31ac99632c5da07ebbc884915e86e816be94a12c5d4641aaffdb8453`. Confirmed `diary-web/index.html` is byte-identical and has the same hash. The calculated Git blob SHA also matches GitHub's blob SHA, confirming the bytes used for the hash. Updated only `latest.json` `webSha256` to the verified value; APK was not built. **Phone Test PASS — user confirmed on 2026-11-26 after the SHA-256 metadata correction.**

## Web Update 481 — Personal Calendar date/time badges inline fit — 2026-11-26

- Adjusted only the Calendar saved-entry badge spacing: compact padding, font size, and gaps allow a short custom category such as “Dawat”, date, and time to remain together on the same line whenever they fit. Wrapping remains available when the row genuinely has insufficient width.
- No changes to saved entries, category values, date/time data, editing, or reminder behavior. No APK created; delivery is through Check for Updates.
- Source and mirror are byte-identical. Web 481 SHA-256: `a6dc79b385696dd24cd42767db10cffef7bfd733dfd87a9d0a6f92ddeec443c8`.
- Backup: `backups/web-source-index-before-calendar-badge-inline-2026-11-26.html`.
- **Phone Test PASS — user confirmed on 2026-11-26.** The user verified that the compact category/date/time badges now stay together when there is room and wrap when needed.

## Web Update 480 — Personal Calendar category badge wrapping — 2026-11-26

- Changed only the Personal Calendar saved-entry category badge layout: its width follows the category label; when the current line has insufficient room, the whole badge wraps to the next line. If enough room exists, it stays on the same line.
- Existing Birthday, Anniversary, Zaroori Din, and Custom labels, date/time badges, saved entries, editing, and reminder behavior are unchanged. No APK was created; this is delivered through Check for Updates.
- Web source and mirror are byte-identical. Published Web Update metadata: **480**; SHA-256: `876419a6c19ed734663b3c8b9bf651669bb320c73aee9f0a5c5f03b04c5a9355`.
- Backup before editing: `backups/web-source-index-before-calendar-badge-wrap-2026-11-26.html`.
- **Phone Test pending — awaiting user confirmation.**

## Web Update 479 — Personal Calendar custom category — 2026-11-26

- Added **✍️ Apni Kism (Custom)** as a fourth Personal Calendar type. Selecting it reveals a required category-name field; the saved Calendar badge displays the user's own category and editing restores it.
- Existing Birthday, Anniversary, and Zaroori Din options and previously saved Calendar records remain unchanged. Custom category is stored separately as `customType`; existing reminder, repeat, alarm, date, and details fields are preserved.
- Web source and mirror are kept byte-identical. Published Web Update metadata: **479**; SHA-256: `4c3c41e8876c3915210d315fb97b4fef18c19ed81245789e00bb6fb55c34e472`.
- Backup before editing: `backups/web-source-index-before-calendar-custom-category-2026-11-26.html`.
- **Phone Test PASS — user confirmed on 2026-11-26.** Personal Calendar custom category option, saving, and editing were phone-tested and passed.

## Web 478 SHA mismatch investigation — 2026-11-26

- User reported that Web Update 478 repeatedly fails in Check for Updates with a SHA-256 mismatch. **Resolved and Phone Test PASS on 2026-11-26:** user confirmed APK 1.0.221 installed over 1.0.220 and Check for Updates passed.
- Verified current `web-source/index.html` and `diary-web/index.html` are now byte-identical; latest.json advertises Web 478 and the same source SHA-256.
- Found the prior Android build workflow was stale: it still required Web Update 466 and the old APK baseline, and a previous build attempt failed because the source/mirror were temporarily out of sync.
- Backups created before the updater/release-workflow change:
  - `backups/add_online_diary_updates-before-web-identity-1.0.221-2026-11-26.py`
  - `backups/build-diary-from-zip-before-web-identity-1.0.221-2026-11-26.yml`
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-web-identity-1.0.221-2026-11-26.md`
- Commit `e3b3e13dc82e795ad20896276c5426a155c7df0f` adds an explicit `Accept-Encoding: identity` request header to the Web bundle downloader and updates the guarded signed build pipeline for My Diary 1.0.221 / versionCode 220, based on installed 1.0.220 / code 219 and Web 478. The delivered APK also includes Web 478's Move Mode fix: closing the Me menu (outside tap or navigation) automatically turns Move Mode OFF without changing saved button positions or sizes.
- GitHub Actions build run **45814673042** completed with **SUCCESS**. Signing keystore/alias validation, debug build, signed Release build, release verification/publication, signed APK upload, and APK upload all passed. The run published My Diary **1.0.221 / versionCode 220** to live latest.json with Web Update **478**. APK SHA-256: `20b3529674dc4a3375c480ca454b06113d67314f48f404d30bc6e7747591cf35`; Web HTML SHA-256: `04374ed939422483b0b832f95e442ddba530b90aa5bc7501460c515d11dd7530`. Update is available through the app's **Check for Updates**; no separate APK delivery. **Phone Test PASS confirmed by user on 2026-11-26**; do not leave this release marked pending.
- Delivery preference unchanged: publish only through the app's Check for Updates; do not send a separate APK file. **Phone Test PASS confirmed by user on 2026-11-26.**

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
