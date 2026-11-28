# My Diary Project Register (Permanent Handover)

Last reviewed: 2026-11-28

## Current release state — 2026-11-28

- Latest published web version: **496** — Sab Notes now uses measured device-viewport pixel dimensions for edge-to-edge mobile display, retaining its existing inner design. The existing panel design, normal saved-note list, order, search, categories, note actions, Recently Deleted, and note data remain unchanged. Source and mirror are byte-identical. **Phone Test pending.** Web 490 remains the last user-confirmed rollback Phone Test PASS; Web 493 was also previously user-confirmed PASS. APK remains My Diary 1.0.222 / versionCode 221 and is unchanged.
- Web 494 source and mirror are byte-identical. SHA-256: `4b10341190d61606c81c3aecba97d0d346652cdc4beab2ec1461c88ebe37da1c`; `latest.json` declares `webVersion: 494` with the same SHA-256. Phone Test pending.
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
- Latest APK: **versionName 1.0.222**, **versionCode 221**, SHA-256 `df2a558ce528d51ae93277fd09d90f9772f53787a364b8c36cd40faec7bdc174`. It contains the exact published Web Update **486** bundle. **APK 1.0.221 → 1.0.222 in-place upgrade PASS; Check for Update PASS; Phone Test PASS — user confirmed on 2026-11-27.** APK 1.0.222 is now the latest phone-tested release.


## Web Update 495 — Sab Notes full-screen sizing correction — 2026-11-28

- User reported that Web 494 was received by Check for Updates but Sab Notes still opened in its previous non-full-screen presentation on the phone.
- Corrected only the opening/closing presentation of the existing Sab Notes list: the same Diary panel now receives direct full-viewport inline sizing when Sab Notes opens on mobile, so the result does not depend on the `:has()` selector or a late-appended CSS block in Android WebView. Closing Sab Notes, opening Recently Deleted, or closing the Diary clears only these temporary full-screen sizing properties.
- Existing panel/header/list design, saved-note list and order, search, categories, note actions, Recently Deleted behavior, note storage/data, photos, PINs, locks, widgets, reminders, and all other modules are unchanged. No APK was built or modified.
- Source and mirror are byte-identical (Git blob SHA `467c276daa92feeb388c1fa7b88adf9a4d4f506a`). Independently verified UTF-8 SHA-256: `bce1180a734ffed02fb9c01e877cfb2ecb023feba159ea031f4097133ac71d7a`; `latest.json` declares Web Update **495** with the same hash.
- Safety backup branch: `backup/pre-web495-sab-notes-fullscreen-fix-2026-11-28`. Backups:
  - `backups/2026-11-28-before-web495-sab-notes-fullscreen-web-source.html`
  - `backups/2026-11-28-before-web495-sab-notes-fullscreen-diary-web.html`
  - `backups/2026-11-28-before-web495-sab-notes-fullscreen-latest.json`
  - `backups/2026-11-28-before-web495-sab-notes-fullscreen-register.md`
- Working branch: `fix/web495-sab-notes-fullscreen-2026-11-28`. Source commit: `e6c5d79dcfa4a0d952fab14aca9c06ba14c448a6`; mirror commit: `c23b856856e6734ae1b1456b50545cf1ee22c6e1`; metadata commit: `01c8cee44b9bbf7dfa15ec229d49ffe79feaf5be`.
- **Phone Test pending — do not mark PASS until the user confirms Sab Notes opens edge-to-edge on the phone and the existing design/list/actions remain correct.**
- APK remains **My Diary 1.0.222 / versionCode 221**. No APK was built or modified.

## Web Update 492 — correction: Sab Notes popup presentation only — 2026-11-28

