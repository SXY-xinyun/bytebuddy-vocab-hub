Evidence folder (Portfolio Part 1)
==================================

screenshots/     PNG files captured from the live website (see filenames).
file_exports/    EV-007 CSV export and EV-014 review JSON (real exports).

Also at project root:
  ByteBuddy_Vocabulary_Database.xlsx  — full 52-word database + APA 7 sources
  Database Evidence Log (1).xlsx      — Change Log + Evidence Index (linked paths)

To refresh exports:
  cd scripts
  node dump_vocab.mjs
  python export_excel_and_evidence.py
  python capture_screenshots.py   (requires local: python -m http.server 8765)
