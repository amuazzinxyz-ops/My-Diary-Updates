# My Diary Project Register (Permanent Handover)

Last reviewed: 2026-11-06

## Project boundary — IMPORTANT

- This repository is the home for **My Diary** project files, release automation, update metadata, and Diary documentation.
- Repository: `amuazzinxyz-ops/My-Diary-Updates`
- Branch: `main`
- Keep MUAZZIN website/app files, workflows, credentials, and deployments separate.
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

At the last inspection, `latest.json` pointed to `My-Diary.apk.apk` for version 1.0.90, while the repository also contained `My-Diary.apk` (older v1.0.89 file). The double extension and the metadata/file alignment need a deliberate cleanup. Do not delete either APK or change latest.json casually; first verify which exact APK is published and update the metadata consistently.

## Rule for future assistants

The user wants a clear map of where existing Diary files and settings are, and wants **MUAZZIN kept separate from My Diary**. Start by reading this register and inspecting the existing Diary repository. Reuse what is already present. Do not ask the user to re-upload or recreate something that already exists. Do not claim an action was completed unless repository/workflow/device evidence confirms it.
