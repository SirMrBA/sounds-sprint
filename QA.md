# Verification · 14 October 2026

Content is based on the 30 supplied PDFs (286 pages). The course outline and Moodle export establish the resit date and the requirement to pass both parts. Coloured answer slides in the wrap-up were rendered to verify the minimal-pair, true-statement and compound-stress solutions. The IPA source diagrams and both cheat-sheet pages were visually inspected.

Browser checks use Playwright with the existing `chrome-headless-shell` binary. The installed desktop browsers are not used for automation.

The integration checks cover data counts and unique answer choices; lesson search; the IPA explorer; flashcard ratings, due/weak queues and persistence; quiz scoring and mistake repair; word-key comparison and IPA cursor insertion; separate RP/GA drafts; all mock fields, timer persistence, accent locking and review; progress export/import; responsive overflow checks; larger text; reduced motion; and offline reloads.

Visual checks include desktop, tablet and phone layouts, the IPA map, exam review and both PDF pages. This is browser emulation, not a physical iPad or iPhone test. External dictionary audio is linked, not hosted or validated as the exact classroom accent. The trainer cannot grade an open transcription as an examiner would, so those tasks remain explicitly self-reviewed.

Result: 15 integration check groups passed; no JavaScript exceptions. No page-level horizontal overflow at 320, 390, 600, 834 or 1440 px. The 2-page PDF also passed word bounding-box checks (no text outside the page).