- User reported that Web 491 incorrectly showed the **Delete Ki Huwi Note** button in the Sab Notes popup and that the normal note names/list did not appear as expected. Corrected this immediately.
- Sab Notes must retain its original normal saved-note list and existing note-open/read/edit behavior. This update changes only the popup presentation to full-screen on mobile; the Recently Deleted button is hidden inside the Sab Notes popup. The close control remains available.
- The normal list renderer remains on the non-trash path (`showingTrash=false`); no note data, save/delete logic, note-card click behavior, storage keys, photos, PINs, locks, widgets, reminders, or other modules were changed. Recently Deleted restore/permanent-delete behavior is unchanged. **No APK was built or modified.**
- Full-screen CSS now applies to the two modes independently, and the trash button hide rule is placed after its shared button styling to prevent it being accidentally displayed in Sab Notes.
- Source and mirror are intended to be byte-identical (verify after merge). Web 492 SHA-256: `6ee8043d781ebcd83cb5c7734d6b75452b9b40afd3464c8df3fbb473a116537c`; `latest.json` advertises Web Update **492** with this hash.
- Safety backup branch: `backup/pre-web492-sab-notes-popup-correction-2026-11-28`. Backups:
  - `backups/2026-11-28-before-web492-web-source.html`
  - `backups/2026-11-28-before-web492-diary-web.html`
  - `backups/2026-11-28-before-web492-latest.json`
  - `backups/2026-11-28-before-web492-register.md`
- Working branch: `fix/web492-sab-notes-popup-correction-2026-11-28`. Source blob: `d22708190406376770a0532a4a95aa7415c8f892`; mirror commit: `dd566a3c0e36f00eba06677bcf4ceb5edd35bdfe`; metadata commit: `fae29bb04321f55cfff165922dbf99bd8058467b`.
- Merged to `main` through PR #527; squash merge commit: `56632485856cbdf05dbf0be7fe5c1cb90c978bcb`. Source, mirror, and `latest.json` were re-fetched and verified after merge.
- **Phone Test pending — do not mark PASS until the user confirms that Sab Notes shows all normal saved-note names, opens notes as before, hides the Recently Deleted button, and closes correctly.**

## Web Update 491 — Sab Notes opens the Recently Deleted-style full-screen panel — 2026-11-28

- At the user's approval, changed only the **Me > Sab Notes** opening/closing presentation so it uses the same mobile full-screen panel layout as **Me > Delete Ki Huwi Note**.
- Sab Notes still renders the normal saved-note list; it does not show deleted notes. The full-screen close control reads **✕ Band Karein**. Tapping it returns to the Me menu and restores the Sab Notes button to its original location. Android Back / Escape / the Diary overlay close continue to close the full Diary overlay.
- The existing Recently Deleted button and its restore/permanent-delete actions were not changed. No note data, save/delete logic, storage keys, photos, PINs, locks, widgets, reminders, or other modules were changed. **No APK was built or modified.**
- `web-source/index.html` and `diary-web/index.html` are byte-identical (Git blob SHA `ac72a972cc8ce96fcee0ca7af67589c8ead54aa7`). Independently computed UTF-8 SHA-256: `cc230ac4d50df2a11a47105be331761a515d20cc4db1a197f6d56c306c2aad2b`; `latest.json` advertises Web Update **491** with this exact hash.
- Safety backup branch: `backup/pre-web491-all-notes-popup-2026-11-28`. Backups:
  - `backups/2026-11-28-before-web491-all-notes-popup-web-source.html`
  - `backups/2026-11-28-before-web491-all-notes-popup-diary-web.html`
  - `backups/2026-11-28-before-web491-all-notes-popup-latest.json`
  - `backups/2026-11-28-before-web491-all-notes-popup-register.md`
- Working branch: `fix/web491-all-notes-popup-2026-11-28`. Source commit: `fd26703e5f5b5cba892b7b211652afd73ec06b16`; mirror commit: `8753027916840c62d1625a408aee88dce7902dc8`; metadata commit: `9b930279078e31accde4f72782c4253a1a2b1b12`.
- Merged to `main` through PR #526; squash merge commit: `9044ff493e3fc377bf7aa995f8cbec326aa72fe9`. Live source, mirror, `latest.json`, and Register were re-fetched and verified after merge.
- Existing APK metadata remains **My Diary 1.0.222 / versionCode 221**, APK SHA-256 `df2a558ce528d51ae93277fd09d90f9772f53787a364b8c36cd40faec7bdc174`. No APK build or signing change.
- **Phone Test pending — do not mark PASS until the user confirms that Sab Notes opens and closes correctly on the phone and still shows normal saved notes.**

