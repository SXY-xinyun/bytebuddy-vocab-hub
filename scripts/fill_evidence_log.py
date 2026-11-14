# -*- coding: utf-8 -*-
"""Fill Database Evidence Log (1).xlsx from project development history."""
from openpyxl import load_workbook
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
XLSX = ROOT / "Database Evidence Log (1).xlsx"

CHANGE_ROWS = {
    "CL-001": (
        "23/10/2026",
        "v0 → v1",
        "Structure / usability",
        "Added",
        "Created offline ByteBuddy Vocab Hub: embedded data (words.js), Browse and Table views, fields for word, module, pos, phonetic, EN/ZH meanings, example, review_status. Seeded 12 CS vocabulary items across four modules.",
        "The assessment requires a purposeful vocabulary database with clear organisation that markers can open directly from a ZIP.",
        "EV-001, EV-002",
        "A working v1 prototype suitable for BUILD/TEST and further iteration.",
        "Add search and filters (CL-002); capture before/after screenshots.",
    ),
    "CL-002": (
        "23/10/2026",
        "v1 → v2",
        "Data manipulation / usability",
        "Added",
        "Added search (word, definitions, example) and Module + Review status filters on Browse and Table; clear-filters control and empty state when no matches.",
        "The brief requires organising, filtering or manipulating vocabulary data for module-specific study.",
        "EV-003, EV-004",
        "Students can find words by module and review list quickly.",
        "Add review tracking (CL-003).",
    ),
    "CL-003": (
        "23/10/2026",
        "v2 → v3",
        "Learning / review",
        "Added",
        "Added N/L/M buttons on Browse cards to set review status; filters and table use effective status via localStorage overrides.",
        "Fields must support review and daily use without installing a server.",
        "EV-005",
        "Personal review workflow works in the browser; progress is device-specific (limitation for reflection).",
        "Add sort and CSV export (CL-004).",
    ),
    "CL-004": (
        "23/10/2026",
        "v3 → v4",
        "Data manipulation",
        "Added",
        "Added sort options (word, module, review status, word length) and Export CSV on Browse/Table, including effective review status (UTF-8 BOM for Excel).",
        "Further manipulation and backup of data supports portfolio evidence and analysis.",
        "EV-006, EV-007",
        "Vocabulary can be exported and sorted for study planning.",
        "Add visuals and pronunciation support (CL-005).",
    ),
    "CL-005": (
        "23/10/2026",
        "v4 → v5",
        "Fields / usability",
        "Added",
        "Added module SVG icons and Listen button (browser text-to-speech) on vocabulary cards.",
        "Richer multimodal learning without hosting audio files offline.",
        "EV-008, EV-009",
        "More engaging browse experience; TTS quality depends on browser.",
        "Expand to 50+ vocabulary items (CL-006).",
    ),
    "CL-006": (
        "23/10/2026",
        "v5 → v6",
        "Vocabulary quality",
        "Added",
        "Expanded database from 12 to 52 single-word CS entries (13 per module: Programming, AI & ML, Maths & Logic, Lab & Tools) via vocab-extra.js.",
        "The brief requires a minimum of 50 relevant Computer Science vocabulary items.",
        "EV-010, EV-011",
        "Content threshold met; even coverage across modules for filtering demos.",
        "Add dashboard and review mode (CL-007–008).",
    ),
    "CL-007": (
        "23/10/2026",
        "v6 → v6.5",
        "Organisation",
        "Added",
        "Added statistics dashboard on Browse (totals by module and review status) for at-a-glance overview.",
        "Supports pitch demo and understanding database scale during testing.",
        "EV-012",
        "Clear overview of 52 items and module balance.",
        "Add flashcard review mode (CL-008).",
    ),
    "CL-008": (
        "23/10/2026",
        "v6.5 → v1.6",
        "Learning / usability",
        "Added",
        "Added Review flashcard page (filter deck, reveal, prev/next, mark status), unified navigation, and Export review progress (JSON) from Browse.",
        "Demonstrates end-to-end learning workflow for the product pitch.",
        "EV-013, EV-014",
        "Complete study path from browse to review; JSON export supports reflection on progress.",
        "Refine content rules and delivery (CL-009–011).",
    ),
    "CL-009": (
        "23/10/2026",
        "v1.6 → v1.7",
        "Vocabulary quality / usability",
        "Changed",
        "Standardised entries to single words only (no phrases/abbreviations); removed source and date fields from UI/data; all default status New; pure SVG module icons; Review defaults to New deck; Reset all to New button; new localStorage key.",
        "Clearer freshman word list; fixed garbled icons on Windows; Review empty deck issue when filtering Learning only.",
        "EV-015, EV-016, EV-017",
        "Cleaner database aligned with user testing feedback.",
        "Add teacher-friendly launcher (CL-010).",
    ),
    "CL-010": (
        "23/10/2026",
        "v1.7 → v1.8",
        "Usability",
        "Changed",
        "Moved main entry to project root: START HERE - Double-click to Open Website.html; website/index.html redirects; navigation links updated for submission.",
        "Markers must recognise how to open the database from the ZIP without instructions.",
        "EV-018, EV-019",
        "Obvious entry point for teachers and peers.",
        "Adjust Chinese display rules (CL-011).",
    ),
    "CL-011": (
        "23/10/2026",
        "v1.8 → v1.9",
        "Usability / bug fix",
        "Changed",
        "Browse/Table show Chinese prominently; Review hides Chinese until Reveal (then ZH + EN + example); fixed SVG icon paths when opening from root (data-asset-prefix / siteAsset).",
        "Match intended study flow (Chinese reference in browse, self-test in review); fix broken icons from root launcher.",
        "EV-020, EV-021",
        "Icons display correctly; consistent bilingual UX across views.",
        "Continue user testing; add screenshots to Evidence Index files.",
    ),
}

