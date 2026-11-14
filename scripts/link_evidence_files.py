# -*- coding: utf-8 -*-
from openpyxl import load_workbook
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
wb = load_workbook(ROOT / "Database Evidence Log (1).xlsx")
ev = wb["Evidence Index"]

links = {
    "EV-002": "evidence/screenshots/EV-002_Initial_Browse.png",
    "EV-004": "evidence/screenshots/EV-004_After_Filters.png",
    "EV-007": "evidence/file_exports/EV-007_CSV_Export.csv",
    "EV-012": "evidence/screenshots/EV-012_Dashboard_Stats.png",
    "EV-013": "evidence/screenshots/EV-013_Review_Flashcard.png",
    "EV-014": "evidence/file_exports/EV-014_Review_Progress.json",
    "EV-015": "evidence/screenshots/EV-015_Single_Word_Table.png",
    "EV-021": "evidence/screenshots/EV-021_Review_After_Reveal.png",
    "EV-024": "ByteBuddy_Vocabulary_Database.xlsx",
}

for row in range(2, ev.max_row + 1):
    eid = ev.cell(row, 1).value
    if eid in links:
        ev.cell(row, 5, links[eid])

wb.save(ROOT / "Database Evidence Log (1).xlsx")
print("Linked", len(links), "evidence files in Excel")