## Web Update 490 — rollback to the exact phone-tested Web Update 486 bundle — 2026-11-28

- At the user's request, restored the exact Web Update 486 HTML rather than trying further changes to the New Note saved-list scrolling issue. Web Updates 487, 488, and 489 are superseded and are no longer part of the active bundle; their historical records and backups remain intact.
- Restored `web-source/index.html` from verified Web 486 source commit `7c455981ddf1fda5d71702f12252561f628d179f` and `diary-web/index.html` from verified Web 486 mirror commit `2b90462da541c25cc04f1c32e81dad6a238445ca`. Both files are byte-identical (Git blob SHA `b1674e673f6ee9a5bb25028a197031a3ed82f6c8`) and have the previously verified SHA-256 `99200a1baaea4241e2231c62650b0a85108006e11c26fe2cf24a9d45bc89885d`.
- Published rollback under monotonically increasing Web Update **490** so Check for Updates can detect it as a new update; `latest.json` points to the restored Web 486 content and matching SHA-256. APK metadata remains My Diary **1.0.222 / versionCode 221**, APK SHA-256 unchanged. No APK was built or modified.
- Safety backup branch: `backup/pre-web490-rollback-2026-11-28`. Working branch: `rollback/web486-as-490-2026-11-28`.
- This is a source/manifest rollback only. **Phone Test PASS — user confirmed on 2026-11-28.** The user confirmed Web Update 490 through Check for Updates and phone testing; this closes the pending device verification. Register-only change; no app source, update bundle, metadata, or APK was changed.

## Web Update 489 — New Note saved-list touch scrolling correction — 2026-11-28

- Re-checked the live source and Master Register after the user reported that Web 488 changed the visible count from seven to eight, but the remaining saved notes still could not be reached.
- Confirmed that `read()` returns all valid saved-note records and `renderList()` iterates every matching note; there is no seven- or eight-note cap, slice, or deletion in the saved-list rendering path.
- Corrected the actual mobile scrolling setup: `#diaryMyNotesList` now has a definite bounded height (`45dvh`), `min-height:0`, and explicit `overflow-y:scroll` / `overflow-x:hidden`. The Diary body's pull-to-refresh touch-start handler now ignores gestures that begin inside the saved-note list, so the list owns its swipe gesture.
- Scoped changes only to the saved New Note list's scroll CSS and the Diary body's pull-to-refresh touch-start guard. No note data, save/delete logic, local-storage keys, photos, PIN/lock behavior, or other modules changed. No APK was built or modified.
- `web-source/index.html` and `diary-web/index.html` are byte-identical (Git blob SHA `f45cc720b71310d7855127f9fd2994bb4fac1263`). Independently verified UTF-8 SHA-256: `acc1e98874913f134a2cec7f1695794639978934fce9e95d574fe64b617e39de`; `latest.json` declares Web Update **489** with the same hash. SHA implementation checked against the standard `abc` vector and the Web 488 backup hash.
- Safety backup branch: `backup/pre-web489-note-scroll-touch-2026-11-28`. Backups:
  - `backups/2026-11-28-before-web489-note-scroll-touch-web-source.html`
  - `backups/2026-11-28-before-web489-note-scroll-touch-diary-web.html`
  - `backups/2026-11-28-before-web489-note-scroll-touch-latest.json`
  - `backups/2026-11-28-before-web489-note-scroll-touch-register.md`
