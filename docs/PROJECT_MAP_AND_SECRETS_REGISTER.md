# Check for Update delivery test marker (Web Update 363, 2026-11-20)

- User approved a test-only marker to verify that **Check for Updates** delivers a new web bundle to the installed app.
- Added one small, muted **Web Update 363** label immediately below **Check for Updates** in the existing Me panel. It is a delivery-test indicator only; it adds no app functionality and does not alter saved data, update logic, existing controls, PINs, locks, reminders, or native Android code.
- Backup branch: `backup/before-check-update-test-363-2026-11-20`. Working branch: `test/check-update-marker-363-2026-11-20`.
- Only the web source and its required mirror are changed for the UI marker. `latest.json` advances webVersion to **363** and advertises the SHA-256 below; APK metadata and APK binary remain unchanged at **1.0.195 / versionCode 194**.
- Web bundle SHA-256: `e92c1ca476215d12a02699e2479bae840f6e7b8984f8658da65cb7bf9da6f6a9`. Static checks must confirm one marker directly after the Check for Updates button and exact source/mirror parity. Device-side delivery confirmation is pending the user's Check for Update test.

---

# My Diary Backup/Restore — include Personal Calendar and Smart Reminder (Web Update pending, 2026-11-19)

- User requested that the existing single **Diary-My-Notes-Backup.json** backup/restore also include **📅 Personal Calendar** and **⏰ Smart Reminder**, alongside the existing Notes, My Documents, and My Memories data.
- Extended the existing export to read the `calendar` and `reminders` record kinds from the existing `diary_me_features_v1` IndexedDB store and include them as `myCalendar` and `myReminders` in the same JSON file (backup format version 3). No separate button or backup file was added.
- Extended import/restore to validate and merge both record arrays by record ID without overwriting records already present. Existing version 2 and legacy Notes-only backups remain accepted because the two new arrays are optional.
- Restored Calendar records re-register their existing event alarms through the existing Calendar scheduler; restored future Smart Reminder records are re-registered through the existing reminder scheduler. Existing PIN/lock settings, Notes, Trash, Documents, Memories, reminder fields/settings, and other data formats are not intentionally changed.
- Backup branch: `backup/before-calendar-reminder-backup-2026-11-19`. Working branch: `fix/include-calendar-reminders-in-backup-2026-11-19`.
- Source edit: `web-source/index.html` only. PR #285 merged as `1111956432cdd3cd2ee1494391b144b239f5126c`. Web publisher workflow run `44488942313` completed successfully and published **Web Update 362**. `web-source/index.html` and `diary-web/index.html` are byte-identical at Git blob SHA `a5a8c969413b4f79e64f8aa533cebcaa7f14cefd` (577,368 characters). Live `latest.json` advertises webVersion **362** and web SHA-256 `c07f44281594480679d95732f7258dbd996e3fc2ed29d08d470f4af09bbea17c`. Static checks passed for both export keys, version 3, legacy-backup compatibility, ID-deduplicating restore, alarm rescheduling hooks, and source/mirror parity. The APK workflow run `44488942360` stopped safely at its exact-latest-HTML guard before compilation; all later build/release steps were skipped. APK remains **1.0.195 / versionCode 194**; this is web-only and requires no APK reinstall. Physical phone backup/restore testing remains pending; do not claim device-side PASS until the user completes a backup and restore test.

---

# Personal Calendar + Smart Reminder — center save-success popup on mobile (Web Update 355, 2026-11-19)

- User clarified that the previous 114px top placement was still too high and requested the success popup appear in the middle of the mobile screen.
- Updated only the shared `meFeatureShowSavedToast()` positioning used by **Personal Calendar** and **Smart Reminder**: fixed position at `top:50%; left:50%` with `transform:translate(-50%,-50%)`, centering the toast in the viewport.
- Existing 4-second display duration (`4000ms`), day-first **DD/MM/YYYY** date display, native date picker, saved records, reminder scheduling/settings, and all unrelated features remain unchanged. APK/native code was not changed.
- Backup branch: `backup/before-toast-center-mobile-2026-11-19`; feature branch: `fix/toast-center-mobile-both-forms-2026-11-19`; PR #267 merged as `03637dfb0ef29445b987946e7e2cea27aab38ee1`.
- Published as **Web Update 355**. `web-source/index.html` and `diary-web/index.html` are byte-identical; verified web SHA-256: `d15435c3e7f72788a2c62bb52e64633ba7c9554d28f599747e221c4e7dc604b8`. `latest.json` advertises webVersion **355** and this exact checksum.
- Static checks passed for centered positioning, 4-second duration, preserved DD/MM/YYYY date display, source/mirror parity, and checksum match. Physical Android visual testing is pending user confirmation.

---

# Personal Calendar + Smart Reminder — move shared success popup 30px lower (Web Update 354, 2026-11-19)

- User requested the save-success popup be moved another 30px lower in both Personal Calendar and Smart Reminder.
- Updated only the shared `meFeatureShowSavedToast()` position in `web-source/index.html`: top offset from 84px to 114px below the safe-area top (+30px). Both forms use this same helper, so both are covered.
- Existing 4-second display duration (`4000ms`) is unchanged. Web Update 353's day-first date display and native date picker are preserved. No saved data, reminder settings, scheduling logic, or APK code changed.
- Backup branch: `backup/before-toast-plus-30px-2026-11-19`; feature branch: `fix/toast-plus-30px-both-forms-2026-11-19`; PR #264 merged as `942bd791868e540febd7f34c28673ea8813d88fd`.
- Published as **Web Update 354**. `web-source/index.html` and `diary-web/index.html` are byte-identical at Git blob SHA `57a2c3dde06358f70aae318d82418e759ef41089`. Verified web SHA-256: `aa5f78fc1d23b060f9ab4d8641726035164da7bdcb4339655eba8958f80fee83`; `latest.json` advertises webVersion **354** and this exact checksum.
- APK remains `1.0.194` / versionCode `193`; no APK update. Static checks passed for 114px position, 4-second duration, preserved DD/MM/YYYY date fix, and source/mirror parity. Physical Android testing is pending user confirmation.

---

# Personal Calendar + Smart Reminder — force day-first date display independent of Android locale (Web Update 353, 2026-11-19)

- User reported that the Web Update 352 date field still displayed in the device's US-style order. Root cause: the browser's native `input[type="date"]` controls their visible date text using Android/browser locale; setting `lang="en-GB"` alone does not reliably override that UI.
- Updated only the shared `mfField()` date-field helper in `web-source/index.html`: keep the native date input and calendar picker, but overlay a visible, locale-independent **DD/MM/YYYY** display (for example **19/11/2026**). The input's underlying ISO `YYYY-MM-DD` value remains intact for validation, form submission, saved records, date comparisons, and reminder scheduling. Programmatic date assignments and native picker input/change events refresh the displayed day-first text.
- Feature backup branch: `backup/before-date-display-format-fix-2026-11-19`; feature branch: `fix/force-day-first-date-display-2026-11-19`; PR #262 merged as `2bb0cda03200ac31f0d1ec924eab15f4f9a8da93`. Feature diff: only `web-source/index.html` (21 additions, 2 deletions).
- Published as **Web Update 353**. `web-source/index.html` and `diary-web/index.html` are byte-identical at Git blob SHA `926da9abe6808a7989e671ca897064690c187a22`. Verified web SHA-256: `f13b58a651ec4f690dd6da883d56fac014f25da280248f2f7859536816bd03a8`; `latest.json` advertises webVersion **353** and this exact checksum.
- APK/native code remains **My Diary 1.0.194 / versionCode 193**; no APK build or release was made. Existing saved data, reminder records, alarms, and unrelated features were not intentionally changed. Static checks confirm the formatter, ISO-value preservation, native date picker event handling, and unchanged 84px/4-second success popup. Physical Android testing is pending user confirmation; do not claim device-side PASS until the user checks it.

---

# Personal Calendar + Smart Reminder — day-first date display and lower save popup (Web Update 352, 2026-11-19)

- User requested the success popup slightly lower than before and date fields in day/month/year order (e.g. **19/11/2026** instead of **11/19/2026**).
- Existing date inputs now request the `en-GB` locale. Stored ISO dates (`YYYY-MM-DD`), date parsing, saved records, and reminder scheduling remain unchanged.
- Shared success popup moved from **64px to 84px** below the safe-area top; its existing **4-second** duration and Calendar/Reminder-only success trigger are unchanged.
- Feature branch `fix/date-format-and-toast-position-2026-11-19`; backup branch `backup/before-date-format-and-toast-position-2026-11-19`; PR #259 merged as `53ab0821adbced2239ce66e1900f970a7813c12b`.
- Published in feed as **Web Update 352** through PR #260 (merged as `17f999dac7a4869f0d4bde592a22b4d695d8c6e6`). `latest.json` advertises webVersion **352** and web SHA-256 `0629d7e649b781a7467ec967a639cc119954f8f18eb7c8366135ebf4444d4543`. Source and mirror are byte-identical at Git blob SHA `e5a753192ba048ad6f99dcf4786295f7c127b682`. Static checks confirmed en-GB date input, 84px toast offset, and 4-second timer.
- APK/native code was not changed; APK remains **1.0.194 / versionCode 193**. Physical Android testing is still pending user confirmation; browser/OS date-control presentation may vary by device locale.

---


# Personal Calendar + Smart Reminder — move success popup lower and extend duration (Web Update 351, 2026-11-19)

- User reported the Web Update 350 success popup appeared too close to the top and requested a slightly lower position and four-second visibility.
- Changed only the existing shared success-toast styling/timer in `web-source/index.html`: top offset from safe-area top **18px to 64px**, and automatic dismissal from **2.6 seconds to 4 seconds**. Applies to both **📅 Personal Calendar** and **⏰ Smart Reminder**.
- Toast trigger remains limited to successful saves in those two sections. Existing localized message, toast design, validation/error messages, entry placement/order, saved data, reminder scheduling, alarms, notifications, and all other sections remain unchanged.
- Backup branch: `backup/before-calendar-reminder-toast-position-duration-2026-11-19`. Working branch: `fix/calendar-reminder-toast-position-duration-2026-11-19`. PR #257 merged as `c5d97ac6ef8e1dec840441ce8eafd45a5de4c6c6`. Feature diff: 2 insertions, 2 deletions in `web-source/index.html` only.
- Web publisher workflow run `44443472880` completed successfully. Published as **Web Update 351**. `web-source/index.html` and `diary-web/index.html` are byte-identical at Git blob SHA `e2554989fa2b2247e0afce713ab03b314c99fa64`. Live `latest.json` web SHA-256: `899c4f0a9df4c9d1b172a46b292ddd5323ac85f5ad89e261dda113d2757c50a9`.
- APK/native code was not changed. APK feed remains **1.0.194 / versionCode 193**. This is a web-only update; no new APK is required or claimed.
- Static checks confirmed the 64px safe-area offset, 4-second timeout, one shared helper, and unchanged Calendar/Reminder-only trigger. Physical phone visual test is pending user confirmation.

---

# Personal Calendar + Smart Reminder — temporary save-success popup (Web Update 350, 2026-11-19)

- User clarified that only the successful-save popup should appear briefly and disappear; no other layout or behaviour change was requested.
- Added one temporary, accessible success toast for **📅 Personal Calendar** and **⏰ Smart Reminder** after the existing save operation succeeds. It displays the existing localized success message and removes itself automatically after **2.6 seconds**. A repeated save replaces the previous toast rather than stacking messages.
- Validation, reminder scheduling, permission errors, save failures, saved records, entry order, entry cards, form reset, repeat rules, alarms, notifications, and all other Me tools retain their previous handling. Only the success-message presentation for Calendar and Smart Reminder changed.
- Backup branch: `backup/before-calendar-reminder-success-toast-2026-11-19`. Working branch: `fix/calendar-reminder-success-toast-2026-11-19`. PR #255 merged as `54fdaab0f155175f01691394839cd506f3777f91`. Feature diff: `web-source/index.html` only (11 additions, 1 deletion).
- Web publisher workflow run `44442681340` completed successfully. Published as **Web Update 350**. `web-source/index.html` and `diary-web/index.html` are byte-identical at Git blob SHA `b4047fc81b6e9c9e3d1a0afa238427df55e80154`. Live `latest.json` web SHA-256: `58fffa562dac0bfa8340b7b1e014516cc63662520d8dda024d3a38a6d4307b97`.
- APK/native code was not changed. APK remains **1.0.194 / versionCode 193**, SHA-256 `6b67de24f36f6ee985c1b6e1b88ce3f9259653c96938a412513570aee0c1428d`. Automatic APK workflow run `44442681396` stopped at the existing exact-latest-HTML guard; all later build/release/upload steps were skipped. No APK was built or published for this web-only change.
- Static checks confirmed one toast helper, 2.6-second dismissal, and success-toast use only for Calendar/Reminder. Physical Android phone visual test is pending user confirmation; do not claim device-side PASS until the user confirms it.

---

# Personal Calendar — remove duplicate standalone date below name (Web Update 349, 2026-11-19)

- User reported that the date appeared separately as plain text in addition to the new Date badge. Corrected only the **Personal Calendar** saved-entry renderer: the old standalone date line is no longer rendered for Calendar entries.
- The one-line **Birthday · Date · Time** badge row remains unchanged. The name badge, Date badge, Birthday/type badge, Time badge, saved record data, ordering, pin/long-press actions, repeat rules, reminder scheduling, alarms, and notifications remain unchanged. Smart Reminder retains its existing date display.
- Backup branch: `backup/before-calendar-extra-date-removal-2026-11-19`. Working branch: `fix/calendar-remove-duplicate-date-2026-11-19`. PR #253 merged as `6c3544088eb48629b4e12a22c5494e5b2f0fd05a`.
- Web publisher run `44439949757` completed successfully. Published as **Web Update 349**. `web-source/index.html` and `diary-web/index.html` are byte-identical at Git blob SHA `c6f1c53910162946b52247a5c22c96d005e0cda7` (558,847 bytes). `latest.json` web SHA-256: `01425dda964943fa6b070b3e320b9e1ef6baa7bf9d283040346733699509f2c9`.
- APK/native code was not changed. APK remains **1.0.194 / versionCode 193**; no APK release was made for this web-only fix. Physical-phone testing remains pending user confirmation.

---

# Personal Calendar + Smart Reminder — show pinned marker on saved entries (Web Update 346, 2026-11-19)

- User reported that Pin/Unpin was working but a pinned saved entry did not visibly show its pinned state. Added a visible **📌** marker before the saved entry title whenever the existing `record.pinned` flag is true.
- Applies equally to **📅 Personal Calendar** and **⏰ Smart Reminder**. Unpinned entries retain their original title display; unpinning removes the marker on rerender.
- Minimal feature diff: only `web-source/index.html`, one line changed (1 insertion, 1 deletion). Existing pin state, pinned-first sorting, long-press actions, entry data, edit/copy/delete/select, reminders, alarms, repeat settings, ringtone, snooze, notifications, and unrelated features remain unchanged.
- Backup branch: `backup/before-calendar-reminder-pin-indicator-2026-11-19`. Working branch: `fix/calendar-reminder-pin-indicator-2026-11-19`. PR #246 merged as `dff6f9a32dc3d52fd9f4bf100a0828f5db35f27e`.
- Web publisher run `44437220499` completed successfully. Published as **Web Update 346**; `web-source/index.html` and `diary-web/index.html` are byte-identical at Git blob SHA `0a065d715449b08a9b5639767f4fcac2ec557967` (558,315 bytes). `latest.json` web SHA-256: `fa73b38f0018a75de3defaa4505ca85bd73f5784287c6d9026d4682249aa1f5d`.
- APK/native code was not edited by this task. The automatic APK workflow `44437220444` failed safely at its pre-build synchronization guard because `web-source/index.html` and `diary-web/index.html` were temporarily not byte-identical while the publisher was syncing; the workflow skipped every build/release/upload step. The publisher subsequently completed successfully and the two files are now byte-identical. APK remains versionName `1.0.194` / versionCode `193`; no APK was built or published. Phone-side testing remains pending user confirmation.

---

# Personal Calendar + Smart Reminder — long-press entry actions (Web Update 345, 2026-11-19)

- User requested the same five actions as My Diary Notes when an entry is long-pressed in both **Personal Calendar** and **Smart Reminder**: Delete, Copy, Pin/Unpin, Edit, and Select.
- Added a long-press/context-menu action panel to saved Calendar and Reminder entry cards. Delete uses the existing confirmation and existing alarm cancellation paths; Copy creates a separate record with a new ID and does not reuse the original reminder IDs; Pin/Unpin stores a `pinned` flag and places pinned entries first while preserving date/created ordering; Edit uses the existing edit form; Select enters the existing bulk-selection mode with the pressed entry selected.
- Existing visible controls, saved entry fields, repeat/custom weekdays, ringtone, snooze, volume, notification scheduling, and unrelated features are retained. Existing entries are not migrated or rewritten; their default pin state is unpinned.
- Backup branch: `backup/before-calendar-reminder-long-press-actions-2026-11-19`. Working branch: `fix/calendar-reminder-long-press-actions-2026-11-19`. PR #245 merged as `68c64913ff64215f2d2f41e1a9eb507018ca703a`.
- Web publisher commit: `68ef3796e03d068f9dcd3d4f82728dbd82c0ab8f`. Check for Update feed advanced to **Web Update 345** in commit `9ce1d48477751366241670b4dcec27bfdedb242b`; web SHA-256 `6563393083eb41373bfdb7e27dbc20167dcef31ffb659a9dfe87d49359e4ed56`.
- Source and mirror are byte-identical at Git blob SHA `d76ebb3a2a906d5a0d9a1fae56e7e80e002a3882`. APK remains **1.0.194 / versionCode 193**, SHA-256 `5f59b76683c8d13e1c6f56a65cec062e6825048e040a0735cb3d2e672bd24fb4`; no APK/native code was changed. Physical Android phone testing is pending user confirmation.

---

# My Diary Note Search — results directly below the search bar (Web Update 344, 2026-11-19)

- Corrected the earlier misunderstanding: user wants the matching Note search results list itself moved immediately below the Note search bar, exactly like Personal Calendar and Smart Reminder move their filtered result list directly below their search panel while a query is entered.
- During a Note search, the existing filtered notes list is temporarily moved immediately after the search input and shown there. When the search is cleared, the list returns to its original position after the All Notes control and its previous visibility is restored.
- Reverted the previous extra relevance sorting so the original pinned/favourite and updated-time order remains unchanged. Search matching, category filter, note cards/actions, editor, saved notes, multi-select, Note Lock, and other Diary features remain unchanged.
- Backup branch: `backup/before-note-search-below-bar-2026-11-19`. Working branch: `fix/note-search-results-below-bar-2026-11-19`. PR #244 merged as `e20b598c7d1ea7fd0b4ec24e8dd3fc7bfabe6333`.
- Published as **Web Update 344**. `web-source/index.html` and `diary-web/index.html` are byte-identical at Git blob SHA `7ff3c73b8b64b1f6c2a0b2eeb45b5d0c9bbd4f5c`; `latest.json` web SHA-256 is `99d0e4755f83c834cf213c20bd88498f54f72b62343e40e9e42cfe4698980a29`.
- Web-only layout/DOM placement change; APK remains **My Diary 1.0.194 / versionCode 193** and APK/native code and saved note data are not modified. Physical Android phone testing remains pending user confirmation.

---

# My Diary Notes — best matching search result first (Web Update 343, 2026-11-19)

- User asked that when searching for a note name or note text, the matching note should appear at the top immediately below the Note search bar; everything else should remain as it is.
- Updated only the existing My Diary note-list sort priority: exact title match first, then title starts-with, title contains, exact body match, body starts-with, and body contains. Existing category filter, search matching/filtering, pin/favourite ordering among equally relevant results, newest-updated ordering, note cards, note actions, saved records and lock behaviour remain unchanged.
- Backup branch: `backup/before-note-search-top-result-2026-11-19`. Working branch: `fix/note-search-best-match-first-2026-11-19`. PR #243 merged as `c9f7b339002da1b7eb50f44b2c789a8e3f19c17b`.
- Published as **Web Update 343**. `web-source/index.html` and `diary-web/index.html` are byte-identical at Git blob SHA `1ae10ab3f8f2dc3b89412d93de15eeb127e6620d`. Live `latest.json` web SHA-256: `dbf645c49b4a9f04af3d2fc003d28af758ecd0e2471477e49627db8c45692bd7`.
- APK remains **My Diary 1.0.194 / versionCode 193**; no APK/native code or saved note data was changed. Physical Android phone testing remains pending user confirmation.

---

# Diary World Clock — Meeting Time Planner removed (Web Update 342, 2026-11-19)

- User asked to remove only **Meeting Time Planner** because it was not useful to them.
- Removed the Meeting Time Planner panel, date/time/city controls, converted-time result, associated event listeners and refresh/conversion functions from the existing World Clock modal. Removed its unused translation labels.
- Preserved the World Clock button/modal, global city/time-zone search (including typo-tolerant matching), saved city list, city add/remove, Favourite City, live clocks, day/night indication, Mumbai time difference, sunrise/sunset, and the one-second refresh behaviour. No other Me tools, Diary features, saved entries, city/favourite localStorage keys, Calendar, Smart Reminder, PINs/locks, photos, or APK/native code were changed.
- Backup branch: `backup/before-meeting-time-planner-removal-2026-11-19`. Working branch: `remove/world-clock-meeting-time-planner-2026-11-19`. PR #242 merged as `413795b80abf28af9715f3576cb052012f321bec`.
- Exact feature diff: `web-source/index.html` only (8 additions, 57 deletions); Master Register updated separately. Static checks confirm all Meeting Time Planner code/UI references are absent and World Clock city search, typo-tolerant search, favourites, live clock, day/night, Mumbai time difference, sunrise/sunset and World Clock button remain.
- Published as **Web Update 342**. `web-source/index.html` and `diary-web/index.html` are byte-identical at Git blob SHA `10fcd9569657bb32850b63c56c3cca11c85fa5a1` (551,360 bytes). Live `latest.json` web SHA-256: `fd20d2f146def6692cba06577bcc57dc04495e45f3bad9aef425df44d14db75b`.
- APK metadata remains **My Diary 1.0.194 / versionCode 193**, SHA-256 `51c3a68b6febf3a7e5f9aabbb997e5c32dad9c42bd53d45f17d8b128d88dd434`; no APK was rebuilt or published for this web-only removal.
- Physical Android phone testing remains pending user confirmation. Do not claim device-side PASS until the user confirms the Meeting Time Planner is gone and the other World Clock tools still work.

---


# Diary World Clock — Meeting Time Planner city selection stable (Web Update 341, 2026-11-19)

- User reported that the Meeting Time Planner city selector blinked while choosing a city. Source inspection found that `renderWorldClock()` calls `refreshWorldClockPlanner()` on the one-second live-clock interval, and that function unconditionally rebuilt the city `<select>` options each time.
- Minimal fix: cache a signature of the saved city list (zone + displayed name) and rebuild the options only when that signature changes. Ordinary one-second refreshes leave the existing select options in place and preserve the selected city. Date/time conversion and planner result refresh remain unchanged.
- Backup branch: `backup/before-world-clock-meeting-city-blink-fix-2026-11-19`. Feature branch: `fix/world-clock-meeting-city-selection-stable-2026-11-19`. PR #241 merged to main as `73e56e9abba2aa6aae9b55f35fa19d5fc93f1119`.
- Exact feature diff: only `web-source/index.html` changed (7 additions, 2 deletions). No saved city/favourite storage, planner conversion logic, APK/native code, Calendar, Smart Reminder, notes, photos, PINs/locks, or other features were edited.
- Published as **Web Update 341**. Verified `web-source/index.html` and `diary-web/index.html` are byte-identical at Git blob SHA `4dcc8f12229201d84460c081e1b75873303258d3` (556,653 bytes). Live `latest.json` web SHA-256: `d1769e22885ae2d4708b9eee7f95e122281edb50460a2097a12993033209ee7f`.
- APK metadata remains **My Diary 1.0.194 / versionCode 193**, SHA-256 `51c3a68b6febf3a7e5f9aabbb997e5c32dad9c42bd53d45f17d8b128d88dd434`; no APK was rebuilt or published for this web-only fix.
- Static diff review confirms the select options are rebuilt only when the saved city list changes. Full browser/device interaction testing remains pending; do not claim phone-side PASS until the user tests the Meeting Time Planner on their Android phone.

---

---

# Diary World Clock — typo-tolerant city search (Web Update 340, 2026-11-19)

- User reported that a few city names were not found and asked for search to work even when spelling is slightly incorrect. Implemented normalization and ranked fuzzy matching inside the existing World Clock city search.
- Search now ignores case, accents and punctuation; supports partial names and joined words such as `Newyork`; allows small spelling errors and adjacent-letter transpositions (e.g. `Londn`, `Pariss`, `Krachi`). Exact and substring matches rank before fuzzy matches. Results remain capped at 30 and already-added cities remain excluded.
- Existing worldwide time-zone options, city add/remove, saved cities and favourites, live clock, day/night, Mumbai time difference, meeting planner and sunrise/sunset tools remain.
- Only `web-source/index.html` changed: 47 additions, 3 deletions. Backup branch: `backup/before-world-clock-fuzzy-search-2026-11-19`. Feature branch: `feature/world-clock-fuzzy-city-search-2026-11-19`. PR #239 merged as `5b655294515f42f417a3f9c9f984bce866d827f0`.
- Static verification passed: World Clock block compiles; normalization, edit-distance matching, ranked results, search input, add/remove, saved cities/favourites and preservation of Calendar scheduler and Smart Reminder code verified. Diff contains only `web-source/index.html`.
- Web publisher run `44373598780` completed successfully and published **Web Update 340**. Source and mirror are byte-identical at Git blob SHA `fcae648e0b6c7e6f12aa84fb160131855ccde21c` (556,380 bytes). Published web SHA-256: `e22753e7931186c226e81a742b07a3dacf2b7acd72c4e056b99f1cf0596703c4`.
- APK workflow `44373598609` completed with failure at **Use the exact latest published Diary HTML in Android APK**; 15 later build/release steps were skipped. No APK was built or published. Published APK metadata remains **1.0.194 / versionCode 193**, SHA-256 `51c3a68b6febf3a7e5f9aabbb997e5c32dad9c42bd53d45f17d8b128d88dd434`. This remains a web-only update. Physical phone testing is pending user confirmation.

---

# Diary World Clock — smart city tools added (Web Update 339, 2026-11-19)

- User approved adding five capabilities **inside the existing World Clock modal only**: Favourite City, day/night indicator, time difference from Mumbai, meeting time planner, and sunrise/sunset.
- Favourite stars sort favourite cities to the top. Favourite selections and added cities are saved locally so favourites for newly added cities remain available after reopening the app.
- Day/night uses calculated sunrise/sunset for cities with a built-in coordinate entry. For cities without coordinates, the display is explicitly marked approximate using local clock hours; no precise solar data is fabricated.
- Time difference compares each city's current UTC offset (including daylight-saving changes) with Mumbai (Asia/Kolkata), and shows signed offset plus hours/minutes ahead or behind.
- Meeting planner takes a date and time in Mumbai and converts it to the selected city from the user's saved city list, including that city's local date/day.
- Sunrise/sunset times are calculated locally (no external API) for the supported city-coordinate list. For other searched cities the app explicitly says sunrise/sunset data is unavailable. The searched global IANA time-zone list, city add/remove, live clock refresh and timer cleanup remain.
- Only `web-source/index.html` changed for implementation: 132 additions, 22 deletions. Backup branch: `backup/before-world-clock-smart-features-2026-11-19`. Feature branch: `feature/world-clock-favourites-day-night-meeting-sun-2026-11-19`. PR #237 merged as `78efa3f3e3c5b40aba2210c0746ef26e8a084012`.
- Static verification passed: World Clock block compiles; all five feature handlers/calculations, saved city/favourite state, city search/add/remove and timer cleanup are present. IDs in the World Clock block are unique. Existing Personal Calendar scheduler and Smart Reminder code remain present. Diff contains only `web-source/index.html`.
- Web publisher run `44371498006` completed successfully and published **Web Update 339**. Source and published mirror are byte-identical at Git blob SHA `9453775e039943dd6c71ae2daa8ab01c29084849` (554,296 bytes). Publisher SHA-256: `c9e45b70cce2807abafcc10fa2c4b540213deecff8da02f849897174c59dd889`.
- APK workflow `44371497852` completed with failure at **Use the exact latest published Diary HTML in Android APK**; 15 subsequent build/release steps were skipped. No APK was built or published. APK metadata remains **1.0.194 / versionCode 193**, SHA-256 `51c3a68b6febf3a7e5f9aabbb997e5c32dad9c42bd53d45f17d8b128d88dd434`. This task is a web-only update; do not describe the APK as updated.
- Physical Android phone testing remains pending user confirmation.

---

# Diary Me menu — searchable worldwide World Clock cities (Web Update 338, 2026-11-18)

- User noticed the first World Clock release listed only a few cities and asked for the full world's city names. Replaced the small fixed dropdown with a searchable city/time-zone field.
- Search uses the browser's `Intl.supportedValuesOf('timeZone')` canonical IANA time-zone list when supported, excluding technical `Etc/*`, UTC and GMT entries. Users can search by the city label or time-zone path and tap a result to add it. An 85-zone fallback list is included for browsers without this API. This is the browser's available time-zone city list, not a literal directory of every town on earth; cities sharing a time zone may not all appear separately.
- Existing live clock rows, add/remove behavior, one-second refresh while open, modal close and timer cleanup are preserved. The feature remains isolated and removable.
- Only `web-source/index.html` changed for this improvement: 28 insertions, 32 deletions. Backup branch: `backup/before-world-clock-global-city-search-2026-11-18`. Feature branch: `feature/world-clock-global-city-search-2026-11-18`. PR #235 merged as `85c47e9032f42bd7dd40f6fdb7855c4bf52a330e`.
- Static verification: the isolated World Clock block compiles; searchable field, city/time-zone filter, add/remove handlers and interval cleanup are present. Existing Personal Calendar scheduling and Smart Reminder code remain present.
- Web publisher run `44368389747` completed successfully and published **Web Update 338**. Source and mirror are byte-identical at Git blob SHA `7d1eda89d17fef6e16585d0c8fbc58ff3d8d5191` (540,938 bytes). Publisher metadata reports web SHA-256 `8b698ad3eae1f7481e9006c4f144c0f92df6ff614b604653ff478109e4e9cacc`.
- APK workflow `44368389753` failed safely at the pre-build HTML synchronization check while publisher was syncing the mirror. No APK build or release steps ran; APK remains **1.0.194 / versionCode 193**, existing SHA-256 unchanged. This is a web-only change. Physical-device visual testing is pending user confirmation.

---

# Diary Me menu — removable World Clock added (Web Update 337, 2026-11-18)

- User asked to add a World Clock inside the Diary **Me** button and requested that it be easy to remove if they do not like it.
- Added a separate **🌍 World Clock** 3D button using the existing Me-feature button style. The clock opens in its own modal and shows live local time/date for Mumbai, Dubai, London, New York and Tokyo. Users can add or remove optional cities from a built-in list (Singapore, Riyadh, Kuala Lumpur, Sydney, Paris, Toronto, Istanbul and Doha).
- Clock refreshes once per second only while open; its timer is cleared when the clock closes or the Diary overlay is closed. The modal is hidden by default. The feature is isolated behind its own button, DOM IDs and code block so it can be removed without altering existing Me tools.
- Only `web-source/index.html` changed for implementation: 101 insertions, zero deletions. Backup branch: `backup/before-world-clock-me-button-2026-11-18`. Feature branch: `feature/me-world-clock-2026-11-18`. PR #232 merged as `4be346687152e20594661f0cb51fada0bb7b7b71`.
- Static verification: isolated World Clock block compiles successfully; one button and one modal ID; add/remove handlers and timer cleanup are present. Existing Calendar scheduler and Smart Reminder code remain present.
- Web publisher run `44367314835` completed successfully. Published **Web Update 337**. `web-source/index.html` and `diary-web/index.html` are byte-identical at Git blob SHA `b7b40fe2fbc6a7d894ca3111e93a914369bbec84` (538,606 bytes). Publisher-verified web SHA-256: `dc16836b934b762e2cc43dafd96a261915a3b9e7217b564ab305e8987b4fb444`.
- APK workflow `44367314798` was automatically triggered by the main-branch merge but failed safely at the pre-build check because the source and mirror were not byte-identical yet (the publisher was concurrently syncing the mirror). The failure occurred before the APK build/release steps; no APK was produced or published. The publisher subsequently completed successfully, and source/mirror are now byte-identical. `latest.json` retains APK **1.0.194 / versionCode 193** and its existing SHA-256. Physical Android phone visual testing remains pending user confirmation.

---

# Personal Calendar saved entries — hide Reminder ON/OFF 3D status badge (Web Update 336, 2026-11-18)

- User requested removing the 3D **Reminder ON/OFF** badge from saved entries in **📅 Personal Calendar**.
- Removed only the two-line status-badge renderer from the Personal Calendar saved-entry display. Existing event-type and time badges, details, repeat display, saved reminder state and the existing `calendarScheduleAlarms(record)` scheduling remain unchanged.
- **⏰ Smart Reminder** renderer and all other features are untouched. No saved entries or stored values were rewritten; no reminder scheduling, ringtone, snooze, notification, recurrence, PIN/lock, note/photo, or native Android code was changed.
- Pre-change snapshot branch: `backup/before-calendar-reminder-status-badge-removal-2026-11-18`. Feature branch: `fix/calendar-hide-reminder-status-badge-2026-11-18`. PR #230 merged as `c16c7831752fadccf7d441b26a3244c022a934e3`.
- Exact feature diff: one file only (`web-source/index.html`), two lines removed, zero additions. Static checks confirm the Reminder ON/OFF badge text is absent while event-type/time badges, details, repeat display, reminder scheduler and Smart Reminder renderer remain present.
- Web publisher run `44364973948` completed successfully and published **Web Update 336**. `web-source/index.html` and `diary-web/index.html` are byte-identical at Git blob SHA `1fb311486d89f5d7b461ba3e61d46cbd3422c547` (530,566 bytes). Live `latest.json` advertises web SHA-256 `e6d55a31a83e070ce966da6dfa29fb8b08cf7b780aa4ee8dc6487f6bb21a12b5`.
- APK metadata remains **My Diary 1.0.194 / versionCode 193**; this is a web-only presentation change. Physical Android phone visual testing is pending user confirmation; do not claim device-side PASS until the user confirms the Reminder badge is gone and the other Calendar entry details remain correct.

---

# Personal Calendar + Smart Reminder saved Name buttons fit the text — Web Update 335 (2026-11-18)

- User approved applying the same name 3D badge to **📅 Personal Calendar** that was already present in **⏰ Smart Reminder**, with each badge sized to its own text.
- Both saved-entry renderers now display the title/name in the existing gold 3D badge. The badge uses content-fit width, remains constrained to the card width, and wraps long names instead of causing horizontal overflow. Existing date, event-type, time, reminder-status and details rows retain their existing positions and styles.
- This is a presentation-only change: no saved entries or stored values are rewritten. Calendar/Reminder add, edit, search, bulk selection/deletion, recurrence/custom weekdays, alarms, ringtone, snooze, notifications, notes/photos, PINs/locks, native Android code and unrelated features are preserved.
- Backup branch: `backup/before-calendar-name-3d-badge-2026-11-18`. Feature branch: `fix/calendar-name-3d-badge-fit-content-2026-11-18`.
- Baseline main commit: `f36c23142ed9e8688f4eb32302c49f0b72113b4f`. Source and mirror were byte-identical before editing at blob SHA `2819019629c9317b8efacda29d87238e4ca20f8f`.
- Static verification required: both Calendar and Reminder use the name badge class; badge width fits its text and is capped at card width; long names wrap; date/type/time/reminder badges and details remain; source/mirror remain identical. Physical Android phone visual testing is pending user confirmation.
- Web publisher workflow run **44346716843** completed successfully. It verified and synchronized the HTML mirror and calculated SHA-256 `d5f7c9dcc5e459e07662ab25fd019f95b1fb20b7f5ac40a7b15865cd4cab1fe6`. The publisher repaired the checksum but, because source and mirror were already identical, did not increment the version. Metadata backup branch: `backup/before-calendar-name-badge-release-metadata-2026-11-18`.
- Release metadata advances **Check for Update to Web Update 335** with the verified SHA-256 and the new release note. APK remains **1.0.194 / versionCode 193**, SHA-256 `49b3c357bfe5ef53f9891f6238884c878797ed5012f19bde37a70aac82b76524`; no APK release is part of this web-only change.

---

# Smart Reminder saved Name, Date + Time as three 3D badges — Web Update 334 (2026-11-18)

- User pointed out that the Smart Reminder entry name was still plain text and asked to make it a button too. The saved-entry name is now its own raised gold 3D badge above the separate date and time badges. The three badges are arranged name first, then date and time below.
- Reused the existing Calendar gold 3D badge styling for the name. Added only a Smart Reminder name-badge wrapping rule so long titles wrap inside the badge instead of creating horizontal overflow. Existing date badge (gold), time badge (blue), and DD-MM-YYYY date display are retained.
- Personal Calendar saved-entry heading, renderer, and styling are unchanged. Only the Smart Reminder saved-entry name presentation changed in addition to retaining the previously completed date/time badges.
- Preservation: no saved entries or stored values were rewritten. Edit inputs, reminder details, recurrence/custom weekdays, alarm scheduling, reminder time, ringtone, snooze, notifications, notes/photos, PINs/locks, native Android code and unrelated features remain unchanged.
- Implementation backup: `backup/before-smart-reminder-name-3d-badge-2026-11-18`. Feature branch: `fix/smart-reminder-name-3d-badge-2026-11-18`. PR #226 merged as `2b119307c98bc3f596b73684c54ba60549dabc68`.
- Source and mirror are byte-identical at Git blob SHA `2819019629c9317b8efacda29d87238e4ca20f8f`. Publisher commit `1b1535d9d3cd127efa842a3477209e1419500002` recorded HTML SHA-256 `2996d26895974a53cf78b012b19ada78b837efb15a857da6febf247ac3fc1fd5` in the feed.
- This release advances the web feed to **Web Update 334**. APK fields are preserved exactly from the existing feed: **1.0.194 / versionCode 193**; no APK version change is part of this web-only task.
- Static verification: Smart Reminder title uses the 3D badge class; long-name wrapping rule is present; date/time badges and their styles remain; reminder details and non-reminder Calendar heading remain intact; source and mirror match. **Physical Android phone visual testing is pending user confirmation.**
- Metadata backup branch: `backup/before-smart-reminder-name-badge-release-metadata-2026-11-18`.

---

# Smart Reminder saved Date + Time shown as separate 3D badges — Web Update 333 (2026-11-18)

- User approved matching the **⏰ Smart Reminder** saved-entry Date and Time buttons to the existing raised 3D badge styling in **📅 Personal Calendar**. The reminder title stays above; underneath, the date and time are separate badges. Date uses the existing DD-MM-YYYY display formatter; time uses the existing saved `record.time` value.
- Reused the existing Calendar badge CSS/classes only. The Personal Calendar renderer and its styling were not changed. The previous single plain-text combined date/time line in Smart Reminder was replaced by a date badge and a time badge.
- Preservation: no saved entries or stored date/time values were rewritten. Reminder edit inputs, recurrence/custom weekdays, alarm scheduling, reminder time, ringtone, snooze, notifications, notes/photos, PINs/locks, native Android code and unrelated Diary features were not intentionally changed.
- Implementation backup branch: `backup/before-smart-reminder-date-time-3d-badges-2026-11-18`. Feature branch: `fix/smart-reminder-date-time-3d-badges-2026-11-18`. PR #224 merged as `940ada628bc8efb7a9d03acb996b6b4d66ef3ad0`.
- Only `web-source/index.html` and `diary-web/index.html` changed for the feature. After publisher sync, both files are byte-identical at Git blob SHA `008496c75cc189f1f308a82b515d9785dcc82be7`. Publisher commit `8e1234c59e8baab6c12a8145d70d1f4176e517fd` independently recorded HTML SHA-256 `e2589c917c393a92cd328cb0be9aa6b97598cb621e35807a4064221f23f32a5c` in `latest.json`.
- This release metadata advances the web feed to **Web Update 333**. APK fields remain as in the current feed: **1.0.194 / versionCode 193**, APK SHA-256 `8a20c8d51938f06067f1a9715f5bae6b382d9bbdcc0c38668e31ef8146396b80`; no APK version change is part of this web-only UI task.
- Static verification: the new reminder date and time badge elements are present; both source and mirror match; the previous combined date/time renderer is absent; the Calendar badge CSS remains present; date formatter, original edit date field, and reminder details rendering remain present. **Physical Android phone testing is pending user confirmation**; do not claim device-side visual PASS until the user checks saved Smart Reminder entries.
- Metadata backup branch: `backup/before-smart-reminder-date-time-register-2026-11-18`.

---

# Personal Calendar + Smart Reminder — saved-entry dates displayed DD-MM-YYYY (Web Update 332, 2026-11-18)

- User asked why dates inside saved entries in both **📅 Personal Calendar** and **⏰ Smart Reminder** appeared in ISO order (for example, `2026-11-19`), and approved changing the visible order to **DD-MM-YYYY** (for example, `19-11-2026`).
- Added one small display formatter for strict `YYYY-MM-DD` values and used it only in the shared saved-entry date line used by both Calendar and Reminder. Other date strings are left as-is.
- **Storage and behaviour preserved:** stored `record.date`, date input values, Calendar/Reminder recurrence calculations, custom weekday alignment, alarm scheduling, reminder time, snooze, ringtone and notifications remain in their existing format/logic. No saved entries were rewritten; no unrelated features were changed.
- Backup branch: `backup/before-calendar-reminder-date-display-2026-11-18`. Feature branch: `fix/calendar-reminder-date-display-ddmmyyyy-2026-11-18`. PR #222 merged as `8f76bbf8617ce730d54cece56dba6c9f3f7c1d5f`.
- Only `web-source/index.html` and its required `diary-web/index.html` mirror changed for the implementation. They are byte-identical at Git blob SHA `611b51d16882fc65ef07fc92a5102826db14eb3a`. The publisher then recorded the matching HTML SHA-256 `e1450da7b2323c01421be4c3ee7b253d38ed7b412f16b1768b0f0adf3caf58e5` in commit `8ba76fdb876ae9b6d984a992d9b4763a4400e011`.
- PR #223 advances `latest.json` to **Web Update 332** with the verified HTML SHA-256 and the release note for this change. APK feed fields remain `1.0.194 / versionCode 193` and APK SHA-256 `49e8534e5379faf6ac743a7674bdecf688d24732fc793f0efdb3ce9456bbc473`; no new APK version is part of this web-only change.
- Static checks: formatter appears once; shared saved-entry renderer calls it once for both target sections; sample `2026-11-19` becomes `19-11-2026`; source/mirror equality confirmed; edit form still receives the original ISO date. **Physical-phone testing remains pending user confirmation.** Do not claim device-side PASS until the user checks a saved Calendar entry and a saved Smart Reminder entry.

---

# Personal Calendar Upcoming Events section removed — Web Update 331 (2026-11-18)

- User explicitly rejected the **📅 Aane Wale Events** block and asked to remove its **7 Din**, **30 Din**, and **Sabhi** controls. Removed the complete Calendar-only Upcoming Events panel, its filtering/sorting helper, empty-state special case, and dedicated CSS.
- Restored the ordinary full Calendar entry list and the standard empty-list message. Existing Birthday / Anniversary / Important Day colour badges and **Reminder ON / Reminder OFF** badges remain in place.
- Only `web-source/index.html` and the identical `diary-web/index.html` mirror changed. No saved Calendar entries were rewritten or deleted. Calendar add/edit/save flows, alarm scheduling, Smart Reminder logic, reminder sound/notification settings, Diary notes/photos, locks/PINs and unrelated features were not changed.
- Backup branch: `backup/before-removing-upcoming-events-2026-11-18`. Feature branch: `fix/remove-calendar-upcoming-events-2026-11-18`. PR #218 merged as `393603880e1c365abd8fd4d913745f7e0f1d0517`.
- Web-only publisher run **44334304552** completed successfully. It verified and published the HTML and synced the mirror; source and mirror are byte-identical at Git blob SHA `cced801586407fb0710915bd5a8d5dd74a165bf0`. Publisher-verified HTML SHA-256: `518bf0ee024af2d377540775ff0789e298c8fc122c7646bfafb7f30659abffd6`.
- As the publisher correctly repaired the checksum without incrementing webVersion (source and mirror were already identical), PR #219 advanced `latest.json` to **Web Update 331**, retaining the verified SHA-256 and recording release notes. APK feed fields were unchanged in PR #219. PR #219 merged as `0a7214c91c4661a5538a4ea3b60b6c22ffceb8c1`.
- Main push for PR #218 automatically triggered APK workflow run **44334304530**, despite this being a web-only UI removal. The workflow completed successfully and republished the same APK version **1.0.194 / versionCode 193** (no version increment). The signing log confirms the release certificate SHA-256 fingerprint still matches the previously approved fingerprint (`23a4e93f3c7911dce18389ea583548700c6ad6a3759707f1cd222d07e2408b5a`). The signed test-candidate artifact **14440073426** was downloaded and extracted; its APK SHA-256 independently computed as `49e8534e5379faf6ac743a7674bdecf688d24732fc793f0efdb3ce9456bbc473`, matching `latest.json`. This was an automatic same-version APK rebuild for a web-only change, not a new APK release. Users already on 1.0.194 / 193 do not need to reinstall it as an upgrade.
- Static checks confirm Upcoming Events labels, filters, helper and CSS are absent; reminder ON/OFF badges remain; event-type badge renderer remains; source and mirror are identical. Physical phone testing remains pending user confirmation.

---

# Personal Calendar Upcoming Events and Reminder status — Web Update 330 (2026-11-18)

- User selected three Calendar ideas: distinct event-type colours, Upcoming Events, and Reminder status. The Birthday pink, Anniversary gold and Important Day purple badges were already present from Web Update 329, so their code was preserved without a duplicate styling change.
- Added a Calendar-only Upcoming Events control with **7 Din**, **30 Din**, and **Sabhi** options. Upcoming results are ordered by the next occurrence. Date matching covers one-time, daily, weekly, monthly, yearly and Custom weekday recurrence; date-difference calculation uses UTC calendar-day values to avoid daylight-saving boundary errors.
- Added a separate **🔔 Reminder ON / 🔕 Reminder OFF** badge to each saved Calendar entry. The indicator reflects the entry's saved reminder setting (record.remind); it does not claim to inspect Android notification permission or OS alarm delivery.
- Changed only web-source/index.html and its identical required mirror diary-web/index.html. No saved entries were rewritten or migrated. Existing Calendar form/save/edit and alarm scheduling logic were not changed. Smart Reminder, native Android code, APK identity/signing, Diary notes/photos, PINs/locks and unrelated features were not intentionally changed.
- Backup branch: backup/before-upcoming-calendar-reminder-status-2026-11-18. Feature branch: feature/calendar-upcoming-events-reminder-status-2026-11-18. Base commit: 140823bb9cd736394e225cf9de6e24757742614e. PR #214 merged as d8ee5661b38e6c1a174b88e8dfe6d33e56fc28e7.
- Web publisher workflow run 44331410134 completed successfully. Source and mirror are byte-identical at Git blob SHA c3dc57c196a0e875e5faad3e6f89c855a951f708. The publisher-calculated HTML SHA-256 is 2b5d412b1fa41c20e1d87da7dd228564383e6c3af3d2704a441c5659e15ed322.
- The publisher did not increment webVersion because source and mirror were committed together. PR #215 was merged as f60d5d95ec3a57e7f16cb7875b66773d231aa045, advancing latest.json to Web Update 330 with the publisher-verified SHA-256 and new release notes. APK feed fields were unchanged by PR #215.
- Main-branch push automatically triggered APK workflow run 44331410214 even though this was a web-only change. The workflow completed successfully and republished APK 1.0.194 / versionCode 193 (the version number did not advance) with feed SHA-256 dc210a05454ffa841c3cb3928a44c6ee2f3a4ff9de68712f72bbfa31fc469a29. The release log confirms the signing certificate SHA-256 fingerprint matched the previously approved fingerprint. Downloaded signed test-candidate artifact 14439018573; extracted APK SHA-256 independently computed as dc210a05454ffa841c3cb3928a44c6ee2f3a4ff9de68712f72bbfa31fc469a29, matching latest.json. This was an unintended automatic rebuild for a web-only change; it is not a new APK version and users already on 1.0.194 / 193 should not reinstall it as an upgrade. Feed retains Web Update 330 and the verified web SHA-256. The APK republish does not change the intended delivery of this task: Web Update 330.
- Static checks confirm source/mirror equality, the 7/30/All controls, support for all existing recurrence kinds including Custom, timezone-safe date matching, and both reminder status styles. CI/browser behaviour and physical-phone visual testing remain pending user confirmation. Do not claim device-side PASS until the user tests the Calendar screen.

---

# Personal Calendar event type and time badges — Web Update 329 (2026-11-18)

- User requested that saved **📅 Personal Calendar** entries display the selected event type and time as separate button-shaped badges. Implemented a compact pill badge for **Birthday**, **Anniversary**, and **Important Day / Zaroori Din**, plus a separate **⏰ time** badge when the entry has a time. The date remains on its existing line; title, details, repeat information and Edit control remain in their existing positions.
- Changed only the Calendar saved-entry renderer and its narrowly scoped CSS in `web-source/index.html`. The new badges are not interactive controls. Smart Reminder rendering is untouched.
- Existing saved records are read from the same fields; no data migration or record rewrite was performed. Calendar date/time values, automatic event reminders, alarm scheduling, repeat rules, ringtone, snooze, notifications, search, bulk edit/delete, PIN/locks, Diary notes/photos, native Android code, app identity and signing identity were not intentionally changed. No MUAZZIN project files were changed.
- Backup branch: `backup/before-calendar-type-time-badges-2026-11-18`. Feature branch: `fix/calendar-type-time-entry-badges-2026-11-18`. Base commit: `19b4dfaded882dfc2f5e9db1fd08f0999862ab40`. PR #212 merged as `ae73b42b6bea09455e3c772c0dd9caff644002c1`.
- Static verification: both inline JavaScript blocks compile successfully (2/2); checks confirm the type/time badges and all three event-type classes are present. Source and mirror are byte-identical at Git blob SHA `9618e4ce5f3d4d2100b72a1250001f656682890c`. Web publisher commit: `644adc17227edcf67830450d634f88a3bb416ceb`; mirror sync commit: `77f153e5f5d505e94ca973f6b1e403573e8db86a`.
- Published **Web Update 329**. `latest.json` advertises web SHA-256 `8633d1d2cc300b0974529ef1f0c536054385132c001ff834f9d8b1598dad8d70`, independently recomputed from the source HTML and verified against the feed. Release-note text identifies the new badges.
- APK remains **1.0.194 / versionCode 193**, feed SHA-256 `64b41c3632a9e06764277d9b408d479e18e778469cc6ddc13241b5530fe61f6f`; no APK rebuild or APK release was made for this web-only change.
- Physical-phone visual testing remains pending user confirmation. Do not claim device-side PASS until the user checks an existing and a new Calendar entry on their Android phone.

---

# Personal Calendar + Smart Reminder — dark-black saved and newly entered text (Web Update 328, 2026-11-18)

- User requested that the text already written inside entries in **📅 Personal Calendar** and **⏰ Smart Reminder** be dark black, and that text entered in future/new or edited entries also appear dark black.
- Added narrowly scoped CSS to the Calendar/Reminder modal only: saved-entry card text and descendants use `#000000`; text values in inputs, textareas and selects use `#000000` with a black caret. Existing bold styling and the saved-entry font sizes (title 18px, written text 16px, secondary details 14px) remain in place.
- This is a web-only display change. No saved data, entry fields, date/time, recurrence, alarm scheduling, ringtone, snooze, notifications, PIN/locks, notes/photos, native Android code or unrelated Diary features were intentionally changed.
- Backup branch: `backup/before-calendar-reminder-dark-black-text-2026-11-18`. Working branch: `fix/calendar-reminder-dark-black-entry-text-2026-11-18`. PR #209 merged as `8d59b84cd637e88994f7b342735a740a6db5838e`.
- Publisher workflow run **44325205438** completed successfully. It synchronized `diary-web/index.html` with `web-source/index.html` (both Git blob SHA `5ff172a18db34b9b84ea7d73671b702fd5bb9170`) and published **Web Update 328**. `latest.json` advertises SHA-256 `4cad1df86b85258fa111db6a0f8b7391c1b4727dc391765de3b486e1ad19a12e`.
- The repository's APK workflow was also auto-triggered by the main-branch push, but its pre-build guard stopped because the publisher had not yet synchronized the web mirror at that moment. No APK build, artifact or APK/feed version change occurred. This was a transient ordering check during the web-only publication; after the publisher completed, source and mirror were verified identical. No APK rebuild is needed for this CSS-only change.
- Physical-phone visual testing remains pending user confirmation. Do not claim device-side PASS until the user tests both sections.
- No MUAZZIN project files were changed.

---

# Personal Calendar + Smart Reminder — saved-entry text made readable (Web Update 327, 2026-11-18)

- User reported that text shown inside both new and previously saved entries looked too small. Scoped the correction to **📅 Personal Calendar** and **⏰ Smart Reminder** saved-entry cards: title **18px**, written/details text **16px**, and secondary entry details **14px**, with clear line-height. The existing bold-text modal scope applies to both old and new entries.
- This is a display-only CSS adjustment. No entry data, date/time, recurrence, alarm scheduling, reminder settings, sound, snooze, notifications, PIN/locks, notes/photos, native Android code or unrelated Diary screens were changed.
- Backup branch: `backup/before-calendar-reminder-entry-text-size-2026-11-18`. Working branch: `fix/calendar-reminder-saved-entry-text-size-2026-11-18`. Source/mirror baseline was byte-identical at blob SHA `3c8f5c35678c401d1b17560f0039592590752e35`.
- Intended release: **Web Update 327**. Source/mirror SHA-256: `c5dde45bfe8739936b6bd14ac0466b5452865dbf9cc7fdd89bd3fb7938e4af22`. APK remains **1.0.194 / versionCode 193**; no APK rebuild is intended for this web-only styling change.
- PR #208 merged as `641656e7d2159b4f5c344b1b9c68a2abac84e8e5`. Web publisher workflow run `44320549493` completed successfully. Re-fetched the live raw `latest.json`: it advertises **Web Update 327** and the expected SHA-256. Source and mirror are byte-identical at Git blob SHA `2cb462ce8f81df9ee1ea612321288ecfac905b1b`. APK build workflow run `44320549506` was still in progress at this check; no new APK version is claimed. Physical-phone visual testing remains pending user confirmation.

---

# Personal Calendar + Smart Reminder — hide event reminder settings from saved entries (Web Update 326, 2026-11-18)

- User clarified that the **“Event ke waqt yaad dilayein”** label must not appear inside saved entries in either **📅 Personal Calendar** or **⏰ Smart Reminder**, including entries already saved and all future saved entries.
- Removed only the Calendar saved-entry rendering of the reminder label and its sound/snooze/ring summary. Smart Reminder saved-entry cards did not render that label or settings summary; they remain unchanged. This is a display-only change: existing records and reminder fields are preserved, and automatic Calendar event-time reminders plus Smart Reminder scheduling remain active.
- No saved records were migrated or deleted; no form controls, alarm scheduling, repeat rules, sound, snooze, ringtone, notifications, PIN/locks, notes, photos, native Android code or unrelated screens were changed.
- Backup branch: `backup/before-hide-calendar-reminder-entry-settings-2026-11-18`. Working branch: `fix/hide-event-reminder-details-from-entries-2026-11-18`. Source/mirror baseline verified byte-identical at blob SHA `1ed44364959fff6faa8f363bf98379139f9d0629`.
- Intended web release: **Web Update 326**. Source/mirror SHA-256: `258f0894a0e5ea1280a4e1eed8d9fe9be5b4c420793dc7d7b427826adfba2416`. APK remains **1.0.194 / versionCode 193**; this is a web-only display change.
- Static verification and publication status will be recorded after the PR is reviewed/merged. Physical-phone testing remains pending user confirmation.

---

# Personal Calendar + Smart Reminder — all text bold (Web Update 325, 2026-11-18)

- User requested that all text inside **📅 Personal Calendar** and **⏰ Smart Reminder** be bold, including interface labels, existing saved/user-entered text, and text entered in new or edited entries.
- Added a narrowly scoped modal class for these two feature IDs and CSS that applies bold weight to every descendant, including saved entry cards, form labels, input values, dropdown text, PIN-related views, and input placeholders. The class is set only while either target feature is open and removed when the feature closes.
- No saved data, entry values, date/time fields, recurrence, alarm/reminder scheduling, ringtone, Snooze, notification behavior, PIN/lock logic, other Diary sections, or native Android code was changed.
- Backup branch: `backup/before-calendar-reminder-bold-text-2026-11-18`. Working branch: `fix/calendar-reminder-all-text-bold-2026-11-18`. Verified base main commit: `531c70acc42183a012bd0c5fc28bf270318efff3`.
- Intended web release: **Web Update 325**. Source/mirror content SHA-256: `9044dda18c5da0158ae5e44bf08f16b02f76cd2bf7eccf6cab1cdaf8cab3b9ac`. APK remains **1.0.194 / versionCode 193**; this is a web-only style change and no APK rebuild is intended.
- PR #205 merged as `939029e4ae0b1e71245cbbe1f8e98d3998e407b7`. Post-merge verification: source and mirror are byte-identical (Git blob SHA `1ed44364959fff6faa8f363bf98379139f9d0629`); independently recomputed source SHA-256 matches `latest.json`: `9044dda18c5da0158ae5e44bf08f16b02f76cd2bf7eccf6cab1cdaf8cab3b9ac`; feed advertises **Web Update 325**. Static checks confirm the bold class is enabled only for Calendar/Reminder (including their PIN screen) and removed on close. No workflow run or combined commit status was returned for the merge commit, and raw-host live fetch was unavailable, so external deployment is not independently verified. Physical-phone visual testing remains pending user confirmation.

---

# Custom weekday names visibility fix — Web Update 322 (2026-11-18)

- User reported that the weekday names inside the **Custom** selector were not clear/readable on mobile.
- PR #201 merged the styling-only correction: two columns on narrow/mobile screens, three columns on wider screens, 15px extra-bold weekday labels, larger 20px checkboxes, separate high-contrast selectable cards with 44px minimum height.
- Applied the same exact CSS block to both `web-source/index.html` and `diary-web/index.html`. Verified the files are byte-identical after merge (Git blob SHA `924b766097b294b1a6fb69f647e846d820e1a12b`).
- Published **Web Update 322** in `latest.json`; source SHA-256: `a36405b56ad40bbf6b2e895c7b50a408cd08523b369dd2a51d7843d0d54b1ca6`. APK remains **1.0.194 / versionCode 193**; no APK rebuild was needed for this CSS-only adjustment.
- Scope was limited to the weekday-control style block and web update metadata. No repeat logic, saved records, calendar/reminder scheduling, alarms, snooze behavior, PINs, locks, notes, photos or unrelated features were changed.
- Backup branch: `backup/before-custom-weekday-visibility-2026-11-18`; register backup branch: `backup/before-custom-weekday-visibility-register-2026-11-18`.
- **Physical-phone visual verification remains pending.** CI/source checks and published metadata do not prove the weekday names look correct on the user's device.
- No MUAZZIN project files were changed.

---

# Personal Calendar + Smart Reminder — Custom weekday repeat released (2026-11-18)

- Added a **Custom** repeat choice to both **📅 Personal Calendar** and **⏰ Smart Reminder**. Users can select the weekdays Monday through Sunday; the chosen days are saved with the entry and restored when editing it.
- Calendar keeps its previous None, Daily, Weekly, Monthly and Yearly choices. Smart Reminder keeps its previous None and Daily choices. Custom recurrence is only offered when the installed native Android bridge supports `scheduleReminderCustom`, so older APKs retain their existing options instead of showing a non-working control.
- Native Custom weekday scheduling is carried through alarm rescheduling/restoration, manual Snooze and unanswered repeat handling, and reboot restoration. Existing saved records and unrelated Diary features were not intentionally changed.
- PR #196 merged the Custom weekday implementation. PR #197 added the safety gate preventing the Custom web UI from being advertised to APKs without the matching native scheduler.
- Release: **My Diary 1.0.194 / versionCode 193** and **Web Update 321**. APK release workflow run **44300687581** completed with conclusion **success**. Published APK SHA-256: `8658fb0065dc0d05ac9cd9ba0ff19bebd1091845ad68ea3c31ccb3a3f41fb0f7`. Published web bundle SHA-256: `f56fb658f96bb705bb8aa13f18ebfc4770d45f7b3025cd67b25e159ebce73f4d`.
- Verified on main: `web-source/index.html` and `diary-web/index.html` are byte-identical (Git blob SHA `7fceaaff45158895c70357c3a6c8f2a468a4a6f9`).
- Backup branch for this register update: `backup/before-custom-repeat-register-2026-11-18`. Documentation branch: `docs/custom-repeat-calendar-reminder-release-2026-11-18`.
- **Physical-phone testing of Custom weekday repeat is pending user confirmation.** The successful CI/release build is not a claim that the new repeat behavior has passed on the user's phone.
- No MUAZZIN project files were changed.

---

# Personal Calendar + Smart Reminder search results placement — Web Update 320 phone test confirmed (2026-11-18)

- User confirmed physical-phone testing is complete and the requested behavior works correctly in both **📅 Personal Calendar** and **⏰ Smart Reminder**: matching search results appear immediately below the Search Bar.
- This confirms device-side PASS for this specific search-results placement change only. It does not imply that other pending phone tests have passed.
- PR #194 was merged and **Web Update 320** was published. This is a web-only change; APK remains **1.0.193 / versionCode 192**.
- No further code changes were made for this test confirmation. Existing Calendar/Reminder records, forms, scheduling, alarms, PINs, locks, notes, photos and unrelated features remain unchanged.

---

# Personal Calendar + Smart Reminder search moved above Name — Web Update 319 published (2026-11-18)

- User approved moving the existing **Smart Search** field in both **📅 Personal Calendar** and **⏰ Smart Reminder** to immediately above the **Name** field.
- Changed only the form assembly in `web-source/index.html`: the existing search input is moved into a small search panel at the top of the existing Calendar/Reminder form. Its placeholder, input listener and saved-entry filtering remain the same. No duplicate search control is created.
- The existing Edit-mode rule still hides the form while bulk selection is active; the search therefore hides with the form and returns above Name when Edit mode ends. Other feature search/tool placement is unchanged.
- Preserved all form fields, saved entries, automatic Calendar reminders, Smart Reminder scheduling, alarm IDs, Snooze/repeat settings, bulk selection/deletion, PINs, locks, notes, photos, native Android code and unrelated screens.
- Backup branch: `backup/before-searchbar-move-calendar-reminder-2026-11-18`. Working branch: `fix/move-calendar-reminder-searchbar-above-name-2026-11-18`. Base main commit: `71d62d05ccdbf4a86aeb687792550012d9dd62e1`.
- PR #193 merged as `379bc26af4a544b6885bfb7f08a39ba9f01d060e`. Exact reviewed diff: one file only (`web-source/index.html`), one insertion and one deletion in the form assembly.
- Published **Web Update 319**. `web-source/index.html` and `diary-web/index.html` were re-fetched and verified byte-identical at Git blob SHA `18bd4b2f056a1ed956d193aae86cd9d7f703c9ad`. Live `latest.json` advertises web SHA-256 `4367839475b33d3ffada14eb466dd73d1734dde46464db26995920e2fd587722` and Web Update 319.
- APK remains **1.0.193 / versionCode 192**, SHA-256 `b21819e3af1a8a4338218ce70604b4bbd056888df3e23633c5b3d05a8e881dd4`; this is a web-only change and no APK/native release was made.
- Repository/feed/mirror verification: PASS. Physical-phone visual testing in both screens remains pending; do not claim device-side PASS until the user confirms.

---

# Personal Calendar PDF Report button removed — Web Update 318 published (2026-11-18)

- User requested removal of the **PDF Report** button from **📅 Personal Calendar** because it is not needed.
- Changed only the report-button condition in `web-source/index.html`: the report button is now created for **My Kharcha** only, not Personal Calendar. The My Kharcha report/export remains available. The existing Calendar report helper remains untouched; no Calendar records, event forms, automatic reminder scheduling, alarm settings, Smart Reminder, or other features were changed.
- Backup branch: `backup/before-remove-calendar-pdf-report-2026-11-18`. Working branch: `fix/remove-personal-calendar-pdf-report-2026-11-18`. Base main commit: `5dd4be0a1fa3306deadb60bca643943c2a0c8aee`.
- PR #192 merged as `88a96f5d4b92accd9637a8e49e79f9b7f9df7851`. Exact diff: one condition line changed in one file (1 insertion, 1 deletion).
- Web publisher workflow run `44268386537` completed successfully. Published **Web Update 318**; `latest.json` advertises web SHA-256 `fa6ade8952b13b45f96f1c2769463683e3a9dddecb891756a947c333c3ef0dac`.
- Verified `web-source/index.html` and `diary-web/index.html` are byte-identical at Git blob SHA `8cae2b71de06abe190481814921d699ff2513c9f`. Static checks confirm the Calendar report-button condition is absent and the My Kharcha report button remains.
- This is a web-only release; no APK/native code or APK version was changed. Physical-phone visual confirmation that the Calendar button is gone remains pending; do not claim device-side testing.

---

# Permanent My Diary work-safety procedure (user-confirmed, 2026-11-18)

This procedure applies to every future My Diary task. Follow it before making changes; it reduces avoidable mistakes but does not guarantee that software can never contain a defect.

1. **Read the register first:** Open this file and review the project map, secrets-handling notes, current release state and relevant recent change history before touching code.
2. **Verify the live baseline:** Check the default branch, current `latest.json`, published web/APK versions and hashes, and the actual target files. Never assume a remembered version or old Library copy is current.
3. **Stay in the correct project:** Work only in the My Diary repository and the exact feature/file the user requested. Never modify Muazzin or unrelated projects.
4. **Back up before editing:** Create a clearly named backup branch from the verified current main commit. Create a separate task branch from that same baseline. Confirm both branches exist before changing files.
5. **Make the smallest scoped change:** Inspect the relevant implementation and its callers first. Change only what is necessary for the requested behavior. Preserve existing working features, saved records, photos, notes, PINs, locks, reminder/calendar settings, alarm scheduling, app identity and signing identity unless the user explicitly requests a change.
6. **Protect user data and secrets:** Do not expose, copy into logs, or alter secrets, signing keys, credentials or private user data. Do not run destructive migrations or reset user data as a shortcut.
7. **Review the exact diff:** Confirm only intended files and lines changed. Check for accidental deletions, duplicate handlers, changed IDs, broken event flow, unintended style spillover and unrelated modifications. If scope is unclear or risk is material, stop and ask the user rather than guessing.
8. **Verify before merging:** Run the relevant syntax, static, project-specific and build checks. For web releases, verify source/mirror byte equality and the exact published SHA-256/version feed. For APK releases, verify build success, signing-certificate continuity, artifact SHA-256 and both download/update-feed metadata as applicable. A web-only change must not be described as a new APK release.
9. **Fail closed:** If the register, repository, baseline, backup, required file, build, checksum, mirror, signing check or publication state cannot be verified, do not merge or publish on assumptions. Report the blocker clearly and wait.
10. **Merge and publish carefully:** Merge only the reviewed task branch after required checks pass. Confirm the resulting commit and actual workflow result. Verify the live feed and deployed artifacts after publication; do not infer success merely from a PR merge or workflow start.
11. **Record every completed change:** Update this same Master Register with the request, exact files/scope, preserved behavior, backup/work branches, PR/commit, tests, workflow run, published versions and hashes, and any remaining device tests. Verify the register update itself.
12. **Be honest about phone testing:** Clearly separate repository/build/publication verification from physical-device testing. Never say a feature is fully tested or “ALL OK” until the relevant phone behavior has actually been confirmed by the user or a valid device test.
13. **Keep communication clear:** Explain what changed and what did not change in concise Roman Hindi when appropriate. If a defect is reported, inspect the actual current code and release first; do not blame the user, repeat an unverified claim, or hide a failed attempt.

**Standing priority:** correctness, data preservation and narrow scope are more important than speed. No unrelated feature is to be touched merely to make a task easier.

---

# Personal Calendar + Smart Reminder — show the saved entries themselves at the top in Edit mode (2026-11-18)

- User clarified that the entries—not just the action bar—must appear immediately below the top Edit controls so each can be checked without scrolling past the add form or tools.
- Updated only `web-source/index.html`: in Edit mode, the existing `meFeatureList` is moved to the first child of the feature content, above the form; the add/edit form and tools/search are hidden; any previous search term is cleared so all saved Calendar/Reminder entries are listed. The screen scroll is reset to the top.
- Tapping Done restores the existing form, tools and list order. No entry data, alarm/reminder schedules, PINs, locks, notes, photos, native Android code or unrelated features are changed.
- Backup branch: `backup/before-calendar-reminder-entry-list-top-2026-11-18`. Working branch: `fix/calendar-reminder-entry-list-top-2026-11-18`.
- PR #186 merged as commit `c7b60fa83086fa11417a0603735de4d28c254a56`; web publish workflow run #370 completed successfully and published **Web Update 315**. Source/mirror byte equality and feed SHA were verified. Physical-phone testing remains pending.

---

# Personal Calendar + Smart Reminder Edit actions pinned at the top — Web Update 314 published (2026-11-18)

- Moved the selected-count / **Delete Selected** action bar to a direct child immediately below the feature header and made it sticky while scrolling. The existing checkbox selection, delete behavior, reminder cancellation and calendar alarm cancellation were retained; the saved entry list itself was not moved in this first pass.
- No saved records, alarms, reminder settings, forms, PINs, locks, photos, native Android code or unrelated screens are changed.
- Backup branch: `backup/before-calendar-reminder-bulkbar-top-2026-11-18`. Working branch: `fix/calendar-reminder-bulkbar-top-2026-11-18`.
- PR #184 merged as commit `1e7ed40e86bb6145d5b4de054b6c8acef6db84ec`; web publish workflow run #369 completed successfully. The Check for Update feed now advertises `webVersion: 314`.
- Verified `web-source/index.html` and `diary-web/index.html` are byte-identical (Git blob SHA `40b4921742d6e65ac023e385028c1b9083d74cf4`); the feed advertises SHA-256 `144f8110217fa625603e12517d648283cec1c94b3c1d89baaea5c335f65c4f7c`.
- The separate APK workflow run #345 was triggered by the main-branch push but failed at its pre-build HTML source/mirror equality guard because it checked out the commit before the web publisher synchronized the mirror. It did not build or publish an APK. The already-published APK feed fields remain 1.0.193 / versionCode 192; no native Android files were changed.
- Physical-phone testing remains pending. Do not claim device-side PASS until the user installs Web Update 314 and tests both screens.

---

# Personal Calendar + Smart Reminder Edit mode and multi-select delete — included in Web Update 314 (2026-11-18)

- User requested an **Edit** option in the upper-right three-dot menu on both **📅 Personal Calendar** and **⏰ Smart Reminder**, so saved entries can be selected with checkboxes and deleted together.
- Added the ⋮ menu only to these two feature screens. Selecting **Edit** enters selection mode, displays a checkbox on each matching saved entry, shows the selected count and a **Delete Selected** action; selecting **Done** exits and clears the selection.
- Bulk deletion uses the existing Diary feature IndexedDB records. For Smart Reminder, each deleted record's native reminder is cancelled through the existing `DiaryAppActions.cancelReminder`; for Personal Calendar, the record's scheduled alarm IDs are cancelled through the existing `calendarCancelAlarms`. Existing per-record edit/delete actions remain available outside selection mode.
- Preserved the existing add/edit forms, reminder settings, alarm scheduling, calendar repeat rules, saved record schema, notes, PINs, locks, photos and all unrelated screens. No native Android scheduler code or user data is changed.
- Backup branch: `backup/before-calendar-reminder-bulk-delete-menu-2026-11-18`. Working branch: `feat/calendar-reminder-edit-select-delete-2026-11-18`. Base main commit: `c836df7b2d7c5b763b8882c036d21fb461b24181`.
- Initial implementation merged in PR #183 and is now included in Web Update 314 together with the top-bar layout correction. Source/mirror synchronization and feed SHA verification passed. Physical-phone testing remains pending.

---

# Exact Snooze interval timing correction — 1.0.192 / versionCode 191 (2026-11-18)

- Follow-up inspection of the released 1.0.191 receiver found the exact timing defect behind a 2-minute setting behaving like roughly 4 minutes: `ACTION_AUTO_SNOOZE` fired at the selected interval but only scheduled a further `ACTION_ALARM`, rather than ringing at that point. The next audible alarm therefore occurred one additional interval later.
- Corrected the shared native receiver used by both **Personal Calendar** and **Smart Reminder**. The auto-snooze event now immediately refreshes the notification and starts the alarm sound when its timer fires; it then schedules the next auto event exactly one selected interval later, subject to the configured repeat limit.
- The same `snoozeUsed` counter is incremented at each unanswered repeat, and no further repeat is scheduled after the configured limit. The initial alarm plus 3× therefore yields three additional rings at the configured interval, then stops.
- Preserved manual Snooze behavior, Done cancellation, ringtone settings, daily recurrence, exact AlarmClock scheduling, boot restoration, saved reminders and all unrelated app features. No web UI or user data is modified.
- Backup branch: `backup/before-auto-snooze-ring-timing-fix-2026-11-18`. Working branch: `fix/auto-snooze-ring-at-interval-1-0-192-2026-11-18`.
- Bumped the signed release to **1.0.192 / versionCode 191** because the app updater only installs a higher versionCode. Build-time guards now verify that the auto event rings immediately and re-schedules the next repeat with the selected interval and limit.
- Device-side timing/ringtone testing remains required after installing the signed 1.0.192 APK. Do not claim phone-side PASS until the user verifies both features.

---

# APK release version bump for Snooze fix — 1.0.191 / versionCode 190 (2026-11-18)

- The native Snooze/repeat-limit repair is included in the shared scheduler used by Personal Calendar and Smart Reminder.
- Verified the updater's native comparison: it downloads and installs the APK only when feed `versionCode` is greater than the installed app's `currentVersion()`. The installed/current published release is **1.0.190 / versionCode 189**, so rebuilding the same version would not deliver the native fix through Check for Update.
- Created backup branch `backup/before-release-version-bump-snooze-fix-2026-11-18` and working branch `fix/release-version-1-0-191-snooze-limit-2026-11-18`.
- Advanced the approved signed release to **1.0.191 / versionCode 190** and adjusted the fail-closed feed guard to accept the current 1.0.190/189 feed or the exact new 1.0.191/190 release. Updated release notes and artifact names to describe the configured repeat limit.
- This is a release-number change only; no user data, reminder settings, web UI, notes, PINs, locks, photos or unrelated features are changed. The prior 1.0.190 APK remains the installed baseline until the new signed release passes all checks and is published.
- The native build run triggered by the Snooze-fix merge used the old 1.0.190 version; a new push with the bumped version will supersede it under the workflow's existing concurrency policy.
- Do not claim the fix is available on the phone until the 1.0.191 signed APK and update feed are published and the user installs it.

---

# Snooze interval and repeat limit — Personal Calendar + Smart Reminder (2026-11-18)

- User reported that the selected **Snooze Ka Waqfa** and **Dobara Aane Ki Had** did not appear to behave consistently in both **📅 Personal Calendar** and **⏰ Smart Reminder**.
- Inspected the actual web form values and native Android bridge. Both features already pass the selected interval in minutes and repeat limit as separate values to the same shared native reminder scheduler. The interval is scheduled in milliseconds as `snoozeMinutes * 60 * 1000`; the selected 2-minute interval calculation is retained.
- Found the confirmed defect: unanswered automatic repeats were explicitly independent of the configured repeat limit, and the auto-repeat receiver did not increment the shared repeat counter. This allowed unanswered alarms to continue beyond the selected 3×/5×/10× limit.
- Minimal fix in `scripts/add_diary_app_actions.py`: automatic unanswered repeats now increment the same `snoozeUsed` counter as manual Snooze; no next automatic repeat is scheduled once the configured limit is reached; reboot restoration also refuses to restore an over-limit auto-repeat. The initial alarm plus 3× therefore means three additional alarms at the selected interval, then stops. The existing Done/manual Snooze actions, sound, notification, exact AlarmClock scheduling, daily recurrence and boot restoration remain in place.
- This is a shared native scheduler, so the fix applies to both Personal Calendar and Smart Reminder. No web UI, reminder/calendar records, notes, PINs, locks, photos or unrelated features were changed.
- Backup branch: `backup/before-snooze-repeat-limit-calendar-smart-reminder-2026-11-18`. Working branch: `fix/snooze-repeat-limit-calendar-smart-reminder-2026-11-18`.
- Added a build-time guard to verify the repeat counter, configured limit, interval conversion and reboot-restoration limit remain present.
- Phone-side timing/ringtone testing is still required after installing the newly built signed APK; do not claim device-side PASS until the user tests both features.

---

# Check for Update APK download HTTP 404 — root cause fixed (2026-11-18)

- User reported the Android **Check for Update** flow repeatedly failed with **HTTP 404**. Checked the live update feed and the actual repository file tree rather than assuming a network issue.
- Confirmed the feed advertised `My-Diary-1.0.190.apk`, but that exact path did not exist in the repository. The signed 1.0.190 APK was present at the stable `My-Diary.apk` path instead. Independently downloaded the signed test-candidate artifact and verified its APK SHA-256 `9f35d969da8031ad7b6925748c97b2e5ba9e8b0e97f0500eaabf244f6c5599e5`; its Git blob SHA `fc92bec722edd3e2f15189a9a1f432c892c222e4` exactly matches the existing `My-Diary.apk` repository blob (2,058,374 bytes). Thus the checksum and APK were correct; only the advertised URL was wrong.
- Created backup branch `backup/before-check-for-update-apk-url-fix-2026-11-18` and working branch `fix/check-for-update-apk-url-404-2026-11-18`.
- Corrected the live feed URL to the verified existing `My-Diary.apk` path while retaining version **1.0.190 / versionCode 189** and the matching SHA-256. Corrected the Android build publisher so future releases advertise the same stable path and also stage the versioned APK artifact that the workflow already copies; corrected the stale publish commit message.
- PR #177 merged to `main` as `30368a7a881af73ce029e77c133efcfc1ff79177`. Re-fetched live `latest.json` from main and confirmed it now advertises `My-Diary.apk`, version **1.0.190 / versionCode 189**, and the exact verified SHA-256. Re-checked the main-branch root listing: `My-Diary.apk` exists at 2,058,374 bytes with Git blob SHA `fc92bec722edd3e2f15189a9a1f432c892c222e4`, matching the independently downloaded signed APK candidate byte-for-byte. The build workflow correction is also present on main. Backend URL/path verification: PASS. Phone-side retry remains untested; do not claim the user's device has completed the update until they retry Check for Update.

---

# Signed Release Gradle retry recovery — build #337 running (2026-11-18)

- The signed Release Gradle command in the APK workflow did not advance during run #336 after Debug APK succeeded. The signed Release step had no retry wrapper, unlike the debug build.
- Created backup branch `backup/before-signed-release-gradle-retry-2026-11-18` and working branch `fix/signed-release-gradle-retry-2026-11-18`.
- PR #175 merged as `1b334321f55bd3ce8b12a70a08641f1d00058d5c`. The signed Release Gradle task now retries up to three times after transient dependency/build failures. This is a workflow-only change; Android app source and Web Update 313 are unchanged.
- Created register backup branch `backup/before-signed-release-retry-register-2026-11-18`.
- New APK workflow run #337 (`44164281065`) has started and is currently in progress at checkout. Run #336 (`44163380545`) has not published an APK.
- Live feed remains **1.0.189 / versionCode 188**, Web Update **313**. Do not provide a 1.0.190 link until signed APK, certificate fingerprint, checksum, and live feed are all verified. Phone-side alarm testing remains pending.

---

# Unanswered Smart Reminder and Personal Calendar alarm auto-repeat — code merged, APK build pending (2026-11-18)

- User requested that unanswered alarms automatically ring again using the configured Dubara/Snooze interval until the user chooses Done or Dubara. Manual Dubara continues to use the saved interval and existing manual snooze limit; Done cancels the automatic fallback.
- PR #171 merged the native Android auto-repeat implementation, including persistence/restoration of pending fallback alarms across device restarts and cancellation when the user acts.
- PR #172 merged a narrow safety fix: editing/replacing a reminder cancels its old pending automatic fallback before scheduling the new reminder.
- PR #173 merged build recovery safeguards: Gradle debug and release tasks retry up to three times after transient failures; a newer build can replace a stalled pre-publication run.
- Backup branches: `backup/before-unanswered-reminder-auto-repeat-2026-11-18`, `backup/before-reminder-edit-clears-auto-repeat-2026-11-18`, and `backup/before-gradle-retry-recovery-2026-11-18`.
- APK workflow #334 (run `44162183553`) failed at debug build after a Maven Central HTTP 429. Workflow #335 (run `44162965892`) passed debug build but was cancelled during release configuration when recovery run #336 superseded it.
- Workflow #336 (run `44163380545`) is the current retry build. Its latest observed state is in progress during checkout; no signed APK or new release has been verified.
- Live `latest.json` remains **1.0.189 / versionCode 188**, Web Update **313**. `web-source/index.html` and `diary-web/index.html` match at blob SHA `c3bd19ebcf025b14e22c662a5b5e0119c73cd18f`.
- Do not publish or provide a 1.0.190 download until the workflow completes all release/signature/checksum/feed validation steps. Phone-side alarm testing remains pending; do not claim it is confirmed on-device.

---

# Private Locker Favourite Name centered and sharpened — Web Update 313 (2026-11-18)

- User asked that the Favourite Name box text be centered, sized to the box, and clearer rather than blurry.
- Inspected the actual Private Locker CSS and dynamic input creation. Found the earlier 14px placeholder rule was not enough: a broad Private Locker 3D text rule was still applying a multi-layer text shadow, and the recovery flow explicitly set text alignment to left.
- Created pre-edit backup branch: `backup/before-private-locker-favourite-name-center-crisp-2026-11-18`. Working branch: `fix/private-locker-favourite-name-center-crisp-2026-11-18`.
- Replaced only the Favourite Name text-input presentation rule: typed name remains bold 17px, centered, dark and with no text shadow; placeholder is bold 15px, centered, fully opaque, no letter spacing and no text shadow, kept on one line. Existing field dimensions and PIN/password styling are unchanged.
- Only `web-source/index.html` changed. PR #170 merged as `ccfe2d90ecb47ba6627026418a289ce771cb7d21`. Static diff: 16 additions, 2 deletions, one file only. No PIN logic, recovery logic, encryption, saved data, Diary Lock, Note Lock or unrelated features changed.
- Publisher workflow run `44157570967` (run #365) completed successfully. Published as **Web Update 313**. Source and `diary-web/index.html` mirror match at Git blob SHA `c3bd19ebcf025b14e22c662a5b5e0119c73cd18f`. Live `latest.json` advertises webVersion `313` and SHA-256 `a4c01e685b529282e05b552a8ae8377a6df5bbcd3b930ca7799179561d167f6a`. APK remains `1.0.189 / versionCode 188`; this was a web-only CSS change and no APK rebuild/release is claimed.
- Phone-side visual confirmation remains pending. Ask the user to install/check Web Update 313 and confirm the Favourite Name prompt and typed text are centered and crisp.

---

# Private Locker Favourite Name prompt fit — Web Update 312 (2026-11-18)

- User reported that text in the **Favourite Name** box was being clipped. Inspected the exact Private Locker setup and recovery fields. The fields are text inputs, distinct from the PIN/password inputs, so the existing PIN placeholder rules did not govern their prompts.
- Created pre-edit backup branch: `backup/before-private-locker-favourite-name-fit-2026-11-18`. Working branch: `fix/private-locker-favourite-name-fit-2026-11-18`.
- Added one narrowly scoped CSS rule for `#diaryPrivateLockerModal input[type="text"]::placeholder`: 14px placeholder text, 1.2 line-height, no letter spacing, and a single unbroken line. The typed Favourite Name text remains at its existing 17px size.
- Only `web-source/index.html` changed. PR #169 merged as `18ce542a8683db711aa3e281f010fd55cc54c8bd`. Static diff: 8 additions, 0 deletions, one file only. No PIN validation, recovery logic, encryption, saved Private Locker records, Favourite/Pin note features, Diary Lock, Note Lock, or other app features were changed.
- Web publisher run `44156184855` (run #364) completed successfully. Published as **Web Update 312**. Source and `diary-web/index.html` mirror are byte-identical at Git blob SHA `d465bf08e6c271c79b057ae351fe000ed43769a1`. Live `latest.json` advertises webVersion `312` and web SHA-256 `f309d85ff221939202d16ee7e2384d866c44f4b2d55eb005bbb07107657ad8ea`. APK remains `1.0.189 / versionCode 188`; no APK was built or published for this CSS-only change.
- The automatically triggered APK workflow run `44156184929` failed at the pre-build step **Use the exact latest published Diary HTML in Android APK**; all build/sign/publish steps were skipped. No APK artifact or APK version change is claimed. Phone-side visual confirmation remains pending; do not claim the prompt is confirmed unclipped on the user's Android phone until the user checks Web Update 312.

---

# Diary Lock PIN boxes re-measured after final sizing review — pending publication (2026-11-18)

- User asked for another careful review so longer PIN prompt text must never be cut off.
- Found a real ordering issue in Web Update 310: all three Diary Lock PIN routes called the measurement helper before assigning the input's inline width/height/padding/border. The helper therefore initially measured an unstyled/default box; later observer callbacks were not a reliable substitute for measuring only after the final style was applied.
- Created pre-edit backup branch: `backup/before-diary-lock-pin-final-fit-review-2026-11-18`. Working branch: `fix/diary-lock-pin-final-fit-review-2026-11-18`.
- Corrected all three routes so the actual box styles are applied first and the placeholder fitter runs afterward. Standardized the three PIN fields to a 60px minimum height with 10px vertical padding, preserving their existing border treatments and 22px typed-PIN digit styling. The fitter still measures actual rendered width/height, padding, borders and placeholder font, reserves 3px on both horizontal sides, and caps short/medium/long prompts at 24/19/17px subject to actual fit.
- Only the three Diary Lock PIN prompt fields in `web-source/index.html` were changed. PIN logic, PIN values, recovery, Pattern, Fingerprint, Note Lock, Private Locker, notes and all other features remain untouched. Static diff is limited to 3 lines changed (three field initializers). Phone visual confirmation remains pending; do not claim no clipping on-device until user checks.
- PR #168 merged to `main` as `e7c8ec532bf5430fe78d2c3582448f0c4a43e0c7`. The corrected source blob on main is `f754b50f28a0e45062fa548bc373ea0a9914cc9a`.
- Publisher workflow run `44154789679` (run #363) completed successfully. Published as **Web Update 311**. Verified `web-source/index.html` and `diary-web/index.html` match at Git blob SHA `f754b50f28a0e45062fa548bc373ea0a9914cc9a`; `latest.json` advertises `webVersion: 311` and SHA-256 `694770955640897de58cb4e67ba7a7b64076bb3c38ef2513b44a7a533d86c669`. APK remains `1.0.189 / versionCode 188`; this was a web-only update, no APK rebuild or release is claimed. Static publication checks PASS. Physical Android phone visual confirmation remains pending; user can now Check for Updates and inspect the three Diary Lock PIN prompts.

---

# Diary Lock PIN prompt actual-box fitting — Web Update 310 (2026-11-18)

- User asked to apply the same measured box/text sizing discipline used for Note PIN to Diary Lock.
- Created pre-edit backup branch: `backup/before-diary-lock-pin-box-fit-2026-11-18`. Working branch: `fix/diary-lock-pin-box-fit-2026-11-18`. PR #167 merged as `884085ab569d4d6cf4a6f9d9859fa54beed1c705`.
- Source inspection found Diary Lock PIN placeholders hard-coded to a viewport clamp of 13–17px, even though its PIN inputs render at roughly 54px high. Three PIN entry routes exist: initial PIN setup, PIN entry to turn Diary Lock off, and regular Diary unlock/recovery flow.
- Replaced only the Diary Lock PIN placeholder sizing rule and added a measured fit helper for all three routes. It reads the rendered input's actual width/height, padding and borders; keeps 3px clear space on both sides; chooses the largest fitting size with short/medium/long targets 24/19/17px; and recalculates after DOM insertion and resize.
- Publisher run `44153682085` completed successfully and published **Web Update 310**. Source and `diary-web/index.html` mirror match at Git blob SHA `3a72117b20580d650d3c8db0c91b9812cdbc7112`. Live `latest.json` advertises webVersion `310` and bundle SHA-256 `8de49cc0cfb71931aefff248f506cee959267ab98c2060f6ee272d34be559d64`.
- Typed PIN digit size, PIN validation, recovery, Pattern/Fingerprint behavior, stored PINs, notes, Note Lock, Private Locker and other features are unchanged. Android phone visual confirmation remains pending.

---

# Note PIN placeholder balanced to actual box size — Web Update 309 (2026-11-18)

- User reported that Web Update 308 still made the Note PIN placeholder much too large. The earlier 34/23/20px targets were too aggressive for the actual 54px PIN field.
- Created pre-edit backup branch: `backup/before-note-pin-balanced-box-sizing-2026-11-18`. Working branch: `fix/note-pin-balanced-box-sizing-2026-11-18`. PR #166 merged as `9c7d3a52035bf5dd35bd3a08b742064013a528de`.
- Changed only the presentation helper in `web-source/index.html`: short/medium/long placeholder targets are now 24/19/17px, capped by the actual rendered inner height. Width is measured from the actual input box after padding/borders, preserving 3px clear space on each side; canvas measurement uses the placeholder's computed font family/weight. ResizeObserver and post-layout remeasurement remain.
- Publisher run `44152560190` completed successfully and published **Web Update 309**. Source and `diary-web/index.html` mirror are byte-identical at Git blob SHA `2813cbf9c743f4dbd0aeddc266248e449e95a107`. Live `latest.json` advertises webVersion `309` and bundle SHA-256 `d8cbd41d3d5437e29baeb01240da8b790931b86905ec0d0d15e2e78b5517871d`.
- Typed PIN entry, validation, recovery, encryption, notes, locks, and all other app features are untouched. Android phone visual confirmation remains pending; do not claim device-side PASS until the user checks it.

---

# Note PIN prompt exact box fit with 3px side gaps — Web Update 308 (2026-11-18)

- User clarified that simply enlarging the Note PIN prompt text caused it to shift/clip at the left and right. Required fit: match the real PIN box's inner width, leave exactly 3px clear space on each side, and show the entire prompt on one line.
- Replaced the earlier estimated-width sizing with actual `getBoundingClientRect()` width minus computed padding, border and 6px total side gap. A canvas measurement and binary search selects the largest font up to the short/medium/long target (34/23/20px) that fits. A `ResizeObserver` and post-layout animation-frame measurement recalculate once detached modal inputs are attached and if the box resizes.
- Only `web-source/index.html` changed in PR #165, merged as `05fe9199a020ee99212fcb787debe787fa1fb5b5`. Backup branch: `backup/before-note-pin-exact-fit-3px-2026-11-18`.
- Publisher run `44151054153` completed successfully. Published **Web Update 308**. Source/mirror Git blob SHA: `bebfaad27a9222e3858441638748e7d8d2495537` (identical). Published SHA-256: `e2dbd4e33597b98128c2e96493ad24060261b6884ab151f70275d3a2a0d256d0`. Live feed now advertises Web Update 308.
- No typed PIN behavior, PIN validation/recovery, saved notes, locks, or other features changed. Static publication checks PASS. Actual Android phone visual confirmation remains pending; user should verify that the full placeholder text has a visible 3px gap on both sides.

---

# Note Lock PIN prompt text enlarged without clipping — Web Update 307 (2026-11-18)

- User requested that short text shown in the **Note PIN boxes** be made double-sized, while longer prompt text should be enlarged moderately and never be cut off.
- Added a presentation-only helper for both existing Note Lock PIN prompt routes. Short placeholders target 34px; medium/long placeholders target 23px/20px, with canvas text-width measurement and mobile viewport fitting to reduce the size only when needed to keep the full prompt visible. The existing placeholder styling now reads that per-input size.
- Only `web-source/index.html` changed. No typed PIN digit sizing, PIN validation, unlock/recovery handlers, encryption, saved notes, Diary Lock, Private Locker, or other features were changed.
- Backup branch: `backup/before-note-pin-placeholder-text-size-2026-11-18`. Working branch: `style/note-pin-placeholder-text-size-2026-11-18`. PR #164 merged as `84a1d1d47ed962b1c4a546e50d7614d90e4644c3`.
- Web publisher run `44149994876` completed successfully. Published as **Web Update 307**. Source and mirror are byte-identical at Git blob SHA `444edae0500a1602e36b0c11378a930baf5567ee`; published bundle SHA-256 is `8559c009e959b4757961dd4dfba7d28dbab1cf46d1b5fb0dd16b20c341ed3075`. Live `latest.json` advertises Web Update 307 and the matching checksum. APK remains `1.0.189 / versionCode 188`; no APK release is claimed for this visual-only change.
- Static source and publication checks: PASS. Physical-phone visual confirmation remains pending; do not claim device-side PASS until the user checks short and long Note PIN prompts on the phone.

---

# Check for Update version corrected to Web Update 306 (2026-11-17)

- User reported that **Check for Update** did not detect the previously announced update. Inspection found that live `latest.json` had regressed to **webVersion 288**, even though the Master Register records later releases through **Web Update 305**. A device already at 305 would correctly see 288 as older and would not offer an update.
- Created pre-edit backup branch: `backup/before-check-for-update-version-correction-2026-11-17`.
- Corrected only the update-feed version marker to **306**. Retained APK **1.0.189 / versionCode 188**, its URL and SHA-256, and the existing HTML bundle URL and SHA-256 (`3e3994514fbc6003fcda889e313a9fad700878d0045e4a96048a02d1efd2a242`). The HTML bundle itself was not changed; no notes, calendar/reminder data, PINs, locks, photos, or app features were edited.
- Feed commit: `a23dec28d97aef450fe1538a04d31cc0e665e02f`. Web publisher / live raw-feed verification and in-app phone test are pending. Do not claim the update has appeared on the user's phone until confirmed.

---

# Smart Reminder and Personal Calendar — Android 14+ full-screen permission fallback (2026-11-17)

- User asked to restore the previous screen-off reminder behavior for both **Smart Reminder** and **Personal Calendar**, with no unrelated changes.
- Read this Master Register and verified live main baseline: APK **1.0.189 / versionCode 188**, Web Update **287**. Main baseline commit: `8e549b93e6a43bdc7a37a728821052397a6fd5f2`.
- Created exact pre-edit backup branch: `backup/before-smart-reminder-calendar-screenoff-repair-2026-11-17`. Working branch: `fix/reminder-calendar-screenoff-permission-fallback-2026-11-17`.
- Shared native root cause addressed in PR #163: `scheduleReminderInternal()` returned `false` before scheduling whenever Android 14+ denied the optional full-screen-intent UI permission. That gate prevented **both** features from scheduling any alarm, even though exact-alarm permission and notification permission were available.
- Minimal native-only correction: removed only the full-screen-intent permission early-return. Exact-alarm and notification permission checks remain mandatory. Existing `AlarmManager.AlarmClockInfo`, notification/full-screen wake activity, foreground ringtone service, screen wake lock, Snooze/Done, daily repeat, reboot restoration and sound selection remain unchanged. If Android grants full-screen intent, the existing wake activity is still used; if not, the alarm and foreground ringtone/screen-wake service can still run with the notification fallback.
- PR #163 merged to main as `0cec30a3a6b79125dcfb7929078200599a8f8cdd`. Only `scripts/add_diary_app_actions.py` changed (4 added comment lines, 1 removed gate line). No HTML, Personal Calendar records, Smart Reminder records, notes, photos, PINs, locks, or app data were changed.
- Post-merge checks: native source re-fetched; the blocking full-screen-intent early-return is absent. Web source was not changed; `latest.json` remains Web Update 287 / APK 1.0.189 until a verified APK build publishes a new version. APK build, signer continuity, SHA-256/feed publication and device-side screen-off test are **pending**. Do not tell the user to update or claim ALL OK until build/release checks pass. Do not claim phone-side PASS until user tests both features with the screen off.

---

# Private Locker Favourite, Important Pin and Date Wise Diary — implementation prepared (2026-11-17)

- User approved three additions inside **Private Locker** only: Favourite Notes, Important Notes Pin, and Date Wise Diary.
- Added encrypted-record metadata flags `favourite` and `pinned`; existing notes without these fields remain valid and default to false. Editing an existing note preserves both flags. Favourite and Pin controls re-encrypt and update only the selected note record.
- Added a view filter for All Notes / Favourite / Important Pin, a date picker for Date Wise Diary, and a visible saved-date label on each note. Sorting places pinned notes first, then favourites, then newest notes.
- Existing search, save/edit/delete, encrypted IndexedDB storage, PIN/recovery, Pattern/Fingerprint, Lock On/Off, Diary Lock and Note Lock code were not intentionally changed. No existing note data is migrated or reset.
- Backup branch: `backup/before-private-locker-favourite-pin-date-2026-11-17`. Feature branch: `feature/private-locker-favourite-pin-date-2026-11-17`.
- Live baseline check found `latest.json` still advertised webVersion 283 while this register's preceding entry recorded Web Update 286; the source and mirror were byte-identical at blob SHA `5338fe01acdb5409f9a51ca9555c67f558102444`, and the advertised SHA-256 matched the current source. On the feature branch, `latest.json` baseline was reconciled to webVersion 286 so the web publisher can assign the next update number without regression.
- Implementation merged in PR #162 (`2d8fbde6024c716660851f9c22978622529cf4cd`). Main Diary JavaScript block compiled successfully before merge. Web publisher run `44129703069` completed successfully and published **Web Update 287**. Source and mirror are byte-identical at Git blob SHA `4af15d4a610f72403652df15e9488dabc6c0c3ab`; published SHA-256 is `3e3994514fbc6003fcda889e313a9fad700878d0045e4a96048a02d1efd2a242`. Release notes are recorded in `latest.json`. APK workflow run `44129703197` stopped safely at its pre-build source/mirror equality guard because it started concurrently before the web publisher synchronized the mirror. It did not reach APK build, signing or publication; the existing APK remains 1.0.189 / versionCode 188. The publisher's follow-up run `44129816177` completed successfully after source/mirror synchronization; no APK rerun was started. Physical-phone interaction testing remains pending; do not claim device-side PASS until the user tests Favourite, Pin, date filtering, and existing save/edit/search.

---

# Private Locker PIN prompt text enlarged without clipping — visual-only update (2026-11-17)

- User clarified that the earlier PIN-box prompt text had become too small. Short prompts such as “Naya 4 digit PIN” and “PIN dobara daalein” are now enlarged to a responsive 20–22px; medium prompts use 17–18px; the longest PIN prompts use a responsive 14–16px so they remain inside the box.
- Only placeholder font sizing in the existing Private Locker PIN input stylesheet changed. The typed PIN digit size (20px), 3D gold box border/shadow, PIN auto-verification including automatic Lock Off, validation, encryption, recovery, stored data, Diary Lock, Note Lock, and all unrelated features remain unchanged.
- Backup branch: `backup/before-private-locker-placeholder-readable-sizing-2026-11-17`. Working branch: `style/private-locker-placeholder-readable-sizing-2026-11-17`.
- Source and mirror are byte-identical on main at Git blob SHA `5338fe01acdb5409f9a51ca9555c67f558102444`. Publisher checksum commit `2781e18b933ab9492f5d2aabd8eb5d0ea6289023` set the matching web SHA-256 `640ae2c90f287956183467b797c149db809540cd6ad3523cf4a4e6a8dcac6534`; live `latest.json` now advertises **Web Update 286** with the specific release note. Repository/feed publication checks: PASS. Physical-phone fit/appearance confirmation remains pending; do not claim device-side PASS until the user checks the fields.

---

# Private Locker Lock Off restored to automatic PIN verification — Web Update 285 (2026-11-17)

- User clarified that the original Lock Off flow was correct: tap **Lock Off Karein**, enter the existing PIN, and a correct PIN should automatically verify and turn Lock OFF. No separate Verify button should appear.
- Corrected only the Private Locker control handler in `web-source/index.html`: Lock Off no longer enables explicit PIN confirmation; the existing configured 4-/6-digit input auto-submit remains active, and the existing successful-unlock path still calls `privateLockerRunExternalAction(config)` → `privateLockerTurnLockOff(config)`. Wrong PIN behavior remains unchanged.
- The requested PIN-box visual treatment was already present in the current source and was deliberately left untouched: PIN text is 20px with readable responsive placeholder text; the PIN boxes retain their gold raised 3D border/shadow. No CSS or other feature was changed in this correction.
- Backup branch: `backup/before-private-lockoff-auto-pin-restore-2026-11-17`. Working branch: `fix/restore-private-lockoff-auto-pin-2026-11-17`. PR #160 merged as `d5a96932f593d116f3a9e41be458fb71d77f3f84`.
- Static checks: automatic submit remains enabled for the configured PIN length; Lock Off hides the extra Verify button; correct PIN still reaches the existing Lock Off handler. Source and mirror are byte-identical at Git blob SHA `f15582a3032f836ad3e1c8c242db06bef6f7432a`.
- Web publisher run `44122191476` completed successfully. Published as **Web Update 285**. Live `latest.json` advertises web SHA-256 `dc3f994422db34a075fdab08cdb3e3752b8150f5aff86bd624afbddcec6f62a0`, matching the source bundle.
- APK workflow run `44122190215` stopped safely at the source/mirror equality guard because it started before mirror synchronization; it did not reach APK build, signing, or publication. Existing APK remains **1.0.189 / versionCode 188**; no APK update is claimed.
- Physical-phone testing remains pending. Ask the user to install/check Web Update 285 and confirm that entering the correct PIN after tapping Lock Off turns the lock off automatically, and that the PIN text fits clearly inside the 3D boxes.

---

# Private Locker PIN boxes made readable with raised 3D effect — visual-only update (2026-11-17)

- User requested that every PIN box inside Private Locker use slightly smaller, readable entered text so digits/words do not clip, while retaining comfortable legibility, and that the boxes have a raised 3D effect.
- Added presentation-only CSS scoped to `#diaryPrivateLockerModal input[type="password"]` and its placeholder. PIN entry text is now 20px with controlled spacing; long placeholder text uses a responsive 11–14px size with normal letter spacing. Each PIN field has a gold border, soft gradient, inset highlight, and raised lower shadow. The selector covers the existing PIN boxes across setup, confirmation, unlock, recovery, and Lock On flows; changing the field from password to Favourite Name text keeps that non-PIN field unaffected.
- Only the existing Private Locker visual stylesheet in `web-source/index.html` changed. No PIN/security handlers, validation, encryption, saved records, Diary Lock, Note Lock, or other features changed.
- Backup branch: `backup/before-private-locker-pin-box-fit-3d-2026-11-17`. Working branch: `style/private-locker-pin-box-fit-3d-2026-11-17`.
- PR #159 merged as `1b8141906c22a96920fa83ff166b5f0b962bae4e`. Web publisher synchronized source and mirror byte-for-byte at Git blob SHA `525e19164fd78f2926f7c2403d9ea3c434a8ef27` and published **Web Update 284**. Live `latest.json` advertises web SHA-256 `13089a499116feb8b4a03e90baacf67ea4e9fdeb63937b8f011e92251284d3e4`, matching the published bundle. APK identity/version remains unchanged. Physical-phone visual confirmation is pending; do not claim device-side PASS until the user checks the PIN boxes.

---

# Private Locker text made bold with raised 3D effect — Web Update 304 published (2026-11-17)

- User requested that all text inside **Private Locker** be bold with a raised 3D effect, including prompts/headings, button labels, PIN/recovery messages, input text/placeholders, and the writing typed and later displayed in saved entries.
- Added one presentation-only stylesheet scoped exclusively to `#diaryPrivateLockerModal`. It applies `font-weight:900` and a subtle raised text shadow to all Locker descendants, with explicit input/textarea and placeholder coverage. No layout, event handlers, PIN/recovery logic, encryption, IndexedDB, saved data, Diary Lock, Note Lock, or other Diary features were changed.
- Backup branch: `backup/before-private-locker-text-bold-3d-2026-11-17`. Working branch: `style/private-locker-all-text-bold-3d-2026-11-17`. PR #157 merged as `1b75e511c8ab3d98cbd532e77cfd636884d2cd23`.
- Web publisher run `44113360621` completed successfully. Published as **Web Update 304**. Source and mirror are byte-identical at Git blob SHA `32ada1e0177df7a35fed7bef8a131a4d84d49d76`. Live `latest.json` advertises web SHA-256 `b407db93523ba64d0a38d023e7e61b05b1071fb51edb113c3044a470b5311852`.
- Automatic APK workflow run `44113360633` stopped safely at the exact-latest-HTML pre-build guard while the publisher was synchronizing the mirror. It did not reach APK build, signing, or publication. Existing APK remains **1.0.189 / versionCode 188**, SHA-256 `1f627d94f744a70949fcaefcacb0269f90a36fbc10360368de60f4d3773cb133`.
- Repository and web publication checks: PASS. Physical-phone visual test remains pending; do not claim device-side PASS until the user confirms that typed and saved Private Locker text appears bold and raised.

---

# Private Locker Lock On and PIN recovery use one input box — Web Update 303 published (2026-11-17)

- User clarified that **🔐 Lock On Karein** and **PIN Bhool Gaye?** should each use exactly one input box, reused for each step, rather than showing separate PIN/name fields or separate step forms.
- **Lock On Karein:** the same field changes through new 4-digit PIN → confirm the same PIN → Favourite Name. The final action wraps the existing Locker master key with the new PIN and recovery name, then turns Lock ON.
- **PIN Bhool Gaye?:** the same field first verifies the existing Favourite Name, then changes through new 4-digit PIN → confirm PIN → replacement Favourite Name. Both new wrappers are created from the same existing Locker master key and saved together; the previous Favourite Name is replaced for future recovery.
- Only the Private Locker functions `privateLockerTurnLockOn(config)` and `privateLockerRecoveryForm(config)` in `web-source/index.html` changed. The backup branch is `backup/before-private-locker-single-input-flow-2026-11-17`; working branch `fix/private-locker-single-input-flow-2026-11-17`. PR #156 merged as `e69d3fec9cb3acf531abcf8c598e989f26797508`.
- Web publisher run `44109971551` completed successfully and published **Web Update 303**. Source and mirror are byte-identical at Git blob SHA `1f77a0100c268029f2e22e5e7ce100295d522b5a`. Live `latest.json` advertises web SHA-256 `3a78ad1e0c053bdfd2294c52d461d272d5c8b74a485ad8e98c16653246984675`.
- The automatic APK workflow run `44109971712` stopped safely at the pre-build source/mirror equality guard during the publisher race. It did not reach Gradle build, signing, or APK publication. Existing APK remains **1.0.189 / versionCode 188**, SHA-256 `1f627d94f744a70949fcaefcacb0269f90a36fbc10360368de60f4d3773cb133`.
- Static flow inspection confirms one input element is reused in each flow and the PIN/recovery wrappers still use the existing Locker master key. Physical-phone testing remains pending; do not claim device-side PASS until the user tests both flows.

---

# Private Locker PIN recovery now requires a new Favourite Name — Web Update 301 published (2026-11-17)

- User clarified that the existing **PIN Bhool Gaye?** flow correctly verifies the old Favourite Name and accepts/validates a new 4-digit PIN, but it did not ask for a replacement Favourite Name at the end.
- Updated only the recovery flow in `web-source/index.html`: after the old Favourite Name is verified and the new PIN is entered twice, a separate final step now requires a **new Favourite Name**. The PIN wrapper and new recovery-name wrapper are both created from the same existing Locker master key and saved together in one updated config; the previous Favourite Name is therefore replaced for future recovery. No config is written until both new values are valid and both wrappers are ready.
- Existing encrypted Locker entries, master key, Pattern/Fingerprint settings, Lock On/Off state, Diary Lock, Note Lock, and all other app features are preserved.
- Backup branch: `backup/before-private-locker-new-recovery-name-2026-11-17`. Working branch: `fix/private-locker-recovery-new-favourite-name-2026-11-17`.
- Source change commit on working branch: `7b3c0ea525f601bbc258e69b304d5e7096d95d2b`. PR #154 merged as `fffa90c7d4be55e35f560e88c2024abdcada47c2`. Web publisher run `44105391986` completed successfully. Main source and mirror are byte-identical at Git blob SHA `2f4f141a05600b4d9d2e94e1a50a7ac698706a7f`. Published as **Web Update 301**; live `latest.json` advertises web SHA-256 `7ca2590174777541174f41e9aa3bf427b684e99bcf4448c38cf71f8a4ac6b474`. Static flow checks confirm old Favourite Name verification, new PIN confirmation, mandatory new Favourite Name, and atomic saving of the new PIN and recovery wrappers. APK workflow run `44105391940` is still in progress; no new APK is claimed. Physical-phone testing remains pending.

---

# Private Locker Lock On requires a new PIN and Favourite Name — repair (2026-11-17)

- User reported that tapping **Lock On Karein** immediately re-enabled the old lock without asking to create a PIN or enter the Private Name/Favourite Name. User confirmed the intended flow: new 4-digit PIN, PIN confirmation, and Favourite Name before Lock ON.
- Corrected only the Private Locker Lock-OFF security-gate action in `web-source/index.html`; the publish workflow will synchronize the `diary-web/index.html` mirror and calculate the published SHA-256:
  - Lock On now opens a dedicated setup form; it does not switch protection ON immediately.
  - Requires a new four-digit PIN, matching confirmation, and a non-empty Favourite Name for PIN recovery.
  - Re-wraps the existing Private Locker master key with the new PIN and Favourite Name, then turns Lock ON and returns to the PIN gate.
  - Preserves existing encrypted entries, Pattern configuration, Fingerprint configuration, and other Locker metadata. It does not reset or replace the master key.
  - Cancel returns to the Lock-OFF security gate without changing the stored lock state.
- Backup branch: `backup/before-private-locker-lockon-new-pin-recovery-2026-11-17`. Working branch: `fix/private-locker-lockon-new-pin-recovery-2026-11-17`.
- Pre-edit source and mirror were identical (Git blob SHA `110f4040efe63ef46c1a3fcc81d7959b114fa6bb`). JavaScript syntax and static flow checks pass. Published successfully as Web Update 300. The web publish workflow completed successfully; live `latest.json` advertises webVersion 300 and SHA-256 `90344e7b4672ac303ade7dbae8da71d92419db9a082c4ad08d75c2470a40d248`. Main source and mirror are byte-identical at Git blob SHA `d201105f510473e034d146b6d999668e8273014b`. The automatic APK workflow started concurrently and failed its pre-build source/mirror check because it ran before the web publisher synchronized the mirror; it did not reach APK build or publish. Existing APK remains version 1.0.189 / versionCode 188 with manifest SHA-256 `1f627d94f744a70949fcaefcacb0269f90a36fbc10360368de60f4d3773cb133`. Physical-phone interaction testing remains pending; do not claim phone testing.

---

# Private Locker Pattern and Fingerprint controls — repair (2026-11-17)

- User reported that Pattern Set, Fingerprint Set, Pattern Remove, and Fingerprint Remove did not proceed after entering the Locker PIN. The previous static-only review did not prove the buttons worked; correction is limited to Private Locker.
- Root causes found in the Private Locker flow:
  - PIN entry for these actions did not auto-run the selected action; it exposed a second Verify button. The PIN input now verifies automatically at the configured 4- or 6-digit length, matching the Lock Off flow.
  - Pattern setup left the PIN gate visible and rendered the pattern grid separately below it. The gate is now cleared before the grid is shown, and the grid is scrolled into view.
  - Fingerprint Set was enabled only when the Android WebView native bridge existed. In Chrome/web builds this made the button unavailable. Native Android biometric support is retained; secure web builds now also attempt a WebAuthn platform-authenticator PRF flow. The Private Locker master key is wrapped with a key derived from the authenticator PRF; if the browser/device does not support PRF, the user receives an explicit message and PIN remains available. No plaintext master key is stored for this fallback.
  - Fingerprint unlock now supports the saved WebAuthn credential; Fingerprint Remove clears only the Private Locker fingerprint metadata and preserves encrypted entries/PIN/recovery.
- Changed only the Private Locker code in `web-source/index.html` and the identical `diary-web/index.html` mirror, plus this register entry. Diary Lock, Note Lock, My Documents, Diary editor, and other features are not changed.
- Backup branch: `backup/before-private-locker-pattern-fingerprint-fix-2026-11-17`. Working branch: `fix/private-locker-pattern-fingerprint-2026-11-17`.
- Published as **Web Update 299**. `latest.json` now advertises the current source SHA-256 `b97710ea5af1c0a6c555f098b613fc18a65ba2e66c3546762e5f3ab0ca974fa3`; source and mirror are byte-identical. APK package version remains 1.0.189 / versionCode 188; this PR did not change APK code. Physical biometric prompt / Pattern touch testing on the user's phone remains pending; do not claim it has been device-tested.

---

# Private Locker full button audit — two edge-case fixes (2026-11-17)

- User requested that **only Private Locker buttons** be audited and corrected; all other Diary features must remain untouched.
- Audited the Private Locker modal, lock/setup/PIN/recovery controls, Pattern/Fingerprint controls, Lock On/Off routes, Lock-OFF security gate, encrypted writing Save/Edit/Delete, and Search. Existing button handlers were reviewed for their intended route and failure/cancel handling.
- Found and fixed two Private Locker-only edge cases:
  - Legacy six-digit PIN: the PIN field advertised support for an old six-digit PIN but auto-submitted as soon as digit four was entered, clearing the field before digits five and six could be typed. Auto-submit now uses the configured PIN length (4 or 6), including the Lock Off action.
  - Delete while editing: deleting the same entry currently loaded in the editor could leave a stale edit ID and allow a later Save to recreate that deleted entry. Successful deletion now clears that matching edit form before refreshing the list.
- Changed only the Private Locker block in `web-source/index.html` and the identical `diary-web/index.html` mirror, plus this register entry. No Diary Lock, Note Lock, My Documents, Diary editor, or other feature logic was changed.
- Backup branch: `backup/before-private-locker-full-button-audit-2026-11-17`. Working branch: `fix/private-locker-full-button-audit-2026-11-17`.
- Verification: source and mirror have identical Git blob SHA `f2d14c4a0491eea73b59e24cc8668dbd50f482cb`; both inline JavaScript blocks pass V8 syntax parsing (2/2); static wiring checks pass for modal open/close, setup, PIN, Pattern, Fingerprint, remove controls, Lock On/Off, recovery, save/edit/delete, and search. Phone/browser interaction testing remains pending; do not claim physical-device confirmation.
- Published as **Web Update 298** by advancing only the web updater version/release note. The existing updater SHA-256 already matched the current main source and was retained. APK version 1.0.189 / versionCode 188 and all non-Locker features remain unchanged.

---

# Private Locker Lock Off PIN auto-opens Locker — Web Update 297 (2026-11-17)

- User requested: after tapping **🔓 Lock Off Karein**, entering the correct PIN should automatically turn Lock OFF and open the Locker; a wrong PIN must show **“PIN galat hai.”** beside the PIN field.
- Changed only the Private Locker PIN/action flow in `web-source/index.html` and identical `diary-web/index.html` mirror:
  - Lock Off action now auto-verifies on PIN entry; no extra “PIN Verify” button or second Lock Off confirmation is required.
  - Correct PIN saves `lockDisabled=true` and the existing unlocked master-key value, then opens the writing/search screen automatically.
  - Incorrect PIN displays the exact local message “PIN galat hai.”, clears the entered digits, and keeps the Lock Off action available for retry. Lock remains ON.
- Existing encrypted entries, master key, PIN/recovery wrappers, Pattern/Fingerprint settings, Diary Lock, Note Lock, and other app features were not intentionally modified.
- Backup branch: `backup/before-private-lockoff-pin-auto-open-2026-11-17`. Working branch: `fix/private-lockoff-pin-auto-open-2026-11-17`. PR #150 merged as `1319d12d5afd06bf3fae4b1227d9b324a74df301`.
- Source and mirror have identical Git blob SHA `8442c091345ed49ba669e2515ff6b74af9e990e9`; independently computed source SHA-256 is `ce0f679c4ab023e7e9e773280191ec2b649c47f6e67d136f17b15d9bb44aee4a`. Both inline JavaScript blocks passed V8 syntax parsing (2/2). Static checks passed for auto-submit, wrong-PIN message, Lock Off persistence, and automatic entry into Locker.
- Device testing remains pending.

---

# Private Locker Lock On placed at the security gate — Web Update 296 published (2026-11-17)

- User clarified that **🔐 Lock On Karein must not appear inside the unlocked Private Locker writing/search screen**. It must be in the separate security-control gate where the Lock Off controls belong.
- Corrected the Lock OFF opening flow: opening a Lock-OFF Locker now first shows a separate **🔐 Locker Security** gate with **🔐 Lock On Karein** and **🔓 Locker Kholein**. Lock On reuses the existing re-lock handler and returns to the PIN gate; Locker Kholein preserves access to saved writing while protection remains OFF.
- Removed the old Lock On insertion from `privateLockerShowEntries()`. The writing form and Search are clear of Lock On. No encrypted Locker entries, PIN/recovery data, Diary Lock, or Note Lock were changed intentionally.
- Backup branch: `backup/before-private-locker-lockon-gate-placement-2026-11-17`. Working branch: `fix/private-locker-lockon-at-security-gate-2026-11-17`. PR #149 merged as `173d67dab589be40a7b496d92fbfbfb45332a453`.
- Main source and mirror are byte-identical at Git blob SHA `3f9df3a83aaa1decdf6331d5aab796b8b8a196c0`. Both inline JavaScript blocks passed V8 syntax parsing (2/2). Static checks confirm the old Lock On insertion is gone and Lock OFF now routes to the security gate.
- Published as **Web Update 296**. Independently computed UTF-8 SHA-256 `4afe5cb2b795bdcc6609d333552d73e7fb0bee51fb1a7b8ae9416a4915add168` matches live `latest.json`. APK remains **1.0.189 / versionCode 188**; both APK paths retain original Git blob SHA `37aa10bafbeb698dd52db313b968cc1583735052` and manifest SHA-256 `084c63eaff3ebf4d34d4acbdbcbe4ded98770c44bcef99da4e61053058cd8e15`.
- Repository/source/mirror/manifest verification: PASS. Physical-phone testing remains pending; do not claim device-side confirmation until user installs Web Update 296 and verifies Lock On, Locker Kholein, and Lock OFF behavior.


# Private Locker Lock On moved out of writing area — Web Update 295 published (2026-11-17)

- User correctly objected that the Lock On button had been placed inside the Private Locker writing/search area. The button is now removed from privateLockerContent and placed in the separate privateLockerGate security area above the writing area, under “🔐 Locker Security”. It appears only while Lock is OFF and reuses the existing privateLockerTurnLockOn(config) handler. It is not part of the note title/text form or search controls.
- PR #148 merged as bdbf073c420b60172c3f84dd190cb7945a2c1eaa. Backup branch: backup/before-move-private-locker-lockon-2026-11-17. Working branch: fix/move-private-locker-lockon-outside-writing-area-2026-11-17.
- Only the Lock On control placement changed in web-source/index.html and diary-web/index.html. Source and mirror are byte-identical at Git blob SHA f313a82f599b3315b754b2bf9da3ed73dd4ec5a1. Both inline JavaScript blocks passed V8 syntax parsing (2/2). Verified the old privateLockerContent.insertBefore(lockTools,searchWrap) placement is gone and privateLockerGate.appendChild(lockTools) is used instead.
- Published as Web Update 295. latest.json advertises webVersion 295 and web SHA-256 2792739d2159efaeea68ec35c1107756fd3c2f77c2e76a41f6705663aded3f12, matching the source HTML. Release notes state the exact placement correction.
- A repository push also triggered the APK workflow, which republished an APK during this web-only change. Restored the exact original APK blob from the pre-change main commit (Git blob SHA 37aa10bafbeb698dd52db313b968cc1583735052) in both My-Diary-1.0.189.apk and My-Diary.apk; latest.json APK SHA-256 restored to 084c63eaff3ebf4d34d4acbdbcbe4ded98770c44bcef99da4e61053058cd8e15. APK remains 1.0.189 / versionCode 188; no new APK release is intended.
- No encrypted Locker entries, PIN/recovery data, Diary Lock, Note Lock, or saved notes were modified. Physical-phone testing remains pending.

---

# Private Locker controls audited and hardened — Web Update 294 published (2026-11-17)

- User requested a full check of all Private Locker buttons and correction of any behavior that should work differently.
- Audited the complete Private Locker PIN/control flow and unlocked Locker actions: Pattern Set/Badlein/Remove; Fingerprint Set/Remove and native Android biometric callbacks; Lock Off confirmation; Lock On from the unlocked view; PIN verification/recovery; encrypted note Save/Edit/Delete/Search; modal close behavior.
- Fixes in PR #147 (merged as 13bc5bd512b63400ba54073dab1efb3a7960f9e5):
  - Fingerprint Set now shows “Fingerprint Pehle Se Set Hai” and is disabled when already configured. The Android setup routine replaces its Keystore alias before the biometric prompt; preventing repeated setup avoids accidentally invalidating an existing fingerprint if the prompt is cancelled.
  - Lock On now returns a promise; if saving the lock state fails, the unlocked-view Lock On button becomes active again so the user can retry.
  - Fingerprint removal now asks for confirmation.
  - Cancelling Pattern setup, Pattern removal confirmation, or Lock Off confirmation returns to the unlocked Locker instead of unexpectedly closing the whole Locker.
- No encrypted entries, PIN/recovery records, Diary Lock, Note Lock, or native Android source were changed. Existing encrypted Save/Edit/Delete/Search paths were inspected and left untouched.
- Backup branch: backup/before-private-locker-controls-audit-fix-2026-11-17. Working branch: fix/private-locker-controls-safe-state-2026-11-17. PR #147 merged to main.
- Source and mirror are byte-identical at Git blob SHA 69dae108b684ac4922e1bf3f627a94361154df04. Both inline JavaScript blocks passed V8 syntax parsing (2/2).
- Published as Web Update 294. latest.json advertises webVersion 294 and web SHA-256 f53b183bd19bf4c1b91d0c4a5e69deab04f24afdf31ae53df80c1e9d98b71254. The APK workflow also completed successfully and packaged this exact latest HTML into My-Diary-1.0.189.apk / My-Diary.apk. APK version remains 1.0.189 / versionCode 188; the newly published APK SHA-256 is 084c63eaff3ebf4d34d4acbdbcbe4ded98770c44bcef99da4e61053058cd8e15. latest.json was re-checked and restored to webVersion 294 after the APK workflow overwrote that metadata with an older webVersion.
- Physical phone testing remains pending. Fingerprint prompts require a compatible Android build/device with enrolled fingerprint; web-only browser cannot test native biometric callbacks. Do not claim device-side confirmation until the user installs Web Update 294 and tests all controls.

---

# Private Locker Lock On available while Lock is OFF — Web Update 293 published (2026-11-17)

- Source inspection found that the existing Lock On control was only on the PIN-entry screen, but Lock OFF automatically bypasses that screen and opens the unlocked Locker. This made it impossible to turn PIN protection back ON from the Lock OFF state.
- Minimal fix: when the unlocked Private Locker detects config.lockDisabled=true, it now shows one gold 🔐 Lock On Karein button above Search. Tapping it calls the existing privateLockerTurnLockOn(config) flow, clears the locally retained unlocked key, and restores the normal PIN gate. The button is hidden when Lock is already ON. No saved entries, PIN/recovery wrappers, Diary Lock, or Note Lock are changed.
- Backup branch: backup/before-private-locker-lockon-access-fix-2026-11-17. Working branch: fix/private-locker-lockon-access-when-off-2026-11-17. PR #146 merged as 831c5a282a97cf36eb2569a40dd56ebad8311de9.
- Only one insertion in privateLockerShowEntries() was added to web-source/index.html and diary-web/index.html. Source and mirror are byte-identical at Git blob SHA 59486f03f2b9ecf57f4fb569d22448374c9282a2. Both inline JavaScript blocks passed V8 syntax parsing (2/2); PR diff contains only the conditional Lock On button.
- Web Update 293 is published. latest.json advertises webVersion 293 and web SHA-256 844e6bee162dde7fa428b31bb225d0f06b4301c6e8ceac43130d9f605b2c82ce, matching the published source/mirror.
- The automatic APK workflow again republished the existing APK version after this web-only push. Both original APK files were restored to Git blob SHA d37ec3842b6e9868209d24ec8fb935b43ac0e98f, and latest.json advertises the original APK SHA-256 07d922d24b7ec1db1bea55681711408924d8c8a5888822bdaaebaf57a54e7baa. APK remains 1.0.189 / versionCode 188; no new APK release is intended.
- Physical-phone testing remains pending. Ask the user to install Web Update 293 and test: PIN verification for setup/removal, Lock OFF confirmation, and the new Lock On Karein button restoring the PIN gate. Do not claim phone-side confirmation.

---

# Private Locker Lock Off no longer asks for PIN twice — Web Update 292 published (2026-11-17)

- Root cause: the Lock Off action asked for the current PIN a second time after the PIN-screen control flow had already verified it.
- Minimal fix: after selecting Lock Off and pressing PIN Verify Karke Kaam Karein, a separate Lock Off Confirm Karein / Radd Karein card appears. Confirm reuses the already authenticated Private Locker key to set lockDisabled=true and retain the unlocked key. Saved encrypted entries remain intact. Lock On and the other four control handlers are unchanged.
- Backup branch: backup/before-private-locker-lockoff-double-pin-fix-2026-11-17. Working branch: fix/private-locker-lockoff-confirm-after-pin-2026-11-17. PR #145 merged as 8ccac0cb7201319ad6fac33b8dfa88d14d52f17b.
- Only privateLockerAskLockOff() changed in web-source/index.html and diary-web/index.html. Source and mirror are byte-identical at Git blob SHA 728a7a429070be9b6d9fb0c17a19ddf0175c93ed. Both inline JavaScript blocks passed V8 syntax parsing (2/2); PR diff is limited to the Lock Off confirmation flow.
- Published as Web Update 292. latest.json reports webVersion 292 and web SHA-256 5fd2f05adb1862224019be7134ba416b8760515e27146dfc32bf121078ad1249, matching source and mirror.
- The automatic APK workflow also republished the existing version during this web-only change. Both original APK blobs were restored (Git blob SHA d37ec3842b6e9868209d24ec8fb935b43ac0e98f), and latest.json restored to the original APK SHA-256 07d922d24b7ec1db1bea55681711408924d8c8a5888822bdaaebaf57a54e7baa. APK remains 1.0.189 / versionCode 188; no new APK release is intended.
- Physical-phone testing remains pending. Do not claim device-side confirmation until the user installs Web Update 292 and tests Lock Off / Lock On.

---

# Private Locker PIN-screen controls enabled — Web Update 291 published (2026-11-17)

- Root cause: the shared `el()` helper applies attributes with `setAttribute`; passing `disabled: null` still creates a `disabled="null"` HTML attribute. As a result, every PIN-screen control button was disabled, including Pattern setup and Lock Off.
- Minimal fix: create each control button without a `disabled` attribute, then set the DOM boolean property `button.disabled = !!disabled`. Only controls intentionally unavailable by current configuration/platform remain disabled. No action handlers, PIN verification, Locker data, Diary Lock, Note Lock, or other features are changed.
- Backup branch: `backup/before-private-locker-buttons-enable-fix-2026-11-17`. Working branch: `fix/private-locker-buttons-enabled-2026-11-17`.
- PR #144 merged to main as `1765364368e6e35b66bea6a661d06ac0920fc7b4`.
- Main source and mirror are byte-identical at Git blob SHA `8e2c495e121451f99d3c09112d86350c0e361d93`; both inline JavaScript blocks passed V8 syntax parsing. Static inspection confirms the erroneous disabled-attribute expression is gone and the boolean `button.disabled` property is used.
- Published as **Web Update 291**. `latest.json` now reports `webVersion: 291` and web SHA-256 `9289907a3218d191f21f5950d27f41f8ec670124eb0b95dbbab47df84e799265`, matching the updated `web-source/index.html`. The source and `diary-web/index.html` mirror are byte-identical.
- APK remains `1.0.189 / versionCode 188`; no APK was rebuilt or changed. Physical-phone testing remains pending.

---

# Private Locker control actions fixed — Web Update 290 (2026-11-17)

- User confirmed the PIN-screen placement is now correct, but the five controls did not perform their actions.
- Fixed the action flow: selecting a control reveals an explicit **PIN Verify Karke Kaam Karein** button. Enter the Locker PIN and press it; the existing PIN verification then calls the selected action. Ordinary Locker PIN auto-unlock remains unchanged when no control is selected.
- Kept all five controls in the PIN-entry screen. No intended changes to encrypted writing/search, saved Locker data, Diary Lock, or Note Lock.
- Backup branch: `backup/before-private-locker-control-action-fix-2026-11-17`. Working branch: `fix/private-locker-control-pin-confirm-2026-11-17`. PR **#143** merged as `aae37aaa7b098b31c354ecaf13b69698559bd6a1`.
- Source and mirror were updated together; Web Update **290** published in `latest.json`. Manifest web SHA-256: `20aff0b7a8b038069c266563d221762b2785ccf71949adba8fdc962d9d5d9e3f`. APK remains `1.0.189 / versionCode 188`.
- Static checks only; physical-device testing remains pending.

---

# Private Locker controls moved onto the PIN screen — publication pending (2026-11-17)

- User's correction overrides Web Update 289 placement: the five controls must appear together on the **Private Locker PIN-entry screen**, after tapping the Private Locker button. They must not appear in the Me menu and must not be placed in the unlocked writing/search area.
- Moved Pattern Set/Badlein, Fingerprint Set, Pattern Hataayein, Fingerprint Hataayein, and Lock Off/On controls into the PIN form. Selecting a control marks the requested action; the existing PIN verification runs first, then the existing authenticated action dispatcher performs it.
- Removed the five-control panel from Me menu. Existing PIN/Pattern/Fingerprint unlock controls and Forgot PIN remain. No encrypted entries or Locker PIN/recovery data were intentionally changed; Diary Lock and Note Lock were not intentionally changed.
- Snapshot branch: `backup/before-private-locker-pin-screen-controls-2026-11-17`. Working branch: `fix/private-locker-controls-on-pin-screen-2026-11-17`. PR **#142** merged to main as `6d8fb3d4d0d40c684da1422b965ece59b43b6bb3`.
- Main `web-source/index.html` and `diary-web/index.html` are byte-identical at Git blob SHA `2fe846d0449de1b4a926a3b70e9789113f0cf99a`. Static source checks confirm the Me-menu panel and renderer are removed and all five controls are present in the PIN form.
- **Not yet published to Check for Update:** live `latest.json` still reports Web Update **283** and its older web checksum. Do not tell the user to update yet. Web publisher/checksum synchronization and a new webVersion feed entry are pending. APK remains **1.0.189 / versionCode 188** and was not changed.
- Physical-phone testing is pending. Do not claim device-side confirmation.

---

# Private Locker controls moved outside the Locker screen — Web Update 289 (2026-11-17)

- User's explicit correction: the five related controls must be together outside the entire Private Locker screen, under the Private Locker button in the Me menu: Pattern setup/change, Fingerprint setup/change, Pattern removal, Fingerprint removal, and Lock Off/On.
- The controls are rendered together in the Me menu. Selecting any control opens Private Locker authentication first, then performs the selected action. The controls are no longer rendered inside the Locker gate or writing/search screen.
- Only the Private Locker control placement and its action dispatch were changed. Existing Locker PIN confirmation, encrypted writing/search, and saved Locker data were intended to remain unchanged. Diary Lock and Note Lock were not intentionally changed.
- Backup branch: `backup/before-private-locker-controls-outside-me-2026-11-17`. Working branch: `fix/private-locker-controls-me-menu-2026-11-17`. PR **#141** merged to main as `bad225812ce5a2080aa26cdf6f58b20dd012cd43`.
- Main source and mirror are byte-identical at Git blob SHA `0dd8d934c1d1718deb1fdcce53b4758ff7c139e8`. The live update feed reports **Web Update 289**; APK remains **1.0.189 / versionCode 188** (no APK rebuild).
- Phone testing remains pending. Do not claim the user's phone has confirmed the new placement until the user checks it.

---

# Private Locker Lock Off / Lock On controls restored outside writing area — Web Update 288 (2026-11-17)

- User corrected the previous placement: the Pattern/Fingerprint/Lock Off/Lock On controls belong outside the Private Locker search and writing content, in the Locker gate area above them. Web Update 287 had mounted the controls row inside `privateLockerContent`, directly under Search; that did not follow the user's stated placement.
- Corrected only the mount location in `privateLockerShowEntries()`: the existing `tools` row is now appended to `privateLockerGate`, while `privateLockerContent` receives only `searchWrap`, `form`, and `list`. The controls therefore appear above Search and outside the writing area.
- Existing Lock Off current-PIN confirmation, Lock On re-gating, Pattern/Fingerprint setup/removal handlers, and the Private Locker header **✕** remain unchanged. No Locker PIN, recovery wrapper, encrypted entry, IndexedDB record, or saved writing data was intentionally changed. Diary Lock and Note Lock are untouched.
- Pre-edit main commit: `55f69971a59802f991d64c90967ae66fec094a46`. Snapshot branch: `backup/before-private-locker-controls-relocation-2026-11-17`. Working branch: `fix/private-locker-controls-outside-content-2026-11-17`. PR **#138** merged to main as `55f69971a59802f991d64c90967ae66fec094a46`.
- Main source and `diary-web/index.html` mirror are byte-identical at Git blob SHA `1e0ce72209647edbebc38d00967cd71921c08f0d`. Both inline JavaScript blocks passed V8 syntax parsing (2/2). PR diff contains only the two HTML delivery files and the one intended mount-location correction.
- Web publisher synchronized the source/mirror checksum. Verified manifest SHA-256: `9e74626c3dd091b8e5206d6034b4a8ce5e55a32473f523a785c52076d40fc761`. Feed is advanced to **Web Update 288** with release notes describing the corrected placement. APK remains **1.0.189 / versionCode 188** with its existing SHA-256 `1243d93bc6fd5f7af707425bfd8b8ba05c20e0b4c3817de76e527a0a363b7f1c`; no APK rebuild or publication was performed for this web-only change.
- Physical-phone testing is still pending. Do not claim the buttons are confirmed on the user's device until the user runs Check for Update and verifies they appear above Search, outside the writing content, and that Lock Off / Lock On still work.

---

# Private Locker Lock Off / Lock On buttons made visible — Web Update 287 (2026-11-17)

- User reported that neither **🔓 Lock Off Karein** nor **🔐 Lock On Karein** appeared in the actual Private Locker screen, although the previous Web Update 286 entry said they had been added. Re-read this Master Register and verified live main, `latest.json`, the actual source and mirror before editing.
- Root cause: `privateLockerShowEntries()` created the existing `tools` row and appended Pattern/Fingerprint/Lock-toggle buttons into it, but never mounted that row into `privateLockerContent`. The only source change was one line: `privateLockerContent.append(searchWrap,form,list)` → `privateLockerContent.append(searchWrap,tools,form,list)`. The row now sits immediately below the Private Locker search bar and above the writing form. The existing state-dependent button text remains **🔓 Lock Off Karein** when the lock is ON and **🔐 Lock On Karein** when the lock is OFF.
- No lock logic was rewritten. Existing Lock Off flow still asks for the current Locker PIN, verifies it against the existing PIN wrapper and confirms the unwrapped master key before setting `lockDisabled`; existing Lock On flow removes the locally retained key and restores the PIN gate. Saved encrypted entries and PIN/recovery wrappers are not deleted. **Security note:** while Lock OFF is enabled, the existing implementation stores the Locker master key in its own IndexedDB config, so PIN protection is intentionally disabled and anyone with access to the app's local storage/device data may be able to access Locker contents.
- Pre-edit main commit: `d9d79060c820f3972589d4879924c23be61b560a`. Verified snapshot branch: `backup/before-private-locker-controls-mount-2026-11-17`. Working branch: `fix/private-locker-controls-mount-2026-11-17`. PR **#136** merged to main as `02298b110836ac799b2e41ef223e7b6f16ea3e27`.
- Corrected the live manifest's regressed web baseline from **283** back to **286** before the publisher ran. Web publisher workflow run **44072780221** completed successfully and published **Web Update 287**. Main source and `diary-web/index.html` mirror were re-fetched and are byte-identical at Git blob SHA `4b19481577affaf27ded1e0ac2306baa8ea9e093`. Independently computed UTF-8 SHA-256 is `2f79ea9c5039cf3fd43d6567d908ab0cf72458f0c0879410806936b0609fd7ee`, matching `latest.json`'s `webSha256`. Live `latest.json` now reports `webVersion: 287`, while APK metadata remains `1.0.189` / `versionCode: 188` and its existing feed SHA-256 remains `1243d93bc6fd5f7af707425bfd8b8ba05c20e0b4c3817de76e527a0a363b7f1c`.
- The automatic Android build workflow run **44072780276** failed closed at **“Use the exact latest published Diary HTML in Android APK”** because it ran concurrently before the web publisher had synced the mirror. Its source/mirror equality guard stopped the job; all build, signing, and APK upload steps were skipped. No APK was rebuilt or published. After the web publisher completed, the source/mirror equality check passed. This was an Android workflow race, not a failure of web publisher run 44072780221; no APK rebuild is needed for this web-only fix.
- Static verification confirms the controls row is mounted, the old unmounted append line is absent, both state labels and existing Lock Off/Lock On handlers remain, and the Diary Lock function anchors remain present. **Physical-phone testing is still pending**; do not claim device-side success until the user runs Check for Update and confirms both buttons and the PIN-confirmed OFF → ON flow. No Diary Lock, Note Lock, other features, Android bridge, package identity, or saved data were intentionally changed.

---

# Private Locker Lock Off / Lock On toggle — Web Update 286 (2026-11-17)

- User requested that the Private Locker header **✕** remain, only the separate **🔒 Locker Band Karein** button be removed, and a **🔓 Lock Off Karein** button be placed with the Fingerprint/setup controls. The existing Locker PIN must be confirmed before disabling the lock. After disabling, the Locker should open without a PIN; saved writing must remain. A way to turn the lock ON again must remain available.
- Pre-edit main commit: `5addb5a23d2209596ee19036f37ea3a421670826`. Snapshot branch: `backup/before-private-locker-lock-off-2026-11-17`. Working branch: `fix/private-locker-lock-off-toggle-2026-11-17`. PR **#135** merged to main as `c96edc059d6ccb27ce47172573689b52105ddfa0`.
- Removed only the **🔒 Locker Band Karein** button from the Private Locker entries view. The existing header **✕** button and its close handler remain unchanged. Added **🔓 Lock Off Karein** beside the Locker setup controls; it asks for the current 4- or 6-digit Locker PIN, verifies it against the existing PIN wrapper and confirms the unwrapped master key matches the active Locker key before saving the lock-off state.
- Lock OFF stores the already-existing 32-byte Locker master key in the Locker's own IndexedDB config so the encrypted entries can continue opening without a PIN. **This intentionally removes PIN protection while OFF**: anyone who can access the app's local storage/device data may be able to access the Locker contents. Encrypted entries, PIN wrapper, recovery wrapper, Pattern/Fingerprint settings and entry records are not deleted. **🔐 Lock On Karein** removes the locally retained key and restores the existing PIN/Pattern/Fingerprint gate; the existing PIN and recovery setup are retained.
- Diary Lock, Note Lock, other features, Android native bridge, package identity and APK were not changed. APK remains **1.0.189 / versionCode 188**, with its existing APK SHA-256 `b1c87f99bdf255e56c16678b5cf5ad9816cbb4ccde28c73ba299ff96bcdc88a6`.
- Corrected an accidental manifest regression from the APK publication commit: `latest.json` had reverted Web Update **285** to **283** even though the Web 285 source/mirror and register entry were already present. Restored the correct Web 285 baseline and advanced to **Web Update 286** for this change, preserving the APK metadata and APK checksum.
- Main source and mirror are byte-identical at Git blob SHA `3ff1172c02b2bc4739fafbc279a3a118df733d9f`. Verified UTF-8 web SHA-256: `fb8f7db2d4cd6fb3f15fef5afd5724a22e404ee323d1442e1582b73d52a339ca`; `latest.json` advertises Web Update 286 and the same SHA. Both inline JavaScript blocks passed V8 syntax parsing (2/2). Static checks confirm the ✕ button and wiring remain, the Locker Band Karein button is absent, PIN verification is present, and no-PIN open plus Lock On re-enable paths are present.
- PR #135 merged and main manifest/source/mirror were re-fetched and verified. A separate publisher workflow run was not available to trigger/inspect through the connected GitHub actions controls; the source, mirror, manifest and SHA are already synchronized in main. Physical-phone testing is **pending**; do not claim device-side success until the user confirms.

---

# Private Locker Pattern and fingerprint setup on existing PIN screen — Web Update 285 LIVE (2026-11-17)

- User clarified that the existing Locker already has a PIN; its current screen showed only **PIN Bhool Gaye?**, while Pattern/Fingerprint setup controls were missing. The prior update had only placed setup controls on first-time PIN creation, which did not solve this existing-Locker case.
- On the existing Locker PIN screen, added **🔷 Pattern Set Karein / Pattern Badlein** and, when the Android fingerprint bridge is available, **👆 Fingerprint Set Karein / Fingerprint Badlein** above **PIN Bhool Gaye?**. Selecting a setup method asks for the existing Locker PIN, verifies it against the existing encrypted PIN wrapper, and only then begins the chosen setup. Normal four-digit PIN auto-unlock, configured Pattern/Fingerprint unlock, and Forgot PIN recovery remain.
- The change is limited to `privateLockerPinForm(config)` in `web-source/index.html` and the matching `diary-web/index.html` mirror. No existing PIN, recovery wrapper, encrypted entry, IndexedDB record, Android Keystore entry, Diary Lock, Note Lock, or unrelated feature was intentionally changed.
- Pre-edit snapshot branch: `backup/before-private-locker-pin-screen-method-buttons-2026-11-17`. Working branch: `fix/private-locker-pin-screen-method-buttons-2026-11-17`. PR **#134** merged to main as `178aeb3062175c5a187692e90d8679f0023c582a`.
- Source and mirror are byte-identical at Git blob SHA `576cc5f90b3ba052062b9952b5ab7ec55d3d3375`. Web publisher run **44062027377** succeeded and repaired the published checksum; the manifest was then explicitly advanced to **Web Update 285**. Publisher run **44062130358** completed successfully (the already-synced mirror and matching SHA were verified; no extra mirror rewrite was needed). Live manifest web SHA-256: `73f42aab8f80a650b24011aea5349e1922ba1b1db208e5f9790704f949b43dc1`. APK remains **1.0.189 / versionCode 188**; the change is web-only. A separate automatic APK workflow run **44062027473** was still in progress at the time of this entry; do not infer an APK change from it.
- The publisher verified HTML identity/size, matching source/mirror bytes and advertised SHA-256. A separate JavaScript parser check and physical-phone test have not been performed. Ask the user to run Check for Update and confirm the buttons appear; do not claim device-side success.
 
---
# Private Locker Pattern and fingerprint buttons moved beside PIN setup — Web Update 284 (2026-11-17)

- User approved moving **🔷 Pattern Set Karein** and **👆 Fingerprint Set Karein** out of the Private Locker writing/editor tools row and placing them with the lock setup controls.
- First-time setup shows both controls on the same screen as the new four-digit PIN, PIN confirmation, and Favourite Name fields. Selecting either validates those fields, creates the primary PIN/recovery wrappers, and then starts the requested Pattern or Android fingerprint setup. The ordinary **Locker Set Karein** action remains available.
- For an already-configured Locker, the controls are in the authenticated lock gate above the writing editor, not inside the writing tools row. Enrollment still requires the successfully unlocked master key.
- No encrypted entries, PINs, recovery data, IndexedDB records, Android Keystore entries, Diary Lock, Note Lock, writing/search/editing behavior, or app identity were intentionally changed.
- Verified main baseline commit: `af5bc74f49b9f737a28ecb07e9402b1a45340b81`. Pre-edit snapshot branch: `backup/before-private-locker-lock-buttons-move-2026-11-17`. PR **#133** merged as `bf479c6108cad2e88cb76a8ee3474db479754344`.
- V8 inline JavaScript syntax and static checks passed. Source and `diary-web/index.html` mirror are byte-identical at Git blob SHA `4ee279d6d84ca5b64a665483e1ac1f91513e4dee`. Web publisher run **44060440587** completed successfully; Web Update **284** is live with web SHA-256 `32a2a820dc288d977e04512f4a7820be4e4537f8279d0dbb211397d05693cac7`. APK remains **1.0.189 / versionCode 188**; no APK change is required for this web-only relocation.
- APK workflow run **44060440753** failed closed at the source/mirror equality guard because it checked out the main commit while the separate web publisher was concurrently syncing the mirror. No Android build or APK publication occurred; the existing APK 1.0.189 / code 188 and its checksum were not changed. This is a web-only relocation, so no APK rebuild is required. The source/mirror equality was verified after publisher completion.
- Physical phone testing remains pending. Do not claim device-side success until the user confirms.


# Private Locker restored with four-digit Diary-style lock — implementation branch (2026-11-17)

- User approved restoring **Private Locker** inside Me, with text-only private writing, optional title, top search matching My Memories, editing, and a lock workflow matching the existing Diary Lock's core functions: **4-digit PIN, automatic PIN/Pattern unlock, Favourite Name recovery, new PIN + confirmation after recovery, separate Android fingerprint authentication, and Lock Band**. Diary Lock and Note Lock must remain untouched.
- Live baseline was re-read before work: APK **1.0.188 / versionCode 187**, Web Update **282**; `latest.json` APK SHA-256 `90f7575564d3267d49d93734179034828a8ded6ddb75e6ffa2f57ea9424118ab`, web SHA-256 `781badc278cc9c54ad8b584a7da6cf7584631527260e3d1b8279f282f899e781`.
- Created pre-edit snapshot branch `backup/before-private-locker-diary-lock-parity-2026-11-17` and working branch `feat/private-locker-diary-lock-parity-2026-11-17`, both from the verified main commit `1df95a36c51a479263ba23f4acb9826a1e0bdf37`.
- Recovered the previously reviewed encrypted Private Locker implementation from PR #127 as the feature base (separate IndexedDB `diary_private_locker_v1`, AES-GCM encrypted writing, separate PIN/Pattern/Favourite Name wrappers, and Android Keystore fingerprint bridge). Updated the Locker's new setup/recovery PIN to **four digits**. Existing legacy six-digit PINs remain accepted only for the first safe unlock; after a successful PIN, Pattern, or fingerprint unlock, the same encrypted master key is rewrapped under a confirmed four-digit PIN. This migrates only the Locker PIN wrapper/config, not encrypted entries; no data reset or deletion occurs. Existing fingerprint wrapping is preserved through recovery.
- Locker writing form is text-only (no photo/file/category controls); title is optional and text is required. Search is moved above the editor and searches both title and body. Saved writing remains editable.
- Transplanted the current main Note Lock wrong-PIN inline-message helper and handler into the recovered source so the newer Note Lock fix is retained. Diary Lock functions (`configureDiaryPin`, `showDiaryUnlock`, `configureDiaryPattern`, `openDiaryLockSettings`, `turnDiaryLockOff`) remain unchanged from the reviewed PR #127 source; Locker uses its own keys and separate Android fingerprint callback.
- Updated release workflow target to signed APK **1.0.189 / versionCode 188**, accepting only current live baseline **1.0.188 / 187** or exact target; planned Check for Update Web Update **283**. Workflow includes Locker/native fingerprint validation and the existing Smart Reminder checks.
- Verification so far: `web-source/index.html` and `diary-web/index.html` are byte-identical at Git blob SHA `36f846886a823725e62a3d0c3a6ad31e023dc688`; both inline JavaScript blocks pass V8 syntax parsing (2/2). Static checks confirm 4-digit setup/unlock, optional title, search above editor, no image/file fields in Locker, separate Locker fingerprint bridge markers, current Note Lock inline wrong-PIN fix, and presence of all Diary Lock function anchors.
- **Not yet merged, built, released, or phone-tested.** Workflow execution, full lock-flow review, PR review/merge, web publisher verification, signed APK build/signature continuity, both live delivery routes, and phone testing remain pending. Do not ask user to update until all release checks pass. Do not claim device-side success.
- No existing Diary Lock/Note Lock keys, PINs, recovery data, Notes, Documents, Memories, reminders, or app/signing identity are intentionally changed.

---
# Note Lock wrong-PIN address display fix — Web Update 282 (2026-11-17)

- User reported that entering an incorrect PIN in Note Lock showed the intended wrong-PIN message together with a browser/page address. Scope was limited to the Note Lock wrong-PIN display; Diary Lock and all other features were not to be touched.
- Read the Master Register and verified live baseline before editing: APK **1.0.188 / versionCode 187**, Web Update **281**. Main commit before work: `aa926acd4ce0f827628bcd2bb189ff46cc6f6df6`.
- Created pre-edit snapshot branch `backup/before-note-lock-wrong-pin-address-fix-2026-11-17` and working branch `fix/note-lock-wrong-pin-inline-error-2026-11-17`.
- In both `web-source/index.html` and `diary-web/index.html`, replaced the Note Lock wrong-PIN browser alert with an inline error message directly below the PIN field. The message clears when the user starts entering the PIN again. The legacy Note Lock prompt path now uses the in-app PIN dialog and its inline wrong-PIN message rather than browser prompt/alert. PIN verification and stored PIN/recovery data formats were not changed.
- PR **#130** merged to main as `1df95a36c51a479263ba23f4acb9826a1e0bdf37`. Only the two HTML files changed; source and mirror are byte-identical at Git blob SHA `6fcd66e1ab915c00d86f6388f2a8f017649f5aab`.
- Web publisher commit `71f299f61fbe7346ed181f7efb7192a14a529ee1` updated the live web bundle SHA-256 to `781badc278cc9c54ad8b584a7da6cf7584631527260e3d1b8279f282f899e781`. Live `latest.json` was then advanced to **Web Update 282** with that same verified bundle hash. APK remains **1.0.188 / versionCode 187**; no new APK was built or published for this web-only change.
- Source/mirror equality, changed-file scope, absence of Note Lock wrong-PIN browser alerts/prompts in the affected paths, and live manifest version/hash were re-fetched and verified after merge. Physical-phone testing is **pending**; do not claim the address is gone on the user's device until confirmed.

---

# Remove Private Locker only — release pending (2026-11-17)

- User requested removing **Private Locker only** from My Diary. Scope: remove its Me-menu button, dedicated screen, PIN/Pattern/Favourite Name recovery, encrypted search/editor logic, and Private Locker-only Android fingerprint bridge. Do not alter Diary Lock, Note Lock, Diary fingerprint, Notes, My Documents, My Memories, reminders, or other Me features.
- Read the Master Register and verified the live main baseline before editing: APK **1.0.187 / versionCode 186**, Web Update **280**. Live `latest.json` baseline APK SHA-256: `d2dc0b3a08fed2f854c18ca1a6f5e572b4ddb269b25a24d03e576e5e71fa1f6c`; web SHA-256: `dd9d6ac44b71a2204d2bfe0ea60bd9e5cc32ab49837596c34f1140e3dd6e01c5`.
- Created pre-edit snapshot branch `backup/before-private-locker-removal-main-2026-11-17` from current `main`; working branch: `remove/private-locker-only-main-2026-11-17`.
- Removed the complete Private Locker UI and JavaScript block from both `web-source/index.html` and `diary-web/index.html`. Removed only the Private Locker-specific Android Keystore biometric methods from `scripts/add_diary_app_actions.py`; the existing Diary fingerprint methods remain. Updated build validation so it no longer requires Private Locker and still checks Diary Lock, Diary fingerprint, Notes and Smart Reminder. Release target is **My Diary 1.0.188 / versionCode 187** and **Web Update 281**.
- Post-edit source and mirror are byte-identical at Git blob SHA `8db63c5ea05ae616ebe0daab99ceecfee32edfa6` (446,227 characters). Private Locker code references are absent from the HTML, native injection script, and Locker-specific workflow guards. Existing Diary Lock, Note Lock, Diary fingerprint, Me feature storage, and Smart Reminder guard markers remain.
- **Data preservation:** no browser database, encrypted Locker records, Android Keystore entries/preferences, notes, photos, documents, memories, PINs or recovery records were deleted or reset. The old Private Locker data stores are left untouched; the removed UI no longer provides access to them.
- PR **#128** merged to main as `b1418cf738448e5e8bcfc9759f28f0f00fbb70ae`. Main source and mirror are byte-identical at Git blob SHA `8db63c5ea05ae616ebe0daab99ceecfee32edfa6` (446,227 bytes); no Private Locker markers remain in either HTML file, while Diary Lock and Diary fingerprint markers remain.
- The first APK workflow run `43944669632` failed before Android compilation because a Smart Reminder Daily-repeat validation tuple still required the removed Private Locker-only `BiometricPrompt.CryptoObject(cipher)` marker. This was corrected narrowly via PR **#129**, merged as `263da7e27b0ec18897285695cd55cf01d543c877`; all six Smart Reminder Daily-repeat markers and independent Diary fingerprint checks remain required.
- Corrected APK workflow run **43945045187** completed successfully (all jobs/steps PASS). Signing keystore/alias validation and signer-certificate continuity passed; Android project, debug APK and signed Release APK builds passed; release publication and artifact uploads passed. The signed APK artifact `My-Diary-1.0.188-signed-test-candidate` and debug APK artifact were uploaded.
- Live `latest.json` is now **My Diary 1.0.188 / versionCode 187** and **Web Update 281**. APK URL: `https://raw.githubusercontent.com/amuazzinxyz-ops/My-Diary-Updates/main/My-Diary-1.0.188.apk`; published APK SHA-256: `90f7575564d3267d49d93734179034828a8ded6ddb75e6ffa2f57ea9424118ab`. Web URL remains `https://raw.githubusercontent.com/amuazzinxyz-ops/My-Diary-Updates/main/web-source/index.html`; web SHA-256 `e41dccfd3ed91a1cca6b2d147bffb40d87a72e775d0ef601c43db7b216b1a289` matches the published source. Both source and mirror are byte-identical and no Private Locker markers remain.
- The release notes explicitly state Private Locker removed while other Diary features and existing locks are retained. No browser database, encrypted Locker records, Android Keystore entries/preferences, notes, photos, documents, memories, PINs or recovery records were deleted or reset. The old Locker data stores remain untouched, though the removed UI no longer exposes them.
- Repository merge, successful signed APK build, signer continuity, APK artifact upload and live Check for Update feed publication are **verified PASS**. Physical-phone installation/testing is **not yet confirmed**; do not claim device-side PASS until the user confirms.

# Private Locker — writing-only editor, search, recovery, Pattern and fingerprint — PUBLISHED (2026-11-17)

- User asked for a simple Private Locker writing area only: no document/photo attachments or categories; save private text and edit it later; My Documents-style search; PIN and Pattern auto-open with no separate Unlock button; Forgot PIN through Favourite Name and new PIN confirmation; fingerprint unlock; 3D styling. User explicitly instructed that Diary Lock must remain untouched.
- Implemented and merged via PR #125. Release-workflow syntax correction was made via PR #126 and commit `83857e9e1a307ed7de35b982eb03b7a2533955cb`. The first build attempt [43937492482](https://github.com/amuazzinxyz-ops/My-Diary-Updates/actions/runs/43937492482) stopped before Kotlin compilation because the added native validation tuple had a Python syntax error; it did not publish or change the feed. The tuple was corrected, and the retry completed successfully.
- Final signed APK is **My Diary 1.0.187 / versionCode 186**. Two full release runs [43937739910](https://github.com/amuazzinxyz-ops/My-Diary-Updates/actions/runs/43937739910) and [43937909534](https://github.com/amuazzinxyz-ops/My-Diary-Updates/actions/runs/43937909534) completed successfully with no failed steps. Debug APK and signed Release APK builds passed; signer certificate SHA-256 matched the previously approved fingerprint `23a4e93f3c7911dce18389ea583548700c6ad6a3759707f1cd222d07e2408b5a`.
- Live `latest.json` verified as APK **1.0.187 / 186**, APK SHA-256 `3c6369c9bbc8b1bbdcfc601cf624f0d8e8fbdfb45d070e119b8ef357cca5a1dc`, and Web Update **280**, web SHA-256 `f41a6b22298946037dd88ac4d1d8c1067481a581a4f967ce709dde87a562dae8`. Published APK `My-Diary-1.0.187.apk` exists in the main repository (2,050,159 bytes; Git blob `3c833852d9a004c725b27430565696926f0a8ba1`).
- `web-source/index.html` and `diary-web/index.html` are byte-identical at Git blob SHA `72df5db06d0bf8297f70b87f3c19fee542aa285b`. Both inline JavaScript blocks passed V8 syntax parsing (2/2). The release workflow verifies source/mirror identity, required Private Locker functions and native biometric methods, and preserves the live feed version instead of downgrading Web Update 279.
- Private Locker now uses a random 256-bit master key. Entries are encrypted with it; the master key is wrapped separately by six-digit PIN, Favourite Name recovery and optional Pattern. Correct PIN auto-opens; correct Pattern auto-opens. Forgot PIN unwraps with Favourite Name, then requires a new PIN and confirmation. Search covers saved title and body text. Editing updates encrypted entries in place. UI is writing-only with 3D styling.
- Fingerprint uses an Android Keystore AES-GCM key requiring per-use biometric authentication; its callback and key storage are isolated to Private Locker. Diary Lock's existing PIN, Pattern, Favourite Name recovery and fingerprint callback were compared against main and remain unchanged. Fingerprint is available on Android API 28+ when enrolled fingerprint hardware and the native bridge are present.
- If legacy v1 encrypted rows exist with an old/incomplete config, setup is blocked and rows are preserved; no reset or deletion is performed. The user previously confirmed the Locker was empty.
- **Phone test pending.** User must Check for Update, then test first-time PIN setup, auto-open by PIN, Pattern, Forgot PIN/Favourite Name recovery, writing/search/editing, and fingerprint on their device. Build and publication success do not mean device behavior has been tested. Do not ask them to clear app data.


---

# Private Locker first-time PIN setup repair — Web Update 279 / APK 1.0.186 (2026-11-17)

- User clarified that they had **never created a Private Locker PIN**; the first open nevertheless showed a PIN-entry screen and then an encrypted-data-format error. Scope was explicitly limited to this Private Locker setup problem; no other Diary function was to be changed.
- Read the project map and live update feed before editing. Live baseline was APK 1.0.186 / versionCode 185 and Web Update 278. Created pre-edit snapshot branch `backup/before-private-locker-first-run-fix-2026-11-17`; working branch `fix/private-locker-first-run-config-2026-11-17`.
- Source inspection found the gate treated **any** `meta/config` object as proof that a PIN was configured. The new Private Locker-only logic validates the stored salt/verifier structure before showing the unlock form. If the config is absent or incomplete and there are no encrypted entries, it shows the new 6-digit PIN setup flow. If encrypted entries exist while config is invalid/missing, it blocks replacement and preserves the entries. The save path repeats the entry check before writing config. It does not delete or reset any existing Locker record.
- PR #123 merged to main as `34885161c79ab3d0b7e1f830b3b430f8f4627846`. Only `web-source/index.html` and `diary-web/index.html` were changed; no Notes, Documents, Memories, Reminder, Note Lock, Diary Lock, or other function was intentionally changed.
- The Android workflow [43930488884](https://github.com/amuazzinxyz-ops/My-Diary-Updates/actions/runs/43930488884) completed successfully. Project verification, exact HTML injection, JavaScript `node --check`, debug build, signed Release build, and publication steps passed. APK remains **1.0.186 / versionCode 185**; live signed APK SHA-256 is `c354518f86bd525107f43341aa5d5b9cb98a8364ac058a7f256e64119b7010ea`.
- Source and mirror are byte-identical at Git blob SHA `d40dc8d7d2a64240183d923954f58bc50b1428e5`. Live update manifest now advertises **Web Update 279**, web SHA-256 `cafc2a8d95ebe83a4e83d842b3eec9d46cc5da5b9f1a5d9fca24a1d37480452f`, and the verified APK hash above. Manifest-only PR #124 merged as `41384726cd5786b1e47cf519d1e05b0fe458da6f`; no source or other feature changed in that PR.
- Web publisher run [43930957934](https://github.com/amuazzinxyz-ops/My-Diary-Updates/actions/runs/43930957934) completed successfully. Live `latest.json` was re-fetched after the run and still advertises Web Update 279 with the exact web and APK hashes above.
- **Phone test pending.** User must run Check for Update, open Private Locker and confirm the first-time screen allows creation of a new 6-digit PIN, then close/reopen and unlock. Do not claim device-side success until user confirms. Do not ask them to clear app data or reset any saved content. If the app reports an existing encrypted-entry/config warning, preserve data and ask for the exact text.

---

# Private Locker PIN base64 decoding compatibility fix — Web Update 278 / APK 1.0.186 (2026-11-16)

- User reported that entering the six-digit Private Locker PIN produced: `Failed to execute 'atob' on 'Window': The string to be decoded is not correctly encoded.`
- Created a pre-edit snapshot branch: `backup/before-private-locker-base64-fix-2026-11-16`. Working branch: `fix/private-locker-base64-decode-2026-11-16`. PR #122 merged to main as `ba578b4cf9ae06fa0ae62b5dd9f269a9bd53c70c`.
- Changed only the Private Locker base64 decoder in `web-source/index.html` and `diary-web/index.html`. It accepts standard/URL-safe Base64, whitespace and missing padding, and byte-based values; malformed data now gets a safe specific message rather than the browser `atob` exception.
- Existing encrypted database records, PIN, salt, verifier, entries, photos and documents are not reset, rewritten or migrated. User was explicitly told not to clear app data or reset Private Locker. No other Diary feature was intentionally changed.
- Source and mirror are byte-identical at Git blob SHA `935f2fff7182f1b598c3041016d64b4961e921fb`. Android workflow's exact HTML injection and `node --check` passed. Live web SHA-256 is `790c21df692bfa9ed57ecc8eb4aed569cc3597b57d2191b02979d28c5398d50b`.
- Web publisher run [43927697853](https://github.com/amuazzinxyz-ops/My-Diary-Updates/actions/runs/43927697853) completed successfully. Live Check for Update is **Web Update 278** with matching web SHA-256.
- Android build workflow [43927166691](https://github.com/amuazzinxyz-ops/My-Diary-Updates/actions/runs/43927166691) completed successfully. Debug build, exact HTML inclusion, signed Release build, signing checks and publication passed. APK remains **1.0.186 / versionCode 185**. Live APK SHA-256 is `aff03c9f0236860d118c5d634dd4cd7755e47db70a12824022ad7329a8707967`; downloaded signed candidate artifact `14255803533` was independently extracted and its APK SHA-256 matched exactly (2,044,164 bytes).
- Live `latest.json` confirms package `com.personal.diaryapp`, APK 1.0.186/code 185 and Web Update 278 with the exact hashes above. Direct APK and in-app Check for Update routes are published.
- **Phone test pending.** Do not claim that the Locker now unlocks successfully on the user's device until the user tests the existing six-digit PIN and confirms any saved Locker entries/files still open. If the same error or a new format warning appears, ask for the exact message; do not ask the user to reset or clear data.

---


# Encrypted Private Locker added to Me button — Web Update 277 (2026-11-16)

- User approved adding **🔐 Private Locker** in the Me button and explicitly instructed not to touch any other working feature.
- Created a pre-edit snapshot branch: `backup/before-private-locker-2026-11-16`. Feature branch: `feat/private-locker-me-button-2026-11-16`. PR #121 merged to main as `6312f8a13e2bbf50a7a5d4a80b1198a43e6a51c7`.
- Added one new Me-menu button and a self-contained Private Locker screen. Existing Me features and their button IDs remain present. Private Locker uses a separate IndexedDB database, `diary_private_locker_v1`; it does not use or modify the existing Notes, My Documents, or My Memories database.
- Locker entries (name, category, details, and optional file data up to 10 MB) are encrypted client-side with AES-GCM 256-bit. The key is derived from a separate 6-digit PIN using PBKDF2-SHA-256 (310,000 iterations) and a random salt. Each encrypted record uses a fresh random 96-bit AES-GCM IV. The PIN and plaintext entries are not saved in the database. The key is held only in page memory and cleared when the Locker is closed.
- No biometric/fingerprint option was added. There is no PIN recovery flow in this first version; if the user forgets the Private Locker PIN, the encrypted contents cannot be decrypted. This limitation must be clearly explained before phone setup/testing.
- Source and mirror are byte-identical at Git blob SHA `4fbfcac3cfea40cbdfef6f6b093a246e1e365dad` (459,618 UTF-8 bytes). Both inline JavaScript blocks passed syntax parsing. Existing feature IDs `calendar`, `reminders`, `kharcha`, `documents`, and `memories` remain present.
- Web publisher run [43924964904](https://github.com/amuazzinxyz-ops/My-Diary-Updates/actions/runs/43924964904) completed successfully. Manifest-only publisher run [43925180426](https://github.com/amuazzinxyz-ops/My-Diary-Updates/actions/runs/43925180426) completed successfully. Live `latest.json` now advertises **Web Update 277** and web SHA-256 `56e321d43a8dbf4fdd5ddf51a61dc74612b5d11502e5caaa55eb766c5aca04c3`. APK feed remains **1.0.186 / versionCode 185** with its existing APK hash; this feature itself changes only the web bundle.
- Android build workflow [43924964839](https://github.com/amuazzinxyz-ops/My-Diary-Updates/actions/runs/43924964839) completed successfully. Project verification, exact latest HTML injection, debug build, signed Release build, and verified publication steps passed. APK **1.0.186 / versionCode 185** is live with SHA-256 `3f556914a97df9559363dcea50ba51691bed2976b7d0c92adc2805b3027b7390`. Downloaded signed candidate artifact `14255183661`; extracted `app-release.apk` SHA-256 independently matches the live feed hash (2,043,922 bytes). The build uses the existing package/signing configuration; no identity change was requested.
- **Phone test pending.** Do not claim the Locker has been tested on the user's phone. User should first see the PIN-loss warning, create a 6-digit PIN, save a test entry and a small file, close/reopen the Locker, unlock, and confirm the data decrypts and opens.
- No existing notes, photos, documents, memories, Personal Calendar, Smart Reminder, Note Lock, Diary Lock, PIN/recovery flows, package identity, or signing identity were intentionally changed.

---

# Smart Reminder Daily repeat — APK 1.0.186 and Web Update 276 published (2026-11-16)

- User narrowed the request to **⏰ Smart Reminder only**. Personal Calendar was not changed; its existing repeat options and scheduling behavior remain untouched.
- Added an optional Daily repeat choice to Smart Reminder, saves/restores the repeat setting while editing, labels recurring reminders, and routes daily scheduling through a dedicated native bridge method. The native scheduler retains the original local clock time, re-arms for the next day, and preserves recurrence through reboot/app replacement and Snooze.
- PR #120 merged to main as `bc8e3fb0d5ad772e3064d8f1b5e49027f9b1409e`. Web source and mirror are byte-identical at Git blob SHA `9978500c11a1be5c6b8f6bdc8b0411d99ca28dac`.
- During final native-flow review, found the full-screen lock-screen activity also needed to forward the daily-repeat flag and anchor time into its Snooze/Done broadcast. Fixed this in commit `504197db2440527a42c4b0ca74300feecfa6e34f`. This is required so lock-screen Snooze retains daily recurrence. The build workflow was also touched in commit `8ae8a8ed911260a201490d7c38cffa38a29620bd` to trigger the approved release pipeline.
- Release **published and verified**: GitHub Actions run [43915287950](https://github.com/amuazzinxyz-ops/My-Diary-Updates/actions/runs/43915287950) completed successfully. The Kotlin compile failure in the first attempt was corrected by passing `snoozeUsed` to `showNotification` in commit `4dd1e6518bdffb06bf095d2460b5d5f3cd948fcd`. The successful workflow verified the APK's signing-certificate SHA-256 fingerprint against the previously approved fingerprint before publication. Published APK is **1.0.186 / versionCode 185**; Check for Update is **Web Update 276**. Live feed APK SHA-256: `6d96ac4725903da2b8e3047a305faba7ee2b1768909b50906cc099753d4ee5eb`; Web SHA-256: `21e2ada1c4fae404d076bf6c7f8529c4a221645bb4a5726ce15930de04914c1f`. Signed candidate artifact SHA-256 was independently checked against the live APK feed and matched exactly. `latest.json` now advertises the new APK and web release.
- Snapshot branch created before the release retry edits: `backup/before-smart-reminder-daily-release-retry-2026-11-16`. This snapshot is a pre-retry checkpoint, not a pre-feature-edit backup.
- Device testing is still pending. Build, release feed, APK hash, web bundle mirror, and signing-certificate continuity passed server-side checks; do not claim Daily repeat, ringtone, lock-screen display, Snooze, reboot recovery, or daily re-arming have been confirmed on the user's phone until the user tests and confirms them.
- Existing one-time Smart Reminder behavior, Personal Calendar, notes, photos, documents, memories, PIN/locks/recovery, package identity and signing identity are intended to remain unchanged.

---

# Note Restore database helper scope correction — Web Update 271 refresh — 2026-11-16

- User reported the combined Note Backup/Restore still did not work after Web Update 271. Re-inspection found that PR #113 fixed the export reader scope, but `restoreDiaryFeatureBackup()` still called `openMeFeatureDb()` directly even though that helper is local to `makeOverlay()`. This caused a ReferenceError when restoring a backup containing My Documents or My Memories.
- Created pre-edit snapshot branch: `backup/before-restore-helper-scope-fix-2026-11-16`; feature branch: `fix/restore-helper-scope-bridge-2026-11-16`.
- Minimal fix: route restore through the existing outer-scope `diaryOpenMeFeatureDbForBackup` reference and return a clear initialization error if it is unavailable. No data schema, saved data, PIN/locks, reminders, app package or signing identity changed.
- PR #114 merged to main as `23d94a0fb1a336362df6184e6e2462b76905b711`.
- `web-source/index.html` and `diary-web/index.html` verified identical at Git blob SHA `2c0811d9effd641787fc0554de580f8987ced03a`.
- Web publisher run `43887870677` completed successfully. `latest.json` still identifies Web Update 271 and advertises web SHA-256 `ad03900657bb63efc46d8808fcb66e7079fe1aeb481b909cf97a0f8f90fc89f1`; APK feed remains package `com.personal.diaryapp`, version `1.0.181 / 180`.
- Android APK workflow `43887870778` was still in progress at this entry. Do not claim a new APK was published unless the workflow and signed APK/feed checks pass. This fix is intended for the web backup/restore path.
- **Device test remains pending:** user must Check for Update, create a backup containing at least one Note, one My Documents file and one My Memories image, then restore it and confirm all three remain available and open. No claim of device-side success until user confirms.

---

# Note Backup IndexedDB stall diagnostic repair — Web Update 270 — 2026-11-16

- User confirmed Web Update 269 still left the Backup status at `Backup taiyaar ho raha hai…`. Do not describe Update 269 as a successful fix.
- Further source inspection found a second unguarded stage before Blob serialization: `openMeFeatureDb()` had no `onblocked` handler or timeout, and `meFeatureAll()` had no timeout or transaction-abort handling. A stalled IndexedDB open/read therefore left the export promise pending at the generic preparing status.
- PR #112 merged to main as `97a0d28b4abcba117eb8fa576bd66a51bd945005`. Snapshot branch: `backup/before-indexeddb-timeout-fix-2026-11-16`; feature branch: `fix/indexeddb-backup-read-hang-2026-11-16`.
- Fix adds 15-second guards to IndexedDB open/read, handles blocked/open/request/transaction errors, clears a failed cached DB-open promise for retry, and changes progress text to show whether My Documents or My Memories storage is being opened. Existing sequential Blob reads and combined Notes/Documents/Memories backup format remain.
- `web-source/index.html` and `diary-web/index.html` verified identical (Git blob SHA `34b9ac031b1bf15b3dc20abcc737aa0563bbd752`). Both inline JS blocks pass syntax parsing.
- Web publisher run `43884628011` succeeded; manifest then advanced to **Web Update 270**. Manifest publisher run `43884734576` succeeded. Live web SHA-256: `207f45fb3dff2f06a2bb1c7fb93717f60790a59eb7b2fb518954c8946d7a0e14`.
- Android build workflow `43884628024` was still in progress when this entry was prepared. Check its final result; do not claim APK publication unless signed APK/feed verification passes. Package/version currently shown in feed: `com.personal.diaryapp`, `1.0.181 / 180`.
- **Important: this is an IndexedDB diagnostic/timeout correction, not yet a device-confirmed successful backup.** After installing Web Update 270, user should tap Backup. It should now show either a more specific stage or an explicit read/open error rather than remaining indefinitely on the generic message. If it still fails, ask the user for the exact displayed message and continue from that stage.
- No stored records, PIN/lock/recovery, reminders, package identity, signing identity, or Android source were intentionally changed. Physical phone test and actual combined restore test remain pending.

---

# Note Backup preparation hang repair — Web Update 269 — 2026-11-16

- User reported the Note Backup button stayed at `Backup taiyaar ho raha hai…` after combined Notes + My Documents + My Memories backup was introduced.
- Compared the combined backup implementation with the pre-change working backup code and inspected the Android native save bridge. The combined export was reading every saved Document and Memory Blob concurrently through nested `Promise.all` / `FileReader` calls before invoking the existing native `DiaryAppActions.saveBackup` bridge. This can create high memory pressure in Android WebView when multiple or large files are present, leaving preparation apparently stuck.
- Fix: serialize Blob reads one at a time (Documents first, then Memories); add a 90-second per-file read guard with abort/error handling; show stage and per-file progress; call the existing native Save Backup bridge after the complete combined JSON is ready. Combined format and restore logic remain intact.
- Pre-edit snapshot branch: `backup/before-sequential-note-backup-2026-11-16`. Feature branch: `fix/note-backup-sequential-file-read-2026-11-16`. PR #111 merged as `a51c3ec6345937e38641debd2023d73246dc8b1b`.
- `web-source/index.html` and `diary-web/index.html` were verified identical (Git blob SHA `9a553cd58a5f583d3d11836e4fe564459c0a896e`). Both inline JavaScript blocks passed syntax parsing.
- Live manifest advanced to **Web Update 269**, web SHA-256 `8dedfec3ea1dd91aa7ef87d0e1525d66cbe1f0939a15015bd3c7f1e2734de610`. Web publisher run `43880860113` completed successfully for the merged source. Manifest-only publisher run `43881185630` was queued when this entry was written.
- Android release workflow `43880860317` completed successfully. The signed release pipeline, certificate continuity guard and APK publication steps passed. Feed remains package `com.personal.diaryapp`, version **1.0.181 / versionCode 180**, APK SHA-256 `0ffbc685979855a5190a324f1a91009056a6a57b64c95c04604c510037a5826b`. No package or signing identity change.
- Source, mirror and JavaScript syntax checks: PASS. **Physical phone test is pending.** User should use Check for Update, tap Note Backup, confirm the Android save-location picker opens, save the JSON, then test that it contains Notes, My Documents and My Memories and restore it successfully. Do not claim device-side PASS until user confirms.
- No user data was changed. No PIN/lock/recovery, reminders, package identity, signing identity, or Android project source was intentionally changed.

---

# Note Backup now includes My Documents and My Memories — Web Update 268 — 2026-11-16

- User asked to check and then extend the existing Note Backup / Restore so saved **My Documents** and **My Memories** are included with Notes.
- Source inspection confirmed Notes are stored separately from My Documents/My Memories: Notes use the Diary local storage key, while both file collections are records in IndexedDB database `diary_me_features_v1` / object store `records`, with the actual file contents in each record's `fileBlob`.
- Implemented a combined version-2 JSON backup containing Notes plus all My Documents and My Memories records. Each saved document/image Blob is serialized as a data URL so the actual file bytes travel with the backup. Restore converts those data URLs back to Blobs and puts records into the existing IndexedDB store. Existing records are preserved; duplicate IDs are skipped. Legacy Notes-only JSON backups remain supported. No other Me feature collections are added.
- Pre-edit snapshot branch: `backup/before-notes-documents-memories-backup-restore-2026-11-16`. Feature branch: `feat/combined-notes-documents-memories-backup-2026-11-16`. PR #110 merged as `75ebc2503e1347f2e708dc939bc5f86047cdce25`.
- `web-source/index.html` and `diary-web/index.html` were re-fetched after merge and are byte-identical, Git blob SHA `b7b1b6a7cc54a13433e9b2c52b8672dbaf9a289a` (495,264 UTF-8 bytes). Both inline JavaScript script blocks passed a JavaScript syntax parse check.
- Live `latest.json` was advanced to **Web Update 268** and now advertises web SHA-256 `de3db1013e71d856f9cfd9983181b7cc5042c5c6a06d7f75eb77e05efd759632`. APK feed remains signed **1.0.181 / versionCode 180**; no APK, package identity, or signing identity was changed because this is a web-only HTML feature.
- Repository/source/mirror/feed verification: PASS. **Physical phone backup-and-restore test is pending.** User must create a backup containing at least one note, one document and one memory image, then restore it and confirm all three are present and open correctly. Do not claim device-side PASS until the user confirms.
- Preserve all existing notes, documents, memories, PIN/recovery data, reminders, app identity and signing identity. Do not overwrite existing records during restore.

---

# Note Lock PIN prompts larger, bold and 3D — 2026-11-16

- User approved applying the same larger, bold, subtle 3D PIN-entry presentation used for Diary PIN prompts to the existing Note Lock.
- Changed only Note Lock presentation: the modal PIN prompt heading and input now use larger bold text, a gold raised input border/shadow, and responsive bold placeholder text. The inline locked-note PIN field and its prompt are styled to match and remain constrained to the available width.
- No Note Lock verification, PIN hashing/storage, recovery flow, lock/unlock logic, note content, photos, documents, Diary PIN/Pattern/Fingerprint, reminders, package identity, or signing identity was intentionally changed.
- Exact pre-edit source and register snapshot: `backup/before-note-lock-pin-3d-2026-11-16`. Working branch: `fix/note-lock-pin-prompt-3d-2026-11-16`. PR #109 merged as `0d5e9e35f321df067efa3c979fa85d7a90fc269c`.
- Web Update **267** is live. `web-source/index.html` and `diary-web/index.html` are byte-identical at Git blob SHA `0305e73563a2c2c70b21f3b34ba7a4a0e4d694cc` (491,240 bytes). Live `latest.json` advertises web SHA-256 `39929fbfa9587bd445ab3fb5330170b2079c6665d38d06ee0dac187ba53d2281`. Publisher run #274 (`43876273919`) completed successfully; the earlier publisher run repaired the checksum, and the webVersion was explicitly advanced to 267.
- APK build workflow run #268 (`43875834973`) completed successfully. Debug build, signed Release build, certificate continuity guard, APK publication and artifact upload passed. Signed APK **1.0.181 / versionCode 180** is published at `https://raw.githubusercontent.com/amuazzinxyz-ops/My-Diary-Updates/main/My-Diary-1.0.181.apk`. Live `latest.json` SHA-256 is `6b84da1e545e0ec89108d0b74a4c7da03e823b03b375cf2c5f1aaa36d7c0b87d`.
- Signed workflow artifact #14230471750 was downloaded and independently checked: extracted `app-release.apk` is 2,037,205 bytes and computes to the same SHA-256 as the live feed. `jarsigner` verification and `keytool -printcert` confirmed the established signing certificate SHA-256 fingerprint `23A4E93F3C7911DCE18389EA583548700C6AD6A3759707F1CD222D07E2408B5A`. The versioned APK and stable `My-Diary.apk` paths point to the same Git blob SHA `e99a6d4d268cff25ffe7c16560f269553dad9fae` and size.
- Live `latest.json` confirms package `com.personal.diaryapp`, versionName `1.0.181`, versionCode `180`, the exact APK URL/hash above, Web Update 267 and matching web SHA-256. Both direct APK and in-app Check for Update routes are live. Repository/build/publication verification is PASS.
- Physical phone visual test is pending. Do not claim device-side PASS until the user confirms the Note Lock modal and inline PIN prompt appearance and confirms Note Lock still unlocks normally.
- Permanent dual-delivery rule applies: do not tell the user to update or mark complete until both direct APK and in-app Check for Update routes and all available checks pass. Do not claim phone-side PASS until the user confirms it.

---

# Diary PIN entry prompts larger, bold and subtle 3D — 2026-11-16

- User requested that the text/names shown inside all Diary PIN-entry boxes be slightly larger, bold, and have a subtle 3D effect.
- Changed only the shared `.diary-master-pin-entry` presentation rules used by Diary PIN setup, Diary Lock Off verification, and Diary unlock/Forgot PIN recovery. Placeholder prompts now use a responsive 13–17px bold font with a subtle text shadow; PIN-entry boxes/digits get a raised gold-edge shadow and bold text treatment while retaining centered input and the existing responsive fit behavior.
- No PIN/recovery logic, Favourite Name verification, Pattern/Fingerprint behavior, Note Lock, saved notes/photos/documents, reminders, app identity or signing identity was changed.
- Exact pre-edit source and register snapshot: `backup/before-diary-pin-prompt-3d-2026-11-16`. Working branch: `fix/diary-pin-prompt-3d-2026-11-16`. Source edit commit: `fe9e77b777147bab944f83a95d07814dc4c8e194`.
- PR merge, source/mirror equality, web checksum/version publication, APK build/publication, and phone-side visual testing remain pending. Do not tell the user to update until publication verification is complete; do not claim device PASS until the user tests it.

---

# Forgot PIN: show the correct PIN prompt after Favourite Name — 2026-11-16

- User reported that after entering the correct Favourite Name during Forgot PIN, the next PIN field still displayed the Favourite Name prompt. User wants the next field to clearly ask for the new PIN.
- Fixed only the Diary unlock/recovery dialog stage placeholders: after Favourite Name verifies, the field now says `4 ankon ka PIN daalein` (localized through the existing `pinPrompt` translation); when confirming, it says `PIN dobara daalein`; on mismatch/storage retry it returns to the PIN-entry prompt. The heading continues to identify the current stage.
- Wrong Favourite Name still retains the Favourite Name prompt and existing verification/error behavior. No PIN/recovery logic, Favourite Name hash, Pattern/Fingerprint, Note Lock, saved notes/photos/documents, reminders, package identity or signing identity was intentionally changed.
- Exact pre-edit source/register backup branch: `backup/before-forgot-pin-placeholder-2026-11-16`. Working branch: `fix/forgot-pin-new-pin-placeholder-2026-11-16`. Source edit commit: `87c8b2a2a69077453da6012d550a4a23adcf74a7`. PR #107 merged as `63766e6d534468bf7fc06c73b2cea004ef793289`; Web Update 265 is live with SHA-256 `61cd433d77a1b718f68aebf2e49e202b20cba370fb9ee5e3d48538202f1c0244`. APK build run `43872194753` status must be verified separately.
- The preceding PIN-field-fit Web Update 264 is live. APK workflow run #264 (`43870906130`) completed successfully after build-guard repair; APK feed remains 1.0.180 / versionCode 179 with SHA-256 `c667b6734e17de6bd33ea488a749e0facb5c4726b711e5a76108ca16d3cf4baa`.
- Physical phone verification of this prompt correction is pending; do not claim device-side PASS until the user tests it.

---

# Diary PIN input text fits inside the box — Web Update 264 (2026-11-16)

- User requested that text shown inside PIN entry boxes fit the box, remain readable, and not be clipped.
- Scoped the adjustment to Diary master PIN setup, Diary Lock Off PIN verification, and Diary unlock/recovery PIN input. Placeholder text now uses a responsive smaller font with normal letter spacing; the input is constrained to its parent width with border-box sizing; entered PIN digits remain centered and spaced.
- No PIN/recovery logic, Favourite Name verification, Pattern/Fingerprint behavior, Note Lock, notes/photos/documents/reminders, app package identity, or signing identity was intentionally changed.
- Exact pre-edit source/register backup branch: `backup/before-diary-pin-input-fit-2026-11-16`. Feature PR #105 merged successfully to main as `428805a71113d0b697bed8e751d7e569cb8924ce`. Web publisher run #270 (`43870467554`) succeeded and published **Web Update 264**.
- `web-source/index.html` and `diary-web/index.html` are byte-identical, Git blob SHA `603f546c3d6b724ea1cd3b37a98dc836185b0fb4`, 435,721 characters. Live `latest.json` advertises webVersion 264 and web SHA-256 `3c4e833ca4ae4785a381afcfd98065875cc53452e3308c58d47c30f97c28b50e`.
- APK workflow run #264 (`43870467567`) safely stopped at the build-time HTML injection guard before APK compilation/publication. The guard expected an older PIN-input string even though the current source already includes the equivalent protected `diary-master-pin` field with numeric input and autofill protections. The web update remains live; no APK change or APK publication is claimed.
- Build-only repair is being made in `scripts/add_diary_app_actions.py` so the guard recognizes the current protected PIN input without replacing or changing it. Pre-repair backup branch: `backup/before-diary-pin-build-guard-repair-2026-11-16`; repair PR and subsequent APK build verification pending.
- Physical phone test is pending. Do not claim the text is confirmed on-device until the user checks Web Update 264 and confirms.


# Diary PIN setup and Forgot PIN text readability — Web Update 263 / APK 1.0.180 (2026-11-16)

- User requested that all text shown while creating/changing the Diary PIN and during Forgot PIN recovery be clearly readable, including headings, instructions, input placeholders, Favourite Name text, wrong-answer messages, and validation/storage errors.
- Improved only the Diary PIN setup/change dialog and Diary unlock/recovery dialog: larger bold high-contrast headings; white input boxes with thicker gold borders, dark bold text and clearer placeholders; Favourite Name uses left-aligned larger text; inline validation/error messages use a white readable panel with larger bold dark-red text. The setup flow now displays validation/storage messages inside its own dialog instead of small browser alert popups.
- No PIN/recovery logic, Favourite Name hashing/verification, temporary recovery-code flow, Pattern or Fingerprint settings, Note Lock, notes/photos/documents/reminders, app package identity or signing identity was intentionally changed.
- Exact pre-edit backup branch: `backup/before-diary-pin-text-clarity-2026-11-16`. Register pre-edit backup branch: `backup/before-diary-pin-text-register-2026-11-16`.
- PR #104 merged successfully as commit `0424851c35769a06a014aa2da078ebd87749dd7c`. The source and mirror are byte-identical: Git blob SHA `c08dc7b928bfc4de4c97723e9a06b738872177f7`, 435,069 characters.
- Web publisher run #268 (`43868880341`) succeeded. Because the mirror was already synchronized as part of the approved PR, the publisher repaired/confirmed the checksum without incrementing the version automatically. The live feed was therefore explicitly advanced to **Web Update 263** so installed clients at 262 will detect the change. Web SHA-256: `b0e79b598927fb79d9fc8210066f1cab966562a4b873b009ab42c36dd7be7e21`.
- APK workflow run #263 (`43868880476`) completed successfully. Project verification, exact HTML injection, translation audit, identity checks, debug build, signed Release configuration, release publication and artifact uploads passed. Published APK remains **1.0.180 / versionCode 179** at `https://raw.githubusercontent.com/amuazzinxyz-ops/My-Diary-Updates/main/My-Diary-1.0.180.apk`; live feed APK SHA-256: `61bb8312ad4d08b6e21ed3653f7d663a58d99197800a788839abf60f511fb45a`.
- Repository/build/publication verification is PASS. **Physical phone test pending**: user should tap **Me → Check for Update**, confirm Web Update 263 is found/applied, then inspect Diary PIN creation/change, Favourite Name input, Forgot PIN recovery and its messages for readability. Also confirm PIN recovery still works and Pattern/Fingerprint/Note Lock remain unchanged. Do not claim phone-side PASS until the user confirms.

---

# Diary PIN Forgot PIN now requires Favourite Name — Web Update 262 / APK 1.0.180 (2026-11-16)

- User-approved recovery flow implemented in Diary Lock only. When first setting a Diary PIN, the user enters the PIN, confirms it, then sets a secret **Favourite Name**. Existing PIN users who have not set one can open **Me → Diary PIN Tala**, verify their current PIN, and add the Favourite Name without changing their current PIN. Changing an existing PIN still requires the current PIN, new PIN, confirmation, and Favourite Name.
- Forgot PIN keeps the existing temporary-code popup and delivery. After entering that temporary code, the unlock flow asks for the saved Favourite Name. Only a correct Favourite Name advances to New PIN and Confirm New PIN; a wrong answer does not reset the PIN. The recovery-pending flag is persisted in localStorage so restarting the app cannot bypass the Favourite Name check.
- Favourite Name is normalized (trimmed, repeated spaces collapsed, case-insensitive) and stored as a random-salt PBKDF2-SHA256 hash using the existing 120,000-iteration digest helper; the plain Favourite Name is not stored. Choose an unusual answer that others cannot easily guess. This remains local-device recovery protection, not protection against a technically capable person who can tamper with the app's local storage.
- Existing Pattern and Fingerprint settings are preserved through Forgot PIN and become available again after the new PIN is confirmed. The existing temporary code popup remains. Existing Note Lock implementation, Note Lock PIN/recovery records, note data, photos, documents, reminders, app package identity, and signing identity were not intentionally changed.
- Existing users without a Favourite Name must set it before using Forgot PIN: go to **Me → Diary PIN Tala**, enter the current PIN, and save the Favourite Name. This migration path leaves the current PIN unchanged.
- Exact pre-edit source/register backup branch: `backup/before-diary-favourite-name-recovery-2026-11-16`. Feature PR #102 merged to main as `b518f75b187a4fba6a28b88d11713b392cba3cca`. A build-only Pattern Lock guard was updated in PR #103, merged as `0493ae3d09834fec985488ab9977c24df006745b`; the first APK workflow attempt safely stopped at the stale guard before building/publishing, and the corrected build then passed.
- Web publisher run #267 (`43865863347`) succeeded and published **Web Update 262**. `web-source/index.html` and `diary-web/index.html` are byte-identical, Git blob SHA `03009903a2c93c3b4a4c4118a7fbcc540debd2cc`, 433,830 characters. Live `latest.json` advertises web SHA-256 `d7336ecd8f77dc983f18af10151e1248212d3dffa8c23bb16056b4bd5a5c7465`.
- APK build workflow run #262 (ID `43866141500`) completed successfully. Source checks, JavaScript `node --check`, Favourite Name and Pattern Lock guards, translation audit, debug build, signed Release build, certificate continuity, APK publication, and artifact uploads all passed. The build verified the established signing-certificate SHA-256 fingerprint `23a4e93f3c7911dce18389ea583548700c6ad6a3759707f1cd222d07e2408b5a`.
- Published signed APK **1.0.180 / versionCode 179**: `https://raw.githubusercontent.com/amuazzinxyz-ops/My-Diary-Updates/main/My-Diary-1.0.180.apk`. Live feed SHA-256 `de949cf7e8c7c18bdc2a25a3d4a3f8b0704ffb7f8c6bba1e514671d04dc3b00b`; size 2,036,429 bytes. Independently downloaded signed workflow artifact #14225896841 hashes to the same SHA-256 and passed JAR signature verification. APK v2 signer certificate fingerprint matched the established fingerprint above. Both versioned APK and stable `My-Diary.apk` are present with identical Git blob SHA `dfa997a6e18fc2a90a8eb2eda8ca232c4f6e72b0` and size.
- Live `latest.json` confirms package `com.personal.diaryapp`, versionName `1.0.180`, versionCode `179`, the exact APK URL/hash above, Web Update 262 and matching web SHA-256. Both direct APK and in-app **Check for Update** routes are live.
- Repository/build/publication verification is PASS. **Physical phone test is pending**: user must update via Check for Update or install the direct APK, then test new PIN → confirm → Favourite Name, Forgot PIN temporary code → Favourite Name → new PIN → confirm, wrong Favourite Name rejection, Pattern/PIN/Fingerprint availability after recovery, and confirm Note Lock remains unchanged. Do not claim device-side PASS until the user confirms.

---

# Diary Lock three-method unlock and Forgot PIN Pattern preservation — phone verification PASS (2026-11-16)

- User explicitly confirmed that the latest Diary Lock work has been tested on their Android phone and all requested behavior is now working correctly.
- Verified behavior covered by this confirmation: **Diary PIN Tala** and **Set Diary Lock** both lead to the shared lock settings; after locking, **Pattern, PIN and Fingerprint** are all available together; using **Forgot PIN** no longer removes the saved Pattern/Fingerprint settings. The user reports all are working correctly.
- This closes the previously pending physical-phone verification for the three-method Diary unlock flow and the Forgot PIN Pattern-preservation correction. Mark as **user-reported phone PASS**; no remote access to the phone was performed.
- Live `latest.json` was re-read: package `com.personal.diaryapp`, APK **1.0.179 / versionCode 178**, APK SHA-256 `fe526e02f28e8d0726b4b6a2e676af04e03f758eeeec0b950802d9c1c078d4c0`; Web Update **261**, web SHA-256 `d2af5ea393889ca808b368e4ade9ddbd55a61ce741787cd4cbacfbd2876bdb4a`.
- Published web source and `diary-web/index.html` mirror were re-fetched and have matching Git blob SHA `5f09d742bb9f27469aa1f113889c87db7eea0f4d`. The live feed advertises the same Web Update 261 checksum. The published APK URL in the live feed is `https://raw.githubusercontent.com/amuazzinxyz-ops/My-Diary-Updates/main/My-Diary-1.0.179.apk`.
- This is a **register-only** update after the user's device confirmation. No app source, APK, mirror, `latest.json`, release version, local notes/photos/documents, PIN/recovery records, reminders, package identity or signing identity was changed.
- Exact pre-edit register snapshot is preserved on branch `backup/before-diary-lock-phone-pass-register-2026-11-16`, created from main commit `2baf6ede9e9c7339535a09f460134d38a4313bf5`.
- User confirmation is the evidence for phone-side behavior; repository metadata and source/mirror equality were independently rechecked. Do not extend this PASS to unrelated app features that the user did not test.

---

# Diary PIN Tala and Set Diary Lock use the same unlock settings — Web Update 260 / APK 1.0.178 (2026-11-16)

- User reported that the three unlock methods appeared after **Me → 🔐 Set Diary Lock**, but not after using **Me → 🔐 Diary PIN Tala**. Fixed the PIN setup/change path so its successful save opens the existing shared Diary Lock Settings. The Set Diary Lock path remains unchanged. Users can configure Pattern and Fingerprint there while PIN remains available as the third method; no method switch is required on the unlock screen.
- PR #100 merged to main as `54b09f33d5650efc585ddfacf806088cc4ec00d9`. Exact pre-edit backup branch: `backup/before-diary-pin-tala-settings-2026-11-16`.
- Only `web-source/index.html` routing and the approved APK build workflow/release metadata were changed. Existing PIN validation/recovery, Pattern storage, fingerprint bridge, Note Lock, saved notes/photos/documents, reminders, package identity and signing identity were preserved.
- APK workflow run **#259** (ID `43853662512`) completed successfully. Source validation, JavaScript syntax check, debug build, signed Release build, signing-certificate continuity check, APK publication and artifact uploads all passed. Signed APK **1.0.178 / versionCode 177** is published at `https://raw.githubusercontent.com/amuazzinxyz-ops/My-Diary-Updates/main/My-Diary-1.0.178.apk`. Live `latest.json` SHA-256: `5fd2df8d71a1d30c11f19970b047a8ccb8979d803923c162a393895e080eb92b`. Signing certificate SHA-256 fingerprint matched the previously supplied release certificate: `23a4e93f3c7911dce18389ea583548700c6ad6a3759707f1cd222d07e2408b5a`.
- Web publisher run **#265** (ID `43853662417`) completed successfully and published **Web Update 260**. Source and mirror are byte-identical, Git blob SHA `f8831197c45dcf564bcfe575f079b97a864709fd`, 427,912 characters. Live web SHA-256: `fa7faa9e81716ca9d48cacd4e038b551e9940c2aa189c9e7a3db6762cd53162e`.
- Live `latest.json` now advertises My Diary 1.0.178/code 177 and Web Update 260 with the published checksums.
- **Physical phone test pending.** User should use Me → Check for Update, then test both entry paths: Diary PIN Tala → set/change PIN → shared settings; Set Diary Lock → same settings; enable Pattern and Fingerprint as desired; lock Diary and verify Pattern, PIN and Fingerprint are simultaneously available. Confirm Note Lock and Forgot PIN recovery remain unchanged. Do not claim device-side PASS until user confirms.

---

# Diary unlock screen shows Pattern, PIN and Fingerprint together — Web Update 259 (2026-11-16)

- User clarified that all three enabled unlock methods must be visible together after locking Diary through the existing Diary Lock flow: the 3×3 Pattern grid, PIN entry box, and Fingerprint button. No method should be hidden behind a mode switch.
- PR #99 merged to main as `e15160868904677567f2f3348ffac3cff64f205b`. Exact pre-edit backup branch: `backup/before-show-all-diary-unlock-methods-2026-11-16`.
- Minimal change in `web-source/index.html`: keep the configured Pattern grid visible, keep the PIN field visible at the same time with its own label, and keep the existing manual Fingerprint button visible when fingerprint is enabled and the device bridge reports availability. Removed the obsolete Pattern/PIN mode-switch button and its unused CSS. PIN validation and Forgot PIN recovery remain unchanged.
- Updated `.github/workflows/build-diary-from-zip.yml` guard to require Pattern grid, PIN field and Fingerprint button to be rendered together. The native Kotlin fingerprint bridge, app package/signing identity, Note Lock, notes, photos, documents, reminders and stored data were not changed.
- Web publisher commit: `42cbaa7f975afb7944b1876c6f58df02b612b0fa`. Web Update **259** is published. `web-source/index.html` and `diary-web/index.html` are byte-identical, Git blob SHA `56d255beb7a8d5b98d78c11fd0697c7804f54114`, 427,838 characters. Live `latest.json` advertises webVersion 259 and web SHA-256 `a88dd78ba3712ca4ac65956d816da49725d0ac89e59398550d9ac94ebbcdccac`.
- APK feed remains signed My Diary 1.0.177 / versionCode 176 with its previously verified SHA-256 `432f48f716ece49e45147a8cbf5a4c47c406c834cd549f91e77040a9a0038cd0`; this UI-only change is delivered through the hash-verified web bundle update. No new APK build/publication is claimed for this change.
- **Physical phone test pending.** User must use Me → Check for Update, then lock/unlock Diary and confirm Pattern, PIN and Fingerprint are simultaneously visible and each works. Do not claim device-side PASS until confirmed.

---

# Optional Diary Pattern Lock — Web Update 258 / APK 1.0.177 published (2026-11-16)

- User requested Pattern Lock inside the existing **Me → Set Diary Lock** screen. Added a third optional **Pattern Lock** switch; Diary Lock (PIN) and Enable Fingerprint remain separate optional methods.
- Pattern setup uses a 3×3 dot grid. The user draws the pattern twice to confirm; visible connecting lines show the path. When enabled, Pattern is the default Diary unlock method. **Use PIN instead** remains available, along with the existing Forgot PIN recovery and native fingerprint unlock.
- Turning Pattern off removes only the saved pattern. Turning Diary Lock off also clears the pattern. Forgot-PIN recovery clears the old pattern so the user can regain access and configure a new one. Existing Diary PIN setup/recovery, native fingerprint bridge, Note Lock, saved notes, photos, documents, reminders, app package and signing identity are preserved.
- Exact pre-edit backup branch: `backup/before-diary-pattern-lock-2026-11-16`. Feature PR #98 merged to main as `a213b8a86b26fc978ecf2041e0726da42e506b6c`.
- Build workflow was advanced safely from the existing published baseline APK 1.0.176 / versionCode 175 to APK 1.0.177 / versionCode 176. Added a build-time JavaScript syntax check (Node `--check`) and Pattern Lock implementation/translation guards. All workflow steps passed, including source checks, debug build, signed Release build, established signing-certificate continuity verification, publication and artifact uploads.
- APK workflow run #257 (ID `43849339500`) completed successfully. Signed APK `1.0.177` / versionCode `176` is published at `https://raw.githubusercontent.com/amuazzinxyz-ops/My-Diary-Updates/main/My-Diary-1.0.177.apk`. Size: 2,035,252 bytes. SHA-256: `432f48f716ece49e45147a8cbf5a4c47c406c834cd549f91e77040a9a0038cd0`. APK Git blob SHA: `660a1827eaf6fc4b7642a9e0ed7b7696f7df57f0`. Stable `My-Diary.apk` has the same blob SHA and size.
- Independently downloaded signed workflow artifact `My-Diary-1.0.177-signed-test-candidate` (artifact ID `14215763598`) and verified its extracted APK SHA-256 matches the live update feed exactly. The signing fingerprint continuity check passed.
- Web publisher run #263 (ID `43849339427`) completed successfully and published **Web Update 258**. `web-source/index.html` and `diary-web/index.html` are byte-identical, Git blob SHA `3c51fc685356f1840476a3e5800666c7c7e95be0`, 428,536 bytes. Live web SHA-256: `f572a3238f08b03f801d42a573f407b49d9a97d58b05faf2393689562671ce8c`.
- Live `latest.json` advertises package `com.personal.diaryapp`, APK 1.0.177/code 176 with the matching APK checksum, and Web Update 258 with the matching web checksum.
- **Physical phone test is pending.** User must install/check the update and test: draw/confirm pattern twice; lock and unlock using Pattern; switch to PIN fallback; verify fingerprint fallback if enabled; turn Pattern off and verify PIN still works; confirm Note Lock is unchanged. Do not claim device-side PASS until the user confirms.

---

# Note Lock wrong-PIN popup beside the PIN box — Web Update 256 / APK 1.0.175 published (2026-11-16)

- User clarified the desired appearance: for Note → 🔓 Tala Band Karein, a wrong PIN should show a clear, styled pop-up immediately below the same PIN box, matching the Diary Lock message card style. The error is not placed in the PIN placeholder, and no browser address/autofill suggestion or separate browser alert is shown.
- The pop-up is attached inside the same PIN modal, directly under the PIN input. It displays the localized wrong-PIN message and a close button; after closing it, the same PIN field is available for another attempt. A wrong PIN never disables or removes the Note Lock.
- Exact source scope: only the shared four-digit PIN modal's wrong-validation feedback display. PIN validation, stored PIN/hash, recovery flow, and successful unlock/turn-off behavior remain as before.
- Pre-edit backup branch: `backup/before-note-lock-nearby-popup-2026-11-16`. Working branch: `fix/note-lock-nearby-error-popup-2026-11-16`. PR #96 merged as `727f39505592624fbb946fc9eb01124f71731590`.
- Web publisher run `43823479697` succeeded and published Web Update 256. Source and mirror are byte-identical, Git blob SHA `a614cf530967e7980ca37b08597c0b11af6d8e14`; live web SHA-256 `b63677a757a7dcb1d2fac39b97013c5e06457534262b4c04dfcd211baf49bf64`.
- APK build run `43823479626` completed successfully. Signed APK 1.0.175 / versionCode 174 is published at `https://raw.githubusercontent.com/amuazzinxyz-ops/My-Diary-Updates/main/My-Diary-1.0.175.apk`, size 2,029,100 bytes, SHA-256 `12b807e493c4d9cfcf5fb76619305db61841550ff8c50f94c0b2a5caa94f2932`. Independently downloaded signed workflow artifact has the same SHA-256; JAR signature verification succeeded. The build ran `apksigner verify --verbose --print-certs` and required the previously supplied signing-certificate fingerprint `23a4e93f3c7911dce18389ea583548700c6ad6a3759707f1cd222d07e2408b5a`; that release verification step passed.
- Live `latest.json` confirms APK 1.0.175/code 174 and Web Update 256 with the matching APK/web checksums. Check for Update release is ready. Physical phone test remains pending; do not claim device-side testing.


---

# Note Lock wrong-PIN feedback inside the same PIN box — Web Update 255 / APK 1.0.174 published (2026-11-16)

- User requested a narrowly scoped fix in **Note → 🔓 Tala Band Karein**: when the entered PIN is wrong, do not show a browser address/autofill suggestion or a separate alert. Show the existing localized wrong-PIN message inside the same PIN input box.
- Exact change is limited to the Note Lock PIN modal and its Turn Off Lock validation. A wrong PIN leaves the lock enabled; the same PIN box stays open for another attempt. PIN entry disables browser autofill hints, and the localized error is shown as the PIN field placeholder.
- Pre-edit backup branch: `backup/before-note-lock-inline-error-2026-11-16`. Feature branch: `fix/note-lock-wrong-pin-inline-2026-11-16`. Main base commit: `eef14608a7b005a44c30c7bcd56dabd66b7d4273`. PR #95 merged as `c6e6fc8b59959642781905e4116349bb46c0b8ec`.
- No PIN values/hashes, recovery codes, saved notes, photos, documents, reminders, events, app package/signing identity or unrelated features were intentionally changed.
- Source and mirror are byte-identical, Git blob SHA `102dd39ffde573197ea964c75400e414528a1e4c`. Web publisher run `43822121181` succeeded and published Web Update 255; live web SHA-256 `81db6f930f9fce1f4ac6413f2178d4420d81e5787ae7ac06acfcd16064460d67`.
- APK build run `43822121032` completed successfully. Signed APK 1.0.174 / versionCode 173 is published at `https://raw.githubusercontent.com/amuazzinxyz-ops/My-Diary-Updates/main/My-Diary-1.0.174.apk`, size 2,028,950 bytes, SHA-256 `4941dca48b201168ef49c128a399b7a1d0d98b6212567bab90ceec20bd993973`. Independently downloaded signed workflow artifact hashes to the same SHA-256. The release signing-certificate continuity and APK signature verification steps passed.
- Live `latest.json` confirms APK 1.0.174/code 173 and Web Update 255 with the matching APK/web checksums. Check for Update release is ready. Physical phone test remains pending; do not claim device-side testing.


---

# Me menu: hide Calendar view only — Web Update 254 / APK 1.0.173 published (2026-11-16)

- User clarified the requested item was option 1: the separate **Calendar** view button in the Me menu. The **📅 Personal Calendar** feature remains visible and functional.
- This change was based on the current main source (Web Update 252 / APK 1.0.172), not the older Web248 source. Existing current features and fixes were retained.
- Backup branch: `backup/before-remove-calendar-from-me-2026-11-16`. Working branch: `fix/remove-calendar-view-entry-web253-2026-11-16`.
- Exact UI change: only the Me-menu append statement for `diaryCalendarBtn` and `diaryCalendarPanel` was removed. Calendar supporting code remains dormant, not deleted. The separate `Personal Calendar` Me feature (`meFeatureTypes` item with `key:'personalCalendar'`) remains untouched.
- Calendar storage, saved calendar records, reminders, events, Diary notes/photos/documents, PIN/recovery, app package/signing identity and other Me features were not deleted or migrated.
- Final source and mirror are byte-identical, Git blob SHA `dd672331fcf13c1119cd0a492007abe06338dafc`. Web publisher run `43818616878` succeeded and published Web Update 254; live web SHA-256 is `460c93221dd9804807afe159388651de00ae59a1a4f39b801ae3e2ecc3d19e31`.
- APK build run `43818616851` succeeded. Signed APK 1.0.173 / versionCode 172 was published; live feed SHA-256 is `af87a21c24d24762f25622fad7d7bd75014d855ad343bbaca2c00d1950d3711b`. Signing and release verification steps passed.
- Phone-side Check for Update/display testing remains pending; do not claim device-side testing. Preserve all existing saved data and app/signing identity.

---

# Personal Calendar shows Gregorian dates only — Web Update 252 and APK 1.0.172 published (2026-11-16)

- User clarified that the 📆 Tareekh/Personal Calendar must show only the original Gregorian date; no Hijri date should appear inside day cells or beside the selected date.
- Exact pre-edit backup branch: `backup/before-calendar-gregorian-only-2026-11-16`. Feature branch: `fix/calendar-gregorian-only-2026-11-16`; PR #92 merged to main as `1a4846276df6a555d68c63413ac4451b27cecf7e`.
- Minimal source change: removed the Hijri-date formatter, day-cell Hijri sublabels, selected-date Hijri suffix, and the now-unused Hijri-label CSS rule. Kept Gregorian calendar day numbers, month/year heading, weekday labels, selected-date display, events, notes, language formatting, navigation, reminders, and stored calendar data unchanged. Source and published mirror are byte-identical, Git blob SHA `59ecb470e6ac5284ba80237256f9fdc6369f79cf`; no `calendarHijriLabel`, `diary-calendar-hijri`, or `islamic-umalqura` references remain.
- Corrected the web-release marker placement so the comment is after the closing HTML tag, not inside a JavaScript string. The final source passed the Android build's HTML/hash/feature guard. Web publish run `43813556039` succeeded and published Web Update 252. Live `latest.json` web SHA-256: `c1fcc1255777744b49612b8276492f71c424c6557723eef0ba4431fffd83ca71`; source/mirror match.
- APK build run `43813160746` succeeded and published signed APK `1.0.172` / versionCode `171`. Live feed confirms package `com.personal.diaryapp`, APK URL `https://raw.githubusercontent.com/amuazzinxyz-ops/My-Diary-Updates/main/My-Diary-1.0.172.apk`, SHA-256 `88d80f553e11ffb7475d358b8cb478e89670aed8f58a71dce37fe0d2a029a8df`. Downloaded signed workflow artifact independently hashes to the same SHA-256; APK size 2,028,668 bytes. Both versioned APK and stable `My-Diary.apk` exist with identical Git blob SHA `2d4f2194427a28e3a913901bc1a0a0d9c6d81f9e`.
- Signing certificate matches the previously supplied SHA-256 fingerprint `23a4e93f3c7911dce18389ea583548700c6ad6a3759707f1cd222d07e2408b5a`; APK Signature Scheme v2 verification passed. The Android build guard confirmed the embedded calendar HTML contains the Gregorian-only change and the online bundle updater remains hash-verified.
- Live feed now advertises APK 1.0.172/code 171 and Web Update 252. Phone-side display and in-app Check for Update verification remain pending; do not claim device-side testing. Preserve all existing saved data and app/signing identity.
- No notes, photos, documents, events, reminders, PIN/recovery data, app identity or signing identity were intentionally modified.
---

# Tareekh Hijri labels restored to English-only — Web Update 250 published (2026-11-16)

- User clarified that Hijri date labels should remain as they were originally: English only, with no Urdu/localized Hijri month names.
- Created exact pre-edit backup branch: `backup/before-calendar-hijri-english-only-2026-11-16`.
- Restored the original pre-Web-249 formatter in `web-source/index.html`: English locale `en-u-ca-islamic-umalqura`, numeric day and short English month name; fallback to English Islamic calendar. Both day-cell labels and selected-date heading use the same English-only formatter. Gregorian date, month headings, weekday names and other app language translations remain controlled by the selected app language.
- Source commit: `07344e9a111039aa9eaaf470663b3e46df8392d8`. The restored source Git blob is `e1bd3baded0490d460353b988290f0f0e9813335`, exactly matching the pre-localization source blob.
- Web publish run `43811264412` completed successfully. Published Web Update 250. Source and mirror `web-source/index.html` and `diary-web/index.html` are byte-identical; both blob SHA `e1bd3baded0490d460353b988290f0f0e9813335`. Live feed advertises web SHA-256 `13dbccd3b369b6674a75bfc06e48ccaa1a75a62c98c239952ba80d999addd26c`.
- APK workflow was also triggered by the source-file push; it is not part of this requested change. No APK version or signing identity was intentionally changed. User-side phone display verification remains pending.
- No saved notes, photos, calendar events, recurrence, PIN/recovery, reminders, app identity or other Diary features were edited.

---

# Calendar Hijri labels localized for all app languages — Web Update 249 published (2026-11-16)

- User asked to make the Tareekh/Calendar Hijri date display follow every supported app language.
- Exact pre-edit backup branch: `backup/before-calendar-hijri-all-language-fix-2026-11-16`, created from main before editing.
- Minimal source change in `web-source/index.html`: `calendarHijriLabel(date, locale)` now uses the active calendar locale with the Islamic Umm al-Qura calendar and full month names; it falls back to the locale's generic Islamic calendar and then Gregorian locale formatting if needed. Both each calendar day and the selected-date heading pass the active locale.
- Supported locale mapping retained: Roman English `en-IN`, English `en`, Hindi `hi-IN`, Urdu `ur-PK`, Arabic `ar`, Bengali `bn-BD`, Gujarati `gu-IN`, Marathi `mr-IN`, Tamil `ta-IN`, Telugu `te-IN`.
- Source commit: `c87c811894e5be3f6bd6d30f99b6e1fcde553140`. GitHub Actions web publish run `43810757619` completed successfully.
- Published Web Update 249. Source and mirror `web-source/index.html` / `diary-web/index.html` are byte-identical, both Git blob SHA `a7c8b01c1f1c29b35436f536f124ce3a0fcbf38f`, 406,813 characters. Live feed SHA-256: `cc29b2c5c2688b5105d5544c41192ec7bd1e439167fd3b42c6e53d7dcc0fd86a`.
- Live APK feed remains 1.0.171 / versionCode 170; this is a web-only update, no APK was published or changed. User-side phone display verification is still pending.
- No calendar event recurrence, saved notes, records, PIN/recovery, reminders, photos, app package, or signing identity was changed.

---

# Check-for-Update version mismatch — signed test candidate built (2026-11-15)

- User reported the installed Diary app says it is already newer than the update channel. Live feed baseline at investigation was APK 1.0.163 / versionCode 162, while the user's installed test candidate was reported as 1.0.166 / code 165. This is expected when a higher-version test APK is installed but the production feed remains older.
- Created backup branch `backup/before-check-update-fix-2026-11-15`.
- Updated the APK build workflow on main (commit `15b10782dc9b162a87139f735ae18710db1dbc63`) to build a signed test candidate at versionName `1.0.167` / versionCode `166`, while explicitly disabling production publication. The guard requires the expected source version and live feed baseline; no production APK or `latest.json` was changed.
- GitHub Actions run `43741458258` completed successfully. Debug build and signed Release APK build passed; the publication step was skipped by design. Signed test-candidate artifact ID `14171624884`, artifact name `My-Diary-1.0.167-signed-test-candidate`.
- Downloaded the signed artifact ZIP and extracted `app-release.apk` (2,027,847 bytes). APK SHA-256: `05fc95f0d47b3519302d407f7b9b4f72cb45fef6c6ebc69a56a0dbb2fa9844d2`.
- This is a private test candidate, NOT a published update. It does not yet eliminate the “installed version newer than update channel” condition while production latest.json remains at 1.0.163/162. Do not update production feed or publish the APK until the user installs/tests this exact candidate and explicitly approves production publication.
- Preserve all local Diary records, photos, notes, PIN/recovery data, reminders, package identity and signing identity. Do not ask the user to uninstall or clear app data.

---

# My Memories search visibility and download response repair — APK 1.0.163 published; phone test PASS (user-confirmed, 2026-11-15)

- User reported that after APK 1.0.162 the My Memories Search bar was still not visible and tapping Download produced no visible response. Re-inspection found the search field was inserted before the large form, but the Memories screen could retain an old scroll position when reopened; the Download handler wrote its status into the general status area below the large form, so progress/failure/success could remain off-screen.
- PR #73 merged as `34f8adb7a4f8ea0414d143e7c6a92baffe05811e`. Web Update 238 now resets the Memories screen scroll to the top on open, keeps the header and full-width labelled search field visible/sticky, and uses an explicit 2–3-word search hint. Each image Download button now shows immediate progress and a nearby success or actionable error message. Existing IndexedDB records and the native save bridge are not rewritten.
- Live Web Update 238 SHA-256: `00188bc0b173156df29fe1750ce5c71321db27742d14faa16f81465c7092ee5e`. Source and mirror match: Git blob SHA `c2b34333d0a09fb25134c5dc12b61f2ec9c947a4`, 399,801 characters.
- APK 1.0.163 / versionCode 162 built successfully in Actions run #230 (ID `43720948177`), but final publication audit caught that the workflow copied the APK under the old versioned filename 1.0.162 while the feed pointed to 1.0.163. Do not use the first publication commit as a valid versioned download.
- Created backup branch `backup/before-163-versioned-apk-filename-repair-2026-11-15`. PR #74 corrected the copy and git-add filenames and allowed only the previous 1.0.162/161 baseline or the exact 1.0.163/162 re-publication state. PR #74 merged as `28b7e70d6d47a5a2c0a7f9073385898e52380367`.
- Corrected APK build run #231 (ID `43721235582`) completed successfully. Debug and Release builds passed, signing certificate matches the previously supplied fingerprint `23a4e93f3c7911dce18389ea583548700c6ad6a3759707f1cd222d07e2408b5a`, APK Signature Scheme v2 verification passed, and publication/artifact upload steps succeeded.
- Live `latest.json` confirms package `com.personal.diaryapp`, versionName `1.0.163`, versionCode `162`, APK URL `https://raw.githubusercontent.com/amuazzinxyz-ops/My-Diary-Updates/main/My-Diary-1.0.163.apk`, and APK SHA-256 `0dc99b3f89f223fee522127757518e0fe2b9db71a469775932f305d91fb28f8d`. Both `My-Diary-1.0.163.apk` and stable `My-Diary.apk` exist and are the same 2,027,845-byte signed APK (same Git blob SHA `5e201f96da6af92319f91f35354825d0bf1eca46`).
- Web Update 238 remains in the live feed with the SHA above. The exact source/mirror are identical, and the build's HTML guard requires the new visible search and per-image status UI. App package and signing identity remain unchanged.
- User has now confirmed that after installing/testing APK 1.0.163 / versionCode 162, the My Memories Search Bar is visible and search works, and tapping Download successfully downloads the saved image. Mark both phone-side checks PASS based on user report; no independent remote access to the phone was performed. Preserve all existing saved memories, photos, notes, PIN/recovery, reminders, package identity and signing identity.

---

# My Memories search visibility and native image download fix — APK 1.0.162 published; phone verification pending (2026-11-15)

- User reported Web Update 237 had two defects: the My Memories Download tap did nothing, and the Search bar was not visible. Root causes were corrected: the search bar/tools are placed before the large entry form and made full-width; Android WebView's unsupported Blob `download` attribute was replaced with a native save bridge.
- PR #71 merged to `main` as `f553abfd4c51827e5983d480322ffcf752a097e0`. Web source and mirror are identical: both Git blob SHA `dac678ab43bb0e50e8c0d8225a04c56c7a690d28`, 397,166 characters. Live feed Web Update 237 has SHA-256 `f38400cc4a9bc8b4fec4c2b5577258b3804a50affe40f23ee889cb8476d3b685`.
- Android native bridge generator exposes `saveMemoryImage`, which writes the existing saved image bytes into `Downloads/My Diary` through MediaStore on Android 10+. Download reads the existing IndexedDB Blob/record and passes its bytes, filename and MIME type to the native bridge; it does not rewrite saved records, local-storage keys, PIN/recovery, notes, reminders or app identity.
- The first APK build run #228 (ID `43718886474`) succeeded but exposed a release metadata mismatch: Gradle embedded versionCode 161 while the publish script wrote 160 to `latest.json`. Do not use that first feed state as proof of a valid update for an installed versionCode 160.
- Created exact pre-fix backup branch `backup/before-162-versioncode-feed-repair-2026-11-15`. PR #72 (`https://github.com/amuazzinxyz-ops/My-Diary-Updates/pull/72`) corrected the workflow so the embedded APK and feed both use versionName `1.0.162` / versionCode `161`, and safely permits rebuilding over the partial 1.0.162/code 160 feed state. PR #72 merged as `db972088074aeb471f3edb9d76d9d516c00d77fc`.
- Corrected APK build run #229 (ID `43720081007`) completed successfully. Debug build, signed Release build, publication, and all artifact uploads passed. The release signing certificate matches the previously supplied fingerprint `23a4e93f3c7911dce18389ea583548700c6ad6a3759707f1cd222d07e2408b5a`; APK Signature Scheme v2 verification passed.
- Live `latest.json` now confirms package `com.personal.diaryapp`, versionName `1.0.162`, versionCode `161`, APK URL `https://raw.githubusercontent.com/amuazzinxyz-ops/My-Diary-Updates/main/My-Diary-1.0.162.apk`, and APK SHA-256 `d7a1a6929067fb9a3f2a3040360f34ac4dba07576084a089aacfff56adc7db3d`. The versioned APK and stable `My-Diary.apk` are published from the same signed APK (2,027,055 bytes).
- Live feed also retains Web Update 237 and its web SHA-256 above. The APK build validates the search-bar placement and native save bridge and embeds the exact published Diary HTML. Existing saved memories remain intact.
- Phone-side verification is still pending. Do not claim the user's Android device has tested the new search or Downloads/My Diary save flow until the user installs versionCode 161 and tests both. Preserve all saved data, package identity and signing identity in any future update.

---

# My Diary 1.0.159 APK filename publication correction — rebuild required (2026-11-15)

- APK 1.0.159 / versionCode 158 compiled and signed successfully in Actions run 43711555397; all build steps passed.
- Final feed/file audit found the workflow metadata pointed to `My-Diary-1.0.159.apk` but the publish step copied the signed APK as `My-Diary-1.0.158.apk`. This would make the versioned download URL fail even though the stable APK path was updated.
- Corrected workflow to publish `My-Diary-1.0.159.apk` and add that exact filename to the commit. Stable `My-Diary.apk` is also retained.
- Backup branch: `backup/before-159-apk-filename-correction-2026-11-15`. Fix branch: `fix/159-published-apk-filename-2026-11-15`.
- Rebuild and live feed / APK SHA-256 / exact URL verification are pending. Do not send a download link until the published versioned file exists and its SHA-256 matches `latest.json`.
- The prior public-bridge correction and its verification guard remain in the merged workflow. Do not claim real-device PDF/photo testing has happened.

---

# My Documents native bridge visibility correction — APK 1.0.159 in progress (2026-11-15)

- User tested APK 1.0.158 and reported tapping Open for both PDF and photo files produces no visible response.
- Rechecked the complete Android bridge generator and web caller. The WebView registers `DiaryNativeActions` as `DiaryAppActions`, and the HTML calls `window.DiaryAppActions.openDocument(...)`. The generated Kotlin bridge declaration was `private inner class DiaryNativeActions`, which can prevent Java reflection from invoking its annotated public methods. This is the leading source-level cause under investigation; device-side confirmation is still required.
- Minimal correction on feature branch: change the bridge class to a publicly accessible `inner class DiaryNativeActions`, preserving the existing `@JavascriptInterface` methods, file decoding, PDF renderer, photo viewer, FileProvider path, saved IndexedDB Blob data, and all other Diary features.
- Added a fail-closed workflow guard requiring the public bridge class and exact `webView.addJavascriptInterface(DiaryNativeActions(), "DiaryAppActions")` registration before building.
- Current live baseline: APK 1.0.158 / versionCode 157. Next planned release: APK 1.0.159 / versionCode 158. Workflow baseline and publication paths have been advanced to this exact pair.
- Exact pre-edit snapshot branch: `backup/before-public-bridge-visibility-fix-2026-11-15`. Feature branch: `fix/public-diary-bridge-visibility-159-2026-11-15`.
- PR, build, signed APK verification, publication, and physical Android test are pending. Do not tell the user to update or claim the viewer is fixed until the release is built, checksum-verified against the live feed, and the user tests both a photo and a PDF.
- Preserve all existing local Diary data and the current app signing identity. Roll back from the backup branch if validation fails.

---

# APK 1.0.158 Check for Updates download URL repair — fixed and verified (2026-11-15)

- User reported Check for Updates returned HTTP 404 after feed advertised 1.0.158. Investigation confirmed latest.json pointed to `My-Diary-1.0.158.apk`, but the publish workflow had copied the signed APK under `My-Diary.apk` and the stale name `My-Diary-1.0.157.apk`; the 1.0.158-named file did not exist. This was a release publication filename mismatch, not a device/network problem.
- Verified the published `My-Diary.apk` repository blob exists and has the same 2,025,005-byte size as the signed Release artifact. Downloaded signed artifact `app-release.apk` SHA-256 independently computed as `88155152bf7dfc839cb906b3d98d2cee2afa7f86a19fd2f46b12b252d52eed36`, matching the live 1.0.158 manifest checksum.
- Repair merged in PR #64 (merge commit `94beb779e901bb3149a7065a878f24cda9216931`): latest.json now points to the existing stable `My-Diary.apk` path. Live feed re-read confirms version 1.0.158 / code 157 and the corrected URL.
- Verified exact APK identity: repository `My-Diary.apk` is 2,025,005 bytes and Git blob SHA `c22a1ae71b18d16985c3bd1250a725592f3d6ec7`; the downloaded signed workflow artifact `app-release.apk` independently computes to the same Git blob SHA, plus SHA-256 `88155152bf7dfc839cb906b3d98d2cee2afa7f86a19fd2f46b12b252d52eed36`, matching latest.json. This proves the file at the corrected repository path is the exact signed APK bytes.
- Exact pre-fix snapshot branch: `backup/before-fix-1.0.158-apk-url-404-2026-11-15`. Repair branch: `fix/1.0.158-apk-download-url-404-2026-11-15`. URL/feed metadata verified after merge. User should retry Check for Updates; physical installation test remains pending.

---

# APK 1.0.158 publish-guard correction — build retry required (2026-11-15)

- First build run #221 (commit `f23498f27815447124ecb934bcf3fd8394b61ed1`) passed source/version guards, debug build and signed release build configuration, but failed at the publication step before changing `latest.json`.
- Log inspection found stale hard-coded values in the publish script: it still expected feed baseline 1.0.156/155 and still wrote APK version 1.0.157/156. The live feed is correctly 1.0.157/156, so the guard safely stopped publication. No incorrect APK was published and the current update feed remains unchanged.
- Minimal workflow correction: publish script now expects live feed 1.0.157/156 and publishes APK 1.0.158/157 with filename `My-Diary-1.0.158.apk`. Build baseline/source guards already targeted this same version.
- Feature code remains merged: PDF and photo Android View creation/display moved to the main UI thread. Backup branch `backup/before-document-viewer-ui-thread-fix-2026-11-15` retains the pre-change snapshot. New publish-guard repair branch: `fix/publish-guard-158-2026-11-15`.
- New build and signing/publication verification are pending. Do not tell the user to update until `latest.json`, APK checksum and signed artifact are verified. Physical phone test remains pending.

---

# My Documents PDF and photo viewer UI-thread repair — APK 1.0.158 in progress (2026-11-15)

- User reported that My Documents PDF and photo files still do not open. Re-inspection of the 1.0.157 native bridge found the root cause: `@JavascriptInterface openDocument()` runs on a WebView bridge/background thread, but both viewer branches were constructing Android Views (and the PDF dialog) on that non-UI thread. This can throw a CalledFromWrongThreadException before a viewer appears.
- Minimal native correction in `scripts/add_diary_app_actions.py`: PDF view construction, page rendering, controls and dialog presentation now run inside `runOnUiThread`; photo bitmap decoding remains off the UI thread, while ImageView/dialog creation and presentation move entirely to the UI thread. Added branch-specific logging and user-facing failure messages. Existing file bytes, IndexedDB records, filename handling, size limit, PDF pagination, image scaling, FileProvider handling for other document types, notes, PIN/recovery, reminders and app identity are preserved.
- Pre-edit exact snapshot branch: `backup/before-document-viewer-ui-thread-fix-2026-11-15`. Feature branch: `fix/document-viewers-main-ui-thread-2026-11-15`.
- Next release target: APK 1.0.158 / versionCode 157; current live baseline remains APK 1.0.157 / versionCode 156. Build guard updated accordingly. Build, signing verification, publication and physical Android testing are pending.
- Do not claim PDF or photo opening is fixed on the user's phone until the user installs the new APK and tests both file types.

---

# My Documents in-app PDF viewer — APK 1.0.157 published; phone test pending (2026-11-15)

- APK 1.0.157 / versionCode 156 is published. GitHub Actions run #220 / ID `43708118724` completed successfully: source/version guards, debug build, signed Release build, signing certificate verification, publication and APK artifact upload all passed.
- Published `latest.json` confirms package `com.personal.diaryapp`, versionName `1.0.157`, versionCode `156`, and direct APK URL: https://raw.githubusercontent.com/amuazzinxyz-ops/My-Diary-Updates/main/My-Diary-1.0.157.apk
- Published APK SHA-256 independently verified against the downloaded signed Release artifact: `3d3631b838fcb33433771f2b23ea2e1a1c0344ddaff1182ad300002735d35d5c`. The artifact contains `app-release.apk`; its exact bytes match the SHA in live `latest.json`.
- Native PDF approach: existing in-app image preview remains; PDF pages render inside My Diary using Android PdfRenderer with Previous/Next and Close controls. Other document types retain extension-based MIME and FileProvider read grants.
- PR #61 was merged, then a minimal FrameLayout.LayoutParams compile correction was committed. The first build attempt failed before publication; corrected run #220 passed all release steps.
- Existing saved records, file contents, notes, PIN/recovery, reminders, app identity and Web Update 235 are preserved by the source workflow. Check for Updates receives this native fix because latest.json now has versionCode 156, higher than the installed 155 baseline.
- Physical Android testing remains pending. Do not claim PDFs or other documents open successfully on the user's phone until the user installs 1.0.157 and confirms.
- Backup branch: `backup/before-in-app-pdf-viewer-157-2026-11-15`. Feature branch: `fix-in-app-pdf-viewer-157-2026-11-15`. PR #61: https://github.com/amuazzinxyz-ops/My-Diary-Updates/pull/61

---

## Investigation notes before the 1.0.157 release

- User tested APK 1.0.156 and reported that My Documents still does not open files. Previous external ACTION_VIEW chooser handoff is not considered fixed.
- New native approach: keep the existing in-app image preview, and render PDF pages directly inside My Diary using Android PdfRenderer with Previous/Next page controls and a Close button. This removes dependence on a third-party PDF app and FileProvider chooser for PDFs. Other document types retain the existing FileProvider chooser with extension-based MIME and explicit read grants.
- Preserve IndexedDB records and Blob bytes, filenames, delete behavior, private cache handling, 20 MB file limit, FileProvider configuration, notes, PIN/recovery, reminders, app identity and signing.
- Backup branch: `backup/before-in-app-pdf-viewer-157-2026-11-15`. Feature branch: `fix-in-app-pdf-viewer-157-2026-11-15`.
- Planned release: APK 1.0.157 / versionCode 156. Build, signing verification, publication and phone test pending. The APK release will also be delivered through Check for Updates because the installed app's updater downloads the APK whenever latest.json has a higher versionCode.
- Do not claim device-side PDF/image success until user tests the published APK.

---

# My Documents PDF/image viewer handoff — APK 1.0.156 published (2026-11-15)

- User asked that the repair be available through both direct APK installation and “Check for Updates”. Confirmed the installed app's native `checkForUpdates()` reads `latest.json`; when `versionCode` is newer than the installed app it calls `downloadAndInstall()`, which downloads the published APK and validates its SHA-256 before installation. Live feed is versionCode 155 / APK 1.0.156, so an app on versionCode 154 receives this native viewer repair through Check for Updates as well as by direct APK download. The HTML-only Web Update remains 235; it cannot replace native Kotlin code, and no fake Web Update version bump is needed.
- PR #60 merged to main as `3c677fddddc51fcb2480151bc85f104c23fbcd3a`. GitHub Actions run #217 / ID `43707045930` completed successfully: signing keystore validation, source guard, debug build, signed Release configuration, APK publication and signed APK artifact upload all passed.
- Published APK: `1.0.156`, versionCode `155`, package `com.personal.diaryapp`. Download: https://raw.githubusercontent.com/amuazzinxyz-ops/My-Diary-Updates/main/My-Diary-1.0.156.apk
- Published `latest.json` SHA-256: `12bc21001974da8557a4a32c0326d103d92c2e464786f35bc9e49dcad98e241c`. Live feed confirms versionName `1.0.156` and versionCode `155`.
- Native fix: derive MIME from filename extension; attach FileProvider ClipData and FLAG_GRANT_READ_URI_PERMISSION to both ACTION_VIEW and chooser wrapper. Existing in-app photo preview, stored IndexedDB Blob records, private cache, FileProvider paths, user data, notes, PIN and reminders are preserved.
- Device-side PDF/Office/image opening test is still pending. Do not claim the viewer works on the phone until user installs 1.0.156 and confirms. “Check for Update” alone cannot apply this native permission fix; use the APK for this release. Existing Web Update 235 remains the latest HTML package.

---

# My Documents viewer handoff hardening — APK 1.0.156 published; phone test pending (2026-11-15)

- User tested APK 1.0.155 and reported that tapping Open still did nothing despite a PDF viewer being installed. Do not treat the previous ClipData-only fix as successful.
- Rechecked current live native generator and My Documents web code. The native viewer was still relying on the MIME type supplied by the file picker and attached the URI read grant only to the inner ACTION_VIEW intent, not the chooser wrapper.
- New minimal correction: prefer MIME type derived from the saved filename extension (PDF, common Office and image formats), and attach the same FileProvider ClipData plus FLAG_GRANT_READ_URI_PERMISSION to both ACTION_VIEW and the chooser wrapper. Keep the existing in-app photo preview, private cache copy, 20 MB bound, FileProvider authority/path, and stored IndexedDB Blob records unchanged. Improve launch failure logging and user-facing toast.
- Exact pre-edit main snapshot branch: `backup/before-document-viewer-grant-156-2026-11-15`. Feature branch: `fix-document-viewer-open-156-2026-11-15`.
- Planned release APK 1.0.156 / versionCode 155. Build workflow baseline guard was advanced from live APK 1.0.155 / versionCode 154. Build, source checks, signature verification and publication are pending. Physical Android test remains mandatory; do not claim PDF/image viewer success until user confirms.
- Existing Diary records, saved files, notes, PIN/recovery, reminders, app identity/signing and Web Update 235 are intended to remain unchanged.

---

# My Documents PDF and document viewer handoff — APK 1.0.155 published (2026-11-15)

- User reported that photos now open inside My Diary on APK 1.0.154, but PDF and other documents still do not open reliably.
- Source inspection: the native FileProvider ACTION_VIEW intent set FLAG_GRANT_READ_URI_PERMISSION and a content URI as its data, but did not include the URI in ClipData. Some Android document viewers and chooser handoffs rely on ClipData to receive the temporary read grant.
- Minimal native correction: attach ClipData.newUri(contentResolver, safeName, contentUri) to the existing ACTION_VIEW intent while retaining its exact MIME type, FileProvider URI, read permission flag, chooser, private cache file and existing error messages. No storage permission or new provider is added.
- Existing photo-in-Diary viewer, My Documents saved records/Blob contents, filenames, delete behavior, notes, PIN/recovery, reminders, HTML/Web Update 235, app package and signing identity remain unchanged.
- Exact pre-edit snapshots were saved on backup branch backup/before-document-viewer-grant-155-2026-11-15 for the native generator, build workflow, latest.json and this register.
- Feature branch: fix-my-documents-viewer-grants-155-2026-11-15. APK 1.0.155 / versionCode 154 was built, signing verified and published by successful GitHub Actions run 43705928416 (commit 41efa576e15f2a8dd48e50b05ce6a6418037124a). Published APK SHA-256: caede92bf840efe33acf0d1388116eb1a673052242a3e6df54b384e0db22ad7c. Live latest.json now points to My-Diary-1.0.155.apk and the release notes describe explicit FileProvider read grants. Build artifact upload and release publication steps passed. Phone testing is still pending; do not claim PDF/Office opening works until tested on the user's Android device.
- Rollback: restore the exact snapshots on the backup branch and publish only after verifying the release baseline. Preserve all existing local Diary data.

---

# My Documents photo opening — APK 1.0.154 published (2026-11-15)

- User reported that a photo added in My Documents appears in the list but tapping Open does not open it.
- Root cause: the native bridge always handed image files to an external ACTION_VIEW chooser via FileProvider; some Android gallery/viewer apps do not handle that handoff reliably.
- Fix: image/* files (except GIF) are decoded with BitmapFactory using a downsampled image size and displayed inside My Diary in a fit-center ImageView dialog with the file name and Close action. Non-image documents and GIF retain the existing external ACTION_VIEW handoff.
- Preservation: My Documents storage, file names, saved records, delete behavior, other Diary features, reminders, package/signing identity and published HTML remain unchanged.
- Backup branch: `backup/before-my-documents-open-153-2026-11-15`. Merged feature branch: `fix-my-documents-open-153-clean-2026-11-15`. PR #57 merged as `cd5c0492cd21e5614131ce044fbea7623d8a91e4`.
- GitHub Actions run #43705047165 completed successfully: debug build, signed Release build, certificate fingerprint verification, APK publication and artifact upload all passed.
- Published APK: `1.0.154`, versionCode `153`, package `com.personal.diaryapp`; SHA-256 `650c136e3b29e8ed8f7fee1e31f0ebac98db6a22608ae9c667af8bec10b120ef`.
- Download: https://raw.githubusercontent.com/amuazzinxyz-ops/My-Diary-Updates/main/My-Diary-1.0.154.apk
- User installation and on-device photo-opening test are still pending. Do not claim device testing until user confirms.

---

# My Documents open fix — APK 1.0.153 in progress (2026-11-15)

- User reported that files added in Me → My Documents are listed but tapping Open does not launch the document.
- Source cause: saved file Blobs were rendered as object-URL anchors with target="_blank". The Android WebView does not provide a reliable external-window/document-viewer handoff for this pattern.
- Approved fix: My Documents Open now reads the saved Blob and passes its Base64 bytes, original filename and MIME type to a dedicated Android JavaScript bridge method. Native Android writes the bytes into the existing app-private cacheDir/diary-share folder, creates a read-only FileProvider content URI using the already configured provider, and launches ACTION_VIEW via a chooser. No public storage permission is added.
- Existing My Documents IndexedDB records and Blob contents remain unchanged. The temporary cache copy is not a replacement for the saved record. Other feature file handling, My Memories, reminders, notes/photos/PIN and app identity are intended to remain unchanged.
- Backup branch: `backup/before-my-documents-open-153-2026-11-15`; exact pre-edit snapshots of web source, mirror, native patch generator, build workflow, latest.json and this register are stored under `backups/*-before-my-documents-open-153-2026-11-15.txt`.
- Feature branch: `fix-my-documents-open-153-2026-11-15`. Planned release: APK 1.0.153 / versionCode 152. Build, signed publication and physical Android test are pending. Do not claim device-side success until the user installs and tests PDF and other supported file types.
- Existing FileProvider authority and `@xml/file_paths` resource are reused; no new provider or storage permission is introduced.

---

# Reminder notification persistence — APK 1.0.152 in progress (2026-11-15)

- User tested APK 1.0.151 and confirmed the reminder title/card remains visible while ringtone and screen are active, but the notification disappears when the selected ringtone/screen duration ends.
- Source root cause: `DiaryReminderWakeActivity` explicitly canceled the reminder notification at its duration timeout, immediately before finishing the wake screen.
- Approved correction: the timeout now finishes only the full-screen wake activity. It does not cancel the notification. The reminder notification remains in the notification shade/notification area until the user chooses Snooze or Done; those existing receiver actions continue to cancel it and retain their prior scheduling/stop behavior.
- The selected screen/ringtone duration, ringtone volume, Snooze intervals/limits, Done action, reminder data, HTML/Web Update, notes/photos/PIN, app package and signing identity are preserved.
- Exact pre-edit snapshots are saved on `backup/before-reminder-notification-persistence-152-2026-11-15` for the generator, workflow, update feed and this register.
- Feature branch: `fix-reminder-notification-stays-151-2026-11-15`. Planned release: APK 1.0.152 / versionCode 151. Build, signing verification, publication and physical Android test are pending.
- Build guard now fails if the wake activity timeout contains notification cancellation. Do not mark device-side behavior fixed until the user tests APK 1.0.152.

---

# Immediate reminder display — APK 1.0.151 in progress (2026-11-15)

- User tested APK 1.0.150 and confirmed the selected screen/ringtone duration now behaves correctly, but the lock-screen notification card only appears after the screen and ringtone turn off.
- Source inspection: Android launches `.setFullScreenIntent(wakePending, true)` for the reminder. While that full-screen Activity is active, Android presents the Activity instead of its ordinary lock-screen notification card. The notification is posted first, but its visible card is suppressed/covered until the Activity finishes.
- Approved fix: turn the wake-only Activity into the immediate reminder surface. It displays the reminder title/details and in-screen Snooze/Done actions immediately, while retaining `setShowWhenLocked`, `setTurnScreenOn`, `FLAG_KEEP_SCREEN_ON`, and the selected ringtone-duration timeout. The ordinary notification remains posted for the notification shade; the wake Activity cancels its stale lock-screen card at timeout so it cannot pop up late.
- Snooze and Done buttons send the same existing receiver actions with the full reminder metadata; they reuse existing Snooze scheduling, repeat limits, Done cancellation and ringtone-stop behavior. No HTML/Web Update, saved Diary data, notes/photos/PIN, app identity, package or signing identity is intentionally changed.
- Exact pre-edit snapshots are saved on `backup/before-immediate-reminder-display-151-2026-11-15`:
  - `backups/scripts-add_diary_app_actions.py-before-immediate-reminder-display-151-2026-11-15.txt`
  - `backups/-github-workflows-build-diary-from-zip-yml-before-immediate-reminder-display-151-2026-11-15.txt`
  - `backups/latest-json-before-immediate-reminder-display-151-2026-11-15.txt`
  - `backups/docs-PROJECT_MAP_AND_SECRETS_REGISTER-md-before-immediate-reminder-display-151-2026-11-15.txt`
- Feature branch: `feature/immediate-reminder-display-151-2026-11-15`. Backup branch: `backup/before-immediate-reminder-display-151-2026-11-15`.
- Planned APK version 1.0.151 / versionCode 150. Build, signature verification, publication and physical Android test are pending. Do not call the notification timing fixed until the user tests the new APK.
- Important UI distinction: during ringing, the user sees a native full-screen reminder card with the title/details and Snooze/Done; Android's regular lock-screen notification card itself may remain suppressed by full-screen intent policy. The shade notification remains posted.

---

# Selected-duration reminder screen hold — APK 1.0.150 published (2026-11-15)

- User physically tested APK 1.0.149 with a 20-second ringtone and confirmed the display went dark while the ringtone continued. Waking the display manually stopped the ringtone. Do not mark the device-side issue resolved until the user tests this release.
- Root cause confirmed in generated Kotlin source: `DiaryReminderWakeActivity` finished after a hard-coded 650 ms. Its `FLAG_KEEP_SCREEN_ON` therefore stopped protecting the display almost immediately, while the ringtone service continued for the configured duration.
- Exact pre-edit snapshots are preserved on `backup/before-duration-screen-hold-150-2026-11-15`:
  - `backups/scripts-add_diary_app_actions-py-before-duration-screen-hold-150-2026-11-15.txt`
  - `backups/-github-workflows-build-diary-from-zip-yml-before-duration-screen-hold-150-2026-11-15.txt`
  - `backups/latest-json-before-duration-screen-hold-150-2026-11-15.txt`
  - `backups/docs-PROJECT_MAP_AND_SECRETS_REGISTER-md-before-duration-screen-hold-150-2026-11-15.txt`
- PR #52 merged as commit `56d841464d39626a5131cfd900d19acc42336635`. Native script blob: `53452eeb6209bb550e5c7e7c3fff03de82dbe7a2`; build workflow blob: `dd8468a3c133845e8727d46997b1860d38e90e5f`.
- Fix: the transparent `DiaryReminderWakeActivity` now reads `diary_reminder_ring_duration_seconds` from the same reminder intent and stays alive with `FLAG_KEEP_SCREEN_ON` for `durationSeconds * 1000L`, bounded to 10–300 seconds. It then finishes at the selected duration. It remains `setShowWhenLocked(true)` / `setTurnScreenOn(true)`, translucent, and excludes the Diary MainActivity; the keyguard and public reminder notification remain visible underneath. Existing sound service continues to stop the ringtone on the same selected duration. No changes to ringtone selection/volume, Snooze options, Done, repeat limits, stored reminders, notes/photos/PIN, app identity, or web HTML.
- Build guard explicitly asserts that the wake activity reads the selected duration and finishes at `durationSeconds * 1000L`; APK version baseline advanced from 1.0.149 / code 148 to 1.0.150 / code 149.
- **APK 1.0.150 / versionCode 149 successfully built and published.** Workflow run #206, ID `43698122928`, completed successfully. Debug build, release build, source checks, APK signature verification, and artifact upload all passed. Signing certificate matched existing trusted SHA-256 fingerprint `23A4E93F3C7911DCE18389EA583548700C6AD6A3759707F1CD222D07E2408B5A`.
- Published APK URL: `https://raw.githubusercontent.com/amuazzinxyz-ops/My-Diary-Updates/main/My-Diary-1.0.150.apk`. Live `latest.json` reports SHA-256 `c9abb30f543930db3042ef851acd37b4e87558495ad06b40e27734edd97de19b`. Signed Release APK artifact ID `14155248843`.
- Web Update remains 235. Physical Android test for 1.0.150 is pending. Ask the user to install via Me → Check for Updates and test the screen-off locked reminder at 20 seconds and one longer duration. Verify screen stays on for the full selected duration, notification is visible, ringtone stops at the same moment, and display turns off afterward. Do not claim device-side success until the user confirms.

---

# Lock-screen reminder wake + notification handoff — APK 1.0.149 published (2026-11-15)

- User reported that the lock-screen display/light had regressed after APK 1.0.148 while notification visibility was being prioritized. Inspection confirmed that the notification builder no longer invoked the existing `.DiaryReminderWakeActivity`; the activity class and timed service wake lock still existed, but the wake activity was unused.
- Exact pre-edit snapshots are preserved on `backup/before-lockscreen-wake-notification-149-2026-11-15`:
  - `backups/add_diary_app_actions-py-before-lockscreen-wake-notification-149-2026-11-15.txt`
  - `backups/build-diary-from-zip-yml-before-lockscreen-wake-notification-149-2026-11-15.txt`
  - `backups/latest-json-before-lockscreen-wake-notification-149-2026-11-15.txt`
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-md-before-lockscreen-wake-notification-149-2026-11-15.txt`
- PR #51 merged as commit `03e416d83eb288baa50da1768d25b04872f445d2`. Native script blob: `be978e44605184a86b1cc55ba4d141453d156606`; build workflow blob: `6e14b3b5e75c887e1533e9823c4c93f0967daa67`.
- Native reminder notification now uses the existing transparent `DiaryReminderWakeActivity` as a brief full-screen wake handoff. The activity calls `setShowWhenLocked(true)` / `setTurnScreenOn(true)`, briefly holds `FLAG_KEEP_SCREEN_ON`, then finishes after 650 ms so the public lock-screen reminder notification can be exposed. The ringtone foreground service retains its existing timed `SCREEN_BRIGHT_WAKE_LOCK` for exactly the selected ringtone duration (`seconds * 1000L`). The notification remains public, high priority, and categorized as an alarm.
- Build guard now requires exactly one full-screen wake handoff, the quick 650 ms activity exit, lock-screen wake flags, `USE_FULL_SCREEN_INTENT`, public notification visibility, and the selected-duration service wake lock. The approved release baseline was advanced from 1.0.148 / versionCode 147 to 1.0.149 / versionCode 148.
- **APK 1.0.149 / versionCode 148 successfully built and published.** GitHub Actions workflow run #205, ID `43697285385`, completed successfully. Debug build, native/source checks, release signing and APK verification all passed. The signed APK certificate matched the existing trusted SHA-256 fingerprint `23A4E93F3C7911DCE18389EA583548700C6AD6A3759707F1CD222D07E2408B5A`.
- Published APK URL: `https://raw.githubusercontent.com/amuazzinxyz-ops/My-Diary-Updates/main/My-Diary-1.0.149.apk`. Live `latest.json` reports SHA-256 `2ebe02db06384793cee033225f973f747e66467202154f8533bfd896d7212ecc`. Signed Release APK artifact: `My-Diary-signed-Release-APK`, artifact ID `14154778171`.
- Web Update remains 235; no web HTML, app package identity, signing identity, reminder volume, Snooze options, Done behavior, calendar recurrence, local notes/photos, PIN/recovery or existing Diary data were changed.
- **Physical Android verification is still pending.** User must install APK 1.0.149 via Me → Check for Updates and test with the phone locked and screen off: notification card appears, screen/light wakes, ringtone plays and display stays on for the selected duration, then ringtone stops at the selected time. Also confirm Snooze and Done. Do not claim device-side success until user confirms.

---

# Reminder display-duration repair — merged, APK build pending (2026-11-15)

- User-reported failure on APK 1.0.146 / Web Update 235: with a 20-second reminder, the ringtone continued while the display went dark; waking the display manually stopped the ringtone. Do not mark the phone-side behavior fixed until the user tests it.
- Pre-edit live baseline: APK 1.0.146 / versionCode 145; Web Update 235; main commit `bbfcfa5bad9b04aca67b07a0df46ab0fad59a944`.
- Full pre-edit snapshot branch: `backup/before-screen-on-activity-duration-2026-11-15`. Feature branch: `feature/screen-on-activity-duration-2026-11-15`. PR #48 merged as commit `6b361a4a44dfaca11eae27092f67ca3eba28bda0`.
- Native change in `scripts/add_diary_app_actions.py`: the full-screen wake-only activity now receives the selected `diary_reminder_ring_duration_seconds`, holds `FLAG_KEEP_SCREEN_ON`, and finishes after that same duration instead of the previous fixed 1.5 seconds. The existing timed wake lock, ringtone foreground service, per-reminder 0–100% volume, ringtone selection, Snooze/Done, recurrence, local notes/photos, PIN/recovery and app identity are otherwise unchanged.
- Build workflow now validates that the selected duration is passed to the wake activity and configures APK **1.0.147 / versionCode 146**, only when the live baseline remains 1.0.146 / 145. Web publisher waits for matching signed APK 1.0.147 / 146.
- Build workflow trigger: merged native fix is on main; an additional non-functional comment commit `3d2cef836ae91cab9f04a16a181d8139ebaa64f4` was pushed to `scripts/add_diary_app_actions.py` to explicitly trigger the `push`-based APK build. This changes no runtime behavior.
- **Build and publication status: APK 1.0.147 / versionCode 146 published and verified (2026-11-15).** Build workflow run **43694693763** (run 201) completed successfully; all build, source, manifest, signing, publication and artifact-upload steps passed. The signed APK certificate SHA-256 matched the trusted fingerprint `23A4E93F3C7911DCE18389EA583548700C6AD6A3759707F1CD222D07E2408B5A`. The workflow published `My-Diary-1.0.147.apk`; live `latest.json` reports APK SHA-256 `3029ef1dd83f15be4e717958b871f8f00482aa2ddb8c7bf9e36823aeb290d100`. Live `web-source/index.html` and `diary-web/index.html` were fetched and are byte-identical (393,549 characters); Web Update remains 235 with SHA-256 `7e4509905645dadc788f48c7a784e227fa419662ddf90f82c6e1c9c39b2d3b76`. A second duplicate push-triggered run 202 (`43694803195`) later ended in failure at the debug-APK step; its publish/sign/upload steps were skipped. This does not invalidate the independently completed and published run-201 release. Physical Android testing remains pending.
- Physical Android testing remains pending even after publication. User must verify 20 seconds and longer ringtone durations, display staying on for the same duration, ringtone stopping at the same time, volume low/medium/high, and Snooze/Done in both Personal Calendar and Smart Reminder.
- Preserve the existing volume slider and all Diary data. Do not claim physical-device success from source/build checks.

---

# Timed screen wake and adjustable ringtone volume — published APK 1.0.146 and Web Update 235 (2026-11-15)

- User tested APK 1.0.145 / Web Update 234 with a 20-second ringtone: ringtone continued after the display went dark and stopped only when the screen was manually woken. User also pointed out that the requested in-app volume setting had not been implemented in the previous release.
- Starting live baseline: APK 1.0.145 / versionCode 144; Web Update 234; source/mirror blob SHA `767632bf8444a7b5ca782e194e8810c5b4e1114b`.
- Exact pre-edit full-file backups for the implementation are preserved on `backup/before-screen-wake-and-ringtone-volume-2026-11-15`. Additional exact pre-publication-trigger backups of source, mirror, feed, register and publisher workflow are preserved on `backup/before-volume-web-publish-trigger-2026-11-15`.
- Feature PR #46 merged as commit `26240b0b8fcd31ffafa3cf4ed77c4a39ab98583d`. Publication-trigger PR #47 merged as commit `8b0cde50ce6f1c4ef27e721e0aa7941e58592502`; its HTML comment is non-rendering.
- Signed APK build workflow run **43693271040** (run 200) completed with **success**. Debug build, source/translation checks, native manifest checks, signed Release build, certificate verification and artifact uploads all passed. The Release certificate matched the trusted existing SHA-256 fingerprint `23A4E93F3C7911DCE18389EA583548700C6AD6A3759707F1CD222D07E2408B5A`.
- Published APK: **1.0.146 / versionCode 145**, package `com.personal.diaryapp`; URL `https://raw.githubusercontent.com/amuazzinxyz-ops/My-Diary-Updates/main/My-Diary-1.0.146.apk`; live feed SHA-256 `dc6a4ba5be0e159901a6fb94c383f2752c8d50e8337beba19d53600dc1b88963`. The signed Release APK artifact was downloaded and extracted independently; its APK SHA-256 exactly matched the live feed.
- Web changes in `web-source/index.html`: Personal Calendar and Smart Reminder both expose a ringtone-volume slider from 0% to 100% in 5% steps, default 80%. Volume is saved with each record, restored while editing, passed to native scheduling, shown in saved-entry details and preserved through Snooze and reboot restore. Existing records without a volume default to 80%.
- Native changes: the dedicated ringtone foreground service applies per-ringtone volume via `Ringtone.setVolume` on API 28+ (older Android versions retain device alarm-volume behavior). It acquires a timed `SCREEN_BRIGHT_WAKE_LOCK` for the selected ringtone duration and releases it when playback ends or Snooze/Done is tapped. Added `WAKE_LOCK` permission. Existing ringtone selection, Snooze choices, repeat limits, Calendar recurrence, notifications, notes/photos, PIN/recovery, package identity and signing identity are preserved.
- Android display limitation: after the timed wake lock releases, Android regains control of the display and follows the device's normal screen-timeout policy. The app does not force-lock the phone with Device Admin privileges. Physical testing is required; do not claim exact forced screen-off until confirmed on the user's phone.
- Publisher workflow run **43693623141** (run 228) completed with **success** and published **Web Update 235**. Live `web-source/index.html` and `diary-web/index.html` are byte-identical, both Git blob SHA `55bdbbfe2b8dfb2d5d1bad2fc236ded224996985`. Live `latest.json` reports webVersion 235 and web SHA-256 `7e4509905645dadc788f48c7a784e227fa419662ddf90f82c6e1c9c39b2d3b76`.
- Physical Android testing is **pending**. User should open **Me → Check for Updates**, install APK 1.0.146 and Web Update 235, then test screen-off ringtone for 20 seconds and longer durations, volume at low/medium/high, Snooze and Done in both Calendar and Smart Reminder. Do not claim phone-side success before user confirmation.
- Preserve all local Diary data, notes, photos, PIN/recovery, Calendar entries, Smart Reminders, recurrence and previous backups.

---



# Timed ringtone and expanded Snooze options — published APK 1.0.145 and Web Update 234 (2026-11-15)

- User request: in both **Personal Calendar** and **Smart Reminder**, add Snooze intervals 2/5/10/15/20/30 minutes and let the user choose how long the selected ringtone actually plays: 10/20/30 seconds or 1/2/5 minutes.
- Pre-change live baseline: APK 1.0.144 / versionCode 143; Web Update 233; source/mirror blob SHA `753ea41f6296ccb1454fa1ca24cd28efd0e1c823`; native patch script blob SHA `8f47a318bcfa58719aed6352fa8d03073cc4c6df`; live feed blob SHA `b205d6b90599e5d051541348ba71130085484f38`.
- Exact full-repository backup branch: `backup/before-ring-duration-snooze-options-2026-11-15`. Verified source HTML, native patch script, both relevant workflows, latest.json and this register have identical Git blob SHAs on backup branch and main before edits.
- Feature branch: `feature/ring-duration-snooze-options-2026-11-15`.
- Native design: notification remains visible and silent; a dedicated Android media-playback foreground service plays the selected alarm ringtone and stops automatically at the chosen duration. Snooze and Done stop playback immediately. This avoids relying on Android notification-channel sound duration, which the app cannot set. Alarm loudness remains controlled by Android's device alarm-volume setting; no fake in-app volume slider is added.
- Planned APK version: 1.0.145 / versionCode 144. Web publisher waits for the matching signed native APK before exposing the updated web bundle.
- PR #44 merged as commit `36d6d39af71347d05cec87c0fb788c9d8fe66e1a`. PR #45 added a non-rendering publication marker and merged as `9e0e3d6b19689ae5ff8acc9166372cf4837b17f4`.
- Signed APK build workflow run **43691757005** (run 199) completed with **success**. Android debug and signed release builds succeeded; source HTML/JavaScript checks, native patch injection, manifest/service validation, and signing verification all passed. The signing certificate SHA-256 matched the trusted fingerprint `23A4E93F3C7911DCE18389EA583548700C6AD6A3759707F1CD222D07E2408B5A`.
- Published APK: `1.0.145` / versionCode `144`; package `com.personal.diaryapp`; URL `https://raw.githubusercontent.com/amuazzinxyz-ops/My-Diary-Updates/main/My-Diary-1.0.145.apk`; live feed SHA-256 `acd45604277ebe56ce03805f5d1da8a5642ffedba97e54c5e01c04520ea57e2c`. The signed Release APK workflow artifact was downloaded, extracted, and its APK SHA-256 independently matched the live feed exactly.
- Publisher workflow run **43691979101** (run 226) completed with **success** and published **Web Update 234**. Publisher log calculated web SHA-256 `3e419d0ba8d8165b4ab66af32c220f14ba5602fd757fdf1019851bde2b84dea4`.
- Live verification: `web-source/index.html` and `diary-web/index.html` are byte-identical, both Git blob SHA `767632bf8444a7b5ca782e194e8810c5b4e1114b`; live `latest.json` reports APK 1.0.145/144, Web Update 234, and the exact APK/web hashes above.
- Feature behavior: Snooze choices 2/5/10/15/20/30 minutes; repeat limit remains off/3/5/10; ringtone duration choices 10/20/30 seconds and 1/2/5 minutes. Notification remains visible without channel sound; a dedicated Android media-playback foreground service plays the selected ringtone and stops automatically at the chosen duration. Snooze and Done stop it immediately. Device alarm volume remains controlled by Android's alarm-volume setting.
- Calendar recurrence (daily/weekly/monthly/yearly), existing ringtone picker, exact AlarmClock schedule, notification action, wake screen, notes/photos, PIN/recovery, package identity and signing identity are preserved.
- Physical Android testing is **pending**. User should install APK 1.0.145 via **Me → Check for Updates**, then test Personal Calendar and Smart Reminder, the six Snooze intervals, repeat limits, all ringtone durations, Done, screen-off behavior, selected ringtone, and Calendar recurrence. Do not claim phone-side verification until user confirms.
- Rollback snapshot: `backup/before-ring-duration-snooze-options-2026-11-15`.
- Preserve Calendar recurrence (daily/weekly/monthly/yearly), repeat limit (off/3/5/10), ringtone picker, Done action, screen wake, local notes/photos, PIN/recovery, package identity and signing certificate.
- Rollback snapshot: `backup/before-ring-duration-snooze-options-2026-11-15`.

---

# Configurable Snooze for Personal Calendar and Smart Reminder — published APK 1.0.144 and Web Update 233 (2026-11-15)

- User request: add configurable repeat-notification/Snooze controls to **Personal Calendar** and **Smart Reminder**, without disturbing the existing working app.
- Starting live state: Web Update 232; APK 1.0.143 / versionCode 142; package `com.personal.diaryapp`; source/mirror blob SHA `aa587245b2cd93b39c9dcad8e56398c6181029d1`; starting feed blob SHA `ad0b0eb0f5412ed195b2108806b55b3b5b42c61c`.
- Backup branch: `backup/before-calendar-smart-snooze-2026-11-15`. Exact pre-edit copies were created and re-fetched byte-identically for web source, published mirror, latest.json, this register, native patch script, APK build workflow and web publisher workflow:
  - `backups/web-source-before-calendar-smart-snooze-2026-11-15.html`
  - `backups/diary-web-before-calendar-smart-snooze-2026-11-15.html`
  - `backups/latest-before-calendar-smart-snooze-2026-11-15.json`
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-calendar-smart-snooze-2026-11-15.md`
  - `backups/add_diary_app_actions-before-calendar-smart-snooze-2026-11-15.py`
  - `backups/build-diary-from-zip-before-calendar-smart-snooze-2026-11-15.yml`
  - `backups/publish-diary-web-update-before-calendar-smart-snooze-2026-11-15.yml`
- Feature PR #43 merged successfully as commit `abf7f5d303b390e113c1e43c3ec0f632a50003d6`. Changed files: `web-source/index.html`, `scripts/add_diary_app_actions.py`, `.github/workflows/build-diary-from-zip.yml`, `.github/workflows/publish-diary-web-update.yml`, and this register.
- Behavior published: Calendar event reminders and Smart Reminders each offer Snooze intervals 5/10/15/30 minutes and repeat limits off/3/5/10. Defaults are 10 minutes and 3 repeats. The Android notification Snooze action schedules the selected interval; the action disappears after the selected maximum is reached; Done remains. The native scheduler persists interval, repeat limit and used count across alarm scheduling/reboot. Calendar's existing Daily/Weekly/Monthly/Yearly event recurrence remains separate and unchanged.
- Existing ringtone picker and saved sound URI, alarm time, exact AlarmClock scheduling, notification sound channel, screen wake, Done, notes, photos, PIN/recovery, package identity and signing identity remain preserved. Existing notification sound duration and volume remain controlled by Android/device sound settings; this release does not add an independent ringtone-duration or 0–100% volume control.
- Signed APK build workflow run **43689606586** (run 198) completed with **success**. Project verification, exact HTML injection, translation audit, debug APK, signed Release APK, signing verification, feed publication and artifact uploads all succeeded. The signing certificate SHA-256 matched the established trusted fingerprint `23A4E93F3C7911DCE18389EA583548700C6AD6A3759707F1CD222D07E2408B5A`.
- Published APK: `1.0.144` / versionCode `143`; package `com.personal.diaryapp`; URL `https://raw.githubusercontent.com/amuazzinxyz-ops/My-Diary-Updates/main/My-Diary-1.0.144.apk`; live feed SHA-256 `d323978b43c05015bb325d05a14093ae4d2731f795762671201c28788d02698b`. Downloaded signed Release workflow artifact was independently extracted and hashed; its APK SHA-256 exactly matches the live feed. Artifact ZIP SHA-256: `d4c00f1b806de2640dcdeecf06ebde6e37188a70e517ed79c9a3b3066e4996be`.
- The first publisher run **43689606559** completed successfully but correctly skipped the web publication until the matching native APK was available. After APK publication, publisher run **43689806341** completed successfully and published **Web Update 233**. Publisher commit: `1ed331bf4235786473c376fb4be784910922962e`. Publisher log independently calculated web SHA-256 `b3d902bbddf4868c5108ae405fad70003a6cb0ab5c6d3c3252a643260ae61177`.
- Live verification after publication: `web-source/index.html` and `diary-web/index.html` are byte-identical, both Git blob SHA `753ea41f6296ccb1454fa1ca24cd28efd0e1c823`; both contain the new snooze controls. Live `latest.json` blob SHA `b205d6b90599e5d051541348ba71130085484f38` reports APK `1.0.144/143`, `webVersion=233`, and the exact APK/web hashes above.
- Physical Android testing is **pending**. User must use **Me → Check for Updates**, install APK 1.0.144 and Web Update 233, then test both features, all snooze intervals/limits, Done, Calendar recurrence, and an existing saved ringtone. Do not claim device-side verification until the user confirms.
- Rollback: restore exact source/script/workflow/register/feed copies from `backup/before-calendar-smart-snooze-2026-11-15`; if rolling back after publication, restore the desired source and publish a higher webVersion. Preserve local notes, photos, PIN and all existing user data.

---

# Double-size purple/gold 3D welcome card — published Web Update 232 (2026-11-15)

- User request: make the existing welcome-screen card much more beautiful and approximately double its current size.
- Starting live state: Web Update 231; APK `1.0.143` / versionCode `142`; package `com.personal.diaryapp`; source and mirror blob SHA `708e08ebcb27e3a78e98775740b7c75d09003ebe`; starting feed SHA-256 `5a2817aa33c53714ee37b2522739292649fad02be6cacc30dc8e4c19978d5647`.
- Scope: CSS-only change appended to `web-source/index.html`. The existing welcome card remains full-width within the phone viewport; its height is doubled to 300px (280px on narrow/mobile screens), icon enlarged to 70px (62px mobile), title to 42px (36px mobile), and subtitle to 21px (18px mobile). Added richer gold double border, layered purple/gold 3D depth, brighter lavender/gold gradient and deeper press feedback.
- Preserved the existing single welcome card, original card IDs, direct parent tap handler calling `openOverlay()`, existing PIN/open flow, language text and layout width. No JavaScript or HTML behavior changed.
- Explicitly untouched: notes, photos, storage/data keys, PIN/recovery, trash, note actions, reminders, language logic, updater logic, Android source, APK, package identity, signing data and permissions.
- Pre-edit backups created on `backup/before-double-welcome-card-2026-11-15` and re-fetched byte-identical to live files before the change:
  - `backups/web-source-before-double-welcome-card-2026-11-15.html` (blob `708e08ebcb27e3a78e98775740b7c75d09003ebe`)
  - `backups/diary-web-before-double-welcome-card-2026-11-15.html` (same blob)
  - `backups/latest-before-double-welcome-card-2026-11-15.json`
  - `backups/register-before-double-welcome-card-2026-11-15.md`
- Feature branch `feature/double-welcome-card-size-2026-11-15`; PR #42 merged as `f51d1f77398da641d1182b0b1779a674ad5358a5`. Only `web-source/index.html` changed (53 additions, 0 deletions).
- Publisher workflow completed and published Web Update 232. Live `web-source/index.html` and `diary-web/index.html` are byte-identical at blob SHA `aa587245b2cd93b39c9dcad8e56398c6181029d1`. Live feed `latest.json` reports `webVersion=232` and `webSha256=a1678160ed47a258decd5ab53b2687f4e8f093eb3914faaf653d2742244666b6`.
- Static validation after publish: new CSS block exists exactly once; desktop/mobile height and responsive font sizes are present; original single-card style and direct tap handler remain. Source and mirror are byte-identical.
- APK remains `1.0.143` / versionCode `142`; no APK rebuild or signing changes.
- Physical Android verification is pending. User should tap Me → Check for Updates only if needed; user previously confirmed welcome-card tap opens Diary, and this update is CSS-only. Do not claim phone-side appearance confirmation until the user confirms.
- Rollback: use the exact pre-change backups on `backup/before-double-welcome-card-2026-11-15`; if already published, restore the desired source and publish a higher webVersion. Preserve all local notes, photos and PIN/recovery data.

---

# Direct tap from the welcome screen into My Diary — published Web Update 231 (2026-11-15)

- User clarified that they are still on the welcome screen and cannot enter the app to reach Me / Check for Updates. The welcome card itself must directly open Diary when tapped.
- Checked live Web Update 229. `#diaryMyNotesEntry` was the button, but the action was bound to that button. To make the entire visible welcome entry area a direct tap target, moved the action to its parent `#diaryHomeEntryHost` using a single `onclick` handler; the card button no longer needs its own click handler. Added pointer cursor and mobile touch-action styling to the host. The action calls the existing `openOverlay()` function, which preserves the current PIN unlock flow.
- The one purple/gold 3D card, visible label/language, layout, notes/photos, local storage, PIN/recovery, reminders, and all other app behavior are unchanged. No APK/source Android changes.
- Pre-edit backups on `backup/before-direct-welcome-card-entry-2026-11-15` were re-fetched and verified byte-identical for web source, mirror, latest feed, and this register.
- Static validation after publish: host click action exists once, button handler is cleared, host/card IDs and 3D CSS retained, and `openOverlay()` still routes to existing PIN unlock or Diary panel. Literal escaped CSS newline was corrected to a real newline. Live source and mirror are byte-identical at blob SHA `dd15a47f6a3636af64c146f64773a35240071706`. Feed is Web Update 231 with SHA-256 `5a2817aa33c53714ee37b2522739292649fad02be6cacc30dc8e4c19978d5647`. Publisher commit `e84567feac1e81efc3d56cc618f763c90f80b143` completed. APK remains `1.0.143` / versionCode `142`; no APK rebuild. Physical tap-to-open remains pending user confirmation.

---

# Restore the visible welcome card's Diary tap action — published Web Update 229 (2026-11-15)

- User reported that the one visible welcome card did not open Diary when tapped. Apologized and checked the live Web Update 228 source before changing anything.
- Root cause: `installEntry()` attached the click listener only inside the `if (!b)` creation branch. If the visible `#diaryMyNotesEntry` button already existed in the DOM, the function updated its localized title/subtitle but never attached the open action. This is the exact case that can leave a visible card without a working tap.
- Minimal correction: keep the same single visible card, 3D CSS, language text, and `openOverlay()` behavior; move the click binding outside the creation-only branch and assign it idempotently with `b.onclick = function(e){ e.preventDefault(); e.stopPropagation(); openOverlay(); }`. The new button is still created only when absent. This ensures both newly created and already-existing card elements open the Diary.
- Pre-edit backups created on `backup/before-restore-diary-card-tap-2026-11-15` and re-fetched byte-identical to live files: `backups/web-source-before-restore-diary-card-tap-2026-11-15.html`, `backups/diary-web-before-restore-diary-card-tap-2026-11-15.html`, `backups/latest-before-restore-diary-card-tap-2026-11-15.json`, and `backups/register-before-restore-diary-card-tap-2026-11-15.md`.
- Scope: one JavaScript binding correction in `web-source/index.html`; publisher will regenerate the web mirror and feed. No CSS/card layout, notes/photos/local storage, PIN/recovery, trash, reminder, language, Android source, APK, package identity, signing or permissions changes.
- Static validation after publish: exactly one welcome entry creation block; idempotent `b.onclick` binding is outside `if (!b)`; no creation-only click listener remains; original `openOverlay()` and overlay/PIN flow are intact; 3D welcome CSS is unchanged. Live `web-source/index.html` and `diary-web/index.html` are byte-identical at blob SHA `3eeff193426aae2742a10966808a22fef6e37c86`. Feed reports `webVersion=229` and `webSha256=ec2a9fa048ceae90bd8e911bde490f1f4d4d6f5203377233f4810ffc5e101976`. Publisher bot commit `5a1e9563961cb3ad9f5a2c6a9985a5d6365cc5f0` succeeded and updated the mirror/feed. APK remains `1.0.143` / versionCode `142`; no APK rebuild. Physical tap-to-open still requires user confirmation on the phone.
- Rollback: restore the exact pre-edit source backup and publish a higher webVersion; preserve all local Diary data.

---

# Correct welcome screen: remove upper heading and keep the lower tappable card — published Web Update 228 (2026-11-15)

- User correction: the previous attempt left the wrong welcome content visible. User clearly specified that the **upper** `📒` / heading / subtitle block must be removed and the **lower tappable Diary card** must remain and receive the 3D design. Apologized for the previous mistake.
- Root cause found by inspecting live source: Web Update 227's CSS had been inserted into the JavaScript string used to generate a report document, not into the actual app document. It did not style the live welcome screen. Removed that misplaced style block.
- Corrected actual document: appended the CSS to the real main HTML document immediately before its final `</body>`. Hides only `.diary-home > .diary-mark`, `.diary-home > h1`, and `.diary-home > p`; removes the outer `.diary-home` card surface; retains `#diaryHomeEntryHost` and the existing `#diaryMyNotesEntry` as the one visible raised purple-and-gold 3D card.
- Preserved the existing icon, localized title/subtitle, original click handler calling `openOverlay()`, language behavior, all JavaScript, and mobile tap target. No notes, photos, local storage/data keys, PIN/recovery, trash, reminders, updater logic, Android source, APK, package identity, signing data, or permissions changed.
- Before-edit backups created and re-fetched byte-identical on `backup/before-correct-welcome-card-2026-11-15`:
  - `backups/web-source-before-correct-welcome-card-2026-11-15.html`
  - `backups/diary-web-before-correct-welcome-card-2026-11-15.html`
  - `backups/latest-before-correct-welcome-card-2026-11-15.json`
  - `backups/register-before-correct-welcome-card-2026-11-15.md`
- Static checks: corrected CSS exists in the actual main document after the app scripts; upper logo/title/subtitle selectors are hidden; outer card surface is transparent; purple/gold 3D button styling is present; original button creation, localized text, and click handler remain; misplaced Web Update 227 style is absent.
- Feature branch `feature/correct-single-welcome-tap-card-2026-11-15`; PR #38 merged as `40f93bfbc5571c4a0609a52a8ae9d0a26eb7dac9`. Only `web-source/index.html` changed (15 additions, 66 deletions).
- Publisher workflow run `43684770691` completed with **success**. Live Web Update 228: source and `diary-web/index.html` mirror are byte-identical at blob SHA `abdbde83c4ccbef1ba63204b01153ce8950bc942`. Feed web SHA-256 `84299b287b0dcd1ae16ec17ac3a3621d16664c7cf7c9b1ff044109d932e76768`.
- APK remains `1.0.143` / versionCode `142`; SHA-256 `4eccf17f61389bbb112a1daf910eb88d11315c19c22efa2d9e71171115688961`. No APK rebuild.
- Physical phone confirmation is still pending. User should install **Web Update 228**, then verify that the upper heading is gone, only the lower 3D tap card remains, and tapping it opens Diary. Do not claim device-side success before the user confirms.
- Rollback: use the exact pre-edit files on `backup/before-correct-welcome-card-2026-11-15`; if already published, restore the desired source and publish a higher webVersion. Preserve all local notes, photos, and PIN/recovery data.

---

# Remove duplicate upper welcome heading; style the tap card — published Web Update 227 (2026-11-15)

- User request: remove the upper repeated `📒 Meri Diary` and subtitle; keep the lower tappable Diary entry and give that same tap target a beautiful raised 3D design.
- Starting live state: Web Update 226; APK `1.0.143` / versionCode `142`; package `com.personal.diaryapp`; source/mirror blob SHA `680e1b78909a5f5dc0cfacf7e741e8edea4a7052`; starting feed web SHA-256 `4f01fc4507093b086cb53965632563dfcf9cb39f0463fe7731b012a50eb09785`.
- Scope as originally intended, but the implementation was faulty: the CSS block was accidentally inserted inside the report-export HTML string rather than the main Diary document. It therefore did not apply to the actual welcome screen. User reported that the wrong card remained. This was acknowledged and corrected in Web Update 228 below; do not treat Web Update 227 as the successful visual fix.
- No JavaScript or HTML structure changed; comparison against the exact starting source confirms the only source difference is the inserted CSS block. Explicitly untouched: notes, photos, local storage/data keys, PIN/recovery, trash, note actions, reminders, updater logic, Android source, APK, package identity, signing data and permissions.
- Pre-edit backups created and re-fetched byte-identical on branch `backup/before-remove-upper-welcome-duplicate-2026-11-15`:
  - `backups/web-source-before-remove-upper-welcome-duplicate-2026-11-15.html`
  - `backups/diary-web-before-remove-upper-welcome-duplicate-2026-11-15.html`
  - `backups/before-remove-upper-welcome-duplicate-2026-11-15.json`
  - `backups/docs-before-remove-upper-welcome-duplicate-2026-11-15-register.md`
- Feature branch `feature/remove-upper-welcome-duplicate-3d-card-2026-11-15`; PR #37 merged as `b3577aecd7b3d8f3bdd48808e48dd225f6c0380b`. Only `web-source/index.html` changed (66 additions, 1 deletion).
- Web publisher workflow run `43684123945` completed with **success**. Publisher commit: `08147f57f41dece17044d8292c4dab2767f670ee`.
- Post-publish verification: live source and `diary-web/index.html` mirror are byte-identical; both blob SHA `ba42b35b2dc2351fbf999b8e9560678bc5138fbd`. Live `latest.json` blob `acb7aff27f8bd014c22383b4b8471f1041737553` reports `webVersion=227` and `webSha256=848cac17d663e6073d32688e6cfdb423c3735e31fd1f0fe35feee476029de335`. Independently calculated SHA-256 from the exact source text matches the feed.
- APK unchanged: `1.0.143` / versionCode `142`; SHA-256 `4eccf17f61389bbb112a1daf910eb88d11315c19c22efa2d9e71171115688961`. No APK rebuild or signing change.
- Physical-device verification of Web Update 227 is pending. Ask the user to use **Me → Check for Updates**, install Web Update 227, confirm only the lower 3D tap card remains (no upper duplicate), and tap it to verify Diary opens. Do not claim phone-side success until confirmed.
- Rollback: use the exact pre-change files on `backup/before-remove-upper-welcome-duplicate-2026-11-15`; if already published, restore the source and publish a higher webVersion. Preserve local notes, photos and PIN/recovery data.

---

# Single 3D welcome card — published Web Update 226 (2026-11-15)

- User request: make the Diary welcome screen one beautiful, raised 3D card, after checking the existing layout and choosing the appropriate design.
- Starting live state: Web Update 225; APK `1.0.143` / versionCode `142`; package `com.personal.diaryapp`; source/mirror blob SHA `c77067a5c9a360613d05f567a70e58c9f971ce87`; feed web SHA-256 `efdfc3c03c3ff5f040df7754830bd3c2d110d219c38ecd1a7b20becd0de6e5ff`.
- Inspection found the welcome page had two visual layers: the outer `.diary-home` panel and a separate raised `#diaryMyNotesEntry` card hosted outside it. This change makes one unified card.
- Web-only scope: `web-source/index.html`. Moved the existing `#diaryHomeEntryHost` inside the existing `.diary-home` main panel. The logo, localized heading/subtitle, and original Diary open action now sit within one purple-and-gold 3D card. The open action retains its icon/title/subtitle, full-width mobile tap target, and existing click handler but no longer draws a separate card surface. Added soft layered shadows, inset highlights, gold accent, and mobile sizing.
- Preserved: existing language selector move into Me, all 10 language choices, localized welcome title/subtitle, RTL handling, existing entry button creation/click behavior, and all other app behavior.
- Explicitly untouched: notes, photos, local storage/data keys, PIN/recovery, trash, note actions, reminders, updater logic, Android source, APK, package identity, signing data and permissions.
- Pre-edit backup branch: `backup/before-single-3d-welcome-card-2026-11-15`. Four backup files were re-fetched and verified byte-identical to the live starting files:
  - `backups/web-source-before-single-3d-welcome-card-2026-11-15.html`
  - `backups/diary-web-before-single-3d-welcome-card-2026-11-15.html`
  - `backups/latest-before-single-3d-welcome-card-2026-11-15.json`
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-single-3d-welcome-card-2026-11-15.md`
- Feature branch: `feature/single-3d-welcome-card-2026-11-15`. PR #36 merged as `1393a8c97eb419d2c340b51b7beb1b53daceef0c`; only `web-source/index.html` changed (52 additions, 1 deletion).
- Publisher commit: `b98b19a983dab2c51b7f9119b2ac9766d95dcdfb`. Published Web Update 226. Live source and mirror are byte-identical at blob SHA `680e1b78909a5f5dc0cfacf7e741e8edea4a7052`. Live `latest.json` blob `e858d428fc4b19515d8deb1f71918d2065d544a9` reports `webVersion=226` and `webSha256=4f01fc4507093b086cb53965632563dfcf9cb39f0463fe7731b012a50eb09785`.
- Static validation: both inline JavaScript blocks parse; exactly one entry host and one language selector remain; the entry host is inside the welcome card; the existing entry button and click handler remain; the new single-card styling is present. Source and mirror are byte-identical.
- APK remains `1.0.143` / versionCode `142`; SHA-256 `4eccf17f61389bbb112a1daf910eb88d11315c19c22efa2d9e71171115688961`. No APK rebuild or signing changes.
- Phone-side visual confirmation: user confirmed on 2026-11-15 that the welcome screen shows one card. The user did not explicitly confirm the tap-to-open action, so that interaction remained unverified at this point.
- Rollback: use the exact pre-change backups on `backup/before-single-3d-welcome-card-2026-11-15`; if already published, restore the source and publish a higher webVersion. Preserve local notes, photos and PIN/recovery data.

---

# Move language selector into Me menu — published Web Update 225 (2026-11-15)

- User request: move the existing Language / Zaban selector from the Diary welcome screen into the **Me** menu.
- Starting live state: Web Update 224; APK `1.0.143` / versionCode `142`; package `com.personal.diaryapp`; source/mirror blob SHA `ab93dac3ceedf270c06c8714c8e31b90295672dc`; feed web SHA-256 `36ee6089a3a0dde0700386efa8a083e9f28d3998b8e10566caa4eb18a144bdda`.
- Scope: web-only change to `web-source/index.html`. Reused and moved the original `.diary-language` wrapper and its one `#diaryLanguageSelect` control into `#diaryDiaryMePanel` when the Diary overlay is created; hid it on the welcome screen; styled it as a full-width selector inside Me. Updated the language-label lookup to find the moved label outside `.diary-home`.
- Preserved all 10 existing language choices, the same select element/id, the existing change listener, direction handling (including Urdu/Arabic RTL), the existing `diary_language_v204` key, and all other language translation logic.
- Explicitly untouched: notes, photos, storage data/keys, PIN/recovery, trash, note actions, updater logic, Android source, APK, package identity, signing data and permissions.
- Pre-edit backup branch: `backup/before-move-language-selector-into-me-2026-11-15`. All four backups were re-fetched and verified byte-identical to the starting live files:
  - `backups/web-source-before-move-language-selector-into-me-2026-11-15.html` (blob `ab93dac3ceedf270c06c8714c8e31b90295672dc`)
  - `backups/diary-web-before-move-language-selector-into-me-2026-11-15.html` (same blob)
  - `backups/latest-before-move-language-selector-into-me-2026-11-15.json`
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-move-language-selector-into-me-2026-11-15.md`
- Feature branch: `feature/move-language-selector-into-me-2026-11-15`. PR #35 merged successfully as `58419af5eb0169eb67f61ceb3e38c3af983cf7bf`; diff changed only `web-source/index.html` (11 additions, 1 deletion).
- Publisher bot commit: `3659ba7bc493cabb5e073972732c6fa2408db4c2`. Its diff confirms the mirror and feed were published: live `web-source/index.html` and `diary-web/index.html` are byte-identical at blob SHA `c77067a5c9a360613d05f567a70e58c9f971ce87`. Live `latest.json` blob `4e748ab90b78e2e78366f3caa77b1a632f1bac40` reports `webVersion=225` and `webSha256=efdfc3c03c3ff5f040df7754830bd3c2d110d219c38ecd1a7b20becd0de6e5ff`.
- Static checks: both inline JavaScript blocks parse; exactly one `diaryLanguageSelect` remains; the existing wrapper is moved rather than duplicated; welcome-screen hiding and Me-menu display rules are present; original language key and change listener remain. Publisher commit and live feed confirm Web Update 225 publication; the workflow run ID/log was not separately surfaced by the available status lookup.
- APK remains `1.0.143` / versionCode `142`; SHA-256 `4eccf17f61389bbb112a1daf910eb88d11315c19c22efa2d9e71171115688961`. No APK rebuild or signing change.
- Physical Android verification is **pending**. User should open **My Diary → Me**, confirm the Language / Zaban selector is inside Me and absent from the welcome screen, change among languages, and confirm the Diary labels and Urdu/Arabic direction update. Do not claim phone-side success until the user confirms.
- Rollback: restore the exact pre-change source/feed/register copies from `backup/before-move-language-selector-into-me-2026-11-15`; if already published, restore the source and publish a higher webVersion. Preserve all local notes, photos and PIN/recovery data.

---

# Note Cover Photo and full-text sharing repair — Web Update 220 (2026-11-15)

- User request: fix three Note Share problems: text placed over **Note ka Cover Photo** shifts from its editor position; long note text is cut off after a line / shown with `...`; and no-photo text-share artwork appears black/dark.
- Starting authoritative state: Web Update 219; APK `1.0.143` / versionCode `142`; package `com.personal.diaryapp`; starting source/mirror blob `25da0ffcef9e263bbdbb10cd419e1d5154f3bbaf`; starting feed web SHA-256 `7ae94bf68546bb77c7b65fa738f82f6138ad0800bacbd531a830490b3991a57e`.
- Scope: web-only change to `web-source/index.html`, inside the existing `shareNote()` canvas composition helpers. Corrected missing editor-style fallback metrics when sharing from the saved-note card (including width, direction, alignment, font, line height, padding, text indent and letter spacing); matched the canvas text line-box offset; calculated Cover and Details panel heights from the actual saved formatting and wrapped content; removed the line-count truncation and appended ellipsis; changed no-photo panels to a light background without the dark photo overlay. Photo panels retain their dark readability overlay.
- Explicitly untouched: saved note/photo data, storage keys and formats, PIN/recovery, note editing and saving, image selection/finger adjustment, unrelated Diary features, updater logic, Android source, APK, package identity and signing data.
- Pre-edit backup branch: `backup/before-note-cover-photo-share-fix-2026-11-15`. All four files were re-fetched and compared exactly with the starting live files:
  - `backups/web-source-before-note-cover-photo-share-fix-2026-11-15.html` (blob `25da0ffcef9e263bbdbb10cd419e1d5154f3bbaf`)
  - `backups/diary-web-before-note-cover-photo-share-fix-2026-11-15.html` (same blob)
  - `backups/latest-before-note-cover-photo-share-fix-2026-11-15.json`
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-note-cover-photo-share-fix-2026-11-15.md`
- Feature branch: `feature/note-cover-photo-share-fix-2026-11-15`; PR #30 merged successfully as `93922f29e9703eb29eeb1b4ad8ec95e21e8c2079`. PR diff contains exactly one changed file, `web-source/index.html` (34 additions, 20 deletions). No storage/data/PIN code was changed.
- Checks: both inline JavaScript blocks parsed successfully; targeted checks confirmed a non-empty style fallback, dynamic panel sizing, no text truncation/ellipsis cap, preserved typed spaces/newlines, and dark overlay applied only to photo panels. Final source and `diary-web/index.html` mirror were re-fetched and are byte-identical; both blob SHA `d53c8f4ebbab33ebd73db732824ef928b9845ffb` (373,250 characters).
- Web Update 220 published through the configured publisher path; publisher bot commit `1025107c149cb52866a89497713cf395ee6e413c` updated the mirror and feed. Live `latest.json`: `webVersion=220`; `webSha256=fbd78a8999898fbfc9f53e728d53ee30f8095a790e6abf508c24eba93db3366d`. Independently computed UTF-8 SHA-256 from the exact re-fetched source bytes matches the feed. The workflow-run/status endpoint did not expose the publisher run details in this session; do not claim its run log was inspected.
- APK unchanged: `1.0.143` / versionCode `142`; package `com.personal.diaryapp`; APK SHA-256 `4eccf17f61389bbb112a1daf910eb88d11315c19c22efa2d9e71171115688961`. No APK rebuild or signing operation.
- Physical-device verification is **pending**. User should use **My Diary → Me → Check for Updates**, install Web Update 220, then share a note with a Cover Photo and long text; verify the text stays in place, the entire writing appears without `...`, and a no-photo text share is readable. Do not claim phone-side success until the user confirms.
- Rollback: exact pre-edit source, mirror, feed and register files on `backup/before-note-cover-photo-share-fix-2026-11-15`. Preserve all local notes, photos and PIN/recovery data.

---

# Restore original colour controls — Custom buttons removed (2026-11-15)

- User request: remove all work specifically introducing or styling Custom / Custom Colour buttons and restore the earlier controls.
- Starting live state: Web Update 218; APK 1.0.143 / versionCode 142; package `com.personal.diaryapp`.
- Backup branch: `backup/before-remove-custom-colour-buttons-2026-11-15`; all four backup files were created and re-fetched successfully.
- Web-only files changed: `web-source/index.html` and identical mirror `diary-web/index.html`. Removed the added Text Colour “Custom” button and its styling; restored the visible native Text Colour input. Restored Cover/Detail image-design picker label to the original Solid Colour label and removed the Custom Colour button styling/class. Existing colour-picker inputs and colour application handlers remain.
- Explicitly untouched: Interface Colours and Diary Theme custom-colour controls; photo/gradient/template choices; note/photo storage; PIN/recovery; updater logic; native Android source, APK, package identity and signing data.
- Targeted checks: custom-button code references absent; native Text Colour input visible; original Solid Colour label restored; Cover and Detail shared formatting controls remain.
- PR #29 merged successfully as `3e67d5b2bcb875cf1b99d649b28b3aa222d3b865`.
- Live source/mirror blob SHA: `25da0ffcef9e263bbdbb10cd419e1d5154f3bbaf`; source and mirror are byte-identical: true.
- Live feed: webVersion `219`; web SHA-256 `7ae94bf68546bb77c7b65fa738f82f6138ad0800bacbd531a830490b3991a57e`. Independently computed UTF-8 SHA-256 from the exact source text: `7ae94bf68546bb77c7b65fa738f82f6138ad0800bacbd531a830490b3991a57e`; it matches the feed.
- APK remains `1.0.143` / versionCode `142`; no APK rebuild or signing change. Publisher workflow status was not available through the current run lookup; direct source/mirror/feed verification completed.
- Physical-device verification pending. User should use **Me → Check for Updates**, install Web Update 219, then confirm Cover and Detail show the old Solid Colour control and both Text Colour toolbars show the original colour swatch. Do not claim phone-side success until confirmed.
- Rollback: exact pre-change files on `backup/before-remove-custom-colour-buttons-2026-11-15`.

---

# Text Colour “Custom” button — published as Web Update 218 (2026-11-15)

- User request: in the existing Text Colour control inside both note-formatting toolbars (Cover/name and Details/text), replace the tiny native colour swatch control with a clearly visible **Custom** button in the same position. Tapping the button should open the existing native colour picker so the user can choose a custom text colour. Do not change any other item named Custom, including Cover/Detail image-design options, Interface Colours, or Diary Theme.
- Starting authoritative state: Web Update 217; APK 1.0.143 / versionCode 142; package `com.personal.diaryapp`; source and mirror blob SHA `1d88a1847e29f807554a2d68679346621c1978ae`; live feed blob `2f6a4d737d6518a1baa707e757fda80b7c1e2419`; starting web SHA-256 `ea90562b2af4c1703f670febd07ebba3831e0a01cae6aff929a1c1e8e7bf519c`.
- Scope: web-only, `web-source/index.html`. In `makeDiaryTextFormatControls()`, added one visible **Custom** button in place of the visible native colour swatch; kept the original `input[type=color]` in the DOM but visually hidden and programmatically available to the button handler. The button calls `showPicker()` when available and falls back to `click()`. The original colour input `input` handler remains responsible for updating the selected formatting state and applying the colour. Both Cover and Details use the same shared function, so both receive the button.
- Explicitly untouched: Cover/Detail image-design Custom Colour controls, Photo/Gradient options, Interface Colours, Diary Theme, preset palettes, font size/family, B/I/U, notes/photos, storage keys/data, PIN/recovery, updater logic, native Android source, APK, package identity and signing data.
- Pre-edit backup branch: `backup/before-text-colour-custom-button-2026-11-15`. Verified readable, exact backups:
  - `backups/web-source-before-text-colour-custom-button-2026-11-15.html`
  - `backups/diary-web-before-text-colour-custom-button-2026-11-15.html`
  - `backups/latest-before-text-colour-custom-button-2026-11-15.json`
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-text-colour-custom-button-2026-11-15.md`
  Both backup HTML files have blob SHA `1d88a1847e29f807554a2d68679346621c1978ae`; backup files were re-fetched and verified readable.
- Feature branch: `feature/text-colour-custom-button-2026-11-15`. PR #28 merged successfully as `0b8551ca4007abc411f1fe304c8c7d60e7778f1a`. Reviewed source diff: only the Text Colour toolbar CSS and `makeDiaryTextFormatControls()` declaration/append/click handler changed. The existing input `input` event handler and reset/load selectors querying `input[type=color]` remain unchanged.
- Publisher workflow run `43634354707`, job `132567766617`, completed with **success**; every listed job step completed successfully. Publisher commit: `573780027df618109769162ef74662d7b660580f`.
- Post-publish verification: live source and `diary-web/index.html` mirror are byte-identical; both blob SHA `5341263f65526888587c18685a344d7a979b5887`. Independently calculated UTF-8 SHA-256 `0d1a4458326adf11568b4795ee565752d43f849a539dc0f72feb12a3abb86f34` matches live `latest.json.webSha256`. Live `webVersion=218`. The publisher workflow also independently calculated and printed the same SHA-256 from the source bytes.
- APK unchanged: `1.0.143` / versionCode `142`; package `com.personal.diaryapp`; APK SHA-256 `4eccf17f61389bbb112a1daf910eb88d11315c19c22efa2d9e71171115688961`. No APK rebuild or signing operation.
- Static targeted checks passed: the visible button is created once per shared toolbar; the click handler opens the existing native picker via `showPicker()` with `click()` fallback; the original colour update handler remains; both Cover and Details still use the shared toolbar function. Physical-device verification is **pending**. User should open **My Diary → Me → Check for Updates**, install Web Update 218, then confirm that both Text Colour toolbars show the **Custom** button, tapping it opens the colour picker, and the selected colour applies independently to the relevant text. Do not claim phone-side success until confirmed.
- Rollback: restore only `web-source/index.html` from the verified backup branch above and publish a higher webVersion if needed. Preserve all local notes, photos and PIN/recovery data.

---

 (READ FIRST EVERY TASK)

**Status checked against live `latest.json` on 2026-11-15:** APK `1.0.143` / versionCode `142`; webVersion `217`; package `com.personal.diaryapp`. Live APK SHA-256 `4eccf17f61389bbb112a1daf910eb88d11315c19c22efa2d9e71171115688961`; web SHA-256 `ea90562b2af4c1703f670febd07ebba3831e0a01cae6aff929a1c1e8e7bf519c`.

**Project/repository:** `amuazzinxyz-ops/My-Diary-Updates`  
**This register:** `docs/PROJECT_MAP_AND_SECRETS_REGISTER.md`  
**Scope:** My Diary only. Never edit or inspect the separate MUAZZIN project for a My Diary task.

## A. Mandatory start gate — do not edit until complete

1. Read this register from the live default branch, including the newest entries and relevant historical notes.
2. Fetch the live `latest.json`; record APK version/versionCode, webVersion, APK URL and hashes. Do not rely on stale version numbers elsewhere in this document.
3. Inspect the current repository tree, recent commits, workflow status and the exact files/functions involved. Identify the latest successful/known-good state for the requested feature. If the live files, register, feed, or history disagree, STOP and reconcile before editing.
4. Confirm whether the request is web-only, native Android, build/workflow, or mixed. Do not change the wrong layer.
5. Write a short scope list: files/functions allowed to change, related dependencies to inspect, and features/files explicitly out of scope.
6. Create a timestamped backup of every file that will be edited, plus the live feed and this register when applicable. Verify the backup exists and is readable before editing. Never overwrite the only known-good backup.

## B. Change rules — preserve existing behaviour

1. Make only the user's explicitly requested change. Prefer the smallest isolated patch; do not refactor, redesign, rename, reorder, or clean up unrelated code.
2. Do not delete, replace, disable, or materially alter an existing feature, button, menu, updater path, data format, storage key, permission, package identity, signing identity, or recovery flow without explicit user approval.
3. Treat shared functions, global CSS, common event handlers, translations, storage and update code as high-impact dependencies. Inspect their callers and effects before changing them.
4. Preserve backward compatibility with existing notes, photos, backups, PIN/recovery records and stored user data. Never clear app data, uninstall the app, or change storage keys as a troubleshooting shortcut.
5. Do not bundle unrelated fixes into one release. If a new request reveals a separate issue, record it and ask/handle it as a separate task.
6. If a test fails or an unexpected difference appears, stop. Do not stack another speculative fix on top. Compare with the backup, isolate the cause, and restore the last known-good state when needed.

## C. Required verification before any publish

1. Review the complete diff against the pre-edit backup. Every changed line must be explainable by the user's request.
2. Run applicable checks: syntax/parse checks, HTML structure checks, targeted function checks, translation checks, data/storage compatibility checks, and automated tests/builds. Also inspect nearby features that share the changed code.
3. For web releases, fetch the final source and published mirror again and prove they are byte-identical. Independently calculate SHA-256 from the exact UTF-8 source bytes and verify it equals `latest.json.webSha256`. Do not copy a guessed or previously used hash.
4. For APK releases, verify debug and signed Release builds, package name, versionName/versionCode, APK SHA-256, live feed URL/hash, and the existing trusted signing-certificate fingerprint. Never regenerate, replace, expose, or modify signing secrets to make a build pass.
5. Verify the update workflow completed successfully and the feed points to the exact artifact that was checked. A queued, failed, cancelled, or partially completed workflow is NOT a published release.
6. Re-fetch every changed live file after writing. Confirm the expected commit/blob SHA, source/mirror/feed consistency, version metadata and backup paths.
7. Do not publish if any required check is missing, contradictory, or failing. Fix the cause or roll back first.

## D. Phone verification — report honestly

1. Automated checks and GitHub success do not prove that the app works on the user's phone.
2. Provide a short, relevant phone test list using the existing in-app route (normally **Me → Check for Updates**). Do not send the user to manual APK links when the in-app updater is the intended route.
3. Clearly separate: **code checked**, **build/workflow checked**, **live release checked**, and **physical-device test pending/confirmed**.
4. Never say “all fixed”, “100% working”, or “phone tested” unless the corresponding evidence exists. Record the user's actual phone-test result in the next register entry.

## E. Rollback and recovery

1. Keep the pre-change backup and last known-good commit/reference. Record exact paths and commit IDs.
2. If the update breaks an existing feature, stop further changes and compare the live code with the pre-change snapshot. Restore only the affected files from the verified last-known-good state; do not roll back unrelated good work.
3. After rollback, re-check source/mirror/feed/hash/version and test the recovery path. Do not claim recovery until verified.
4. Never delete backups, historical register entries, or signing records as part of routine cleanup.

## F. Register and release record

**MANDATORY SUCCESS-ENTRY RULE:** Whenever any requested work is completed successfully, immediately append a dated entry to this Master Register before reporting the work as complete. This applies to every successful task—not only published releases—including small UI fixes, code changes, translations, investigations that resolve an issue, configuration changes, and confirmed user/device test results. Record what was requested, what was actually completed, the evidence/checks, exact files or areas changed (or explicitly state no files changed), what was left untouched, and any pending limitations. If a task is not successful or remains incomplete, record its status honestly as pending/blocked/failed where useful; never write an unverified success claim. Do not rely on chat history as a substitute for the Register entry.

For every task, append a dated entry containing: user request; starting commit/version; exact files changed; exact behaviour changed; files/features deliberately untouched; backup paths; tests and results; workflow/run and commit IDs; source/mirror blob identity; independently verified SHA-256; feed values; APK/signing checks if applicable; rollback reference; and phone-test status. Mark unknown or untested items as **pending**, never as passed.

Keep historical entries as history. If an old entry contains stale version information, do not silently rewrite history; clearly identify the current live values near the top and state that `latest.json` is authoritative.

## G. Reusable task checklist — complete every time

- [ ] Correct project and repository confirmed (My Diary only)
- [ ] Master Register and live latest.json read
- [ ] Latest known-good commit/version identified
- [ ] Scope and dependencies inspected
- [ ] Pre-edit backups created and verified
- [ ] Only requested minimal change made
- [ ] Full diff reviewed; unrelated features preserved
- [ ] Relevant regression/syntax/data/build checks passed
- [ ] Source and mirror byte-identical (web change)
- [ ] Exact SHA-256 matches live feed (web change)
- [ ] APK version/hash/signing fingerprint verified (APK change)
- [ ] Workflow completed successfully
- [ ] Changed files re-fetched and live metadata verified
- [ ] **Successful work has a dated Master Register entry before completion is reported**
- [ ] Register updated with evidence and backup paths
- [ ] Phone-test status clearly marked; no unsupported success claim

**STOP RULE:** If any item required for the type of release cannot be verified, do not publish and do not describe the task as complete. Tell the user exactly what is blocked and preserve the last known-good version.


---



# Web Update 217 — Make Custom Colour a clearly visible tappable button (2026-11-15)

- User reported that the Cover and Detail control showed only the “🎨 Custom Colour” name and did not look like a proper tappable button. Requested a real visible button, while all other features remained correct.
- Starting live state: Web Update 216; APK 1.0.143 / versionCode 142; package `com.personal.diaryapp`; source/mirror blob SHA `102531d7e44feccfb9283cba87ca835ac1e9a663`; live feed web SHA-256 `cf54d5f058ca3175ba1a2eec6265f852b3c70fe09e959e26ddd3a04b1b94fff5`.
- Changed only the existing CSS rule in `web-source/index.html` for `.diary-image-choice-actions-custom .diary-image-choice-solid`: made the existing button explicitly display as a centered flex control, full width, minimum height 46px, with gold border, gold gradient fill, raised 3D shadow, bold centered label and pointer cursor. The existing HTML button element, label, and click handler are unchanged; the colour picker still opens through its original handler.
- Cover and Detail only. Photo chooser, gradient controls, image selection, note data, photos, local storage, PIN/recovery, updater logic, native Android source, APK, package identity and signing data were not changed.
- Pre-edit backup branch: `backup/before-custom-colour-button-style-2026-11-15`. Verified readable exact backups:
  - `backups/web-source-before-custom-colour-button-style-2026-11-15.html`
  - `backups/latest-before-custom-colour-button-style-2026-11-15.json`
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-custom-colour-button-style-2026-11-15.md`
- Source change PR #27 merged; merge commit `afe9d380f4a65bdecb32b916af3fbd6fd31ba50f`. Web-only workflow run `43632692522`, job `132562572265`, completed with **success**. Publisher commit `36cc17b` (“Publish My Diary web bundle update”).
- Post-publish verification: source and mirror are byte-identical; both Git blob SHA `1d88a1847e29f807554a2d68679346621c1978ae`. Publisher independently calculated UTF-8 SHA-256 `ea90562b2af4c1703f670febd07ebba3831e0a01cae6aff929a1c1e8e7bf519c`, matching live `latest.json.webSha256`. Live `webVersion=217`. CSS brace counts and style-tag counts are balanced; targeted source check confirms the explicit full-width button rule is present. No JavaScript or HTML structure was changed by this CSS-only patch.
- APK unchanged: 1.0.143 / versionCode 142 / SHA-256 `4eccf17f61389bbb112a1daf910eb88d11315c19c22efa2d9e71171115688961`; no APK rebuild or signing changes.
- Physical-device verification is **pending**. User should use **Me → Check for Updates**, install Web Update 217, then confirm that Cover and Detail both show a full-width raised gold **🎨 Custom Colour** button and tapping anywhere on the button opens the colour picker. Photo and Gradient should remain unchanged. Do not claim phone-side success until confirmed.
- Rollback: exact pre-edit files on `backup/before-custom-colour-button-style-2026-11-15`; preserve all diary data and settings.

---

# Web Update 215 — Restore Diary main page after Update 214 script break (2026-11-15)

- User reported that the Diary main page had disappeared after Update 214.
- Root cause confirmed by direct source comparison: the Update 214 CSS block `diary-custom-colour-button-full-label` had been inserted into the JavaScript-generated report HTML string, immediately after `<p>Loading…</p>`, instead of in the document head. The inserted raw newline/style markup broke the JavaScript source. Removing only that inserted block did not recreate the original; exact recovery used the verified pre-Update-214 backup.
- Starting live state: Web Update 214; APK 1.0.143 / versionCode 142; package `com.personal.diaryapp`; broken source/mirror blob SHA `0e12683dc6e027a310e73a49100517fabbafaf93`; feed web SHA-256 `3aece64a96b3e288a247ca5c09353fc6321a5474238c2c0568094b392fead0c4`.
- Restored `web-source/index.html` byte-for-byte from the verified Web Update 213 backup on branch `backup/custom-colour-button-width-2026-11-15`, file `backups/web-source-before-custom-colour-button-width-2026-11-15.html`. Restored `diary-web/index.html` to the same exact content. No other feature logic, storage keys, notes, photos, PIN/recovery, updater code, native Android source, APK, package identity or signing data was changed.
- Before restore, backed up the broken live source, live feed and this register on branch `backup/before-main-page-restore-2026-11-15`:
  - `backups/web-source-before-main-page-restore-2026-11-15.html` (source blob `0e12683dc6e027a310e73a49100517fabbafaf93`)
  - `backups/latest-before-main-page-restore-2026-11-15.json`
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-main-page-restore-2026-11-15.md`
- Restore PR #25 merged; merge commit `75df5d1e99d8e9092f49dd8541d131f4809cb8f4`. Restored source blob and mirror blob are both `34b1a0276f83a082949052fd0fba4b0d6169075d`; source and mirror re-fetches are byte-identical. Main document markers `.diary-home` and `#diaryHomeEntryHost` are present; malformed CSS block is absent.
- Feed advanced to Web Update 215; `latest.json` re-fetched and reports webVersion `215`, web SHA-256 `ecaff11b09037db2330241b87873d932ec956a4cdff30d559b900a7803c90885`, and the restored source URL. This SHA-256 is the independently recorded publisher-verified hash for the exact Web Update 213 source bytes, now restored unchanged.
- APK unchanged: 1.0.143 / versionCode 142 / SHA-256 `4eccf17f61389bbb112a1daf910eb88d11315c19c22efa2d9e71171115688961`.
- Physical-device verification is pending. User should use **Me → Check for Updates**, install Web Update 215, then confirm the Diary main page opens. Do not claim phone-side recovery until confirmed.
- Rollback/reference: preserve broken-state backup branch `backup/before-main-page-restore-2026-11-15` and known-good Web Update 213 backup branch `backup/custom-colour-button-width-2026-11-15`.

# Web Update 213 — Label Cover and Detail colour picker buttons “Custom Colour” (2026-11-15)

- User request: show a clearly named **🎨 Custom Colour** button in both the Cover and Detail image-design menus, in the same position as the existing single-colour picker button.
- Starting live state: Web Update 212; APK 1.0.143 / versionCode 142; package `com.personal.diaryapp`; source/mirror blob SHA `113e4cf0cdeb145ff03949890f09996de0586d34`; live feed SHA-256 `34fe487da10d5103c1aeea8dbe0e0a8eb73621d99fd59019d134ac21768baae3`.
- Changed only `web-source/index.html`: the existing solid-colour button now displays **🎨 Custom Colour** when the chooser is for Cover or Detail. The button remains in the same location and keeps its existing native colour-picker behaviour. The separate Photo chooser retains its previous **Solid Colour** label. No picker logic, colour values, gradient controls, translations, stored note/photo data, storage keys, PIN/recovery, updater, native Android source, APK, package identity, or signing data changed.
- Pre-edit backup branch: `backup/before-custom-colour-button-label-2026-11-15`. Verified readable backups:
  - `backups/web-source-before-custom-colour-button-label-2026-11-15.html`
  - `backups/latest-before-custom-colour-button-label-2026-11-15.json`
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-custom-colour-button-label-2026-11-15.md`
- Source change PR #23 merged. Source commit: `6bbe65567f6ad69e0500585612ea1fee28564f30`. Publisher commit: `77f41be13b33bb2b4f1a98ba7a8e75220fbd2a9b`. Web-only workflow run `43627992184` completed with **success**; all job steps completed successfully.
- Post-publish verification: source and mirror are byte-identical; both Git blob SHA `34b1a0276f83a082949052fd0fba4b0d6169075d`. Publisher independently computed UTF-8 SHA-256 `ecaff11b09037db2330241b87873d932ec956a4cdff30d559b900a7803c90885`, printed in the successful workflow log, and it matches live `latest.json.webSha256`. Live `webVersion=213`; feed blob SHA `3fcf1855b2a267c36ba9c2f3f7f28ed9292877b1`. Both source and mirror contain the new label; Photo's original label remains unchanged.
- APK unchanged: 1.0.143 / versionCode 142 / SHA-256 `4eccf17f61389bbb112a1daf910eb88d11315c19c22efa2d9e71171115688961`; no APK rebuild or signing changes.
- Physical-device verification is **pending**. Use **Me → Check for Updates** and confirm the Cover and Detail menus both show **🎨 Custom Colour**, and the Photo menu still shows **Solid Colour**.
- Rollback: exact pre-edit files on `backup/before-custom-colour-button-label-2026-11-15`; preserve all diary data and settings.

# Web Update 153 — Independent adjustment for each image (2026-11-13)

- User reported that adjusting one image prevented another image from being adjusted. Root cause: shared `diaryFingerAdjustKind` gated all document-level Pointer/Touch handlers, so only the most recently activated image kind could receive gestures.
- Starting state: Web Update 152; APK 1.0.136 / versionCode 135; package `com.personal.diaryapp`; prior source/mirror blob SHA `4ea139d2ca9ee04b72a31b1a9cbc712a3d87ca41`; prior feed SHA-256 `b3916ea90ea9f46a633a6e11fb47e89540f9ba2a17db7e7993f9cb2529ccef84`.
- Changed only `web-source/index.html`, source commit `5b591b65deb262efc0fd988c3530ce60948a5efe`. Removed the global active-kind gate from pointer and touch gesture handlers; each bound image now accepts gestures only when the pointer is inside its own bounds / belongs to its own tracked pointer IDs. Starting adjustment no longer disables the previously selected image. Photo preview is always gesture-enabled when present. Clearing/resetting a note removes adjustment styling from all active image targets. Existing per-image colour/position/zoom state and zoom limits remain unchanged.
- Pre-edit backup branch: `backup/pre-independent-image-adjustment-2026-11-13`; verified exact readable backups:
  - `backups/web-source-before-independent-image-adjustment-2026-11-13.html`
  - `backups/diary-web-before-independent-image-adjustment-2026-11-13.html`
  - `backups/latest-before-independent-image-adjustment-2026-11-13.json`
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-independent-image-adjustment-2026-11-13.md`
- Diff contained only the shared gesture activation/gating and Photo preview active styling. Both inline JavaScript blocks parsed successfully. Targeted checks confirmed all four Pointer/Touch global-kind gates removed, independent per-target pointer tracking retained, and reset clears all active targets.
- Publisher output commit: `de42b4b796738149e0dfe7c0ffbdbcc38fb9ee9a` (“Publish My Diary web bundle update”). Feed advanced to Web Update 153. Live source and mirror are byte-identical; both blob SHA `aa9a115ce37c1e3cad115046f13dcf3f7f63a75e`. Live feed web SHA-256: `d43796f0c2e4998cbeda3bc1f16dfe7019c44076d9574e9ef5e0f64dbdf0b145`. Publisher commit updated `diary-web/index.html` and `latest.json` with matching source patch and release metadata.
- APK unchanged: 1.0.136 / versionCode 135 / SHA-256 `6fc74ca82888fed4121cc352c1846ec8c6a7063e2d2a33fbe032726f7a244348`; no APK rebuild or signing changes.
- Physical-device verification pending. Ask user to use **Me → Check for Updates**, then test adjustment separately on Cover, Detail and Photo, switching between them in both directions. Do not claim phone-side success until user confirms.
- Rollback: exact pre-edit files on `backup/pre-independent-image-adjustment-2026-11-13`; preserve all diary data and settings.


# Web Update 152 — Automatic finger adjustment after image selection (2026-11-13)

- User requested removal of the separate “Ungli se Adjust Karein” button and automatic image adjustment as soon as an image is selected.
- Starting live state: Web Update 151; APK 1.0.136 / versionCode 135; package `com.personal.diaryapp`; source/mirror blob SHA `99785ad58c1a0a03f0b90b5dc3bd5fe3de9b6077`; feed SHA-256 `4043dc99f56adba90e65d54869f711bc7f05d3c54c3974e1f17108d7be05bfc8`.
- Changed only `web-source/index.html` in source commit `acc35a9b44f44cacffe8ddf610c142ea2dfecea2`. Removed the manual adjustment button and hint from the Cover, Detail and Photo image-design menu. Added automatic adjustment activation after successful image selection for Cover, Detail and attached Photo. Existing pointer/touch gesture engine, one-finger drag, two-finger pinch, zoom range 0.8–4, rendering and saved position/zoom state remain in place. No other feature, translation values, storage/data keys, note/photo records, PIN/recovery, native Android source, APK, package identity or signing data changed.
- Pre-edit backup branch: `backup/pre-auto-finger-adjust-no-button-2026-11-13`. Verified readable exact backups:
  - `backups/web-source-before-auto-finger-adjust-no-button-2026-11-13.html`
  - `backups/diary-web-before-auto-finger-adjust-no-button-2026-11-13.html`
  - `backups/latest-before-auto-finger-adjust-no-button-2026-11-13.json`
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-auto-finger-adjust-no-button-2026-11-13.md`
- Source diff reviewed; only the requested adjustment UI/activation logic changed. Both inline JavaScript blocks parsed successfully. No remaining `diary-finger-adjust-button` references in the updated source; the automatic activation function is called from all three image-selection handlers.
- Publisher output commit: `23fe1494f9f5efa4b2681feef048e08060195b2c` (GitHub Actions bot, “Publish My Diary web bundle update”). Live feed advanced to Web Update 152. Re-fetched source and mirror are byte-identical; both Git blob SHA `4ea139d2ca9ee04b72a31b1a9cbc712a3d87ca41`. Independently computed UTF-8 SHA-256 `b3916ea90ea9f46a633a6e11fb47e89540f9ba2a17db7e7993f9cb2529ccef84` matches live `latest.json.webSha256`. Source/mirror/feed checks passed. The workflow-run listing/status endpoint did not expose a run ID or conclusion in this session; publisher bot output commit and updated feed/mirror were verified.
- APK remains 1.0.136 / versionCode 135; APK SHA-256 remains `6fc74ca82888fed4121cc352c1846ec8c6a7063e2d2a33fbe032726f7a244348`. No APK rebuild or signing operation.
- Physical-device verification is **pending**. User should install Web Update 152 using the existing **Me → Check for Updates** path, then confirm image selection automatically enables drag and pinch zoom in Cover, Detail and Photo. Do not claim phone-side success until the user confirms.
- Rollback: use exact pre-edit files on `backup/pre-auto-finger-adjust-no-button-2026-11-13`; preserve notes, photos, PIN data and app data.


# Web Update 132 — Keep the Diary Me button label as “Me” in every language (2026-11-12)

- User request: restore the Me button to its previous literal label, “Me”, in every supported language; make no other changes.
- Starting live state: Web Update 131; APK 1.0.135 / versionCode 134; package `com.personal.diaryapp`. Source commit before this task: `ccf1cdc0d8e56f001b71f67676bab6017a1fa310`.
- Scope: web-only; changed only the nine non-English `words[language]["me"]` values (Roman English, Hindi, Urdu, Arabic, Bengali, Gujarati, Marathi, Tamil, Telugu) to the literal `Me`. English was already `Me`. All ten language dictionaries now return exactly `Me` for this button.
- No other translation keys, button labels, layouts, menus, feature logic, notes, photos, storage, PIN/recovery flows, native Android source, APK, package identity, or signing data were changed.
- Pre-edit backup branch: `backup/pre-me-button-label-all-languages-2026-11-12`. Readable verified backups on that branch:
  - `backups/web-source-before-me-button-label-all-languages-2026-11-12.html`
  - `backups/diary-web-before-me-button-label-all-languages-2026-11-12.html`
  - `backups/latest-before-me-button-label-all-languages-2026-11-12.json`
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-me-button-label-all-languages-2026-11-12.md`
- Exact source change commit: `0ca75c82322828981b509952baebf78d53ba7788`; publisher commit: `e638557b24da1a8f5ae0b4b44c45e4266662260c`. Web-only workflow run `43269118234` completed with **success**.
- Post-publish verification: `web-source/index.html` and `diary-web/index.html` are byte-identical; both Git blob SHA `9f654af4acfd0e24e48268214cfd0fc9068b7774`. Independently computed UTF-8 SHA-256 `ef03b5fc97252aa133b46339ef6bff59add404283584f96091e2412d61ba6707` matches live `latest.json.webSha256`; live `webVersion=132`.
- APK remains `1.0.135` / versionCode `134`; package `com.personal.diaryapp`; APK URL and SHA-256 remain unchanged (`c3e312ec7cd8504bab68c12f9df996c8d10018670d0d1ccef9373408d4ddba4d`). No APK rebuild or signing operation.
- Source diff review: exactly one file changed in the source commit, with 9 additions and 9 deletions; each line is one requested Me-label value.
- Automated language-value check: all ten language keys resolve to exactly `Me`. Workflow and source/mirror/feed checks passed. Physical-device verification remains **pending**; use the existing in-app **Me → Check for Updates** path and confirm the button says “Me” after update.
- Rollback: use the verified backup branch and the exact pre-edit backup files above; preserve the existing last-known-good state.



---

# Web Update 113 — Note Lock Forgot PIN uses Diary-style in-app dialogs (2026-11-12)

- User reported that the Android WebView page address still appeared during Note Lock → Forgot PIN. Re-inspection found remaining native `window.alert()` calls in the Note Lock recovery path, including Copy PIN failure and PIN/storage/crypto error branches; Web Update 112 covered only the wrong temporary-PIN message.
- Updated the Note Lock Forgot PIN path and its new-PIN creation/confirmation path to use the same custom in-app message popup as Diary Lock. The temporary PIN popup, custom four-digit input, wrong-PIN retry, PIN hashing/storage sequence, and new PIN creation flow remain intact.
- Backups: `backups/web112-before-note-forgot-pin-inapp-dialogs-2026-11-12.html`, `backups/diary-web112-before-note-forgot-pin-inapp-dialogs-2026-11-12.html`, `backups/latest-before-web113-note-forgot-pin-inapp-dialogs-2026-11-12.json`, and `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-web113-note-forgot-pin-inapp-dialogs-2026-11-12.md`.
- Web Update 113 SHA-256: `dcbcfce3eeb54d17ac6766dcb703d46e994cbbdc8acea36e6881f8931caea27d`. Source and mirror were written from the same exact HTML content. APK remains 1.0.135; no APK rebuild or app-data change.
- Static verification: no native `window.alert()` / `window.prompt()` remains in the Note Lock Forgot PIN and new-PIN confirmation paths. Physical-device verification is pending; use Me → Check for Updates and test Copy PIN, wrong temporary PIN, and PIN mismatch.

---

# Web Update 112 — In-app Note Lock wrong PIN message (2026-11-12)

- Replaced the native WebView `window.alert` for a wrong temporary PIN in Note Lock → Forgot PIN with a custom in-app message popup.
- The popup shows only the localized Diary message **“Diary PIN galat hai.”** and a close button; the Android page-address heading is no longer shown for this error.
- Closing the message retries the temporary PIN prompt. PIN comparison and recovery logic are unchanged.
- Backup: `backups/web111-before-custom-note-pin-error-2026-11-12.html`
- Feed backup: `backups/latest-before-web112-custom-note-pin-error-2026-11-12.json`
- Master Register backup: `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-web112-custom-note-pin-error-2026-11-12.md`
- Source SHA-256: `28b0fca7bd482c728827bd4b47073adeb3d4a2387de8f6e42db14543dbf89e3a`; source/mirror sync is being verified.
- Web Update 112 only; APK remains `1.0.135` and is not rebuilt. Device-side test pending.

---

# Web Update 111 — Note Lock wrong temporary PIN message (2026-11-12)

- User-requested wording only: when the temporary PIN entered during Note Lock → Forgot PIN is wrong, the message now uses the existing Diary Lock wording: **“Diary PIN galat hai.”**
- Implemented only in the temporary-PIN verification branch by calling the existing `diaryPinWrong` message. The separate legacy recovery-code error text remains unchanged.
- The retry flow, temporary PIN generation, PIN verification, stored lock data, new PIN creation/confirmation, notes, photos, Diary Lock, APK and unrelated features were not changed.
- Backup before change: `backups/web110-before-note-forgot-pin-error-wording-2026-11-12.html`
- Update-feed backup: `backups/latest-before-web111-note-pin-error-2026-11-12.json`
- Master Register backup: `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-web111-note-pin-error-2026-11-12.md`
- Source and mirror were verified byte-identical; SHA-256: `bbb84e19d76f69333ad7e95b8fa6cf5bbd279264f6fba0e47349bd19910fa317`.
- Web Update 111 published in `latest.json`; APK version and APK URL remain unchanged.
- Device-side verification is still pending; user should use **Me → Check for Updates** and test a deliberately wrong temporary PIN.

---

# Web Update 110 — exact UTF-8 SHA-256 correction (2026-11-12)

- User reported that Check for Updates failed with “Diary update SHA-256 match nahi hua”.
- Root cause confirmed: `latest.json` contained an incorrect `webSha256` value (`fa4d6f6a66b835542cd56bcc5246f954b5d41ae33a73a072c323db708512df7f`) for the current `web-source/index.html` bytes.
- Backed up the live feed to `backups/latest-before-web110-sha256-correction-2026-11-12.json` and backed up this register before editing.
- Recomputed SHA-256 over the exact UTF-8 HTML bytes using a SHA-256 implementation verified against the standard `abc` test vector. Correct digest: `163f14796d8a84867ad68e17833991e01bbf4f0d1baa5c1f4696c2362805bf78`.
- Updated only `latest.json` metadata: `webVersion=110`, corrected `webSha256`, and checksum-repair release note. The HTML source, published mirror, APK URL/hash/version, package identity, signing identity, notes/photos/PIN storage, and all app features were not changed.
- Re-fetched the source, mirror, and feed after publishing. Source and mirror are byte-identical and have matching Git blob SHA `3c53a0c8af11d0341d8a9839be3bd12ae5b54ca2`; the independently recalculated source SHA-256 exactly matches the live feed.
- This is a metadata-only web update. Device-side Check for Updates success still requires the user's test; do not claim phone-side verification.

---

# My Diary recovery — restore last-known-good 11:00 AM state (2026-11-12)

- User reported that My Diary worked correctly until approximately 11:00 AM IST on 2026-11-12 and became unstable after later changes.
- Read the Master Register and inspected the live repository history. The last coherent web state at the requested cutoff is **Web Update 98**, recorded at approximately 10:54 AM IST. Subsequent changes altered Note Lock Forgot PIN recovery (manual recovery-PIN verification was replaced by a Copy PIN flow, then repeatedly changed/restored), and later web updates 101–104 plus repeated checksum corrections.
- Created a full pre-repair Git backup branch: `backup/pre-web98-restore-2026-11-12` from pre-repair main head `e90785349d0f9e906798cfd05dd329c1b4edc324`.
- Restored `web-source/index.html` byte-for-byte from the Web Update 98 snapshot at commit `1ace3bd50656ac2e55640e8f198d3f3880e66814`; synchronized `diary-web/index.html` to the same content. Restored source and mirror Git blob SHA: `af8e3bc167b6f3410569663831f7aded9727319d` (225,579 characters each).
- Published **Web Update 105** in `latest.json`, retaining APK identity/version **1.0.135 / versionCode 134**, package `com.personal.diaryapp`, APK URL and APK SHA-256 unchanged. The Web 98 checksum was restored from the matching Web 98 feed: `4545038ad06640840613940e67645eb66b1dc2e655185a53665b8cf4e23843c7`.
- This is a web-content rollback/recovery only. No user data, notes, photos, local storage, PIN/recovery records, package identity, keystore secrets, or signing identity were changed. No new APK was built because the existing 1.0.135 updater can deliver the restored web bundle through **Me → Check for Updates**; do not uninstall or clear data.
- Device-side update and feature behavior still require the user's Check for Updates test. This register entry supersedes the older stale Web Update 85 / APK 1.0.131 note below.

---

# SHA-256 update-feed repair — 2026-11-12

- User again reported the installed app's web-update error: `Diary update SHA-256 match nahi hua`.
- Re-inspected the actual Android updater path. This message is raised only when the downloaded HTML bundle's bytes do not match `latest.json.webSha256`; the APK downloader uses a different error message.
- Verified the signed APK build artifact from workflow run **43089651168** independently: SHA-256 `04a9863ff35f13ca2beccecceaffc49c2e41d6bb8e72bac1df4d4501238b04a2`, matching the APK hash already in `latest.json`. No APK rebuild or APK metadata change was needed.
- Created pre-repair backups:
  - `backups/web-source-index-before-sha-publish-repair-2026-11-12.html`
  - `backups/diary-web-index-before-sha-publish-repair-2026-11-12.html`
  - `backups/latest-before-sha-publish-repair-2026-11-12.json`
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-sha-publish-repair-2026-11-12.md`
- Re-published the exact same Diary HTML with only a non-visible HTML comment added to trigger a fresh release record. No interface, layout, button, feature, or app logic changed.
- Synchronized `diary-web/index.html` byte-for-byte with `web-source/index.html`; both now have Git blob SHA `a211e05028c20bd029c7d00560c9a558576a084e`.
- Independently computed UTF-8 SHA-256 for the exact current HTML and checked the implementation against the standard SHA-256 test vector `abc`. Current HTML SHA-256: `9085dade0a1a84ec2938488e434d89cf825b00d266f2da9542b9db5992775697`.
- Updated `latest.json` to **Web Update 85** with that exact `webSha256`. Re-fetched all three files after commits and verified source/mirror blob SHAs match and feed checksum equals the independently calculated HTML checksum.
- APK remains **1.0.131 / versionCode 130**; signed APK checksum, package name, and signing identity were not changed. Notes, photos, PIN/recovery data and app data were not touched.
- GitHub Actions web-publisher run **43095216483** was triggered by the source change but remained queued during this repair; direct source/mirror/feed synchronization and hash verification were completed independently. Device-side download/install still requires the user's Check for Updates test.

---

# Latest correction — Camera/status-bar background made transparent (2026-11-11)

- User asked to remove the separate background strip above the phone's front camera while keeping the Diary title and content below the camera/status icons.
- Retrieved the exact original Android source from the successful 1.0.126 build artifact; no ZIP upload from the user was needed.
- Updated only the native status-bar setup generated by `scripts/add_diary_app_actions.py`: transparent status bar, edge-to-edge layout behind the system bar, and dark status icons. The current published Diary HTML already includes `viewport-fit=cover` and `env(safe-area-inset-top)` top padding, so the page background extends behind the status bar while the welcome panel stays below the camera/status icons.
- Kept the Diary HTML, panel border/design, buttons, data storage, notes/photos/PIN, package name, and signing identity unchanged.
- Prepared APK **1.0.127 / versionCode 126**, based on installed **1.0.126 / versionCode 125**. Workflow release guard and APK filename/feed update were advanced together. Publish only if debug and signed Release builds, certificate fingerprint, APK checksum, and feed checks all pass.
- Phone appearance remains unverified until the user installs the update through **Me → Check for Updates**.

## APK publish guard alignment — 2026-11-11

- Debug APK and signed Release APK build succeeded in run 43050047044; existing signing certificate fingerprint matched.
- The final publish step correctly refused to publish because a second stale baseline check still expected 1.0.124/123, while the live feed is 1.0.125/124. Updated that final guard to the actual installed baseline. No APK or live feed was changed by the blocked publish.
- This workflow-only correction triggers a fresh signed build. Publish only if all checks pass.

## Backup Save As build correction 2 — 2026-11-11

- Second APK workflow attempt 43049587648 passed source checks and the native patch script, then Kotlin compilation found a duplicate `android.app.Activity` import because the original Android project already imports Activity.
- Removed only the redundant import insertion. The existing Activity import is retained and used by the Save As result handler. No app feature or data change.
- A fresh APK build is triggered by this commit. Publish only after debug and signed Release builds, signing fingerprint, APK checksum and feed all pass.

## Backup Save As build correction — 2026-11-11

- First APK workflow attempt 43049271326 stopped in the patch script before compilation. The exact failure was a generated Python string searching for a literal backslash-n instead of the MainActivity closing-line newline.
- Corrected the generator's class-end search and insertion newline. The Activity-level Save As result handler remains outside the inner JavaScript bridge class, as required.
- The next push triggers a fresh full build; do not publish or install until it passes all source, debug, signed Release, certificate, checksum and feed checks.

# Latest correction — Android Backup opens Save As and confirms only after saving (2026-11-11)

- Backup button root cause: export used a hidden download anchor and displayed success immediately without letting Android choose a folder or filename.
- Web export now calls the Android native bridge in the installed app; regular browser download fallback remains.
- Android bridge uses ACTION_CREATE_DOCUMENT with suggested filename `Diary-My-Notes-Backup.json`. User can choose folder and change filename. JSON is written to selected URI. Success is shown only after stream write completes; cancel/failure clears success status.
- Existing backup JSON structure, restore, notes/photos/PIN data, local storage, styling and app identity are preserved.
- Pre-edit backups stored at `backups/*-before-native-backup-save-dialog-2026-11-11.bak` for edited files.
- Prepared next APK **1.0.126 / versionCode 125**, based on installed **1.0.125 / versionCode 124**. Web Update 79. Workflow builds from tracked Android project ZIP, applies updated native bridge script, and verifies signing identity before publishing.
- Device-side Save As flow remains unverified until installed and tested on Android.

# Latest correction — Inner Diary panel moved down a further 2px (2026-11-11)

- User asked for a very small additional downward adjustment after Web Update 77.
- Inspected the current project register, main web source, published mirror, and update feed. Source and mirror matched before editing; Web Update 77 had the panel at 6px down.
- Changed only the opened inner Diary panel offset from 6px to 8px total using a later, narrowly scoped CSS override. No other layout, controls, features, APK, or user data changed.
- Backups created before editing: `backups/web-source-index-before-inner-diary-downshift-8px-2026-11-11.html`, `backups/diary-web-index-before-inner-diary-downshift-8px-2026-11-11.html`, `backups/latest-before-inner-diary-downshift-8px-2026-11-11.json`, `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-inner-diary-downshift-8px-2026-11-11.md`.
- Published Web Update 78; HTML SHA-256: `98ce041e2b32c238072b23d73ba12a0f2652526e18031ccea3afa9e0dfdf7740`. APK remains 1.0.125 / versionCode 124; no APK rebuild.
- Source/mirror/feed/register will be checked after write. Actual phone appearance awaits user confirmation.

# Latest correction — Opened inner Diary panel moved slightly lower (2026-11-11)

- User asked for the Diary panel that opens inside the app to sit a little lower, matching the recent top-spacing adjustment.
- Inspected the current main web source and published mirror; they were byte-identical before editing. The opened Diary panel is centered inside `#diaryMyNotesOverlay` and already has its own 3D perspective transform.
- Narrow web-only CSS adjustment: added `position:relative; top:6px` to `#diaryMyNotesPanel`. This shifts only the opened inner Diary panel down by 6px while preserving its existing centering, perspective transform, purple outer border, camera safe-area spacing, and Diary behavior.
- Backups created before editing: `backups/web-source-index-before-inner-diary-downshift-2026-11-11.html`, `backups/diary-web-index-before-inner-diary-downshift-2026-11-11.html`, `backups/latest-before-inner-diary-downshift-2026-11-11.json`, and `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-inner-diary-downshift-2026-11-11.md`.
- Published Web Update 77; HTML SHA-256: `49904d23be30b44a0dbfb3714fe84fae907e361efb0b247bb26384e4da39cfba`. APK remains 1.0.125 / versionCode 124; no APK rebuild or app-data changes.
- Static source, mirror, and feed verification completed after publishing. Physical-phone appearance remains pending user confirmation.

# Latest correction — Diary header starts below the camera/status-bar safe area (2026-11-11)

- User clarified that the existing purple 3D border should begin below the phone's front-camera / status-bar area, not behind or beside notification icons.
- Inspected the current published HTML: it uses `viewport-fit=cover` but the page body had a fixed `14px` top padding and did not account for `env(safe-area-inset-top)`.
- Narrow web-only correction: body top padding now uses `calc(14px + env(safe-area-inset-top, 0px))`. This moves the existing Diary content and purple header border below the reported safe area while preserving the existing horizontal/bottom spacing, border design, buttons, and all Diary behaviour.
- Backups created before editing: `backups/web-source-index-before-camera-safe-area-spacing-2026-11-11.html`, `backups/diary-web-index-before-camera-safe-area-spacing-2026-11-11.html`, `backups/latest-before-camera-safe-area-spacing-2026-11-11.json`, and `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-camera-safe-area-spacing-2026-11-11.md`.
- Published Web Update 76; feed records HTML SHA-256 `69daf44646cbaa878b1626a43549b1b073be92457ec6805123be0dcc4110357f`. Source and mirror are byte-identical (Git blob SHA `3bfd3ae6418f008e704e850e048fec4ae0b15271`). APK remains 1.0.125 / versionCode 124; no APK rebuild, signing change, notes/photos/PIN changes, or unrelated feature changes.
- Static source/feed checks passed. Physical-phone appearance remains pending user confirmation after **Me → Check for Updates**.

# Latest correction — Android status bar no longer overlays the Diary page (2026-11-11)

- User showed that Android notification icons (for example Vi and WhatsApp) appeared over the top of the My Diary welcome screen because the native Activity enabled `SYSTEM_UI_FLAG_LAYOUT_STABLE`, allowing the WebView content to draw behind the transparent status bar.
- Updated `scripts/add_diary_app_actions.py` to remove that layout-behind-status-bar flag, set an opaque pale lavender status-bar background (`#FAF7FF`), and enable dark status-bar icons. The status bar now occupies its own area; time, network, battery, and notification icons remain visible, but no longer overlay the Diary content.
- Pre-edit backups: `backups/add_diary_app_actions-before-statusbar-separation-2026-11-11.py`, `backups/build-diary-from-zip-before-statusbar-separation-2026-11-11.yml`, and `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-statusbar-separation-2026-11-11.md`.
- Signed APK **1.0.124 / versionCode 123** built and published successfully by workflow run **43033906461**. Debug build, signed Release build, signing-certificate fingerprint verification, publish, and artifact upload all succeeded. Live `latest.json` now points to `My-Diary-1.0.124.apk` with SHA-256 `391f08f3cdd00cef316668b0cf2111a3fef6bebe0e82946fcb30ff92cb0a1ecb`. Web bundle remains Web Update **74**; its hash and content were not changed.
- No Diary HTML redesign, local notes/photos, PIN/recovery data, package identity, signing identity, or unrelated app features were changed. Physical-device appearance is pending user confirmation after installing 1.0.124 via **Me → Check for Updates**.

# MY DIARY — MASTER PROJECT REGISTER

**Single source of truth. Last updated: 2026-11-11 (published APK 1.0.122 / versionCode 121; Web Update 58).**

## Latest correction — Check for Updates starts APK download directly (2026-11-11)

- User requires the installed app's **Me → Check for Updates** control itself to carry out the update; do not substitute a manually supplied APK link.
- Root cause in the generated native updater: when a newer APK was found, the button opened an extra confirmation dialog with a separate **Download & Install** button. This interrupted the requested one-button update flow.
- Narrow repair in `scripts/add_diary_app_actions.py`: when the feed reports a newer APK, the existing button now immediately calls the existing `downloadAndInstall()` routine. That routine retains the progress display, retries, SHA-256 verification, package/version validation, and Android's system installer handoff. Android's own final install confirmation cannot be bypassed.
- Kept the second generator, `scripts/add_online_diary_updates.py`, compatible with the new branch. It now validates/preserves the direct APK-download branch while retaining the existing web-bundle update path when the installed APK is already current.
- When the installed APK is already current, the existing web-bundle hash-check/update path remains in place. Notes, photos, PIN/recovery data, package identity, signing identity, UI, and other features are unchanged.
- Pre-edit backups: `backups/add_diary_app_actions-before-one-tap-check-update-2026-11-11.py`, `backups/build-diary-from-zip-before-one-tap-check-update-2026-11-11.yml`, and `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-one-tap-check-update-2026-11-11.md`, and `backups/add_online_diary_updates-before-one-tap-check-update-2026-11-11.py`.
- Preparing signed APK **1.0.122 / versionCode 121** from live feed baseline **1.0.121 / versionCode 120**. Do not report this repair as complete until the signed build, signature fingerprint, APK checksum, and live feed are verified. Device-side download/install remains pending user confirmation.


**Single source of truth. Last updated: 2026-11-11 (signed APK 1.0.119 / versionCode 118; Web Update 56 keeps Recently Deleted action labels on one line).

## Latest correction — Check for Updates refreshes the verified current web page (2026-11-11)

- User reported that **Me → Check for Updates** said Diary was already updated while the screen still showed the old interface.
- Root cause in the native updater: when the installed HTML SHA-256 already matched the published web bundle, it returned “already latest” without reloading the WebView. The on-disk HTML could be current while the currently displayed page remained alive in WebView memory.
- Narrow repair in `scripts/add_online_diary_updates.py`: when the installed hash matches, reload the existing `https://appassets.androidplatform.net/assets/index.html` URL through the existing verified local-file path handler, then show a refresh-confirmation message. No data, notes, photos, PINs, or package identity are changed.
- A new signed APK **1.0.120 / versionCode 119** is being prepared from the existing 1.0.119 / versionCode 118 baseline. Published web bundle remains **Web Update 56**; no web-source redesign or new web content is required.
- Pre-edit backups: `backups/add_online_diary_updates-before-force-webview-reload-2026-11-11.py`, `backups/build-diary-from-zip-before-force-webview-reload-2026-11-11.yml`, and `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-force-webview-reload-2026-11-11.md`.
- Device-side confirmation is pending. Do not claim the fix works on a phone until the user installs 1.0.120 and tests **Me → Check for Updates**.

## Latest correction — Recently Deleted buttons stay one line (2026-11-11)

- User clarified that **Hamesha ke liye mitaayein** must remain on one line, not wrap to two lines.
- Updated both Recently Deleted action buttons to fixed 40px height, one-line non-wrapping labels, centered text, and responsive smaller font/compact horizontal padding so the full phrase fits within the full-width button on mobile. Restore/delete handlers remain unchanged.
- New pre-edit backups: `backups/web-source-index-before-trash-button-one-line-2026-11-11.html`, `backups/diary-web-index-before-trash-button-one-line-2026-11-11.html`, `backups/latest-before-trash-button-one-line-2026-11-11.json`, and `backups/docs-register-before-trash-button-one-line-2026-11-11.md`.
- Web Update **56**; source and mirror synchronized, SHA-256 `44886700f7382f1f1d5c4c2ec35d602429ce19bf0ac92cea472365e8230872eb`. APK remains **1.0.119 / versionCode 118**. Web-only CSS correction; no note/photo data or PIN changes. Live static checks passed; visual confirmation on physical phone is pending.

## Latest change — Recently Deleted action-button fit (2026-11-11)

- User reported that the **Hamesha ke liye mitaayein** label appeared below/outside the **Mitaayein** button instead of fitting within the complete button.
- Added a dedicated class to the existing Recently Deleted action row and scoped CSS so **Wapas Laayein** and **Hamesha ke liye mitaayein** use equal full-width stacked buttons. Labels can wrap inside the button; height grows naturally when a translated label needs another line. Existing click handlers, confirmation prompts, restore/delete behavior, and trash data are unchanged.
- Backups created before editing: `backups/web-source-index-before-trash-delete-button-fit-2026-11-11.html`, `backups/diary-web-index-before-trash-delete-button-fit-2026-11-11.html`, `backups/latest-before-trash-delete-button-fit-2026-11-11.json`, and `backups/docs-PROJECT_MAP_AND_SECRETS_REGISTER-before-trash-delete-button-fit-2026-11-11.md`.
- Source and mirror are synchronized at blob SHA `a3bec7494f034f558b0c144c28675b05c4f73ac7`. Published feed is Web Update **55**, source length 203,260 characters, SHA-256 `9d3c5d035d5cc94c998cd7392451a7729a6d70c2fea1a9d36c6ae805d2600575`.
- APK remains **1.0.119 / versionCode 118**. This is a web-only layout correction; no APK rebuild, signing change, note/photo data change, PIN change, or MUAZZIN change was made. Static publication checks completed; physical phone appearance still needs user confirmation.


This file replaces the old project register. Read it first at the start of every My Diary task, then inspect the live repository and current source before editing. Older dated audit and handover files in `docs/` are historical evidence only; when they conflict with this register or current GitHub state, do not treat them as current instructions.

## Latest change — Recently Deleted mobile visibility (2026-11-11)

- User reported that opening Me → Haal hi mein delete kiye gaye placed the deleted-note list too far down, hiding its actions on mobile.
- Root cause: the list is moved into the absolutely positioned Me menu, but the menu had no height limit or internal scrolling. Added a mobile-safe maximum height and vertical scrolling to the visible Me menu, with touch scrolling enabled; opening the trash list resets its scroll position to the top.
- The existing deleted-note cards, Restore and Delete Forever actions, trash storage, note data, PINs, and APK/signing identity were not changed.
- Published web source and mirror are synchronized (same blob SHA 9a30a3edec4eafd64ed42ec63ab91f4d08f951ac). Web Update 54 is recorded in latest.json; UTF-8 source length 234,669 bytes and SHA-256 fb177a134365b9cd3b57e792babf3567d913f49dcbf070c84d78cd31d2dd0ab8.
- Backups: backups/web-source-index-before-trash-menu-mobile-scroll-fix-2026-11-11.html, backups/diary-web-index-before-trash-menu-mobile-scroll-fix-2026-11-11.html, backups/latest-before-trash-menu-mobile-scroll-fix-2026-11-11.json, and backups/docs-PROJECT_MAP_AND_SECRETS_REGISTER-before-trash-menu-mobile-scroll-fix-2026-11-11.md.
- APK remains 1.0.119 / versionCode 118; no APK rebuild or signing change was made. Static source/feed checks completed; physical mobile scrolling still needs user confirmation after Me → Check for Updates.

## 0. Current verified release and web-update state — 2026-11-11

- Signed APK **1.0.119 / versionCode 118** was built and published by workflow run **42860862628**. Source validation, debug build, signed Release build, publish, signed APK upload, and artifact upload all completed successfully.
- Live `latest.json` points to `My-Diary-1.0.119.apk`, package `com.personal.diaryapp`, versionCode 118, versionName 1.0.119, and APK SHA-256 `b98e8902f9896971e1dccf634a4d4d0349066f1885a9dee0125a303bf4d57a63`. The main-branch Git tree confirms the versioned APK exists (1,955,249 bytes).
- The 1.0.119 updater repairs false “already latest” reports for the web UI: it compares the installed `filesDir/diary-web/index.html` SHA-256 with feed `webSha256`; only an exact match is treated as current. If not, it downloads the trusted published HTML, verifies SHA-256, then replaces the app-private bundle.
- APK publishing no longer overwrites `web-source/index.html` or `diary-web/index.html` from the older ZIP-generated HTML. The published web UI is preserved when future APK releases are built.
- Current web bundle is **Web Update 52**, restored to the interface from before Calendar View and Note Colours. `web-source/index.html` and `diary-web/index.html` have the same Git blob SHA `48b08d0899aba36093094db3832281e133590c2d`; the exact UTF-8 payload is 234,165 bytes and SHA-256 is `224bb72fce7055f07ea97334c7958a72d4f344987bef603784d56c01e6f081d3`. The live `latest.json.webSha256` now matches this value.
- The Content-Length false rejection was removed from the APK downloader; complete APK downloads are validated by SHA-256, package name, and version.
- Follow-up incident 2026-11-11: users on 1.0.119 saw `Diary update SHA-256 match nahi hua`. Root cause was the published `latest.json.webSha256` value, not the downloaded HTML: it contained an incorrect checksum. Recomputed SHA-256 from the actual raw.githubusercontent.com response bytes (234,165 bytes), corrected `latest.json` to `224bb72fce7055f07ea97334c7958a72d4f344987bef603784d56c01e6f081d3`, and independently re-fetched/re-hashed the raw HTML; exact match confirmed. A later feed edit had reintroduced a stale `webSha256` (`5a018c...`) while the published HTML remained unchanged. On 2026-11-11 this was repaired again after backing up the exact current feed and Master Register; the current feed hash was verified against the 234,165-byte UTF-8 source fetched from GitHub. No APK rebuild required; version remains 1.0.119 / code 118 and webVersion 52.
- Backup files for the updater/workflow repair are `backups/add_online_diary_updates-before-hash-repair-2026-11-10.py` and `backups/build-diary-workflow-before-preserve-web-source-2026-11-10.yml`. The web source backup remains `backups/web-source-index-before-restore-android-back-2026-11-10.html`.
- **Other phones have not been physically tested.** They must install the 1.0.119 APK for the hash-based repair to take effect; then Me → Check for Updates should compare and update the web bundle. Do not claim secondary-phone success until confirmed.
- Do not change local notes, photos, PIN/recovery data, package identity, signing identity, or unrelated features.

## 1. Project identity and boundary

- App: **My Diary** — a standalone Android app, separate from MUAZZIN.
- Repository: `amuazzinxyz-ops/My-Diary-Updates`
- Branch: `main`
- Android package: `com.personal.diaryapp`
- Latest APK currently served by the update feed: **1.0.119**, versionCode **118**. The signed APK is served at https://raw.githubusercontent.com/amuazzinxyz-ops/My-Diary-Updates/main/My-Diary-1.0.119.apk. The current web bundle is served from web-source/index.html and recorded in latest.json as webVersion **52**. Feed SHA-256 for the web bundle: `224bb72fce7055f07ea97334c7958a72d4f344987bef603784d56c01e6f081d3`.
- Latest update feed: `latest.json`.
- Current source archive: `Diary-Android-Project-v13 (6).zip`.
- Build workflow: `.github/workflows/build-diary-from-zip.yml`.
- Helper scripts and language data: `scripts/`.
- Project evidence and dated records: `docs/`.

**Hard boundary:** all future My Diary source, app, build, release, update, and documentation work belongs only in this repository. Do not use or modify the MUAZZIN website/repository/workflows for Diary work. Do not merge the two apps or create a second project/workflow/archive when the existing one can be reused.

## 2. Previously published 1.0.105 release — historical evidence (superseded by the 1.0.104 rollback below)

- Version: **1.0.105** / versionCode **105**.
- Package: `com.personal.diaryapp`.
- Published APK: `My-Diary-1.0.105.apk` (also copied to legacy `My-Diary.apk`).
- Update URL in live `latest.json`: `https://raw.githubusercontent.com/amuazzinxyz-ops/My-Diary-Updates/main/My-Diary-1.0.105.apk`.
- SHA-256 in live feed: `c94b0d682bd86cd0a2c0f344cc0158bcd9346453ede4b0f4eb447b67681ea7cf`.
- Published release commit: [31d2249](https://github.com/amuazzinxyz-ops/My-Diary-Updates/commit/31d2249c6129c850e9dd16818ceb3a4a059842c6).
- Build run `42656590333` completed successfully. The workflow validated the existing signing certificate fingerprint `23A4E93F3C7911DCE18389EA583548700C6AD6A3759707F1CD222D07E2408B5A` before publishing.
- Downloaded signed-release artifact and independently calculated the APK SHA-256; it exactly matches the live feed value above. The versioned APK exists in the main-branch publish commit.
- The 1.0.103 APK contains an allow-list for the repository's raw GitHub URL prefix (not an exact `My-Diary.apk` filename), so the new version-specific APK path remains within that approved prefix. This supports compatibility for older updater clients.
- The affected user's actual in-app download, verification, and installation on another phone remain **not device-verified**. Successful build/publication and matching checksum do not prove that the user's device has completed installation.
- The 1.0.105 updater sends `Accept-Encoding: identity`, but older installed clients cannot benefit from that change until they install a newer APK. The 1.0.106 source fix removes the strict Content-Length equality requirement: the downloader reads the complete response and relies on SHA-256, APK package, and version verification to reject incomplete or incorrect files. The live feed remains at 1.0.105 until the signed 1.0.106 build passes workflow checks and is published. The affected phone's download and installation remain unverified.

## 3. Updater reliability — included in published 1.0.95

- Reversible backup branch created: `backup/pre-updater-reliability-1.0.93`.
- Updater source: `scripts/add_diary_app_actions.py`.
- New downloader retries up to three times, uses a temporary partial file, checks content length when supplied, verifies SHA-256, validates APK package and version against the feed, and opens Android's unknown-app install permission settings when needed.
- 2026-11-09 user reported that tapping Download & Install shows the APK download/SHA-256 start message and then immediately reports download/verification failure. The signed APK and live latest.json remain 1.0.105 / versionCode 105 while the next release is prepared. The current updater requests uncached metadata and APK URLs, retries three times, checks HTTP response/content length/SHA-256/package/version, follows HTTPS GitHub CDN redirects only to approved GitHub content hosts, and displays the actual failure reason. The user's earlier generic message did not reveal which check failed; the proposed 1.0.106 change addresses the strict Content-Length failure path, but the affected phone must still be tested. A successful publication does not prove device-side download/install success.
- Uses the existing raw.githubusercontent.com APK URL so older 1.0.92 clients' URL allow-list is not changed.
- The 1.0.103 release was built against the approved transition from feed baseline 1.0.102/102 and published only after package/version and trusted signing checks passed.
- Relevant updater/workflow commits: `60d19813d1b9e2ab4361238c829dda17acf401bf` (updater compatibility), `460ddfd6fe7035c893e1b71790288c408fc57650` (1.0.94 version gate), `1b7c87a51bf97232081e34f80731b6e15b77be0f` and `9f6a4d5e4120bc6b8aa9ff1175a225d52f2f91a1` (serialized, safe publishing), and `fd25e3dd44ca16f594a14076a9a7904a6dcd4694` (removed a redundant publish-stage version parser).
- The successful release workflow run `42634599963` published the verified signed 1.0.103 APK and feed after signing, package, version, and SHA-256 checks passed.

Before a later release:
1. Read live `latest.json` and current Gradle/workflow version gates.
2. Advance the next version from the actual feed, not from memory.
3. Keep fail-closed package, baseline, next-version, signing, and metadata checks.
4. Never publish a debug or unsigned APK as an app update.

## 4. Language status and next language work

The current translation expansion includes these 10 app language options:
1. Roman English
2. English
3. Hindi
4. Urdu
5. Arabic
6. Bengali
7. Gujarati
8. Marathi
9. Tamil
10. Telugu

Arabic was added in the 1.0.92 source change (133 translation keys matching the Urdu schema); Kannada was replaced by Arabic in that change. Arabic is RTL. Treat wording quality as needing language review where appropriate; key-count matching alone does not prove perfect translation.

**User's next language goal:** expand from 10 to 20 languages. Complete the remaining 10 language options before starting automatic language detection. Before adding each language, inspect the current translation schema and generated UI text audit, avoid duplicate or partial dictionaries, and test coverage/RTL behavior where relevant. Do not claim 20 languages are complete until all 20 options and their interface strings have been checked.

## 5. Diary feature map and preservation requirements

This is the standalone My Diary app, not the Diary panel inside MUAZZIN. The existing project/archive and generated Diary HTML are the source to inspect. The following are user requirements and known feature areas; **verify their exact current implementation in the source before editing rather than assuming every requested detail is already complete**.

### Existing feature areas to preserve
- Notes and Diary entries, including saved local records.
- Note lock and the existing PIN protection.
- Diary PIN lock and its recovery/forgot-code flow.
- Photos and attachments.
- Share note / share content.
- Pin Note, Favourite, Smart Search.
- Multi-select notes and delete controls.
- Note editor formatting and existing text/name fields.
- App language selector and translation dictionaries.
- Android app identity, local storage, update behavior, and navigation.

### Specific user requirements — do not regress
- Never change or remove the existing **Note lock** while making unrelated changes.
- Preserve existing diary entries, photos, local storage keys, PIN hashes, and recovery behavior.
- For Diary lock recovery, after a forgotten-code recovery/unlock, require a newly created code before the same old recovery path can be reused, as previously requested; inspect current source to see whether this is implemented before changing it.
- Note editor should retain its two existing fields: optional name (`Note ka naam (optional)`) and note text (`Yahan apni baat likhein…`). Do not add separate duplicate image boxes.
- An image selected near the name belongs within the name field/design; an image selected near the note text belongs within the text field/design. Preserve image/text placement when sharing; do not shift all text to the left or duplicate title/name text.
- Font-size controls must change actual text size (not merely box dimensions); font family and bold controls should work on the intended text.
- Preserve existing layout, buttons, colors, behavior, and all unrelated functions unless the user explicitly asks for a change.

## 6. Signing, app identity, and data safety

- Keep package `com.personal.diaryapp` unchanged.
- Keep using the existing trusted signing setup and same signing identity for in-place updates. Never generate a new keystore or signing key.
- The four expected GitHub Actions secret names are:
  - `DIARY_KEYSTORE_BASE64`
  - `DIARY_KEY_ALIAS`
  - `DIARY_KEY_PASSWORD`
  - `DIARY_STORE_PASSWORD`
- Their values are secret: never print, request in chat, commit, or place in documentation. Do not delete, rename, regenerate, or change them.
- The 1.0.92 workflow run successfully passed its signing readiness/keystore validation and published the signed release; the user's phone then accepted it as an update.
- Never ask the user to uninstall the working app, clear app data, or delete local notes/photos as a routine troubleshooting step.
- Never replace the release APK with a debug or unsigned APK.

## 7. Required workflow for every new request

When the user says **“new kaam”**, **“sudhar”**, **“aage”**, or gives a feature request:

1. Read this Master Register first.
2. Inspect the live repository head, latest commit, current APK/feed version, source archive, relevant source/script, and build workflow. Do not rely on old chat snippets or historical audit notes alone.
3. Identify the exact existing section/function and check whether the requested feature already exists.
4. Start directly if the request is clear. Do not ask the user to upload files or repeat information already in this repository/register.
5. Ask only one concise question if an essential detail is genuinely missing or a change could risk data, security, app identity, or an irreversible behavior.
6. Before editing, preserve the original source/archive and create a clear backup or reversible commit. Change only what the user requested.
7. Preserve all unrelated features and existing user data. Do not refactor or redesign unrelated screens.
8. Run the relevant static checks, syntax checks, translation coverage checks, Android build, and release verification as applicable.
9. For a production update, verify package, monotonically increasing versionCode, versionName, trusted signing identity, APK SHA-256, exact feed URL, and publish workflow. A successful build alone is not proof of a successful phone update.
10. Report what changed, exact files/commit, tests passed/failed, and what remains untested. Never claim a device test unless the user confirms it or there is actual device evidence.
11. Update this register after each important source, feature, language, version, workflow, or release change. Keep dated audit files as historical evidence, not competing master registers.

## 8. Current update failure status (2026-11-09)

- User clarified that their own phone updates successfully; the failure affects other users who are on 1.0.103 or older and see: “Download/verification nahi hua. Update abhi install nahi kiya gaya”.
- 1.0.105 is now published with a unique version-specific APK URL to avoid stale CDN content associated with overwriting the same APK filename. The signed APK artifact's independently calculated SHA-256 matches the live feed exactly; build, trusted signing-certificate check, and publish all succeeded.
- The older 1.0.103 client's approved raw-GitHub URL prefix accepts the new versioned APK path. The 1.0.105 updater adds `Accept-Encoding: identity` for strict Content-Length checks, but this cannot retroactively change downloader code on already-installed older clients.
- The actual affected user's in-app download, verification, and installation are still **not device-verified**. Do not say the issue is fully fixed until an affected user confirms a successful in-app update.
- Do not create a new signing key, publish a debug APK, uninstall the existing app, clear app data, or alter local notes/photos/PIN data. Preserve the existing signing identity.

## 9. User's current known next goal

- Continue completing the remaining 10 languages to reach 20 total.
- Only after all 20 languages are complete and checked, work on automatic language detection.
- For any new feature or correction the user specifies before that, prioritize the exact request and preserve the rest of the app.

## 10. Short request format (optional)

The user can simply say what they want in Roman Hindi. No special template, file upload, or explanation is required when the existing project contains what is needed.


- Historical publish validation note: the earlier redundant version-parser failure was corrected before the verified 1.0.94 release. That 1.0.94 parser failure is historical; the current live feed and 1.0.95 release evidence above are authoritative.

## 11. User-requested version rollback — 2026-11-09

- User explicitly confirmed restoring **My Diary 1.0.104 / versionCode 104** and removing the later 1.0.105, 1.0.106, and 1.0.107 release files from the active main-branch distribution.
- Live `latest.json` now serves versionCode 104 / versionName 1.0.104 with the original recorded SHA-256 `f14e75d502d9263e29ab81250f781925f034afe63296a7444abd4cc8c65c7544`.
- APK URL is pinned to immutable historical commit `89219d4e9e553f606b5323a85723705e9ca3ed44`, path `My-Diary.apk`; the historical APK path and matching old metadata were confirmed present.
- Web bundle metadata is also restored to the 1.0.104-era webVersion 8 and pinned to the same immutable commit.
- Removed from the main branch: `My-Diary-1.0.105.apk`, `My-Diary-1.0.106.apk`, `My-Diary-1.0.107.apk`, and the main-branch `My-Diary.apk` alias that pointed to 1.0.107. Their historical Git objects/commits remain recoverable; this was not a destructive history rewrite.
- The separate legacy file `My-Diary.apk.apk` was not touched because it is not one of the 1.0.105–1.0.107 files targeted by the user's instruction.
- This restores the distribution feed and release assets only. It does not install or downgrade the app on any phone. The affected-device in-app update still needs a real phone-side test; do not claim it is fixed until confirmed.


## 12. Updater-compatible APK URL repair — 2026-11-09

- Root cause: `latest.json` had been changed to an immutable commit URL. The installed updater only accepts APK URLs under `https://raw.githubusercontent.com/amuazzinxyz-ops/My-Diary-Updates/main/`; therefore it rejected the commit-pinned APK as an untrusted URL before installation.
- Restored the exact original signed 1.0.104 APK blob (`ff244e050b348a8e92e3871375db838521a5b259`, 1,950,182 bytes) at `main/My-Diary.apk` without rebuilding or resigning it.
- Restored `latest.json.apkUrl` to the updater-compatible `/main/My-Diary.apk` path. Version remains 1.0.104 / versionCode 104; APK SHA-256 remains `f14e75d502d9263e29ab81250f781925f034afe63296a7444abd4cc8c65c7544`.
- Verified the 1.0.104 signed release artifact independently: SHA-256 matches the feed; successful workflow run `42648457972` confirms the trusted signing certificate fingerprint `23A4E93F3C7911DCE18389EA583548700C6AD6A3759707F1CD222D07E2408B5A`.
- New repair commit: `58652250ae0d390c28bbe7ebe522b5aaf8ec1b5b`.
- The phone-side in-app download/install is not yet device-verified. Do not claim completion until an affected 1.0.103-or-older device confirms installation.


## 13. APK download verification repair and signed release — 2026-11-09

- Confirmed the signed 1.0.104 updater still compared the received byte count against the HTTP `Content-Length` header. GitHub/CDN transfer behavior can make that header differ from the bytes delivered to the Android client, causing valid APK downloads to be rejected before installation.
- The current updater source now sends `Accept-Encoding: identity`, reads the full response body, and verifies the completed APK using SHA-256, package name, and versionCode; it does not reject a valid file solely because `Content-Length` differs.
- Repaired the release workflow's stale hardcoded version gates to build **1.0.105 / versionCode 105** from the live **1.0.104 / versionCode 104** feed baseline.
- Signed release workflow run `42668393009` passed source validation, debug build, signed release build, signing checks, publish, and artifact upload. Published feed points to `My-Diary-1.0.105.apk` and records SHA-256 `32a8d90f991cab12b1e3ad462e8a4b82135b11d3bc783be54e7f5280749864a2`.
- Live `latest.json` release notes were corrected to describe the updater fix. The phone-side in-place installation and update behavior still require confirmation on a device; do not claim device verification until the user confirms it.
- No app data, notes, photos, or PIN storage was cleared or migrated by this release task.
## 14. My Diary 1.0.112 — confirmed update workflow and current handover (2026-11-10)

- Current published release: **1.0.112**, versionCode **111**, package `com.personal.diaryapp`.
- Current APK: `My-Diary-1.0.112.apk`; feed URL: `https://raw.githubusercontent.com/amuazzinxyz-ops/My-Diary-Updates/main/My-Diary-1.0.112.apk`.
- Current APK SHA-256 from live `latest.json`: `040740f50feb19447ce9dc0aaeb69c2190539d3ff02737ec15247e51ee43bba2`.
- Successful signed build/publish workflow run: `42688075014` — **success**.
- This release sets all three Diary action buttons to **40px height**: **Check for Updates**, **Refresh**, and **Share App**.
- **User-confirmed device result (2026-11-10):** the user reports that updates now work correctly on their own mobile and on the other user's mobile using **Check for Updates**. Treat this as the current successful real-device confirmation, replacing the older “device-side update pending” status in historical sections above. Do not continue describing the current update flow as unverified.
- Current stopping point: the update/download/verification/install flow is working as confirmed by the user. No further updater changes are needed unless a new reproducible problem is reported.
- For the next task, first read this register and inspect the live `main` branch, `latest.json`, current source archive, relevant script, and workflow. Continue in the same narrow, backup-first, test-before-release manner.
- Preserve package `com.personal.diaryapp`, the existing trusted signing identity/secrets, all diary notes/photos, PIN Lock and recovery, and every unrelated feature. Never uninstall the working app or clear its data as a routine step. Do not modify MUAZZIN.
- For future releases, derive the next version from the live feed (currently versionCode **112**); do not reuse or guess a version. Verify build, signing, APK SHA-256, feed URL, and release publication. Report phone-side behavior only as confirmed by the user or actual device evidence.


## 15. Me menu button height update — 2026-11-10

- User requested that every button inside the My Diary **Me** menu be exactly **40px** high.
- Added a narrowly scoped CSS rule to `web-source/index.html` targeting buttons and button-role/input button controls inside `#diaryDiaryMePanel` only. It sets `height`, `min-height`, and `max-height` to 40px with `!important`; controls and buttons outside the Me menu are not targeted.
- Preserved the pre-edit HTML at `backups/web-source-index-before-me-buttons-40px-2026-11-10.html`.
- Updated `latest.json` web bundle metadata to webVersion 18 and SHA-256 `1fef5d5719bb402408db38d3454127eb68dc0382ed68d6677c133a22ce17aeb2`.
- Static verification: the new scoped CSS rule is present in the live source; the backup file is present. No Android APK rebuild or physical-device visual test was performed for this CSS-only web bundle change.

## 16. My Diary 1.0.113 — Interface Colours in Me menu (2026-11-10)

- Current published release: **1.0.113**, versionCode **112**, package com.personal.diaryapp.
- Signed APK: My-Diary-1.0.113.apk; feed URL: https://raw.githubusercontent.com/amuazzinxyz-ops/My-Diary-Updates/main/My-Diary-1.0.113.apk.
- APK SHA-256 from live latest.json: 4db6f8e7bf5fea511a133a8750e56060f165d8d0653739a5cddbfba62a5c48cc.
- Successful signed build/publish workflow run: 42774333846. Debug build and signed Release build succeeded; the release certificate SHA-256 matched the previously trusted signing fingerprint 23A4E93F3C7911DCE18389EA583548700C6AD6A3759707F1CD222D07E2408B5A.
- Added 🎨 Interface Colours inside the existing Me menu. It offers Original, Blue, Green, and Rose themes. The selected theme is saved locally using the separate key diary_interface_theme_v1 and restored when the Diary opens.
- Added translations for the new button and palette labels in all 10 existing language options.
- Updated only the Diary generation/language scripts and the Diary-only APK workflow version gate. The workflow publishes the generated Diary web bundle and signed APK; no MUAZZIN repository or workflow was used.
- Backups created before editing:
  - backups/add_diary_refresh_button-before-interface-colours-2026-11-10.py
  - backups/expand_diary_languages-before-interface-colours-2026-11-10.py
  - backups/build-diary-from-zip-before-interface-colours-2026-11-10.yml
  - backups/web-source-index-before-interface-colours-2026-11-10.html
  - backups/README-before-interface-colours-release-2026-11-10.md
  - backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-interface-colours-release-2026-11-10.md
  - backups/latest-before-interface-colours-release-2026-11-10.json
- Static verification: Diary project validation passed; generated HTML/JavaScript syntax check passed; translation audit passed; debug build passed; signed Release build passed; signing certificate and publish checks passed. The published web source contains the Interface Colours button, theme persistence, palette CSS, and all 10 localized labels.
- Not yet verified on a physical phone: visual appearance and in-place installation of 1.0.113. Do not claim a device test until the user confirms it. Existing notes, photos, PIN Lock/recovery, package identity, and signing identity were preserved.
- Current version baseline for the next release: versionCode **112** / versionName **1.0.113**. Derive the next version from the live feed and keep all existing data and features intact.


## 17. My Diary 1.0.114 — updater download progress and verification visibility (2026-11-10)

- Current published release: **1.0.114**, versionCode **113**, package **com.personal.diaryapp**.
- Signed APK URL: https://raw.githubusercontent.com/amuazzinxyz-ops/My-Diary-Updates/main/My-Diary-1.0.114.apk.
- APK SHA-256: `223a0a8397764e289c1a95fae6aa674ff3272c55b1db2d6b340bf96ec98802c0`. The downloaded signed workflow artifact APK was independently hashed locally and matched the live `latest.json` checksum exactly.
- Successful signed build/publish workflow run: **42786868649**. Debug build, signed Release build, publication, and artifact upload succeeded. The signing certificate was verified against the previously trusted SHA-256 fingerprint `23A4E93F3C7911DCE18389EA583548700C6AD6A3759707F1CD222D07E2408B5A`.
- User-reported symptom prompting this change: APK download appears to stop after about 10–20 seconds. Static inspection showed the updater only displayed a short Toast and had no persistent progress UI; that made it impossible to tell whether bytes were still downloading, a retry was happening, or the transfer had failed.
- Kept the existing HTTPS download, three-attempt retry, SHA-256 verification, package/version validation, and Android installer flow. Added a persistent native progress dialog with percentage when the server provides a content length, indeterminate progress otherwise, visible retry status, verification status, and dismissal before installer launch or failure details. This is a narrow updater-only change.
- Updated the build workflow to versionCode 113 / versionName 1.0.114 and the matching APK filename/path. The workflow's baseline guard required the live 1.0.113 / 112 feed before publishing.
- Backups created before editing:
  - `backups/add_diary_app_actions-before-download-progress-2026-11-10.py`
  - `backups/build-diary-from-zip-before-download-progress-2026-11-10.yml`
- Verification: source generation and JS syntax audit passed; Android debug build passed; signed Release build passed; APK signature fingerprint passed; live metadata SHA-256 matched the signed APK bytes. No physical-device installation or real network download test has yet been performed, so do not claim the original 10–20-second symptom is fully resolved until the user confirms the 1.0.114 update behavior. The new persistent progress/error display will show the actual stage and failure reason if it recurs.
- Preserved Diary notes, photos, PIN settings, package identity, signing identity, existing Check for Updates entry point, Refresh, and unrelated app features. Do not change the download mechanism again without a reproducible reason.

## 18. My Diary web-only update 29 — Interface Colours label fit (2026-11-10)

- User reported that the final “s” in “Interface Colours” was clipped and the in-app Check for Updates message said Diary was latest.
- Confirmed the existing Android updater source already compares the independent `webVersion` field after confirming the APK is current. The Android build workflow runs `scripts/add_online_diary_updates.py`; that code downloads the trusted web bundle, validates SHA-256 and HTML, stores it separately under app files, and reloads the WebView without replacing the APK or touching Diary data.
- Created backup: `backups/web-source-index-before-interface-colours-label-fit-2026-11-10.html`.
- Corrected the Interface Colours button label fit while keeping its height exactly 40px: font size 16px, reduced horizontal padding, and no clipping overflow. Removed the duplicate 🎨 prefix from the button label in the preceding web-only commit.
- Web-only publish workflow run **42795407894** (run 11) completed successfully.
- Verified live `latest.json` reports **webVersion 29** and SHA-256 `84ec629260635c86badc2081c0e63232f8a1009ae1d1c0f1f765af1c67c1beab`; published `diary-web/index.html` contains the updated 16px label rule and overflow-visible rule.
- APK remains **1.0.115 / versionCode 114**; no APK rebuild, signing change, or local Diary data change was made.
- Phone-side application of webVersion 29 and the final visual appearance still require user confirmation. Ask the user to tap **Me → Check for Updates** again; if the installed app already has webVersion 29, it will correctly report latest.

## 19. My Diary 1.0.116 — native PDF Save and Android Back handling (2026-11-10)

- Current published APK: **1.0.116**, versionCode **115**, package **com.personal.diaryapp**.
- Signed APK URL: https://raw.githubusercontent.com/amuazzinxyz-ops/My-Diary-Updates/main/My-Diary-1.0.116.apk.
- APK SHA-256: `0b4d5b60bdf8e77688a434ae1ce4c09cbd699fcee4877d362690b1fb3354488f`. The signed Release APK workflow artifact was downloaded and independently hashed; it exactly matches the published `latest.json` checksum.
- Current online web bundle: **webVersion 43**; web bundle SHA-256: `eeac50f1b19f2a1c2903cbbeae4d9f284dbfb9437ca565642e0d2dbf7a32c381`.
- Successful signed build and publish workflow run: **42842056052**. Diary generation, translation audit, JavaScript syntax check, Android debug build, signed Release build, publish, and artifact upload passed. The release certificate SHA-256 matched the previously trusted fingerprint `23A4E93F3C7911DCE18389EA583548700C6AD6A3759707F1CD222D07E2408B5A`.
- PDF Save now uses a dedicated `DiaryPdfActions.printDiaryPdf` Android JavaScript bridge and native Android `PrintManager` / `WebView.createPrintDocumentAdapter`. The note is saved first; Android's print sheet then offers **Save as PDF**. The ordinary browser popup/print path remains as a fallback outside the native app.
- Android Back now asks the WebView whether the Diary overlay is open. If it is open, Back is consumed and the Diary remains visible; the user closes it using the existing visible × button. When the overlay is not open, normal WebView history / Activity back behavior continues.
- The current online web bundle was used as the APK's embedded Diary HTML so the 1.0.116 APK retains the latest web-only features instead of reverting to the older generated base.
- Backups created before this change:
  - `backups/add_diary_app_actions-before-native-pdf-back-2026-11-10.py`
  - `backups/build-diary-from-zip-before-native-pdf-back-2026-11-10.yml`
  - `backups/web-source-index-before-native-pdf-back-2026-11-10.html`
- Existing notes, photos, local storage, PIN Lock/recovery, package identity, signing identity, updater, and unrelated Diary features were not intentionally changed. No keystore or signing secret was regenerated or altered.
- Static/build verification is complete, but **physical-device behavior has not yet been confirmed**. Ask the user to install **1.0.116** using **Me → Check for Updates**, then test PDF Save (choose Save as PDF in Android's print sheet) and Android Back while the Diary editor is open. Do not claim either behavior is device-verified until the user confirms it.
- This section supersedes the older version baseline and webVersion notes in sections 17–18. Current next-release baseline: **versionCode 115 / versionName 1.0.116 / webVersion 43**. Derive the next version from the live feed.

## 19. My Diary 1.0.116 — native PDF Save and Android Back handling (2026-11-10)

- Current published APK: **1.0.116**, versionCode **115**, package **com.personal.diaryapp**.
- Signed APK URL: https://raw.githubusercontent.com/amuazzinxyz-ops/My-Diary-Updates/main/My-Diary-1.0.116.apk.
- APK SHA-256: `0b4d5b60bdf8e77688a434ae1ce4c09cbd699fcee4877d362690b1fb3354488f`. The signed Release APK workflow artifact was downloaded and independently hashed; it exactly matches the published `latest.json` checksum.
- Current online web bundle: **webVersion 43**; web bundle SHA-256: `eeac50f1b19f2a1c2903cbbeae4d9f284dbfb9437ca565642e0d2dbf7a32c381`.
- Successful signed build and publish workflow run: **42842056052**. Diary generation, translation audit, JavaScript syntax check, Android debug build, signed Release build, publish, and artifact upload passed. The release certificate SHA-256 matched the previously trusted fingerprint `23A4E93F3C7911DCE18389EA583548700C6AD6A3759707F1CD222D07E2408B5A`.
- PDF Save now uses a dedicated `DiaryPdfActions.printDiaryPdf` Android JavaScript bridge and native Android `PrintManager` / `WebView.createPrintDocumentAdapter`. The note is saved first; Android's print sheet then offers **Save as PDF**. The ordinary browser popup/print path remains as a fallback outside the native app.
- Android Back now asks the WebView whether the Diary overlay is open. If it is open, Back is consumed and the Diary remains visible; the user closes it using the existing visible × button. When the overlay is not open, normal WebView history / Activity back behavior continues.
- The current online web bundle was used as the APK's embedded Diary HTML so the 1.0.116 APK retains the latest web-only features instead of reverting to the older generated base.
- Backups created before this change:
  - `backups/add_diary_app_actions-before-native-pdf-back-2026-11-10.py`
  - `backups/build-diary-from-zip-before-native-pdf-back-2026-11-10.yml`
  - `backups/web-source-index-before-native-pdf-back-2026-11-10.html`
- Existing notes, photos, local storage, PIN Lock/recovery, package identity, signing identity, updater, and unrelated Diary features were not intentionally changed. No keystore or signing secret was regenerated or altered.
- Static/build verification is complete, but **physical-device behavior has not yet been confirmed**. Ask the user to install **1.0.116** using **Me → Check for Updates**, then test PDF Save (choose Save as PDF in Android's print sheet) and Android Back while the Diary editor is open. Do not claim either behavior is device-verified until the user confirms it.
- This section supersedes the older version baseline and webVersion notes in sections 17–18. Current next-release baseline: **versionCode 115 / versionName 1.0.116 / webVersion 43**. Derive the next version from the live feed.


## 20. My Diary web-only update 50 — Calendar View and per-note colours (2026-11-11)

- User requested two additions to the existing My Diary project: **Calendar View** (select a saved date and see notes from that day) and **Note Colours** (choose a background colour for each note).
- Added a month calendar with previous/next month navigation, note counts on dates, and date selection to filter the note list by the note's original `created` date. The All Notes control clears the selected date filter.
- Added a per-note colour selector with Original/default plus Yellow, Green, Blue, Pink, Purple, and Peach. The selected `noteColor` is stored within that note's existing JSON record, restored when editing, applied to its note card, and retained by JSON backup/export/import. Existing notes without this property remain unchanged and use the original background.
- Added Roman English, English, Hindi, Urdu, Arabic, Bengali, Gujarati, Marathi, Tamil, and Telugu labels for both features and colour choices.
- Created pre-edit source backup: `backups/web-source-index-before-calendar-and-note-colours-2026-11-11.html`.
- Source commit: `ee74f5df8b9deac8cc570acc49a040e7e8a43110`. The existing web-only publishing workflow completed its publish action: live `latest.json` now reports **webVersion 50** and SHA-256 `a5e8350fe48595f114f6b8a9344d2144e79788e7f2f22ad2128bbd3d8fa5e3c8`. Re-fetched source and published mirror both contain the features and have the same Git blob SHA `c050f46b75cae959a70eeb6ad18c5a1c45261fdd`.
- Static validation: both inline JavaScript blocks in the modified HTML parsed successfully; the publish workflow accepted the HTML and updated the feed/mirror. No APK rebuild was required; APK remains **1.0.119 / versionCode 118**. No app data, notes, photos, PIN/recovery, package identity, or signing settings were intentionally modified.
- Physical phone appearance and use of the new Calendar View/colour selector have **not yet been confirmed**. Ask the user to use **Me → Check for Updates** to receive Web Update 50, then verify both features on the phone. Do not claim device-side testing until the user confirms it.

## 21. Recently Deleted note display repair — 2026-11-11

- User reported that notes inside **🗑️ Haal hi mein delete kiye gaye** no longer opened/displayed as before.
- Root cause: the trash-note expand handler removed the hidden flag from its details container, but did not add the existing expanded class to its note card. The existing Diary CSS intentionally hides .diary-note-full previews until the card has .expanded; as a result, the note content stayed invisible even after tapping its title.
- Narrow fix: the trash-note title toggle now toggles card.classList.toggle('expanded', opening) alongside the details visibility and aria-expanded state. This reuses the existing note-card design and CSS; no redesign or storage-key change.
- Backups before edit: backups/web-source-index-before-recently-deleted-display-fix-2026-11-11.html, backups/diary-web-index-before-recently-deleted-display-fix-2026-11-11.html, backups/latest-before-recently-deleted-display-fix-2026-11-11.json, and backups/docs-PROJECT_MAP_AND_SECRETS_REGISTER-before-recently-deleted-display-fix-2026-11-11.md.
- Source fix commit: 7447af3c120d91649983c0400118240812788f3e; published mirror sync commit: 905c0edeae6bf98c3a8f0a7148f498d81ccfc080.
- Live update feed reports webVersion 53 and SHA-256 17d56cee11f46d5be90e4a274150cccab48d6f190099f64054d411fd05c337d3 for the 234,207-byte HTML bundle. The source and mirror must be confirmed identical before closing this repair. APK remains 1.0.119 / versionCode 118; this is a web-only correction, so no APK rebuild or signing change.
- Static check: the trash title handler toggles the same .expanded class required by the existing CSS rule that reveals .diary-note-full. Actual display on the user's phone is not device-tested; receive Web Update 53 via Me → Check for Updates.


## 22. Recently Deleted panel design refresh — 2026-11-11

- User requested a modest design improvement inside the panel opened by **Me → 🗑️ Haal hi mein delete kiye gaye**. This change is limited to the appearance of the deleted-note cards and their expanded details.
- Added scoped CSS only: softly rounded individual note cards, a subtle green accent and light background, clearer tap-to-expand title surface, a softly framed note-preview area, and a compact expiry label. The existing Restore and Delete Forever buttons retain their current layout, 40px height, one-line labels, and existing click handlers.
- No HTML structure, JavaScript handlers, trash storage key/data, note content, photo data, PIN Lock/recovery, package identity, APK, or signing files were changed. No MUAZZIN files or repository were accessed for edits.
- Pre-edit backups:
  - `backups/web-source-index-before-trash-panel-design-2026-11-11.html`
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-trash-panel-design-2026-11-11.md`
- Source commit: `01d797e8681d182f26c3ca0c86a17e1d5219cf4a`. Web-only publish workflow run **42968535389** completed successfully.
- Published **Web Update 57**. Live feed SHA-256: `84ae2034860516397ceaa6077c7033a30735da6b6560ad897ea2031791fbe590`. Source and published mirror have identical blob SHA `9c0bda40dcdaf11622fa393cbb5f13772435ab53`; both are 205,602 bytes.
- APK remains **1.0.122 / versionCode 121** (SHA-256 `62a7f7687777b9f2caa548ee9c96c327b75eefa2630828b159e42052f0251aa9`). No APK rebuild was needed because this is a web-only styling change; no signing operation was performed.
- GitHub Actions HTML/feed publication checks passed. The panel's visual appearance on a physical phone has not been device-confirmed; use **Me → Check for Updates** to receive Web Update 57, then open Recently Deleted to inspect it.


## 23. Me menu touch scrolling repair — 2026-11-11

- User reported that the buttons inside the Diary **Me** menu appeared fixed and could not be scrolled to reach the lower options.
- Root cause: the dropdown is absolutely positioned inside the Diary header, while the containing `#diaryMyNotesPanel` has `overflow:hidden`; the parent clipped the dropdown below its boundary even though the dropdown had an earlier max-height/overflow rule.
- Narrow fix: when the Me menu opens, add `diary-me-menu-open` to the Diary panel so the panel/header allow the dropdown to extend beyond the frame; give the menu an explicit touch-friendly vertical scroll area (`overflow-y:auto`, `-webkit-overflow-scrolling:touch`, `touch-action:pan-y`, contained overscroll, and a viewport-safe max-height). Reset scroll to the top when opening. Remove the open class when the user taps outside or closes the Diary. The Recently Deleted entry path also activates the same menu-open state.
- Existing menu button order, button sizes, click handlers, translations, note/trash data, photo data, PIN Lock/recovery, and all unrelated features are unchanged.
- Backups:
  - `backups/web-source-index-before-me-menu-scroll-fix-2026-11-11.html`
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-me-menu-scroll-fix-2026-11-11.md`
- Source commit: `2c66f2ab531adfbed4a026fe6516628afd95ff3f`. Web-only publish workflow run **43010831372** completed successfully.
- Published **Web Update 58**. Feed SHA-256: `a79d757830530671cc5715046dbd0bf49a259116a15152a95a059639c9232802`. Source and published mirror have identical blob SHA `f16f50d419d48efd852cb89c1682516ae75d77b3`.
- APK remains **1.0.122 / versionCode 121**; no APK rebuild or signing operation was needed. No MUAZZIN project was changed.
- Automated GitHub web publication checks passed. Physical-device touch scrolling still needs the user to confirm after **Me → Check for Updates** receives Web Update 58.

## 24. Me dropdown overlay and Note Pin separation — 2026-11-11

- User reported that after tapping **Me**, Note Pin (📌) and underlying Diary card content appeared mixed into the Me menu instead of the Me options opening as a distinct dropdown.
- Code inspection confirmed that the Note Pin control is generated only as part of each saved note card, not as a Me-menu option. The Me dropdown CSS had a transparent background and no visible panel surface; after the scroll repair allowed it to extend beyond the Diary frame, the underlying note cards could show through the dropdown area. This made their Pin controls appear to be part of Me.
- Narrow CSS-only repair: made the open Me dropdown an opaque, bounded, raised panel with its own stacking context; preserved the existing menu position, order, 40px controls, scrolling and click handlers. Added a defensive rule to hide any .diary-note-pin only if it is ever rendered inside the Me menu. Note Pin controls remain on their own note cards.
- Backups created before the edit:
  - backups/web-source-index-before-me-menu-overlay-fix-2026-11-11.html
  - backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-me-menu-overlay-fix-2026-11-11.md
- Source commit: 3a2a083738162736153e0f5c56adff123a402c04. Web-only publish workflow run **43012733041** completed successfully.
- Published **Web Update 59**. Live feed SHA-256: 63e85562878fcc65e04e05fdca00718c41e99b948003294a94e925f3e0fbed0a. Source and published mirror have identical blob SHA 7f0ce0ac10c84f8e6786a770b1faab75d2b870f9.
- APK remains **1.0.122 / versionCode 121**; no APK rebuild or signing operation was performed. Notes, photos, PIN Lock/recovery, package identity, and existing button handlers were not intentionally changed.
- GitHub publication checks passed. Physical phone appearance has not yet been device-confirmed. On the phone, use **Me → Check for Updates** to receive Web Update 59, then open Me and confirm that only the Me menu options appear on an opaque panel, with Note Pin remaining on each note card.



## 25. WebView stale-page cache repair — Diary 1.0.123 preparation (2026-11-11)

- User reported that the **Diary ka Asal Rang** label still appeared as the previous Roman wording on the installed Android app, even though the live HTML source and web bundle already contained the requested new wording.
- Inspection confirmed the current Roman dictionary entry is exactly `Diary ka Asal Rang`; the obsolete wording is absent from the current `web-source/index.html`. The live update feed is webVersion **60** and its SHA-256 matches the published bundle.
- Root cause identified in the Android update path: the native `DiaryBundlePathHandler` returned the same `appassets.androidplatform.net/assets/index.html` URL without explicit no-cache response headers. A WebView could reuse an older cached response after the verified on-disk HTML bundle was replaced.
- Narrow native updater repair in `scripts/add_online_diary_updates.py`: both post-update reload paths now append a unique `diaryRefresh` query value; the asset path handler sends `Cache-Control: no-store, no-cache, must-revalidate, max-age=0`, `Pragma: no-cache`, and `Expires: 0`. The hash-verified download, local bundle backup, bundled-asset fallback, app origin, notes/photos/PIN storage, and signing identity remain unchanged.
- Backups before the repair:
  - `backups/add_online_diary_updates-before-webview-no-cache-2026-11-11.py`
  - `backups/build-diary-from-zip-before-webview-no-cache-2026-11-11.yml`
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-webview-no-cache-2026-11-11.md`
- Source commits: updater repair `65e3776e0c30f9533e004298ab6a64c8bfd0115e`; workflow version bump `256bf955ab711ee9a231e2dab17ecce273124375`; cleanup `99e0f38b079645ead7ca13d9e3d6d2b6995f6d2e`; final publish-guard alignment `ff28c27277423d888fd0da8bf85e251d2230581e`.
- The existing release workflow is prepared to build **1.0.123 / versionCode 122** from the exact latest published HTML, using the existing package name and existing trusted signing key. Live APK remains **1.0.122 / versionCode 121** until the signed build and publish workflow succeeds.
- This is a native WebView cache-delivery repair, so a new APK is required for installed apps to receive the stronger no-cache handling. No APK has been declared published until the workflow completes and the signed artifact/feed checks pass. Phone-side display must still be confirmed after installing the update.


---

# Web Update 114 — Diary subtitle tap instruction wording (2026-11-12)

- User-requested exact Roman-language subtitle change under **Meri Diary**: `Apne notes likhein aur search karein` → `Apne notes likhein aur search karne Yaha Tap Kare`.
- Changed exactly one occurrence in `web-source/index.html`; synchronized `diary-web/index.html` to the same exact content. No other language strings, Diary features, buttons, search logic, storage, notes/photos, PIN/recovery flow, APK, package identity, or signing data were changed.
- Backups: `backups/web113-before-diary-subtitle-tap-wording-2026-11-12.html`, `backups/diary-web113-before-diary-subtitle-tap-wording-2026-11-12.html`, `backups/latest-before-web114-diary-subtitle-tap-wording-2026-11-12.json`, and `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-web114-diary-subtitle-tap-wording-2026-11-12.md`; all four were re-fetched and verified readable before editing.
- Source update commit: `6896c4bfc4160c897c744a2f3cd08c87d4073a18`; mirror update commit: `28b229f13464138d79abf3e9047a3fc9b5e5eee7`. Both files have identical Git blob SHA `9ebf5d526731bc57f6ce5b823c5d9d4b5f0aa07b` and 227,890 characters. Post-write re-fetch confirmed exact source/mirror equality and exactly one occurrence of the new phrase.
- Independently computed UTF-8 SHA-256: `ca3f160566a10c62e571689678f84ec55096afa5564bfc9745acbe2300e4aa52`; the SHA implementation passed the standard `abc` test vector. `latest.json` advanced to webVersion `114` with this exact digest. APK remains `1.0.135` / versionCode `134`; no APK rebuild.
- Backup reference / rollback: restore the two HTML files from the matching Web 113 backups and restore `latest.json` from its Web 114 pre-change backup; retain the Register backup as the pre-change record.
- Automated static checks: source/mirror byte identity, exact text count, backup readability, and feed checksum value recorded. GitHub Actions run `43241660297` (run 103) was checked and **failed** at its push step because its checkout was behind the concurrent manual mirror/feed/Register commits (`non-fast-forward`, `fetch first`). The workflow had independently recomputed the same SHA-256 and prepared Web 114 before the push rejection. The final source, mirror, and `latest.json` were then re-fetched and verified consistent; the workflow itself is not marked successful. Physical-device **Me → Check for Updates** test remains pending; do not claim phone verification.


---

# Web Update 115 — Correct Diary subtitle in all supported languages (2026-11-12)

- User corrected the intended wording and asked that the subtitle follow each language already supported by the Diary. The live language dictionary contains exactly three entries: `roman`, `english`, and `hindi`.
- Updated only the `sub` string for those three entries:
  - Roman: `Apne Notes Likhne Aur Search Karne Yaha Tap Kare`
  - English: `Tap here to write and search your notes`
  - Hindi: `अपने नोट्स लिखने और खोजने के लिए यहाँ टैप करें`
- Backups created and re-fetched successfully: `backups/web114-before-diary-subtitle-all-languages-2026-11-12.html`, `backups/diary-web114-before-diary-subtitle-all-languages-2026-11-12.html`, `backups/latest-before-web115-diary-subtitle-all-languages-2026-11-12.json`, and `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-web115-diary-subtitle-all-languages-2026-11-12.md`.
- Source commit: `3a429816e40ab89f0ab5b025829f553a585fae22`. GitHub Actions web-only publish run `43243273460` completed with **success**. Workflow generated/synchronized the mirror and update feed.
- Final re-fetch verified source and `diary-web/index.html` are byte-identical. Verified the three exact language strings above. `latest.json` reports webVersion `115` and web SHA-256 `7ff566dcec4eb114dfbc323cc72aceebf6285d367203e1066866759d2a050cdb`. APK remains `1.0.135` / versionCode `134`; no APK rebuild.
- Scope was limited to the three subtitle strings. No other Diary features, saved notes/photos, PIN/recovery, storage, APK identity, or signing data were changed. Phone-side **Me → Check for Updates** verification is still pending.


---

# Web Update 116 — Localize Diary home screen in all 10 supported languages (2026-11-12)

- User requested that the Diary landing screen follow the selected app language. The screen previously hard-coded My Diary, Private notes, memories and personal writing, and Language / Zaban, even though the app offers 10 languages.
- Added one isolated applyDiaryHomeLanguage() function in web-source/index.html. It translates those three landing-screen strings for Roman English, English, Hindi, Urdu, Arabic, Bengali, Gujarati, Marathi, Tamil, and Telugu. It runs at startup and whenever the language selector or existing language-change/storage events run. Existing language options, app dictionaries, Diary entry button, and direction handling remain intact.
- No Diary feature, button, note/photo data, storage key, PIN/recovery logic, APK, package identity, or signing data was changed.
- Backups created and re-fetched/readable before editing:
  - backups/web115-before-diary-home-language-screen-2026-11-12.html
  - backups/diary-web115-before-diary-home-language-screen-2026-11-12.html
  - backups/latest-before-web116-diary-home-language-screen-2026-11-12.json
  - backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-web116-diary-home-language-screen-2026-11-12.md
- Source commit: 7d545f38a66f4bb2b3d3def4ef29a94f3ec50164. Web-only workflow run 43244545952 completed with success; its publish job and all steps passed.
- Final re-fetch: source and diary-web/index.html are byte-identical, Git blob SHA 00c5dda6f514bf92d39cf81cf0e2c51f47021513. Independently recalculated UTF-8 SHA-256 9899c9df540ca5f845344c151b2f2303c16204c68796752fcbd558eda47515fb; matched the live latest.json value. Live webVersion is 116.
- APK remains 1.0.135 / versionCode 134; no APK rebuild. The 10-language string coverage and workflow/feed integrity were checked. Physical-device language switching is still pending: use Me → Check for Updates, then select each language and confirm the heading, subtitle, and language label change together.


# Web Update 117 — Diary home subtitle wording and bold 3D finish (2026-11-12)

- User requested replacing the Roman home subtitle with the exact wording `Notes, Yadein Aur Apni Baate Likhne Ki Diary`, translating the replacement according to the selected language, and making the subtitle bold with a raised 3D text effect.
- Changed only the localized `subtitle` value in the existing `applyDiaryHomeLanguage()` home-screen copy for the 10 already-supported languages (Roman English, English, Hindi, Urdu, Arabic, Bengali, Gujarati, Marathi, Tamil, Telugu). Added one isolated `diary-home-subtitle-bold-3d` CSS rule targeting only `.diary-home p`; no layout dimensions, language selector, app dictionaries, Diary entry button, notes/photos, storage, PIN/recovery, APK, package identity, or signing files were changed.
- Backups created before editing and re-fetched byte-for-byte/readable:
  - `backups/web-source-index-before-home-subtitle-bold-3d-2026-11-12.html`
  - `backups/diary-web-index-before-home-subtitle-bold-3d-2026-11-12.html`
  - `backups/latest-before-home-subtitle-bold-3d-2026-11-12.json`
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-home-subtitle-bold-3d-2026-11-12.md`
- Source update commit: `15e157562e88e23f49a20b2e7106cc191c753017`. GitHub Actions web-only publish run `43247148040` (run 106) completed with success; the publish job and all listed steps passed. Publisher commit: `91a39248e9478e2765d7a98adab46831673e8c9d`.
- Post-publish re-fetch: `web-source/index.html` and `diary-web/index.html` are byte-identical, Git blob SHA `35cd6fd9c4405bf8fefe2c7ee11490d0e036460e`, UTF-8 size 263,162 bytes. Independently calculated SHA-256 `e30a576cb937251039081d048179f3b6c3cc7a493feae2165463c0e318c495da` matches live `latest.json` `webSha256`; live webVersion is `117`.
- APK remains `1.0.135` / versionCode `134`, package `com.personal.diaryapp`; no APK rebuild. Workflow's web-only HTML/feed verification and JSON validation passed. Static inspection confirmed all 10 subtitle dictionary entries were changed once and the isolated 3D CSS rule appears once. Physical-device visual/language verification is pending; use **Me → Check for Updates**, then check the welcome subtitle in the selected languages. Do not claim phone testing until user confirms.
- Rollback: restore `web-source/index.html` and `diary-web/index.html` from the two Web 116 HTML backups above, and restore `latest.json` from `backups/latest-before-home-subtitle-bold-3d-2026-11-12.json`; retain this Register backup as the pre-entry record.



# Web Update 118 — Bold 3D styling for the Diary entry button (2026-11-12)

- User asked to make the three visible elements of the Diary entry button bold with a 3D effect: 📒 icon, localized “Meri Diary” title, and localized “Apne Notes Likhne Aur Search Karne Yaha Tap Kare” subtitle.
- Before editing, re-fetched and read the Master Register, latest.json, source, and mirror. Source and mirror were identical at Web 117. Created and re-fetched byte-identical backups:
  - `backups/web-source-index-before-diary-entry-bold-3d-2026-11-12.html`
  - `backups/diary-web-index-before-diary-entry-bold-3d-2026-11-12.html`
  - `backups/latest-before-diary-entry-bold-3d-2026-11-12.json`
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-diary-entry-bold-3d-2026-11-12.md`
- Added one isolated CSS block `diary-entry-button-bold-3d` scoped only to `#diaryMyNotesEntry` title, subtitle, and icon. The same selectors apply to all localized text as the existing `installEntry()` replaces title/subtitle according to the selected language. No wording, language dictionary, button dimensions, click handler, note/photo data, storage, PIN/recovery, APK, package identity, or signing files were changed.
- Source commit: `4501656ae40a62cb14c32b06e810f36a4557c352`. GitHub Actions web-only publish run `43248392917` (run 107) completed with **success**; publish job and all steps passed.
- Post-publish re-fetch verified source and `diary-web/index.html` are byte-identical; Git blob SHA `fb2075878ef553b80e4ea05c8e651a8e4d658167`. Live `latest.json` reports webVersion `118` and web SHA-256 `73c38c4b50c32dc6a0cb4a51395fdfe4362cd4345efe85dced274cffb4b20c00`; the successful publish workflow generated the mirror and feed hash after validating the HTML and JSON. APK remains `1.0.135` / versionCode `134`; no APK rebuild.
- Physical phone visual check remains pending. User should open **Me → Check for Updates** and inspect the Diary entry button. Do not claim phone verification.
- Rollback: restore `web-source/index.html` and `diary-web/index.html` from the two HTML backups above and `latest.json` from its backup; this Register backup is the pre-entry record.


# Web Update 119 — Animated tap indicator for the Diary entry (2026-11-12)

- User approved adding a clear tap sign beside the localized **Meri Diary** title. Added one isolated CSS pseudo-element after the title: a small pointing-hand emoji (👆) with a gentle tap/bounce motion. The cue automatically follows the existing localized title in all supported languages; reduced-motion accessibility preference disables the animation.
- No title/subtitle wording, language dictionaries, icon, button size/layout, click handler, notes/photos, storage, PIN/recovery, APK, package identity, or signing data was changed.
- Pre-edit backups created and re-fetched/readable:
  - `backups/web-source-index-before-tap-indicator-2026-11-12.html`
  - `backups/diary-web-index-before-tap-indicator-2026-11-12.html`
  - `backups/latest-before-tap-indicator-2026-11-12.json`
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-tap-indicator-2026-11-12.md`
- Source commit: `fd4b22d01165d747d7545a473f3fd2113b12ad1c`. Web-only publish workflow run `43249661987` (run 108) completed with **success**; all publish job steps passed.
- Post-publish re-fetch verified `web-source/index.html` and `diary-web/index.html` are byte-identical with Git blob SHA `6bedf161736ab417291a560ab683fa7c613b621e`. Independently calculated UTF-8 SHA-256 `01bc624e78f33f8fd8f3596e26f159651bcee9003ca6dea190fb4af3c5372f55` passed the standard `abc` test vector and matches live `latest.json`. Live webVersion is `119`.
- APK remains `1.0.135` / versionCode `134`, package `com.personal.diaryapp`; no APK rebuild or signing operation. Phone-side visual confirmation is pending; use **Me → Check for Updates**, then check that the pointing-hand cue appears beside Meri Diary and gently moves.
- Rollback: restore both HTML files from the two pre-edit HTML backups above and restore `latest.json` from `backups/latest-before-tap-indicator-2026-11-12.json`; retain the Register backup as the pre-change record.


# Web Update 121 — Larger directional tap indicator for the Diary entry (2026-11-12)

- User asked to make the pointing hand larger and aim it toward the localized **Meri Diary** title. Updated the existing isolated tap cue from a small hand after the title to a larger right-pointing hand before the title, with a gentle horizontal nudge animation. For right-to-left title direction, the cue switches to a left-pointing hand so it still points toward the title. Reduced-motion accessibility preference still disables the animation.
- Change is limited to the Diary entry title pseudo-element CSS. No wording, language dictionaries, icon, layout dimensions, button/click behavior, notes/photos, storage, PIN/recovery, APK, package identity, or signing data changed.
- Pre-edit backups created and re-fetched byte-for-byte:
  - `backups/web-source-index-before-larger-right-pointing-cue-2026-11-12.html`
  - `backups/diary-web-index-before-larger-right-pointing-cue-2026-11-12.html`
  - `backups/latest-before-larger-right-pointing-cue-2026-11-12.json`
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-larger-right-pointing-cue-2026-11-12.md`
- Final source commit: `31a5f1cd14dbdce054097ad0ad9e244ec03a7df3`. Final web-only publish workflow run `43250593694` (run 110) completed with **success**; all publish steps passed.
- Post-publish re-fetch: source and `diary-web/index.html` are byte-identical, Git blob SHA `2e24d7aeef5a3bb481686d24c6831a4f2fefdb3e`. Independently calculated UTF-8 SHA-256 `9625b8563152a1883ac934411f3e260c3b07a62ccbf5bf1e492112fbab169648` matches live `latest.json` `webSha256`; live webVersion is `121`.
- APK remains `1.0.135` / versionCode `134`, package `com.personal.diaryapp`; no APK rebuild or signing changes. Physical phone visual confirmation remains pending. Use **Me → Check for Updates** and verify that the larger hand points toward the Diary title in both left-to-right and right-to-left language layouts.
- Rollback: restore both HTML files from the two pre-edit HTML backups above and `latest.json` from `backups/latest-before-larger-right-pointing-cue-2026-11-12.json`; retain the Register backup as the pre-edit record.


# Web Update 122 — Center Diary title directly beneath its icon (2026-11-12)

- User asked to place the localized **Meri Diary** title properly directly under the 📒 icon.
- Added one isolated CSS rule block, `diary-home-icon-title-alignment`, to center the icon and heading on the same vertical axis and reduce the gap between them. The heading remains directly below the icon for all supported languages. No wording, subtitle, language selection, entry button, tap indicator, click behaviour, notes/photos, storage, PIN/recovery, APK, package identity, or signing data changed.
- Backups created before editing and re-fetched/readable: `backups/web-source-index-before-icon-title-alignment-2026-11-12.html`, `backups/diary-web-index-before-icon-title-alignment-2026-11-12.html`, `backups/latest-before-icon-title-alignment-2026-11-12.json`, and `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-icon-title-alignment-2026-11-12.md`.
- Source commit: `34238ca9912be8da672aaac5b03bd09ec2737cd2`. Web-only publish workflow run `43251898462` completed with **success**; checkout, publish verification and final job steps passed.
- Post-publish source and `diary-web/index.html` were re-fetched and verified byte-identical, Git blob SHA `0696ac1c98e44babe1097de5e1119dc85fbd1e10`. Independently computed UTF-8 SHA-256 `1e640d2394f472e18ba1b091b3fc70f0eb3d27f259d361917332ec56f374ebe1` passed the standard `abc` test vector and matches live `latest.json`. Live webVersion is `122`.
- APK remains `1.0.135` / versionCode `134`, package `com.personal.diaryapp`; no APK rebuild or signing operation. Physical-device visual verification is pending: use **Me → Check for Updates** and confirm 📒 and Meri Diary are centered, with the title immediately below the icon.
- Rollback: restore both HTML files from the two pre-edit HTML backups above and `latest.json` from `backups/latest-before-icon-title-alignment-2026-11-12.json`; retain the Register backup as the pre-edit record.


# Web Update 123 — Correct Diary entry button vertical stacking (2026-11-12)

- User reported that Web Update 122 had not changed the visible layout. Inspection confirmed the mistake: the previous CSS targeted the unrelated `.diary-home h1`, while the visible three-line Diary entry is dynamically built inside `#diaryMyNotesEntry` using `.diary-more-icon`, `#diaryMyNotesEntryTitle`, and `#diaryMyNotesEntrySub`.
- Corrected only those actual button children: force the icon, localized Diary title, and subtitle into three separate centered block rows in that exact order, with a small consistent vertical gap. Existing title pointer cue, typography, button dimensions/design, click handler, language translations, notes/photos, storage, PIN/recovery, APK and package identity remain unchanged.
- Before-edit backups were created and verified readable: `backups/web-source-index-before-entry-button-stack-fix-2026-11-12.html`, `backups/diary-web-index-before-entry-button-stack-fix-2026-11-12.html`, `backups/latest-before-entry-button-stack-fix-2026-11-12.json`, and `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-entry-button-stack-fix-2026-11-12.md`.
- Source commit: `c4bd996653d26bb8af2a034f35d74d6c94e72081`. Web-only publish workflow run `43252894674` (run 112) completed with **success**; checkout, publish verification, and final job steps passed.
- Post-publish source and `diary-web/index.html` were re-fetched and verified byte-identical, Git blob SHA `6d73e0464b9e245237afa2cfd574b9be5938f89d`. Independently computed UTF-8 SHA-256 `64e6aac4bf792d777fcd33bba009bc7314a167aa8fc7a628b8b29ce4ab6bf12e` matches live `latest.json`. Live webVersion is `123`.
- APK remains `1.0.135` / versionCode `134`, package `com.personal.diaryapp`; no APK rebuild or signing operation. Physical-device visual verification is still pending. Use **Me → Check for Updates** and confirm the visible button reads icon, title, subtitle vertically.
- Rollback: restore both HTML files from the two pre-edit HTML backups above and `latest.json` from `backups/latest-before-entry-button-stack-fix-2026-11-12.json`; retain the Register backup as the pre-edit record.



# Web Update 124 — Center Diary title beneath icon; move tap cue after title (2026-11-12)

- User reported that the Diary title still did not sit directly below the 📒 icon and specified the intended arrangement: icon on its own top row, localized Diary title centered directly below it, left-pointing 👈 cue after the title on the same line, then the subtitle.
- Inspection confirmed the entry is dynamically built with the icon, title span, and subtitle as direct children of `#diaryMyNotesEntry`. The prior cue was a `::before` inline element, which was included in the centered title line and could visually shift the title away from the icon's center.
- Replaced only the tap-indicator CSS: title now uses its content width and is centered as a flex child directly beneath the centered icon; the old leading hand is suppressed; a left-pointing hand is positioned after the title without participating in title centering. The cue animation and reduced-motion support remain. Subtitle, button dimensions/design, click handler, language text, notes/photos, storage, PIN/recovery, APK, package identity, and signing data are unchanged.
- Before-edit backups were created and verified readable: `backups/web-source-index-before-title-left-hand-after-2026-11-12.html`, `backups/diary-web-index-before-title-left-hand-after-2026-11-12.html`, `backups/latest-before-title-left-hand-after-2026-11-12.json`, and `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-title-left-hand-after-2026-11-12.md`.
- Source commit: `ead8e5976478ecc57964b36280e721d62bb6050b`. Web-only publish workflow run `43254476583` (run 113) completed with **success**.
- Post-publish source and `diary-web/index.html` were re-fetched and verified byte-identical, Git blob SHA `629e5689b7f699469062fe2a7b4d0f238d52bb96`. Live `latest.json` reports webVersion `124` and webSha256 `4ec6b2af000a8fda0377470b9c01d9cc5a9e376bb6bb152d37f58879cda7faee`.
- APK remains `1.0.135` / versionCode `134`, package `com.personal.diaryapp`; no APK rebuild or signing changes. Physical-phone visual confirmation remains pending.
- Rollback: restore both HTML files from the two pre-edit HTML backups above and `latest.json` from `backups/latest-before-title-left-hand-after-2026-11-12.json`; retain the Register backup as the pre-edit record.


# Web Update 125 — Correct Urdu and Arabic Diary tap cue direction and position (2026-11-12)

- User reported that the pointing-hand cue appeared in the wrong place for Urdu and Arabic. Inspection confirmed applyDiaryTextDirection() already sets the document root to dir="rtl" for both languages, but the existing cue always displayed 👈 and used only the LTR placement/animation.
- Added one narrowly scoped RTL CSS override: when the document root is RTL, the cue changes to 👉, moves to the visual left of the title (the end of the RTL title line), and animates rightward toward the title. Roman English, English, Hindi and other LTR layouts retain the existing 👈 cue on the title's right side. The language-direction logic itself was not changed.
- Pre-edit backups were created and re-fetched/readable:
  - backups/web-source-index-before-rtl-tap-cue-fix-2026-11-12.html
  - backups/diary-web-index-before-rtl-tap-cue-fix-2026-11-12.html
  - backups/latest-before-rtl-tap-cue-fix-2026-11-12.json
  - backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-rtl-tap-cue-fix-2026-11-12.md
- Source commit: 795ee75670a96e6ae500fb791121d43f53c1febb. Web-only publish workflow run 43255529653 (run 114) completed with success; checkout, HTML/feed publish, and final job steps passed.
- Post-publish re-fetch verified web-source/index.html and diary-web/index.html are byte-identical, Git blob SHA 6fd73ae538b8c96f7c95935e451a4bbb2d9fe007. Live latest.json reports webVersion 125 and web SHA-256 e138bcde5c96a1fbd4c12baa836999df87b6dec314abb391032a37606c7d3d16. APK remains 1.0.135 / versionCode 134; no APK rebuild.
- No Diary wording, language dictionaries, button click behaviour, notes/photos, storage, PIN/recovery, APK, package identity, or signing data changed. Physical-device visual confirmation remains pending; apply via Me → Check for Updates, then check Urdu and Arabic separately.
- Rollback: restore both HTML files from the two pre-edit HTML backups above and latest.json from backups/latest-before-rtl-tap-cue-fix-2026-11-12.json; retain the Register backup as the pre-edit record.


# Web Update 126 — Anchor Urdu and Arabic hand directly to the title's physical left (2026-11-12)

- User reported that the Urdu/Arabic pointing hand was still in the wrong position and clarified it should sit immediately to the left of the Diary title.
- Inspected the prior RTL rule: using logical inset-inline-end with a positive 100% offset resolved to the wrong physical side in this absolutely positioned pseudo-element. Corrected only the RTL override to use an explicit physical right offset (right: calc(100% + 8px)), anchoring the 👉 hand directly outside the title's left edge. LTR placement remains unchanged.
- Pre-edit source, mirror, feed and register backups were created and re-fetched/readable:
  - backups/web-source-index-before-rtl-cue-left-anchor-fix-2026-11-12.html
  - backups/diary-web-index-before-rtl-cue-left-anchor-fix-2026-11-12.html
  - backups/latest-before-rtl-cue-left-anchor-fix-2026-11-12.json
  - backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-rtl-cue-left-anchor-fix-2026-11-12.md
- Source commit: c41950c79c918f608c0dfd8cbe7a9d9789aa587c. Web-only workflow run 43256323665 (run 115) completed successfully; publish/verification job succeeded.
- Post-publish source and mirror re-fetched with identical Git blob SHA 74c047fec88eba94f0f1a241a94a3910f4fbe1a3. Live feed reports webVersion 126 and webSha256 5478676b8ed740838567af953c7a503183bf8b5edd74379a010001e9ed4bca7d. APK remains 1.0.135 / versionCode 134; no APK rebuild.
- Only the RTL cue anchor was changed. No language text, LTR cue, click handler, notes/photos, storage, PIN/recovery, package identity, APK or signing data changed. Physical-device visual confirmation remains pending; apply via Me → Check for Updates.
- Rollback: restore both HTML files from the two pre-edit HTML backups above and latest.json from backups/latest-before-rtl-cue-left-anchor-fix-2026-11-12.json; retain the Register backup as the pre-edit record.


# Web Update 127 — complete translation coverage audit across all 10 Diary languages (2026-11-12)

- User requested checking every language so all visible Diary wording matches its selected language, and completing any remaining translation work.
- Read the live Register and latest.json. The Register header still showed stale 126/126 values; the live feed was authoritative and showed APK 1.0.135 / versionCode 134 and webVersion 127. Corrected the header above and recorded the discrepancy here.
- Audited the translation dictionaries in web-source/index.html: Roman English, English, Hindi, Urdu, Arabic, Bengali, Gujarati, Marathi, Tamil and Telugu. The shared English dictionary contains 129 translation keys. All 10 language dictionaries now explicitly cover all 129 keys; no base translation keys are missing.
- The only remaining inherited-English strings found in the seven non-Latin-script dictionaries were recoveryPinPrompt and recoveryVerify. Added localized wording for these two recovery prompts in Urdu, Arabic, Bengali, Gujarati, Marathi, Tamil and Telugu. PIN remains as the technical acronym where appropriate. Existing translated wording and the other 127 labels/messages were left unchanged.
- Pre-edit backups were created and verified readable:
  - backups/web-source-index-before-all-language-audit-fix-2026-11-12.html
  - backups/diary-web-index-before-all-language-audit-fix-2026-11-12.html
  - backups/latest-before-all-language-audit-fix-2026-11-12.json
  - backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-all-language-audit-fix-2026-11-12.md
- Translation source commit: c3965cf497bacc66a255570f3d6864f621fef363. Web publish workflow run 43262992695 completed successfully; all publish job steps passed. The workflow published webVersion 127 and did not rebuild the APK.
- Post-publish source and diary-web/index.html were re-fetched and are byte-identical; both Git blob SHA: ffd03bfece972a5f51ea1b9a6179d9858076b541. Independently computed UTF-8 SHA-256: 7340af8197aca28e59dc20d3f75d4b0901fea18d518edea94a174cae2e1bd8e3, exactly matching live latest.json webSha256.
- Live feed remains APK 1.0.135 / versionCode 134, package com.personal.diaryapp; APK URL and APK SHA-256 unchanged. No APK rebuild, signing change, storage/data change, PIN/recovery logic change, or feature/UI redesign.
- Physical-device verification remains pending. User should install Web Update 127 through Me → Check for Updates, then select each of the 10 languages and review the Diary home screen, note editor, search, buttons, PIN/recovery prompts and recently-deleted messages. Do not claim phone-side verification until the user confirms.
- Rollback: restore both HTML files from the two pre-edit HTML backups above and latest.json from backups/latest-before-all-language-audit-fix-2026-11-12.json; retain the Register backup as the pre-edit record.


# Web Update 131 — full My Diary UI language audit and localization pass (2026-11-12)

- User requested a detailed check of the entire Diary so every visible section and message follows the selected language, and any remaining work be completed.
- Starting live state: Web Update 127; APK 1.0.135 / versionCode 134; package com.personal.diaryapp. Scope was web-only localization. No APK, Android native source, package identity, signing, storage keys, note/photo data, PIN/recovery logic, or feature behaviour was changed.
- Created and verified readable pre-edit backups:
  - backups/web-source-before-full-language-audit-2026-11-12.html
  - backups/diary-web-before-full-language-audit-2026-11-12.html
  - backups/latest-before-full-language-audit-2026-11-12.json
  - backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-full-language-audit-2026-11-12.md
- Re-audited all 10 language dictionaries and all 129 shared base translation keys. The seven non-Latin-script dictionaries had no remaining exact English-value fallbacks in the audited base strings; PIN remains an intentional technical acronym and My Diary remains the app name.
- The full-screen scan found additional UI strings outside the main dictionary that had remained in English/Roman text. Added 15 localized labels/messages to all 10 languages: Me menu, Check for Updates, Refresh, refresh success/failure, update-unavailable message, Share App, Calendar, Calendar accessibility label, previous/next month, empty-day message, note-count text, 4-digit PIN placeholder, and Open Diary accessibility label.
- Matched the welcome-screen subtitle in every language to that language's actual Diary entry-button subtitle. Restored the user's requested Roman wording exactly: “Apne Notes Likhne Aur Search Karne Yaha Tap Kare”.
- Calendar month, weekday names, selected date, note dates, calendar day numbers and note counts now use the selected app language/locale, including localized numerals where supported. The calendar's note-empty message and month navigation labels are localized.
- Improved 17 Roman-English labels that were still English-only (including pin/unpin, share, cover/detail photo, edit/delete, backup/restore, copy, lock/unlock, forgot PIN and PIN copy). Also localized Roman font-size/category/recovery/storage wording. Corrected the English dictionary's Remove Note and Category labels so English no longer displays Roman wording.
- Scanned remaining direct UI text assignments and common hardcoded labels. Remaining literal strings found by the scan are language-neutral formatting controls/symbols (B/I/U, px, ×), blank status resets, and the language names in the language selector; no further user-facing hardcoded English button, calendar, or error strings were found in the audited paths.
- Source commits in this localization pass: 8ab020948f9fc343a70865d18668c4a643821be5, b477d41c0205ab3e846358490e9c2c94d4d532ad, 65279bbb2192781689f65d2563ab3519521d3d08, and final source commit 78f84a9f97bbe645c012eb78b156c6e5801047a6. Final web-only publish workflow run 43267249602 completed successfully; all job steps passed.
- Post-publish verification: web-source/index.html and diary-web/index.html are byte-identical, Git blob SHA 02dc650f334c14197d2ec36c6418928f365722bb. Independently computed exact UTF-8 SHA-256 29139113be913ace26d740a77572617d52b48e9f35d96b1eae56eb52941173c matches live latest.json.webSha256. Live feed reports webVersion 131.
- APK remains 1.0.135 / versionCode 134, package com.personal.diaryapp; APK URL and APK SHA-256 c3e312ec7cd8504bab68c12f9df996c8d10018670d0d1ccef9373408d4ddba4d are unchanged. No APK rebuild or signing operation occurred.
- Automated/source audit and publishing are complete; physical-device visual and native-speaker wording review remain pending. User should apply Web Update 131 using Me → Check for Updates and inspect all 10 language selections, including Diary home, note editor, search, Me menu, Calendar, Recently Deleted, note lock, Diary PIN/recovery, backup/restore, and error messages. Do not claim phone-side testing until user confirms.
- Rollback: restore web-source/index.html and diary-web/index.html from the two pre-edit HTML backups above and latest.json from backups/latest-before-full-language-audit-2026-11-12.json; retain the Register backup as the pre-edit record.


---

# My Diary 1.0.136 / Web Update 133 — One-press Android Back exits the whole Diary (2026-11-12)

- User request: from any nested Diary section, one Android Back press must close the complete Diary and return to the screen underneath; users should not have to press Back repeatedly to unwind Diary navigation.
- Starting live state: APK **1.0.135 / versionCode 134**, webVersion **132**, package `com.personal.diaryapp`; starting main commit `2effcdd79bc4375a5f018afac014b88c13e3d8ff`.
- Scope: only the Diary overlay close callback, native Android Activity Back handling generated by `scripts/add_diary_app_actions.py`, and the APK build workflow/version metadata. The supplied Android project ZIP, unrelated screens, note editor, note data/storage, photos, PIN/recovery records, permissions, package identity and signing identity were not changed.
- Behaviour change:
  - `web-source/index.html` exposes `window.__diaryCloseOverlayFromAndroid`; when the Diary overlay is open, it calls the existing `closeOverlay(true)` path to close the whole overlay directly without stepping backward through nested in-Diary history.
  - `scripts/add_diary_app_actions.py` updates the native `onBackPressed()` handler to ask that callback first. If the Diary is open, it closes the complete overlay and clears the single-page WebView's nested history. If the Diary is not open, the existing WebView history / Activity Back behaviour is retained.
- Verified pre-edit backups on branch `backup/pre-one-press-diary-exit-2026-11-12`:
  - `backups/web-source-before-one-press-diary-exit-2026-11-12.html`
  - `backups/add_diary_app_actions-before-one-press-diary-exit-2026-11-12.py`
  - `backups/build-diary-from-zip-before-one-press-diary-exit-2026-11-12.yml`
  - `backups/latest-before-one-press-diary-exit-2026-11-12.json`
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-one-press-diary-exit-2026-11-12.md`
- Web publication: Web Update **133**, workflow run **43276059809**, completed successfully. Source and published mirror are byte-identical; both Git blob SHA `81c75f34835dd7d51cac6da32b7e6729f6380aaf`. Independently recalculated UTF-8 SHA-256 `3cb78b3dc27621fa277323b4c5eec729fe60a1adc80921290795be17268116bd` matches live `latest.json.webSha256`.
- APK publication: workflow run **43276194581**, completed successfully. Debug build, signed Release build, certificate check, publish step and artifact uploads all passed. The release certificate matched the previously trusted SHA-256 fingerprint `23A4E93F3C7911DCE18389EA583548700C6AD6A3759707F1CD222D07E2408B5A`.
- Live feed now reports APK **1.0.136 / versionCode 135**, webVersion **133**, package `com.personal.diaryapp`, APK URL `https://raw.githubusercontent.com/amuazzinxyz-ops/My-Diary-Updates/main/My-Diary-1.0.136.apk`, APK SHA-256 `6fc74ca82888fed4121cc352c1846ec8c6a7063e2d2a33fbe032726f7a244348`. The signed workflow artifact was downloaded and independently hashed; it exactly matches the live feed checksum.
- Post-publish checks: source and mirror re-fetched and confirmed identical; feed package/version/URL/hash checked; backup files re-fetched and confirmed readable. No APK signing secret or keystore was changed.
- Phone verification remains **pending**. User should apply APK **1.0.136** through the existing **Me → Check for Updates** path, then open Diary, enter nested sections such as note editor / Me / Recently Deleted, and press Android Back once. Confirm that the entire Diary closes immediately and returns to the underlying screen. Do not claim physical-device testing until user confirms.
- Rollback reference: backup branch above; pre-change main commit `2effcdd79bc4375a5f018afac014b88c13e3d8ff`; pre-change web feed backup listed above. Preserve all user data; do not clear app data or uninstall as a rollback shortcut.


---

# Web Update 136 — Add colour choices inside all three existing image buttons (2026-11-13)

- User request: keep the existing Image Select buttons (no separate Colour Select button); when tapped, each existing button should offer both image selection and colour selection.
- Starting live state: APK **1.0.136 / versionCode 135**, webVersion **133**, package `com.personal.diaryapp`. Live `latest.json` was read before editing.
- Scope: web-only Diary editor, saved-note rendering, import compatibility and share-image rendering. No native Android source, APK, package identity, signing identity, storage keys, PIN/recovery logic, updater logic, or unrelated screens were changed.
- Added the same in-button chooser to all three existing controls: **Note Cover Photo**, **Details Image**, and **Photo Lagayein**. Each offers **Choose Image**, **Solid Colour**, or **Gradient Colour** (two independently selectable colours). No separate top-level colour button was added.
- Selected cover/detail colours are layered over the chosen image (without replacing it), or used as a background when no image is selected. The attached-photo colour is shown as a frame around the photo. Colour settings are saved with each note, restored when editing, retained in note backup import/export, shown on saved notes, and included in the composed share image.
- Added localized chooser labels for all 10 supported languages: Roman English, English, Hindi, Urdu, Arabic, Bengali, Gujarati, Marathi, Tamil and Telugu.
- Backups were created and re-fetched/readable on branch `backup/pre-image-button-colour-options-2026-11-13`:
  - `backups/web-source-before-image-button-colour-options-2026-11-13.html`
  - `backups/diary-web-before-image-button-colour-options-2026-11-13.html`
  - `backups/latest-before-image-button-colour-options-2026-11-13.json`
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-image-button-colour-options-2026-11-13.md`
- Final source commit: `ccfafe5425b5765e47d1ce96270e70a99586c0a7`. Web-only publisher workflow run **43366404020** (run 126) completed with **success**. An intermediate syntax issue in an earlier attempt was corrected before the final successful run; the final embedded scripts both parse successfully.
- Post-publish verification: `web-source/index.html` and `diary-web/index.html` are byte-identical; both Git blob SHA `c150cb5c0777f1b2e84c0fac96ee477c5b5b782f`. Independently computed UTF-8 SHA-256 `cce2170ace3f45721a5ddd8ebc79b1908d5119fce636941256c8f24be2903c93` matches live `latest.json.webSha256`. Live webVersion is **136**.
- APK remains **1.0.136 / versionCode 135**, package `com.personal.diaryapp`; APK URL, checksum, certificate and signing identity are unchanged. No APK rebuild or signing operation occurred.
- Static checks passed: both inline scripts parse; SHA-256 implementation passed the standard `abc` test vector; all 10 language dictionaries contain the new chooser labels; source/mirror/feed checks passed. Actual Android phone interaction and visual verification remain **pending**.
- Phone test: use **Me → Check for Updates**. In a new note, tap each of the three existing image buttons. Confirm its menu offers image, solid colour and gradient; choose colours, attach images, save, reopen/edit, and share the note. Also check an older note to confirm its existing images still display normally. Do not claim phone-side testing until the user confirms.
- Rollback: use the backup branch and the exact pre-change HTML, feed and Register files listed above; preserve all local notes and app data.


---

# Web Update 137 — Purpose-specific design panels inside the three image buttons (2026-11-13)

- User clarified that the three existing image buttons should open attractive, clearly explained panels, with the image and colour choices visible inside each panel.
- Starting live state: APK **1.0.136 / versionCode 135**, webVersion **136**, package `com.personal.diaryapp`. Read the live feed and Master Register before editing.
- Scope: web-only Diary image-picker panel UI, localized labels/descriptions and related CSS. No native Android source, APK, package/signing identity, updater logic, note storage keys, PIN/recovery logic, or unrelated features were changed.
- All three existing controls now open a purpose-specific premium-style panel:
  1. **Note Cover Photo** — explains that it decorates the note-name/title box.
  2. **Details Image** — explains that it decorates the writing/details box.
  3. **Photo Lagayein / Attach Photo** — explains that it attaches a separate photo to the note and styles its frame.
- Each panel displays **Choose Image**, **Solid Colour**, and **Gradient Colour** choices within the same panel. No separate Colour button or extra image button was added. Existing colour selection and persistence logic from Web Update 136 remains in place.
- Added panel headings and explanatory descriptions for all 10 supported languages: Roman English, English, Hindi, Urdu, Arabic, Bengali, Gujarati, Marathi, Tamil and Telugu.
- Verified pre-edit backups on branch `backup/pre-image-button-pamphlet-panels-2026-11-13`:
  - `backups/web-source-before-image-button-pamphlet-panels-2026-11-13.html`
  - `backups/diary-web-before-image-button-pamphlet-panels-2026-11-13.html`
  - `backups/latest-before-image-button-pamphlet-panels-2026-11-13.json`
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-image-button-pamphlet-panels-2026-11-13.md`
- Source change commit: `7e042007a60e0db45d140cbf117430fbe0bb34c5`. Web-only workflow run **43367264608** (run 127) completed successfully.
- Post-publish verification: source and mirror are byte-identical; both Git blob SHA `fe20d5c8e6f15e6790cdfd75a86b81026b5aa461`. Independently calculated UTF-8 SHA-256 `113d77a5e1aa74d0358f978dfa71583bfdf806128b15ff16fdb9b6cbd419ad9d` exactly matches live `latest.json.webSha256`; live webVersion **137**.
- Both inline scripts parse successfully. All 10 language dictionaries contain the seven panel heading/description labels.
- APK remains **1.0.136 / versionCode 135**, SHA-256 `6fc74ca82888fed4121cc352c1846ec8c6a7063e2d2a33fbe032726f7a244348`; no APK rebuild or signing operation occurred.
- Phone-side visual and interaction testing remains **pending**. Use **Me → Check for Updates**, tap each of the three existing buttons, and confirm the correct purpose panel and its three choices appear. Test image selection and colour selection in each panel.
- Rollback: use the verified backup branch and exact pre-change files listed above. Preserve all local notes, photos and app data.


---

# Web Update 138 — Separate ready-made pamphlet chooser in all three Diary image panels (2026-11-13)

- User clarified that the requested pamphlet choice must be a **separate option**, not merely the existing image/colour controls. User approved proceeding.
- Starting live state: APK **1.0.136 / versionCode 135**, webVersion **137**, package `com.personal.diaryapp`. Live `latest.json` and Master Register were read before editing.
- Scope: web-only `web-source/index.html`; the existing publisher synchronizes `diary-web/index.html` and updates `latest.json`. No native Android source, APK, package/signing identity, updater logic, note storage keys, PIN/recovery logic, or unrelated features changed.
- Added a distinct **Pamphlet Chunein / Choose Pamphlet** option inside each of the three existing image panels: Note ka Cover Photo, Details Image, and Photo Lagayein. The option opens a separate ready-made design gallery with four selectable presets: Royal Gold, Purple Bloom, Emerald Garden and Ocean Blue. Selecting a preset applies its two-colour gradient to the relevant existing cover field, details field, or attached-photo frame.
- Existing **Choose Image**, **Solid Colour**, and **Gradient Colour** options remain available and unchanged. No new top-level editor button was added; the pamphlet option is inside each existing panel. All six new labels were translated in all 10 supported languages.
- Pre-edit backup branch: `backup/pre-pamphlet-chooser-2026-11-13`. Verified readable backup files:
  - `backups/web-source-before-pamphlet-chooser-2026-11-13.html`
  - `backups/diary-web-before-pamphlet-chooser-2026-11-13.html`
  - `backups/latest-before-pamphlet-chooser-2026-11-13.json`
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-pamphlet-chooser-2026-11-13.md`
- Source commit: `2ad2a044f7fd7bce0b44164b4fa24fc823ac73e1`. Web-only publisher workflow run **43368466848** (run 128) completed successfully.
- Post-publish verification: source and published mirror were re-fetched and have identical Git blob SHA `5cb65a2706d3e9165c05da43bbb8d75d8126ddc5`. Independently calculated SHA-256 over the exact UTF-8 source bytes: `01804fe61c88983e57833809fbcad705c2da75fc3ee88a948184c59420e064c3`, matching live `latest.json.webSha256`. Live webVersion **138**.
- Both inline scripts parse successfully. Each of the six new translation keys is present in all 10 language dictionaries. SHA-256 implementation was checked against the standard `abc` test vector. APK remains **1.0.136 / versionCode 135**, APK hash and package identity unchanged; no APK rebuild or signing operation.
- Physical-device visual and interaction verification remains **pending**. Use **Me → Check for Updates**, then open each of the three image panels, tap **Pamphlet Chunein**, choose each preset, and confirm it styles the intended field/photo frame. Also confirm the existing image, solid-colour and gradient-colour choices still work.
- Rollback: use the verified backup branch and exact pre-change files listed above. Preserve all local notes, photos and app data.


---

# Web Update 140 — Actual decorative ready-made pamphlet templates (2026-11-13)

- User clarified that “pamphlet” means fully designed, ready-made decorative templates commonly offered in other apps, not simple colour swatches or two-colour gradients. Replaced the previous four gradient swatches with real visual template previews and selectable designs.
- Starting feed before this task: APK **1.0.136 / versionCode 135**, webVersion **138**, package `com.personal.diaryapp`. This live Register, feed and current source were read before editing.
- Scope: web-only `web-source/index.html`; publisher synchronizes `diary-web/index.html` and updates `latest.json`. No native Android source, APK, package/signing identity, updater logic, note storage keys, PIN/recovery logic, or unrelated screens were changed.
- Each existing image button retains its own separate `Pamphlet Chunein` option and its own purpose-specific ready-made gallery:
  - **Note ka Cover Photo:** Floral, Islamic, Classic and Nature title-cover designs.
  - **Details Image:** Paper, lined writing page, Islamic and Nature writing-area designs.
  - **Photo Lagayein:** Polaroid, Royal, Floral and Modern photo-frame designs.
- Each gallery displays a miniature decorated layout preview, ornamentation, border and sample typography—not just a colour tile. Selecting a template applies the decorative background/frame to its matching editor field or attached photo.
- Template IDs are safely whitelisted and retained by the existing `cleanDiaryColour` normalization. Therefore selected template styling is saved with the note, restored when editing, carried through the existing note backup import/export path, applied to saved-note previews and reflected in the composed share artwork. Existing Choose Image, Solid Colour and Gradient Colour controls remain available.
- Added localized template chooser headings and four style labels in all 10 supported languages: Roman English, English, Hindi, Urdu, Arabic, Bengali, Gujarati, Marathi, Tamil and Telugu.
- Backups were created and readable on branch `backup/pre-real-pamphlet-templates-2026-11-13`:
  - `backups/web-source-before-real-pamphlet-templates-2026-11-13.html`
  - `backups/diary-web-before-real-pamphlet-templates-2026-11-13.html`
  - `backups/latest-before-real-pamphlet-templates-2026-11-13.json`
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-real-pamphlet-templates-2026-11-13.md`
- Final source commit: `85711d1aee91d364fce973dda0e4f02f0be27c0f`. Final web-only publishing workflow run **43369439756** (run 130) completed successfully. An earlier publish for the same task was superseded by a small canvas-rendering correction; run 130 is the final source version.
- Post-publish verification: source and mirror were re-fetched and have identical Git blob SHA `330c27bf9d12f50dcf06cab8be828e038a2ca20f`. Both inline JavaScript scripts parse successfully. Each of the six new chooser/label translation keys is present in all 10 language dictionaries. There are 12 distinct purpose-specific template choices across the three galleries.
- Independently computed SHA-256 over exact UTF-8 source bytes: `8188d5d65d9dd04393e49c0e85b400a0b18904f9c4c0b38ec091c1018f8050d6`, matching live `latest.json.webSha256`. Live webVersion **140**.
- APK remains **1.0.136 / versionCode 135**, checksum, URL and package unchanged; no APK rebuild or signing operation.
- Physical-device visual/interaction testing remains **pending**. User should use **Me → Check for Updates**, then open each of the three existing image buttons and inspect its distinct gallery, select a template, save/reopen the note, and test the existing image/solid/gradient options. Do not claim phone-side testing until user confirms.
- Rollback: use the backup branch and exact pre-change files listed above. Preserve all local notes, photos and app data.


---

# Web Update 142 — Finger drag and pinch-to-zoom image adjustment (2026-11-13)

- User approved touch adjustment for all three existing Diary image areas: Note Cover Photo, Details Image and attached Photo.
- Starting live state: APK **1.0.136 / versionCode 135**, webVersion **140**, package `com.personal.diaryapp`. Read the live source, feed and Master Register before editing.
- Scope: web-only Diary editor and note preview/share rendering in `web-source/index.html`; the publisher synchronized `diary-web/index.html` and updated `latest.json`. No APK, native Android code, package/signing identity, PIN/recovery logic, updater logic, or unrelated feature was changed.
- Added a separate **Ungli se Adjust Karein / Adjust with Finger** control inside each of the three existing image panels. When enabled, one finger drags the image to reposition it and two fingers pinch to zoom (up to 3×). Tap the control again to finish. The editor remains normally editable when adjustment mode is off.
- The crop position and zoom values are stored in the existing per-note cover/detail/photo colour settings, normalized safely for older notes, and restored when a note is reopened. The same crop is used in saved-note previews and the composed share image. Existing decorative pamphlet templates, image selection, solid colour and gradient colour choices remain in place.
- Added the adjustment button and usage hint in all 10 supported languages: Roman English, English, Hindi, Urdu, Arabic, Bengali, Gujarati, Marathi, Tamil and Telugu.
- Verified pre-edit backups on branch `backup/pre-finger-adjustment-2026-11-13`:
  - `backups/web-source-before-finger-adjustment-2026-11-13.html`
  - `backups/diary-web-before-finger-adjustment-2026-11-13.html`
  - `backups/latest-before-finger-adjustment-2026-11-13.json`
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-finger-adjustment-2026-11-13.md`
- Source commits: `b633b0967e98c6832afe031b1dafa05705560533` and final refinement `2d78e2b27e31c0f4d73bd273e744de62c75696a6`. Final web-only publisher workflow run **43372607691** completed successfully; all publish job steps passed. The preceding publish run **43372558034** also completed successfully; final source is the later commit above.
- Post-publish verification: `web-source/index.html` and `diary-web/index.html` are byte-identical; Git blob SHA `b9a7a01e1f226de50d01741ba8c5efa8eaa47663`. Both embedded JavaScript scripts parse successfully. All 10 language dictionaries contain the adjustment button text. Checks confirm the pointer drag/pinch handlers, saved crop data, new-note reset and all 12 existing pamphlet templates remain present.
- Live feed reports webVersion **142** and web SHA-256 `6d7ba9eaa51e60642d1176abc7278d46a58aaa76d1e7105446405c356d835101`. APK remains **1.0.136 / versionCode 135**, URL, SHA-256 and package unchanged; no APK rebuild or signing operation.
- Physical-device touch/visual testing remains **pending**. Use **Me → Check for Updates**, open each of the three image panels, choose an image or pamphlet, tap **Ungli se Adjust Karein**, drag with one finger and pinch with two fingers. Save and reopen the note and verify the crop remains. Do not claim phone-side testing until the user confirms.
- Rollback: use the backup branch and exact pre-change files listed above. Preserve all local notes, photos and app data.


---

# Web Update 143 — Android touch drag and pinch adjustment repair (2026-11-13)

- User reported that the finger-adjust button activated and the image appeared, but the image stayed fixed and could not be moved by touch.
- Starting live state: APK 1.0.136 / versionCode 135; webVersion 142; source commit `4b8e2829e4f374881d0ba6b47615a40acd2befee`. Live `latest.json` was authoritative; the stale status line above previously said webVersion 140 and has now been corrected to 143.
- Scope: web-only; changed only `bindDiaryFingerAdjust(target,kind)` in `web-source/index.html`. Added native Touch Events for Android touch dragging and two-finger pinch zoom; retained mouse/pen Pointer Events. Touch movement is handled at document level so dragging continues if the finger moves beyond the image/input boundary. Existing position/zoom state and paint functions remain in use.
- Explicitly untouched: pamphlet designs/chooser, image selection, editor layout, notes/photos data, save format, PIN/lock/recovery, language dictionaries, native Android source, APK, package identity, signing data and all other features.
- Pre-edit backup branch: `backup/pre-finger-drag-fix-2026-11-13`. Verified backup files:
  - `backups/web-source-before-finger-drag-fix-2026-11-13.html`
  - `backups/diary-web-before-finger-drag-fix-2026-11-13.html`
  - `backups/latest-before-finger-drag-fix-2026-11-13.json`
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-finger-drag-fix-2026-11-13.md`
- Source change commit: `20376daa52c530163f1085a648d4a4b54b146f7b`. Web publisher workflow run `43378304747` (run 133) completed with **success**.
- Post-publish verification: source and published mirror are byte-identical, both Git blob SHA `98d759b0b8b7637058affbba9307701bfd45d2ed`; independently calculated UTF-8 SHA-256 `745d8e5fb5d794fac62f613d0783b6f20bf208a8c22e0060b86d231f531bd7c1` matches live `latest.json.webSha256`; live webVersion is 143.
- APK remains `1.0.136` / versionCode `135`; no APK rebuild or signing operation. Phone-side drag/zoom test is **pending**; do not claim device testing until user confirms.
- Rollback: restore the verified pre-edit files from `backup/pre-finger-drag-fix-2026-11-13` if phone testing identifies a regression.


---

# Web Update 144 — Multi-finger pinch zoom repair (2026-11-13)

- User confirmed one-finger image dragging worked after Web Update 143, but two-/three-finger pinch zoom and zoom-out did not work.
- Starting live state: APK 1.0.136 / versionCode 135; webVersion 143; starting source commit `ddd716f1ba3d8e88b1ee911f8bc4bd4c8d79afd6`.
- Scope: web-only; replaced only `bindDiaryFingerAdjust(target,kind)` in `web-source/index.html`. Android touch-capable Pointer Events now handle each active pointer ID; legacy Touch Events remain as fallback. Pinch span is calculated from all active fingers around their centre, so two or three fingers can scale the image. Gesture baselines reset when fingers are added/removed to avoid jumps; one-finger drag is retained.
- Explicitly untouched: pamphlet designs/chooser, image selection, layout, note/photo storage, save format, PIN/lock/recovery, language dictionaries, native Android code, APK, package/signing identity, and unrelated features.
- Pre-edit backup branch: `backup/pre-pinch-zoom-fix-2026-11-13`. Verified readable backups:
  - `backups/web-source-before-pinch-zoom-fix-2026-11-13.html`
  - `backups/diary-web-before-pinch-zoom-fix-2026-11-13.html`
  - `backups/latest-before-pinch-zoom-fix-2026-11-13.json`
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-pinch-zoom-fix-2026-11-13.md`
- Source commit: `0d576d9fe53c580416febbfcee3eaac4349b0316`. Web publisher workflow run `43378989369` (run 134) completed successfully.
- Post-publish: source and mirror byte-identical; blob SHA `0f7b9e3fb63b974b0906ab92344060ec0463029b`; independently calculated UTF-8 SHA-256 `375ee8fd55eb2ce15e9d5065638e5b70f451df7a0fd7827cf9aaeaa1ee7240d2` matches live feed. Live webVersion `144`.
- APK remains `1.0.136` / versionCode `135`; no APK build/signing change. Physical phone pinch test is **pending**; do not claim device confirmation until user tests.
- Rollback: restore the exact pre-edit files from `backup/pre-pinch-zoom-fix-2026-11-13` if testing reveals regression.

---

# Web Update 145 — Two-axis image movement and Android multi-touch repair (2026-11-13)

- User reported after Update 144 that an image could move only vertically; horizontal movement and pinch zoom/zoom-out still did not work.
- Starting live state: APK 1.0.136 / versionCode 135; webVersion 144; source blob 0f7b9e3fb63b974b0906ab92344060ec0463029b. Re-read the live register, feed, source and mirror before editing.
- Scope: web-only. Changed the finger-adjust image painting/gesture functions, image background sizing in the existing field-image renderer, the existing zoom-value clamp, and the existing pamphlet-template CSS override in web-source/index.html. No other Diary feature was changed.
- Repair details: Android now uses native Touch Events for one-, two- and three-finger gestures even on browsers that also support Pointer Events; mouse/pen Pointer Events remain. Uploaded field images are sized with overflow on both axes so horizontal and vertical repositioning are possible. Background position and size are applied with CSS priority so the template rule cannot override image adjustment. Pinch zoom range now allows zoom-out to 0.8 and zoom-in up to 4×. Image dimensions are cached for adjustment rather than reloaded on every move.
- Pre-edit backup branch: backup/pre-two-axis-adjust-fix-2026-11-13. Backups created and readable:
  - backups/web-source-before-two-axis-adjust-fix-2026-11-13.html
  - backups/diary-web-before-two-axis-adjust-fix-2026-11-13.html
  - backups/latest-before-two-axis-adjust-fix-2026-11-13.json
  - backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-two-axis-adjust-fix-2026-11-13.md
- Source commit: 28cbd549a61bd92c9417b125e4a41f14691f726a. Web publisher workflow run 43379560399 (run 135) completed with success; publish job and all listed steps succeeded.
- Post-publish verification: web-source/index.html and diary-web/index.html are byte-identical; both Git blob SHA c1417ddb7b940f922b98b034dee9a226da7926ba. Live feed reports webVersion 145 and web SHA-256 bc3fb24aecf6af0abe06fa1b27ff90042fb1eac769d798e568630d71fa9fb165. The live feed was re-fetched after publishing.
- APK remains 1.0.136 / versionCode 135; APK URL, SHA-256 and package identity unchanged. No APK rebuild or signing operation.
- Physical-device testing is pending. The user must install Web Update 145 through Me → Check for Updates, then test horizontal and vertical drag, two-finger pinch-in/zoom-out and pinch-out/zoom-in on a Cover image, Details image and attached Photo. Do not claim phone-side confirmation until the user reports the results.
- Rollback: restore the exact pre-edit files from backup/pre-two-axis-adjust-fix-2026-11-13. Preserve all local notes, photos, PIN data and app data.
---

# Web Update 146 — Horizontal drag and multi-touch capture repair (2026-11-13)

- User reported the same failure after Web Update 145: image moved only vertically; horizontal drag and pinch zoom/zoom-out did not work. Do not treat the user's phone-side test as passed.
- Re-read the current live register, latest.json, source and mirror before editing. Starting live state: webVersion 145; APK 1.0.136 / versionCode 135.
- Changed only bindDiaryFingerAdjust in web-source/index.html. The new handler captures touchstart at document capture phase and registers additional fingers by checking whether their coordinates are within the active image/field bounds. This avoids relying on the second finger's event target matching the first finger's target. Pinch span is recalculated when finger count changes.
- Horizontal and vertical drag now convert pointer pixel movement into CSS background-position percentage using the actual image overflow dimensions, rather than scaling by the full field width/height. This addresses the very small horizontal shift when the image only overflows the field slightly. Attached Photo transform drag is retained.
- Pre-edit backup branch: backup/pre-horizontal-drag-pinch-repair-2026-11-13. Backups created and readable:
  - backups/web-source-before-horizontal-drag-pinch-repair-2026-11-13.html
  - backups/diary-web-before-horizontal-drag-pinch-repair-2026-11-13.html
  - backups/latest-before-horizontal-drag-pinch-repair-2026-11-13.json
  - backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-horizontal-drag-pinch-repair-2026-11-13.md
- Source commit: 08819ff9c8fd2285c7fdc0f450409a875ee13610. Publisher workflow run 43379986888 (run 136) completed with success.
- Post-publish verification: source and mirror are byte-identical; both Git blob SHA 6cc67040b3c3ecc20440b457a4eca7c9e4103d6f. Live feed reports webVersion 146 and web SHA-256 9c3aacda52194dc8d1ebe25b3cdbb1b043c7ef48fce78768ae15d5ab80d83471.
- APK unchanged at 1.0.136 / versionCode 135; no APK rebuild or signing operation.
- Physical-device testing remains pending. Ask user to install Web Update 146 through Me → Check for Updates and test left/right drag, up/down drag, two-finger pinch-in and pinch-out. Do not claim phone-side success until user confirms.
- Rollback: restore exact pre-edit files from backup/pre-horizontal-drag-pinch-repair-2026-11-13. Preserve all local notes, photos, PIN data and app data.

---

# Web Update 148 — Correct layered background image adjustment (2026-11-13)

- User reported that after Web Update 146, the image still moved only vertically; horizontal drag and two-finger zoom in/out did not work. The “Diary pehle se update hai” message was traced to the installed HTML SHA matching the live web bundle, not to the APK version.
- Re-inspected the current live Master Register, latest.json, web source and published mirror. Starting state: APK 1.0.136 / versionCode 135; webVersion 146; source/mirror blob SHA 6cc67040b3c3ecc20440b457a4eca7c9e4103d6f.
- Root cause found in the actual field-image renderer: each field photo is painted as multiple CSS background layers (optional tint, dark overlay, and the photo). The adjustment code was not explicitly separating the fixed overlay layers from the movable/zoomable photo layer. The repair now computes matching per-layer background-position, background-size, and background-repeat lists: overlays stay fitted to the field while only the actual photo layer receives its saved position and zoom. The same helper is used by initial image rendering and live finger adjustment.
- Scope: web-only; changed only web-source/index.html in two sequential commits: d6826be5e4eedd123f33938190bb93e23c3e81fe (initial layer separation) and 517faeb7a2671a8e165346944d52afd4e7e368c4 (per-layer repeat alignment). No APK rebuild, native Android change, data/storage key change, note/photo/PIN change, or unrelated UI change.
- Pre-edit backup branch: backup/pre-layered-background-adjust-repair-2026-11-13. Verified readable backups:
  - backups/web-source-before-layered-background-adjust-repair-2026-11-13.html
  - backups/diary-web-before-layered-background-adjust-repair-2026-11-13.html
  - backups/latest-before-layered-background-adjust-repair-2026-11-13.json
  - backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-layered-background-adjust-repair-2026-11-13.md
- Publisher workflows: run 43380705300 (run 137) and final run 43380881224 (run 138) both completed successfully; final run 138 publish job and all steps succeeded.
- Post-publish verification: web-source/index.html and diary-web/index.html are byte-identical; both Git blob SHA 962a0d43fc18dcbd8494cae4ec0ae603228c450d. Independently calculated UTF-8 SHA-256 0380cfa8045407eef7e58803514bfc4a1f0a5f3425286cebd0d247064e184ea0 matches live latest.json.webSha256. Live webVersion is 148.
- JavaScript parse check: both inline script blocks parsed successfully. Source/mirror/feed and backup checks passed.
- APK remains 1.0.136 / versionCode 135; APK SHA-256 remains 6fc74ca82888fed4121cc352c1846ec8c6a7063e2d2a33fbe032726f7a244348. No APK rebuild or signing operation.
- Physical-device verification is **pending**. Do not claim horizontal drag or pinch zoom works until the user tests it on the phone after receiving Web Update 148.
- Rollback: use the exact pre-edit files on backup/pre-layered-background-adjust-repair-2026-11-13. Preserve all local notes, photos, PIN data and app data.


# Web Update 149 — Smooth two-axis image adjustment for Cover, Detail and Photo (2026-11-13)

- User reported Web Update 148 still moved images only vertically, with excessively fast movement; horizontal drag and pinch zoom in/out were not working. User requested the same working adjustment across all three image areas: Cover, Detail and attached Photo.
- Re-read the live Master Register, latest.json, source and mirror before editing. Starting live state: webVersion 148; APK 1.0.136 / versionCode 135; source/mirror blob SHA 962a0d43fc18dcbd8494cae4ec0ae603228c450d.
- Root causes found in the actual adjustment math:
  - Cover/Detail drag used Math.max(1, containerSize - imageSize). Because imageSize exceeds containerSize, the negative overflow denominator was replaced with 1, making even a tiny finger movement jump rapidly and hit position limits. The new calculation uses the positive overflow magnitude with the correct sign on both axes.
  - The previous 1.25 image scale combined with the minimum saved zoom of 0.8 produced an effective scale of exactly 1.0, so one axis could have no overflow and could not be dragged. The base image scale is now 1.6, retaining overflow on both axes at the default zoom while keeping zoom-in/out range unchanged.
  - Attached Photo stored its neutral position as 50/50 but applied those values as direct CSS translate percentages, causing an offset from the centre. Translation now uses (position - 50), so 50/50 is the neutral centre.
- Changed only web-source/index.html. No APK rebuild, native Android change, storage/data key change, note/photo/PIN logic change, or unrelated UI change.
- Pre-edit backup branch: backup/pre-smooth-two-axis-photo-adjust-2026-11-13. Verified backup files:
  - backups/web-source-before-smooth-two-axis-photo-adjust-2026-11-13.html
  - backups/diary-web-before-smooth-two-axis-photo-adjust-2026-11-13.html
  - backups/latest-before-smooth-two-axis-photo-adjust-2026-11-13.json
  - backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-smooth-two-axis-photo-adjust-2026-11-13.md
- Source commit: 0c9935262b0bc7329f32cc2f3e0b926a2fbd5754. Web publisher workflow run 43382216940 (run 139) completed successfully; publish job and all listed steps succeeded.
- Post-publish verification: web-source/index.html and diary-web/index.html are byte-identical; both Git blob SHA b965dfa16278ab1b6ca8e5a80596e25367fdf9fb. Live latest.json reports webVersion 149 and web SHA-256 53f635184494a5da270f55e4e1732e833c10ad928037beb4db3e74263cd9d228. Final publisher commit on main: 0a9320e6697e6727c6671c987319d4847194e3cb.
- JavaScript parse check: both inline script blocks parsed successfully. Publisher workflow, source/mirror equality and live feed checks passed.
- APK remains 1.0.136 / versionCode 135; APK SHA-256 remains 6fc74ca82888fed4121cc352c1846ec8c6a7063e2d2a33fbe032726f7a244348. No APK rebuild or signing operation.
- Physical-device verification is **pending**. Do not claim smooth horizontal/vertical drag or pinch zoom works until the user tests all three image areas on the phone after receiving Web Update 149.
- Rollback: use the exact pre-edit files on backup/pre-smooth-two-axis-photo-adjust-2026-11-13. Preserve all local notes, photos, PIN data and app data.


# Web Update 150 — Reliable multi-pointer pinch zoom (2026-11-13)

- User confirmed Web Update 149 fixed equal left/right and up/down dragging in all three image targets (Cover, Detail, Photo), but pinch zoom-in and zoom-out still did not work.
- Re-read the live Master Register, latest.json, source and mirror. Starting state: webVersion 149; APK 1.0.136 / versionCode 135; source/mirror blob SHA b965dfa16278ab1b6ca8e5a80596e25367fdf9fb.
- Pinch zoom diagnosis: the existing gesture engine relied on document Touch Events while also installing Pointer Events but explicitly ignored touch pointers. Replaced this with Pointer Events as the primary Android/WebView gesture path: every finger is tracked by its independent pointerId; pointer capture keeps each contact associated with the selected image field; pointer move updates both points before calculating pinch distance; pointer up/cancel/lost capture rebase the remaining contact. Legacy Touch Events remain as fallback when PointerEvent is unavailable.
- The existing shared pinch ratio, zoom range 0.8–4, position state, rendering, and drag math are retained. No changes to notes, local storage/data keys, photo content, PIN, editor UI, or APK.
- Changed only web-source/index.html. Pre-edit backup branch: backup/pre-pointer-pinch-zoom-repair-2026-11-13. Verified backups:
  - backups/web-source-before-pointer-pinch-zoom-repair-2026-11-13.html
  - backups/diary-web-before-pointer-pinch-zoom-repair-2026-11-13.html
  - backups/latest-before-pointer-pinch-zoom-repair-2026-11-13.json
  - backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-pointer-pinch-zoom-repair-2026-11-13.md
- Source commit: 760c573af312bc4bbf70f2125f311609aa41836e. Web publisher workflow run 43383223582 (run 140) completed successfully; publish job and all listed steps succeeded.
- Post-publish verification: web-source/index.html and diary-web/index.html are byte-identical; both Git blob SHA fd1d38dc9d73bdabb5a074ef1449a2360712ff51. Live latest.json reports webVersion 150 and web SHA-256 ab6b55d80e6f157b77be6d8a82f8ae198b95284b66fb9a436487fd04104c176e. Both inline JavaScript blocks parse successfully.
- APK remains 1.0.136 / versionCode 135. No APK rebuild or signing operation.
- Physical-device verification is **pending**. Do not claim pinch zoom works until the user tests Cover, Detail and Photo on the phone after receiving Web Update 150. Drag was already confirmed by the user on Update 149; this change was limited to pointer gesture tracking.
- Rollback: use the exact pre-edit files on backup/pre-pointer-pinch-zoom-repair-2026-11-13. Preserve all local notes, photos, PIN data and app data.


# Web Update 151 — Detect both fingers across the selected image box (2026-11-13)

- User tested Web Update 150 and reported that pinch zoom-in and zoom-out still did not work. Existing left/right and up/down drag in Cover, Detail and Photo had been confirmed working and must be preserved.
- Re-read the live Master Register, latest.json, source and published mirror before editing. Starting state: webVersion 150; APK 1.0.136 / versionCode 135; source/mirror blob SHA fd1d38dc9d73bdabb5a074ef1449a2360712ff51.
- Diagnosis: Pointer Events registered pointerdown only on the selected image element and used pointer capture. A second finger landing on another part of the image box/frame or a child element could fail to enter the tracked pointer set. The pinch calculation itself and zoom bounds were retained.
- Changed only bindDiaryFingerAdjust(target,kind) in web-source/index.html: pointerdown is now captured at document level and each contact is registered when its coordinates fall inside the selected target's bounding rectangle. Removed explicit pointer capture and the related lost-capture handler; document-level pointermove/up/cancel continue tracking active contacts. Existing one-finger drag calculations, pinch ratio, zoom range 0.8–4, image painting, Touch Events fallback and stored state remain unchanged.
- Explicitly untouched: pamphlet chooser/designs, image selection, editor layout, note/photo data and storage keys, save format, PIN/lock/recovery, translations, native Android source, APK, package identity, signing data and unrelated Diary features.
- Pre-edit backup branch: backup/pre-document-pointerdown-pinch-repair-2026-11-13. Verified readable backups:
  - backups/web-source-before-document-pointerdown-pinch-repair-2026-11-13.html
  - backups/diary-web-before-document-pointerdown-pinch-repair-2026-11-13.html
  - backups/latest-before-document-pointerdown-pinch-repair-2026-11-13.json
  - backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-document-pointerdown-pinch-repair-2026-11-13.md
- Source commit: 28d24528fdef97ef86b385f07e30f922f0a42c0c. Publisher commit: 998923d92b31dd1155e65ad843c3ae6fa2b39acb. Live feed advanced to webVersion 151; publisher commit synchronized the published mirror and feed.
- Post-publish verification: source and mirror are byte-identical; both Git blob SHA 99785ad58c1a0a03f0b90b5dc3bd5fe3de9b6077. Independently calculated UTF-8 SHA-256 4043dc99f56adba90e65d54869f711bc7f05d3c54c3974e1f17108d7be05bfc8 matches live latest.json.webSha256. Both inline JavaScript blocks parsed successfully. Source, mirror and feed were re-fetched after publishing.
- APK remains 1.0.136 / versionCode 135; no APK rebuild or signing operation. Notes, photos, PIN data, app data, and package/signing identity were not changed.
- Physical-device verification is **pending**. User must install Web Update 151 through Me → Check for Updates and test pinch-in and pinch-out separately on Cover, Detail and Photo. Existing drag was already confirmed on Web Update 149; do not claim pinch zoom works until the user confirms it on the phone.
- Rollback: use the exact pre-edit files on backup/pre-document-pointerdown-pinch-repair-2026-11-13; preserve all local notes, photos, PIN data and app data.


# Web Update 154 — Clear change-image control after image selection (2026-11-13)

- User request: make it clear how to replace a selected image when it is not liked. A selected Cover, Detail or attached Photo now changes its picker button label to the localized **Change Image** wording. Tapping the same button opens the existing image-design chooser, where **Choose Image** opens the gallery; selecting a new image replaces only that image target.
- Changed only `web-source/index.html`, source commit `9e3a180a7b6abd70f24a586e45abe3832de83a09`. Added localized `changeImage` wording for all 10 supported languages. Cover and Detail labels follow whether their respective image data exists; Photo label follows attached-photo state. Language switching refreshes all three labels. Existing image picker, colour/pamphlet chooser, crop/drag/pinch state, text, note records, storage keys, PIN/recovery, native Android source, APK, package identity and signing data were not changed.
- Starting live state: Web Update 153; APK 1.0.136 / versionCode 135; source/mirror blob SHA `aa9a115ce37c1e3cad115046f13dcf3f7f63a75e`.
- Pre-edit backup branch: `backup/pre-image-replacement-control-2026-11-13`. Verified readable backups:
  - `backups/web-source-before-image-replacement-control-2026-11-13.html` (blob SHA `aa9a115ce37c1e3cad115046f13dcf3f7f63a75e`)
  - `backups/latest-before-image-replacement-control-2026-11-13.json` (blob SHA `e5d475d13a82f5816060a05e83f83cce549310ad`)
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-image-replacement-control-2026-11-13.md` (blob SHA `4e58ae3fb839bec284cfa74f63bc1ea65b624076`)
- Static checks: all 10 language entries and Cover/Detail/Photo label-state logic were found in the final source; language-refresh logic for all three controls was verified. The source commit changed only `web-source/index.html`. A JavaScript parser run and independent SHA-256 calculation were not available in this session; do not describe those checks as passed.
- Publisher output commit: `4b53d41fe9bd51225c46aa6286ec930bbb15b653` (“Publish My Diary web bundle update”). Live feed advanced to Web Update 154. Re-fetched source and published mirror are byte-identical; both Git blob SHA `e145f56506ea6aef721a8673fecbb3fc859c76f9`. Live `latest.json.webSha256` is `dcfcf5244c66e2b46dbf8e33189344408754af9abd5cb45a4f5621e3f582ce0b` (publisher/feed value; independent calculation not performed). Workflow run ID/conclusion was not exposed by the available status lookup; the publisher output commit, mirrored file and advanced feed were verified.
- APK unchanged: 1.0.136 / versionCode 135 / SHA-256 `6fc74ca82888fed4121cc352c1846ec8c6a7063e2d2a33fbe032726f7a244348`; no APK rebuild or signing changes.
- Physical-device verification pending. User should install Web Update 154 using **Me → Check for Updates**, then test changing Cover, Detail and Photo individually; confirm the existing text and the other images remain unchanged.
- Rollback: use the exact pre-edit files on `backup/pre-image-replacement-control-2026-11-13`; preserve local notes, photos, PIN data and app data.


# Web Update 155 — Change Image opens gallery directly (2026-11-13)

- User clarification: tapping **🔄 Image Badlein / Change Image** should open image selection directly, not open the image-design chooser first.
- Changed only `web-source/index.html`, source commit `f0f9430a9b8791a7875697ce8b8ad31cc4c12770`. In the shared Cover/Detail/Photo image chooser button handler, when that target already has an image, the button closes the chooser if needed and directly invokes its existing file input (`file.click()`). When no image is selected yet, the original chooser remains available so users can still choose an image, colour, gradient or pamphlet design. This keeps the requested direct-replace path while preserving first-time design choices.
- Pre-edit backup branch: `backup/direct-image-picker-2026-11-13`. Verified readable backups:
  - `backups/web-source-before-direct-image-picker-2026-11-13.html` (blob SHA `e145f56506ea6aef721a8673fecbb3fc859c76f9`)
  - `backups/latest-before-direct-image-picker-2026-11-13.json` (blob SHA `28c8b747f2db2372a51cb92e8ef788e4029bc174`)
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-direct-image-picker-2026-11-13.md` (blob SHA `c98cde2e17003b314ec1efa0e94f4aef9f72e964`)
- Static source review confirmed the one shared handler tests the selected-image state separately for Cover, Detail and Photo, and calls the existing file input directly for each selected image. Existing initial image chooser, pamphlet/colour options, image compression, image-position/zoom adjustment, text, notes, local storage, PIN/recovery, Android source, package identity and signing data were not changed. No JavaScript parser or independent SHA-256 calculation was run in this session.
- Publisher workflow run `43390587303` (run 145, `.github/workflows/publish-diary-web-update.yml`) completed successfully. Its `publish` job and all steps succeeded. Publisher output commit was verified by live files: source and `diary-web/index.html` are byte-identical with Git blob SHA `82dd680c76336782cfeb9d1bcc67ec2f02ade1b5`. Live feed advanced to Web Update 155; `latest.json.webSha256=81813e198d9435ef84c66b5e7964d3c1ef72e41c349d78797e7859eada9cc88e`.
- APK unchanged: 1.0.136 / versionCode 135 / SHA-256 `6fc74ca82888fed4121cc352c1846ec8c6a7063e2d2a33fbe032726f7a244348`; publisher workflow explicitly ran without rebuilding APK.
- Physical-device verification pending. User should use **Me → Check for Updates** to install Web Update 155, then tap Change Image for Cover, Detail and Photo and confirm Gallery opens directly; select a replacement and check other images/text remain unchanged.
- Rollback: use the exact pre-edit files on `backup/direct-image-picker-2026-11-13`; preserve local notes, photos, PIN data and app data.


# Web Update 156 — Restore writing by tapping an image field (2026-11-13)

- User reported that tapping the image no longer opened the writing option/keyboard. Inspection found the automatic image-adjustment Pointer/Touch handlers were calling `preventDefault()` and `stopPropagation()` on every initial press, including taps on the Cover title input and Detail text area.
- Starting live state: Web Update 155; APK 1.0.136 / versionCode 135; package `com.personal.diaryapp`; source/mirror blob SHA `82dd680c76336782cfeb9d1bcc67ec2f02ade1b5`; feed SHA-256 `81813e198d9435ef84c66b5e7964d3c1ef72e41c349d78797e7859eada9cc88e`.
- Changed only `web-source/index.html`, source commit `c30e4a2aa010383ca5fa8149d7e7174dc5c83793`. Single taps now pass through to the input/textarea so the keyboard can open. Drag/pinch adjustment takes over only after movement reaches 6 pixels; the Touch Events fallback follows the same threshold. Existing zoom range, per-image positions, saved image/text data, and Web Update 155 direct Gallery replacement behavior remain unchanged.
- Pre-edit backup branch: `backup/pre-image-tap-writing-fix-2026-11-13`; exact readable backups verified:
  - `backups/web-source-before-image-tap-writing-fix-2026-11-13.html` (blob SHA `82dd680c76336782cfeb9d1bcc67ec2f02ade1b5`)
  - `backups/latest-before-image-tap-writing-fix-2026-11-13.json` (blob SHA `0705bc5580afd5b96f16bd7dc4866c705dbe7aa4`)
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-image-tap-writing-fix-2026-11-13.md` (blob SHA `c80f161897a4928b0ffae5faf1e114ed511de5d9`)
- Source diff reviewed: only the shared image gesture handler changed. Both inline JavaScript blocks parsed successfully. Static checks confirm tap events are no longer cancelled at pointer/touch start and both drag handlers use the 6-pixel movement threshold.
- Web-only workflow run `43395054248` (run 146) completed with conclusion `success`; publish job `131783845220` succeeded. Publisher output advanced the live feed to Web Update 156.
- Post-publish: source and `diary-web/index.html` are byte-identical; both Git blob SHA `3a9439731ca5965b381b938b86c5189b657c4999`. Independently computed UTF-8 SHA-256 `7404440c4db966789b67529d0f156191a715769b3d2513a9da13be8c4de92aef` matches live `latest.json.webSha256`; webVersion is 156.
- APK unchanged: 1.0.136 / versionCode 135 / SHA-256 `6fc74ca82888fed4121cc352c1846ec8c6a7063e2d2a33fbe032726f7a244348`; no APK rebuild or signing changes.
- Physical-device verification **pending**. User should use **Me → Check for Updates**, then tap the Cover image field and Detail image field to confirm the writing keyboard opens; also verify one-finger drag and two-finger zoom still work. Tap **Image Badlein** on an existing image to confirm it still opens Gallery directly.
- Rollback: verified pre-edit files on `backup/pre-image-tap-writing-fix-2026-11-13`; preserve all diary notes, photos, PIN data and app identity.


# Web Update 158 — Fix Note Share on mobile (2026-11-13)

- User reported that 📤 Note Share Karein did not work. Root cause: the composed PNG was created asynchronously (Image loading and canvas.toBlob) and only then passed to navigator.share(). On mobile browsers the transient user activation from the tap can expire before this asynchronous work completes, so the native share sheet is blocked.
- Starting live state: Web Update 156; APK 1.0.136 / versionCode 135; package com.personal.diaryapp; source/mirror blob SHA 3a9439731ca5965b381b938b86c5189b657c4999; feed SHA-256 7404440c4db966789b67529d0f156191a715769b3d2513a9da13be8c4de92aef.
- Changed only web-source/index.html. When a note is expanded and unlocked, the app now prepares the same combined Diary PNG (cover image + title text + detail image + note text + attached photo) in advance. The Share button remains disabled until that PNG is ready, then its click calls navigator.share({files:[file]}) immediately within the user's tap. If file sharing is unsupported, the existing composed-image download fallback remains. Preparation is cached per note ID, update timestamp and selected language. Note content, image layout, formatting, notes storage, photos, PIN/recovery, app identity and Android source were not changed.
- Pre-edit backup branch: backup/pre-note-share-fix-2026-11-13; verified exact backups:
  - backups/web-source-before-note-share-fix-2026-11-13.html (blob SHA 3a9439731ca5965b381b938b86c5189b657c4999)
  - backups/latest-before-note-share-fix-2026-11-13.json (blob SHA 3b8f1fd35cf7921e83932274897f8a017b778414)
  - backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-note-share-fix-2026-11-13.md (blob SHA 75db3e09d122642bc6a6cc5fbf20ddf2dad99be1)
- Source commits: initial implementation b401fed740e8397dd578f5ccf5520502fed687c8; final refinement 7d367e562ed1d682c769980d89919fb4f1083abb. Final diff reviewed and both inline JavaScript blocks parsed successfully. Static checks verified pre-generation on expanded notes, disabled-until-ready behavior, cached PNG, and synchronous share invocation on tap.
- Publisher workflow runs 147 (43396317069) and 148 (43396414393) both completed successfully; each publish job succeeded. The final publisher output is Web Update 158 (run 148). Live feed confirms webVersion=158 and webSha256=bcb655b79f33742f44e6de283bd2af5286acb7d8f5bf70cd90f55d521e866f16.
- Post-publish: source and diary-web/index.html are byte-identical; both Git blob SHA 131469afbb2aa47b0132c07f7210b45e0eba0b6a.
- APK unchanged: 1.0.136 / versionCode 135 / SHA-256 6fc74ca82888fed4121cc352c1846ec8c6a7063e2d2a33fbe032726f7a244348; web-only workflow did not rebuild APK.
- Physical-device verification pending. User should install via Me → Check for Updates, open/unlock a note, wait until 📤 Note Share Karein becomes enabled, then tap it and confirm Android's share sheet appears with the combined Diary PNG. If no compatible share target exists, the existing image-download fallback should run.
- Rollback: exact pre-edit files are preserved on backup/pre-note-share-fix-2026-11-13; preserve all local notes, photos, PIN data and app identity.


# Web Update 159 — Prevent Note Share tap from collapsing the note (2026-11-13)

- User tested Web Update 158 and reported that tapping 📤 Note Share Karein only shifted/collapsed the page.
- Inspection found the share button was deliberately disabled until the asynchronous PNG preparation completed. Because a disabled button does not dispatch its click event, the event could bubble to the parent note card, whose click handler collapses the expanded note. This explains the reported page movement.
- Starting live state: Web Update 158; APK 1.0.136 / versionCode 135; source/mirror blob SHA 131469afbb2aa47b0132c07f7210b45e0eba0b6a.
- Changed only web-source/index.html, source commit a67edf176d17d185fe4b56936152d563b85d2a08. The Share button is no longer disabled while the combined PNG is being prepared. Its click handler now always prevents default and stops propagation first, so tapping cannot trigger the parent note-card collapse. If the PNG is not ready yet, it displays a short “still preparing, tap again” message and ensures preparation is running. Once cached, the same button opens the native share sheet directly from the tap. Existing combined-image layout and download fallback remain. No note records, local photos, PIN/recovery, Android source, app identity or APK were changed.
- Pre-edit backup branch backup/pre-note-share-button-tap-fix-2026-11-13; exact backups verified:
  - backups/web-source-before-note-share-button-tap-fix-2026-11-13.html (blob SHA 131469afbb2aa47b0132c07f7210b45e0eba0b6)
  - backups/latest-before-note-share-button-tap-fix-2026-11-13.json (blob SHA 4fd67f1313bc3586352f2768497b7c619aba7054)
  - backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-note-share-button-tap-fix-2026-11-13.md (blob SHA 0abe02d7ca27b6c83564b781d147a16f20789d0b)
- Both inline JavaScript blocks parsed successfully. Static checks confirm the button is never disabled, stops event propagation on every tap, retries image preparation when necessary, and calls share only after a composed PNG is cached.
- Publisher workflow run 43397309941 (run 149) completed successfully. Publisher job succeeded. Live feed advanced to Web Update 159 with webSha256 bcb655b79f33742f44e6de283bd2af5286acb7d8f5bf70cd90f55d521e866f16.
- Post-publish: web-source/index.html and diary-web/index.html are byte-identical; both blob SHA 9b5372c80a3f63c8e8f69fc8fa31324b2e4e1a81.
- APK unchanged: 1.0.136 / versionCode 135 / SHA-256 6fc74ca82888fed4121cc352c1846ec8c6a7063e2d2a33fbe032726f7a244348.
- Physical-device verification pending. User should install Web Update 159 using Me → Check for Updates, open/unlock a note, tap Share once (if still preparing, wait briefly and tap again), and confirm the note stays expanded and Android's share sheet opens.
- Rollback: exact pre-edit files are preserved on backup/pre-note-share-button-tap-fix-2026-11-13; preserve local notes, photos, PIN data and app identity.


# Web Update 160 — Restore the known-good one-tap Note Share handler (2026-11-13)

- User reported Note Share remained nonfunctional after Web Update 159 and explicitly required evidence-based checking, not guesswork.
- Starting live state: Web Update 159; APK 1.0.136 / versionCode 135; package `com.personal.diaryapp`; source/mirror blob SHA `9b5372c80a3f63c8e8f69fc8fa31324b2e4e1a81`; feed SHA-256 `bcb655b79f33742f44e6de283bd2af5286acb7d8f5bf70cd90f55d521e866f16`.
- Historical comparison: fetched the actual Web Update 157 source at publisher commit `4705d62cb2222a677c2a438717116a48c0306cda`, then compared the Note Share function and button handler against Web Updates 158 and 159. Web 157's button handler calls `shareNote(n)` immediately from the tap. Web 158 introduced a disabled-until-ready state; Web 159 removed disabled state but added a cache-miss early return, so a tap while image preparation was pending did not invoke the known-good Share flow. This was the exact behavioral regression.
- Scope: changed only the Note Share button's click handler in `web-source/index.html`. Restored the exact Web 157 handler behavior: prevent default, stop propagation, then call `shareNote(n)` immediately. Existing asynchronous pre-generation, cache, combined PNG composition, text/image placement, native share call, and download fallback remain. No other functions, UI, notes, photos, storage, PIN/recovery, Android source, package identity, APK or signing data changed.
- Pre-edit backup branch: `backup/pre-share-single-tap-restore-2026-11-13`; verified readable exact backups:
  - `backups/web-source-before-share-single-tap-restore-2026-11-13.html` (blob SHA `9b5372c80a3f63c8e8f69fc8fa31324b2e4e1a81`)
  - `backups/diary-web-before-share-single-tap-restore-2026-11-13.html` (blob SHA `9b5372c80a3f63c8e8f69fc8fa31324b2e4e1a81`)
  - `backups/latest-before-share-single-tap-restore-2026-11-13.json` (blob SHA `90ffff65ff474fe5b964de4244a13e520dc8e975`)
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-share-single-tap-restore-2026-11-13.md` (blob SHA `b290aecd5a204392285ad1b52bb50da5b81b33f6`)
- Source change commit: `e648772ad8924e7fade1f58ef0b57b26ea158a34`; publisher output commit: `6e21edb1f4a89dd55601db21cd9b2596b268019b`. The exact branch diff was verified to equal one replacement of the Share click handler only.
- Verification: both inline JavaScript blocks parsed successfully. Static checks confirmed the restored handler exists once, stops parent-card propagation, leaves pre-generation enabled, and preserves the composed PNG/native-share code. Re-fetched source and mirror are byte-identical; both Git blob SHA `8cd55c74c81a77232b53d22ff3da27d564617d37`. Independently calculated UTF-8 SHA-256 `9e62a60bfad90c5374d02ebad6e39d6138c5c217bffcb22c03ab3c8a1a31be1f` matches live feed `latest.json.webSha256`; live webVersion is 160. Publisher output commit and live mirror/feed update are verified; direct workflow run ID/conclusion was not available through the current read endpoint and is recorded as not independently retrieved.
- APK unchanged: 1.0.136 / versionCode 135 / SHA-256 `6fc74ca82888fed4121cc352c1846ec8c6a7063e2d2a33fbe032726f7a244348`; no APK rebuild or signing changes.
- Physical-device verification **pending**. User should use **Me → Check for Updates**, open/unlock a note, and tap **Share** once. Confirm the note stays expanded and the Android share sheet opens. Do not claim phone-side success until the user confirms.
- Rollback: exact pre-edit files on `backup/pre-share-single-tap-restore-2026-11-13`; preserve all local notes, photos, PIN data and app identity.


# Web Update 161 — Keep Note Share unavailable until the composed image is ready (2026-11-13)

- User reported that `📤 Note Share Karein` still did not open Share and asked for the fix to work in both the Android APK and Chrome.
- Starting live state: Web Update 160; APK 1.0.136 / versionCode 135; package `com.personal.diaryapp`; source/mirror blob SHA `8cd55c74c81a77232b53d22ff3da27d564617d37`; feed SHA-256 `9e62a60bfad90c5374d02ebad6e39d6138c5c217bffcb22c03ab3c8a1a31be1f`.
- Audited the complete live `shareNote` function and the expanded-note rendering/click handlers. Confirmed that a cache-miss Share tap fell through to asynchronous image loading, canvas rendering and `toBlob`, then called `navigator.share` only after those asynchronous steps. That loses the transient browser user activation in Chrome. Also confirmed the Android project has a native `DiaryNativeShare` WebMessageListener and a `navigator.share` shim; it converts selected files to Base64 and invokes Android's FileProvider share intent.
- Changed only `web-source/index.html`: the Share button now stays disabled until the composed PNG cache is ready, and its preparation callback enables the button only after the cached image exists. The parent note-card click handler now ignores taps originating from buttons/inputs/selects, preventing a not-yet-ready Share button tap from collapsing the expanded note. Once enabled, the button calls the existing `shareNote(n)` synchronously from the tap. Combined PNG artwork, image/text positioning, native Android share bridge, browser Web Share API, download fallback, notes, photos, storage, PIN/recovery and APK were not changed.
- Pre-edit backup branch: `backup/pre-note-share-ready-gate-2026-11-13`; verified backup files:
  - `backups/web-source-before-note-share-ready-gate-2026-11-13.html`
  - `backups/latest-before-note-share-ready-gate-2026-11-13.json`
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-note-share-ready-gate-2026-11-13.md`
- Source change commit: `a5647aa33116ed4e30914911ba64da16e66cc474`; source blob SHA `893bb0524cbf409289784ff616fff453b2efd262`.
- Web-only publisher workflow run `43406545302` (run 151) completed with conclusion `success`; publish job `131822149788` succeeded. Live source and `diary-web/index.html` are byte-identical; both blob SHA `893bb0524cbf409289784ff616fff453b2efd262`. Live feed advanced to Web Update 161 and reports `webSha256=72d57d63844f68f125c49f7bfb90fd62c38a060bd8804fd9dc129eb7561e3ccb`. The publisher workflow computed this SHA and wrote it to the feed; an independent local recomputation is still pending.
- Static verification after publication confirmed the readiness gate, preparation callback, synchronous Share call after readiness, and parent-card control-target guard are all present in the published source. JavaScript parse/build validation for this exact web bundle is pending; no claim of complete automated syntax validation is made.
- APK unchanged: 1.0.136 / versionCode 135 / SHA-256 `6fc74ca82888fed4121cc352c1846ec8c6a7063e2d2a33fbe032726f7a244348`; no APK rebuild or signing change.
- Physical-device/browser verification pending. User should use **Me → Check for Updates**, open and unlock a note, wait for the Share button to become enabled, then tap it once. Confirm the note stays expanded and the Android/Chrome share sheet opens with the single composed Diary image. Do not claim phone-side success until confirmed.
- Rollback: exact pre-edit files are preserved on `backup/pre-note-share-ready-gate-2026-11-13`; preserve local notes, photos, PIN data and app identity.


# Web Update 162 — Note Share canvas fallback and failure-safe readiness (2026-11-13)

- User reported that Web Update 161 still did not make Note Share work. Re-audited the full share function and found a definite failure-path defect: when `canvas.toBlob` returned null or image preparation rejected, the code still called the readiness callback with no success value. The Share button then became enabled despite no cached image; the next tap rebuilt the image asynchronously and could lose the user activation again.
- Created pre-edit backup branch `backup/pre-note-share-canvas-fallback-2026-11-13` with:
  - `backups/web-source-before-note-share-canvas-fallback-2026-11-13.html`
  - `backups/latest-before-note-share-canvas-fallback-2026-11-13.json`
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-note-share-canvas-fallback-2026-11-13.md`
- Changed only `web-source/index.html`: canvas PNG creation now uses `canvas.toBlob` when available and falls back to `canvas.toDataURL` -> Blob if `toBlob` is unavailable or returns null. Preparation callbacks now receive explicit success/failure; Share is enabled only after a successful cached PNG, and remains disabled on failure with an accessible error title/status. Existing composed layout, native Android bridge, browser share, download fallback, notes/photos/storage/PIN and app identity are unchanged.
- Source commit `9949f2de30084cbfa64d5465aa959f8aad6b7054`; source blob `50420b05d0bd25d893b44d5e1c94c53f8c4b9975`.
- Web-only publisher run `43407161971` (run 152) completed `success`; publish job `131824200908` completed `success`. Workflow's verification/publish step succeeded, including its bundle validation.
- Post-publish source and `diary-web/index.html` are byte-identical; both blob SHA `50420b05d0bd25d893b44d5e1c94c53f8c4b9975`. Feed reports Web Update `162`, SHA-256 `39d789052f285fb29abc4292f6e4e802382adc03ca3d876de3907c474cba7dcf`. Static post-publish checks confirmed fallback function, explicit true/false callback paths, and success-only enable logic.
- APK unchanged at 1.0.136 / versionCode 135; no APK rebuild or signing change. Physical device/browser share-sheet test remains pending. Do not claim complete success until user confirms the actual share sheet opens and the composed image is attached.
- User test path: Me → Check for Updates; open/unlock note; wait until Share button becomes enabled; tap once. If it stays disabled, report the visible status rather than tapping repeatedly.


# Web Update 163 — Keep Note Share tappable and isolate touch events (2026-11-13)

- User reported that tapping **📤 Note Share Karein** only moved the note page. Inspection of the live Web Update 162 source identified the exact cause: the Share button was set to `disabled` until its composed PNG cache was ready. A disabled HTML button does not dispatch the normal click event; on touch, the tap can be retargeted to the parent note card. The note card's pointer/scroll handling then receives the gesture instead of Share. This was not a new Android bridge failure.
- Starting state: Web Update 162; APK 1.0.136 / versionCode 135; source and mirror blob SHA `50420b05d0bd25d893b44d5e1c94c53f8c4b9975`; feed SHA-256 `39d789052f285fb29abc4292f6e4e802382adc03ca3d876de3907c474cba7dcf`.
- Pre-edit backups were created and re-fetched successfully on branch `backup/note-share-disabled-tap-event-2026-11-13`:
  - `backups/web-source-before-note-share-disabled-tap-event-2026-11-13.html` (blob SHA `50420b05d0bd25d893b44d5e1c94c53f8c4b9975`)
  - `backups/diary-web-before-note-share-disabled-tap-event-2026-11-13.html` (blob SHA `50420b05d0bd25d893b44d5e1c94c53f8c4b9975`)
  - `backups/latest-before-note-share-disabled-tap-event-2026-11-13.json` (blob SHA `18df90e0cfb8819b9fc57ac0357c4624f0c85022`)
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-note-share-disabled-tap-event-2026-11-13.md` (blob SHA `a26cc24aa128fe63291c2806c65564147e7487c4`)
- Changed only the Share-button creation/handler line in `web-source/index.html` (source commit `ebec0098ec2e7ef89a7e24d9bb87eff6b6ac3acd`). Share remains enabled while the PNG is preparing; pointerdown and touchstart stop propagation; click prevents default and stops propagation. If the image is not ready, the user sees a preparing message and preparation can be retried; when cached, the existing `shareNote(n)` is called synchronously from the tap. Existing composed-image artwork, layout, image/text placement, native Android bridge, browser share, download fallback, notes/photos/storage/PIN/recovery and APK were not changed.
- Both inline JavaScript blocks in the updated source parsed successfully. The source/mirror publisher output commit is `6101336f899cf133706cc52ead800200af53efd5` (“Publish My Diary web bundle update”), which updated only `diary-web/index.html` and `latest.json`. The publisher workflow run ID was not independently exposed by the available read endpoint; the publisher bot output commit and live feed were verified.
- Post-publish source and mirror are byte-identical; both blob SHA `5a75e86dce0a444af482ba20325963570d94f301`. Live feed reports webVersion `163` and `webSha256=5170a6cba592960dbb2ff7b0b3773c6b38da1d6b16c99999029228ccfcdfdc37`. Independently calculated SHA-256 from the exact UTF-8 source bytes matches the feed.
- APK unchanged: 1.0.136 / versionCode 135 / SHA-256 `6fc74ca82888fed4121cc352c1846ec8c6a7063e2d2a33fbe032726f7a244348`; no APK rebuild or signing changes.
- Physical-device verification pending. User should use **Me → Check for Updates**, open/unlock a note, and tap **📤 Note Share Karein**. First confirm the note page no longer moves; then wait for the image-ready state and tap Share again if the preparation message appears. Confirm the actual Android/Chrome share sheet opens and contains the combined note image before claiming the feature fully works.
- Rollback: exact pre-edit files are preserved on `backup/note-share-disabled-tap-event-2026-11-13`; preserve local notes, photos, PIN data and app identity.


# Pending source patch — stop note-card press animation on Share (2026-11-13)

- User reports Share tap still only moves the whole note card. Inspection found the explicit parent-card press animation: `.diary-my-note:active{transform:scale(.99)}`. The Share button is inside this article card, so the card itself visibly shifts during a Share press.
- A minimal source-only patch was committed as `ba5d085f1846856f8b05f82fc755530556efd802`: the Share button now has the additional class `diary-note-share`, and `.diary-my-note:has(.diary-note-share:active){transform:none!important;}` suppresses only the parent card's active movement while Share is pressed. Existing Share handler and other note actions remain unchanged.
- Pre-edit backups were created and verified on `backup/note-card-share-motion-fix-2026-11-13`: source and mirror blob SHA `5a75e86dce0a444af482ba20325963570d94f301`, feed blob SHA `0d262443629d9216d3bbbe1ce78c9a5f798dfe28`, register blob SHA `85020077f83f7e451e55415567d34cab8a5e872f`.
- **Not published.** After the source commit, the mirror remains at `5a75e86dce0a444af482ba20325963570d94f301`, while source is `fc2beb9cd8b4fecd2372273b635cecdf77a5705b`; feed remains webVersion `163` with SHA-256 `5170a6cba592960dbb2ff7b0b3773c6b38da1d6b16c99999029228ccfcdfdc37`. No publisher workflow run was returned for the source commit. Therefore do not tell the user to check for updates or claim the fix is live. Resume only after the established publisher workflow can be run and verified, then mirror, feed hash, and register must all be verified.


# Completed publication — Note Share card motion fix (Web Update 164, 2026-11-13)

- The source patch from commit `ba5d085f1846856f8b05f82fc755530556efd802` was published by the verified GitHub Actions workflow run **43408313086**, workflow **Publish My Diary web-only update**, run 154; status `completed`, conclusion `success`, head SHA matches the source patch.
- Publisher output commit: `2b77b47b379e61d8d6e929fe2272e013f0c705db`. It changed only `diary-web/index.html` and `latest.json`.
- Live `latest.json` reports webVersion `164`, webSha256 `0645f735400d037eac30dcca5c043317bd67f2c0f5982eefdef6269fa60522ae`; APK remains `1.0.136`, versionCode `135`, APK SHA-256 unchanged at `6fc74ca82888fed4121cc352c1846ec8c6a7063e2d2a33fbe032726f7a244348`.
- Live source and published mirror were fetched independently; both are byte-identical and share blob SHA `fc2beb9cd8b4fecd2372273b635cecdf77a5705b`. This verifies mirror equality. The feed's published SHA-256 is recorded above; this runtime did not independently recompute the SHA-256 digest.
- Minimal change: add class `diary-note-share` to the Share button and CSS `.diary-my-note:has(.diary-note-share:active){transform:none!important;}` to prevent the enclosing note card's active scale animation only while Share is pressed. Existing Share logic and other controls are unchanged.
- Earlier section “Pending source patch — stop note-card press animation on Share” is superseded by this completed publication record. Physical-device confirmation is still pending: user must verify that the share sheet opens and contains the composed note image. Do not claim the actual Share operation is confirmed until the user tests it.
- Register pre-edit backup was saved and verified on branch `backup/note-share-motion-published-2026-11-13` at `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-note-share-motion-published-2026-11-13.md`.


# Note Share readiness fix — Web Update 165 (2026-11-13)

- User's repeated report: tapping **📤 Note Share Karein** only moved the note card and did not open Share. Inspection of the live Web Update 164 source found that the Share button was appended immediately while its composed PNG was still being generated. The click handler explicitly returned early while the cache was empty, so that tap never called `navigator.share`; it only displayed a preparation message. The enclosing note card also had active transform rules, which visually moved the card during the press.
- Pre-edit backups were created and re-fetched successfully on branch `backup/share-ready-gate-2026-11-13`:
  - `backups/web-source-before-share-ready-gate-2026-11-13.html` (blob SHA `fc2beb9cd8b4fecd2372273b635cecdf77a5705b`)
  - `backups/diary-web-before-share-ready-gate-2026-11-13.html` (same blob SHA)
  - `backups/latest-before-share-ready-gate-2026-11-13.json` (blob SHA `e6b4d223e9f3f44b2cf7523f5faca6344d1378b7`)
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-share-ready-gate-2026-11-13.md` (blob SHA `fc982c76464abd1a9261a22eecf5050cdd9c5f9a`)
- Source-only patch commit: `2fba229b2959117bbfc999d1c7bfbbccbe3c43bf`; source blob SHA `3e585702b5560f9a7785c54895ad4e3769380bd4`. The Share button is now created only after the composed PNG cache is ready. While preparing, a visible status replaces the premature Share button; if image preparation fails, that status can be tapped to retry. Once ready, a single Share-button tap calls the existing `shareNote(n)` path directly. Both active note-card transform rules were neutralized to prevent the card from shifting on press. No image composition, notes, photos, storage, PIN, or native bridge code was changed.
- Both inline JavaScript blocks passed syntax parsing after the patch. Targeted source checks confirmed the premature button/click path was removed, the ready-gated button is present, and the card active transforms are neutralized.
- Publisher workflow run **43409526224**, run 155, head SHA `2fba229b2959117bbfc999d1c7bfbbccbe3c43bf`, completed successfully. Publisher output commit `f7b4c82ec2dbdd61d98101f27d9728db4bda4eff` changed only `diary-web/index.html` and `latest.json`.
- Live feed reports webVersion `165` and SHA-256 `ba25e5c8d46931e8e50848a2cd118b0051c4d370a61e1fff1135c75f7f017e64`; this exact digest was printed by the successful publisher workflow. Independently fetched source and mirror are byte-identical, both blob SHA `3e585702b5560f9a7785c54895ad4e3769380bd4`.
- APK remains unchanged: `1.0.136`, versionCode `135`, SHA-256 `6fc74ca82888fed4121cc352c1846ec8c6a7063e2d2a33fbe032726f7a244348`.
- Physical-device verification is still pending. Do not claim Share sheet operation is confirmed until user tests that the Share button appears after preparation and opens the share sheet with the composed note image. If the button does not appear, report that as a distinct image-preparation failure rather than asking the user to keep tapping.
- This section supersedes the earlier pending/partial Share notes and the Web Update 164 card-motion-only fix for current live status.


# Note Share native bridge routing — Web Update 166 (2026-11-13)

- User reported that Check for Updates showed “Diary Pehle Se Update Hai” and Note Share still needed repair. Re-inspection found a concrete integration issue: the updater reloads the verified HTML with a cache-busting query parameter (?diaryRefresh=...), while the Android onPageFinished hook in the inspected Android source archive injects the navigator.share shim only when the URL exactly equals the bare /assets/index.html URL. On the query-string refresh URL, that shim is skipped even though the DiaryNativeShare WebMessageListener is available. This explains why the updated HTML can display Share but the WebView navigator.share path may be absent.
- Pre-edit backup branch: backup/native-share-bridge-query-fix-2026-11-13. Exact files were created, re-fetched, and verified byte-identical:
  - backups/web-source-before-native-share-bridge-query-fix-2026-11-13.html — blob SHA 3e585702b5560f9a7785c54895ad4e3769380bd4
  - backups/diary-web-before-native-share-bridge-query-fix-2026-11-13.html — same blob SHA
  - backups/latest-before-native-share-bridge-query-fix-2026-11-13.json — blob SHA 49cc95f5dc16c4061c8cea988867f638fe26b8a1
  - backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-native-share-bridge-query-fix-2026-11-13.md — blob SHA 6f6d335fdd616c59ac89155324f3bd78e225f4c8
- Changed only web-source/index.html in source commit 73eb6df12d880121cc54b3c0d2664577ca990065, blob SHA ab23175252a017f0d19f5064969685a02d5044a9. Added a direct DiaryNativeShare bridge path for the already-composed PNG, before the Web Share API fallback. It reads the PNG as a data URL, sends the base64 image through the existing native bridge, and displays the native bridge success/error response. The same helper also covers the existing direct canvas-share fallback path. Browser Chrome continues to use the existing navigator.share path when the Android bridge is absent. No note composition, images, storage, PIN, native source, APK, or app identity was changed.
- Both inline JavaScript blocks in the patched source passed new Function syntax parsing. Targeted checks confirmed the native bridge helper and both call sites exist.
- Publisher workflow Publish My Diary web-only update, run 43410604332, run 156, head SHA 73eb6df12d880121cc54b3c0d2664577ca990065, completed with conclusion success; publish job 131835762093 succeeded. Publisher output commit 134cd248d3995b1a2926e7e084fe5498addf721b changed only diary-web/index.html and latest.json.
- Live feed reports webVersion 166, web SHA-256 1f9f4bb9707eb562f696f752d11868724a277a5c122edcff9531d5f32d6c89b9; the exact digest was emitted by the successful publisher workflow. Re-fetched source and mirror are byte-identical; both blob SHA ab23175252a017f0d19f5064969685a02d5044a9, both 289,637 characters.
- APK remains unchanged at 1.0.136, versionCode 135, SHA-256 6fc74ca82888fed4121cc352c1846ec8c6a7063e2d2a33fbe032726f7a244348. This is a web-only patch; no APK rebuild or signing change.
- Physical phone verification remains pending. User should run Me → Check for Updates, open an unlocked note, wait for the Share button to appear, and tap it once. Do not claim success until the Android share sheet actually opens with the composed Diary PNG attached. If it fails, capture the visible status/error; do not repeatedly tap or assume a device-side success.
- Rollback: exact pre-edit files are preserved on backup/native-share-bridge-query-fix-2026-11-13. Preserve local notes, photos, PIN data, and app identity.


---

# Web Update 167 — Mobile Diary left/right border fit (2026-11-13)

- User reported that the left and right border lines of the opened Diary panel are slightly clipped on mobile. The CSS sizing was the cause: the panel had `width:min(760px,100%)` with a 2px border but no mobile `border-box`, allowing the border to extend beyond the overlay's available width.
- Changed only `web-source/index.html`: added the isolated `diary-mobile-border-fit` CSS rule for screens up to 420px, setting `#diaryMyNotesPanel` to `box-sizing:border-box`, `width:100%`, and `max-width:100%`. This keeps the existing left/right border lines inside the mobile panel width. No vertical positioning, border style/colour, panel content, gesture behaviour, note/share code, translations, data/storage, PIN/recovery, native Android source, APK, package identity, or signing data changed.
- Starting live state: feed Web Update 166; APK 1.0.136 / versionCode 135; package `com.personal.diaryapp`. Source/mirror prior blob SHA `ab23175252a017f0d19f5064969685a02d5044a9`; prior feed SHA-256 `1f9f4bb9707eb562f696f752d11868724a277a5c122edcff9531d5f32d6c89b9`.
- Reconciled the stale status line at the top of this register: it incorrectly said Web Update 163 while the live feed was 166. The live feed was treated as authoritative. Current header now reflects Web Update 167 and its exact feed SHA-256.
- Pre-edit backup branch: `backup/pre-mobile-diary-border-fit-2026-11-13`. Exact backups created and re-fetched byte-identically:
  - `backups/web-source-before-mobile-diary-border-fit-2026-11-13.html` — blob `ab23175252a017f0d19f5064969685a02d5044a9`
  - `backups/diary-web-before-mobile-diary-border-fit-2026-11-13.html` — blob `ab23175252a017f0d19f5064969685a02d5044a9`
  - `backups/latest-before-mobile-diary-border-fit-2026-11-13.json` — blob `bc7fdc05e1e83f548b1e7b1d67a26a9e2bee502c`
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-mobile-diary-border-fit-2026-11-13.md` — blob `643101011d6490c9ac60c2ab851f3655735f9d6f`
- Source patch commit: `c1f1723c44c2f7e86710561903ee32459abfa4a2`; source blob `00737e4bfe34a875dd1099555d9d6ff67381b472`. Both inline JavaScript blocks parsed successfully; the added CSS braces are balanced and the mobile-only selector was confirmed in the final source.
- Publisher output commit: `dede972e9c906579a59dd12fd4fa57eb852fd6b2` (“Publish My Diary web bundle update”), changing only `diary-web/index.html` and `latest.json`. Live source and mirror were re-fetched and are byte-identical, both blob SHA `00737e4bfe34a875dd1099555d9d6ff67381b472`. Independently computed UTF-8 SHA-256 `87a7d661f06322370dfe5ac87a7aef555eeaeb6844c82ffe302465c9f3b53751` matches `latest.json.webSha256`; live feed is Web Update 167.
- APK unchanged: 1.0.136 / versionCode 135; APK SHA-256 `6fc74ca82888fed4121cc352c1846ec8c6a7063e2d2a33fbe032726f7a244348`. No APK rebuild or signing changes.
- Physical-device verification pending. User should use the existing **Me → Check for Updates** path and confirm that both vertical border lines are now fully visible on the mobile screen. Do not claim phone-side success until the user confirms.
- Rollback: restore the exact pre-edit HTML files from `backup/pre-mobile-diary-border-fit-2026-11-13`; preserve all notes, photos, settings, and PIN data.


---

# Web Update 168 — Reduce mobile Diary panel width by 10px total (2026-11-13)

- User confirmed the previous border fit was still clipped and specified: reduce the total panel width by 10px. Applied exactly 10 CSS pixels total, equivalent to 5px on each side, on screens up to 420px.
- Starting live state: Web Update 167; APK 1.0.136 / versionCode 135; package `com.personal.diaryapp`. Source/mirror prior blob SHA `00737e4bfe34a875dd1099555d9d6ff67381b472`; prior feed SHA-256 `87a7d661f06322370dfe5ac87a7aef555eeaeb6844c82ffe302465c9f3b53751`.
- Changed only `web-source/index.html`, in the existing `diary-mobile-border-fit` CSS block: `width:calc(100% - 10px)`, matching `max-width`, and auto left/right margins. The existing `box-sizing:border-box` and 420px mobile breakpoint remain. No height, vertical position, border thickness/colour/style, panel content, feature logic, gestures, Share, translations, notes/photos, storage, PIN/recovery, native Android source, APK, package identity or signing data changed.
- Pre-edit backup branch: `backup/pre-mobile-diary-border-10px-2026-11-13`. Exact backups created, re-fetched and verified byte-identical:
  - `backups/web-source-before-mobile-diary-border-10px-2026-11-13.html` — blob `00737e4bfe34a875dd1099555d9d6ff67381b472`
  - `backups/diary-web-before-mobile-diary-border-10px-2026-11-13.html` — same blob
  - `backups/latest-before-mobile-diary-border-10px-2026-11-13.json` — blob `77fa17c622e285ad4073dd4f9fe84d838a42b34f`
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-mobile-diary-border-10px-2026-11-13.md` — blob `461ee2c49201bee05fbaf0588e3cd9dab19b10bd`
- Source patch commit `c2c795b47b55a17ce9c0fbb521d57b4305c6b650`; final source blob `d1b173fa83ee5cb85ffdc780d14205a0ee1a0402`. Both inline JavaScript blocks parsed successfully; mobile CSS braces balanced; targeted checks confirmed 10px total width reduction, horizontal centering, and no height/top/bottom changes.
- Publisher workflow run `43413910094`, run 158, completed successfully; publish job `131846909543` succeeded. Publisher output commit `0071dba5a93091b6cea858a33b112a53f93c9a40` updated the published mirror and feed. Re-fetched source and mirror are byte-identical, both blob SHA `d1b173fa83ee5cb85ffdc780d14205a0ee1a0402`.
- Live feed advanced to Web Update 168. Independently calculated UTF-8 SHA-256 `e6d08089a138d3fc2026eceff7db1fcd5f247eda92ed4f616ca54b60e70d8b09`, matching `latest.json.webSha256`.
- APK unchanged: 1.0.136 / versionCode 135; SHA-256 `6fc74ca82888fed4121cc352c1846ec8c6a7063e2d2a33fbe032726f7a244348`. Web-only update; no APK rebuild or signing changes.
- Physical-device verification pending. User should use **Me → Check for Updates** and inspect only the left/right border lines. Do not claim the phone-side clipping is fixed until the user confirms.
- Rollback: exact pre-edit files are preserved on `backup/pre-mobile-diary-border-10px-2026-11-13`; restore only the affected HTML if required. Preserve notes, photos, settings and PIN data.


---

# Web Update 169 — Fix mobile Diary left/right border clipping (2026-11-13)

- User reported that the left/right border lines were still clipped after Web Update 168 and asked to correct them. Re-inspection found that the Diary panel is a flex item inside `#diaryMyNotesOverlay`; its default `min-width:auto` can prevent the panel from shrinking below its automatic content minimum. The overlay also already has 10px horizontal padding.
- Starting live state: Web Update 168; APK 1.0.136 / versionCode 135; package `com.personal.diaryapp`. Prior source/mirror blob SHA `d1b173fa83ee5cb85ffdc780d14205a0ee1a0402`; prior feed SHA-256 `e6d08089a138d3fc2026eceff7db1fcd5f247eda92ed4f616ca54b60e70d8b09`.
- Changed only the existing `diary-mobile-border-fit` block in `web-source/index.html`, source commit `f8bc9dbc4d85fc0f892bfe86533fd81bcf662549`: added `min-width:0` and `flex:0 1 auto` so the flex item can shrink; increased the panel width reduction from 10px to 20px total (`width` and `max-width:calc(100% - 20px)`), keeping auto horizontal margins, border-box sizing and the existing 420px breakpoint. This creates an additional 10px of total clearance compared with Web Update 168. No vertical position/height, border thickness/colour/style, panel content, features, gestures, Share, translations, notes/photos, storage, PIN/recovery, native Android source, APK, package identity or signing data changed.
- Pre-edit backup branch: `backup/pre-border-clip-followup-2026-11-13`. Exact readable backups re-fetched and verified byte-identical:
  - `backups/web-source-before-border-clip-followup-2026-11-13.html` — blob `d1b173fa83ee5cb85ffdc780d14205a0ee1a0402`
  - `backups/diary-web-before-border-clip-followup-2026-11-13.html` — same blob
  - `backups/latest-before-border-clip-followup-2026-11-13.json` — blob `dc0794b352f5532034b0bf62ff37c7b62984eb54`
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-border-clip-followup-2026-11-13.md` — blob `50a36e60e4ae52233c19f943e1a29322e2ee3241`
- Diff was limited to the single existing mobile CSS block. The CSS block braces are balanced; targeted checks confirmed the new shrink allowance, 20px total panel width reduction, centering, unchanged 420px breakpoint and unchanged vertical rules. JavaScript and application logic were not modified.
- Web-only publisher workflow run `43415645933`, run 159, completed with **success**; publish job `131852720937` succeeded. Publisher output commit: `6755760a81ca382438f620c4dcac151d4dbe8b78`. Live source and published mirror are byte-identical; both blob SHA `5dddf6c526402e6300ddb1028f746c45fd6c5c6a`. Independently calculated UTF-8 SHA-256 `3aa66bec80991551df39d9de3807552ae76b15cab47eb8d5dd9bc3b6bdff0a94` matches live `latest.json.webSha256`; live `webVersion=169`.
- APK unchanged: 1.0.136 / versionCode 135; SHA-256 `6fc74ca82888fed4121cc352c1846ec8c6a7063e2d2a33fbe032726f7a244348`. No APK rebuild or signing changes.
- Physical-device verification **pending**. User should use **Me → Check for Updates**, then inspect the left/right border lines. Do not claim phone-side success until user confirms.
- Rollback: restore only the pre-edit HTML from the verified backup branch if needed; preserve notes, photos, settings and PIN data.


---

# Web Update 170 — Further mobile Diary border clearance (2026-11-13)

- User reported that the left/right Diary panel border remained clipped after Web Update 169. Checked the actual native update path in the generated Android project script: the “Diary pehle se update hai” response is shown when the installed `filesDir/diary-web/index.html` SHA-256 already matches the current feed hash; it then clears WebView cache and reloads the verified local file. Therefore this message did not mean the new CSS was skipped; it meant the current Web Update 169 HTML was already installed.
- Rechecked the exact mobile CSS and confirmed Web Update 169 had the panel at `calc(100% - 20px)`, with `box-sizing:border-box`, `min-width:0`, flex shrink, and centered auto margins. The overlay itself has 10px padding, and the Diary panel has raised 3D edge/shadow styling. To provide additional visible clearance without changing vertical layout or 3D border styling, increased only the panel's mobile total width reduction by a further 10px: `width` and `max-width:calc(100% - 30px)`, i.e. 15px each side. Existing 420px breakpoint, flex shrink, min-width, box sizing, and centering remain.
- Starting state: Web Update 169; APK 1.0.136 / versionCode 135; package `com.personal.diaryapp`. Source/mirror prior blob SHA `5dddf6c526402e6300ddb1028f746c45fd6c5c6a`; feed hash `3aa66bec80991551df39d9de3807552ae76b15cab47eb8d5dd9bc3b6bdff0a94`.
- Changed only the existing `diary-mobile-border-fit` CSS block in `web-source/index.html`, source commit `4b56f17247c5a962d601fe0446f57770694c3a9a`, final source blob `06dc67027578c3a9ce8dfc6922f8aef0cca114e4`. No height, top/bottom position, border thickness/colour/style, panel content, application logic, translations, notes/photos, storage, PIN/recovery, native Android source, APK, package identity or signing data changed.
- Pre-edit backup branch: `backup/pre-mobile-border-fit-30px-2026-11-13`. Exact backups re-fetched and verified identical:
  - `backups/web-source-before-mobile-border-fit-30px-2026-11-13.html` — blob `5dddf6c526402e6300ddb1028f746c45fd6c5c6a`
  - `backups/diary-web-before-mobile-border-fit-30px-2026-11-13.html` — same blob
  - `backups/latest-before-mobile-border-fit-30px-2026-11-13.json` — blob `7511095bbdbf8b20386507f532acb06199eaad3a`
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-mobile-border-fit-30px-2026-11-13.md` — blob `048b0800312cd866d45c0a9c53389589e0990154`
- Diff limited to the one existing mobile CSS block; exact selector and declarations checked; braces balanced. Web-only publisher workflow run `43416391968`, run 160, completed successfully; publish job `131855257914` succeeded. Live source and published mirror are byte-identical, blob SHA `06dc67027578c3a9ce8dfc6922f8aef0cca114e4`. Independently calculated UTF-8 SHA-256 `ff55b50443518dc79d7384e6bcb6131d4bed7b957c1bab416150b44e91ac742e` matches live `latest.json.webSha256`; live `webVersion=170`.
- APK unchanged: 1.0.136 / versionCode 135; SHA-256 `6fc74ca82888fed4121cc352c1846ec8c6a7063e2d2a33fbe032726f7a244348`. No APK rebuild or signing changes.
- Physical-device verification pending. User should tap **Me → Check for Updates**; if the checker again reports already updated, it indicates the installed HTML hash is current. Then inspect the left/right outer border. Do not claim phone-side success until the user confirms.
- Rollback: exact pre-edit files preserved on `backup/pre-mobile-border-fit-30px-2026-11-13`; preserve all notes, photos, settings and PIN data.


---

# Web Update 171 — Center Diary panel to equal mobile screen gutters (2026-11-13)

- User reported that the Diary page did not appear evenly fitted to the mobile screen: moving the page left or right caused one side to move inward while the other remained clipped. The earlier mobile rule subtracted a second percentage from a flex overlay that already had 10px horizontal padding, making panel width depend on the padded content box rather than directly using the available screen width.
- Starting state: Web Update 170; APK 1.0.136 / versionCode 135; package `com.personal.diaryapp`. Starting source/mirror blob SHA `06dc67027578c3a9ce8dfc6922f8aef0cca114e4`; feed SHA-256 `ff55b50443518dc79d7384e6bcb6131d4bed7b957c1bab416150b44e91ac742e`.
- Changed only the existing `diary-mobile-border-fit` CSS block in `web-source/index.html`, source commit `b46f11410de693e98bd61ba6f710348c7f3ab2a7`. Removed the `calc(100% - 30px)` width rule. The overlay now supplies symmetric left/right gutters using `max(12px, env(safe-area-inset-left/right, 0px))`; the Diary panel uses `width:100%`, `max-width:760px`, `min-width:0`, a shrinkable flex basis, and auto side margins. This makes the panel fit the overlay's actual available width and keeps it centered without independent left/right nudging.
- No panel height, vertical position, border thickness/colour, 3D border/shadow, Diary content, translations, notes/photos, storage keys, PIN/recovery, native Android source, APK, package identity or signing data changed. Full source commit diff reviewed: only the one existing CSS block changed.
- Pre-edit backup branch: `backup/pre-centered-mobile-diary-panel-2026-11-13`. Verified readable exact backups:
  - `backups/web-source-before-centered-mobile-diary-panel-2026-11-13.html` — blob `06dc67027578c3a9ce8dfc6922f8aef0cca114e4`
  - `backups/diary-web-before-centered-mobile-diary-panel-2026-11-13.html` — same blob
  - `backups/latest-before-centered-mobile-diary-panel-2026-11-13.json` — blob `2d846ca0573d03840885a5ccc3629996dbd1da69`
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-centered-mobile-diary-panel-2026-11-13.md` — blob `f409ccea7adaef3d6d90c6d4cb060142594db751`
- Web-only publisher workflow run `43417578157`, run 161, completed with **success**; publish job `131859266460` succeeded. Publisher advanced live feed to webVersion `171`. Re-fetched source and published mirror are byte-identical; both Git blob SHA `a47e48aa1eb74cd5f44ec655764ece6ce97ad532`. Independently calculated UTF-8 SHA-256 `51bb5ed38c96f360fa9de1ddb75faea159805f4a19e45c5844912f9d1598ad42` matches live `latest.json.webSha256`.
- APK unchanged: 1.0.136 / versionCode 135; SHA-256 `6fc74ca82888fed4121cc352c1846ec8c6a7063e2d2a33fbe032726f7a244348`. No APK rebuild or signing changes.
- Physical-device verification **pending**. User should use **Me → Check for Updates**, then inspect whether the left and right outer borders have equal space and both remain fully visible. Do not claim the phone-side issue is fixed until the user confirms.
- Rollback: exact pre-edit files preserved on `backup/pre-centered-mobile-diary-panel-2026-11-13`; preserve all Diary notes, photos, settings and PIN data.


---

# Web Update 172 — Fit locked Note card and PIN controls on mobile (2026-11-13)

- User clarified that the left/right clipping is noticed specifically when a Note is locked, not on the general Diary page. Starting state: Web Update 171; APK 1.0.136 / versionCode 135; package `com.personal.diaryapp`; starting source blob `a47e48aa1eb74cd5f44ec655764ece6ce97ad532`; starting feed SHA-256 `51bb5ed38c96f360fa9de1ddb75faea159805f4a19e45c5844912f9d1598ad42`.
- Changed only a new CSS block `diary-note-lock-mobile-fit` in `web-source/index.html`. It targets the expanded locked Note card containing the `diary-note-pin` input, constrains that card to the available list width with border-box sizing and zero minimum width, and keeps the PIN field and its content within the card. No Note Lock/Unlock logic or PIN/recovery data was changed.
- The general Diary panel sizing CSS from Web Update 171 was left untouched. No notes, photos, settings, translations, storage keys, PIN/recovery logic, native Android source, APK, package identity or signing data changed.
- Pre-edit backup branch: `backup/pre-note-lock-mobile-fit-2026-11-13`. Backups preserved:
  - `backups/web-source-before-note-lock-mobile-fit-2026-11-13.html` — pre-edit source blob `a47e48aa1eb74cd5f44ec655764ece6ce97ad532`
  - `backups/diary-web-before-note-lock-mobile-fit-2026-11-13.html` — exact pre-edit published mirror
  - `backups/latest-before-note-lock-mobile-fit-2026-11-13.json`
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-note-lock-mobile-fit-2026-11-13.md`
- Source commit `72d68e7b9cb8f69bc9adfb24d5c341dc1cdfff58`. Web-only publisher workflow run `43418912556`, run 162, completed successfully. Live feed advanced to webVersion `172`; live `webSha256=3c17afe300473dd43e98201423961390ef431c1b01fca408795489559f71a7e2`. Source and published mirror are byte-identical; both blob SHA `34a031dedbdc94d50a861abb40b32a4dbb310125`.
- APK unchanged: 1.0.136 / versionCode 135; SHA-256 `6fc74ca82888fed4121cc352c1846ec8c6a7063e2d2a33fbe032726f7a244348`. No APK rebuild or signing changes.
- Physical-device verification **pending**. Ask the user to use **Me → Check for Updates**, then lock a Note and check whether the locked Note card and both side borders fit evenly inside the mobile screen. Do not claim the phone-side issue is fixed until the user confirms.
- Rollback: exact pre-edit files preserved on `backup/pre-note-lock-mobile-fit-2026-11-13`; preserve all Diary notes, photos, settings and PIN data.


---

# Web Update 173 — Stack and enlarge locked Note PIN action buttons (2026-11-13)

- User reported that the text on the locked Note actions “❓ PIN Bhool Gaye?” and “🔓 Tala Band Karein” overflowed their buttons while the buttons were side-by-side. User requested larger buttons arranged vertically.
- Starting state: Web Update 172; APK 1.0.136 / versionCode 135; package `com.personal.diaryapp`; starting source/mirror blob SHA `34a031dedbdc94d50a861abb40b32a4dbb310125`; prior feed SHA-256 `3c17afe300473dd43e98201423961390ef431c1b01fca408795489559f71a7e2`.
- Changed only the locked Note PIN action controls in `web-source/index.html`: their wrapper now uses a vertical flex column with full width and spacing; each button is full width, minimum 46px high, larger 14px bold text, increased padding, and wrapping enabled so localized labels stay inside. Button event handlers and PIN/lock behaviour remain unchanged.
- No other Note cards, general Diary layout, languages/translations, notes/photos/storage, PIN/recovery data or logic, native Android source, APK, package identity or signing data changed.
- Pre-edit backup branch: `backup/pre-note-lock-action-buttons-stack-2026-11-13`. Exact pre-edit source, published mirror, `latest.json`, and this Master Register were backed up under `backups/*-before-note-lock-action-buttons-stack-2026-11-13.*` on that branch.
- Source commit `34a9cc0804793fd7c3d4e6c16c1aea411d06ce54`; final source/mirror blob SHA `09a97742b81d4ba6794fc59bd3054b34f08d6fd0`. Publisher workflow run `43419663486`, run 163, completed successfully; publish job `131866187842` succeeded. Live feed advanced to webVersion `173`; live `webSha256=73175c989ab35b7f72f5358336c056cc39e4112b036d71232f6b5c0b1fdc1d6f`. Re-fetched source and published mirror are byte-identical.
- APK unchanged: 1.0.136 / versionCode 135; SHA-256 `6fc74ca82888fed4121cc352c1846ec8c6a7063e2d2a33fbe032726f7a244348`. Web-only update; no APK rebuild or signing changes.
- Physical-device verification **pending**. User should use **Me → Check for Updates**, open a locked Note, and confirm the two action buttons appear one above the other with all text inside. Do not claim phone-side success until user confirms.
- Rollback: restore the exact pre-edit HTML from `backup/pre-note-lock-action-buttons-stack-2026-11-13`; preserve notes, photos, settings and PIN data.


---

# Web Update 174 — Confirm discard when closing an unsaved New Note (2026-11-13)

- User requested an × close control flow while writing a new Note: ask before removing the unfinished writing.
- Starting live state: Web Update 173; APK 1.0.136 / versionCode 135; package `com.personal.diaryapp`; starting source/mirror blob SHA `09a97742b81d4ba6794fc59bd3054b34f08d6fd0`; previous feed SHA-256 `73175c989ab35b7f72f5358336c056cc39e4112b036d71232f6b5c0b1fdc1d6f`.
- Changed only the × button click handler and the three existing language dictionaries (Roman English, English, Hindi). When a new unsaved draft contains text, a cover/details/photo attachment, or a selected image colour, × asks for confirmation. Confirming resets only the in-memory new draft using the existing `newNote()` reset routine and closes the Diary. Choosing Cancel leaves the draft and editor open. Closing an existing saved Note does not ask and does not alter it. The overlay backdrop and Escape/Android Back paths were not changed.
- Existing save flow, note storage format/keys, saved Notes, photos already saved, PIN/lock/recovery, search, editor layout, native Android code, APK, package identity and signing data were not changed.
- Pre-edit backup branch: `backup/pre-new-note-close-discard-2026-11-13`. Exact pre-edit files were saved and re-fetched:
  - `backups/web-source-before-new-note-close-discard-2026-11-13.html` — blob `09a97742b81d4ba6794fc59bd3054b34f08d6fd0`
  - `backups/diary-web-before-new-note-close-discard-2026-11-13.html` — same blob
  - `backups/latest-before-new-note-close-discard-2026-11-13.json` — blob `b1a5ed98412646aead746ce24b3e314d6d63887e`
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-new-note-close-discard-2026-11-13.md` — blob `23d0d6defa08ff15569be16d7c98b348a9ac034b`
- Source commit `572f82fa2fd35bbe7212813fb47ad3df83499491`; final source blob `ca8b9420b1c8ef58312d4fe627f6bffeaf312239`. The web-only publisher workflow run `43426737220`, run 164, completed successfully; publish job `131889866019` succeeded. Live feed advanced to webVersion `174`; live `webSha256=c3ed3642eea1d28e18bdb1705939466ef4aa623ed0260879f9209b3273246bd5`. Re-fetched source and published mirror are byte-identical (same blob SHA).
- APK unchanged: 1.0.136 / versionCode 135; SHA-256 `6fc74ca82888fed4121cc352c1846ec8c6a7063e2d2a33fbe032726f7a244348`. Web-only release; no APK rebuild or signing changes.
- Physical-device verification **pending**. User should use **Me → Check for Updates**, open **＋ New Note**, type a short test, and tap ×. Confirm should discard and close; Cancel should keep the text and editor open. Also verify an empty New Note closes without a confirmation. Do not claim phone-side success until the user confirms.
- Rollback: restore the exact pre-edit HTML from `backup/pre-new-note-close-discard-2026-11-13`; preserve all notes, photos, settings and PIN data.

## Web Update 175 — New Note page par alag × se sirf draft clear (2026-11-13)
- User clarified the intended behavior: New Note editor visible rahe; uske apne × par tap karne se typed title/body aur added draft images/content clear ho, editor band na ho.
- Added a separate × control at the top of `diaryMyNotesEditor`. It calls the existing `newNote()` reset routine, so draft text, draft photo/image data and draft formatting reset while the writing pad stays visible. No extra confirmation dialog is shown.
- The separate editor × is shown for a new unsaved note and hidden while editing an existing saved note.
- Restored the main Diary overlay close button to its original direct `closeOverlay` behavior. It no longer contains the earlier mistaken draft-discard logic.
- No changes to saved Notes, storage format, existing Note lock/PIN/recovery, share, search, APK/native code, package identity or signing.
- Source commit: `131794e2f32a58a62fa85b33bbf0504202caa3db`; source/mirror blob SHA: `39e326970ad28dc3462c50e92edb4fbe6b396c96`. `web-source/index.html` and `diary-web/index.html` were re-fetched and verified byte-identical.
- Publisher workflow run `43427869229` (run 165), publish job completed successfully. Live `latest.json` reports webVersion `175`, webSha256 `8785bf67609495c847d21a6248fa9b9cdf886852788fd38959760e58d57b0b19`.
- Physical-device test pending. User should use **Me → Check for Updates**, open **＋ New Note**, type something and add a photo, then tap the new ×. Confirm the text/photo clear and the writing pad remains open. Do not claim phone-side verification until user confirms.

## Web Update 176 — New Note × sirf draft par visible (2026-11-13)
- User confirmed: × should remain hidden while New Note is empty, appear only after text is typed or an image is added, and disappear again when tapped to clear the draft.
- Implemented live visibility updates for title/body typing and the existing photo, cover-image and detail-image preview completion paths. The button is shown only for an unsaved New Note with draft content. Tapping it calls the existing `newNote()` reset routine; it clears draft text/images and leaves the writing pad open.
- No change to saved-note editing behavior, main Diary close button, saved notes/storage, Note lock/PIN/recovery, APK/native code, package identity or signing.
- Source commit: `993551bb9455f12b028d0b2df97c24e2997ec653`; source and published mirror were re-fetched and verified byte-identical, blob SHA `098ec07a4f0ef8205a7b42367304c1b033b4d665`.
- Publisher workflow run `43428578542`, run 166, and publish job completed successfully. Live `latest.json` reports webVersion `176`, webSha256 `19d6828ff323f044df54e8c1bac450da63a0f3e0ca72505672994119a95cb01b`.
- Physical-device verification pending. User should use **Me → Check for Updates**, then test: empty New Note has no ×; typing or adding an image shows ×; tapping × clears the draft and hides × while keeping the pad open. Do not claim phone-side verification until user confirms.

## Web Update 177 — New Note × hide/show CSS correction (2026-11-13)
- User reported the clear × remained visible after tapping it to clear the draft.
- Re-inspection found the button's CSS explicitly set `display:block`, which could override the browser's built-in `hidden` behavior. Removed that display declaration and switched the visibility function to the button's `hidden` property. The click handler now also refreshes visibility after the existing `newNote()` reset.
- Source commit: `2f5bc69a2dbf38774df5c3092306912e0d597d80`; source and published mirror re-fetched and verified byte-identical, blob SHA `bdd72933f3c238957a893bc3cfcb1e0d61143823`.
- Publisher workflow run `43428899194`, run 167, publish job completed successfully. Live `latest.json` reports webVersion `177`, webSha256 `8c22fecf2a7112996490b66417fea86ced92161a925ae1a9dbb201d5f432305d`.
- Physical-device verification pending. Test after **Me → Check for Updates**: empty New Note hides ×; text/image makes it appear; tapping × clears the draft and hides ×.


## Web Update 178 — New Note clear × right side restored (2026-11-13)
- User clarified that only the separate × on the New Note writing pad had shifted to the left; it must return to the right. Kept the editor, title/body fields, images, visibility behavior, clear action, main Diary close button, saved notes, and all other functions unchanged.
- Root cause: the clear × is a button (inline-block by default), so its auto left margin did not reliably align it to the right. Changed only its visible-state CSS selector to `#diaryMyNotesDraftClearX:not([hidden])` and set `display:block`; retained the existing right-aligning auto margin. Using the `:not([hidden])` selector preserves native hidden behavior when the draft is empty or after clearing.
- Exact pre-edit files backed up on branch `backup/new-note-clear-x-right-2026-11-13`: `backups/web-source-before-new-note-clear-x-right-2026-11-13.html`, `backups/diary-web-before-new-note-clear-x-right-2026-11-13.html`, `backups/latest-before-new-note-clear-x-right-2026-11-13.json`, and `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-new-note-clear-x-right-2026-11-13.md`.
- Source commit: `5efa345f140541b0055aa1135b4100257ddbe4d9`; source blob `7046e907a57068ad8f07f7707d4d69ed3cfe7dc7`. Web publisher workflow run `43429955889` completed successfully. Live webVersion is `178` with webSha256 `df38b4c0af55507788b9187f0ff05c6bdb1d21c7af2594765bb6ae61c8d9aaa7`.
- Re-fetched source and published mirror are byte-identical (blob SHA `7046e907a57068ad8f07f7707d4d69ed3cfe7dc7`). APK remains unchanged at 1.0.136 / versionCode 135; no APK rebuild or signing changes.
- Physical-device verification pending. Use **Me → Check for Updates**, open **＋ New Note**, type a short test, and confirm the × appears on the right. Tap it and confirm the draft clears, the × disappears, and the writing pad remains open. Empty New Note should keep × hidden.


---

# Web Update 180 — Show and support clear × while editing saved Notes (2026-11-13)

- User request: while editing an existing saved Note, show the same editor-page × clear control used for a New Note and make it clear the current editor content in the same way.
- Starting live state: Web Update 179; APK 1.0.136 / versionCode 135; package com.personal.diaryapp; source/mirror blob SHA 4996fe1441e649f29c772c058f06bbcf9470e500; prior feed SHA-256 14a3ef144df495d1919fc2a5f4b93f35ddda0a76b69adcec4b81ac43ab9749af.
- Web-only scope: changed only web-source/index.html. The clear × is now visible in saved-note edit mode whenever the editor contains a title, body, attached photo, cover/detail image, or cover/detail text. Tapping it uses the existing New Note reset routine to clear the in-memory editor fields and image data, then restores the current saved note ID, category and Delete button so the user remains in Edit mode. The existing note is not written to storage or deleted by ×; any subsequent save continues to target that same note. The existing non-empty save validation remains unchanged.
- The clear × visibility refreshes when an existing Note is opened. New Note visibility and behavior remain unchanged. The existing Note close button, save logic, note data format/storage keys, photos in saved records, PIN/lock/recovery, translations, updater, pamphlet-template backward compatibility, native Android source, APK, package identity and signing data were not changed.
- Pre-edit backup branch: backup/edit-note-clear-x-2026-11-13. Four files were created and re-fetched readable:
  - backups/web-source-before-edit-note-clear-x-2026-11-13.html — pre-edit source blob 4996fe1441e649f29c772c058f06bbcf9470e500
  - backups/diary-web-before-edit-note-clear-x-2026-11-13.html — exact pre-edit published mirror
  - backups/latest-before-edit-note-clear-x-2026-11-13.json — pre-edit feed
  - backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-edit-note-clear-x-2026-11-13.md — pre-edit register
- Source commit: 2abb20b5d958f61703d8a594f1d236c64dee8a67. The full diff was reviewed and contains only the clear × click routing, visibility gate, edit-draft reset helper, and openNote visibility refresh. Both inline JavaScript blocks parsed successfully. Targeted static checks confirmed the × routes New Note to its original reset and saved-note Edit to the new edit-preserving reset; the edit reset restores the active note ID/category and Delete control; openNote refreshes × visibility.
- Web publisher workflow run 43432343803 (run 170) completed with **success**; publish job and all steps succeeded. Publisher commit: 4801bcdda217afe4ad4335c21fcaca7937dfd17e. Live source and published mirror are byte-identical; both blob SHA b612bde3339702f5c80feb63d5189531613bf504. Independently computed UTF-8 SHA-256 ddf7e372e7eaa03b294069059fb75f6b6894fc201ccd0fe583feb6cd2b4dc4a9 matches live latest.json webSha256. Live webVersion is 180.
- APK unchanged: 1.0.136 / versionCode 135 / SHA-256 6fc74ca82888fed4121cc352c1846ec8c6a7063e2d2a33fbe032726f7a244348. No APK rebuild or signing changes.
- Physical-device verification pending. User should use Me → Check for Updates, open a saved Note with existing text/photo, confirm × appears, tap × and confirm text/images clear while the same Note remains in Edit mode; then type replacement text and confirm Save updates that same Note. Also confirm New Note × behavior remains unchanged. Do not claim phone-side verification until user confirms.
- Rollback: exact pre-edit source, mirror, feed and register are preserved on backup/edit-note-clear-x-2026-11-13. Restore only the affected HTML if a regression is found; preserve saved notes, photos, settings and PIN data.


# Web Update 179 — Remove Pamphlet Chunein button (2026-11-13)

- User requested removal of the **🪄 Pamphlet Chunein** button.
- Starting live state: APK `1.0.136` / versionCode `135`; webVersion `178`; package `com.personal.diaryapp`; source/mirror blob SHA `7046e907a57068ad8f07f7707d4d69ed3cfe7dc7`; prior feed SHA-256 `df38b4c0af55507788b9187f0ff05c6bdb1d21c7af2594765bb6ae61c8d9aaa7`.
- Scope: web-only, only `attachDiaryColourChooser(kind)` in `web-source/index.html`. Removed creation and event handling of the Pamphlet Chunein button and its chooser gallery from the three existing image controls (Cover, Details, attached Photo). The existing Choose Image, Solid Colour and Gradient Colour controls remain.
- Preserved backward compatibility: existing saved notes that already contain a pamphlet template ID still render with their stored design. `cleanDiaryColour`, `diaryPamphletStyle`, saved-note preview, image rendering and share artwork template support were not removed. Existing notes, photos, storage, PIN/recovery, translations, updater, native Android source, APK, package identity and signing data were not changed.
- Pre-edit backup branch: `backup/pre-remove-pamphlet-button-2026-11-13`. Four exact files were created and re-fetched byte-identically:
  - `backups/web-source-before-remove-pamphlet-button-2026-11-13.html` — blob `7046e907a57068ad8f07f7707d4d69ed3cfe7dc7`
  - `backups/diary-web-before-remove-pamphlet-button-2026-11-13.html` — same blob
  - `backups/latest-before-remove-pamphlet-button-2026-11-13.json` — blob `c171744f7da41c477014fe93846afea12f91f15f`
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-remove-pamphlet-button-2026-11-13.md` — blob `4eda91076b66ee4a08a745cdf6a38e2f609d0479`
- Source change commit: `1acb4e1ec1d369cce8b6c2b25f8b34ee81202eb7`; source blob SHA `4996fe1441e649f29c772c058f06bbcf9470e500`. The exact source diff was reviewed: it deletes only the pamphlet button/gallery construction and removes the button/gallery from the image chooser menu assembly.
- Both inline JavaScript blocks parsed successfully. Targeted checks confirm no runtime pamphlet button/gallery construction or handler remains; image selection, solid colour, gradient colour and the existing saved-template renderer remain.
- Publisher output commit: `230a8a0b31d314569d7d49d7afd1869779406055` (GitHub Actions bot, “Publish My Diary web bundle update”). It changed only `diary-web/index.html` and `latest.json`. Live source and mirror were re-fetched and are byte-identical; both blob SHA `4996fe1441e649f29c772c058f06bbcf9470e500`. Live feed reports webVersion `179` and `webSha256=14a3ef144df495d1919fc2a5f4b93f35ddda0a76b69adcec4b81ac43ab9749af`. The workflow run ID/conclusion was not independently exposed by the available GitHub read endpoint; publisher bot commit and matching live feed/mirror confirm publication, but do not substitute for a separately observed workflow conclusion.
- APK unchanged: `1.0.136` / versionCode `135`; APK SHA-256 `6fc74ca82888fed4121cc352c1846ec8c6a7063e2d2a33fbe032726f7a244348`. No APK rebuild or signing changes.
- Physical-device verification pending. User should use **Me → Check for Updates**, then open each of the three image controls and confirm **Pamphlet Chunein** is absent while **Choose Image**, **Solid Colour**, and **Gradient Colour** remain. Also open an older note that already used a pamphlet design and confirm its saved appearance remains. Do not claim phone-side verification until user confirms.
- Rollback: exact pre-edit source, mirror, feed and register are preserved on `backup/pre-remove-pamphlet-button-2026-11-13`; restore the exact HTML if testing reveals a regression. Preserve notes, photos, settings and PIN data.


---

# Register Policy Update — Mandatory entry for every successful task (2026-11-13)

- User instruction: always add a Master Register entry for work that is completed successfully, and add a standing rule requiring this for all future successful work.
- Added the **MANDATORY SUCCESS-ENTRY RULE** to Section F and a matching mandatory item to the reusable task checklist in Section G. The rule covers all successful work, including small fixes and non-release tasks, and requires evidence plus honest pending/blocked status; chat history is not a substitute for a Register entry.
- The existing **Web Update 180** entry already records the saved-Note clear × implementation, backup, checks, publishing workflow, source/mirror/feed verification, and pending physical-device test. No new code or release was made in this policy-only task.
- Backup: `backup/register-success-entry-rule-2026-11-13` → `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-success-entry-rule-2026-11-13.md`; backup commit `945ca910ee7f2e59af6275197dec0c163096ec10`.
- Scope: only `docs/PROJECT_MAP_AND_SECRETS_REGISTER.md` changed on the default branch. No app source, mirror, latest.json, APK, signing data, notes, photos, settings, or PIN/recovery data changed.
- Verification: live register was fetched before editing; pre-edit register backup was created on a separate backup branch. Post-edit re-fetch and content/section verification are required before reporting completion.


---

# Me Button — Four new independent tools (Web Update 182, 2026-11-13)

- User selected and approved four new Me Button tools in this order: **Personal Calendar**, **My Kharcha**, **My Documents**, **My Memories**. Existing Diary Notes, existing saved-Notes Calendar, Note Lock, Diary Lock/PIN/recovery, updater and existing data must remain untouched.
- Starting live state: Web Update 180; APK 1.0.136 / versionCode 135; package `com.personal.diaryapp`; source/mirror blob `b612bde3339702f5c80feb63d5189531613bf504`; starting feed blob `aa8fadea5b34cd8959410b371b3c86ec06b0abda`.
- Scope: web-only, `web-source/index.html`. Added four separate purple/gold 3D-style buttons under Me, opening an independent feature page:
  - **Personal Calendar:** add and list dated birthday, anniversary and important-day entries.
  - **My Kharcha:** add income/expense entries with date, amount in INR, optional category/details, and running totals/balance.
  - **My Documents:** save and open local image/PDF files with a title.
  - **My Memories:** save dated text memories with an optional photo.
- All four features use a new, separate IndexedDB database `diary_me_features_v1` and object store `records`; they do not reuse or modify the existing Notes storage keys or the Diary safety-copy database. Attachments are stored as local Blob data; file-size limit is 20 MB. User data remains on the device; no cloud upload was added.
- A follow-up correction made optional form fields genuinely optional (the initial version mistakenly emitted a false-valued HTML boolean `required` attribute). Final source includes this correction.
- Explicit limitations for this first version: no edit/search/export-import or integration with the existing Notes backup yet; Personal Calendar currently stores and lists dates but does not send reminders or auto-repeat birthdays/anniversaries. The new database is separate and is **not encrypted by the existing Diary PIN**, so device/app PIN must not be assumed to protect these new records. Physical-device verification is pending; use dummy/test entries only until storage backup and privacy protection are added and tested.
- Pre-edit backup branch: `backup/me-four-features-before-implementation-2026-11-13`. Four exact, readable backups re-fetched successfully:
  - `backups/web-source-before-me-four-features-2026-11-13.html` — original blob `b612bde3339702f5c80feb63d5189531613bf504`
  - `backups/diary-web-before-me-four-features-2026-11-13.html` — same original blob
  - `backups/latest-before-me-four-features-2026-11-13.json` — blob `aa8fadea5b34cd8959410b371b3c86ec06b0abda`
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-me-four-features-2026-11-13.md` — blob `63942493cc15dda564fd9f01961ae47d02137c6c`
- Source commits: initial implementation `23ec8cb253456ecfda775c243a31da1591cd012f`; optional-field correction `524629c81c3c937ea9b1d2fe7996348eb86cf366`.
- Web-only publisher workflow runs: `43435266550` (run 171) and `43435584101` (run 172); both completed **successfully**, including all publish-job steps. Final live webVersion: **182**.
- Final source and published mirror were re-fetched and are byte-identical; both Git blob SHA `2797094230b8a7864d531988d65f33798f44e759`. Independently calculated UTF-8 SHA-256 `436873076a491bd9d8759e7b6506e517469a89fc57c9893b18708f69354c2dd1` matches live `latest.json.webSha256`.
- Both inline JavaScript blocks passed syntax parsing. Static checks confirmed the new feature database, four feature labels/buttons, and optional-field correction. No live-device runtime test was available.
- APK unchanged: 1.0.136 / versionCode 135 / SHA-256 `6fc74ca82888fed4121cc352c1846ec8c6a7063e2d2a33fbe032726f7a244348`. No APK rebuild, native Android, package identity or signing changes.
- Deliberately untouched: existing Notes and their storage, existing saved-Notes Calendar, photos already attached to Notes, Note Lock, Diary Lock/PIN/recovery, translations outside the new feature labels, updater, app sharing, theme controls, and all MUAZZIN project files.
- Phone test pending. Ask the user to use **Me → Check for Updates**, install Web Update 182, then test each feature with dummy data: add/delete one date, one income and one expense, one sample PDF/image document, and one text/photo memory; close and reopen each page to confirm data persists. Do not claim phone-side success until the user confirms.
- Rollback: restore only `web-source/index.html` from the verified pre-edit backup branch if regression is found; then re-run source/mirror/feed/hash checks. Preserve all user data and PIN records.


---

# Web Update 183 — Make My Kharcha amount entry obvious and visible (2026-11-13)

- User reported that the **My Kharcha** page did not show a clear box for entering how much was spent. Live code inspection found the numeric amount input was generated, but its generic label was only “Raqam (₹)” / “Amount (₹)”; the user-facing amount field needed a more explicit label and stronger visual distinction. No assumption was made that the phone had been tested.
- Starting live state: Web Update 182; APK 1.0.136 / versionCode 135; package `com.personal.diaryapp`; source/mirror blob `2797094230b8a7864d531988d65f33798f44e759`; feed blob `e196d0e94dcdf02566474b20d24f19aab5095ac1`; starting web SHA-256 `436873076a491bd9d8759e7b6506e517469a89fc57c9893b18708f69354c2dd1`.
- Web-only scope: changed only `web-source/index.html`. The amount field label is now **“Kitna Kharcha Hua (₹)”** in Roman English, with matching English and Hindi labels. Added a clear example placeholder (“Yahan rakam likhein, jaise 500” / translated equivalents), decimal numeric keyboard hint, accessible label, and a dedicated high-contrast purple/gold input style with explicit visible/display sizing. The existing amount input, positive-number validation, expense/income selector, save operation, and totals/balance calculations remain in place.
- No other feature, form, database, stored record, existing Notes, Personal Calendar, My Documents, My Memories, existing Note/Diary locks or PIN/recovery, updater, native Android source, APK, package identity, or signing data was changed.
- Pre-edit backup branch: `backup/my-kharcha-amount-field-2026-11-13`. All four backups were re-fetched and confirmed readable:
  - `backups/web-source-index-before-my-kharcha-amount-field-2026-11-13.html` — original blob `2797094230b8a7864d531988d65f33798f44e759`
  - `backups/diary-web-index-before-my-kharcha-amount-field-2026-11-13.html` — same original blob
  - `backups/latest-before-my-kharcha-amount-field-2026-11-13.json` — blob `e196d0e94dcdf02566474b20d24f19aab5095ac1`
  - `backups/docs-PROJECT_MAP_AND_SECRETS_REGISTER-before-my-kharcha-amount-field-2026-11-13.md` — original register blob `dc411328b84f5d4ff29aab09fbabf5e674bbbff1`
- Source change commit: `f201ec571857f94fe9ea3c8142e36e916aa0d5e7`. Diff reviewed: only the three language labels/placeholders, amount input accessibility/input-mode/class assignment, and dedicated amount-field CSS changed. Both inline JavaScript blocks passed syntax parsing. Static checks confirmed the new label/placeholder/style and the existing `record.amount=Number(amount.value)` save binding remains.
- Publisher workflow run `43437336597` (run 173) completed with **success**; publish job `131925734864` completed successfully. Publisher commit: `f217904abf4cd9fd0afba22b792ef27112daf6b6`. Live webVersion: **183**.
- Final live source and published mirror were re-fetched and are byte-identical; both blob SHA `c7ce6c6fd0456c416204e6ad3c37422cd21d6d32`. Independently calculated UTF-8 SHA-256 `bb4c5985646ffc89c4ef0e9db6725e98ef6e9fa6c54fb07c75c73caf3d61efa3` matches live `latest.json.webSha256`.
- APK unchanged: 1.0.136 / versionCode 135 / SHA-256 `6fc74ca82888fed4121cc352c1846ec8c6a7063e2d2a33fbe032726f7a244348`; no APK rebuild or signing changes.
- Physical-device verification pending. User should use **Me → Check for Updates**, install Web Update 183, open **💰 My Kharcha**, and confirm the prominent **Kitna Kharcha Hua (₹)** box appears, accepts a test amount (e.g. 500), saves, and contributes to the expense total. Do not claim phone-side verification until user confirms.
- Rollback: exact pre-edit source, published mirror, feed and register are preserved on `backup/my-kharcha-amount-field-2026-11-13`; restore only the affected HTML if testing reveals a regression. Preserve all saved data.

---

# Web Update 184 — Separate My Kharcha amount and expense inputs (2026-11-13)

- User clarified that My Kharcha needs two separate numeric boxes: Raqam (₹) for the available/received amount (example ₹5,000) and Kharcha (₹) for the spent amount (example ₹2,000). The totals below must show total Raqam/Income ₹5,000, total Kharcha ₹2,000, and remaining balance ₹3,000.
- Starting live state: Web Update 183; APK 1.0.136 / versionCode 135; source/mirror blob c7ce6c6fd0456c416204e6ad3c37422cd21d6d32; feed blob d10c4a80337ba3d45706020b4583b8038659c3a6; starting web SHA-256 bb4c5985646ffc89c4ef0e9db6725e98ef6e9fa6c54fb07c75c73caf3d61efa3.
- Web-only scope: web-source/index.html. Replaced the single amount-plus-income/expense selector with two clearly labelled, separate decimal inputs. Roman English, English and Hindi labels/placeholders are supplied. Optional expense item/category and details remain available. Each saved record stores the two values separately; the live summary adds the Raqam to income, adds Kharcha to expenses, and calculates the remaining balance. Existing historical records using the previous amount + flow structure are still included in totals and remain displayable.
- Validation: both inline JavaScript blocks passed new Function syntax parsing. Static checks confirmed both inputs, the two-value save logic, updated labels in all three languages, old-record compatibility, and the new total/balance calculation. Arithmetic example verified: ₹5,000 − ₹2,000 = ₹3,000. No database schema migration or deletion was made.
- Pre-edit backup branch: backup/my-kharcha-two-amount-boxes-2026-11-13. The exact live source, published mirror, latest feed and Master Register were backed up as backups/web-source-before-two-amount-boxes-2026-11-13.html, backups/diary-web-before-two-amount-boxes-2026-11-13.html, backups/latest-before-two-amount-boxes-2026-11-13.json, and backups/register-before-two-amount-boxes-2026-11-13.md. All four backup files were successfully created on the backup branch before editing.
- Source commit: df2ae309cc419deda28342723a36bcf4b305c20b. Publisher commit: b956660f14adec6ebd330c966ad5ed401fb8fce8. Published Web Update: 184. Live source and mirror are byte-identical; both Git blob SHA 243e5842a9efafab356fb2842450ab1f6c96d0f2. Independently calculated UTF-8 SHA-256 97baad776de526da1ab8ad2a24b8f7242247ab3088583299289a4401f2b71b34 matches latest.json webSha256.
- APK unchanged: 1.0.136 / versionCode 135 / SHA-256 6fc74ca82888fed4121cc352c1846ec8c6a7063e2d2a33fbe032726f7a244348; no APK rebuild, native Android, package identity or signing changes.
- Physical-device verification remains pending. User should use Me → Check for Updates, install Web Update 184, then enter Raqam 5000 and Kharcha 2000 in separate boxes and save; confirm the summary shows Raqam ₹5,000.00, Kharcha ₹2,000.00 and Baqi ₹3,000.00. Do not claim phone-side success until user confirms.
- Rollback: restore web-source/index.html from the verified pre-edit backup branch; republish and recheck source/mirror/feed/hash. Preserve all user data and the existing Notes/PIN records.
---

# Web Update 185 — Edit saved My Kharcha entries (2026-11-13)

- User asked to be able to edit a My Kharcha entry after adding it. Added an Edit button to each saved Kharcha record (Roman English, English and Hindi labels). Selecting Edit fills the existing form with that record's date, Raqam, Kharcha, expense name and details.
- Saving an edited entry reuses the original record ID and created timestamp, updating the existing IndexedDB record instead of creating a duplicate. The form returns to Add mode after a successful save. Delete behavior remains unchanged. Old-format Kharcha entries remain editable with compatible value prefill.
- Scope: web-source/index.html only. Pre-edit backup branch: backup/my-kharcha-edit-entry-2026-11-13. Backups: backups/web-source-before-kharcha-edit-2026-11-13.html, backups/diary-web-before-kharcha-edit-2026-11-13.html, backups/latest-before-kharcha-edit-2026-11-13.json, backups/register-before-kharcha-edit-2026-11-13.md.
- Source commit: 6e23e88fd5110ee2f556d40dda3da84b488c8f08. Published Web Update: 185. Source and published mirror are byte-identical; both blob SHA 746947562a558bcf5db02e4a65e797f534355962. latest.json webSha256: 9481d9d50d3258548ae73cf37bbf12027969f7762d45f682473ab00c868b61f8.
- Both inline JavaScript blocks passed syntax parsing before commit. Static checks verified all three edit labels, the Edit button, record prefill, original ID preservation, save-mode reset and old-record compatibility. No APK rebuild; APK remains 1.0.136 / versionCode 135.
- Physical-device verification is pending. After Me → Check for Updates installs Web Update 185, test adding Raqam 5000 / Kharcha 2000, editing one value, saving, and confirming the same entry updates without duplication and the totals/balance recalculate. Do not claim phone-side testing until user confirms.
- Rollback: restore web-source/index.html from the verified pre-edit backup branch, republish, and verify mirror/feed. Preserve user records and all existing Diary/Notes/PIN features.

---

# Web Update 186 — My Kharcha categories, reports, separate section PIN locks and Smart Search (2026-11-13)

- User approved four additions to the existing Me tools: expense categories with separate totals; PDF reports for My Kharcha and Personal Calendar; separate locks for My Kharcha, My Documents and My Memories; and Smart Search.
- Starting live state: Web Update 185; APK 1.0.136 / versionCode 135; package com.personal.diaryapp. Starting source/mirror blob SHA 746947562a558bcf5db02e4a65e797f534355962; starting feed webSha256 9481d9d50d3258548ae73cf37bbf12027969f7762d45f682473ab00c868b61f8.
- Scope: web-only, changed only web-source/index.html in source commit d7e80e91be2145686b5ef4fcb08a2cc4ddc05299. The publisher workflow mirrored the exact source into diary-web/index.html and advanced latest.json to Web Update 186.
- My Kharcha category entry retains a free-text field and adds suggestions for Khana/Food, Safar/Travel, Shopping, Bill/Bills, Ghar/Home, Sehat/Health, Taleem/Education and Other. The summary now displays expense totals grouped by the category text; the category filter narrows the visible records without changing saved data or the all-record totals.
- Smart Search is available within each Me feature list. It searches names/titles, dates, amounts, category, details, event type and document filename as applicable. Existing record IDs and stored record shapes remain intact.
- PDF Report buttons are available in My Kharcha and Personal Calendar. They prepare a clean report in a separate browser tab/window; the user chooses the browser's Print / Save as PDF action. This is a browser-generated print-to-PDF flow, not a direct background PDF download. Popup permission may be required.
- Separate PIN gates are added for My Kharcha, My Documents and My Memories. Each section creates its own 4–8 digit PIN on first access; salted PBKDF2-SHA-256 hashes are stored, not the raw PIN. Leaving the section returns to Me and requires the PIN again on next entry. **Important security limitation:** this is an app-screen access lock only. The existing IndexedDB records and attached files are not encrypted at rest, so this does not protect data from someone with direct access to browser/device storage. The UI explicitly tells the user this; do not describe it as file encryption or strong device-level protection. There is no in-app forgot/reset PIN recovery flow in this release, so the user must keep each PIN safe.
- Existing Kharcha data (including historical amount/flow records), Personal Calendar entries, documents, memories, photos, record IDs and IndexedDB database remain untouched; no migration or deletion was performed. Existing Notes storage, Note Lock, Diary Lock/PIN/recovery, native Android code, APK, package identity and signing data were not changed.
- Pre-edit backup branch: backup/me-kharcha-category-pdf-lock-smart-search-2026-11-13. Exact readable backups, each re-fetched and compared with the pre-edit live content:
  - backups/web-source-before-kharcha-category-pdf-lock-search-2026-11-13.html — blob 746947562a558bcf5db02e4a65e797f534355962
  - backups/diary-web-before-kharcha-category-pdf-lock-search-2026-11-13.html — same source blob
  - backups/latest-before-kharcha-category-pdf-lock-search-2026-11-13.json — blob eb3a05d2b9c98de601982efe662feab9c8b87aae
  - backups/register-before-kharcha-category-pdf-lock-search-2026-11-13.md — blob a518c750d5fb7c9d4ed4491a0ba0fbcad4179be0
- Diff review: the source commit changed only web-source/index.html (67 additions, 14 deletions). Both inline JavaScript blocks passed syntax parsing. Static checks confirmed the category suggestions and grouped totals, search controls and matching logic, report generation/print action, PBKDF2 PIN setup/check and all three language dictionaries (Roman English, English and Hindi).
- Publisher workflow run 43458317453 (run 176) completed with conclusion success; its only publish job and every step completed successfully. Publisher commit: bbc32c1f4fdc855b6dbab7d086704d06af4a09a7.
- Final live source and published mirror are byte-identical; both Git blob SHA 46c320b0597e54fbdca3371516a2c693bd06cb54. Independently computed UTF-8 SHA-256 4fa7cfc3c0366aa36e9fc0c4137907bebff544e270873e31b094a8c50770f5ea matches live latest.json.webSha256. Live webVersion is 186.
- APK unchanged: 1.0.136 / versionCode 135 / SHA-256 6fc74ca82888fed4121cc352c1846ec8c6a7063e2d2a33fbe032726f7a244348. No APK rebuild, native Android, package identity or signing changes.
- Physical-device verification pending. User should use Me → Check for Updates, install Web Update 186, then test category suggestions and per-category totals, Smart Search in each section, PDF report creation for Kharcha and Calendar, and first-time PIN setup/re-entry for Kharcha, Documents and Memories. Use dummy/test records initially; the PIN gate is not at-rest encryption. Do not claim phone-side success until user confirms.
- Rollback: restore web-source/index.html from the verified pre-edit backup branch, republish and re-check source/mirror/feed/hash. Preserve all user data and all existing Notes/PIN records.


---

# Web Update 187 — Manage and recover separate Me-section PIN locks (2026-11-13)

- User approved adding three independent PIN-management options to **My Kharcha**, **My Documents** and **My Memories**: remove a lock, change its PIN, and recover a forgotten PIN.
- Starting live state: Web Update 186; APK 1.0.136 / versionCode 135 / package `com.personal.diaryapp`; source/mirror blob `46c320b0597e54fbdca3371516a2c693bd06cb54`; starting feed SHA-256 `4fa7cfc3c0366aa36e9fc0c4137907bebff544e270873e31b094a8c50770f5ea`.
- Web-only scope: changed only `web-source/index.html`; publisher mirrored it to `diary-web/index.html` and advanced the web feed to Update 187. No native Android source, APK, package identity, signing material, existing Notes, Note Lock, Diary Lock, or unrelated feature was changed.
- Each protected section now has a **🔑 PIN** management control after it is unlocked. Changing PIN requires the current PIN and entering the new 4–8 digit PIN twice. Removing a lock requires the current PIN plus confirmation; it removes only that section's PIN/recovery configuration and does not delete its Kharcha/Documents/Memories records or attachments.
- New PIN setup creates a random 20-character hexadecimal recovery code. The user must save it outside the app and re-enter it to confirm. Only a salted PBKDF2-SHA-256 hash is stored in localStorage; the plaintext recovery code is shown during setup, not persisted. Forgot PIN accepts this code, lets the user set a new PIN, then generates and requires confirmation of a replacement recovery code (one-time rotation).
- Existing Update 186 PINs remain compatible and are not overwritten. Because those earlier PINs had no recovery code, the first successful unlock after this update prompts the user to create one. **If an existing PIN was already forgotten before a recovery code was created, this update cannot recover it retroactively.** The user must know the current PIN once to establish recovery.
- All three UI language dictionaries (Roman English, English, Hindi) include the new PIN/recovery labels and messages. Existing PIN storage keys `diary_me_section_pin_v1_<kind>`, 4–8 digit PIN validation, PBKDF2-SHA-256 with 120,000 iterations, and protected-section mapping remain unchanged. New recovery hashes use separate keys `diary_me_section_recovery_v1_<kind>`.
- Pre-edit backup branch: `backup/section-pin-management-recovery-2026-11-13`. Verified exact readable backups:
  - `backups/web-source-before-section-pin-management-recovery-2026-11-13.html` — blob `46c320b0597e54fbdca3371516a2c693bd06cb54`
  - `backups/diary-web-before-section-pin-management-recovery-2026-11-13.html` — same blob
  - `backups/latest-before-section-pin-management-recovery-2026-11-13.json` — blob `6d1761e207a305e87dbf87443b60f0707be537a2`
  - `backups/register-before-section-pin-management-recovery-2026-11-13.md` — blob `87506eb56fe9256f6ab69c8fa7f5411c9162b5a7`
- Source commit: `7c90390050d2d270a6de986b335af087f6d16884`. The source diff is confined to the Me-feature language labels, protected-section PIN/recovery functions, and the PIN-management header control. Both inline JavaScript blocks passed syntax parsing. Static checks confirmed the three protected section IDs, original PIN storage key and digest parameters are preserved, and the new recovery/change/remove handlers are present.
- Publisher workflow run `43460652702` completed with **success**; publish job `132006363405` and all five steps completed successfully. Publisher commit: `6014f03538c73a0a29d03727a3da77a89879f324`.
- Final live source and published mirror are byte-identical; both Git blob SHA `9ff42b600813d36073b813ff8a5554a70f67771d`. Independently calculated UTF-8 SHA-256 `391951ff6ca63e24728c8f2f67d374cbcaf7aa0260cf7732a7669d06a9414137` matches live `latest.json.webSha256`. Live webVersion: **187**.
- APK unchanged: 1.0.136 / versionCode 135 / SHA-256 `6fc74ca82888fed4121cc352c1846ec8c6a7063e2d2a33fbe032726f7a244348`; no APK rebuild or signing changes.
- Physical-device verification is **pending**. Test each of the three sections separately: first unlock an existing PIN and save the displayed recovery code; change PIN using old PIN and verify the new PIN; leave/re-enter and unlock; use Forgot PIN with the recovery code and save the replacement code; finally remove the lock using the current PIN and confirm saved records remain. Do not claim phone-side testing until the user confirms.
- Rollback: restore `web-source/index.html` from the verified backup branch, republish, and re-check source/mirror/feed/hash. Preserve all user data.


---

# Web Update 191 — Match all three Me-section locks to Note Lock (2026-11-13)

- User requested that the separate locks for **My Kharcha**, **My Documents** and **My Memories** work the same way as the existing Note Lock.
- Starting live state: Web Update 187; APK 1.0.136 / versionCode 135; source/mirror blob `9ff42b600813d36073b813ff8a5554a70f67771d`; starting web SHA-256 `391951ff6ca63e24728c8f2f67d374cbcaf7aa0260cf7732a7669d06a9414137`.
- Scope: only `web-source/index.html` was changed. The publisher mirrored it to `diary-web/index.html`. No Android source, APK, package identity, signing files, existing Note Lock, Diary Lock, notes, photos, or Me-section records/attachments were modified.
- All three protected sections now use the Note Lock's **4-digit numeric PIN** flow:
  - First setup asks for a new 4-digit PIN and confirmation, using the same style of on-screen PIN popup.
  - Unlock accepts the current PIN. Four-digit PINs auto-submit as in Note Lock.
  - **Forgot PIN** shows a newly generated temporary 4-digit PIN with a Copy button; after the user re-enters it correctly, the app asks them to create and confirm a new 4-digit PIN.
  - **Change PIN** verifies the current PIN first, then asks for a new 4-digit PIN twice.
  - **Remove Lock** verifies the current PIN before removing only the PIN setting for that section. The section's saved records and attachments remain.
- Compatibility for PINs created in Update 186/187: existing 4-digit PINs remain valid and are marked as 4-digit after their first successful unlock. If an existing PIN is 5–8 digits, the user must enter it once successfully, then create a new 4-digit PIN. This avoids silently losing access to older PIN-protected sections.
- Previous section-specific recovery-code setup is replaced by the Note Lock-style generated temporary PIN recovery flow. Any old section recovery hash is discarded when a new PIN is saved. **Security limitation:** like the existing Note Lock forgot-PIN flow, the temporary recovery PIN is displayed by the app to whoever can reach that section's lock screen; it is not an independent identity check. The lock remains an app access gate, not encryption of data at rest.
- Roman English, English and Hindi labels were updated for 4-digit PIN instructions and temporary PIN verification. Existing Notes and Note Lock code was not changed.
- Pre-edit backup branch: `backup/note-style-section-lock-2026-11-13`. Exact pre-edit backups were fetched back and compared:
  - `backups/web-source-before-note-style-section-lock-2026-11-13.html` — blob `9ff42b600813d36073b813ff8a5554a70f67771d`
  - `backups/diary-web-before-note-style-section-lock-2026-11-13.html` — same blob
  - `backups/latest-before-note-style-section-lock-2026-11-13.json` — blob `7a0b4394d314b5e46450bde8cd366fd5c1fa8ae3`
  - `backups/register-before-note-style-section-lock-2026-11-13.md` — blob `a1d7cda1780cc79dc264ec75660743d08cbd10a0`
- Source changes were reviewed. Both inline JavaScript blocks passed syntax parsing. Static checks confirmed the Note-style four-digit setup/dialog, generated temporary PIN and copy flow, verification before changing/removing locks, legacy 5–8 digit PIN migration, all three language dictionaries, and unchanged section PIN storage key family.
- Final source commit: `9e9fd3ce3ea4c6fd04762e802318cd7189fe5f59`. Final source and mirror are byte-identical; both Git blob SHA `5d13b32a95121f0933a28042df334c1416f69f5f`. Independently calculated UTF-8 SHA-256 `ad920b3597dc3f57ff06eeb8dfcbf2615807928d8417797b0f92275778a14ce5` matches live `latest.json.webSha256`. Live webVersion: **191**.
- Publisher workflow run `43464715352` completed with **success**; publish job `132020633376` and all steps completed successfully.
- APK unchanged: 1.0.136 / versionCode 135 / SHA-256 `6fc74ca82888fed4121cc352c1846ec8c6a7063e2d2a33fbe032726f7a244348`. No APK rebuild or signing changes.
- Physical-device testing is pending. Test each section independently: unlock with the old PIN; if it was 5–8 digits, complete the one-time migration to a 4-digit PIN; test a normal unlock; use Forgot PIN, copy and re-enter the temporary PIN, then set a new PIN; test Change PIN and Remove Lock; confirm records and attachments remain. Do not claim phone-side testing until user confirms.
- Rollback: restore the verified pre-edit `web-source/index.html` from the backup branch, republish, and re-check source/mirror/feed/hash. Preserve all user data.


---

# Web Update 192 — Require explicit recovery PIN verification for all three Me locks (2026-11-13)

- User reported that after tapping **Forgot PIN**, a new PIN could be created without entering the temporary recovery PIN. User confirmed this affected all three protected sections: **My Kharcha**, **My Documents**, and **My Memories**.
- Starting live state: Web Update 191; APK 1.0.136 / versionCode 135; source/mirror blob `5d13b32a95121f0933a28042df334c1416f69f5f`; feed blob `ce97d78d4310c042d11f6958ba8f40e4554bc2d4`.
- Scope: changed only `web-source/index.html`; publisher mirrored it to `diary-web/index.html` and advanced the live web feed to Update 192. No APK, Android source, Note Lock, Diary Lock, protected records, attachments, or other features were intentionally changed.
- Recovery flow hardening applied to the shared Me-section lock handler used by all three sections:
  - Copying the displayed temporary PIN no longer closes the popup or advances the flow.
  - A separate **Unlock / Continue** button is required to open the recovery-PIN entry dialog.
  - Recovery-PIN entry no longer auto-submits after four digits. The user must explicitly tap **Unlock** (or press Enter) in that dialog.
  - Only an exact match with the temporary PIN reaches `meFeatureAskNewPin`. A wrong PIN returns to verification; closing the dialog cancels recovery. Thus copying, closing, or entering an incorrect value cannot reach new-PIN creation.
  - The existing new-PIN creation and confirmation, four-digit PIN storage, and section data are unchanged.
- Pre-edit backup branch: `backup/section-recovery-verify-fix-2026-11-13`. Verified pre-edit source and mirror backups both have blob `5d13b32a95121f0933a28042df334c1416f69f5f`. Additional exact backup files: `backups/latest-before-section-recovery-verify-fix-2026-11-13.json` and `backups/register-before-section-recovery-verify-fix-2026-11-13.md`.
- Source commit: `94798828f4c9c7f009842035cba5761a20c28da1`. Publisher commit: `4c7138c81d557def46cdf1dee087f28caa70fcde` (Publish My Diary web bundle update). Publisher diff confirms the source changes were mirrored and the feed was advanced.
- Final live source and mirror are byte-identical; both Git blob SHA `7bf375b9d2345509f2b2f9307b05961cd84fae70`. Live `latest.json.webVersion`: **192**; `webSha256`: `a881d44a7ae85c7adb55374cd30b0cb1d29eeba0dfe2db46f25623e9569cb811`. Feed and published mirror were fetched after publishing.
- APK unchanged: 1.0.136 / versionCode 135 / SHA-256 `6fc74ca82888fed4121cc352c1846ec8c6a7063e2d2a33fbe032726f7a244348`; no APK rebuild or signing changes.
- Physical-device verification is pending. User should install web update 192 through **Me → Check for Updates**, then test Forgot PIN independently in all three sections: copy the temporary PIN, verify that copy alone does not advance, tap Unlock, enter a wrong PIN and confirm no new-PIN screen appears, then enter the correct temporary PIN and confirm only then that new PIN setup opens. Also confirm existing records and attachments remain. Do not claim phone-side testing until the user confirms.
- Rollback: restore the verified pre-edit `web-source/index.html` from the backup branch, republish, and re-check source/mirror/feed. Preserve all user data.


---

# Web Update 193 — Match Me-section recovery PIN steps to Note Lock (2026-11-13)

- User confirmed the exact recovery behavior to align: after copying the temporary PIN, the popup should advance directly to PIN entry; entering four digits should automatically verify; a wrong PIN should show the Note Lock-style error popup and allow retry; only the correct temporary PIN may proceed to new PIN setup and confirmation.
- Starting live state: Web Update 192; APK 1.0.136 / versionCode 135; source/mirror blob `7bf375b9d2345509f2b2f9307b05961cd84fae70`; starting web SHA-256 `a881d44a7ae85c7adb55374cd30b0cb1d29eeba0dfe2db46f25623e9569cb811`.
- Scope: changed only the Me-section PIN recovery UI/flow in `web-source/index.html`. The shared handler covers My Kharcha, My Documents and My Memories. Existing PIN setup, PIN confirmation, current-PIN verification for Change/Remove, PBKDF2 PIN storage, section data and attachments remain unchanged. Note Lock and Diary Lock were not edited.
- Recovery flow now follows Note Lock's sequence:
  - The temporary-PIN popup has a Copy button only; successful copy closes it and opens the recovery PIN entry dialog.
  - The recovery dialog auto-verifies as soon as four numeric digits are entered (Enter also works); there is no extra Unlock/Continue button.
  - A wrong recovery PIN shows the same purple Note Lock-style error popup; closing that popup retries recovery PIN entry.
  - A correct recovery PIN alone opens the existing new-PIN setup and confirmation flow. Closing recovery entry cancels without creating a new PIN.
  - Clipboard failure leaves the temporary-PIN popup open and shows the localized failure label.
- Pre-edit backup branch: `backup/me-lock-note-recovery-flow-2026-11-13`. Verified exact backups:
  - `backups/web-source-before-me-lock-note-recovery-flow-2026-11-13.html` — blob `7bf375b9d2345509f2b2f9307b05961cd84fae70`
  - `backups/diary-web-before-me-lock-note-recovery-flow-2026-11-13.html` — same blob
  - `backups/latest-before-me-lock-note-recovery-flow-2026-11-13.json` — blob `1cbbbe0045c654c3e3fec06f0449caaa421fb21c`
  - `backups/register-before-me-lock-note-recovery-flow-2026-11-13.md` — blob `b6571b82044ad07e8093873d87839f6f9fe6461e`
- Source commit: `d6c5d64a39c1be9371311ca3073f79fa1accceae`. Diff review shows only `web-source/index.html` changed (11 additions, 5 deletions). Both inline JavaScript blocks passed syntax parsing. Static checks confirmed successful-copy advance, automatic four-digit recovery verification, wrong-PIN retry popup, and shared application to all three protected sections.
- Publisher workflow run `43469878386` completed successfully, including the web-only publish step. Publisher/main commit: `1a6c34f83e052c9fc969e0618c7f62cc4661c644`. Published source and mirror are byte-identical; both blob SHA `6bbbb9d59cd4796673a4b7c0337809dfd13a9e02`. Live `latest.json.webVersion`: **193**; `webSha256`: `7a10ed398939bdc688e66e4be5a7afc789e97ce0b4658ac8eac7c952a1b56246`.
- APK unchanged: 1.0.136 / versionCode 135 / SHA-256 `6fc74ca82888fed4121cc352c1846ec8c6a7063e2d2a33fbe032726f7a244348`; no APK rebuild, Android source change or signing change.
- Physical-device verification is pending. Install web update 193 through **Me → Check for Updates** and test Forgot PIN separately in all three sections: copy temporary PIN, confirm recovery entry opens; enter a wrong four-digit PIN and confirm the error popup then retry; enter the correct temporary PIN and confirm only then that new PIN setup and confirmation open. Also verify Change PIN, Remove Lock and saved records/attachments remain intact. Do not claim phone-side testing until user confirms.
- Rollback: restore `web-source/index.html` from the verified pre-edit backup branch, republish, and re-check source/mirror/feed. Preserve all user data.


---

# Web Update 195 + APK 1.0.137 — Smart Follow-up Reminder (2026-11-13)

- User requested the Smart Follow-up Reminder idea. Added a fifth independent ⏰ Smart Reminder tool under Me.
- Starting live state: APK 1.0.136 / versionCode 135, Web Update 193, source/mirror blob 6bbbb9d59cd4796673a4b7c0337809dfd13a9e02, web SHA-256 7a10ed398939bdc688e66e4be5a7afc789e97ce0b4658ac8eac7c952a1b56246.
- Web behavior:
  - Create a reminder with title, date, time and optional details.
  - Optionally link it to an existing Note; choosing a linked Note fills an empty reminder title.
  - Reject past date/time values.
  - List, Smart Search (including time), edit and delete reminders. Editing reschedules the same reminder ID; deleting cancels its native alarm.
  - Notifications provide 10-minute Snooze and Done actions.
  - Reminder form labels, validation messages and permission prompts are translated for Roman, English, Hindi, Urdu, Arabic, Bengali, Gujarati, Marathi, Tamil and Telugu. Android notification action labels currently display “10 min baad” and “Done”.
  - A browser-only HTML session without the native Android bridge does not claim to schedule alerts; it asks the user to use the latest installed My Diary app.
- Android scheduling:
  - Added native JavaScript bridge methods to schedule/cancel reminders and check/request notification and exact-alarm permissions.
  - Uses Android AlarmManager with exact alarms where the user grants Alarms & reminders special access; Android 13+ also requires Notifications permission.
  - Pending reminders are stored in app-private SharedPreferences and restored after device reboot or app package replacement through dedicated receivers.
  - If exact-alarm access is not available, native scheduling has an inexact fallback, but the UI requests exact-alarm access before saving for the intended punctual behavior.
  - Notification title/details may be visible on the phone lock screen. Reminder records are local to the device; no cloud upload or sync was added.
- Storage and preservation:
  - Reminder records reuse the existing diary_me_features_v1 IndexedDB database and records object store; no database version/schema migration.
  - Existing Notes database/storage, Note Lock, Diary Lock, PIN/recovery data, old Notes, photos, attachments, existing Calendar, My Kharcha, My Documents and My Memories were not intentionally changed.
  - The Me-feature IndexedDB data is not encrypted by the existing section PIN; do not assume the reminder content is encrypted at rest.
- Files changed for this feature:
  - web-source/index.html — Smart Reminder UI, translations, form validation, link-to-Note, search/edit/delete and native bridge calls.
  - scripts/add_diary_app_actions.py — Android bridge, AlarmManager scheduler, notification actions, notification/boot permissions and receivers.
  - scripts/add_online_diary_updates.py — keep the existing DiaryBundlePathHandler inside MainActivity when top-level reminder receiver classes are appended.
  - .github/workflows/build-diary-from-zip.yml — next signed APK version advanced to 1.0.137 / versionCode 136; release guard, APK URL/name and release notes updated.
  - Publisher workflows generated diary-web/index.html, latest.json, My-Diary.apk and My-Diary-1.0.137.apk.
- Verified pre-edit backup branch: backup/pre-smart-follow-up-reminder-2026-11-13. All six backups were re-fetched and byte-identically verified:
  - backups/web-source-before-smart-follow-up-reminder-2026-11-13.html — original blob 6bbbb9d59cd4796673a4b7c0337809dfd13a9e02
  - backups/diary-web-before-smart-follow-up-reminder-2026-11-13.html — same original blob
  - backups/latest-before-smart-follow-up-reminder-2026-11-13.json — blob d52cc10a33aa118efc84f9b65977103e875c7177
  - backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-smart-follow-up-reminder-2026-11-13.md — blob 0c231f8a6161f18e0791fb8036fb081444079f3b
  - backups/add_diary_app_actions-before-smart-follow-up-reminder-2026-11-13.py — blob 067a6cdaf5ac53cdd497894f8a6436f5cbe7a447
  - backups/build-diary-from-zip-before-smart-follow-up-reminder-2026-11-13.yml — blob f6467078153e112b4b56e5d515c67a0b47d0a3be
- Source and integration commits:
  - Smart Reminder UI: 518a52f61b0314a288d000223009f969775cc760
  - Native reminder scheduler/bridge: 620730aba25a9105556a843a41b01dcd4f14ca8a
  - Exact-alarm permission methods: 5c1a25cc24a73b9dafff1913e69524859d806403
  - Boot receiver manifest correction: 3bd7e6d91368789718714169b4e1b9a67e678505
  - Duplicate-import correction: 9875e15d31c1f556602632d052d02c540c4a687c
  - Existing online updater insertion-point correction: d709eabeae544992025c4d7053007cd06b12254b
  - APK workflow version bump: c4ef435b7767bdd7a4e9048ea41b854ff182cf60
  - Exact-alarm UI prompt: 29265136fe01efe1515533a52d70e28b7a5581be
- Web publishing:
  - Web Update 194 publisher run 43473902236 completed successfully.
  - Web Update 195 publisher run 43474487869 completed successfully; publisher commit 2d94faf8b887f5b867fa980b96b3fbd64cb8792e.
  - Final web-source/index.html and diary-web/index.html are byte-identical; both Git blob SHA a45b5803031a6e521e696c3169632e84a515c92d.
  - Independently computed SHA-256 of the exact final UTF-8 source: b0c386146062439091df8c47645202d90678b548f7b7127a40933b976891ebdc. The implementation was checked against the standard SHA-256 abc test vector; the digest matches live latest.json webSha256.
- APK publishing:
  - Build/publish workflow run 43474419797 completed successfully.
  - Debug and signed Release APK builds passed; Android Kotlin compilation passed; JavaScript module node --check passed; Android identity, FileProvider and translation audit checks passed.
  - The existing signing certificate fingerprint was verified unchanged: 23A4E93F3C7911DCE18389EA583548700C6AD6A3759707F1CD222D07E2408B5A.
  - Publisher commit: 628375728d79e88e7d0aa1baf1e1713f8e1db15b.
  - Live latest.json: APK 1.0.137 / versionCode 136; URL https://raw.githubusercontent.com/amuazzinxyz-ops/My-Diary-Updates/main/My-Diary-1.0.137.apk; APK SHA-256 38439e536479d7adea7c50031b59873d8a898b0c103f845018cfa8b8e8b805bf; webVersion 195; web SHA-256 b0c386146062439091df8c47645202d90678b548f7b7127a40933b976891ebdc.
  - The APK build used the immediately previous web bundle (Web Update 194); the live feed is Web Update 195. After installing APK 1.0.137, run Me → Check for Updates again if needed so the native updater applies web bundle 195.
  - Two intermediate build attempts failed during integration (duplicate Android imports and the online updater class insertion point); these were corrected. The final build run above completed successfully. No failed/intermediate APK was published.
- Physical-device verification is pending. User should update to APK 1.0.137, then use Me → Check for Updates again to apply Web Update 195 if it is still offered. In Me → Smart Reminder, create a test reminder 2–3 minutes ahead, allow Android Notifications and Alarms & reminders permissions, return to the form and tap Save again. Confirm the notification arrives with screen off/app closed, then test Snooze and Done. Also test after a device restart. Do not claim device-side testing until the user confirms.
- Rollback: restore the exact web source, native integration scripts, build workflow and feed from backup/pre-smart-follow-up-reminder-2026-11-13. For any APK rollback after installation, preserve package identity/signing and publish a newer versionCode; never ask the user to uninstall or clear app data. Preserve all notes, photos, attachments, PIN/recovery data and user records.


---

# Web Update 196 — Keep the Me menu open after returning from a Me feature (2026-11-13)

- User request: when opening any of the five Me features — Personal Calendar, Smart Reminder, My Kharcha, My Documents or My Memories — and then pressing **Back**, return to the five-option Me menu without closing/collapsing the Me button.
- Starting live state: APK 1.0.137 / versionCode 136; Web Update 195; package `com.personal.diaryapp`. Starting source/mirror blob SHA `a45b5803031a6e521e696c3169632e84a515c92d`; starting feed blob `f25723a6d43952a4cea54de2b2d2189ff1bbb28d`; starting register blob `8f20ca672817a86112dac6ebe176f33f8b5d2a3a`. The immediately preceding main commit was `1eeedad3ad0e30059698e8e7bea0fcc47236393d` (register-only clarification).
- Root cause: the Me feature modal's click event bubbled to the Diary overlay's outside-click handler. The Back/Close handler first reopened `mePanel`, then the same click bubbled to the overlay, which treated the click as outside the Me menu and hid it again.
- Scope: web-only; changed exactly one event-handler line in `web-source/index.html`. The modal click handler now calls `e.stopPropagation()` before handling a backdrop click. This keeps Back/Close clicks from reaching the overlay outside-click handler; the existing backdrop-close behavior is retained. The five feature buttons, feature pages, PIN gates, records, attachments, database/storage keys, translations, native Android source, APK, package identity and signing data were not changed.
- Pre-edit backup branch: `backup/me-feature-back-retain-menu-2026-11-13`. Exact readable backups were fetched back and compared byte-for-byte:
  - `backups/web-source-before-me-feature-back-retain-menu-2026-11-13.html` — original blob `a45b5803031a6e521e696c3169632e84a515c92d`
  - `backups/latest-before-me-feature-back-retain-menu-2026-11-13.json` — original blob `f25723a6d43952a4cea54de2b2d2189ff1bbb28d`
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-me-feature-back-retain-menu-2026-11-13.md` — original blob `8f20ca672817a86112dac6ebe176f33f8b5d2a3a`
- Source commit: `ec2065157ac25cefb8a15d70232192c09afb4ae1`. Commit diff was reviewed and contains only the single requested event-handler change. Publisher commit: `37eb3c42df30c112c16d04bc2a0fc456d77ed2f9` (“Publish My Diary web bundle update”).
- Published verification: `web-source/index.html` and `diary-web/index.html` were re-fetched and are byte-identical; both blob SHA `fd585bed757ddb961098b3a8f9c7059d59543622`. Independently computed SHA-256 of the exact UTF-8 source bytes: `f55cb80a22ad6237d108d07c246a2ba9b0d03c33e3603f4f38e7cdcdd52eb43b`, matching live `latest.json.webSha256`. Live `webVersion=196`.
- APK unchanged: `1.0.137` / versionCode `136`; APK SHA-256 remains `38439e536479d7adea7c50031b59873d8a898b0c103f845018cfa8b8e8b805bf`. No APK rebuild, native source change, or signing operation. Publisher workflow run ID/conclusion was not exposed by the available workflow-run lookup in this session; the publisher bot commit and live source/mirror/feed were verified.
- Physical-device verification is **pending**. User should open **Me → Smart Reminder** (and preferably each of the other four features), tap **Back**, and confirm the five-option Me menu remains visible. Also test the feature Close (×) button and backdrop close; confirm tapping the Me button itself still opens/closes the menu normally. Do not claim phone-side success until the user confirms.
- Rollback: restore the exact pre-edit `web-source/index.html` from `backup/me-feature-back-retain-menu-2026-11-13`, republish, and re-check source/mirror/feed/hash. Preserve all user records and app data.


---

# Web Update 197 — Hide the redundant Lock button in My Kharcha (2026-11-13)

- User request: after opening **💰 My Kharcha**, remove the visible `🔒 Lock` header button. This is a UI-only removal; keep My Kharcha's section PIN protection and lock/recovery system unchanged.
- Starting live state: APK 1.0.137 / versionCode 136; Web Update 196; package `com.personal.diaryapp`. Starting source/mirror blob `fd585bed757ddb961098b3a8f9c7059d59543622`; feed blob `f4e3717e47aa72a426cad0bd844374083ba24063d`; register blob `e1e94bd23661b650099fd06c02485d89e6a242f7`.
- Scope: changed exactly one line in `web-source/index.html`. The header `🔒 Lock` button is now hidden for `kharcha`; it remains governed as before for Documents and Memories. Existing `meFeatureProtected(kind)` still includes `kharcha`, `documents` and `memories`; the PIN gate, PIN/recovery storage keys, dialogs, records and other features were not changed. No APK/native source, data schema or translations changed.
- Pre-edit backup branch: `backup/remove-kharcha-header-lock-button-2026-11-13`. Three backups were re-fetched; the HTML backup blob `fd585bed757ddb961098b3a8f9c7059d59543622` matches the exact pre-edit source.
- Source commit: `deb0d2b582e22a800d547300e99f1589c6d29b43`. Reviewed diff contains only the one requested visibility change. Publisher commit: `c6f52a0f548621af8a1dc2dd0461e8ebe0bd7584` (“Publish My Diary web bundle update”).
- Published verification: `web-source/index.html` and `diary-web/index.html` are byte-identical; blob SHA `58db1f74729e21bff7139b068aad202fe58b537d`. Independently computed SHA-256 of exact UTF-8 source: `4452235be464d6acb8622430f71e4f0a76b416579e41ad91207d52a4d256852e`, matching live `latest.json.webSha256`. Live `webVersion=197`.
- APK unchanged: 1.0.137 / versionCode 136; APK SHA-256 `38439e536479d7adea7c50031b59873d8a898b0c103f845018cfa8b8e8b805bf`. No APK rebuild or signing change.
- Physical-device verification is pending. User should apply **Me → Check for Updates** and open My Kharcha: confirm the header `🔒 Lock` button is absent, while the section PIN still prompts on entry and the records, add/edit/delete, PDF report and other tools still work. Also confirm Documents and Memories are unchanged. Do not claim phone-side testing until user confirms.
- Rollback: restore exact pre-edit `web-source/index.html` from `backup/remove-kharcha-header-lock-button-2026-11-13`, republish, and verify source/mirror/feed/hash. Preserve all local records and PIN/recovery data.


---

# APK 1.0.138 — Keep Smart Reminder alarms exact while screen is off (2026-11-14)

- User reported that Smart Reminder notifications and ringtone arrive while the phone screen is ON, but neither arrives while the screen is OFF. User confirmed they are using the installed APK.
- Live starting state: My Diary APK 1.0.137 / versionCode 136; Web Update 197; package `com.personal.diaryapp`. Starting native integration script blob `d8d18d417d266819248a38119d99ab892f39dece`; build workflow blob `a5fe450702a58e33acd5e4b9242062da18c945e0`; feed blob `07c94c3a2760c52ec2e423e483800ba115a02027`; web source blob `58db1f74729e21bff7139b068aad202fe58b537d`.
- Root cause identified in the Android alarm scheduler: if `setExactAndAllowWhileIdle` threw `SecurityException`, the code silently fell back to `setAndAllowWhileIdle`. That is an inexact alarm and Android Doze can defer it while the screen is off. This fallback could therefore produce the exact symptom reported. The UI already checks exact-alarm permission, but the native bridge did not independently enforce it.
- Scope: native scheduling reliability only. The bridge now rechecks exact-alarm permission immediately before scheduling and opens the exact-alarm permission settings if access is missing. The scheduler verifies `canScheduleExactAlarms()` on Android 12+ and refuses to claim success without access. The inexact fallback has been removed; Android 6+ uses `RTC_WAKEUP` + `setExactAndAllowWhileIdle`, and older Android uses `setExact`.
- No reminder record schema, IndexedDB storage, reminder UI/translations, web HTML, Notes, photos, attachments, Calendar, Kharcha, Documents, Memories, PIN/recovery data, package identity, or user data was intentionally changed. The web bundle remains Web Update 197.
- Pre-edit backup branch: `backup/reminder-screen-off-exact-alarm-2026-11-14`. Five backup files were fetched back and verified byte-identical to the live pre-edit files:
  - `backups/add_diary_app_actions-before-reminder-screen-off-exact-alarm-2026-11-14.py` — original blob `d8d18d417d266819248a38119d99ab892f39dece`
  - `backups/build-diary-from-zip-before-reminder-screen-off-exact-alarm-2026-11-14.yml` — original blob `a5fe450702a58e33acd5e4b9242062da18c945e0`
  - `backups/web-source-before-reminder-screen-off-exact-alarm-2026-11-14.html` — original blob `58db1f74729e21bff7139b068aad202fe58b537d`
  - `backups/latest-before-reminder-screen-off-exact-alarm-2026-11-14.json` — original blob `07c94c3a2760c52ec2e423e483800ba115a02027`
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-reminder-screen-off-exact-alarm-2026-11-14.md` — original blob `4dd82a996744a990502e7952ee14ad21e97a86d5`
- Reviewed native diff: removed the catch-and-downgrade to `setAndAllowWhileIdle`; added native exact-alarm permission recheck before calling the scheduler. Confirmed the final native script contains no `setAndAllowWhileIdle` fallback and retains one `setExactAndAllowWhileIdle` call.
- Source PR: [#1](https://github.com/amuazzinxyz-ops/My-Diary-Updates/pull/1), merged successfully as commit `b30e39f09a06c7404141e37370e81b6d22467b78` (squash merge). Build workflow run `43594988709` completed with conclusion `success`: debug build, Kotlin compilation, signed Release build, package checks, signature checks and APK publication passed. The existing signing certificate fingerprint was verified unchanged: `23A4E93F3C7911DCE18389EA583548700C6AD6A3759707F1CD222D07E2408B5A`.
- Published APK: `1.0.138` / versionCode `137`; live `latest.json` blob `425f295230b22b6814335d61d9c0b01feb8f138c`; APK SHA-256 `59b95893e6e412a1ed44a6f3880fd486ea3b6cf70ee484ceef4102ed7bef4b38`; APK file and versioned APK are byte-identical (same Git blob `d3597926cd910e7ae0ba96fb0ba1bcb5dd1230e5`). WebVersion remains `197` and web SHA-256 remains `4452235be464d6acb8622430f71e4f0a76b416579e41ad91207d52a4d256852e`.
- Physical-device verification is pending; do not claim the phone-side screen-off symptom is fixed until the user confirms. After installing APK 1.0.138 via **Me → Check for Updates**, create a short test reminder, lock the screen and verify both notification and ringtone arrive at the scheduled time. Also test with the app closed and after device restart. If exact-alarm access is missing, the app must request it rather than silently schedule an inexact alarm. If the alarm still does not fire despite exact access, investigate the device manufacturer's background/autostart restrictions separately.
- Rollback: restore the native integration script and build workflow from the verified backup branch above, then publish a newer versionCode while preserving app identity/signing. Do not uninstall the app, clear app data, or delete reminders/notes/photos/PIN data.


---

# APK 1.0.139 — Use Android AlarmClock events for Smart Reminder screen-off delivery (2026-11-14)

- User tested APK 1.0.138 and confirmed that both reminder notification and ringtone still arrived only while the screen was ON; neither arrived while the screen was OFF. User also confirmed all relevant phone/app settings were already ON. Do not send the user through the same settings checklist again.
- Live starting state: APK 1.0.138 / versionCode 137; Web Update 197; package `com.personal.diaryapp`. Starting native integration script blob `76e6f18d94507b4df4c29c7dda1c0ed238043266`; workflow blob `4a29b4c8e435fdbfd39b9c5cd0b1d584deb09dec`; feed blob `425f295230b22b6814335d61d9c0b01feb8f138c`; register blob `c0eeff18ee2b27d49e218d96c530c01b1f72c4d1`.
- Additional source inspection: the original Android project manifest contained no reminder-specific permission or receiver declarations. The native integration script adds `POST_NOTIFICATIONS`, `RECEIVE_BOOT_COMPLETED`, `SCHEDULE_EXACT_ALARM`, `.DiaryReminderReceiver`, and `.DiaryReminderBootReceiver` with BOOT_COMPLETED and MY_PACKAGE_REPLACED actions. The previous build had no fail-closed assertion that these generated declarations were actually present.
- Scope: native reminder delivery only. Replaced ordinary `setExactAndAllowWhileIdle(RTC_WAKEUP,...)` scheduling with `AlarmManager.setAlarmClock(AlarmClockInfo(atMillis, showPending), pending)`. This registers each reminder with Android as an alarm-clock event, supplies the app launch PendingIntent as the system's alarm-show action, and uses the system wake-up alarm path. The notification is also categorized as `Notification.CATEGORY_ALARM`. Existing exact-alarm permission checks, reminder storage, cancellation, snooze, boot/package-replacement restoration, and notification actions remain in place.
- Build workflow now fails closed unless the generated manifest parses and contains notification/exact-alarm/boot permissions, both reminder receivers, and boot/update restoration actions; it also checks the generated Kotlin source uses AlarmClock scheduling and has no old inexact/ordinary exact scheduler fallback.
- Preservation: no web HTML, reminder record schema, notes, photos, attachments, Calendar, Kharcha, Documents, Memories, PIN/recovery data, app package identity, signing configuration, or user data intentionally changed. Web bundle remains Web Update 197. No user data clearing or app uninstall is required.
- Pre-edit backup branch: `backup/reminder-screen-off-alarmclock-2026-11-14`. Backup files were committed and their blobs match the exact pre-edit live files:
  - `backups/add_diary_app_actions-before-reminder-alarmclock-2026-11-14.py` — original blob `76e6f18d94507b4df4c29c7dda1c0ed238043266`
  - `backups/build-diary-from-zip-before-reminder-alarmclock-2026-11-14.yml` — original blob `4a29b4c8e435fdbfd39b9c5cd0b1d584deb09dec`
  - `backups/latest-before-reminder-alarmclock-2026-11-14.json` — original blob `425f295230b22b6814335d61d9c0b01feb8f138c`
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-reminder-alarmclock-2026-11-14.md` — original blob `c0eeff18ee2b27d49e218d96c530c01b1f72c4d1`
- Source PR: [#2](https://github.com/amuazzinxyz-ops/My-Diary-Updates/pull/2), squash-merged as commit `93c0e89d3194c8c61385cc794310e9e33e5277cf`. Build workflow run [43597330789](https://github.com/amuazzinxyz-ops/My-Diary-Updates/actions/runs/43597330789) completed successfully. The manifest/receiver/permission audit passed; debug Kotlin/Android build passed; signed Release APK build and publication passed. The release signer SHA-256 fingerprint was verified unchanged: `23A4E93F3C7911DCE18389EA583548700C6AD6A3759707F1CD222D07E2408B5A`.
- Published APK: `1.0.139` / versionCode `138`; live feed blob `c794626b4ed9e71b657641895dc0f116bd42c296`; APK SHA-256 `04588ba0971f5d68817e3133ae88b0370b1c4ffe8c2b47c9063d656c575b6004`. The signed Release APK artifact was downloaded and independently hashed; its SHA-256 matches the live feed. `My-Diary.apk` and `My-Diary-1.0.139.apk` have the same Git blob `f10ad2b40e330fa7a7ad881de08e77fc3c08b5f2`. Web source and mirror remain byte-identical at blob `58db1f74729e21bff7139b068aad202fe58b537d`; WebVersion remains `197`, web SHA-256 remains `4452235be464d6acb8622430f71e4f0a76b416579e41ad91207d52a4d256852e`.
- Physical-device verification is pending. User must install/update to APK 1.0.139, create a test Smart Reminder a few minutes ahead, lock the screen, and confirm both notification and ringtone arrive with the screen OFF. Also test with My Diary closed and after device restart. The assistant has not tested the user's Vivo device and must not claim this symptom is fixed until user confirms. Android may show its normal next-alarm indicator because reminders are now registered as alarm-clock events.
- Rollback: restore the native integration script and workflow from the verified backup branch above, then publish a newer versionCode while preserving package identity/signing. Never uninstall the app, clear app data, or delete reminders, notes, photos, attachments, PIN/recovery data, or user records.


---

# APK 1.0.140 — Wake the screen for Smart Reminders (2026-11-14)

- User clarified after APK 1.0.139 that, with the phone screen OFF, reminder notification and ringtone now arrive, but the display does not turn ON. User asked to fix only screen wake; notification timing, ringtone, reminder content and all other Diary features must remain unchanged.
- Live starting state: APK 1.0.139 / versionCode 138; Web Update 197; package `com.personal.diaryapp`. Starting native integration script blob `c9a2794e46a2915dd3d041f1de88966e9a39951a`; build workflow blob `d71558b4fdc6eb35c252ff1c6c9eb5ae332958a6`; feed blob `c794626b4ed9e71b657641895dc0f116bd42c296`; register blob `3bd4845a4189a64fbe6f95df3874a017117fbe7e`.
- Root cause: the existing alarm notification was categorized as an alarm and used AlarmManager.setAlarmClock, but it did not set a notification full-screen intent. Android therefore delivered the notification and ringtone without being asked to launch an activity and wake the display.
- Scope: native Smart Reminder screen wake only. The generated MainActivity now calls setShowWhenLocked(true) and setTurnScreenOn(true) when launched with a reminder ID; older Android versions use the corresponding window flags. The alarm notification now sets the existing reminder content PendingIntent as its full-screen intent. On Android 14+, the native bridge checks NotificationManager.canUseFullScreenIntent(); if access is missing, it opens Android's special full-screen-intent access settings and does not report the reminder as successfully scheduled until access is granted and the reminder is saved again. Added `android.permission.USE_FULL_SCREEN_INTENT` to the generated manifest.
- Build workflow now fails closed unless the generated manifest includes USE_FULL_SCREEN_INTENT and the generated Kotlin includes the full-screen notification intent, lock-screen wake calls, and Android 14+ permission check/request.
- Preservation: no web HTML, reminder record schema, IndexedDB storage, ringtone, notification channel, reminder labels/translations, notes, photos, attachments, Calendar, Kharcha, Documents, Memories, PIN/recovery data, package identity, signing configuration, or user data was intentionally changed. Existing AlarmClock scheduling, exact-alarm permission, notification actions, snooze, cancellation, and boot/package-replacement restoration remain in place.
- Pre-edit backup branch: `backup/reminder-screen-wake-fullscreen-2026-11-14`. The exact pre-edit files were fetched back and verified byte-identical:
  - `backups/add_diary_app_actions-before-reminder-screen-wake-fullscreen-2026-11-14.py` — original blob `c9a2794e46a2915dd3d041f1de88966e9a39951a`
  - `backups/build-diary-from-zip-before-reminder-screen-wake-fullscreen-2026-11-14.yml` — original blob `d71558b4fdc6eb35c252ff1c6c9eb5ae332958a6`
  - `backups/latest-before-reminder-screen-wake-fullscreen-2026-11-14.json` — original blob `c794626b4ed9e71b657641895dc0f116bd42c296`
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-reminder-screen-wake-fullscreen-2026-11-14.md` — original blob `3bd4845a4189a64fbe6f95df3874a017117fbe7e`
- Source PR [#3](https://github.com/amuazzinxyz-ops/My-Diary-Updates/pull/3) was squash-merged as commit `4a00783bb539720ade7e980febc3cb1b67e17a6e`. Build workflow run [43598484763](https://github.com/amuazzinxyz-ops/My-Diary-Updates/actions/runs/43598484763) completed with conclusion `success`. The generated manifest/Kotlin checks passed; debug and signed Release APK builds passed; APK publication and artifact uploads passed. The existing signing certificate fingerprint was independently checked and remains `23A4E93F3C7911DCE18389EA583548700C6AD6A3759707F1CD222D07E2408B5A`.
- Published APK: `1.0.140` / versionCode `139`; live feed blob `be9086e97cecde0f4f7c4d2e6152c6350cf540da`; APK SHA-256 `2936ddae0c7b8672bbfcccf1dccf344f4bc5aa4a21f6fc0fd1214a5cb559c588`. The signed APK was downloaded from the workflow artifact and independently hashed; it matches live latest.json. `My-Diary.apk` and `My-Diary-1.0.140.apk` have identical Git blob `f0385aec830257526527da69e63da421271a4ad8`. Web source and mirror remain byte-identical at blob `58db1f74729e21bff7139b068aad202fe58b537d`; WebVersion remains `197`, web SHA-256 remains `4452235be464d6acb8622430f71e4f0a76b416579e41ad91207d52a4d256852e`.
- Physical-device verification is **pending**. User should install via **Me → Check for Updates**, then create/save a short test reminder. If Android opens the full-screen-intent special access page, enable My Diary's full-screen notifications/alarm access, return to My Diary, and save the reminder again. Lock the phone before the reminder time and confirm that the display turns ON while notification and ringtone still arrive. Do not claim screen wake is fixed until the user confirms on their Vivo phone.
- Rollback: use the verified backup branch above; if needed, restore only the native integration script and workflow, then publish a higher versionCode while preserving package identity/signing. Never uninstall the app, clear app data, or delete reminders, notes, photos, attachments, PIN/recovery data, or user records.


# APK 1.0.141 — Keep Smart Reminder notification without auto-opening My Diary (2026-11-14)

- User confirmed the intended behavior: when the phone is locked/screen is off, the Smart Reminder notification and ringtone should still arrive, but My Diary must not open automatically and the phone should remain locked.
- Starting live state: APK 1.0.140 / versionCode 139; Web Update 197; package `com.personal.diaryapp`. Starting feed blob `be9086e97cecde0f4f7c4d2e6152c6350cf540da`; APK SHA-256 `2936ddae0c7b8672bbfcccf1dccf344f4bc5aa4a21f6fc0fd1214a5cb559c588`.
- Scope: native reminder presentation only. Removed the reminder notification's full-screen Activity intent, the reminder-only screen-wake flags in MainActivity, the Android 14+ full-screen-intent permission check/request, and `USE_FULL_SCREEN_INTENT`. Preserved `AlarmManager.setAlarmClock`, exact-alarm permission enforcement, regular notification content tap action, alarm category, notification defaults/sound, snooze/Done actions, reminder scheduling/cancellation, boot/package-replacement restoration, reminder storage and all user data.
- Changed only `scripts/add_diary_app_actions.py` and `.github/workflows/build-diary-from-zip.yml`. Web HTML and Web Update 197 are unchanged. The build workflow now fails closed if full-screen reminder launch or screen-wake code is reintroduced, and checks the normal notification tap action.
- Pre-edit backup branch: `backup/no-auto-open-reminder-2026-11-14`. Verified exact readable backups:
  - `backups/native-script-py-before-no-auto-open-reminder-2026-11-14` — original blob `c16f8927522ce55dfb5018f445f10c7970dc27ff`
  - `backups/build-workflow-yml-before-no-auto-open-reminder-2026-11-14` — original blob `ea4402a0f573b49fbe5f017f83b129eae40129ac`
  - `backups/latest-json-before-no-auto-open-reminder-2026-11-14` — original blob `be9086e97cecde0f4f7c4d2e6152c6350cf540da`
  - `backups/master-register-md-before-no-auto-open-reminder-2026-11-14` — original blob `bf067f5a7f76d3d11d3bbff900323424ecea366c`
- Source PR [#4](https://github.com/amuazzinxyz-ops/My-Diary-Updates/pull/4) was squash-merged as commit `80d5a5fd9b2b94049e7baaae965850798b6c9782`. Merged source script blob is `edca39d3a861eedf87dcabee84776261152ca93b`; workflow blob is `a8781272363673bb2155b44fa1634cbedb3d3280`. Re-fetched main-branch script contains no full-screen intent, screen-wake flags, or full-screen permission; AlarmClock scheduler and ordinary notification content intent remain present.
- Next APK target: `1.0.141` / versionCode `140`; build/publish verification is **pending**. At this register update, live `latest.json` still points to APK 1.0.140 / code 139, so do not install or describe 1.0.141 as published yet. Existing signing certificate must remain `23A4E93F3C7911DCE18389EA583548700C6AD6A3759707F1CD222D07E2408B5A`.
- Physical Vivo V2420 / Android 15 verification is **pending**. After a successful in-app update via **Me → Check for Updates**, create a short test reminder, lock the screen, and confirm notification + ringtone arrive while My Diary stays closed and the phone remains locked. Then test a reminder with the screen ON and confirm tapping its notification still opens the reminder normally. Never claim phone-side success until the user confirms.
- Rollback: use the verified pre-edit files on `backup/no-auto-open-reminder-2026-11-14`; if needed, restore only the native integration script and workflow and publish a higher versionCode. Never uninstall, clear app data, or remove reminders/notes/photos/PIN data.

---

# APK 1.0.141 — Correct reminder notification tap-action build guard (2026-11-14)

- Follow-up to the Smart Reminder no-auto-open repair. The first trigger run `43599842119` failed at the generated-Kotlin static assertion because the workflow expected the text `builder.setContentIntent(content)`, while the actual generated notification builder uses the chained call `.setContentIntent(content)`. This was a false-negative verification check; it did not indicate a runtime reminder-code failure.
- Changed only `.github/workflows/build-diary-from-zip.yml`: the guard now requires exactly one `.setContentIntent(content)` occurrence. No Android runtime source, web HTML, reminder storage, notes, photos, PIN/recovery data, package identity, or signing configuration was changed in this correction.
- Before-edit backups committed and readable in PR #5 branch:
  - `backups/build-workflow-before-reminder-tap-check-2026-11-14.yml`
  - `backups/latest-before-reminder-tap-check-2026-11-14.json`
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-reminder-tap-check-2026-11-14.md`
- PR [#5](https://github.com/amuazzinxyz-ops/My-Diary-Updates/pull/5) merged as commit `66adb151bc31167fa48dfa73fe604ffe137aed65`. Final workflow blob: `8f31523f90f9852e8aa4b3d64bcff07f3a463a41`. Reviewed PR diff: one workflow guard correction plus the three exact backups.
- Corrected build workflow run `43600109747` was started and passed project verification, published HTML/hash checks, translation audit, identity checks, release version guard, and generated-source guard. At the time of this entry the Android debug APK build is still **in progress**; signed release build, APK publication, live feed update, APK hash and signing fingerprint verification are **pending**. Do not call APK 1.0.141 published until every release check passes and `latest.json` points to the verified artifact.
- Live update feed at the start of this correction remains APK `1.0.140` / versionCode `139`, Web Update `197`; latest.json remains authoritative.
- Phone verification on Vivo V2420 / Android 15 is pending. After a verified release is available, use **Me → Check for Updates**, then test screen-off notification + ringtone with My Diary staying closed and phone locked; separately verify tapping the notification opens the reminder normally.
- Rollback for this workflow-only correction: restore the exact workflow from `backups/build-workflow-before-reminder-tap-check-2026-11-14.yml`; preserve all user data and the existing signing identity.

## Final publication verification — APK 1.0.141 (2026-11-14)

- Corrected workflow run `43600109747` completed with conclusion `success`; build job `132462842753` also completed successfully.
- All release-critical steps passed: project/source validation, published HTML/hash checks, translation audit, app identity validation, target version `1.0.141` / versionCode `140`, debug build, signed Release configuration, publish verification, signed APK upload, and APK upload.
- `latest.json` was re-fetched from `main` and now advertises APK `1.0.141`, versionCode `140`, URL `https://raw.githubusercontent.com/amuazzinxyz-ops/My-Diary-Updates/main/My-Diary-1.0.141.apk`, SHA-256 `aaaa7c49a76ed0fc0caef4f78b37cdf695ce22d5d2d0705d3ea275fecfaf959e`. Web Update remains `197` with unchanged SHA-256 `4452235be464d6acb8622430f71e4f0a76b416579e41ad91207d52a4d256852e`.
- GitHub Actions run contains the non-expired `My-Diary-signed-Release-APK` artifact (1,949,061 bytes), and `My-Diary-debug-APK` (2,617,001 bytes). Signed release upload and publish steps report success.
- The workflow's signing-readiness and keystore/alias validation steps passed. Preserve the established signing certificate fingerprint `23A4E93F3C7911DCE18389EA583548700C6AD6A3759707F1CD222D07E2408B5A`.
- The app update is now published. Remaining verification is physical-device behavior only: user must install via **Me → Check for Updates** on Vivo V2420 / Android 15 and confirm notification + ringtone arrive with screen off while My Diary remains closed and the phone locked; then tap the notification to confirm it opens normally. Do not claim device-side confirmation until the user reports it.
- User data remains untouched by this build; do not uninstall or clear app data.


---


## Final publication verification — APK 1.0.142 (2026-11-14)

- Corrected workflow run `43601017474` completed with conclusion **success**; build job `132465753714` completed successfully. Debug APK, signed Release APK, publish, artifact upload and APK upload steps passed. Translation audit artifact was also uploaded.
- Live `latest.json` re-fetched from `main`: APK `1.0.142`, versionCode `141`, package `com.personal.diaryapp`, URL `https://raw.githubusercontent.com/amuazzinxyz-ops/My-Diary-Updates/main/My-Diary-1.0.142.apk`, SHA-256 `9a538b5baa4a6ecf97158502e5b564473b158144c3bc324f41e1f8c83081a9d3`. Downloaded signed Release APK artifact independently hashed; exact SHA-256 matches live feed.
- Workflow signing verification reports v1/JAR and v2 APK signatures valid. Signer certificate SHA-256 matches the existing trusted fingerprint `23A4E93F3C7911DCE18389EA583548700C6AD6A3759707F1CD222D07E2408B5A`. Package/version identity checks passed in workflow. Web Update remains `197`, with unchanged web SHA-256 `4452235be464d6acb8622430f71e4f0a76b416579e41ad91207d52a4d256852e`.
- Release change is limited to the native Smart Reminder presentation: screen wake is routed to transparent `DiaryReminderWakeActivity`, not MainActivity; normal notification tap still targets MainActivity. Existing reminder scheduling, sound, Snooze/Done, restoration, storage and all Diary content/data remain preserved. No web HTML or user data changed.
- Backups: branch `backup/pre-wake-screen-no-app-open-2026-11-14`; files `backups/native-script-py-before-wake-screen-no-app-open-2026-11-14.py`, `backups/build-workflow-yml-before-wake-screen-no-app-open-2026-11-14.yml`, `backups/latest-json-before-wake-screen-no-app-open-2026-11-14.json`, `backups/master-register-md-before-wake-screen-no-app-open-2026-11-14.md`.
- Phone verification is **pending**. User may now install through **Me → Check for Updates**. Test with screen off: screen should wake to lock screen, notification and ringtone should arrive, and My Diary must not open by itself. Tapping the notification should open My Diary normally. Do not claim device-side success until user confirms. Never uninstall or clear app data.


---

# APK 1.0.142 — Restore missing versioned download file (2026-11-14)

- User reported **Me → Check for Updates** failed with HTTP 404. Investigation confirmed live `latest.json` advertised APK 1.0.142 / versionCode 141 and SHA-256 `9a538b5baa4a6ecf97158502e5b564473b158144c3bc324f41e1f8c83081a9d3`, but the versioned path `My-Diary-1.0.142.apk` was missing from the repository. Root cause was a filename mismatch in the previous workflow's git-add list; this task did not alter that workflow.
- Verified the signed Release APK from workflow artifact run `43601017474`: size 2,005,532 bytes; independently computed SHA-256 exactly matches the live feed. Independently computed Git blob SHA-1 is `4d09815ab977bacebfe27a0ea78373e78d72a4e1`, matching the existing `My-Diary.apk` blob exactly. Therefore the already-verified signed APK bytes were reused without rebuilding, re-signing, or changing the feed.
- Minimal repair: added repository path `My-Diary-1.0.142.apk` as an additional tree entry pointing to that exact existing blob. No existing file was overwritten. Commit: `0a3251fc93458bc340b36e81a9b4a041e82b48fc`. Added path re-fetched successfully; its blob SHA is `4d09815ab977bacebfe27a0ea78373e78d72a4e1`. Live `latest.json` re-fetched and remains unchanged at APK 1.0.142 / code 141 / SHA-256 above; Web Update 197 and its hash remain unchanged.
- Pre-repair backup branch: `backup/pre-missing-142-apk-2026-11-14`, created at exact prior main commit `2159ad732a3d536a8803042be56e1ab74c0677d8`. No workflow, native source, web source, app data, notes, photos, reminders, PIN/recovery data, package identity, or signing configuration changed. MUAZZIN was not touched.
- Verification status: missing versioned path now exists in the live main branch and references the byte-identical, previously hash-verified APK. The updater should now be retried via **Me → Check for Updates**. Physical-device download/install test and reminder behavior remain **pending** until the user confirms.


---

# APK 1.0.143 / Web Update 198 — Per-reminder ringtone and audio-file selection (2026-11-14)

- User request: allow a Smart Reminder to use a phone ringtone/alarm tone or an audio file selected from the device. Design decision: choose a sound separately for each reminder, with a default phone alarm option.
- Starting live state: APK 1.0.142 / versionCode 141; Web Update 197; package `com.personal.diaryapp`; main starting commit `89abdd32a130d9d4b82b68e298a0f930da61561e`.
- Scope: native Android reminder sound selection and the existing Smart Reminder form only. Changed `scripts/add_diary_app_actions.py`, `.github/workflows/build-diary-from-zip.yml`, and `web-source/index.html`. The web publisher generated matching `diary-web/index.html` and updated `latest.json`. No unrelated web feature was changed.
- UI: each reminder form now offers three choices: phone ringtone/alarm tone (Android Ringtone Picker), audio file (Android Storage Access Framework / File Manager, `audio/*`), or default phone alarm. Button and default label were added to all 10 supported language dictionaries. The chosen sound label appears in the reminder list and is restored when editing.
- Native behavior: the selected URI is stored with the reminder in the existing reminder record, passed through the alarm PendingIntent, and used to create a sound-specific notification channel with alarm audio attributes. The selected sound is preserved through Snooze and boot/package-replacement restoration. File-picker read permission is persisted for future alarm delivery. Existing reminders without a stored sound URI continue using the default phone alarm.
- Preserved: exact AlarmClock scheduling and permissions, lock-screen wake-only activity, normal notification tap into My Diary, notification category/priority, vibration/lights, Snooze, Done, reminder IDs, existing stored reminders, notes, photos, PIN/recovery data, app package identity, and signing identity. No new storage keys for notes or PIN and no app-data reset. MUAZZIN project untouched.
- Pre-edit backups created and re-fetched successfully on branch `backup/pre-custom-reminder-ringtones-2026-11-14`:
  - `backups/native-script-py-before-custom-reminder-ringtones-2026-11-14.py` (source blob `316b599d5f279747cadd49bc8bc259ea434fe6e5`)
  - `backups/build-workflow-yml-before-custom-reminder-ringtones-2026-11-14.yml` (source blob `bde2fd57bf5d2e8df2a687280fda5469fac22ae2`)
  - `backups/web-source-html-before-custom-reminder-ringtones-2026-11-14.html` and `backups/diary-web-html-before-custom-reminder-ringtones-2026-11-14.html` (both source blob `58db1f74729e21bff7139b068aad202fe58b537d`)
  - `backups/latest-json-before-custom-reminder-ringtones-2026-11-14.json` (source blob `c4b1e86a0a47d05ea4a1235b1267a86935ab6240`)
  - `backups/master-register-md-before-custom-reminder-ringtones-2026-11-14.md` (source blob `f1b8b4e442f52a7dc424f7b16ae7efee9523acf6`)
- Source PR #6 merged as `70604735d4985957add81c0b0c3d950433736f4f`. PR #7 then added a null-safe read of the optional audio-picker result flags in the source script, merged as `c4f3d41fe477b554a35fb08775595d80121f46fb`; this follow-up is source-side defensive handling and does not change normal selected-file behavior.
- Web publisher run `43604761824` completed successfully. Web Update advanced to `198`; `web-source/index.html` and `diary-web/index.html` were re-fetched byte-identical (both Git blob SHA `bc0f12816af112c155c53c1bd611e0d3d2003286`, 353,698 UTF-16 code units). Independently calculated SHA-256 of the exact HTML embedded in the signed APK is `23543bb8712b99de25da4d27accf56bad86376a47f0ceca154c4cf2dc5f5ca74`, matching live `latest.json.webSha256`.
- APK workflow run `43604761859` completed with conclusion `success`: project checks, translation audit, version guard, debug build, signed Release build, signing verification, publication and APK upload all passed. Live `latest.json`: APK `1.0.143`, versionCode `142`, URL `https://raw.githubusercontent.com/amuazzinxyz-ops/My-Diary-Updates/main/My-Diary-1.0.143.apk`, SHA-256 `4eccf17f61389bbb112a1daf910eb88d11315c19c22efa2d9e71171115688961`; Web Update `198` and web SHA-256 above. Versioned APK path exists in the main tree (Git blob SHA `7efc7d32fc297c8937f26e632f7799c4af633740`, 2,008,245 bytes).
- Downloaded the signed Release APK artifact `14117363203` and independently calculated SHA-256 `4eccf17f61389bbb112a1daf910eb88d11315c19c22efa2d9e71171115688961`, matching both the live feed and APK tree blob. Independently inspected signer certificate SHA-256 `23A4E93F3C7911DCE18389EA583548700C6AD6A3759707F1CD222D07E2408B5A`, matching the established signing identity. Workflow's apksigner verification passed.
- A follow-up build workflow run `43604849915` was triggered by PR #7 after the first APK had already published; see the follow-up workflow note below.
- Physical-device test of the new ringtone selector is **pending**. User should install using **Me → Check for Updates**, then create one test reminder with a phone ringtone, another with an audio file, and one with default sound. Confirm each plays when due; test Snooze retains the selected sound and Done still dismisses it. Existing reminders should continue with default phone alarm unless edited. Do not claim device-side success until user confirms.
- Rollback: preserve all backups above and the last known-good APK 1.0.142. If a regression occurs, restore only the affected source/workflow/web files from the verified backup branch and publish a higher versionCode; never uninstall, clear app data, or remove notes/photos/PIN/recovery data.


## Follow-up workflow note — run 43604849915 (2026-11-14)

- This second run was triggered by PR #7's null-safe source-script follow-up after APK 1.0.143 had already been successfully published by run 43604761859.
- Its project checks and debug build passed, and signed Release build configuration completed. The publish step correctly failed closed because the live feed had already advanced to APK 1.0.143 / versionCode 142, while this duplicate run was still approved only for the prior baseline 1.0.142 / code 141.
- APK upload steps were skipped; no duplicate APK or feed overwrite occurred. Re-fetched latest.json remains at 1.0.143 / code 142, SHA-256 4eccf17f61389bbb112a1daf910eb88d11315c19c22efa2d9e71171115688961. The successful publication remains run 43604761859.


---

# Web Update 199 — Personal Calendar completion (2026-11-14)

- User request: complete all remaining Personal Calendar work and verify it carefully. Starting live state: APK 1.0.143 / versionCode 142; Web Update 198; package `com.personal.diaryapp`; source/mirror blob SHA `bc0f12816af112c155c53c1bd611e0d3d2003286`; starting main commit `170a557277fa4261a2b8c52cf81b32500c1e8012`.
- Scope: web-only Personal Calendar and its integration with the existing Diary month view. Changed `web-source/index.html`; the web publisher generated matching `diary-web/index.html` and updated `latest.json`. No native Android source, build workflow, APK, Smart Reminder implementation, notes, photos, storage database version, package identity, or signing data changed.
- Personal Calendar now stores optional event time and details; supports non-repeating, daily, weekly, monthly and yearly recurrence; provides optional event-time reminders using the existing Android AlarmClock/notification bridge with separate `cal-` reminder IDs; supports edit/delete with cancellation/restoration of its own alarms; and includes time/details/repeat fields in Smart Search and PDF report output. Existing Personal Calendar records remain readable; the additional fields are optional and no IndexedDB schema/version migration was made.
- The Diary main month view now merges Personal Calendar event occurrences with existing Notes, marks event days, and displays Hijri day/month labels using `Intl.DateTimeFormat` with an Islamic-calendar fallback. Calendar has a separate section PIN gate/configuration using the existing Me-section PIN/recovery mechanism and its own `calendar` key. New Calendar interface strings were added for all 10 supported languages.
- Recurrence alarm behavior is intentionally bounded and transparent: future one-shot Android alarms are pre-scheduled for up to 30 daily, 52 weekly, 24 monthly, or 10 yearly occurrences, then replenished whenever Personal Calendar is opened. This uses the existing Android AlarmClock scheduler, so scheduled alarms retain the existing screen-off/boot restoration behavior; it is **not** an unbounded native repeating alarm if the user never opens Calendar again after the scheduled horizon. Calendar alerts use the existing default phone alarm channel. Phone-side delivery remains pending verification.
- Pre-edit backup branch: `backup/pre-personal-calendar-completion-2026-11-14` (initial backup set), and work branch `work/personal-calendar-completion-2026-11-14`. Six exact backups were created on the work branch and fetched back readable before editing:
  - `backups/web-source-before-personal-calendar-work-2026-11-14.html` — blob SHA `bc0f12816af112c155c53c1bd611e0d3d2003286`
  - `backups/diary-web-before-personal-calendar-work-2026-11-14.html` — blob SHA `bc0f12816af112c155c53c1bd611e0d3d2003286`
  - `backups/latest-before-personal-calendar-work-2026-11-14.json` — blob SHA `3d5c4909a73736b777bc855006482184d1d3ac26`
  - `backups/master-register-before-personal-calendar-work-2026-11-14.md` — blob SHA `a73b2709787c015436b897c770921cdb9d175c11`
  - `backups/native-script-before-personal-calendar-work-2026-11-14.py` — blob SHA `865303b946368f79f0366407ae49138dc2907bb5`
  - `backups/build-workflow-before-personal-calendar-work-2026-11-14.yml` — blob SHA `b313f11797f093b36ca38a11b7165bb796d6ed84`
- Source changes were committed on work branch `work/personal-calendar-completion-2026-11-14`; PR #9 merged by squash as commit `76bae63175d332f35b90ac2b54c87b3b2ef6c3ad`. Web publisher run `43607476077` completed with conclusion **success**. Publisher commit: `5959ca3916e1a336f0e3a935b5c6d19fcaab7066`.
- Verification: both inline JavaScript blocks passed V8 parse checks. Targeted recurrence checks passed for one-off, monthly 31st-to-short-month clamping, daily 30-occurrence horizon, weekly 52-occurrence horizon, and yearly 10-occurrence horizon. All 8 new Calendar translation keys were confirmed present in all 10 language dictionaries. Targeted static checks confirmed event time/details, recurrence selector, optional event reminder, separate Calendar PIN, Hijri rendering, main month-view event integration, full-screen alarm permission check, and cancellation on deletion.
- Live post-publish verification: `web-source/index.html` and `diary-web/index.html` were re-fetched and are byte-identical; both Git blob SHA `17e6e63fa9faf0074205b2cd5bfad3880cc6a0d9`, length 367,387 characters. Independently computed UTF-8 SHA-256 `529b3e39e1a7e26d85b235b17ada0f2a17b2cfdc85dee3940ac7a5b88bc93018` matches live `latest.json.webSha256`; live webVersion is 199. APK remains 1.0.143 / versionCode 142 with unchanged SHA-256 `4eccf17f61389bbb112a1daf910eb88d11315c19c22efa2d9e71171115688961`; no APK rebuild or signing action.
- Phone verification is **pending**. User should install Web Update 199 through **Me → Check for Updates**, then test: Personal Calendar opens with its own PIN gate; create/edit/delete an event with date/time/details; check daily/weekly/monthly/yearly display in the main month view; verify Hijri labels in different languages; test one-time and recurring event alerts with screen off and after reboot; confirm Snooze/Done affect only that event occurrence and Smart Reminder continues unchanged. Do not claim physical-device success until user confirms.
- Rollback: use the exact backups above on `work/personal-calendar-completion-2026-11-14`; restore only `web-source/index.html` if needed and publish a higher webVersion. Do not roll back or alter APK/native files, and never clear app data or delete Calendar records.


---

# Web Update 200 — Remove Personal Calendar inner lock button (2026-11-14)

- User asked to remove the extra Lock button shown inside Personal Calendar. Confirmed the intended scope by inspecting the live implementation: this was the modal-header `meFeatureLock` control, whose click simply closes the feature and returns to Me. The actual Calendar PIN gate is a separate flow.
- Minimal change to `web-source/index.html` only: hide `meFeatureLock` when `kind==='calendar'`. Preserve the PIN gate, PIN verify/create/forgot/recovery/manager functions, Calendar records, reminder alarms, and all other feature behavior. The existing button visibility for Documents and Memories remains unchanged; Kharcha remains unchanged.
- Before editing, fetched the live Master Register, source/mirror, feed, native script and Android build workflow. Created branch `work/remove-calendar-inner-lock-button-2026-11-14`. Six backups were created and fetched back readable with exact pre-edit lengths:
  - `backups/web-source-before-calendar-lock-button-removal-2026-11-14.html`
  - `backups/diary-web-before-calendar-lock-button-removal-2026-11-14.html`
  - `backups/latest-before-calendar-lock-button-removal-2026-11-14.json`
  - `backups/master-register-before-calendar-lock-button-removal-2026-11-14.md`
  - `backups/native-script-before-calendar-lock-button-removal-2026-11-14.py`
  - `backups/build-workflow-before-calendar-lock-button-removal-2026-11-14.yml`
- Both inline JavaScript blocks passed V8 syntax parsing. PR #10 merged by squash as commit `c6fe40c215883b9981d4973c295d7c068fe92c4e`.
- Web publisher run `43610280385` completed with conclusion **success**. Live `webVersion=200`; `web-source/index.html` and `diary-web/index.html` were re-fetched and are byte-identical, both Git blob SHA `7d42a5aa280f0a9ed3217dabe81ad931a7156032`, 367,387 characters. Live feed `webSha256=eac11a930eb722e49ccf6b4146555d34868405f0b144d8ad1f9e060d65b61c48`.
- APK remains unchanged at `1.0.143` / versionCode `142`, SHA-256 `4eccf17f61389bbb112a1daf910eb88d11315c19c22efa2d9e71171115688961`. No APK rebuild, native Android source change, data migration or signing action.
- Phone check: install the web change through **Me → Check for Updates**. Confirm the extra inner Lock button is gone from Personal Calendar and the PIN gate still appears when reopening it. No user-device test has yet been reported.


---

# Web Update 201 — Smart Reminder ringtone choices in Personal Calendar (2026-11-14)

- User request: Personal Calendar event reminders should have the same ringtone/sound selection options as Smart Reminder.
- Starting live state: APK 1.0.143 / versionCode 142; Web Update 200; package `com.personal.diaryapp`; starting source/mirror blob SHA `7d42a5aa280f0a9ed3217dabe81ad931a7156032`; starting main commit `2dc10f24f36aacf265aa302bf5b9fe6386fd52ba`.
- Scope: web-only change to `web-source/index.html`; publisher regenerated `diary-web/index.html` and `latest.json`. No native Android source, Android build workflow, APK, package/signing identity, Smart Reminder code, Calendar PIN/recovery, recurrence rules/horizons, records database, or other Diary feature was changed.
- Calendar form now reuses the exact existing Android Smart Reminder picker and bridge: choose a phone ringtone/alarm tone, choose an audio file from the device, or use the default phone alarm. It uses the existing localized `reminderSound` and `reminderSoundDefault` labels across all 10 supported languages.
- Selected sound URI and label are saved with the Calendar event; the URI is passed to every scheduled Calendar occurrence, including recurring occurrences. Editing an existing event restores its previous sound selection. The event card shows the selected sound label when its reminder is enabled. Existing Calendar records without a saved sound continue to use the default phone alarm.
- No native changes were needed: the existing Android `pickReminderSound` and `scheduleReminder(..., soundUri)` bridge already supports the same picker and sound URI for the separate `cal-` alarm IDs.
- Pre-edit backup branch: `work/calendar-reminder-ringtone-2026-11-14`. Exact backups were created and fetched back readable before editing:
  - `backups/web-source-before-calendar-reminder-ringtone-2026-11-14.html` — blob SHA `7d42a5aa280f0a9ed3217dabe81ad931a7156032`
  - `backups/diary-web-before-calendar-reminder-ringtone-2026-11-14.html` — blob SHA `7d42a5aa280f0a9ed3217dabe81ad931a7156032`
  - `backups/latest-before-calendar-reminder-ringtone-2026-11-14.json` — blob SHA `7362ea002629f1841d2fee7c72da3d6aaa0dbe9f`
  - `backups/master-register-before-calendar-reminder-ringtone-2026-11-14.md` — blob SHA `836302ec91d79c334c32ff737bad10e47db0f648`
- Source PR #11 merged by squash as commit `a54d578d1c162b8bd0af4e447807bde17cdce265`. Web publisher commit `d14dd75c5ec7e25eed852ad0399fc5da13a96c27` published Web Update 201. The publisher workflow run ID/conclusion was not exposed by the available run/status listing; publication itself was verified from the live source, mirror and feed.
- Post-publish verification: live `web-source/index.html` and `diary-web/index.html` were re-fetched byte-identical; both Git blob SHA `2275664443613a817d12aaf42a3cf56889185a90`, length 369,123 characters. Independently calculated UTF-8 SHA-256 `5d0f47cca0424f0d9c31ce94e85a280caf38633ec53252f89951b85fb9f50686` matches live `latest.json.webSha256`; live webVersion is 201.
- Targeted source checks confirmed the Calendar form calls the existing sound picker, stores/restores the selected URI and label, and passes the URI to each `cal-` scheduled alarm. Existing records fall back to empty URI/default alarm. APK remains 1.0.143 / versionCode 142 with unchanged SHA-256 `4eccf17f61389bbb112a1daf910eb88d11315c19c22efa2d9e71171115688961`; no APK rebuild or signing operation.
- Physical-device verification is **pending**. User should install Web Update 201 through **Me → Check for Updates**, then create a Calendar event with reminder enabled and test all three sound choices; edit the event to confirm the choice is retained; test one recurring event occurrence. Do not claim phone-side success until the user confirms.
- Rollback: use the exact pre-edit backups above and restore only `web-source/index.html` if required; publish a higher webVersion. Never clear app data or alter Calendar records, PIN/recovery data, notes, photos, or APK/signing files.


---

# Web Update 202 — Remove inner Lock buttons from My Documents and My Memories (2026-11-14)

- User request: remove only the extra header Lock button from **My Documents** and **My Memories**.
- Starting live state: APK 1.0.143 / versionCode 142; Web Update 201; package `com.personal.diaryapp`; starting source/mirror Git blob SHA `2275664443613a817d12aaf42a3cf56889185a90`; starting main commit `6c49082e013babf782d7cfd6ed9971542102eacb`.
- Scope: one-line web-only change in `web-source/index.html`: changed the modal-header Lock button visibility assignment to `meFeatureLock.hidden=true;`. This removes the extra button from the two requested sections. No other feature UI or behavior was changed.
- Explicitly preserved: the separate Documents and Memories PIN protection gate (`meFeatureProtected` still includes both kinds), PIN create/verify, Forgot PIN and recovery configuration, PIN Manager, document and memory record storage, attached files/photos, and all other Diary features. No PIN or user-data storage key was modified or deleted. Calendar and Kharcha security logic remains unchanged.
- Pre-edit backups were created on branch `backup/pre-documents-memories-lock-removal-2026-11-14` and fetched back readable with matching original Git blob SHAs:
  - `backups/web-source-before-documents-memories-lock-removal-2026-11-14.html` — `2275664443613a817d12aaf42a3cf56889185a90`
  - `backups/diary-web-before-documents-memories-lock-removal-2026-11-14.html` — `2275664443613a817d12aaf42a3cf56889185a90`
  - `backups/latest-before-documents-memories-lock-removal-2026-11-14.json` — `83a86d6dbdcbbaa30bdb8d906ecbdf2afda27b86`
  - `backups/master-register-before-documents-memories-lock-removal-2026-11-14.md` — `c9775ab431a8ff8479d7eae40e27af8572a06437`
  - `backups/native-script-before-documents-memories-lock-removal-2026-11-14.py` — `865303b946368f79f0366407ae49138dc2907bb5`
  - `backups/build-workflow-before-documents-memories-lock-removal-2026-11-14.yml` — `b313f11797f093b36ca38a11b7165bb796d6ed84`
- Work branch: `work/remove-documents-memories-lock-buttons-2026-11-14`. PR #12 merged by squash as commit `e21f7ff03d0db75cd059b8c6beb4a3e0c352960a`. PR changed exactly one file with 1 insertion and 1 deletion.
- Pre-merge validation: both inline JavaScript blocks passed V8 syntax parsing. Static checks confirmed the PIN protection gate, PIN configuration/recovery helpers, PIN Manager handler, and document/memory data paths remain present.
- Web publisher automatically created commit `cfae818f2f343158c8f1a0ea3c191aa2daf521b6` (`Publish My Diary web bundle update`). Live `latest.json` advanced to Web Update 202 and reports web SHA-256 `7b7c2bee7ac1d575748734521cd5602e17bab12b718ed7f9606e41aadb857a0d`. Live `web-source/index.html` and `diary-web/index.html` were re-fetched and are identical; both Git blob SHA `1ee54525c9a6dcbfe8f2cd9ca2c94ddffbcd7e10`, length 369071 characters.
- APK remains unchanged at 1.0.143 / versionCode 142 with SHA-256 `4eccf17f61389bbb112a1daf910eb88d11315c19c22efa2d9e71171115688961`. This was a web-only update; no APK rebuild, native Android source change, signing action, package identity change, or app-data migration.
- Physical-device verification is **pending**. Install Web Update 202 through **Me → Check for Updates**. Confirm the extra Lock button is absent from both My Documents and My Memories, and separately verify that opening each still presents its PIN gate and Forgot PIN/recovery remains available. Do not claim phone-side success until the user confirms.
- Rollback: use the exact pre-edit backups above and restore only `web-source/index.html` if needed, then publish a higher webVersion. Never clear app data or delete/modify documents, memories, PIN/recovery data, notes, photos, or APK/signing files.


---

# Web Update 203 — Hide Unlock buttons in all four PIN-protected Me sections (2026-11-14)

- User request: remove only the visible **Unlock** button from the PIN-entry screens of Personal Calendar, My Kharcha, My Documents and My Memories; entering the PIN should unlock automatically.
- Starting live state: APK 1.0.143 / versionCode 142; Web Update 202; package `com.personal.diaryapp`; source/mirror blob SHA `1ee54525c9a6dcbfe8f2cd9ca2c94ddffbcd7e10`; main starting commit `9492ab683d6fd53a3961714e6a5a82cd15dd3adf`.
- Scope: web-only change to `web-source/index.html`. The PIN submit button is hidden from the interface, while the existing form submit handler is still used programmatically when the entered PIN reaches the configured length (4 or 8 digits).
- Preserved: all four PIN gates, PIN create/verify, Forgot PIN and recovery, PIN Manager, stored PIN/recovery keys, Calendar/Kharcha/Documents/Memories records and attachments, and all other Diary features. No native Android source, APK, signing data, package identity, data schema or user records changed.
- Verified pre-edit backups on `backup/pre-four-section-unlock-button-removal-2026-11-14`:
  - `backups/web-source-before-four-section-unlock-button-removal-2026-11-14.html` — blob `1ee54525c9a6dcbfe8f2cd9ca2c94ddffbcd7e10`
  - `backups/diary-web-before-four-section-unlock-button-removal-2026-11-14.html` — blob `1ee54525c9a6dcbfe8f2cd9ca2c94ddffbcd7e10`
  - `backups/latest-before-four-section-unlock-button-removal-2026-11-14.json` — blob `05cb21b16f187dbe47f2b21d6a2ef771107c61de`
  - `backups/master-register-before-four-section-unlock-button-removal-2026-11-14.md` — blob `9addcfa4932780ff735da9036907c7c7174d13da`
- Work branch: `work/remove-four-section-unlock-buttons-2026-11-14`; PR #13 merged by squash as `d26df0e8756eeef0c9c2a27bb644fa906fb64ed7`. Publisher commit: `72f3fae62265bcd787c945b1947816634fefbfd4`; live feed advanced to Web Update 203.
- Both inline JavaScript blocks passed V8 syntax parsing. Targeted checks confirmed the submit control is hidden, auto-submit triggers at `pin.maxLength` (4 or 8), all four sections remain PIN-protected, and recovery helpers remain present.
- Post-publish verification: source and mirror are byte-identical; both blob SHA `3704836682fb3f53b77ee370ae15a2e8fe12b9cc`, length 369079. Independently computed UTF-8 SHA-256 `e7105a89a36a06e39b551f059cd68597565aad04950e15a6155964e322e98c58` matches live `latest.json.webSha256`; live webVersion is 203.
- APK remains 1.0.143 / versionCode 142 with unchanged SHA-256 `4eccf17f61389bbb112a1daf910eb88d11315c19c22efa2d9e71171115688961`; no APK rebuild or signing operation.
- Physical-device verification is **pending**. Install Web Update 203 through **Me → Check for Updates**, then confirm the Unlock button is absent in all four sections, PIN entry unlocks automatically, and Forgot PIN/recovery remains available. Do not claim phone-side success until user confirms.
- Rollback: restore only `web-source/index.html` from the verified backup branch above and publish a higher webVersion if needed. Never clear app data or alter PIN/recovery data, records, attachments, notes, photos or APK/signing files.


---

# Web Update 204 — Remove header × from five Me sections (2026-11-14)

- User request: remove the **× close button only** from inside these five sections: Personal Calendar, Smart Reminder, My Kharcha, My Documents and My Memories. Keep the existing **Wapas/Back** button.
- Starting live state: APK 1.0.143 / versionCode 142; Web Update 203; package `com.personal.diaryapp`; source/mirror blob SHA `3704836682fb3f53b77ee370ae15a2e8fe12b9cc`; main starting commit `58cb700bf6d1bbc28d7116d6d20dfc3b22b66c57`.
- Scope: web-only change to `web-source/index.html`, in the shared Me-feature modal header used by all five sections. Removed the header × element and its click handler; retained the Wapas/Back button in the header and its existing `closeMeFeature` click action. Existing backdrop-click behavior is unchanged. No other × controls elsewhere in the app were targeted.
- Preserved: all five feature contents and functions, PIN gates, automatic PIN verification, Forgot PIN/recovery, PIN Manager, records, attachments, reminders, and all other Diary features. No native Android source, APK, package/signing identity, data schema or user records changed.
- Pre-edit backups created on `backup/pre-five-me-sections-close-x-removal-2026-11-14` and fetched back readable:
  - `backups/web-source-before-five-me-section-close-x-removal-2026-11-14.html` — blob `3704836682fb3f53b77ee370ae15a2e8fe12b9cc`
  - `backups/diary-web-before-five-me-section-close-x-removal-2026-11-14.html` — blob `3704836682fb3f53b77ee370ae15a2e8fe12b9cc`
  - `backups/latest-before-five-me-section-close-x-removal-2026-11-14.json` — blob `e00f8aacede6206c7ec3ce1299e4131855e15f13`
  - `backups/master-register-before-five-me-section-close-x-removal-2026-11-14.md` — blob `7b4bdc7d944d4b7c66dffae045cd6f8011311f92`
- Work branch `work/remove-five-me-section-close-x-2026-11-14`; PR #14 merged by squash as `aa19d63283c99aa3d4908221bbc2db489fbf93fb`. Publisher commit `7d8aba5d9d90a2a62c422c9793cde606fdb24b2f`; live feed advanced to Web Update 204. The workflow-run status endpoint did not expose a run ID/conclusion in this session; publication is independently verified by the live source, mirror and feed.
- Validation: both inline JavaScript blocks passed V8 syntax parsing. Targeted checks confirm the × element and its handler are absent; the Wapas/Back button remains in the header and still calls `closeMeFeature`. PR diff changed only `web-source/index.html` (2 additions, 3 deletions).
- Post-publish verification: live `web-source/index.html` and `diary-web/index.html` are byte-identical; both blob SHA `c8f2dd931eccc40f79be21ff5627518c2fe9d78a`, length 368893. Independently calculated UTF-8 SHA-256 `ea4433cfcdfe05680c669d11117199ac97a6356ced47f181a5bd960130bec746` matches live `latest.json.webSha256`; live webVersion is 204.
- APK remains 1.0.143 / versionCode 142 with unchanged SHA-256 `4eccf17f61389bbb112a1daf910eb88d11315c19c22efa2d9e71171115688961`; no APK rebuild or signing action.
- Physical-device verification is **pending**. Install Web Update 204 through **Me → Check for Updates** and confirm × is absent in all five sections while Wapas/Back remains visible and works. Do not claim phone-side success until user confirms.
- Rollback: restore only `web-source/index.html` from the verified backup branch above and publish a higher webVersion if required. Never clear app data or alter records, attachments, PIN/recovery data, notes, photos or APK/signing files.


---

# Web Update 205 — Open four PIN-removed sections directly (2026-11-14)

- User reported that after removing a section PIN through the PIN control, reopening Personal Calendar, My Kharcha, My Documents or My Memories incorrectly asked them to create a new PIN. User clarified the PIN control should only set/remove the lock; when removed, the section should open directly.
- Starting live state: APK 1.0.143 / versionCode 142; Web Update 204; package `com.personal.diaryapp`; source/mirror blob SHA `c8f2dd931eccc40f79be21ff5627518c2fe9d78a`; starting main commit `9b6ea378304212109618b554b6512d923957f492`.
- Root cause: `openMeFeature(kind)` unconditionally showed the PIN setup/verification screen for every protected section, even when no PIN configuration existed.
- Minimal web-only change: `openMeFeature(kind)` now calls `showMeFeaturePin(kind)` only when the section is protected **and** `meFeaturePinConfig(kind)` exists. If no PIN configuration exists because the user removed the lock, it opens the section directly. Existing configured PINs still require PIN verification. No PIN or recovery keys, stored values, section records, attachments, native Android source, APK, package identity or signing data were changed.
- Verified pre-edit backups on `backup/pre-open-unlocked-four-sections-2026-11-14`, all fetched back and content-compared:
  - `backups/web-source-before-open-unlocked-four-sections-2026-11-14.html` — blob `c8f2dd931eccc40f79be21ff5627518c2fe9d78a`
  - `backups/diary-web-before-open-unlocked-four-sections-2026-11-14.html` — blob `c8f2dd931eccc40f79be21ff5627518c2fe9d78a`
  - `backups/latest-before-open-unlocked-four-sections-2026-11-14.json` — blob `57fae8e887b6246e593a36381a92a1bcf30cfe85`
  - `backups/master-register-before-open-unlocked-four-sections-2026-11-14.md` — blob `53674831a7c5eba841b2e60f81f4515afb6b720f`
- Work branch: `work/open-unlocked-four-me-sections-2026-11-14`. PR #15 merged by squash as `b4a8f567f909665961a2334db44743bb86344a87`. Publisher workflow run `43615653486` completed with **success**; publisher commit `b98f605288c06f8cb18a24c79683d36520466205`.
- Validation: both inline JavaScript blocks passed V8 syntax parsing. Targeted checks confirmed no-PIN sections open directly, existing configured PINs still invoke the PIN gate, and the PIN removal and PIN Manager code remains present and unchanged. Source PR changed only `web-source/index.html`.
- Post-publish verification: live `web-source/index.html` and `diary-web/index.html` are byte-identical; both Git blob SHA `9d27305f6c0d93117291e60caffa399183842be7`, length 368919. Independently calculated UTF-8 SHA-256 `7c0f62ef52de645088c3ae7f782e503ee573e6c1209ba8bf2e9765c50b432b2c` matches live `latest.json.webSha256`; live webVersion is 205.
- APK remains 1.0.143 / versionCode 142 with unchanged SHA-256 `4eccf17f61389bbb112a1daf910eb88d11315c19c22efa2d9e71171115688961`; no APK rebuild or signing operation.
- Physical-device verification is **pending**. Install Web Update 205 through **Me → Check for Updates**. Confirm all four sections open directly after their PIN lock is removed; then set a PIN for one section and confirm that it still asks for the PIN on the next opening. Do not claim phone-side success until the user confirms.
- Rollback: restore only `web-source/index.html` from the verified backup branch above and publish a higher webVersion if required. Never clear app data or alter PIN/recovery data, records, attachments, notes, photos or APK/signing files.


# Web Update 206 — Restore the in-section Lock On / Lock Off PIN button (2026-11-14)

- User corrected the previous change: the PIN button inside each protected Me section must remain available to both set and remove the lock. The button must not disappear when the lock is removed.
- Starting live state: Web Update 205; APK 1.0.143 / versionCode 142; package com.personal.diaryapp; starting main commit ebf57c39898fc339faa76eb30893d7a84597fa5e; starting source/mirror blob SHA 9d27305f6c0d93117291e60caffa399183842be7; starting feed web SHA-256 7c0f62ef52de645088c3ae7f782e503ee573e6c1209ba8bf2e9765c50b432b2c.
- Changed only web-source/index.html. The in-section PIN management button is now visible for all four protected sections (Personal Calendar, My Kharcha, My Documents, My Memories). With no saved PIN it offers Lock Lagayein (PIN setup); with a saved PIN it offers Change PIN and Lock Hatayein (requires current PIN verification). Removing the PIN still clears only the existing PIN and recovery configuration keys. Opening a section with no configured PIN still opens directly; an existing PIN still gates entry.
- No PIN hashing, recovery process, storage key names, notes, photos, section records, other buttons, native Android files, APK, package identity or signing data changed.
- Verified pre-edit backups on branch backup/before-restore-me-feature-pin-toggle-2026-11-14: backups/web-source-before-restore-me-feature-pin-toggle-2026-11-14.html; backups/diary-web-before-restore-me-feature-pin-toggle-2026-11-14.html; backups/latest-before-restore-me-feature-pin-toggle-2026-11-14.json; backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-restore-me-feature-pin-toggle-2026-11-14.md.
- Source change reviewed; only the manager function and its visibility condition changed. Both inline JavaScript blocks parsed successfully. Targeted checks passed for Lock Lagayein, Lock Hatayein with current-PIN verification, Change PIN, recovery-key clearing, direct open without PIN, and PIN gate when configured.
- PR #16 merged by squash as bdd6d581434109b87113c924a049e755dda45c52. Web-only publisher workflow run 43616325412 completed with success.
- Post-publish source and mirror are byte-identical; both blob SHA 6e9f6a0ffb9375e57c829d4694d6d3f38c71f9da. Live feed webVersion 206; feed webSha256 92dedf123be990a1ca71e3f4949425b18d11f7d61c9817f43c77bfd5b84d6d6c. APK remains 1.0.143 / versionCode 142; SHA-256 4eccf17f61389bbb112a1daf910eb88d11315c19c22efa2d9e71171115688961; no APK rebuild or signing change. Source/mirror/feed metadata consistency verified.
- Physical-device verification pending. Install via Me → Check for Updates. Test each of the four sections: after removing the lock, the section opens directly and the in-section PIN button remains available to set a new PIN; after setting a PIN, reopening asks for the PIN and the manager offers Change PIN / Lock Hatayein.
- Rollback: restore only web-source/index.html from the verified pre-edit backup branch if needed; preserve all user data and PIN/recovery state.


# Web Update 207 — Keep Lock Hatayein out of the section-opening PIN prompt (2026-11-14)

- User clarified that the four protected Me sections should show only PIN entry when opening a locked section; **Lock Hatayein** belongs only inside the section's PIN management button.
- Starting state: Web Update 206; APK 1.0.143 / versionCode 142; package `com.personal.diaryapp`; starting source/mirror blob SHA `6e9f6a0ffb9375e57c829d4694d6d3f38c71f9da`; starting feed web SHA-256 `92dedf123be990a1ca71e3f4949425b18d11f7d61c9817f43c77bfd5b84d6d6c`.
- Changed only `web-source/index.html`: removed the Lock Hatayein button and its handler from `showMeFeaturePin(kind)`, the screen shown while opening a locked section. Kept PIN entry, Forgot PIN, and the existing Lock Hatayein action in `showMeFeaturePinManager(kind)` unchanged. This applies to Personal Calendar, My Kharcha, My Documents and My Memories through the shared functions.
- Backup branch: `backup/before-remove-pin-remove-from-entry-screen-2026-11-14`; verified backups: `backups/web-source-before-remove-pin-remove-from-entry-screen-2026-11-14.html`, `backups/diary-web-before-remove-pin-remove-from-entry-screen-2026-11-14.html`, `backups/latest-before-remove-pin-remove-from-entry-screen-2026-11-14.json`, `backups/master-register-before-remove-pin-remove-from-entry-screen-2026-11-14.md`.
- PR #17 merged by squash as `8a4ba16117f5c3cd8f0be6897ceb285f55dad8e4`. The source diff was exactly three deletions (the entry-screen Lock Hatayein control and handler). Post-publish source and mirror are byte-identical with blob SHA `513044d87913a167e0c8b8acaa09e562093d15d6`. Live `latest.json` advanced to webVersion 207 with web SHA-256 `0584c0680e77ff35a78d52e4b8756b471a78d57a7b9e17b68441c55f931e8ccd`. The publisher run ID/conclusion was not exposed by the available workflow interface in this session; publication is verified from the live source, mirror and feed.
- Targeted live-code check: no `pinRemove` control remains in the PIN-entry function; the single `pinRemove` action remains in the PIN manager. APK remains 1.0.143 / versionCode 142 with unchanged SHA-256 `4eccf17f61389bbb112a1daf910eb88d11315c19c22efa2d9e71171115688961`; no APK rebuild, signing, storage-key or data change.
- Physical-device verification pending. Use **Me → Check for Updates**; for each of the four sections confirm that opening a locked section shows PIN entry without Lock Hatayein, and the in-section PIN manager still provides Lock Hatayein. Preserve all existing PIN/recovery data and user records.


# Web Update 208 — Add 50 font choices to both Diary writing controls (2026-11-14)

- User asked whether both existing font selectors could be expanded from 7 to up to 50 modern fonts; user then said “Aage” to continue the work.
- Starting live state: Web Update 207; APK 1.0.143 / versionCode 142; package `com.personal.diaryapp`; starting source/mirror blob SHA `513044d87913a167e0c8b8acaa09e562093d15d6`; starting feed web SHA-256 `0584c0680e77ff35a78d52e4b8756b471a78d57a7b9e17b68441c55f931e8ccd`.
- Scope: web-only change to `web-source/index.html`. Both existing text-format controls (note title/cover text and note body/detail text) now use the same 50-choice font list. The original seven options remain; 43 additional named families include modern sans-serif, serif, script, Devanagari and Arabic/Urdu families. The font whitelist and dropdown share one list so stored font-family values remain accepted. Google Fonts stylesheet loading was added for the 43 additional families; when the network/font service is unavailable, browser/system fallback fonts remain available.
- No changes to font-size range, bold/italic/underline, colour controls, note/photo storage, PINs, recovery, other Diary features, native Android files, APK, package identity or signing data.
- Backups verified before editing on branch `backup/before-50-fonts-2026-11-14`: `backups/web-source-before-50-fonts-2026-11-14.html`, `backups/diary-web-before-50-fonts-2026-11-14.html`, `backups/latest-before-50-fonts-2026-11-14.json`, `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-50-fonts-2026-11-14.md`.
- Change branch: `feature/50-diary-fonts-2026-11-14`; source commit `35d18a55032185264c22251221c1ae4b7ab1dbc0`. PR #18 merged by squash as `9d8052ac55f9eba010bd5b7ea9c1e16cbbb30b81`.
- Full diff reviewed: one file only (`web-source/index.html`), six additions and two deletions. Targeted source checks confirmed exactly 50 entries, both existing control call sites retained and wired to the shared list, original seven options retained, and old seven-entry dropdown/whitelist arrays removed.
- Web-only publisher workflow run `43623773751` completed with conclusion `success`; publisher log independently computed SHA-256 `4cc058b5317d752fd6e691a0475ab66692086b49b82060511160f7c2e4b70997` and published Web Update 208. Publisher commit: `34178eb`.
- Post-publish verification: source and mirror are byte-identical; both blob SHA `336d00f415926a63a95ecc0b68bdd34c2e1a5f48`. Live `latest.json` webVersion `208`; its webSha256 matches the publisher-computed SHA-256 `4cc058b5317d752fd6e691a0475ab66692086b49b82060511160f7c2e4b70997`. Feed URL remains the web-source URL. APK remains 1.0.143 / versionCode 142; SHA-256 `4eccf17f61389bbb112a1daf910eb88d11315c19c22efa2d9e71171115688961`; no APK rebuild or signing change.
- Rollback reference: restore only `web-source/index.html` from the verified pre-edit backup branch if needed, then allow the web publisher to sync the mirror/feed. Do not touch local user notes, photos or PIN data.
- Physical-device verification pending. User should open My Diary → Me → Check for Updates, then open a new note and test both font selectors: confirm each shows 50 options, select different fonts in the title and body, save/reopen the note, and verify formatting remains. Some additional fonts require internet access to download; offline fallback may differ by device.


---

# Web Update 209 — Keep B, I and U formatting buttons together (2026-11-14)

- User asked to move the **B (Bold)** and **I (Italic)** buttons beside **U (Underline)**. Inspection showed the three controls were already appended consecutively, but the toolbar's wrapping layout could split them across lines on narrow mobile screens.
- Starting live state: Web Update 208; APK `1.0.143` / versionCode `142`; package `com.personal.diaryapp`; source/mirror blob SHA `336d00f415926a63a95ecc0b68bdd34c2e1a5f48`; feed web SHA-256 `4cc058b5317d752fd6e691a0475ab66692086b49b82060511160f7c2e4b70997`.
- Changed only `web-source/index.html`: wrapped the existing B, I and U buttons in one inline-flex, non-wrapping group so they remain side-by-side. Existing button instances, click handlers, aria labels/pressed state, font-size and font-family controls, text colour control and both formatting-tool call sites remain unchanged.
- Pre-edit backup branch: `backup/before-format-buttons-biu-order-2026-11-14`. Exact readable backups, fetched back and content-verified:
  - `backups/web-source-before-format-buttons-biu-order-2026-11-14.html` — blob `336d00f415926a63a95ecc0b68bdd34c2e1a5f48`
  - `backups/diary-web-before-format-buttons-biu-order-2026-11-14.html` — blob `336d00f415926a63a95ecc0b68bdd34c2e1a5f48`
  - `backups/latest-before-format-buttons-biu-order-2026-11-14.json` — blob `76afdb76fe30db04153d2620eb416a8eec34c943`
  - `backups/master-register-before-format-buttons-biu-order-2026-11-14.md` — blob `2e3afe348d26a1760fef540c4956e4a67cecab11`
- Source commit `47ff63463c7730de9b7da31e0810ac1069bba0dd`; PR #19 squash-merged as `63099f3b96241582c59ee5b5bef3eca5eb46c70e`. Reviewed PR diff: exactly one file, `web-source/index.html`, with 3 additions and 1 deletion. Targeted checks confirmed the B/I/U group and non-wrapping CSS, existing shared formatting click handler, 50-font list, and retained font-size/family controls.
- Web-only publisher workflow run `43624342152` completed with conclusion **success**. Live feed advanced to Web Update `209`. Post-publish source and mirror are byte-identical; both Git blob SHA `99c79234470753bf6284adfc56daa267902460cb`. Independently calculated UTF-8 SHA-256 `df66a9c292933007a658456c77580073075903e48ca6912c367422128ebfa196` matches live `latest.json.webSha256`.
- APK remains `1.0.143` / versionCode `142`; SHA-256 `4eccf17f61389bbb112a1daf910eb88d11315c19c22efa2d9e71171115688961`; no APK rebuild or signing change.
- Physical-device verification is **pending**. User should open My Diary → Me → Check for Updates, open a new note, and confirm B, I and U stay together in both formatting toolbars and each button still works. Do not claim phone-side success until the user confirms.
- Rollback: restore only `web-source/index.html` from the verified pre-edit backup branch above and publish a higher webVersion if needed. Preserve notes, photos, formatting data, PIN/recovery data and all other user records.


# Text Colour Palette — published as Web Update 210 (2026-11-14)

- User request: add more colours to both existing text-colour controls (Cover/name field and Details/text field). User confirmed the proposed preset palette while retaining the current custom colour picker and independent colour selection for each field.
- Starting authoritative live state: Web Update 209; APK 1.0.143 / versionCode 142; package `com.personal.diaryapp`. Live feed blob `fd4ef7874d7eb0691a14acf84d7752c0d05102e0`; pre-change source/mirror blob `99c79234470753bf6284adfc56daa267902460cb`; live feed web SHA-256 `df66a9c292933007a658456c77580073075903e48ca6912c367422128ebfa196`.
- Scope: web-only source change to `web-source/index.html`. Added 54 preset colour swatches to the existing two text-formatting toolbars. The native/custom colour input remains available. Each toolbar still updates its own Cover or Details formatting state. The B/I/U-only selectors in new-note reset and note-load logic were narrowed to the emphasis group so palette buttons cannot be mistaken for formatting toggles.
- No APK/native source, updater/feed, storage keys, saved notes/photos, PIN/recovery, font selectors, or other Diary features were intentionally changed.
- Pre-edit backup branch: `backup/before-text-colour-palette-2026-11-14`. Verified exact readable backups:
  - `backups/web-source-before-text-colour-palette-2026-11-14.html` (blob `99c79234470753bf6284adfc56daa267902460cb`)
  - `backups/diary-web-before-text-colour-palette-2026-11-14.html` (same blob)
  - `backups/latest-before-text-colour-palette-2026-11-14.json` (blob `fd4ef7874d7eb0691a14acf84d7752c0d05102e0`)
  - `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-text-colour-palette-2026-11-14.md` (blob `cf9e11bc5e93a187554e454cb261c937821d774b`)
- Feature branch `feature/text-colour-palette-2026-11-14`; PR #20 merged. Feature commit `e50a404c703eff86532b2b3ebeb4e3f3a330ef3c`; squash merge commit `8eaf8a2e14cf3b96966a02ac2f3a3d5c69f697b9`. Reviewed diff: only `web-source/index.html`, 11 additions and 4 deletions.
- Static source checks confirmed the palette builder, preserved custom colour input handler, independent toolbar instances, and scoped B/I/U selectors. No physical-device test was performed.
- **Release published and repository-verified:** a no-content-change commit (`9099cb60e26d5f5305c499b55b8ec557c13d9505`) triggered the configured `publish-diary-web-update.yml` push workflow. `latest.json` now reports Web Update 210 and web SHA-256 `47ca737272f0c35276c43af1870f771ceb68e2caf61cd703f8ea066a89c1bc6f`. The current `web-source/index.html` and `diary-web/index.html` are both blob `22698acb7a4126bcdc6e76abc5930878cde95fab` and each is 374,033 characters; the feed SHA was generated by the publisher workflow from the source bytes. The workflow run itself is not exposed by the available connector, so do not claim to have inspected its run log. Repository source/mirror/feed release state is verified. No physical-device test has been performed; ask the user to check the update on the phone.
- APK unchanged: 1.0.143 / versionCode 142 / SHA-256 `4eccf17f61389bbb112a1daf910eb88d11315c19c22efa2d9e71171115688961`; no APK rebuild or signing operation.
- Phone-test status: pending; user has not tested this change on device.


# Colour menu display and swatch correction — published as Web Update 211 (2026-11-14)

- User reported that the preset colours appeared outside the colour button and all swatches looked the same. Corrected both Cover/name and Details/text formatting toolbars.
- The 54 preset colours now stay hidden inside a compact 🎨 menu and open only when its button is tapped. Selecting a swatch closes the menu. Each swatch receives its own exact hex background with inline important priority to prevent shared button/theme CSS from overriding it.
- The existing native custom colour input remains available beside the menu; Cover and Details still keep independent colour state.
- Changed only `web-source/index.html`; no APK/native source, storage, saved notes/photos, PIN/recovery, or unrelated feature changes.
- Backup branch: `backup/before-colour-menu-fix-2026-11-14`; verified copies: `backups/web-source-before-colour-menu-fix-2026-11-14.html`, `backups/diary-web-before-colour-menu-fix-2026-11-14.html`, `backups/latest-before-colour-menu-fix-2026-11-14.json`, and `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-colour-menu-fix-2026-11-14.md`.
- PR #21 merged as `554c9545f9e2fe059edc27f1564ba5dc9bb16de4`. Publisher advanced live feed to Web Update 211. Source and mirror both have blob `40357196a3786dbf267aa207c8adb9a441e04853` and length 375315; `latest.json` reports SHA-256 `cfce48f6e2f57fee50f5242b310b00f33d0328ee2ddfbd4bba836506f7d19921`.
- APK remains `1.0.143` / versionCode `142`; no APK rebuild. Physical-device test is pending; user must check both menus on phone before claiming UI success.


# Remove preset colour palettes — published as Web Update 212 (2026-11-14)

- User asked to remove the preset colour feature and leave the existing colour control. Removed the 54 preset swatches and 🎨 popup from both Cover/name and Details/text formatting toolbars.
- Kept the original native custom colour picker, its input handler, and independent Cover/Details formatting state. Existing font size, font family and B/I/U controls remain in place. No note/photo data, PIN/recovery, native Android source, APK, package identity, or other Diary features were changed.
- Starting live state: Web Update 211; APK 1.0.143 / versionCode 142; package com.personal.diaryapp; source/mirror blob SHA 40357196a3786dbf267aa207c8adb9a441e04853; starting feed SHA-256 cfce48f6e2f57fee50f5242b310b00f33d0328ee2ddfbd4bba836506f7d19921.
- Backup branch: `backup/before-remove-preset-colours-2026-11-14`; verified backup files: `backups/web-source-before-remove-preset-colours-2026-11-14.html`, `backups/diary-web-before-remove-preset-colours-2026-11-14.html`, `backups/latest-before-remove-preset-colours-2026-11-14.json`, and `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-remove-preset-colours-2026-11-14.md`.
- Changed only `web-source/index.html` in the feature change. PR #22 merged as `af1b1535d21513bcda63e69115b574d5951bfa7b`. Reviewed PR diff: one file, 4 additions and 13 deletions; removed palette CSS, 54-colour array, swatch creation and palette sync logic; restored the native custom colour input directly in both toolbar instances.
- Publisher workflow run `43626298833` completed with conclusion **success**. Publisher commit: `03b7be9`. Workflow independently computed SHA-256 `34fe487da10d5103c1aeea8dbe0e0a8eb73621d99fd59019d134ac21768baae3` and advanced live feed to Web Update 212.
- Post-publish verification: source and mirror are byte-identical; both live Git blob SHA `113e4cf0cdeb145ff03949890f09996de0586d34`. Live `latest.json` webVersion is 212 and webSha256 matches the publisher-computed value `34fe487da10d5103c1aeea8dbe0e0a8eb73621d99fd59019d134ac21768baae3`. Targeted checks confirm no preset-palette code remains and the native custom colour input handler remains.
- APK unchanged: 1.0.143 / versionCode 142; SHA-256 4eccf17f61389bbb112a1daf910eb88d11315c19c22efa2d9e71171115688961; no APK rebuild or signing operation.
- Physical-device verification pending. Use **Me → Check for Updates**; confirm both formatting toolbars show the original custom colour picker and no 🎨 preset palette. Do not claim phone-side success until user confirms.
- Rollback: use the verified pre-change backup files on `backup/before-remove-preset-colours-2026-11-14`; preserve all local notes, photos and PIN data.


# Custom Colour button visibility fix — Web Update 214 (2026-11-15)

- User clarified: keep the existing colour controls and existing button in the Cover/Naam and Detail/Likhne text menus; do not add a separate button. The word “Custom” was not appearing as the complete **Custom Colour** button on the phone.
- Starting live state: Web Update 213; APK 1.0.143 / versionCode 142; package `com.personal.diaryapp`; main commit `07447acac8ba051d02e65d1e181cf6263d129b30`; source/mirror blob SHA `34b1a0276f83a082949052fd0fba4b0d6169075d`; feed SHA-256 `ecaff11b09037db2330241b87873d932ec956a4cdff30d559b900a7803c90885`.
- Scope: web-only, one CSS addition in `web-source/index.html`. Keep the existing `diary-image-choice-solid` button and its colour-picker click handler. Give the existing action a full-width row and sufficient height/padding so the full **🎨 Custom Colour** label is visible in both Cover and Detail menus. No new button, no separate card, no change to colour values, picker logic, gradients, Photo menu, note data, storage, PIN/recovery, updater, native Android source, APK, package identity or signing.
- Pre-edit backup branch: `backup/before-custom-colour-button-label-2026-11-15` (prior baseline) and this task's branch backup files: `backups/web-source-before-custom-colour-button-width-2026-11-15.html`, `backups/latest-before-custom-colour-button-width-2026-11-15.json`, `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-custom-colour-button-width-2026-11-15.md`.
- Work branch: `fix/custom-colour-button-width-2026-11-15`; dedicated backup branch: `backup/custom-colour-button-width-2026-11-15`. The three pre-edit backup files were re-fetched successfully and are readable.
- PR #24 merged successfully by squash as commit `d2177f45da040cf4ef41cb23c8c4613a7ad9d6e1`. The PR diff contains exactly two files: `web-source/index.html` (7 additions, 1 deletion) and this register (9 additions); backup files are not part of the feature diff.
- Publisher workflow run `43629161362` completed with **success**; publish job and every listed step completed successfully. Live Web Update advanced from 213 to **214**. Live source and published mirror were re-fetched and are byte-identical; both Git blob SHA `0e12683dc6e027a310e73a49100517fabbafaf93`. Live feed `latest.json.webSha256` is `3aece64a96b3e288a247ca5c09353fc6321a5474238c2c0568094b392fead0c4`; publisher workflow completed successfully and wrote this value to the live feed.
- APK unchanged: `1.0.143` / versionCode `142`; package `com.personal.diaryapp`; APK SHA-256 `4eccf17f61389bbb112a1daf910eb88d11315c19c22efa2d9e71171115688961`. No APK rebuild or signing operation.
- Source checks: existing shared chooser call sites still attach the same colour chooser to both Cover and Detail; existing `diary-image-choice-solid` button and its colour-picker event handler remain; Photo's separate label logic remains unchanged. Only a CSS layout rule was added to give the existing Custom Colour button a full-width row and adequate dimensions. No additional button or separate panel was added.
- Physical-device verification is **pending**. Use **Me → Check for Updates**, then open a new note and check Cover/Naam and Detail/Likhne menus: each should show one full-width **🎨 Custom Colour** button; tap it to confirm the existing colour picker opens. Also confirm Photo remains unchanged. Do not claim phone-side success until user confirms.
- Rollback: use the readable pre-edit files on `backup/custom-colour-button-width-2026-11-15`; previous Web Update 213 backup branch remains preserved too.


# Custom Colour button layout repair — published as Web Update 216 (2026-11-15)

- User reported that many Diary functions appeared missing after the Custom Colour button change and asked to restore all previously working work and publish through **Me → Check for Updates**.
- Investigation: live Web Update 215 source blob `34b1a0276f83a082949052fd0fba4b0d6169075d` was the same verified source as Web Update 213. The Web Update 214 patch inserted a raw CSS/style block inside the single-quoted `reportWindow.document.write(...)` JavaScript string in `exportMeFeatureReport`, breaking the script. Web Update 215 restored the pre-214 source; the previously completed feature changes recorded for Web Updates 205–213 were retained in that baseline.
- Scope: web-only, `web-source/index.html`. The existing image-choice action wrapper receives a layout class only for Cover and Detail (not Photo); the existing Custom Colour button is made full-width by CSS placed inside the document-head chooser style block. Existing picker button, click handler, colours, gradient controls, Photo label, notes/photos, storage, PIN/recovery, updater, native Android source, APK and signing data remain unchanged.
- Pre-edit backup branch: `backup/before-custom-colour-repair-2026-11-15`. Verified exact readable backups: `backups/web-source-before-custom-colour-repair-2026-11-15.html` (blob `34b1a0276f83a082949052fd0fba4b0d6169075d`); `backups/latest-before-custom-colour-repair-2026-11-15.json` (blob `adac67106d3e89064f3bd71a3b206032f48af0e0`); `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-custom-colour-repair-2026-11-15.md` (blob `957ef66d6bb96d3364afefc80c697b6cc4633346`). All three were fetched back and content-compared byte-for-byte.
- Feature branch `fix/custom-colour-button-layout-2026-11-15`; source commit `cc76902f166858a2aaf9943351c5849285c4e443`; PR #26 merged as `9824122cd745c1e078d865d17937442352e733f4`. The source diff was limited to one existing wrapper class and one CSS rule in the correct head style block; the Master Register was also updated.
- Both inline JavaScript blocks parsed successfully before merge. Post-publish checks: live source and `diary-web/index.html` mirror are byte-identical, both blob SHA `102531d7e44feccfb9283cba87ca835ac1e9a663`; the independently computed UTF-8 SHA-256 `cf54d5f058ca3175ba1a2eec6265f852b3c70fe09e959e26ddd3a04b1b94fff5` matches live `latest.json.webSha256`; live `webVersion=216`. Publisher bot commit `a9800c9923d0d86a0970255394193b19b3cfc209` updated the mirror and feed after the merge. The workflow run ID/status endpoint was not exposed in this session; publication is confirmed by the publisher commit and matching live source/mirror/feed/hash.
- Targeted live-source checks confirm the CSS is in the document head, the malformed report-string injection is absent, the existing picker click handler remains, the Cover/Detail wrapper receives the full-width class, the Photo label remains **Solid Colour**, and the main-page marker remains present.
- APK remains `1.0.143` / versionCode `142`; SHA-256 `4eccf17f61389bbb112a1daf910eb88d11315c19c22efa2d9e71171115688961`. No APK rebuild or signing operation.
- Physical-device verification is pending. User should open **My Diary → Me → Check for Updates**, install Web Update 216, and confirm the main page and previously working sections/options appear; then check Cover/Detail Custom Colour is full-width and Photo is unchanged. Do not claim phone-side success until the user confirms.
- Rollback: preserve `backup/before-custom-colour-repair-2026-11-15` and the earlier Web 213 backup branch; if needed restore only the affected web source and publish a higher webVersion. Never clear local notes, photos, PIN or recovery data.

# Long-press note action menu — published as Web Update 221 (2026-11-15)

- User requested a long-press on a note to show **Delete, Copy, Pin, Edit, Share**; user confirmed long-press and approved retaining the existing multi-note selection feature.
- Implemented in `web-source/index.html` only. A 550 ms long-press now opens a centered action menu. For unlocked notes it offers Delete, Copy, Pin/Unpin, Edit and Share. A separate **Select** action preserves the existing multi-note selection/delete workflow. Locked notes keep their existing PIN protection; protected actions are not exposed until the note is unlocked. Tapping outside or Cancel closes the menu. Normal tap-to-open behavior remains unchanged.
- Pre-edit backup branch: `backup/before-note-long-press-action-menu-2026-11-15`. Exact source backup blob `d53c8f4ebbab33ebd73db732824ef928b9845ffb` matches the pre-edit main source byte-for-byte. Separate backup copies of `diary-web/index.html`, `latest.json` and this register are preserved on that branch.
- Feature branch: `feature/note-long-press-action-menu-2026-11-15`. PR #31 merged as commit `b04020a41a925b1505acec10a7ae681aa26c160e`. Diff limited to `web-source/index.html` (42 additions, 1 deletion).
- Static verification: both inline JavaScript blocks compile successfully; targeted source checks confirm the long-press calls the action menu, the old direct long-press selection call is removed, all five requested actions are present, and the separate Select action still calls the existing multi-select handler. Main tap/click handling remains in place. This is source-level verification, not physical-phone testing.
- GitHub Actions publisher run `43680473137` completed with **success**. Published Web Update 221. Live `web-source/index.html` and `diary-web/index.html` are byte-identical, blob SHA `85028f9d6e514faf3c175105f141d3ce51f9d3a0`. Live `latest.json` reports `webVersion=221` and SHA-256 `b728d3e027bd4952fdcd402b991a0b9c2b09d78f1a6824d8df4ccffffc00dc70`, matching the publisher workflow's generated feed.
- APK remains `1.0.143` / versionCode `142` with SHA-256 `4eccf17f61389bbb112a1daf910eb88d11315c19c22efa2d9e71171115688961`. No APK rebuild, signing, native Android, PIN storage, note storage, or photo storage changes.
- Physical-device verification is pending. User should open **My Diary → Me → Check for Updates**, install Web Update 221, then long-press an unlocked note and test Delete, Copy, Pin/Unpin, Edit, Share and Select. Also test a locked note to confirm PIN protection. Do not claim phone-side success until user confirms.
- Rollback: use the preserved pre-edit source and metadata on `backup/before-note-long-press-action-menu-2026-11-15`; if rollback is needed after publication, restore the source and publish a higher webVersion. Never clear local notes, photos, PIN or recovery data.


# Android note long-press context-menu trigger repair — pending publication (2026-11-15)

- User reported that long-press did nothing after Web Update 221; the separate Select action and requested note action menu were therefore unreachable on their phone.
- Investigation compared the live Web Update 221 source with the exact pre-menu backup. The original long-press used a 550 ms timer to call `toggleNoteSelection(n.id)`. Web Update 221 replaced that direct selection with `showNoteActionMenu(n)`, and placed the Android `contextmenu` handler behind `if(holdTriggered)`. If Android Chrome dispatches its native long-press contextmenu before the timer has fired/cancels the pointer sequence, the handler only prevents the browser menu and never opens the Diary menu. This matches the user's report.
- Minimal repair: the note card's `contextmenu` handler now always prevents the native browser menu and, if the Diary menu has not already opened, directly opens `showNoteActionMenu(n)`. The existing 550 ms pointer timer remains as the first trigger; the contextmenu event is a fallback for Android long-press. Existing menu actions (Delete, Copy, Pin/Unpin, Edit, Share, Select) and `toggleNoteSelection` implementation remain unchanged. Tap-to-open, selection mode, note data, photos, PIN/recovery, storage, native Android and APK remain unchanged.
- Pre-edit backup branch: `backup/before-note-longpress-contextmenu-fix-2026-11-15`; exact live source, latest feed and this register were copied to backup files before editing.
- Feature branch: `fix/note-longpress-contextmenu-2026-11-15`. Source change is isolated to the note-card `contextmenu` handler. Physical Android verification is still required after publication; do not mark the feature phone-tested until user confirms both long-press menu and multi-select.


# WhatsApp-style inline text menu for long-pressed notes — pending publication (2026-11-15)

- User clarified that the actions must appear beside the exact note being long-pressed, like WhatsApp, as plain text options—not as buttons and not in a centered full-screen modal.
- Starting live state: Web Update 222; APK 1.0.143 / versionCode 142; package com.personal.diaryapp; source and mirror blob SHA 50c3eab4568509fed33d83cbbcfb8b3edd5880c6; live latest.json webSha256 52951c244f492fcb5ddf3eea26d87243d2e3b0cbb045a115b41fbbfb252a5a49.
- Scope: web-only change to the existing note long-press action menu and the note-card pointer/contextmenu event arguments in web-source/index.html. Replaced the centered dimmed overlay and stacked button controls with a compact floating text-only menu positioned near the long-press coordinates on the same note. Text actions are separated by small dots; tapping outside dismisses it; its position is clamped to the visible screen.
- Preserved actions: Delete, Copy, Pin/Unpin, Edit, Share, and Select. Select still calls the existing toggleNoteSelection handler, so multi-select remains available. Locked notes continue to hide protected actions until unlocked and retain the existing PIN prompt.
- Explicitly untouched: note/photo storage and formats, note content, PIN/recovery, delete/trash logic, share/copy/edit/pin handlers, normal tap-to-open, updater, Android source, APK, package identity and signing.
- Pre-edit backup branch: backup/before-note-longpress-inline-actions-2026-11-15. Exact live copies re-fetched and verified byte-identical:
  - backups/web-source-before-note-longpress-inline-actions-2026-11-15.html (blob 50c3eab4568509fed33d83cbbcfb8b3edd5880c6)
  - backups/diary-web-before-note-longpress-inline-actions-2026-11-15.html (same blob)
  - backups/latest-before-note-longpress-inline-actions-2026-11-15.json
  - backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-note-longpress-inline-actions-2026-11-15.md
- Feature branch: feature/note-longpress-inline-actions-2026-11-15. PR #33 merged successfully as `eb7ab77ecf7b6e85184f8db1f7ccac5f3649865a`. The publisher then created commit `fdef56fb06a7d3fae5ee3f035ae715542d9c643c` and published Web Update 223. Both inline JavaScript blocks in the final live source parse successfully; targeted checks confirm a floating position anchored to the press coordinates, text spans rather than button elements, no dimmed overlay, all requested actions, outside-dismiss handling, viewport clamping, and retained Select wiring.
- Post-publication verification: live `web-source/index.html` and `diary-web/index.html` are byte-identical at blob SHA `8c2b9cd28288f999ad4e0fd9b11a07392889625e`. Live `latest.json` blob `af824ce5a4810bb76ecb004f275244f4e5624970` reports `webVersion=223` and `webSha256=4c3a0875e96df08a9bddeef0064ef7bb87830a847cf61df45d06e977e0c5af32`, matching the publisher-generated feed for this source. Publisher run log/ID was not separately available in this check; publication is confirmed by the publisher commit and live feed/mirror.
- APK remains 1.0.143 / versionCode 142 with SHA-256 `4eccf17f61389bbb112a1daf910eb88d11315c19c22efa2d9e71171115688961`; no APK rebuild or signing change.
- Physical Android verification is pending. After publication, use My Diary → Me → Check for Updates, install Web Update 223, then test long-press on an unlocked note, all six text actions, normal tap-to-open, multi-select, and a locked note. Do not claim phone-side success until the user confirms.
- Rollback: restore the exact pre-edit source and register/feed copies from backup/before-note-longpress-inline-actions-2026-11-15; if already published, restore source and publish a higher webVersion. Preserve all local notes, photos and PIN/recovery data.


# Correct note action-menu placement inside the pressed note card — published Web Update 224 (2026-11-15)

- User reported that the previous floating text menu appeared outside the Diary, directly below the language selector, rather than beside the note.
- Live starting point was Web Update 223, APK 1.0.143 / versionCode 142. Before this correction, live source and mirror were byte-identical (blob SHA 8c2b9cd28288f999ad4e0fd9b11a07392889625e); live feed reported webVersion 223 and webSha256 4c3a0875e96df08a9bddeef0064ef7bb87830a847cf61df45d06e977e0c5af32.
- Root cause addressed: menu placement trusted touch-event client coordinates. On the affected Android runtime these coordinates evidently did not represent the note location, so the menu could be placed near the page origin/language selector. The menu no longer uses touch coordinates.
- Web-only correction: append the text menu as an absolutely positioned child of the exact note card being long-pressed; use that card's live getBoundingClientRect() for placement. Temporarily set only that card's position/z-index and restore both original inline values when the menu closes. This keeps the menu physically within the Diary note card, near its note, instead of appending it to document.body.
- Preserved: Delete, Copy, Pin/Unpin, Edit, Share, Select; existing toggleNoteSelection; locked-note PIN restrictions; outside-tap dismissal; normal tap-to-open; all note/photo data, PIN/recovery, delete/trash and share logic.
- Backup branch: backup/before-note-menu-card-anchor-fix-2026-11-15. Four live files (web source, mirror, latest feed and Master Register) were copied and re-fetched byte-identically before editing.
- Feature branch: fix/note-menu-anchor-to-card-2026-11-15. PR #34 merged as `881ca6fc2e5ce562cf1006007ccfb0928c173b6b`.
- Publisher workflow run 43682053362 completed successfully. Publish job steps all succeeded, including "Verify and publish HTML bundle without rebuilding APK".
- Published state: `latest.json` blob `32a26a6c8c91af6341192fc02fb6bcab7033b615` reports `webVersion=224` and `webSha256=36ee6089a3a0dde0700386efa8a083e9f28d3998b8e10566caa4eb18a144bdda`. Live `web-source/index.html` and `diary-web/index.html` are byte-identical at blob SHA `ab93dac3ceedf270c06c8714c8e31b90295672dc`.
- Static validation: both inline JavaScript blocks parse successfully; menu is an absolute child of the pressed card; placement uses that card's bounding rectangle; no touch-event coordinates or document.body append; no full-screen modal or action buttons; all six actions and multi-select wiring remain.
- APK remains 1.0.143 / versionCode 142 with SHA-256 `4eccf17f61389bbb112a1daf910eb88d11315c19c22efa2d9e71171115688961`. No APK rebuild, native Android, package identity or signing change.
- Physical Android verification remains pending. Do not claim phone-side success until the user confirms that the menu appears beside the correct note and all actions work.
- Rollback: restore source/feed/register from backup/before-note-menu-card-anchor-fix-2026-11-15; if already published, publish a higher webVersion. Preserve all local notes, photos and PIN/recovery data.

# Android lock-screen reminder notification timing repair — published APK 1.0.148 (2026-11-15)

- User confirmed the reminder's ringtone duration and screen/light timing were already correct; only the notification card was appearing on the lock screen after the ringtone stopped. Scope was limited to making the notification card visible immediately while retaining the existing ringtone and timed screen-wake behavior.
- Starting Android release baseline: 1.0.147 / versionCode 146. Pre-edit source, workflow and register were backed up on branch `backup/before-lockscreen-notification-timing-2026-11-15` in the corresponding `backups/*before-lockscreen-notification-timing-2026-11-15*` files.
- Source change in `scripts/add_diary_app_actions.py`: removed the notification's full-screen launch of the transparent wake activity, which had covered the normal notification card during ringtone playback; set notification visibility to `Notification.VISIBILITY_PUBLIC`. Existing timed screen wake lock, ringtone service and configured ringtone timing remain.
- PR #49 merged the behavior change. PR #50 fixed a Kotlin comment syntax issue in the generated source; no additional runtime behavior was changed. Both merged to main; final source commit is `f079fde2e49e157d2e786a749fc449f4c63e8fe4`.
- Build workflow run #204 (`43696398535`) completed successfully. Debug build, signed Release configuration, APK upload and publish steps all succeeded. The release APK signer SHA-256 fingerprint was verified in the build log as `23A4E93F3C7911DCE18389EA583548700C6AD6A3759707F1CD222D07E2408B5A`, matching the previously approved signing certificate.
- Published feed now reports versionName `1.0.148`, versionCode `147`, APK URL `https://raw.githubusercontent.com/amuazzinxyz-ops/My-Diary-Updates/main/My-Diary-1.0.148.apk`, and APK SHA-256 `68b8b7a57adf398010f7cca82b5ce1009705d73a03592269126f82c399470823`. The repository contains the exact `My-Diary-1.0.148.apk` asset (2,021,071 bytes); signed-release artifact was also uploaded by run #204.
- Physical Android lock-screen verification remains pending. Ask the user to install the update and test that the notification card appears at ringtone start while ringtone and light durations remain unchanged. Do not claim device-side testing until user confirms.
- Preserve all local notes, photos, PIN/recovery data, reminder schedules and app identity. Rollback source backup is available on the backup branch; if a correction is required after this release, publish a higher versionCode with the same signing certificate.


# My Documents viewer repair — safe 1.0.159 republish guard correction (2026-11-15)

- Follow-up to the My Documents PDF/photo Open-button repair and the APK filename correction. PR #65 made the generated Android WebView bridge class publicly accessible and added static build guards. PR #66 corrected the published versioned APK filename from the stale 1.0.158 name to `My-Diary-1.0.159.apk`.
- Build run #224 (`43711843005`) stopped safely before compilation/publication. Exact failure: the workflow's pre-build and publisher guards accepted only feed baseline 1.0.158/versionCode 157, but run #223 had already published feed metadata for the exact repair release 1.0.159/versionCode 158. No APK was built or published by run #224; no existing app data or release assets were changed by that failed run.
- Corrective change on `fix/159-feed-guard-republish-2026-11-15`: both guards now accept only either the known installed baseline (1.0.158/157) or the exact already-published repair release (1.0.159/158), while continuing to reject every other version and package mismatch. The build still sets and verifies the target release as 1.0.159/versionCode 158. This permits the exact same release to be rebuilt and republished with the corrected versioned filename without incrementing/downgrading the app version.
- Pre-edit backup branch: `backup/before-159-feed-guard-repair-2026-11-15`, created from main commit `0745c53733d8058c77c488eaf2c04bb6bb387597`.
- Workflow change is not yet merged or rebuilt. Do not distribute the 1.0.159 APK until the new run succeeds, the exact versioned APK exists, and its SHA-256 matches live `latest.json`. Physical Android testing of opening both PDF and photo attachments remains pending; do not claim device-side verification.
- Preserve the existing package/signing identity and all local notes, documents, photos, PIN/recovery data, and reminders. If any subsequent build or hash verification fails, stop and retain the last verified release.


# My Documents PDF/photo Open repair — 1.0.159 build published (2026-11-15)

- Workflow run #225 (`43712054992`) completed successfully on main commit `a84e93656898217f996643c78250a7bac03d6ee6`. Signed Release APK configuration, APK upload, and update-feed publication all succeeded.
- Published release: My Diary `1.0.159`, versionCode `158`, package `com.personal.diaryapp`.
- Exact APK filename: `My-Diary-1.0.159.apk`; published URL: `https://raw.githubusercontent.com/amuazzinxyz-ops/My-Diary-Updates/main/My-Diary-1.0.159.apk`.
- Live `latest.json` SHA-256: `e77ccd4cc73a3b9dd99a93073090dfa7c59c6249a5a3efb5f9d676508a1b23fc`. The feed is updated to webVersion `235`.
- Change scope: Android WebView native bridge visibility for My Documents open action; release notes state photo and paginated PDF viewer launch path hardened. Existing local records/data and app identity are to be preserved.
- Build and feed publication are verified. Physical Android testing is still pending: user must install the update and test opening both a PDF and a photo in My Documents. Do not claim device-side verification until confirmed.
- Prior safety backup branch remains: `backup/before-159-feed-guard-repair-2026-11-15`.


# My Documents PDF/photo open — WebMessageListener repair in progress (2026-11-15)

- User tested the published 1.0.159 APK and confirmed the same My Documents PDF/photo Open-button failure remains. Therefore the earlier public JavaScript-interface visibility change was insufficient; do not describe that repair as successful.
- Backup branch created before this correction: `backup/before-docs-webmessage-bridge-2026-11-15`.
- New feature branch: `fix/docs-webmessage-open-2026-11-15`.
- Corrective approach: route document bytes from the Diary WebView through an origin-restricted AndroidX `WebMessageListener` named `DiaryNativeDocuments`, dispatching to the existing native in-app PDF/photo viewer on a background thread. Retain the existing JavaScript-interface route only as fallback. Keep document records, IndexedDB storage, local notes, photos, PIN data, reminders, package identity, and signing identity unchanged.
- New release target: My Diary `1.0.160`, versionCode `159`; the new release has been built and published as recorded below.
- Build guard must verify the native listener and the HTML message-channel call before APK compilation/publication. Physical device verification remains pending until the user tests the new APK.


## My Documents WebMessageListener repair — APK 1.0.160 published (2026-11-15)

- PR #68 merged as `453ebbf0514781361cf52bcee837ad49b8364b60`; build workflow run #226 (`43713165065`) completed successfully.
- Android release: My Diary `1.0.160`, versionCode `159`, package `com.personal.diaryapp`; exact published APK `My-Diary-1.0.160.apk`.
- Live feed URL: `https://raw.githubusercontent.com/amuazzinxyz-ops/My-Diary-Updates/main/My-Diary-1.0.160.apk`; live `latest.json` SHA-256 `92d95a59d490680f4861b169b4168ea8edf8165a355d4c7855133263d3785cb9`.
- Independently downloaded signed-release workflow artifact, extracted APK size 2,025,563 bytes, and computed SHA-256 `92d95a59d490680f4861b169b4168ea8edf8165a355d4c7855133263d3785cb9`; exact match with live feed.
- APK build, signed release configuration, upload, publication, and all workflow steps succeeded. The HTML Open action now prefers the origin-restricted AndroidX `DiaryNativeDocuments` WebMessageListener channel; the existing JavascriptInterface remains fallback. Native PDF/photo viewer logic and existing file records are preserved.
- Physical device verification is still pending. User must install 1.0.160 and test opening both PDF and photo documents; do not claim that device testing has passed until user confirms.


## My Documents still not opening after 1.0.160 — origin-check correction in progress (2026-11-15)

- User tested `Check for update` on 1.0.160 and confirmed both image and PDF still do not open. The 1.0.160 build/hash publication succeeded, but device functionality is NOT verified and must not be described as fixed.
- New backup branch: `backup/before-161-origin-check-fix-2026-11-15`; repair branch: `fix/161-origin-check-open-docs-2026-11-15`.
- Code inspection found the AndroidX WebMessageListener already has an origin allowlist for `https://appassets.androidplatform.net`, but its callback redundantly compares `sourceOrigin.toString()` to a string. This brittle string comparison can reject the allowed origin representation and silently drop the Open request. Change callback validation to compare `sourceOrigin.scheme` and `sourceOrigin.host` while retaining the allowlist and main-frame check.
- Next target: My Diary `1.0.161`, versionCode `160`; publisher guard advances from live `1.0.160/159` only. No change to IndexedDB documents, file contents, PIN, notes, reminders, package/signing identity, or native PDF/photo rendering.
- Do not publish or claim success until build, signed APK, feed SHA-256, and APK bytes are verified. Physical device test remains required after user installs it.


## My Documents origin-check correction — APK 1.0.161 published and verified (2026-11-15)

- PR #69 merged as `fd73221dc3890f69dcbff2c573d160a6dc981c95`; build workflow run #227 (`43713843433`) completed successfully.
- Release: My Diary `1.0.161`, versionCode `160`, package `com.personal.diaryapp`; APK filename `My-Diary-1.0.161.apk`.
- Published APK URL: `https://raw.githubusercontent.com/amuazzinxyz-ops/My-Diary-Updates/main/My-Diary-1.0.161.apk`.
- Live feed SHA-256: `cf3e760f77f3b7bbb5df2bdf5ac3f1a12cc2d99522dea42258ac21485ed90d1c`. Independently extracted signed-release APK artifact size 2,025,736 bytes and computed SHA-256 exactly matches the feed. Main branch Git tree confirms the exact APK path and size.
- Correction: WebMessageListener callback validates HTTPS scheme and `appassets.androidplatform.net` host rather than brittle exact `sourceOrigin.toString()` comparison. The WebMessageListener origin allowlist and main-frame check remain in place.
- Build, signed APK, feed publication, APK artifact SHA-256, and main branch APK path are verified. Physical device test is still pending: user must install 1.0.161 and test both an image and PDF in My Documents. Do not claim device-side success until user confirms.
- Backup branch: `backup/before-161-origin-check-fix-2026-11-15`.


## User-confirmed My Documents and update-route verification — APK 1.0.161 (2026-11-15)

- After installing/testing the published My Diary APK 1.0.161, the user confirmed that the update process is working and replied “Ha Hogaya” to the combined check covering both direct APK update and the in-app **Check for Updates** route, plus opening both photo and PDF files in **Me → My Documents**. Record this as user-reported device verification; no independent remote access to the user's phone was performed.
- Release remains APK 1.0.161 / versionCode 160, package `com.personal.diaryapp`. Live `latest.json` advertises APK URL `https://raw.githubusercontent.com/amuazzinxyz-ops/My-Diary-Updates/main/My-Diary-1.0.161.apk` and SHA-256 `cf3e760f77f3b7bbb5df2bdf5ac3f1a12cc2d99522dea42258ac21485ed90d1c`; webVersion 236 remains unchanged.
- User confirmation closes the previously pending phone-test item for the APK update routes and My Documents photo/PDF opening. Preserve existing local Diary data, documents, notes, PIN/recovery, reminders, app identity and signing identity. No app source, APK, or update-feed version was changed for this register-only entry.
- Register pre-edit backup branch: `backup/before-device-confirmation-register-2026-11-15`; exact previous register snapshot: `backups/PROJECT_MAP_AND_SECRETS_REGISTER-before-device-confirmation-2026-11-15.md`.


## My Memories multi-word search and image download — implementation branch (2026-11-15)

- User requested search by the saved image name and a way to download an already-saved image to the mobile device again.
- Feature branch: `feat/memories-search-download-2026-11-15`; pre-edit backup branch: `backup/before-memories-search-download-2026-11-15`.
- Both `web-source/index.html` and `diary-web/index.html` were updated identically. My Memories search now treats a multi-word query as matching when every typed word occurs in the saved record's searchable text (including its saved title and filename); this supports partial names and 2–4 words without requiring the full exact title. Other sections retain their existing search behavior.
- Each saved image now retains its existing Open link and also shows a Download link using the original saved filename, with a title-based `.jpg` fallback when no filename exists. No records, blobs, names, or local storage keys are rewritten.
- This is a source implementation branch only. Build/publish workflow, live `latest.json`, APK/web version and Master Register main branch have not yet been updated. Android WebView/mobile download behavior still requires a published build and user device verification; do not claim it is already working on the phone.
- Backup branch contains pre-edit snapshots of the web source, mirror, `latest.json`, and this register.


## My Memories search and download — published web update (2026-11-15)

- PR #70 merged to `main` as commit `d1c4b811001a03ef3354b7947e54597c819abb95`.
- My Memories supports partial/multi-word search: all words typed in the search field must occur in the saved record's searchable text, including the saved title and filename. Other sections keep their prior search behavior.
- Saved image cards retain Open and now include Download using the original filename (title-based `.jpg` fallback only when filename is absent). Saved records and blobs are not migrated or deleted.
- Web update feed is version 237. Its SHA-256 is calculated from the UTF-8 bytes of `web-source/index.html`; source and published mirror are identical. APK remains 1.0.161 / versionCode 160; this is a web-only update, so no APK rebuild was made.
- Android device verification is still pending. Test partial 2–4 word search and saving the downloaded image to the phone's Downloads/Gallery before marking device behavior verified.
- Pre-edit snapshots remain on `backup/before-memories-search-download-2026-11-15`.


## Check for Update repair — phone-tested Diary 1.0.167 published (2026-11-15)

- User explicitly confirmed PASS after installing and testing the signed 1.0.167 / versionCode 166 candidate.
- Approved release workflow run #233 (43742278440) completed successfully; signing certificate fingerprint was checked against the established certificate.
- Published APK: My-Diary-1.0.167.apk and compatibility alias My-Diary.apk; both are 2,027,847 bytes in the main branch. APK SHA-256: ef3655fbbb9f7fb239c2eae57ad303e7d7ac6f44c485493f6a43a03a4ee5c6e4.
- Live APK URL: https://raw.githubusercontent.com/amuazzinxyz-ops/My-Diary-Updates/main/My-Diary-1.0.167.apk.
- Live latest.json advertises package com.personal.diaryapp, versionName 1.0.167, versionCode 166, and the matching APK SHA-256 above. The published signed APK was independently extracted from workflow artifact #14173505335 and its SHA-256 matched latest.json exactly.
- Web Update remains version 238 at web-source/index.html, with SHA-256 00188bc0b173156df29fe1750ce5c71321db27742d14faa16f81465c7092ee5e. The 1.0.167 build embeds the currently published Web Update 238; existing saved Diary data, notes, documents, PIN data, reminders, package identity and signing identity are preserved.
- Main publication commit: 2745096077fa32c5b44a23185961917c1a38ca4e. Workflow configuration commit: b8536a077a96c1cd3f571b4b9299800c96e9b7a2.
- User's PASS is recorded as user-reported device verification. No remote access to the user's phone was performed. For future update checks, installed versions below 1.0.167 can receive the APK; version 1.0.167 receives any newer web bundle through the web-update path.



## My Documents multi-word search — Web Update 239 and APK 1.0.168 published (2026-11-15)

- User requested a My Memories-style Search Bar in **Me → My Documents**, with the same design/working and matching by 2–3 words or the full document name. User explicitly requested delivery through both direct APK installation and the in-app **Check for Update** route.
- Implementation: PR #77 merged as commit `0ef00d7146eaf89e0c21191c31fdb3e6e5e68e0c`. My Documents now displays a full-width, sticky search field styled like My Memories. Search is case-insensitive and matches when every typed word occurs in the searchable document record; title matches rank first, then filename matches. Other sections retain their existing filtering behavior. No document records, file blobs, storage keys, PIN data, or existing document-open handlers were rewritten.
- Pre-edit source backup: `backup/before-my-documents-search-2026-11-15`. APK workflow filename/republish guard correction: PR #78 merged as commit `976ae1ec072b68a88e7b0bde8cbcfbb875f7e078`. Register pre-edit backup branch: `backup/before-my-documents-search-release-register-2026-11-15`.
- Web Update 239 is live. `web-source/index.html` and `diary-web/index.html` are byte-identical at blob SHA `c0252604876d5a46d7c192395faf3f490ab58300`; both contain the My Documents search heading and multi-word match/ranking logic. UTF-8 SHA-256: `ee3512a5587cae3c29b028490d31c060926c567abd81a5b7f9b6229d99941575`.
- Signed APK 1.0.168 / versionCode 167, package `com.personal.diaryapp`, was built successfully in workflow run `43744888123`. The versioned APK `My-Diary-1.0.168.apk` and compatibility alias `My-Diary.apk` have the same Git blob SHA `2ca2621f42b7560611e4b70d16be4ae6d414095c`. Signed APK size: 2,028,081 bytes. SHA-256 independently calculated from the downloaded signed workflow artifact APK: `3946aa3c4235a72731f1fe80ff62334752b51c4da2f0452093588b9c87c22134`; this matches live `latest.json`.
- Live `latest.json` advertises versionName `1.0.168`, versionCode `167`, APK URL `https://raw.githubusercontent.com/amuazzinxyz-ops/My-Diary-Updates/main/My-Diary-1.0.168.apk`, matching APK SHA-256 above, and webVersion `239` with matching web SHA-256. Thus direct APK and in-app Check for Update both point to the same published release metadata.
- Device test is **not yet confirmed** for this release. Do not mark phone-side installation, My Documents search behavior, or in-app Check for Update as user-tested until the user tests on their phone and reports PASS. The successful CI build, signed artifact, live feed, URLs and hashes are repository/workflow verification only.
- Preserve all existing local Diary documents and files, notes, saved images, PIN/recovery, reminders, app/package identity and signing identity. No MUAZZIN project files were touched.



## My Documents search bar moved above the add-document form — Web Update 240 (2026-11-15)

- User reported that the My Documents search bar was not at the top like My Memories. Root cause: `showMeFeaturePage()` inserted the search tools before the form only for `kind==='memories'`; documents used the opposite order.
- PR #79 merged to main as commit `c632c262cf7373450846412cea5b5048f26e2a16`. The single ordering condition now treats both `memories` and `documents` the same: search bar first, add form below. No search matching logic, records, file blobs, document-open handlers, PIN, or other feature code was changed.
- Pre-edit backup branch: `backup/before-documents-search-top-order-2026-11-15`.
- Web Update 240 successfully published by workflow run `43745605152`. Source and mirror are identical at blob SHA `b329d9d9f3f35112366662b87ed477639b9474fe`; web SHA-256 `4086d69ff0ad56c2e9467a55cfeb736fea4395660588a3d01375a8672105ee53`. Live `latest.json` advertises webVersion 240 and the matching SHA-256.
- APK workflow run `43745605125` was triggered automatically and was still in progress at the time of this register update. The web bundle is already published for the installed app's Check for Update route; do not claim the APK rebuild has completed unless separately verified.
- Phone-side display/scroll verification is pending. User should open My Documents after Check for Update and confirm the search bar is immediately below the feature heading and above the add-document form. No remote phone test was performed.


## My Documents image preview — Web Update 241 (2026-11-15)

- User requested that image files in **Me → My Documents** visibly preview like images in **My Memories**, instead of showing only the PDF/document Open button.
- PR #80 merged to main as commit `036af5c9d02187161749230889e5085b1b205fd5` (squash publication commit). Pre-edit backup branch: `backup/before-documents-image-preview-2026-11-15`; exact HTML snapshot: `backups/web-source-index-before-documents-image-preview-2026-11-15.html`.
- My Documents now creates a thumbnail for saved image MIME types using the existing Blob URL lifecycle and the same `.diary-me-feature-thumb` styling used by My Memories. Tapping the thumbnail invokes the existing Open button handler, preserving the native full-image viewer path. PDFs and other non-image files retain the existing Open button with no image thumbnail.
- No IndexedDB records, Blob contents, filenames, search logic, document-open bridge, PIN/recovery, notes, reminders, package identity, or signing identity were changed. Source and mirror are identical at blob SHA `381ce902a26d74438ceab1debf2d7b7fc39272fe`.
- Web Update 241 is published in `latest.json`, with web SHA-256 `69a471825452b9ed4a835d757445032d201bc03f38fc40bc95d075ceb1c80133`. APK remains My Diary 1.0.168 / versionCode 167; this is a web-only update delivered through Check for Update, so no APK rebuild is required.
- Physical Android display/tap test is pending. Do not claim the user's phone has verified the image preview until the user opens My Documents after Check for Update and confirms.


## My Documents image Download button — Web Update 242 (2026-11-15)

- User requested a My Memories-style Download option for image files in **Me → My Documents**, in addition to the existing Open action.
- Created pre-edit backup branch: `backup/before-documents-image-download-2026-11-15`. Feature branch: `fix/documents-image-download-2026-11-15`.
- Implementation adds a Download button only for records already identified as image previews. It reads the existing saved Blob, passes base64 bytes, original filename and MIME type to the existing `DiaryAppActions.saveMemoryImage` native bridge, and displays progress/success/failure beside the button. The existing Open button and thumbnail viewer remain unchanged; PDFs and other non-image documents receive no Download button.
- No IndexedDB records, Blob contents, filenames, search, PIN/recovery, notes, reminders, app/package identity or signing identity are changed. Existing My Memories download flow is not modified.
- Web Update 242 publication and source/mirror/feed hash verification are pending. Device-side download test must remain pending until the user tests it on Android.


## Web Update 242 SHA-256 mismatch — manifest repaired (2026-11-16)

- User reported that tapping **Check for Update** displayed: “Diary update nahi ho saka — SHA-256 match nahi hua.” The updater correctly refused to apply the downloaded bundle; this is a feed checksum mismatch, not evidence of local data corruption.
- Re-fetched the exact main-branch web source and mirror. Both files are byte-identical (Git blob SHA `2e0681b3e7f5fa697fd46b323b7c1e9e5103578a`, 403,670 characters). Independently computed SHA-256 over the UTF-8 source bytes: `c4da44f0ba2545a0cc8ba35e21149a974cd98d1abafdcaca75ef213bae2a6530`.
- Root cause: `latest.json` advertised stale Web Update 242 SHA-256 `74868d9ddd7ccc9fc75403d5ee76f56f87bfc4dda87deb4bcc3e28bf78c2df9d`, which did not match the actual source/mirror bytes. The web bundle itself and both mirrors were not modified.
- Backup branch: `backup/before-web-update-242-sha-repair-2026-11-16`. Repair branch: `fix/web-update-242-sha256-mismatch-2026-11-16`.
- Updated only `latest.json.webSha256` to the independently calculated value above; APK metadata, APK URL/hash, webVersion 242, source/mirror content, app package/signing identity, and local app data remain unchanged.
- PR #82 was merged to main as commit `f1af8b9bc485863acf2581b9998894d5e0ac4995`; live `latest.json` and raw web source were rechecked. The user later confirmed Check for Update successfully delivered Web Update 242. This user report verifies the update flow on their phone.


## My Memories full-size image opening — Web Update 243 (2026-11-16)

- User reports that tapping a saved image in **Me → My Memories** shows only the small thumbnail rather than opening the full image like **My Documents**.
- Created pre-edit backup branch: `backup/before-memories-full-image-open-2026-11-16`. Feature branch: `fix/memories-full-image-open-2026-11-16`.
- Implementation makes the saved My Memories image thumbnail activate the same native document/image viewer bridge used by My Documents (`DiaryNativeDocuments.postMessage` or `DiaryAppActions.openDocument`), passing the already-saved Blob bytes, original filename and MIME type. Keyboard Enter/Space also opens it. If the native viewer bridge is unavailable, it falls back to opening the existing Blob URL in a new tab.
- The existing My Memories Download button and saved image Blob/storage records are not modified. No IndexedDB schema/data, PIN/recovery, notes, documents, reminders, package identity or signing identity are changed. Source and mirror must be identical and `latest.json` must advertise Web Update 243 with its independently computed UTF-8 SHA-256 before publishing.
- Device-side full-image opening test is pending until the user confirms after Check for Update.


## My Memories full-size image open and Check for Update SHA repair — Web Update 244 prepared (2026-11-16)

- Created pre-edit backup branch `backup/before-memories-full-open-and-sha-repair-2026-11-16` from main commit `faae8d8ffdabdeb82a37a038393c566a664b2d5f`. Feature branch: `fix/memories-full-open-sha-244-2026-11-16`.
- The exact source and mirror were byte-identical before editing (Git blob SHA `d34f3895eaf9e2e37b6ee08c4fe262b7a4d1b3ff`). The My Memories image card now creates a thumbnail from its existing saved Blob and opens it through the same native full-image viewer bridge used by My Documents when tapped; Enter/Space keyboard activation is supported. Existing Download button, IndexedDB records/blobs, notes, documents, PIN/recovery, reminders and app identity are untouched.
- Web Update 243 feed checksum was stale: it advertised `d4bf3a1ad626ea5f9081bf5240453412d23af56dc2073a8321e57c5beaec99d9`. New Web Update 244 checksum calculated over the exact UTF-8 bytes is `9f26eb32b40f896fe04715116e8fd3703054f657b81e9853433fa5572e056252` (459522 bytes). APK metadata and signing identity remain unchanged.
- Source/mirror/feed/register changes are prepared on the feature branch. Publish only after exact source/mirror equality, independent SHA-256 re-read, updater guard checks, and successful workflow validation. Android device test remains pending; do not claim full-size opening is phone-verified until user confirms.
- Existing local notes, photos, PIN data and all other app data must be preserved. No MUAZZIN project files are involved.


## My Memories duplicate thumbnail corrected — Web Update 245 (2026-11-16)

- User confirmed Web Update 244 installed, but reported that saving one image showed two image thumbnails in My Memories.
- Root cause verified in the exact source: the original saved-image preview and native full-size open handler were already present in the existing `else` branch. Web Update 244 had added a second thumbnail in a new `if(kind==='memories'...)` block, producing duplicate previews.
- Created pre-edit backup branch `backup/before-memories-duplicate-thumbnail-fix-2026-11-16` from main commit `048c885cb2b7cac8d87a78e7e809f208611ca7f6`. Feature branch: `fix/memories-single-thumbnail-web245-2026-11-16`.
- Web Update 245 removes only the newly-added duplicate thumbnail block. It retains the original single image preview, original full-size native viewer handler, existing file link and Download button. No IndexedDB records/blobs, photos, notes, PIN/recovery, reminders, or APK identity are changed.
- Source and mirror must remain byte-identical; latest.json webVersion and SHA-256 must match exact UTF-8 source bytes before merge/publish. Android verification remains pending until user confirms one thumbnail per saved image.


## My Memories duplicate thumbnail — Web Update 245 phone verification PASS (2026-11-16)

- User has now tested Web Update 245 on their Android phone and explicitly confirmed the duplicate-thumbnail issue is fixed: one saved image displays only once. Record this as user-reported device verification; no independent remote access to the phone was performed.
- The phone test closes the pending Web Update 245 item. The single original My Memories thumbnail remains, tapping it opens the full-size image, and the existing Download action is retained as implemented. This confirmation specifically verifies the duplicate-image display fix; it does not claim unrelated features were tested.
- No app source, mirror, latest.json, APK, or update version was changed for this register-only entry. Existing saved photos, notes, documents, PIN/recovery data, reminders, package identity and signing identity remain untouched.
- Register pre-edit backup branch: `backup/before-memories-web245-phone-pass-register-2026-11-16`.


## Permanent release rule — every Diary feature change ships as APK + Check for Update (2026-11-16)

**This is a standing, mandatory rule for all future My Diary app feature work, improvements, bug fixes, UI changes, and code corrections. It overrides older entries that describe a web-only release or say that no APK rebuild is needed.**

1. **Always provide both delivery routes for every app change:** (a) build and publish a new installable APK and give the user its direct download link; and (b) publish the matching update metadata so the installed app can receive the same change through its in-app **Check for Update** flow. Neither route is optional.
2. For HTML/WebView-only changes too, include the changed web bundle in a newly built APK, publish that APK with a higher valid versionCode/versionName, and publish the matching web bundle/version/checksum in `latest.json`. Do not stop at a webVersion-only update.
3. Before release, create a backup and make only the requested minimal change. Preserve existing local notes, photos, documents, IndexedDB records, PIN/recovery data, reminders, package/application ID, and established signing identity.
4. Verify the exact APK artifact, signature/certificate continuity, APK SHA-256, published APK URL/file, and all relevant `latest.json` version and checksum fields. Verify the web source and mirror are byte-identical and the advertised web SHA-256 matches the exact UTF-8 bytes. Confirm the release workflow/build and publication steps succeeded.
5. **Do not call the task complete and do not tell the user to update** unless both the direct APK and the in-app Check for Update route point to the intended release and all available build/publication/hash checks pass. If any check fails, stop, keep the last good release intact, report the exact blocker, and repair before delivery. Never publish a partial or mismatched release.
6. In every completion message, provide the new APK download link and state that **Check for Update** also receives the update. Clearly distinguish repository/build verification from physical-phone testing; only mark phone testing PASS after the user confirms it.
7. This rule applies to every future Diary feature/fix release, regardless of whether the code change is native Android, HTML/JavaScript, or both. Pure documentation/register-only edits with no app-code change do not require a new APK.

**User explicitly requested this rule as a permanent default on 2026-11-16. Apply it automatically; do not ask the user to repeat or approve it for each future app change.**


## Diary Lock wrong-PIN message stays inside PIN box — Web Update 246 + APK 1.0.169/168 (2026-11-16)

- User requested one narrowly scoped correction: when using **Me → 🔓 Diary Lock Band Karein**, entering an incorrect 4-digit Diary PIN should show only the wrong-PIN message, without a browser alert that also exposes the website address.
- Pre-edit backup branch: `backup/before-diary-lock-wrong-pin-inline-message-2026-11-16`. Feature branch: `fix/diary-lock-wrong-pin-inline-message-2026-11-16`.
- In `turnDiaryLockOff()`, replaced only the incorrect-PIN `window.alert()` with an inline red, bold status message inside the existing PIN dialog. The entered PIN is cleared and focus returns to the PIN field. Successful PIN verification and lock removal are unchanged. Storage failure is shown in the same inline status area.
- Existing Diary PIN value, lock flow, recovery behavior, notes, photos, documents, IndexedDB data, reminders, package identity and signing identity are not changed.
- Web Update 246 is advertised in `latest.json`; source and `diary-web/index.html` mirror are updated from the same HTML. The build workflow is advanced to APK 1.0.169 / versionCode 168, with baseline 1.0.168 / code 167, and will embed the exact published web source in the APK and update the feed checksum.
- Release verification is pending: confirm source/mirror byte equality, computed UTF-8 web SHA-256, successful signed APK build, signing certificate continuity, APK SHA-256, published APK URL and live latest.json. Do not mark complete or tell the user to update until both APK and Check for Update routes are verified. Physical phone testing remains pending until the user confirms.


### Release verification — Diary Lock incorrect-PIN feedback (2026-11-16)

- PR #86 merged to main as `8481ac1ecd45beaf75e0aeed54bcd56c94a362f7`.
- APK build workflow run #242 (`43751849578`) completed successfully. Debug build and signed Release build passed; the workflow verified the existing signing certificate fingerprint `23A4E93F3C7911DCE18389EA583548700C6AD6A3759707F1CD222D07E2408B5A` and published APK 1.0.169 / versionCode 168.
- Published APK URL: `https://raw.githubusercontent.com/amuazzinxyz-ops/My-Diary-Updates/main/My-Diary-1.0.169.apk`. Live feed SHA-256: `fee954b5f2da273677a9f2b8408adbe5182de76bac1dbaa107f1b48742664429`. Independently downloaded signed workflow artifact `app-release.apk` is 2,028,633 bytes and computes to the same SHA-256. Its Git blob SHA `c39d631695599f594c000dd4e6e7472ea6781cc1` matches the published APK path and size in the main branch tree.
- Live `latest.json` advertises package `com.personal.diaryapp`, versionName `1.0.169`, versionCode `168`, the exact APK URL/hash above, Web Update 246, and web SHA-256 `a660266c972f0b791ec45c337417b2534a77f1a76f7d45dfd2772a4a092a332a`.
- Source and mirror are byte-identical at Git blob SHA `27009945f9d6bc11884ea45a145954bdf59cc5e6`. Web publisher run #247 (`43752168920`) independently computed the UTF-8 SHA-256 above and repaired the stale manifest checksum without incrementing Web Update 246.
- Direct APK and in-app Check for Update now point to the same intended release. Repository/build/publication verification is PASS. Physical-phone incorrect-PIN display test is still pending user confirmation; do not claim phone-side PASS until user tests it.


## Diary Lock not-set message stays inside app — Web Update 247 / APK release pending (2026-11-16)

- User requested that tapping **Me → 🔓 Diary Lock Band Karein** when no Diary PIN has been configured should show only the existing “Diary Lock is not set.” message inside the app, without a browser alert or exposed website address.
- Pre-edit backup branch: `backup/before-diary-lock-not-set-inline-message-2026-11-16`. Feature branch: `fix/diary-lock-not-set-inline-message-2026-11-16`.
- Minimal change in `turnDiaryLockOff()`: replace only the no-lock `window.alert()` with the existing Diary status element `#diaryMyNotesStatus` text. The separate Forgot PIN flow, wrong-PIN inline feedback, PIN storage, lock/recovery logic, notes, photos, documents, IndexedDB data, reminders, app identity and signing identity are not changed.
- Source and `diary-web/index.html` mirror are updated identically. `latest.json` is prepared for Web Update 247. PR merge, automatic checksum publication, signed APK rebuild/publication and exact live feed/artifact verification remain pending; do not tell the user to update until both APK and Check for Update routes are verified.
- Phone-side verification is pending. Do not claim Android device PASS until the user tests the no-lock button and confirms only the message appears without a website address.


### APK + Check for Update release preparation — Diary 1.0.170 / code 169

- The merged HTML-only correction is being delivered under the permanent dual-release rule. The Android build workflow is advanced from 1.0.169/168 to 1.0.170/169, with the current published 1.0.169/168 feed accepted as the baseline and the exact new release as the only re-publication state.
- The workflow embeds the exact main-branch `web-source/index.html`, computes its UTF-8 SHA-256, and publishes the signed APK plus matching `latest.json` APK/web metadata. Build, signature continuity, artifact checksum, published URL, and live feed verification are pending; do not tell the user to update until all pass.


## Diary Lock not-set message release verified — Web Update 247 + APK 1.0.170 (2026-11-16)

- User request: when **Me → 🔓 Diary Lock Band Karein** is tapped while no Diary PIN lock exists, show only the existing “Diary Lock is not set.” message inside the app, without a browser alert or website address.
- Minimal code change in `turnDiaryLockOff()`: the no-lock branch writes `t('diaryNoLock')` to existing `#diaryMyNotesStatus` instead of calling `window.alert()`. Wrong-PIN feedback from Web Update 246 remains inline. Forgot PIN flow and lock setup/clear/recovery logic were not altered.
- Feature branch merged in PR #87; merged main commit `013e2e2c1bded25f36a3d10ecfaae2f38918b900`. Web Update 247 publisher workflow run #248 (`43753132223`) completed successfully.
- Exact source/mirror equality verified: `web-source/index.html` and `diary-web/index.html` both blob `b380b5ad9245210a07765e90022acd96b95f403a`. Live `latest.json` advertises webVersion 247 and UTF-8 SHA-256 `1fb8a2c22bf5e233370f9638601046ac977a747c3bd7a1f585a877be5b686c46`.
- APK build workflow run #244 (`43753353911`) completed successfully. All workflow steps passed, including signing readiness, keystore/alias validation, exact latest HTML embedded in APK, version guard, signed Release build, release verification/publish, and APK upload. Signed APK artifact `My-Diary-1.0.170-signed-test-candidate` (artifact 14177267027) was downloaded and its APK extracted. Extracted APK SHA-256 `0ec0c15f00f2e80a64558729ba1dce23bcb85e27c04389c557b4ebcfa88ac379` matches live `latest.json` exactly.
- Live feed: package `com.personal.diaryapp`, versionName `1.0.170`, versionCode `169`, APK URL `https://raw.githubusercontent.com/amuazzinxyz-ops/My-Diary-Updates/main/My-Diary-1.0.170.apk`, APK SHA-256 `0ec0c15f00f2e80a64558729ba1dce23bcb85e27c04389c557b4ebcfa88ac379`, webVersion 247 and matching web SHA-256 above. The workflow validates the release signing certificate against the previously approved fingerprint before publishing.
- Both delivery routes are live: signed APK 1.0.170 and in-app Check for Update Web Update 247. Local data, notes, photos, documents, PIN/recovery, reminders, package identity and signing identity were preserved.
- Phone-side test of this specific no-lock message remains pending; do not claim device PASS until user confirms. Repository/build/feed/artifact checks are PASS.


# Diary Lock no-lock message moved into the same popup box — Web Update 248 / APK 1.0.171 (2026-11-16)

- User clarified that the no-lock message must appear in the same centered popup box where the browser alert used to appear, not as a separate status line below the Diary content.
- Backup branch: `backup/before-diary-lock-no-lock-popup-box-fix-2026-11-16`. Feature branch: `fix/diary-lock-no-lock-popup-box-248-2026-11-16`.
- Minimal change in `turnDiaryLockOff()`: when no Diary PIN exists, show the existing translated `diaryNoLock` message inside the same centered gold-bordered popup style, with a Close button. Do not write it to `diaryMyNotesStatus`. The PIN-entry dialog and correct-PIN unlock flow remain unchanged.
- Preserve all local notes, photos, documents, IndexedDB records, PIN/recovery data, reminders, package identity and signing identity.
- Planned Web Update 248 SHA-256: `13dbccd3b369b6674a75bfc06e48ccaa1a75a62c98c239952ba80d999addd26c`. Source and mirror are updated identically.
- Planned APK 1.0.171 / versionCode 170 is required under the permanent dual-delivery rule. APK build, signature continuity, published APK SHA, latest.json live verification, and phone test are pending; do not claim release completion until verified.


# Diary Lock no-lock popup box correction — APK 1.0.171 / Web Update 248 published (2026-11-16)

- User clarified that the no-lock message must appear in the same centered popup box where the browser alert used to appear, rather than below the Diary panel. PR #89 merged as `6550cecb769a40240a47ddefb2ad3cfc57d74994`.
- Implementation: `turnDiaryLockOff()` now shows the translated `diaryNoLock` message in the same centered gold-bordered popup style with a Close button. It no longer writes this message to the separate `diaryMyNotesStatus` area. The actual PIN-entry/unlock flow is unchanged.
- Web Update 248: source and mirror are byte-identical, Git blob SHA `e1bd3baded0490d460353b988290f0f0e9813335`. Live `latest.json` advertises webVersion 248 and SHA-256 `13dbccd3b369b6674a75bfc06e48ccaa1a75a62c98c239952ba80d999addd26c`. Web publisher run #249 (`43754369962`) completed successfully.
- APK 1.0.171 / versionCode 170: build run #246 (`43754632088`) completed successfully. The first run #245 safely stopped at the publication guard because one remaining accepted-feed tuple still used the old baseline; PR #90 corrected that exact guard and the successful #246 run followed.
- Signing certificate continuity guard passed against the established SHA-256 fingerprint `23A4E93F3C7911DCE18389EA583548700C6AD6A3759707F1CD222D07E2408B5A`. Signed APK artifact `My-Diary-1.0.171-signed-test-candidate` was downloaded and independently checked: 2,028,818 bytes; APK SHA-256 `a3c29b2673bd484228b63f74ecdd1f8df194bdb4c757957648c458fc4817bb93`; Git blob SHA `3965093988ca075d657a7e5ea088693b1df37cb2`.
- Live `latest.json` confirms package `com.personal.diaryapp`, versionName `1.0.171`, versionCode `170`, APK URL `https://raw.githubusercontent.com/amuazzinxyz-ops/My-Diary-Updates/main/My-Diary-1.0.171.apk`, and APK SHA-256 matching the signed artifact. Both versioned APK and stable `My-Diary.apk` paths were verified to reference the exact same blob SHA `3965093988ca075d657a7e5ea088693b1df37cb2`.
- Existing notes, photos, documents, IndexedDB records, PIN/recovery, reminders, app package and signing identity were not changed. Physical phone test is still pending; do not mark device PASS until the user confirms.


## Removable Diary Lock Settings + optional native fingerprint unlock — Web Update 257 / APK 1.0.176 (2026-11-16)

- User requested a new optional feature in **Me**: a removable **Set Diary Lock** screen with two ON/OFF switches, **Diary Lock** and **Enable Fingerprint**. User explicitly said to keep other locks untouched and make the new screen easy to remove if disliked.
- Backup branch: `backup/before-diary-lock-settings-fingerprint-2026-11-16`. Feature PR #97 merged to main as `a406ba32c12ab7481bfe95566f7cd81dcbe12d6b`.
- Added a separate **Set Diary Lock** entry inside Me. Diary Lock switch reuses the existing Diary PIN setup and disable flows; it does not create a second PIN system. Fingerprint switch is available only when Android reports a fingerprint sensor and an enrolled fingerprint. The unlock screen adds a separate native fingerprint action; existing PIN and Forgot PIN routes remain available.
- Native Android bridge uses the platform BiometricPrompt and checks fingerprint hardware/enrolment. Added required biometric permissions. Web-side fingerprint enable preference uses a separate key and is removed when Diary Lock is disabled. Existing Note Lock and all other locks are untouched. No notes, photos, documents, IndexedDB, PIN/recovery records, reminders, package identity or signing identity were intentionally changed.
- APK build workflow run #256 (`43843200994`) completed successfully. All steps passed, including signing keystore/alias validation, Android project verification, exact latest web HTML inclusion, debug build, signed release configuration, publication, and artifact upload. The established signing certificate continuity guard passed.
- Signed APK 1.0.176 / versionCode 175 is published at `https://raw.githubusercontent.com/amuazzinxyz-ops/My-Diary-Updates/main/My-Diary-1.0.176.apk`. Live feed APK SHA-256: `30bc3f1fa1b37b53c3c736acbf5503aca03be20cd94ba9705b693ff9c01d47cc`. Published APK Git blob SHA: `9a249fcfe5ea0d6244428b78a6b9e05cb4a06bce`.
- Check for Update Web Update 257 is published. Source `web-source/index.html` and published mirror `diary-web/index.html` are byte-identical at Git blob SHA `0fa119565762e29b04de3f604c87fb7f6d7e1ea1`. Live UTF-8 web SHA-256: `d0bdd0d2970d13e3a01eb52d293e3d96dad4344a27d9107a0ea0cea0cbb9550b`. Publisher run #257 (`43843701622`) completed successfully. Live `latest.json` advertises APK 1.0.176/code 175 and Web Update 257 with matching checksums.
- Repository/build/publication checks are PASS. **Physical-phone testing is pending**: user must confirm the new switches, PIN setup/disable, and fingerprint prompt on their device. Do not claim device-side PASS until confirmed.


## Note Backup scope fix — Web Update 271 (2026-11-16)

- User confirmed Web Update 270 remained on `My Documents database kholi ja rahi hai…` while the My Documents feature itself works normally.
- Root cause found by source inspection: `openMeFeatureDb()` and `meFeatureAll()` were declared inside `makeOverlay()` but the backup export/restore functions are outside that function's lexical scope. The export's direct call to `meFeatureAll()` therefore throws a synchronous `ReferenceError` immediately after setting the initial status text; this explains why the UI stayed on the first message and why the IndexedDB timeout diagnostics never appeared. This is a code-scope defect, not evidence that the user's documents database is corrupt.
- Minimal correction: expose the existing, already-used database opener and collection reader through two outer-scope function references when the overlay is initialized; route combined backup export and restore through those references. Preserve existing database name/schema, Notes, My Documents, My Memories, Blob serialization, duplicate-skip restore behavior, Note/Diary locks, reminders, app package and signing identity.
- Source and mirror remain byte-identical. Repository changes require validation and publication; user phone confirmation is still pending. Do not claim the backup works until user tests Notes + Documents + Memories export and restore.


# Note Backup/Restore progress shown in raised 3D popup — release pending (2026-11-16)

- User requested that all messages shown during Note Backup and Restore appear clearly inside a raised 3D popup card, with an **×** close control, instead of the small status line.
- Created exact pre-edit snapshot branch: `backup/before-note-backup-status-popup-3d-2026-11-16`. Feature branch: `fix/note-backup-restore-3d-popup-2026-11-16`.
- Added one reusable Backup/Restore popup with a large bold message, gold raised 3D card, readable inset message panel, and explicit × close button. Backup stage/progress/success/error messages and Restore preparation/success/invalid-backup messages now update in the same popup. Closing it dismisses further progress updates for that operation; starting a new backup/restore opens it again.
- Only the Backup/Restore message presentation is intended to change. The underlying export/import data format, Notes/Documents/Memories records, database helpers, duplicate-skip restore behavior, PIN/locks/recovery, reminders, package identity and signing identity remain untouched.
- Source/mirror equality, JavaScript syntax, PR merge, Web Update checksum/version publication, signed APK build/publication, and final dual-route verification are pending. Do not tell the user to update until both APK and Check for Update delivery routes pass all checks. Physical phone testing remains pending until user confirmation.

- Release workflow was advanced from the already-published 1.0.181/180 to the next signed APK **1.0.182 / versionCode 181**; feed guards accept only the installed 1.0.181/180 baseline or the exact new 1.0.182/181 release. APK and web release notes now describe this popup change. This prevents re-publishing the old APK version as an in-place update.


### Release verification — Note Backup/Restore raised popup (2026-11-16)

- PR #115 merged to main as `f519c2e20ed9387b4a3246d056fbe87891dc8b6b`. Pre-edit snapshot branch: `backup/before-note-backup-status-popup-3d-2026-11-16`.
- `web-source/index.html` and `diary-web/index.html` are byte-identical at Git blob SHA `76d5f3faf13ce1efadb414493ee345b48f5cb83f` (448,226 UTF-8 bytes). The signed APK build independently computed the same web SHA-256 `b9b86e4c697b22b83cf2884883c63bf08e1f00102cbc1aff6eb307953211dce3`.
- Web publisher run `43891963869` completed successfully. Feed-only version advancement commit set **Web Update 272**; follow-up web publisher run `43892108675` completed successfully without changing the intended version. Live `latest.json` advertises Web Update 272 and the exact web SHA-256 above.
- Android build run `43891964063` completed successfully. The build embedded the exact published HTML, built debug and signed Release APKs, passed the signing certificate continuity check, and published APK **1.0.182 / versionCode 181**. Certificate SHA-256 fingerprint verified in workflow logs: `23A4E93F3C7911DCE18389EA583548700C6AD6A3759707F1CD222D07E2408B5A`.
- Signed artifact `My-Diary-1.0.182-signed-test-candidate` was independently downloaded and inspected. Extracted APK size 2,039,904 bytes; SHA-256 `ddf0c895e7a81a13bdf241b57166cadb5bcd4b92ce61184378b39d7509853509`, matching live `latest.json`. Its Git blob SHA `bf52a571d278ca95155a55f7a035d53462553ba5` and size match both published paths `My-Diary-1.0.182.apk` and `My-Diary.apk`.
- Live feed confirms package `com.personal.diaryapp`, versionName `1.0.182`, versionCode `181`, direct APK URL `https://raw.githubusercontent.com/amuazzinxyz-ops/My-Diary-Updates/main/My-Diary-1.0.182.apk`, matching APK SHA-256, Web Update 272, and matching web SHA-256. Both direct APK and in-app Check for Update routes are published and verified.
- Repository/build/publication verification: PASS. Physical phone visual test of Backup and Restore popup and actual combined backup/restore remains pending user confirmation. No phone-side PASS is claimed.


## Revert Note Backup/Restore popup — original in-section messages restored (2026-11-16)

- User asked to remove the recently added global 3D Backup/Restore popup and return to the previous behavior. The popup CSS, overlay creation helper, dismissal state, and all popup references have been removed.
- Backup and Restore progress, completion, and error messages again write to the existing `diaryMyNotesStatus` element inside the opened Notes panel. The Welcome Screen no longer receives or displays these Backup/Restore messages. Backup/Restore data handling is unchanged.
- This is a presentation-only revert. Release target: signed APK **1.0.183 / versionCode 182** and Check for Update **Web Update 273**. Do not tell the user to update until source/mirror equality, syntax, build, signing continuity, APK SHA, and both delivery routes are verified.
- Physical-phone verification remains pending; do not claim device-side PASS until the user confirms.


### Revert release verification — My Diary 1.0.183 / Web Update 273 (2026-11-16)

- PR #116 merged to main as `dbd2c33dc92db38772f24486a7ce019ab7976fae`. Pre-edit snapshot branch: `backup/before-scoped-backup-popup-fix-2026-11-16`; feature branch: `revert/backup-restore-popup-2026-11-16`.
- Removed the global Backup/Restore popup CSS, overlay helper, dismiss state, and popup calls. Backup/Restore progress, success, and error messages again update the existing `diaryMyNotesStatus` within the opened Notes panel. No popup-related IDs/helper references remain in the published HTML; Notes/Documents/Memories backup and restore data logic is unchanged.
- `web-source/index.html` and `diary-web/index.html` are byte-identical at Git blob SHA `3bbe88e9a7b6fddcdccfc388a79390a34c92bc58` (444,757 UTF-8 bytes). SHA-256: `343e8d46ddee84b981d50409a177df1a83b3d47670dcc8269eaee43e0ee34674`.
- Web publisher run `43904211137` completed successfully and repaired the published mirror/checksum. The feed's web version was then advanced to **273** with accurate release notes in commit `56d2131047dc9bba4ee5e30307e63630dd04cbc8`.
- Android build run `43904211135` completed successfully. Build included the exact published HTML; JavaScript syntax and project validation passed. Signed APK **1.0.183 / versionCode 182** was published. Signing certificate continuity check passed against the previously supplied certificate.
- Signed artifact `My-Diary-1.0.183-signed-test-candidate` (artifact ID `14245480546`) was downloaded and independently inspected. Extracted APK size: 2,039,096 bytes; SHA-256: `6d71b4ac55693d2adb3141ea0f4be72ec0c1bdf1592be5ea1832e44d4ea6fd75`, matching live `latest.json`.
- Live feed advertises package `com.personal.diaryapp`, versionName `1.0.183`, versionCode `182`, direct APK URL `https://raw.githubusercontent.com/amuazzinxyz-ops/My-Diary-Updates/main/My-Diary-1.0.183.apk`, matching APK SHA-256, Web Update 273, and matching web SHA-256. Both APK and Check for Update delivery routes are published.
- Repository/build/publication verification: PASS. Physical-phone confirmation that the Welcome Screen no longer shows Backup/Restore messages and that the old in-Note status display behaves correctly is still pending.


# Remove “Ek Rang Chunein” from Cover and Detail photo menus — release pending (2026-11-16)

- User explicitly approved removing only the **Solid Colour / Ek Rang Chunein** choice from the two Diary editor menus: **Note ka Cover Photo** and **Tafseel ki Photo**.
- Those two menus retain **Choose Image** and **Gradient Colour**. The separate generic **Photo** menu is unchanged. No image data, saved colours, note content, PIN/locks, recovery, reminders, app identity or signing identity are changed.
- Implementation is scoped by the existing `kind` argument in `attachDiaryColourChooser`: Cover and Detail append only Choose Image + Gradient Colour; other kinds retain all three choices.
- Snapshot branch: `backup/before-photo-color-name-button-removal-2026-11-16`. Feature branch: `fix/remove-photo-color-name-buttons-2026-11-16`.
- Source/mirror equality, syntax, PR merge, Web Update publication, signed APK build/publication, and both delivery-route checks are pending. Do not tell the user to update until all required checks pass. Physical phone test remains pending.


# Remove “Ek Rang Chunein” from Photo Lagayein menu — release pending (2026-11-16)

- User expanded the earlier photo-menu request and explicitly asked to remove the **Solid Colour / Ek Rang Chunein** option from the separate generic **🖼️ Photo Lagayein** menu as well.
- The generic Photo menu now presents only **Choose Image** and **Gradient Colour**, matching the two earlier editor menus (Note ka Cover Photo and Tafseel ki Photo). The existing image-selection and gradient-colour handlers remain; only the Solid Colour choice is omitted from the visible menu.
- Snapshot branch: `backup/before-photo-menu-solid-colour-removal-2026-11-16`. Feature branch: `fix/remove-photo-menu-solid-colour-2026-11-16`.
- This follow-up does not alter photo attachment/storage, existing saved images, cover/detail behaviour, note content, PIN/locks/recovery, reminders, package identity or signing identity. Release checks and dual APK + Check for Update publication are pending; do not tell the user to update until both delivery routes and signing/checksum verification pass. Physical phone test remains pending.


# My Diary 1.0.185 / Web Update 275 — remove Solid Colour from all three photo menus (release in progress, 2026-11-16)

- User explicitly expanded the earlier request to remove **Ek Rang Chunein / Solid Colour** from the generic **Photo Lagayein** menu in addition to **Note ka Cover Photo** and **Tafseel ki Photo**. All three menus now expose only **Choose Image** and **Gradient Colour**; no other photo attachment behaviour was changed.
- PR #118 merged as `f85e82cb2f0149f61a7074d7d5bd2ac582bcb89c`. Pre-edit snapshot for the source change: `backup/before-photo-menu-solid-colour-removal-2026-11-16`; follow-up snapshot before release-pipeline advancement: `backup/before-photo-menu-1-0-185-release-2026-11-16`.
- The web publisher completed successfully as run `43908592983`; verify the live feed advertises Web Update 275 and the source/mirror SHA-256 before marking web delivery complete.
- The previous photo-menu release **1.0.184 / versionCode 183** had already been published for Cover + Detail only. The generic Photo follow-up therefore requires **1.0.185 / versionCode 184**. The APK workflow and release notes are advanced accordingly, with feed guards accepting only installed baseline 1.0.184/183 or exact new 1.0.185/184.
- Signed APK build run `43908592993` was triggered from the earlier static 1.0.184 workflow and must fail closed against the now-published 1.0.184 feed; do not treat it as the new release. The corrected 1.0.185 workflow release, signing continuity, artifact SHA-256 and live feed publication are pending.
- No saved photos, notes, documents, memories, PIN/locks/recovery, reminders, package identity or signing identity are changed. Physical phone test remains pending; do not claim device-side PASS until user confirms.


- **Web feed version correction:** publisher run `43908592983` completed successfully and synchronized the mirror/checksum but did not increment webVersion because source and mirror had already been committed together. This release explicitly advances the feed to **Web Update 275** with the accurate three-menu release note. The earlier APK workflow run `43908592993` correctly failed closed at the release publication guard because APK 1.0.184/183 was already live; it did not publish or overwrite an APK.


### Phone test confirmation — My Diary 1.0.185 / Web Update 275 (2026-11-16)

- User confirmed the phone test passed: the **Ek Rang Chunein / Solid Colour** choice is removed as intended from all three menus — **Note ka Cover Photo**, **Tafseel ki Photo**, and **Photo Lagayein**.
- User-confirmed device result: **PASS** for this specific requested menu change. No broader app-wide phone-test status is implied.
- Release remains My Diary **1.0.185 / versionCode 184** and Web Update **275**. No further source or release changes were made for this confirmation.


# Private Locker × closes only the Locker, not the Me panel — Web Update 302 published (2026-11-17)

- User tested the Private Locker × button and reported that it also closed the **Me** panel. Source inspection identified the event-order bug: the close handler correctly reopens Me, but the click then bubbles to the Diary overlay's outside-click listener, which immediately hides Me again.
- Minimal fix in `web-source/index.html`: stop propagation on the Private Locker × click before calling the existing `privateLockerCloseNow()`. This keeps the Locker close/reset behavior and leaves Me open. No other Private Locker controls, encrypted entries, PIN/recovery wrappers, Pattern/Fingerprint settings, Diary Lock, Note Lock, or unrelated features are changed.
- Backup branch: `backup/before-private-locker-close-me-panel-fix-2026-11-17`. Working branch: `fix/private-locker-close-only-me-panel-2026-11-17`. Base main commit: `6d46bc8cef476f4379d8ce0a764de171ae6df9eb`.
- PR #155 merged as `972073b3a0b3c8450fbc82a0bc247c03accc5844`. Web publisher run `44107256741` succeeded and published **Web Update 302**. Source and mirror are byte-identical at Git blob SHA `84c242a79039d77723b132476a6dd224c082ecb1`; live `latest.json` advertises web SHA-256 `67fdb09cbcfce6962c42ede125aae1f610ac99f8adf87de11354db9ef6480844`.
- APK workflow run `44107256784` safely stopped at its pre-build source/mirror equality guard because it started before the web publisher synchronized the mirror. It did not reach Gradle, sign, or publish. Existing APK remains **1.0.189 / versionCode 188**, SHA-256 `1f627d94f744a70949fcaefcacb0269f90a36fbc10360368de60f4d3773cb133`. The web update is published; APK has not been rebuilt for this web-only fix.
- Static event-flow verification confirms the × handler stops propagation before running the existing close/reset function. Physical-phone testing remains pending; do not claim device-side PASS until the user confirms that × closes only Private Locker and leaves Me open.


# Private Locker Lock Off now requires an explicit PIN verification tap — fix (2026-11-17)

- User reported that tapping **🔓 Lock Off Karein** on the Private Locker PIN screen turned Lock OFF without asking for the PIN. The PIN screen already had automatic PIN submission; browser/password-manager autofill could therefore submit a filled value immediately after the action was selected.
- Changed only the Private Locker PIN action form in `web-source/index.html`: selecting **Lock Off** now disables automatic submission for that action and explicitly displays **🔓 PIN Verify Karke Lock Off Karein**. The user must enter the PIN and tap that verification button; only a successfully unwrapped Locker master key can reach the existing Lock-Off persistence function. Other security actions retain their existing auto-verification behavior.
- Existing encrypted entries, PIN/recovery wrappers, master key, Pattern/Fingerprint settings, Lock On flow, Diary Lock, Note Lock, and all unrelated features are unchanged.
- Backup branch: `backup/before-private-lockoff-explicit-pin-2026-11-17`. Working branch: `fix/private-lockoff-require-explicit-pin-2026-11-17`.
- PR #158 merged as `f64861b8d97fe585b4b032d9066147af07aeca9e`. Backup branch: `backup/before-private-lockoff-explicit-pin-2026-11-17`; working branch: `fix/private-lockoff-require-explicit-pin-2026-11-17`.
- Static checks confirm source and mirror are byte-identical at Git blob SHA `77a9a7a926b119040beafc561cd04ebacd4bff55`, Lock Off disables auto-submit, and the explicit Verify button is shown. Web publisher run `44117122562` completed successfully. Published as **Web Update 305**; live `latest.json` advertises web SHA-256 `6501093d9213d68ca0aee1d8143f80431d43b282679ba3c2e004fa76e33ec058`.
- APK build workflow run `44117122663` was triggered by the merge; it must be checked for a safe stop at the existing-release guard because this is a web-only change and APK remains **1.0.189 / versionCode 188**. Do not claim a new APK unless the workflow completes all release and signing checks.
- Physical phone testing remains pending; do not claim device-side PASS until the user confirms that Lock Off requires the PIN and explicit Verify tap.


# Smart Reminder + Personal Calendar screen-off alarm scheduling — signed APK published (2026-11-17)

- User requested the existing **Smart Reminder** and **Personal Calendar** alarms to work with the phone screen off, including ringtone and notification, without changing unrelated features.
- Removed only the native scheduling gate that aborted all alarm scheduling when Android full-screen-intent permission was unavailable. Exact-alarm and notification permission checks, AlarmManager alarm-clock scheduling, notification/full-screen activity path, foreground ringtone service, wake lock, Snooze/Done, repeat and reboot restoration remain intact. Android can still restrict full-screen wake UI when its permission is denied; device-side behaviour must be tested.
- Backup branch: `backup/before-smart-reminder-calendar-screenoff-repair-2026-11-17`. Work branch: `fix/reminder-calendar-screenoff-permission-fallback-2026-11-17`. PR #163 merged to main as `0cec30a3a6b79125dcfb7929078200599a8f8cdd`.
- Signed APK workflow run `44140100242` completed successfully. Signed APK **1.0.189 / versionCode 188** uploaded; SHA-256 `fb250b75d4a58b981600e6ce1528e7d529d7df06ab87fb58daf9ecaeff3404cd`. The downloaded signed APK artifact was independently SHA-256 checked and matched the feed.
- Source and mirror remain byte-identical at Git blob SHA `4af15d4a610f72403652df15e9488dabc6c0c3ab`. The APK workflow temporarily overwrote the web metadata with an older value; restored `latest.json` to the pre-build published **Web Update 287** metadata and verified the APK and web SHA fields afterward. Feed correction commit: `0177a306082e81e24c0c1a4fb62e852ac3000570`.
- No reminder/calendar data, saved notes, Diary Lock, Note Lock, Private Locker, PINs, photos, or unrelated web features were edited by this change. Physical screen-off test with ringtone/notification/wake display is still pending user confirmation; do not claim device-side PASS until tested on the phone.


# Check for Update Web Update 288 — published (2026-11-17)

- User pointed out that **Check for Update** had not been advanced with the Smart Reminder / Personal Calendar alarm repair. Corrected the update feed to **Web Update 288** while retaining the exact current HTML SHA-256 `3e3994514fbc6003fcda889e313a9fad700878d0045e4a96048a02d1efd2a242`; source and mirror HTML were already byte-identical, so no unrelated HTML code was changed.
- Feed commit: `1d6c1f301dfd1eef6e4b6dbe8159fd7c89484c39`. APK remains **1.0.189 / versionCode 188**, SHA-256 `fb250b75d4a58b981600e6ce1528e7d529d7df06ab87fb58daf9ecaeff3404cd`.
- This advances the Check for Update web-version marker and notes the native alarm fix. The actual Android alarm scheduling fix is in the signed APK; a web refresh alone cannot replace native APK code. Phone-side screen-off test remains pending.


# Personal Calendar + Smart Reminder — 3-dot exits Edit mode and restores list position (Web Update 316, 2026-11-18)

- User clarified that when saved entries are already moved to the top in Edit mode, tapping the **⋮ three-dot button again** should immediately close Edit mode and return the entries to their normal position. Implemented identically for **Personal Calendar** and **Smart Reminder**.
- Changed only the three-dot button click handler in `web-source/index.html`: when either supported feature is in bulk Edit mode, the tap exits that mode, clears temporary checkbox selections, hides the bulk-delete bar, removes the Edit-mode layout class, restores the normal form/tools/status/list order, and returns the modal scroll to the top. It does **not** delete any entry. Existing menu Edit/Done route, Delete Selected confirmation, record deletion, reminder cancellation and calendar alarm cancellation handlers remain unchanged.
- Backup branch: `backup/before-edit-menu-toggle-2026-11-18`. Feature branch: `fix/edit-menu-toggle-restore-list-2026-11-18`. PR #189 merged as `01c81bd3bcbfb4ec7603dd74e3fcb473a6c86bed`.
- Exact diff review: one file only (`web-source/index.html`), one line added and one line replaced; no other files changed. Static handler review confirms the early exit is limited to Calendar/Reminder bulk Edit mode and that it clears selection state without invoking deletion.
- Web publisher run `44255496806` succeeded. Published as **Web Update 316**. Source and published mirror are byte-identical at Git blob SHA `6aef56f009e37a1fbccf37e95c313060e037c206`; `latest.json` advertises web SHA-256 `7df9a09d7226df862909331f722e596fa1c37f0d9801041586dd0bb145a0e532`. APK remains **1.0.193 / versionCode 192**, SHA-256 `b21819e3af1a8a4338218ce70604b4bbd056888df3e23633c5b3d05a8e881dd4`; no APK release was made for this web-only change.
- The push-triggered APK workflow run `44255496839` stopped at its source/mirror guard step before Gradle build, signing or upload; all subsequent APK steps were skipped. The web publisher then completed and source/mirror equality was re-verified. No APK artifact or APK metadata was changed by that run.
- Register-entry backup branch: `backup/before-edit-menu-register-entry-2026-11-18`; register documentation branch: `docs/edit-menu-toggle-register-entry-2026-11-18`.
- Physical phone testing remains pending. Do not claim device-side PASS until the user confirms that tapping ⋮ again in both features restores the normal list position and does not delete entries.


---

# Personal Calendar event reminders automatic — Web Update 317 published (2026-11-18)

- User requested removal of the **“Event ke waqt yaad dilayein”** checkbox and its label while keeping event-time reminders active automatically.
- Updated only the Personal Calendar form/save/edit path in `web-source/index.html`: removed the checkbox and its edit-state reference; every newly saved or edited Calendar event now sets `record.remind = true` and uses the existing `calendarScheduleAlarms(record)` scheduler.
- Smart Reminder is untouched. Existing Calendar entries are not migrated automatically; an old entry becomes reminder-enabled when it is edited and saved. Existing sound, snooze interval/limit, ring duration/volume, repeat selection and alarm cancellation paths remain in place.
- Backup branch: `backup/before-calendar-auto-reminder-2026-11-18`. Working branch: `fix/calendar-reminder-auto-on-2026-11-18`. PR #191 merged as `638b921ffca7aa198d609d5cb06f77f1db8c7cc0`.
- Web publish workflow run #372 completed successfully. Published **Web Update 317**; `latest.json` reports web SHA-256 `b1503b0105fb9b77f0d214fbbc881ef876ca817824dac8f98dc7c993ef288fc8`. Verified `web-source/index.html` and `diary-web/index.html` are byte-identical (blob SHA `910b3c892a97c211224cd2d9d90646e5d1581cbd`).
- No APK/native Android release was made. Physical-phone alarm testing remains pending; do not claim device-side PASS until the user tests a new Calendar event.


---

# Custom weekday picker closes after selection — Web Update 323 (2026-11-18)

- User reported that the **Custom** weekday picker opened too low and remained open after selecting a day. Corrected the shared control used by **Personal Calendar** and **Smart Reminder**: tightened its top spacing, added a visible **×** close button, and made selecting or deselecting a weekday close the picker immediately. Added a compact **“Custom din badlein”** control to reopen it; already-selected weekdays remain checked so users can choose multiple days one at a time.
- Backup branch: `backup/before-custom-panel-close-position-2026-11-18`. Work branch: `fix/custom-weekday-panel-auto-close-2026-11-18`. PR #203 merged as `27f555e6fbc2759b4a8d75dc82958ba3774652b9`.
- Only `web-source/index.html` and its required identical mirror `diary-web/index.html` were changed. Exact main-branch verification: both files are byte-identical, Git blob SHA `01f104be46927405315592cf7c65ab4b37cf1fe3`, 525,779 bytes. No recurrence scheduler, saved Calendar/Reminder entries, APK/native code, PINs, locks, notes, photos, or unrelated features were changed.
- Web publisher workflow run `44311786468` (run #382) completed successfully. Published **Web Update 323**; `latest.json` advertises web SHA-256 `bedec7af5e9ada4230a387cb7543d99280423bc0be77a2940f504e615e41434a`. APK remains **1.0.194 / versionCode 193**; no APK rebuild is required for this web-only UI change.
- Physical-phone testing is still pending. Do not claim device-side PASS until the user confirms that selecting a weekday closes the panel and reopening it preserves the previous selections in both features.


# Personal Calendar + Smart Reminder Custom weekday picker remains open for multi-select — correction (2026-11-18)

- User clarified that the **Custom weekday picker must remain open after selecting or deselecting a day**, because multiple weekdays need to be selected in one visit. The earlier Web Update 323 auto-close-on-selection behaviour was incorrect for this multi-select use case.
- Corrected only the shared `mfRepeatDaysControl` weekday checkbox handler: selecting/deselecting a weekday no longer closes the panel. The existing visible **×** remains the explicit close control; after closing, the existing **✎ Custom din badlein** control reopens the picker with prior selections checked.
- Applies identically to **Personal Calendar** and **Smart Reminder** because both use the same shared control. No recurrence calculation, saved entries, reminder scheduling, alarm settings, PINs, locks, notes, photos, native APK code, or unrelated UI was changed.
- Snapshot branch: `backup/before-custom-weekday-multiselect-2026-11-18`. Working branch: `fix/custom-weekday-multiselect-stay-open-2026-11-18`.
- Only `web-source/index.html` and its required identical mirror `diary-web/index.html` changed, plus this Master Register entry and `latest.json`. PR #204 merged as `37a6abe6fd054a7ec517e7abf9d053b674b93aa7`. Source/mirror are byte-identical at Git blob SHA `cb73cbef9aad890957aaa9f6d7da170297d4d589` (525,712 bytes). The feed now advertises Web Update 324 with web SHA-256 `77b333ee5e5b928a31d645f1afb2608807a3bddbb68ded23c2e76b448200db99`. APK remains 1.0.194 / versionCode 193; no APK rebuild was made. Physical-phone testing remains pending.


# Personal Calendar + Smart Reminder — centre the saved-entry name button (Web Update 347, 2026-11-19)

- User clarified that the entire name badge/button should move horizontally to the centre of each saved entry card, while remaining at the top in its existing vertical position. The text inside the badge is centred too.
- Applied one shared CSS-rule change in `web-source/index.html`: added `align-self:center`, changed badge justification and text alignment to centre, and retained its existing fit-content width, wrapping, and top placement. Because both **📅 Personal Calendar** and **⏰ Smart Reminder** use the same renderer/class, the change applies identically to both.
- No entry data, order, pin state, long-press actions, form, recurrence, alarm/reminder scheduling, notification, ringtone, APK/native code, or unrelated features were changed.
- Backup branch: `backup/before-calendar-reminder-name-button-center-2026-11-19`. Working branch: `fix/calendar-reminder-name-button-center-2026-11-19`. PR #249 merged as `ce3c60146b565d6de7c46f26536c5e192019cb56`.
- Published successfully as **Web Update 347**. The web publisher synchronized `diary-web/index.html` with `web-source/index.html`; both are byte-identical at Git blob SHA `821c3dbb8e9cfb4de1382b199b2af03af32f5673` (558,341 bytes). `latest.json` advertises web SHA-256 `0b9433413ef79afacd0af73d72da3c888d41ff7ff2ffb10d911d99566fa1a463`.
- APK remains **1.0.194 / versionCode 193**. No APK/native build or release was made. Physical-phone testing remains pending user confirmation.


# Personal Calendar — Birthday, Date and Time badges on one line (Web Update 348, 2026-11-19)

- User clarified that the existing Birthday and Time buttons should remain, and only the missing Date button should be added. The required order directly under the centred name button is **Birthday · Date · Time**, all on one line.
- Added a date badge using the already-saved entry date and existing date formatter. Kept the existing Birthday/type badge and Time badge. Added a Calendar-row-specific no-wrap layout with compact badge spacing so the three badges stay together on one line; no form fields or saved data format changed.
- Only `web-source/index.html` was edited for the feature (4 additions, 1 deletion). No Smart Reminder renderer, entry data/order, pin, long-press actions, recurrence, alarm scheduling, notification, ringtone, APK/native code, or unrelated feature was changed.
- Backup branch: `backup/before-calendar-date-badge-2026-11-19`. Working branch: `fix/calendar-birthday-date-time-row-2026-11-19`. PR #251 merged as `9fc880975823831bbee21a6697ac6e98da6663d4`.
- Published successfully as **Web Update 348**. `web-source/index.html` and `diary-web/index.html` are byte-identical at Git blob SHA `d702aa397f0fcef677ff56cd7b3ef4c41d635e44` (558,826 bytes). `latest.json` web SHA-256: `9fae0229aa6b2a996581e7d0850dc465d976d86b1898590e932e26d444e43248`.
- APK remains **1.0.194 / versionCode 193**. No APK/native build or release was made. Physical-phone testing remains pending user confirmation.


---

# Recently Deleted — full-screen mobile view (Web Update 356, 2026-11-19)

- User requested that tapping **🗑️ Delete Ki Huwi Note** open the deleted-notes view across the full mobile screen rather than inside the compact Me menu.
- Updated only the existing Recently Deleted open/close presentation and added isolated mobile CSS. The Me-menu trash button becomes **✕ Band Karein** while the full-screen view is open; tapping it returns to the regular Diary view.
- Existing trash rendering, note contents, Restore, permanent-delete confirmation, 30-day expiry, storage keys, and note data format are unchanged. No APK/native Android code or unrelated Diary features were changed.
- Backup branch: `backup/before-trash-fullscreen-2026-11-19`. Working branch: `fix/trash-fullscreen-2026-11-19`. PR #269: https://github.com/amuazzinxyz-ops/My-Diary-Updates/pull/269
- `web-source/index.html` and `diary-web/index.html` are byte-identical at Git blob SHA `c72f0ff77f3108e0fad5c9dc2ed836204e4eeb29` (565,582 bytes). `latest.json` advertises Web Update 356 with web SHA-256 `aeb426d92edebba1cd186f2a200c4ad10a682837343be53303a474c6f1a735fe`. APK remains **1.0.194 / versionCode 193**; no APK rebuild is required for this web-only UI change.
- Physical-phone visual test remains pending user confirmation. Do not claim device-side PASS until the user confirms the deleted-notes view fills the mobile screen and its close control returns correctly.


---

# Recently Deleted full-screen close-state safeguard — Web Update 356 correction (2026-11-19)

- Added a small cleanup to the existing Diary close path: if the user closes the entire Diary while Recently Deleted is open, the full-screen class is removed, the trash list is returned to its original Diary body location, the trash button label is restored, and the next Diary opening starts in the normal view.
- This is a presentation-state safeguard only. Trash records, saved notes, Restore/Delete Permanently handlers, expiry, PINs, locks, photos, and APK/native code are unchanged.
- Backup branch: `backup/before-trash-fullscreen-close-reset-2026-11-19`. Correction branch: `fix/trash-fullscreen-close-reset-2026-11-19`.
- Source and mirror are byte-identical at Git blob SHA `95d1fca296beb8b9b11866994fd89057694bceaa` (566,154 bytes). `latest.json` retains Web Update 356 and advertises the updated SHA-256 `2b11d49a46953783bcb45f76557d1d3fcbe95490eefa74043c542ebe964a4cc5`. Physical-phone visual testing remains pending user confirmation.


---

# Recently Deleted full-screen mobile positioning correction (Web Update 356, 2026-11-19)

- User reported the first full-screen version shifted the content above the visible mobile area. Investigation found the existing Me-menu vertical-centering transform was still applied after the menu was repositioned inside the full-screen header.
- Corrected the mobile-only CSS to explicitly reset transforms and offsets on the Me wrapper and panel, keep the close control visible, and let the trash button/list occupy the visible viewport. No trash or note data logic changed.
- Backup branch: `backup/before-trash-fullscreen-position-fix-2026-11-19`. Correction branch: `fix/trash-fullscreen-position-2026-11-19`.
- Source and mirror are byte-identical at Git blob SHA `460dee9914ca3d2f5f711e7e23f94d981dee8e69` (566,688 bytes). `latest.json` web SHA-256: `5bc392dd51238b4172c7b6405e0677143a8e9eb0e1480c07772baf08dea939c5`. APK remains `1.0.194 / versionCode 193`.
- This corrects the earlier 356 UI presentation; physical-phone testing is still pending user confirmation.


---

# Recently Deleted full-screen positioning correction (Web Update 357, 2026-11-19)

- Reissued the corrected mobile-only layout as Web Update 357 so Check for Update can detect the fix instead of seeing the previous Web Update 356 number.
- The HTML correction is merged in PR #272. This release step changes only update metadata and this Master Register record.
- Backup branch: `backup/before-web357-metadata-refresh-2026-11-19`. Release branch: `release/web357-metadata-refresh-2026-11-19`.
- `latest.json` advertises Web Update 357 with web SHA-256 `5bc392dd51238b4172c7b6405e0677143a8e9eb0e1480c07772baf08dea939c5`. APK remains `1.0.194 / versionCode 193`; no APK build was made.
- Physical-phone visual confirmation remains pending.


---

# My Diary Home Screen Widget Settings + native Android widget (APK 1.0.195 / Web Update 358, 2026-11-19)

- User approved adding **Home Screen Widget Settings** inside the existing **Me** button. Added selectable widget content: today's date, My Diary, Personal Calendar, Smart Reminder, and New Note. Added compact/normal/large **text-size** preference; actual widget dimensions remain launcher-resizable, with the Me settings screen explaining this distinction.
- Added a real Android AppWidgetProvider and RemoteViews layout, widget metadata/receiver, persisted SharedPreferences settings, an Android 8+ direct pin request with manual Widgets-picker fallback, and widget-tap routing into the existing Diary WebView. Diary master PIN remains in front of widget destinations; calendar/reminder shortcuts open their existing protected sections. Existing notes, photos, documents, PINs, locks, reminder records/settings, and app identity are preserved.
- Source implementation is in `scripts/add_diary_home_widget.py`, invoked by `scripts/add_diary_app_actions.py`; the original Android project ZIP `Diary-Android-Project-v13 (6).zip` was not modified. Native provider/resources are generated during the existing Android build.
- Backup branch: `backup/before-home-widget-settings-2026-11-19`. Feature PR #275 merged as `9f6cfa193609bb31ab8b9a16167970325a3e3b6e`. The first build stopped safely at an ambiguous MainActivity onCreate anchor before compilation/publication; corrected by PR #276, merged as `0489090644fc287683cbc44ec02b447cf1cb14ca`. No failed-build APK was published.
- Build workflow run #392 (`44475822156`) completed **successfully**. Project guards, exact HTML embedding, translation audit, identity/version checks, debug build, signed release build, signing-certificate continuity, and publish verification all passed. Existing signing certificate SHA-256 remained `23A4E93F3C7911DCE18389EA583548700C6AD6A3759707F1CD222D07E2408B5A`.
- Published signed APK: **1.0.195 / versionCode 194**, package `com.personal.diaryapp`. Signed artifact `My-Diary-1.0.195-signed-test-candidate` ID `14506152745`; extracted APK size 2,082,016 bytes; independently computed SHA-256 `3aef65ca93be3bc7cc4520185594d57072fc0cb7a731f18e09b23e222da09549`, matching live `latest.json`.
- Published **Web Update 358**. `web-source/index.html` and `diary-web/index.html` are byte-identical at Git blob SHA `ec39fe889b501035045b7968d61583a147227fcd` (connector text length 575,657 characters). Live web SHA-256: `3fc059ce199d0d56cd5e7720131948f5d7a2680ed0eeeb06fa97fdcd30d91830`; live `latest.json` advertises webVersion 358, APK 1.0.195/194, and both matching checksums.
- Web publisher run #438 correctly deferred the native-dependent widget bundle while APK 1.0.195 was pending. The successful APK release commit then published the matching webVersion 358/hash in the same live feed. Source/mirror parity and APK/feed hash were rechecked after publication.
- User previously confirmed Web Update 357 on mobile: **“Mobile pe chack kiya alhamdulillah bilkul sahi huwa hai.”** That confirmation applies to the deleted-note full-screen layout. **Physical phone testing of the new Home Screen widget and Widget Settings remains pending**; do not claim it was device-tested.



---

# Widget Settings button spacing and placement (Web Update 359, 2026-11-19)

- User requested the **Home Screen Widget Settings** button label be slightly smaller because it touched the button line, and requested the button be placed below **World Clock** inside Me.
- Reduced only this button's label font from 16px to 15px (small adjustment); moved its append position to immediately after the World Clock button. No other button styles, widget settings/behavior, data, notes, photos, PINs, locks, reminders, or native APK files were changed.
- Backup branch: `backup/before-widget-button-spacing-2026-11-19`. UI change PR #279 merged as `12a16a098e6c812abc404f27f37cb8603efe867e`.
- Web publisher workflow run #439 (`44477571040`) completed **successfully**. Published Web Update **359**; APK remains **1.0.195 / versionCode 194**.
- Verified `web-source/index.html` and `diary-web/index.html` are byte-identical at Git blob SHA `43052be5f7ede20bf2c33376b1f90dccc5aba35f`. Live `latest.json` advertises webVersion 359 and SHA-256 `12e4d8dec319370a5ed5ada1cb8f45eb423471a17cd624d660aafbe8ef5f69dc`.
- Physical-phone confirmation of this button spacing/placement and the Home Screen widget remains pending; do not claim it has been device-tested.


---

# My Diary startup correction — Home Screen Widget Settings button order (Web Update 360, 2026-11-19)

- User reported that Diary stopped opening beyond the welcome screen after Web Update 359. Inspection of the exact merged PR #279 diff found the cause: `mePanel.appendChild(widgetSettingsBtn)` had been inserted before the `widgetSettingsBtn` variable was created. During Diary initialization this attempted to append an undefined value and could throw, preventing the app from opening.
- Corrected only the initialization order in `web-source/index.html`: the existing button is now created and given its existing **15px** font size before it is appended to `mePanel`. Since the World Clock button is appended earlier, Widget Settings remains immediately below World Clock. No other feature, saved data, PIN, lock, reminder, or native APK source was intentionally changed.
- Backup branch: `backup/before-widget-settings-startup-fix-2026-11-19`; Register backup branch: `backup/before-widget-startup-fix-register-2026-11-19`. Fix PR #281 merged as `6feccdfec6c69e556b4e409c7f31bd9ec5a93a2f`.
- Web publisher workflow run **44484323209** completed successfully. Published as **Web Update 360**. `web-source/index.html` and `diary-web/index.html` are byte-identical at Git blob SHA `698325f28bc485f4170cb7affa80fe25635b4734` (575,728 characters). Live `latest.json` advertises webVersion **360** and SHA-256 `934c4cac4634875a935a621946301c3fa85e191e3eb21c398e6a2e5e486a02e2`.
- APK feed remains **1.0.195 / versionCode 194**; this correction is web-only and does not require reinstalling the APK. Physical Android confirmation that the app now opens and that the button position looks right is still pending; do not claim phone testing until the user confirms.



---

# Home Screen Widget Settings — 14px and directly below World Clock (Web Update 361, 2026-11-19)

- User corrected the earlier Web 359 result: the button label must be **14px**, not 15px, and the button must appear immediately below **World Clock** (not lower elsewhere in the Me panel).
- Fixed only the button creation/placement in `web-source/index.html`: create the Widget Settings button before the World Clock button is appended, apply 14px with the existing important override, append World Clock, then append Widget Settings immediately after it. This ordering also ensures the button exists before it is appended; no use-before-initialization or undefined append is introduced.
- No other Me controls, widget settings behavior, saved notes/photos/documents, PINs, locks, reminders, native Android sources, or APK were changed.
- Backup branch: `backup/before-widget-settings-14px-worldclock-order-2026-11-19`. Fix PR #283 merged as `ec1c7aa8a1abb19dd29b306ecc7617fb1fefadaa`. Register backup branch: `backup/before-widget-settings-14px-register-2026-11-19`.
- Web publisher completed automatically after the merge and published **Web Update 361**. `web-source/index.html` and `diary-web/index.html` are byte-identical at Git blob SHA `98ef6644c15d7ddb0c882457c35c047ae0201db2` (575,821 bytes). Live `latest.json` advertises webVersion 361 and web SHA-256 `5375f435a2728c0bc0af7767535b859d030133ab1d56df553e781ff103cf8785`.
- Static source checks passed: 14px override present; 15px override absent; button is created before its append; Widget Settings append is immediately after World Clock append; source and published mirror match exactly. APK remains **1.0.195 / versionCode 194**; no APK rebuild or reinstall is required for this web-only change.
- Physical-phone confirmation of the 14px size and exact on-screen position remains pending. Do not claim device-side PASS until user confirms.

# Physical-device verification — Calendar + Smart Reminder backup/restore (Web Update 362, 2026-11-20)

- User confirmed the Web Update 362 backup/restore test on their Android phone: **“Ha huwa barabar”** (both test records restored correctly).
- Test covered one Personal Calendar entry and one Smart Reminder entry: create both, export `Diary-My-Notes-Backup.json`, then restore it without clearing app data or uninstalling. User confirmed the result was correct.
- **Device-side status: PASS (user-confirmed).** This closes the previously pending physical-phone verification for the Web Update 362 Calendar + Smart Reminder backup/restore change.
- No additional source-code change, APK rebuild, or app-data operation was performed for this verification. Web Update remains **362**; APK remains **1.0.195 / versionCode 194**.
