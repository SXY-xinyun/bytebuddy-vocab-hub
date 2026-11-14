function uniqueSources(entries) {
  const seen = new Set();
  const list = [];
  entries.forEach((e) => {
    const s = (e.source_apa || "").trim();
    if (!s || seen.has(s)) return;
    seen.add(s);
    list.push(s);
  });
  return list.sort((a, b) => a.localeCompare(b));
}

document.addEventListener("DOMContentLoaded", () => {
  const ol = document.getElementById("references-list");
  const count = document.getElementById("ref-count");
  if (!ol) return;
  const sources = uniqueSources(VOCABULARY);
  count.textContent = `${sources.length} unique source(s) for ${VOCABULARY.length} entries`;
  ol.innerHTML = sources
    .map((s, i) => `<li id="ref-${i + 1}">${escapeHtml(s)}</li>`)
    .join("");
});
