# -*- coding: utf-8 -*-
from openpyxl import load_workbook
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
wb = load_workbook(ROOT / "Database Evidence Log (1).xlsx")
ev = wb["Evidence Index"]

path_updates = {
    "EV-007": "evidence/file_exports/EV-007_CSV_Export.csv",
    "EV-014": "evidence/file_exports/EV-014_Review_Progress.json",
}

for row in range(2, ev.max_row + 1):
    eid = ev.cell(row, 1).value
    if eid in path_updates:
        ev.cell(row, 5, path_updates[eid])

# Add CL-012 row if empty CL-012 exists
cl = wb["Change Log"]
for row in range(2, cl.max_row + 1):
    if cl.cell(row, 1).value == "CL-012" and cl.cell(row, 2).value is None:
        cl.cell(row, 2, "24/10/2026")
        cl.cell(row, 3, "v1.9 → v2.0")
        cl.cell(row, 4, "Fields / academic integrity")
        cl.cell(row, 5, "Added")
        cl.cell(row, 6, "Added APA 7 source_apa field to all 52 entries; small-type Source line on Browse/Table/Review; exported ByteBuddy_Vocabulary_Database.xlsx and evidence file_exports (CSV, JSON).")
        cl.cell(row, 7, "Brief requires APA referencing; Excel backup supports portfolio and marking.")
        cl.cell(row, 8, "EV-007, EV-014, EV-024")
        cl.cell(row, 9, "Traceable definitions and separate vocabulary spreadsheet for teachers.")
        cl.cell(row, 10, "Complete screenshot folder evidence/screenshots/.")
        break

# EV-024 for excel
for row in range(2, ev.max_row + 1):
    if ev.cell(row, 1).value == "EV-024":
        ev.cell(row, 2, "24/10/2026")
        ev.cell(row, 3, "File export")
        ev.cell(row, 4, "Current")
        ev.cell(row, 5, "ByteBuddy_Vocabulary_Database.xlsx")
        ev.cell(row, 6, "Full vocabulary database export with APA sources.")
        ev.cell(row, 7, "CL-012")
        break
else:
    # find first empty EV row
    for row in range(2, ev.max_row + 1):
        if str(ev.cell(row, 1).value or "").startswith("EV-") and ev.cell(row, 2).value is None:
            ev.cell(row, 1, "EV-024")
            ev.cell(row, 2, "24/10/2026")
            ev.cell(row, 3, "File export")
            ev.cell(row, 4, "Current")
            ev.cell(row, 5, "ByteBuddy_Vocabulary_Database.xlsx")
            ev.cell(row, 6, "Full vocabulary database export with APA sources.")
            ev.cell(row, 7, "CL-012")
            break

wb.save(ROOT / "Database Evidence Log (1).xlsx")
print("Updated evidence paths and CL-012")
