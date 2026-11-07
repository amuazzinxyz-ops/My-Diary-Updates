# My Diary Project Register (Permanent Handover)

Last reviewed: 2026-11-07

## Project boundary — IMPORTANT

- This repository is the home for **My Diary** project files, release automation, update metadata, and Diary documentation.
- Repository: `amuazzinxyz-ops/My-Diary-Updates`
- Branch: `main`
- **All future My Diary work must be done only in the My-Diary-Updates repository / Diary section.** This includes every Diary code change, Android build, APK release, update workflow, documentation, assets, credentials, and troubleshooting.
- Never do Diary work in the MUAZZIN website, the MUAZZIN repository (`amuazzinxyz-ops/Muazzin-New`), or any MUAZZIN workflow/deployment. Do not add Diary files, code, workflows, or settings there.
- Keep MUAZZIN website/app files, workflows, credentials, and deployments completely separate.
- Do not create a second copy of an existing Diary workflow, project archive, signing key, or release setup without first checking this register and the actual repository.
- Before every future Diary task: read this register, then inspect the current files/workflows and latest commits. Update this register when anything changes.

## Where Diary project items live

| Item | Repository location | Purpose / instruction |
|---|---|---|
| Android project archive | `Diary-Android-Project-v13 (6).zip` | Existing Diary Android project source archive. Inspect before creating or replacing a project. |
| Build from project ZIP workflow | `.github/workflows/build-diary-from-zip.yml` | Diary Android build workflow. |
| Publish/update workflow | `.github/workflows/publish-diary-update.yml` | Diary release/update publishing automation. Inspect before changing release behavior. |
| APK release file (older filename) | `My-Diary.apk` | Existing APK file. Check version/signature before replacing. |
| APK release file (newer upload name) | `My-Diary.apk.apk` | Uploaded candidate for v1.0.90; double extension is accidental/undesirable. Do not delete until latest.json is safely corrected and release file is verified. |
| Update metadata | `latest.json` | App's update-check metadata. Its APK URL, version, and SHA-256 must match the actual published APK. |
| Project assets | `assets/` | Diary-only assets. Inspect before adding duplicates. |
| Build/helper scripts | `scripts/` | Diary-only helper scripts. Inspect before creating duplicates. |
| Project documentation | `docs/` | Audits and handover notes. Add future project maps, test reports, and release notes here. |
| Main repository instructions | `README.md` | Project boundary, release requirements, and links to handover docs. Keep it current. |

## Four Android signing secrets — current location

These are **GitHub Actions repository secrets**, not folders and not files in the repository. Their values are private and are not visible in repository files. Never put their values in a commit, README, issue, log, chat, or plain-text documentation.

The four existing secret names are:

1. `DIARY_KEYSTORE_BASE64`
2. `DIARY_KEY_ALIAS`
3. `DIARY_KEY_PASSWORD`
4. `DIARY_STORE_PASSWORD`

**Current recorded location:**  
`amuazzinxyz-ops/Muazzin-New` → Settings → Secrets and variables → Actions → Repository secrets.

**Important:** Keep these four existing Diary signing secrets at that location. No transfer or recreation is planned. Do not delete, rename, regenerate, or change their values. The assistant's connected GitHub integration can inspect repository files/workflows but cannot read secret values.

Trusted existing Diary signing certificate fingerprint:
`23A4E93F3C7911DCE18389EA583548700C6AD6A3759707F1CD222D07E2408B5A`

## Known app identity and release safety

- Android package: `com.personal.diaryapp`
- Last user-confirmed installed app: versionName `1.0.90`, versionCode `90`.
- Trusted signing certificate fingerprint: `23A4E93F3C7911DCE18389EA583548700C6AD6A3759707F1CD222D07E2408B5A`.
- Preserve the same signing certificate for all future in-place app updates. Never ask the user to uninstall the installed app as a routine update step.
- Never publish a release until package, version, signature, checksum, metadata URL, and install/update behavior are checked.

## Known release metadata caution

