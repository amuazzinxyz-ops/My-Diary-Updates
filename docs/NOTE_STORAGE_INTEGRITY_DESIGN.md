# Note Storage Integrity — Design Before Implementation

## Temporary note-save diagnostics — isolated investigation branch — 2026-11-28

- Created branch `diagnostic/note-save-visibility-2026-11-28` from live `main` (Web 501). No release branch or production ref was changed.
- Added temporary diagnostics only: capture the note IDs present immediately before Save; read the raw active-note IDs from localStorage after Save; collect IDs attached to the note cards rendered after the list refresh; save these ID-only arrays and timestamp under separate key `diary_note_save_diagnostic_v1`. No note titles, bodies, photos, PINs, or other private content is copied into diagnostics.
- After each Save, the status line shows counts for pre-save notes, storage records, and rendered cards. A **Jaanch Report Copy** control copies the ID-only report (or opens a copy prompt when clipboard access is unavailable).
- Each rendered note card receives a diagnostic-only `data-diary-note-id` attribute. No existing note storage, save/delete behavior, filtering, ordering, UI feature, or APK logic is intentionally changed.
- Source and mirror are byte-identical on this branch (Git blob SHA `dd8ded8ffd63f9f77fd1208bf141bacc3e7eedfd`). Live `main` remains Web 501 with its original source/mirror and manifest SHA-256. Prepared as diagnostic Web Update 502 candidate on this isolated branch; branch `latest.json` records its manifest SHA-256. Source/mirror identity and JavaScript syntax have passed static checks. The branch is not yet live on `main`; Phone Test is pending.
- Automated validation and exact device reproduction remain pending. This diagnostic build is not Phone Test PASS and does not claim the underlying cause is fixed.
- After Web 502 is merged to `main`, the user can use Check for Update to run the diagnostic. No APK is needed. Do not ask the user to clear app data, uninstall, or rebuild the APK.


Date: 2026-11-28
Status: design only; no app code or release changed.

## Why this work is necessary

The user has repeatedly reported that saving a new note makes an earlier note appear missing. Web Updates 500 and 501 did not resolve the phone-reported symptom. The current implementation has a single IndexedDB safety record named `latest`, and startup restores it only when localStorage is syntactically invalid. A valid but incomplete JSON array is accepted and then copied over the only safety record.

The current `write(a, requiredIds)` check is conditional: when callers supply `requiredIds`, it checks the current read set; when callers omit it, the check is skipped. Several non-delete mutation paths call `write(all)` / `write(latest)` without a required-ID baseline. Those operations include note PIN changes and favourite toggles. Explicit delete flows also call `write()`, but deletion must remain possible when it is a deliberate user action. Therefore simply requiring all prior IDs in every write would break legitimate deletion and restore behavior.

This confirms weaknesses in the storage protection design. It does not prove the exact cause of every reported incident, and it does not establish that any missing note has been recovered.

## Current source audit

Audited the live `web-source/index.html` and confirmed `diary-web/index.html` is byte-identical.

- `saveDiarySafetyCopy()` stores only one record under IndexedDB key `latest`.
- `prepareDiaryStorage()` checks only whether localStorage parses as an array. It does not compare the array's note IDs or content against the safety copy before trusting it.
- Startup then calls `saveDiarySafetyCopy()`, which can replace the previous good snapshot with the incomplete-but-valid localStorage array.
- `write(a, requiredIds)` validates candidate IDs and data shape. The protection against missing current IDs runs only when `requiredIds` is an array.
- `saveNote()` supplies the current note IDs, but other write call sites do not all supply an equivalent baseline.
- Explicit delete and bulk-delete flows move notes to Recently Deleted and then remove them from the saved list. Restore and backup-import flows intentionally add records. These operations need explicit, typed intent rather than a blanket “never remove IDs” rule.
- IndexedDB safety-copy writes are queued, but callers generally do not await their completion. A successful localStorage write is therefore not proof that its safety snapshot has committed.

## Proposed safety model (not yet implemented)

### 1. Make the durable journal the commit authority

Use IndexedDB transactions for a versioned journal and snapshots. A committed journal entry must include:
- monotonically increasing sequence number and unique operation ID;
- previous committed sequence / snapshot reference;
- full note and Recently Deleted state (or a rigorously verified content-addressed snapshot plus deltas);
- ordered note IDs and content digest;
- operation type: create, edit, metadata update, move-to-trash, restore, permanent-delete, import-merge, or recovery;
- explicit affected IDs and explicit removal/tombstone IDs;
- timestamp and schema version.

