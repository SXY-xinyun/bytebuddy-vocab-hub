const SORT_OPTIONS = {
  "word-asc": { label: "Word (A → Z)", fn: (a, b) => a.word.localeCompare(b.word) },
  "word-desc": { label: "Word (Z → A)", fn: (a, b) => b.word.localeCompare(a.word) },
  "module-asc": {
    label: "Module, then word",
    fn: (a, b) =>
      a.module.localeCompare(b.module) || a.word.localeCompare(b.word),
  },
  "date-desc": {
    label: "Word length",
    fn: (a, b) => a.word.length - b.word.length || a.word.localeCompare(b.word),
  },
  "status-group": {
    label: "Review status",
    fn: (a, b) => {
      const order = { New: 0, Learning: 1, Mastered: 2 };
      const sa = order[getEffectiveReviewStatus(a)] ?? 9;
      const sb = order[getEffectiveReviewStatus(b)] ?? 9;
      return sa - sb || a.word.localeCompare(b.word);
    },
  },
};

function sortVocabulary(entries, sortKey) {
  const spec = SORT_OPTIONS[sortKey] || SORT_OPTIONS["word-asc"];
  return [...entries].sort(spec.fn);
}

function csvEscape(value) {
  const s = String(value ?? "").replace(/"/g, '""');
  return `"${s}"`;
}

function vocabularyToCsv(entries) {
  const headers = [
    "word",
    "module",
    "pos",
    "phonetic",
    "en_definition",
    "zh_meaning",
    "example",
    "review_status",
    "review_status_effective",
    "source_apa",
  ];
  const rows = entries.map((e) =>
    [
      e.word,
      e.module,
      e.pos,
      e.phonetic,
      e.en_definition,
      e.zh_meaning,
      e.example,
      e.review_status,
      getEffectiveReviewStatus(e),
      e.source_apa || "",
    ]
      .map(csvEscape)
      .join(",")
  );
  return [headers.join(","), ...rows].join("\r\n");
}

function exportVocabularyCsv(entries, filenamePrefix) {
  const stamp = new Date().toISOString().slice(0, 10);
  downloadTextFile(
    `${filenamePrefix}_${stamp}.csv`,
    vocabularyToCsv(entries),
    "text/csv;charset=utf-8"
  );
}