At the 2026-11-07 inspection, `latest.json` declared version 1.0.90 / versionCode 90, pointed to `My-Diary.apk.apk`, and declared SHA-256 `3850b28ceb48794f6712f8a003b7be5ae7c1d257b08c703f22bc684a0c2546d5`. The existing `.github/workflows/publish-diary-update.yml` validates the canonical URL ending in `My-Diary.apk`, so the current metadata URL and workflow rule do not agree. The APK binary at the current double-extension URL has not been independently downloaded and re-hashed in this check. The older `My-Diary.apk` was recorded as v1.0.89. A repository directory listing on 2026-11-07 confirms both files exist: `My-Diary.apk` is 1,942,255 bytes and `My-Diary.apk.apk` is 1,941,678 bytes. The latter size exactly matches the extracted v1.0.90 candidate APK size recorded in the signed-build handover, but its SHA-256 has not been recomputed from the repository binary in this check; matching size alone is not cryptographic verification. Do not delete either APK or change `latest.json` until the exact repository APK, checksum, canonical URL, package/version, and trusted signing certificate are reconciled. README and signed-build handover were corrected on 2026-11-07 to distinguish the last independently verified published release (v1.0.89) from the v1.0.90 signed build candidate and its unresolved feed state. The alternate publish workflow also requires a committed `source-artifact-url.txt` containing a temporary ZIP URL from its allow-listed host; a direct check on 2026-11-07 returned 404 for that file, so this route is not currently staged. It additionally requires a ZIP containing the canonical `My-Diary.apk` plus a matching `latest.json`; do not create or trigger it without a verified signed package and an authorized artifact URL. A further build-version mismatch was confirmed from the `Diary-original-Android-source` artifact of Diary Actions run `42362746781`: its `app/build.gradle.kts` declares `versionCode = 1` and `versionName = "1.0"`; `scripts/apply_diary_identity.py` changes package/label/icon only, and `build-diary-from-zip.yml` contains no step that updates the Gradle version. The source integrity verifier passed for that extracted artifact, but this means the dedicated ZIP workflow must not be treated as a valid v1.0.90 release builder without a controlled versioning correction. Do not change version to 91 or publish anything until the intended next version and installed-app update compatibility are explicitly reconciled.

## Latest focused corrections — 2026-11-07

- Diary PIN address-autofill correction is documented in `docs/PIN_ADDRESS_AUTOFILL_FIX_2026-11-07.md`.
- Close-button × glyph alignment correction is documented in `docs/CLOSE_BUTTON_GLYPH_FIX_2026-11-07.md`.
- Both corrections are applied by the existing `scripts/add_diary_app_actions.py` during the ZIP-based build; the original project ZIP remains unchanged.
- Latest combined debug build succeeded in Actions run `42362746781` (commit `1136583f0a689a29aedf938c1ff34d89ca8c1c58`). Its APK was downloaded and inspected: packaged HTML contains the close-glyph rule and both PIN autofill protections. APK SHA-256: `7ad638283ce7f9a4f0d24ac01bd0f5fa74dc46ebf4cb1ff26c7798202d7bbaf2`.
- The run did not produce a signed Release APK because the dedicated Diary repository workflow did not receive the four existing signing secrets. Do not publish the debug APK or change `latest.json` until a trusted signed build is available.
- Android phone visual testing and PIN autofill behavior testing remain pending.

## Rule for future assistants

The user wants a clear map of where existing Diary files and settings are, and wants **MUAZZIN kept separate from My Diary**. Start by reading this register and inspecting the existing Diary repository. Reuse what is already present. Do not ask the user to re-upload or recreate something that already exists. Do not claim an action was completed unless repository/workflow/device evidence confirms it.

## Reusable instruction for every new Diary task

The user does not need to repeat the project rules. For every new My Diary request, follow these instructions automatically:

- Work only in `amuazzinxyz-ops/My-Diary-Updates` and its Diary project files/workflows. Never use the MUAZZIN website or `amuazzinxyz-ops/Muazzin-New` for Diary work.
- First read this register, inspect the current repository files and relevant workflow, and identify the current working version before editing.
- Preserve all existing Diary features, screens, design, colors, buttons, data, app identity, signing setup, and update behavior unless the user explicitly asks to change a particular item.
- Make only the requested new feature or correction. Do not rewrite, remove, rename, or change unrelated code or files.
- Check whether the requested feature or fix already exists before adding another copy. Reuse existing code and project structure where appropriate.
- After editing, run the available relevant checks/builds. Report exactly what changed, which files changed, what checks passed/failed, and anything not tested. Never claim a build or phone test succeeded unless verified.
- Keep the existing Android package and trusted signing certificate unchanged for updates. Never generate a new signing key or change signing credentials without explicit permission.
- Keep the project register and relevant handover notes updated when project structure, versions, or important decisions change.
- If an essential detail is missing, ask only the one necessary question before making a risky or ambiguous change. Do not make assumptions that could alter existing behavior.

### Short message the user can send

For a new feature:
“MY DIARY — Naya kaam: [yahan feature ka naam aur kya karna hai likhein]. Register ke sab rules follow karo. Pehle current Diary project check karo, sirf ye feature add karo, purana kuch mat bigaadna. Test karke batao kya complete hua aur kya baaki hai.”

For a correction:
“MY DIARY — Sudhar: [yahan problem aur expected result likhein]. Register ke sab rules follow karo. Pehle problem ka asli reason check karo, sirf isi ko fix karo, baaki design/features/code ko mat chhedna. Test karke result batao.”

For a general continuation:
“MY DIARY — Register padhkar My-Diary-Updates repository mein Diary ka kaam aage badhao. MUAZZIN website/repository ko bilkul mat chhedna.”