- Working branch: `fix/web489-note-scroll-touch-2026-11-28`. Source commit: `b909f1f23f2f9fc4e7ad97dfb433c059b3d50131`; mirror commit: `d7683a190dbbc4d635a2ba8ddddd6a1ff5702c8f`.
- Published to `main` through PR #524; squash merge commit `85d225468b9d012e8a47773e2a1c730d849fd295`. Live source, mirror, Web 489 metadata SHA-256, and Master Register were re-fetched and verified after merge.
- **Phone Test pending — do not mark PASS until the user confirms that saved notes beyond the first eight can be reached by swiping inside the saved-note list.**
- APK metadata remains **My Diary 1.0.222 / versionCode 221**; no APK was built or changed.

## Web Update 488 — New Note saved-list independent scrolling — 2026-11-28

- User reported that Web Update 487 did not resolve the phone issue: only seven saved notes appeared and the list would not scroll. Re-inspection confirmed that `renderList()` iterates over all matching saved notes and contains no seven-note cap or truncation.
- Web 487's body-scroll rule was present in the live source, but did not solve the user's actual phone behavior. This update gives `#diaryMyNotesList` its own bounded vertical scroll area with `overflow-y:auto`, touch vertical panning, momentum scrolling, and contained overscroll. The user can swipe directly within the saved-note list.
- CSS-only change to the saved-note list rule in `web-source/index.html` and `diary-web/index.html`. No JavaScript, save/delete logic, local-storage keys, note data, photos, PIN/lock behavior, or other modules changed. No APK created.
- Source and mirror are byte-identical (Git blob SHA `3d4f888bb29f06d7f772ce91026c5bc53191f813`). Independently calculated UTF-8 SHA-256: `1547b3344fa3f26b3382b0b3811ba994873f7b365f693f248b28dc449f8b4ec0`; `latest.json` declares Web 488 with this exact hash. SHA implementation verified against the standard `abc` test vector.
- Backups on `backup/pre-web488-note-list-scroll-2026-11-28`:
  - `backups/2026-11-28-before-web488-note-list-scroll-web-source.html`
  - `backups/2026-11-28-before-web488-note-list-scroll-diary-web.html`
  - `backups/2026-11-28-before-web488-note-list-scroll-latest.json`
  - `backups/2026-11-28-before-web488-note-list-scroll-register.md`
- Working branch: `fix/web488-note-list-scroll-2026-11-28`. Source commit `444e6564703b3ec88b0d3ee873787cac9a29a853`; mirror commit `1d54a1089f06eceed6b084037fb3c925be43e633`.
- Published to `main` through PR #523; squash merge commit `18b78eea3c8b5d7e8bc4d14e196927fc330b4774`. Live source, mirror, metadata SHA-256, Web 488 version, and Master Register were re-fetched and verified after merge.
- **Phone Test pending — do not mark PASS until the user confirms that notes beyond the first seven can be reached by swiping inside the saved-note list.**
- Existing APK metadata remains unchanged: My Diary 1.0.222 / versionCode 221. No APK was built or modified.

## Web Update 487 — saved New Note list scrolling — 2026-11-28

- Fixed only the saved-notes scroll area in My Diary. The scroll body is a flex child inside the height-limited Diary panel; it now has `flex:1 1 auto` and `min-height:0`, allowing it to shrink and scroll instead of being clipped after the first visible notes.
- No JavaScript, note-saving/deleting logic, local-storage keys, note data, PIN/lock logic, photos, buttons, or other modules were changed. No notes are deleted or capped by this fix.
- `web-source/index.html` and `diary-web/index.html` are byte-identical; Git blob SHA: `be6dca993f157a24eabde30226fee26cb4582838`. Independently verified UTF-8 SHA-256: `dabba9033041e6eb78876e388986da7833076bdc5034c0f68da41f3af45b4514`; `latest.json` advertises Web Update **487** with the same hash.
- Safety backup branch: `backup/pre-web487-note-scroll-2026-11-28`. Pre-edit backups: `backups/2026-11-28-before-note-scroll-web-source-index.html`, `backups/2026-11-28-before-note-scroll-diary-web-index.html`, `backups/2026-11-28-before-note-scroll-latest.json`, and `backups/2026-11-28-before-note-scroll-PROJECT_MAP_AND_SECRETS_REGISTER.md`.
- Work branch: `fix/web487-note-scroll-2026-11-28`. Source commit: `fe5bb6fe0f27954c58b939ccad16c9378e8b2909`; mirror commit: `281ec033d9c0ac41592697f3dee630dcf15f82df`. Metadata and Register commits are recorded in the branch history.
- Main publication commits: source `4f85ed44e09a19cfb673e4896a8945ba3e2c30f9`; mirror `94c6c556afba158a3d9933e7df3335ee8c01571f`; `latest.json` `485e8af37dc61958101c8a37e01392fda080bcf6`.
- Web-only update; no APK was built or changed. Delivery is through the app's **Check for Updates**. **Phone Test pending** until the user confirms scrolling works on the phone.

