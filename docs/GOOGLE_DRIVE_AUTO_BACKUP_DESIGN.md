# My Diary — Google Drive automatic backup design

Status: design/audit only; no application code is changed by this document.

## Goals

- Each installation authorizes and writes only to the Google account selected by that user.
- No app-owner/service-account Drive storage, backend server, broad Drive permission, or upload of plaintext diary content.
- One current backup object per Google account in that account's app-private Drive data area; update the existing object instead of creating duplicates.
- Explicit opt-in, visible connection/backup status, last successful backup time, retry state, restore action, and clear recovery-passphrase warning.
- Existing manual JSON export/import remains available and backward-compatible.

## Native authorization and Drive

- Android Google Identity Services AuthorizationClient; request only `https://www.googleapis.com/auth/drive.appdata`.
- Handle consent/permission resolution through Android Activity Result APIs. Re-request authorization when needed; access tokens are short-lived and must not be stored as permanent credentials.
- Drive v3 REST calls with the user's access token:
  - list `files` in `appDataFolder` by the fixed app backup filename;
  - create one file with `parents: ["appDataFolder"]` if absent;
  - update the existing file's media content if present.
- Use the account chosen by the user; if consent is revoked or account selection changes, stop and show the user which account needs authorization.
- The appDataFolder is hidden from ordinary Drive browsing and only this app can access it. Restore/status therefore must be implemented inside My Diary. This folder is not the same as a visible Drive folder.
- Do not add `drive`, `drive.readonly`, or other broad scopes. No server auth code or refresh-token backend is planned.

## Complete local-data inventory (must be confirmed against actual runtime schema before release)

| Source | Data | Backup handling |
|---|---|---|
| localStorage `diary_personal_notes_v1` | Notes, photos/text/layout, note lock fields | Include all valid records |
| localStorage `diary_personal_notes_trash_v1` | Deleted Notes / Trash | Include; do not silently omit |
| IndexedDB `diary_me_features_v1`, object store `records` | My Documents, My Memories, Personal Calendar, Smart Reminder | Include all record kinds and binary attachments |
| IndexedDB `diary_private_locker_v1`, stores `entries` and `meta` | Legacy encrypted Private Locker entries and wrapped key/config | Preserve as opaque ciphertext/config; never decrypt or rewrite during backup |
| IndexedDB `diary_diary_safety_v1`, store `snapshots` | Redundant local safety copy of Notes and Trash | Not required as a second copy if primary Notes + Trash are captured; use only for recovery if primary store is invalid |
| localStorage security values | Diary PIN, Pattern, fingerprint-enabled setting, recovery-name salt/hash, Me-section PIN/recovery values, Note Lock embedded fields | Include only inside the outer encrypted payload; preserve exact values |
| localStorage preferences | language, theme/custom colour, note font, World Clock cities/favourites and other persistent app preferences | Include after full key audit; exclude transient UI/session state |

Before coding, inspect every persistent key and every IndexedDB record kind at the current Web 362 baseline. Do not assume the list above is exhaustive. Never include access tokens, OAuth credentials, device identifiers, temporary dialogs, or session-only UI state.

## Encryption and cross-device recovery

- The entire serialized backup is encrypted before any network request. Plain JSON, Note PIN/recovery values, photos, attachments, and old Locker metadata must never be sent to Drive.
- Proposed portable encryption: random 256-bit data-encryption key (DEK); AES-256-GCM for the compressed backup payload; PBKDF2-HMAC-SHA256-derived key-encryption key (KEK) with a random 16-byte salt wraps the DEK; every GCM encryption uses a fresh random 12-byte nonce. Store algorithm names, KDF parameters, salt, nonce, schema version and wrapped DEK with the ciphertext. Validate KDF cost on representative Android devices before finalizing the iteration count.
- For same-device unattended uploads, keep a local copy of the DEK encrypted by an Android Keystore AES key. The portable passphrase-wrapped DEK remains in the cloud envelope. Keystore key is device-local and must never be the only recovery path.
- On another device or after reinstall, require the user's recovery passphrase to unwrap the DEK. Do not upload or store the passphrase. Warn clearly that losing it makes encrypted cloud data unrecoverable.
- Use a versioned envelope, authenticated metadata/AAD, integrity checks, strict size limits, and atomic local writes. Never log tokens, passphrases, decrypted JSON, note text, or attachment data.

## Snapshot, automatic scheduling and restore

- Build one canonical snapshot collector shared by the manual export and cloud backup where practical; do not fork divergent data schemas. Keep the current manual JSON version 3 reader/writer compatible.
- A save in any backed-up store marks the snapshot dirty. Debounce frequent edits, serialize only after successful storage commits, encrypt locally, and persist the encrypted pending snapshot before queuing network work.
- Use unique WorkManager work with network-connected constraints and exponential backoff. On app launch/resume, reconcile pending dirty state and retry. If Google consent/account resolution requires UI, retain the encrypted pending snapshot and request authorization on the next foreground session; do not discard it.
- Do not promise background upload while the app is closed until the Worker can obtain a valid token silently on supported Android versions and the consent-revoked path has been tested.
- Restore is opt-in. Download ciphertext, verify envelope/schema/size, ask for passphrase if local DEK is unavailable, authenticate/decrypt, parse and validate every store, then stage the full restore before committing. Merge records by stable ID where appropriate; preserve existing records and never reset current PIN/locks. Keep alarms/schedulers consistent with existing restore functions. On any failure, leave current app data untouched.
- Maintain one backup file; use a stable name and update file content. Never delete a prior cloud backup until a replacement upload has succeeded and been verified.

## Acceptance checks

1. Static checks: exact scope, no broad scopes, no service account, no secrets in source, no plaintext upload, correct file create/update/list behavior, one-file logic, encryption/version/AAD validation, size limits, retries and redacted logs.
2. Data tests: round-trip every store including Trash, attachments, lock settings and opaque Locker data; old manual JSON v2/v3 and legacy Notes-only restore still works; unknown fields/versions fail safely.
3. Security tests: wrong passphrase, corrupted ciphertext, tampered metadata, missing Keystore key, revoked OAuth, account switch, no network, Drive quota/rate limit, partial upload, process death during snapshot/restore.
4. Build tests: workflow guards, Kotlin compilation, Gradle build, signed APK, signer certificate continuity, release checksum and metadata.
5. Device tests: first consent, backup to user's own account, update same file (no duplicate), force-close/reopen retry, restore on same device, restore on a second device using passphrase, and confirm local data remains intact after every injected failure.

## Current status

- Android OAuth Client ID received from the user; package and signing SHA-1 values are recorded in the Master Register. The Cloud Console's internal settings are not independently inspectable from this repository.
- Pre-edit backup branch `backup/before-google-drive-auto-backup-2026-11-19`; working branch `feature/google-drive-auto-backup-2026-11-19`.
- Audit and data inventory are documented in `docs/PROJECT_MAP_AND_SECRETS_REGISTER.md`.
- No app source, Android ZIP, web HTML, release metadata, or user data has been changed. No upload/restore/device test has been performed.
