# My Diary Project Register (Permanent Handover)

Last reviewed: 2026-11-06

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