## Restored APK 1.0.222 / Web Update 486 — post-restore phone test — 2026-11-27

- After restoring the previously user-confirmed PASS release state (APK **1.0.222**, versionCode **221**, Web Update **486**), the user performed a fresh device check and confirmed: **Phone Test PASS — user confirmed on 2026-11-27**.
- This confirmation applies to the restored APK 1.0.222 + Web 486 state. Web Update 487 and the later recovery-build changes remain excluded from the active release. The safety backup branch and historical commits are retained.
- No app source, APK, release metadata, or Web bundle was changed for this confirmation; this is a Register-only record.
- Register backup created before editing: `backups/2026-11-27-before-restored-1.0.222-phone-test-pass-register-update.md`.

## APK 1.0.222 — cumulative Web Update 486 bundle — 2026-11-27

- Built **My Diary 1.0.222**, **versionCode 221**, package `com.personal.diaryapp`, as an in-place upgrade target for the phone-tested 1.0.221 / versionCode 220 release.
- The APK embeds the exact currently published `web-source/index.html` for **Web Update 486**, not the older Web 478 bundle. Therefore it includes all retained published Web Updates **479–486** on top of the 1.0.221 baseline. Rolled-back Web 471 behavior remains excluded.
- Exact embedded Web source and mirror are byte-identical: Git blob SHA `b1674e673f6ee9a5bb25028a197031a3ed82f6c8`; verified Web SHA-256 `99200a1baaea4241e2231c62650b0a85108006e11c26fe2cf24a9d45bc89885d`. Build guards specifically verified Web 483's Photo-only Gradient removal and Web 486's Me-button box-size slider implementation.
- APK SHA-256: `df2a558ce528d51ae93277fd09d90f9772f53787a364b8c36cd40faec7bdc174`. Published as both `My-Diary.apk` and `My-Diary-1.0.222.apk` (same Git blob SHA `b66486f2579fe6b8d8607f44d19e7031c91b39f1`; 2,105,922 bytes).
- Signing readiness and keystore validation PASS. The signed APK passed the workflow's exact previously approved signing-certificate SHA-256 fingerprint check: `23:A4:E9:3F:3C:79:11:DC:E1:83:89:EA:58:35:48:70:0C:6A:D6:A3:75:97:07:F1:CD:22:2D:07:E2:40:8B:5A`. This preserves the same signing identity as APK 1.0.221.
- Verification: original Android project verification PASS; exact Web 486 source/hash/mirror guard PASS; version/package/feed guard PASS; debug build PASS; signed Release build PASS; signing fingerprint check PASS; publication PASS; signed APK artifact upload PASS; translation audit upload PASS.
- GitHub Actions build run 582: https://github.com/amuazzinxyz-ops/My-Diary-Updates/actions/runs/45968165096 — completed **success**. APK publication commit: `cd984f1b6485b024c1a8687a9468cdb020dcc6cc`. Build workflow preparation commit: `8ed85b8173eafd5603542c936de1c1b55380f5e5`. Safety backup branch: `backup/pre-apk-1.0.222-2026-11-27`.
- **Phone installation / upgrade test: PASS — user confirmed on 2026-11-27.** The user installed APK 1.0.222 over APK 1.0.221; in-place upgrade PASS, Check for Update PASS, and Phone Test PASS. This confirms the user's requested three checks. APK 1.0.222 is now the latest phone-tested release.