EVIDENCE_ROWS = [
    ("EV-001", "23/10/2026", "Screenshot", "Current", "EV-001_Initial_Browse_v1.png", "Browse view showing first vocabulary cards and module labels (early shell).", "CL-001"),
    ("EV-002", "23/10/2026", "Screenshot", "Current", "EV-002_Initial_Table_v1.png", "Table view showing database columns and structure.", "CL-001"),
    ("EV-003", "23/10/2026", "Screenshot", "Before", "EV-003_Before_Filters.png", "Browse before module/review filters were added (optional if unavailable).", "CL-002"),
    ("EV-004", "23/10/2026", "Screenshot", "After", "EV-004_After_Filters.png", "Browse with Module filter applied and reduced result set.", "CL-002"),
    ("EV-005", "23/10/2026", "Screenshot", "After", "EV-005_Review_Status_LocalStorage.png", "Card with Learning/Mastered mark and filter by Learning.", "CL-003"),
    ("EV-006", "23/10/2026", "Screenshot", "After", "EV-006_Sort_Applied.png", "Browse or Table with sort option applied (e.g. module then word).", "CL-004"),
    ("EV-007", "23/10/2026", "File export", "After", "EV-007_CSV_Export.csv", "CSV exported from database opened in Excel.", "CL-004"),
    ("EV-008", "23/10/2026", "Screenshot", "After", "EV-008_Listen_TTS.png", "Vocabulary card showing Listen button and module icon.", "CL-005"),
    ("EV-009", "23/10/2026", "Screenshot", "Current", "EV-009_Module_SVG_Icons.png", "Four module icon files or cards showing distinct SVG icons.", "CL-005"),
    ("EV-010", "23/10/2026", "Screenshot", "After", "EV-010_Stats_52_Words.png", "Dashboard or footer showing 52 vocabulary items.", "CL-006"),
    ("EV-011", "23/10/2026", "Screenshot", "After", "EV-011_Module_Filter_13.png", "Module filter showing ~13 words in one module.", "CL-006"),
    ("EV-012", "23/10/2026", "Screenshot", "After", "EV-012_Dashboard_Stats.png", "Browse sidebar dashboard with module and status counts.", "CL-007"),
    ("EV-013", "23/10/2026", "Screenshot", "After", "EV-013_Review_Flashcard.png", "Review mode flashcard before Reveal.", "CL-008"),
    ("EV-014", "23/10/2026", "File export", "After", "EV-014_Review_Progress.json", "Exported review progress JSON from Browse.", "CL-008"),
    ("EV-015", "23/10/2026", "Screenshot", "After", "EV-015_Single_Word_Table.png", "Table showing single-word entries and ZH column (no source/date).", "CL-009"),
    ("EV-016", "23/10/2026", "Screenshot", "After", "EV-016_Review_New_Deck.png", "Review page with New deck showing cards (not empty).", "CL-009"),
    ("EV-017", "23/10/2026", "Screenshot", "After", "EV-017_Pure_SVG_Icons.png", "Module icons rendering correctly (not garbled).", "CL-009"),
    ("EV-018", "23/10/2026", "Screenshot", "Current", "EV-018_START_HERE_File.png", "Project folder showing START HERE - Double-click to Open Website.html.", "CL-010"),
    ("EV-019", "23/10/2026", "Screenshot", "After", "EV-019_Open_From_START.png", "Website opened from root START file in browser.", "CL-010"),
    ("EV-020", "23/10/2026", "Screenshot", "After", "EV-020_Browse_Chinese_Prominent.png", "Browse card with Chinese meaning above English definition.", "CL-011"),
    ("EV-021", "23/10/2026", "Screenshot", "After", "EV-021_Review_After_Reveal.png", "Review card after Reveal showing Chinese + English + example.", "CL-011"),
]


def main():
    wb = load_workbook(XLSX)
    cl = wb["Change Log"]
    for entry_id, values in CHANGE_ROWS.items():
        for row in range(2, cl.max_row + 1):
            if cl.cell(row, 1).value == entry_id:
                for col, val in enumerate(values, start=2):
                    cl.cell(row, col, val)
                break
        else:
            raise SystemExit(f"Row not found for {entry_id}")

    ev = wb["Evidence Index"]
    start_row = 3  # row 2 is template example; overwrite from row 3
    for i, row_data in enumerate(EVIDENCE_ROWS):
        r = start_row + i
        for col, val in enumerate(row_data, start=1):
            ev.cell(r, col, val)

    wb.save(XLSX)
    print("Saved", XLSX, "—", len(CHANGE_ROWS), "CL entries,", len(EVIDENCE_ROWS), "EV entries")


if __name__ == "__main__":
    main()
