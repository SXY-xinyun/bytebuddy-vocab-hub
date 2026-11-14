const MODULES = ["Programming", "AI & ML", "Maths & Logic", "Lab & Tools"];

/** Prefix for assets when the entry HTML lives in the project root (website/ subfolder). */
function siteAsset(relativePath) {
  const prefix = document.body?.dataset?.assetPrefix || "";
  const path = relativePath.replace(/^\//, "");
  return prefix + path;
}

function normalizeQuery(q) {
  return q.trim().toLowerCase();
}

function entryMatchesSearch(entry, query) {
  if (!query) return true;
  const haystack = [
    entry.word,
    entry.en_definition,
    entry.zh_meaning,
    entry.example,
    entry.module,
    entry.pos,
  ]
    .join(" ")
    .toLowerCase();
  return haystack.includes(query);
}

function filterVocabulary(entries, { search, module, reviewStatus }) {
  const q = normalizeQuery(search);
  return entries.filter((entry) => {
    if (module && entry.module !== module) return false;
    const effective = getEffectiveReviewStatus(entry);
    if (reviewStatus !== undefined && reviewStatus !== "" && effective !== reviewStatus)
      return false;
    return entryMatchesSearch(entry, q);
  });
}

function countByModule(entries) {
  const counts = Object.fromEntries(MODULES.map((m) => [m, 0]));
  entries.forEach((e) => {
    if (counts[e.module] !== undefined) counts[e.module]++;
  });
  return counts;
}

function escapeHtml(text) {
  const div = document.createElement("div");
  div.textContent = text;
  return div.innerHTML;
}

function downloadTextFile(filename, content, mime) {
  const blob = new Blob(["\ufeff" + content], { type: mime });
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = filename;
  a.click();
  URL.revokeObjectURL(url);
}

function formatDate(iso) {
  try {
    return new Date(iso + "T12:00:00").toLocaleDateString("en-GB", {
      day: "numeric",
      month: "short",
      year: "numeric",
    });
  } catch {
    return iso;
  }
}
