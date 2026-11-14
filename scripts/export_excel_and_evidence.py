# -*- coding: utf-8 -*-
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DUMP = ROOT / "vocab_dump.json"
XLSX = ROOT / "ByteBuddy_Vocabulary_Database.xlsx"
FILES = ROOT / "evidence" / "file_exports"

FIELDS = [
    "id", "word", "module", "pos", "phonetic",
    "en_definition", "zh_meaning", "example", "review_status", "source_apa",
]


def main():
    entries = json.loads(DUMP.read_text(encoding="utf-8"))
    print("Loaded", len(entries), "entries")

    from openpyxl import Workbook
    from openpyxl.styles import Font, Alignment

    wb = Workbook()
    ws = wb.active
    ws.title = "Vocabulary"
    ws.append(FIELDS)
    for c in ws[1]:
        c.font = Font(bold=True)
    for e in sorted(entries, key=lambda x: (x["module"], x["word"])):
        ws.append([e.get(k, "") for k in FIELDS])
    for row in ws.iter_rows(min_row=2, max_row=ws.max_row):
        for cell in row:
            cell.alignment = Alignment(wrap_text=True, vertical="top")
    ws.column_dimensions["F"].width = 42
    ws.column_dimensions["G"].width = 38
    ws.column_dimensions["J"].width = 55
    wb.save(XLSX)
    print("Excel:", XLSX)

    FILES.mkdir(parents=True, exist_ok=True)
    csv_path = FILES / "EV-007_CSV_Export.csv"
    with csv_path.open("w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, extrasaction="ignore")
        w.writeheader()
        for e in sorted(entries, key=lambda x: x["word"]):
            w.writerow(e)
    print("CSV:", csv_path)

    json_path = FILES / "EV-014_Review_Progress.json"
    json_path.write_text(
        json.dumps(
            {
                "exported": "2026-10-24T12:00:00.000Z",
                "note": "Sample export; overrides empty at initial state.",
                "overrides": {},
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    print("JSON:", json_path)


if __name__ == "__main__":
    main()
