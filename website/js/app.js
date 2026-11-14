const state = {
  search: "",
  module: "",
  reviewStatus: "",
  sort: "word-asc",
};

function bindFilters() {
  const searchEl = document.getElementById("search");
  const moduleEl = document.getElementById("filter-module");
  const reviewEl = document.getElementById("filter-review");

  searchEl.addEventListener("input", () => {
    state.search = searchEl.value;
    renderBrowse();
  });

  moduleEl.addEventListener("change", () => {
    state.module = moduleEl.value;
    renderBrowse();
  });

  reviewEl.addEventListener("change", () => {
    state.reviewStatus = reviewEl.value;
    renderBrowse();
  });

  const sortEl = document.getElementById("filter-sort");
  if (sortEl) {
    sortEl.addEventListener("change", () => {
      state.sort = sortEl.value;
      renderBrowse();
    });
  }

  const exportBtn = document.getElementById("btn-export-csv");
  if (exportBtn) {
    exportBtn.addEventListener("click", () => {
      const filtered = sortVocabulary(filterVocabulary(VOCABULARY, state), state.sort);
      exportVocabularyCsv(filtered, "bytebuddy_vocab_export");
    });
  }

  document.getElementById("btn-clear-filters").addEventListener("click", () => {
    state.search = "";
    state.module = "";
    state.reviewStatus = "";
    searchEl.value = "";
    moduleEl.value = "";
    reviewEl.value = "";
    renderBrowse();
    searchEl.focus();
  });
}

function renderStats(filtered, total) {
  const el = document.getElementById("result-stats");
  el.textContent =
    filtered.length === total
      ? `${total} words in your hub`
      : `Showing ${filtered.length} of ${total} words`;
}

function renderCards(entries) {
  const grid = document.getElementById("card-grid");
  const empty = document.getElementById("empty-state");

  if (entries.length === 0) {
    grid.innerHTML = "";
    empty.hidden = false;
    return;
  }

  empty.hidden = true;
  grid.innerHTML = entries
    .map((entry, index) => {
      const status = getEffectiveReviewStatus(entry);
      const delay = Math.min(index * 0.04, 0.48);
      const img = entryImageUrl(entry);
      return `
        <article class="vocab-card pop-in" style="animation-delay: ${delay}s" data-id="${escapeHtml(entry.id)}">
          <div class="card-media">
            <img class="card-icon" src="${escapeHtml(img)}" alt="" width="56" height="56" loading="lazy" />
            <button type="button" class="btn-listen" data-speak="${escapeHtml(entry.word)}" title="Listen (browser TTS)">🔊 Listen</button>
          </div>
          <header class="card-head">
            <div>
              <h2 class="card-word">${escapeHtml(entry.word)}</h2>
              <p class="card-meta">${escapeHtml(entry.pos)} · ${escapeHtml(entry.phonetic)}</p>
            </div>
            <span class="module-pill">${escapeHtml(entry.module)}</span>
          </header>
          <p class="card-zh card-zh-primary">${escapeHtml(entry.zh_meaning)}</p>
          <p class="card-en">${escapeHtml(entry.en_definition)}</p>
          ${entry.source_apa ? `<p class="source-apa">Source (APA 7): ${escapeHtml(entry.source_apa)}</p>` : ""}
          <blockquote class="card-example">“${escapeHtml(entry.example)}”</blockquote>
          <footer class="card-foot">
            <span class="review-badge ${reviewStatusClass(status)}">${escapeHtml(status)}</span>
            <div class="review-actions" role="group" aria-label="Update review status">
              ${REVIEW_STATUSES.map(
                (s) =>
                  `<button type="button" class="review-btn ${s === status ? "is-active" : ""}" data-status="${s}" data-id="${escapeHtml(entry.id)}" title="Mark as ${s}">${s.charAt(0)}</button>`
              ).join("")}
            </div>
          </footer>
        </article>
      `;
    })
    .join("");

  bindSpeakButtons(grid);

  grid.querySelectorAll(".review-btn").forEach((btn) => {
    btn.addEventListener("click", () => {
      const id = btn.dataset.id;
      const status = btn.dataset.status;
      const entry = VOCABULARY.find((e) => e.id === id);
      if (!entry) return;
      if (status === entry.review_status) {
        clearReviewOverride(id);
      } else {
        setReviewOverride(id, status);
      }
      renderBrowse();
    });
  });
}

function renderBrowse() {
  const filtered = sortVocabulary(
    filterVocabulary(VOCABULARY, state),
    state.sort
  );
  renderStats(filtered, VOCABULARY.length);
  renderCards(filtered);
  if (typeof renderDashboard === "function") renderDashboard();
}

function initMascot() {
  const mascot = document.querySelector(".mascot");
  if (!mascot) return;
  mascot.addEventListener("click", () => {
    mascot.classList.remove("wiggle");
    void mascot.offsetWidth;
    mascot.classList.add("wiggle");
  });
}

document.addEventListener("DOMContentLoaded", () => {
  bindFilters();
  renderBrowse();
  initMascot();
});