## APK 1.0.222 — user phone-test confirmation — 2026-11-27

- **In-place upgrade:** APK **1.0.222 installed over APK 1.0.221 — PASS**.
- **Check for Update:** **PASS**.
- **Phone Test:** **PASS — user confirmed on 2026-11-27**.
- Result: all three user-reported checks passed. The previously pending phone verification for APK 1.0.222 is now closed. Preserve the existing build/source/signing audit details in the release section above; no app source or APK was changed as part of this Register-only update.
- Register safety backup created before editing: `backups/2026-11-27-before-apk-1.0.222-phone-test-pass-register-update.md`.

## Web Update 486 — resize the Me button itself, not its text — 2026-11-26

- Corrected the previous interpretation: the size slider must change the **actual Me button box**, not the text size. The Me label stays at its original 13px; the button width, height, min-width, max-width, min-height, and max-height now scale together from 75% to 160%.
- At 100%, the button remains the original 36×36px. Its existing appearance, label, colour, 3D styling, and action are retained. The × button, position behavior, and all other controls/functions were not changed.
- Updated `web-source/index.html` and `diary-web/index.html`; both are byte-identical with Git blob SHA `b1674e673f6ee9a5bb25028a197031a3ed82f6c8`.
- `latest.json` declares **webVersion 486** and verified Web SHA-256 `99200a1baaea4241e2231c62650b0a85108006e11c26fe2cf24a9d45bc89885d`. This matches the current source and mirror (both Git blob SHA `b1674e673f6ee9a5bb25028a197031a3ed82f6c8`). The earlier Register SHA `964ade81...` was stale and is corrected here. At Web 486 publication, APK was still **1.0.221 / versionCode 220**; APK 1.0.222 subsequently bundled this exact Web 486 source (see the APK 1.0.222 section below).
- Commits: source `7c455981ddf1fda5d71702f12252561f628d179f`; mirror `2b90462da541c25cc04f1c32e81dad6a238445ca`; metadata `7a4348ee858ec94a70083aa9d4c7e450d963b981`.
- Delivery is through Check for Updates. **Phone Test PASS — user confirmed on 2026-11-27.**

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


## Web Update 496 — Sab Notes measured mobile viewport sizing — 2026-11-28

- Follow-up to Web 495 after the user confirmed the Sab Notes panel still did not visually reach the top and bottom edges on the phone.
- Changed only the outer sizing helper for the existing Sab Notes view. It now measures the actual device viewport and applies pixel-based width/height to the existing panel and overlay, with mobile detection that also recognizes touch devices and Android WebView. This avoids relying on inconsistent CSS viewport-unit handling.
- Sab Notes keeps its own existing header, list placement, note order, search, categories, note actions, and close behavior. It does not borrow the Recently Deleted inner layout. No note data, photos, PINs, locks, widgets, reminders, other modules, or APK files were changed.
- Source and mirror are byte-identical (verify after merge). UTF-8 SHA-256: `0fdcabbbaa95454873937659ca79a0ad085ff201eb27c9cb2ced638dc47b2fa5`; `latest.json` declares Web Update **496** with the same hash.
- Safety backup branch: `backup/pre-web496-sab-notes-viewport-fix-2026-11-28`. Backups: `backups/2026-11-28-before-web496-sab-notes-viewport-web-source.html`, `backups/2026-11-28-before-web496-sab-notes-viewport-diary-web.html`, `backups/2026-11-28-before-web496-sab-notes-viewport-latest.json`, and `backups/2026-11-28-before-web496-sab-notes-viewport-register.md`.
- Working branch: `fix/web496-sab-notes-viewport-fix-2026-11-28`.
- **Phone Test pending — do not mark PASS until the user confirms Sab Notes fills the phone screen from top to bottom and the existing design/list/actions remain correct.**
- APK remains **My Diary 1.0.222 / versionCode 221**. No APK was built or modified.