The journal entry and current-head pointer must be committed atomically in one IndexedDB transaction. Do not acknowledge a save as successful until this durable commit completes. Only after the durable commit should the localStorage compatibility mirror be updated and read back. If either step fails, report failure and retain the last committed journal state.

### 2. Distinguish deliberate deletion from unexplained disappearance

- Create/edit/PIN/favourite/format changes must preserve every ID from the committed baseline unless the operation explicitly declares a deletion.
- Move-to-trash must atomically record the note in trash and tombstone it from active notes in the same committed operation.
- Restore must atomically move the same ID from trash back to active notes.
- Permanent delete must record an explicit permanent-delete tombstone before any historical copy containing that note can be pruned.
- Import-merge may add validated IDs but may not silently remove existing IDs.
- An unexplained missing ID must cause a blocked/conflict state; never auto-merge or silently overwrite. Offer recovery choices only after preserving both candidate states.

### 3. Startup reconciliation

On startup, compare the localStorage mirror with the latest committed journal head using schema, sequence, ID set, and content digest.

- If it exactly matches: continue normally.
- If localStorage is missing/corrupt but the journal head is valid: restore the exact committed state and verify it.
- If localStorage is valid but differs: preserve the mirror and journal snapshot as separate candidates, block destructive writes, and record a recoverable conflict. Do not guess which is correct.
- If IndexedDB is unavailable or quota/write fails: do not claim protected save success. Keep the existing data untouched and show a clear storage error.
- Never overwrite a known-good journal head merely because localStorage parses successfully.

### 4. Snapshot retention and quota

Retain multiple verified generations, not a single `latest` record. Pruning must be bounded, quota-aware, and happen only after a newer journal head is committed and verified. Do not prune the only generation containing a note until its explicit deletion/tombstone history is safely committed. Large photo payloads require quota tests; if full snapshots are too large, use a verified immutable base plus append-only deltas and periodic compaction.

### 5. Compatibility and rollout

The existing app uses synchronous `read()` / `write()` throughout multiple features. Moving to an asynchronous durable commit is a cross-cutting change. Do not implement a partial journal around only the New Note Save button. First enumerate and migrate every note mutation path, including note PIN changes, favourite toggles, single delete, bulk delete, Recently Deleted restore/permanent delete, backup import, startup migration, and recovery. Preserve legacy note IDs/data, photos, PINs, ordering, and other modules.

For first launch after upgrade, do not assume the current localStorage state or the old single IndexedDB snapshot is authoritative if they differ. Preserve both and require a safe reconciliation path; do not silently discard either.

## Required automated test matrix before any release

1. Create: repeated saves at 1, 7, 8, 9, 10, 14, 15, 16, 17, and 30 notes preserve every prior ID and payload.
2. Edit: update title/body/category/photos/layout and prove no unrelated ID or payload changes.
3. Metadata: favourite, pin/unpin, note PIN set/change/recovery/off, and formatting changes preserve every other note.
4. Delete: single and bulk delete move exactly the selected IDs to trash; all unselected notes remain byte-for-byte equivalent.
5. Restore: restore one trashed note without duplicates; other active/trash notes remain unchanged.
6. Permanent delete: explicit tombstone is committed; no accidental removal of unrelated notes.
7. Import: valid backup merge adds only eligible IDs; malformed backup leaves all stores unchanged.
8. Startup: valid complete mirror, corrupt mirror, missing mirror, valid-but-incomplete mirror, stale mirror, and journal-ahead crash recovery.
9. Failure injection: IndexedDB unavailable, transaction abort, quota exceeded, localStorage quota exceeded, read-back mismatch, and process termination between each commit phase.
10. Concurrency: rapid consecutive saves, repeated taps, asynchronous PIN digest completing late, and stale operation attempts cannot overwrite a newer commit.
11. Legacy migration: missing/duplicate IDs and non-object legacy entries remain recoverable and do not get silently dropped.
12. Photo-heavy notes and large trash sets: quota/compaction/pruning cannot discard the only verified copy.

Each test must assert IDs and full payloads, not just note counts or UI visibility. Run tests against both the extracted storage module and app-level mutation flows. Verify source/mirror equality, syntax, update manifest hash, and backup/rollback before release.

## Release gate

No source change, Web Update, or APK is authorized by this design note. Keep Web 501 live and clearly marked Phone Test pending / not resolved. Do not ask the user to create more test notes, clear app data, or uninstall. Only proceed to implementation after the storage design covers all mutation paths and automated failure-injection tests pass. User phone confirmation remains required after any eventual release.
