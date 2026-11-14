function countByReviewStatus(entries) {
  const counts = { New: 0, Learning: 0, Mastered: 0 };
  entries.forEach((e) => {
    const s = getEffectiveReviewStatus(e);
    if (counts[s] !== undefined) counts[s]++;
  });
  return counts;
}

function renderDashboard() {
  const el = document.getElementById("dashboard-stats");
  if (!el) return;

  const total = VOCABULARY.length;
  const byModule = countByModule(VOCABULARY);
  const byReview = countByReviewStatus(VOCABULARY);

  el.innerHTML = `
    <div class="dash-grid">
      <div class="dash-card"><span class="dash-num">${total}</span><span class="dash-label">Total words</span></div>
      ${MODULES.map(
        (m) =>
          `<div class="dash-card dash-module"><span class="dash-num">${byModule[m]}</span><span class="dash-label">${escapeHtml(m)}</span></div>`
      ).join("")}
      ${REVIEW_STATUSES.map(
        (s) =>
          `<div class="dash-card"><span class="dash-num">${byReview[s]}</span><span class="dash-label">${s}</span></div>`
      ).join("")}
    </div>`;
}
