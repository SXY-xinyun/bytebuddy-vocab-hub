# Database development log (project copy)

Use with **Database Evidence Log (1).xlsx**. Copy rows into **Change Log** and link **Evidence ID(s)** after screenshots.

**Current database version:** `VOCAB_DB_VERSION = v2.0` · **52 vocabulary entries** (single word each, APA 7 `source_apa`)

**Teacher entry point:** `START HERE - Double-click to Open Website.html` (project root)

---

## CL-001 — Initial vocabulary database & static website shell

| Field | Content |
|--------|---------|
| **Date** | 23 Oct 2026 |
| **Version** | v0 → v1 |
| **Change category** | Structure / usability |
| **Change type** | Added |
| **What changed?** | Offline **ByteBuddy Vocab Hub**: `words.js`, Browse + Table views, MVP fields (word, module, pos, phonetic, en_definition, zh_meaning, example, review_status, date_added, source_apa). **12** seed entries across four modules. |
| **Why did you change it?** | Assessment needs a purposeful, openable vocabulary database with clear structure. |
| **Evidence ID(s)** | EV-001, EV-002 |
| **Result / impact** | Working prototype for BUILD/TEST cycle. |
| **Next step** | Filters and review features (CL-002–003). |

---

## CL-002 — Search and data manipulation filters

| Field | Content |
|--------|---------|
| **Date** | 23 Oct 2026 |
| **Version** | v1 → v2 |
| **Change category** | Data manipulation / usability |
| **Change type** | Added |
| **What changed?** | Search plus **Module** and **Review status** filters on Browse and Table; clear filters; empty state. |
| **Why did you change it?** | Brief requires filtering/manipulating data for module-specific study. |
| **Evidence ID(s)** | EV-004, EV-005 |
| **Result / impact** | Targeted word lists for review sessions. |
| **Next step** | Review tracking (CL-003). |

---

## CL-003 — Review progress via localStorage

| Field | Content |
|--------|---------|
| **Date** | 23 Oct 2026 |
| **Version** | v2 → v3 |
| **Change category** | Learning / review |
| **Change type** | Added |
| **What changed?** | N/L/M buttons on cards; effective status in filters and table; browser-only overrides. |
| **Why did you change it?** | Support **review** and **use** without a backend. |
| **Evidence ID(s)** | EV-006 |
| **Result / impact** | Personal progress tracking; device-specific (note in reflection). |
| **Next step** | Sort/export (CL-004). |

---

## CL-004 — Sort options and CSV export

| Field | Content |
|--------|---------|
| **Date** | 23 Oct 2026 |
| **Version** | v3 → v4 |
| **Change category** | Data manipulation |
| **Change type** | Added |
| **What changed?** | Sort dropdown (word, module, date, review status); clickable table headers; **Export CSV** on Browse/Table (includes effective review status); UTF-8 BOM for Excel. |
| **Why did you change it?** | Further data manipulation for analysis, backup, and portfolio evidence. |
| **Evidence ID(s)** | EV-007 (sort applied), EV-008 (downloaded CSV open in Excel) |
| **Result / impact** | Data portable outside the website; supports reflection on workflow. |
| **Next step** | Media + pronunciation (CL-005). |

---

## CL-005 — Visual icons and listen (TTS) support

| Field | Content |
|--------|---------|
| **Date** | 23 Oct 2026 |
| **Version** | v4 → v5 |
| **Change category** | Fields / usability |
| **Change type** | Added |
| **What changed?** | Optional `image_url` in schema; default **module SVG icons** in `assets/images/`; **Listen** button using browser speech synthesis on cards and flashcards. |
| **Why did you change it?** | Richer entries (visual + audio) for understanding; offline-friendly without hosting MP3 files. |
| **Evidence ID(s)** | EV-009 (card with icon + Listen), EV-010 (module icons folder) |
| **Result / impact** | More engaging study experience; TTS quality varies by browser (limitation for pitch). |
| **Next step** | Expand content to 50+ (CL-006). |

---

## CL-006 — Expand vocabulary to 52 items (50+ requirement)

| Field | Content |
|--------|---------|
| **Date** | 23 Oct 2026 |
| **Version** | v5 → v6 |
| **Change category** | Vocabulary quality |
| **Change type** | Added |
| **What changed?** | Added **40** entries in `vocab-extra.js` merged into `VOCABULARY` (**13 per module**, 52 total). Each includes EN/ZH, example, APA `source_apa`. |
| **Why did you change it?** | Brief minimum **50** CS-relevant items; even coverage across Programming, AI & ML, Maths & Logic, Lab & Tools. |
| **Evidence ID(s)** | EV-011 (table row count / stats dashboard showing 52), EV-012 (module filter showing ~13 each) |
| **Result / impact** | Database meets content threshold; ready for sustained personal testing. |
| **Next step** | Study features and references page (CL-007–008). |

---

## CL-007 — Dashboard stats and References page

| Field | Content |
|--------|---------|
| **Date** | 23 Oct 2026 |
| **Version** | v6 → v6.5 |
| **Change category** | Organisation / academic integrity |
| **Change type** | Added |
| **What changed?** | Browse **dashboard** (totals by module and review status); **references.html** listing unique APA sources from the database. |
| **Why did you change it?** | Quick overview for pitch; centralised references for APA portfolio requirement. |
| **Evidence ID(s)** | EV-013 (dashboard), EV-014 (References page) |
| **Result / impact** | Clearer database overview; easier integrity compliance. |
| **Next step** | Dedicated review mode (CL-008). |

---

## CL-008 — Flashcard review mode + export review JSON

| Field | Content |
|--------|---------|
| **Date** | 23 Oct 2026 |
| **Version** | v6.5 → **v1.6** |
| **Change category** | Learning / usability |
| **Change type** | Added |
| **What changed?** | **review.html** flashcard deck (filter by module + status, reveal, prev/next, mark N/L/M); unified nav (Browse, Table, Review, References); **Export review progress** JSON from Browse; version footer `v1.6`. |
| **Why did you change it?** | Pitch demo for “how freshmen review daily”; partial answer to localStorage sync limitation. |
| **Evidence ID(s)** | EV-015 (Review mode), EV-016 (export JSON) |
| **Result / impact** | End-to-end learning workflow; JSON export documents personal overrides for reflection. |
| **Next step** | User testing with classmates; optional future: MP3 per word, cloud sync, print flashcards. |

---

## CL-012 — APA 7 sources, vocabulary Excel, evidence file exports

| Field | Content |
|--------|---------|
| **Date** | 24 Oct 2026 |
| **Version** | v1.9 → **v2.0** |
| **Change category** | Academic integrity / data export |
| **Change type** | Added |
| **What changed?** | `source_apa` on all 52 entries; small-type Source (APA 7) on Browse/Table/Review; **`ByteBuddy_Vocabulary_Database.xlsx`**; **`evidence/file_exports/`** (EV-007 CSV, EV-014 JSON); automated screenshots (Playwright) for key EV PNGs; Excel Evidence Log paths updated. |
| **Why did you change it?** | Portfolio requires APA referencing and verifiable exports; Evidence Index must link real files. |
| **Evidence ID(s)** | EV-007, EV-014, EV-024, EV-002, EV-004, EV-012, EV-013, EV-015, EV-021 |
| **Result / impact** | Submittable evidence bundle; teachers can read full database in Excel. |
| **Next step** | Personalise reflection; record pitch from `PITCH_SCRIPT_5min.md`. |

---

## CL-011 — Chinese on Browse/Table; Review reveal; SVG path fix

| Field | Content |
|--------|---------|
| **Date** | 23 Oct 2026 |
| **Version** | v1.8 → **v1.9** |
| **Change category** | Usability / bug fix |
| **Change type** | Changed |
| **What changed?** | **Browse**: Chinese meaning shown prominently above English. **Table**: ZH column moved before EN, labelled 中文. **Review**: Chinese hidden until **Reveal** (then ZH + EN + example). Fixed module **SVG icons** when opening from root via `data-asset-prefix="website/"` and `siteAsset()`. |
| **Why did you change it?** | Match intended study flow; icons broke because asset paths were relative to `website/` only. |
| **Evidence ID(s)** | EV-022 (icons on START page), EV-023 (Review before/after Reveal) |
| **Result / impact** | Consistent Chinese visibility; icons load from root launcher. |
| **Next step** | Ctrl+F5 refresh after update. |

---

## CL-010 — Root launcher + Chinese-first flashcards

| Field | Content |
|--------|---------|
| **Date** | 23 Oct 2026 |
| **Version** | v1.7 → **v1.8** |
| **Change category** | Usability / learning |
| **Change type** | Changed |
| **What changed?** | Moved main Browse page to **`START HERE - Double-click to Open Website.html`** at project root; `website/index.html` redirects; nav links updated. Review flashcards now show **Chinese meaning immediately**; Reveal adds English definition + example. |
| **Why did you change it?** | Teachers must recognise the entry file instantly; beginners need Chinese gloss while learning English headwords. |
| **Evidence ID(s)** | EV-020 (root START file), EV-021 (Review with Chinese visible before reveal) |
| **Result / impact** | Clearer submission layout; gentler learning curve in Review mode. |
| **Next step** | Zip portfolio with START file visible at top level. |

---

## CL-009 — Content rules, icons fix, Review defaults (user feedback)

| Field | Content |
|--------|---------|
| **Date** | 23 Oct 2026 |
| **Version** | v1.6 → **v1.7** |
| **Change category** | Vocabulary quality / usability |
| **Change type** | Changed |
| **What changed?** | Replaced multi-word entries and abbreviations (e.g. API, IDE, neural network) with **single-word** terms; removed **source_apa** and **date_added** from data and UI/CSV; all entries default **review_status: New**; module icons redrawn as **pure SVG** (no emoji in SVG — fixes garbled icon on Windows); Review page defaults to **New** deck; removed References from nav; **Reset all to New** button; new localStorage key so old progress does not carry over. |
| **Why did you change it?** | Clearer study list for freshmen; icons must render offline on all systems; empty Review screen was confusing when deck filtered to Learning only. |
| **Evidence ID(s)** | EV-017 (icons), EV-018 (table without source/date), EV-019 (Review shows New deck) |
| **Result / impact** | Cleaner database; Review mode works on first visit; user controls when words leave New. |
| **Next step** | Personal testing; screenshots for portfolio. |

---

## Evidence index quick map

| ID | Suggested capture |
|----|-------------------|
| EV-001 | Early scaffold (if available) |
| EV-002–003 | Browse + Table baseline |
| EV-004–005 | Filters before/after |
| EV-006 | Review status change + filter |
| EV-007–008 | Sort + CSV in Excel |
| EV-009–010 | Listen + module icons |
| EV-011–012 | 52 words / per-module counts |
| EV-013–014 | Dashboard + References |
| EV-015–016 | Flashcard review + JSON export |

---

## References (portfolio)

Unique sources are auto-listed on `website/references.html`. Copy into your 1000-word reflection References section.
