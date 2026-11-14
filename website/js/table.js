const tableState = {
  search: "",
  module: "",
  reviewStatus: "",
  sort: "word-asc",
};

const TABLE_SORT_KEYS = {
  word: "word-asc",
  module: "module-asc",
};

function bindTableFilters() {
  const searchEl = document.getElementById("search");
  const moduleEl = document.getElementById("filter-module");
  const reviewEl = document.getElementById("filter-review");
  const sortEl = document.getElementById("filter-sort");

  searchEl.addEventListener("input", () => {
    tableState.search = searchEl.value;
    renderTable();
  });
  moduleEl.addEventListener("change", () => {
    tableState.module = moduleEl.value;
    renderTable();
  });
  reviewEl.addEventListener("change", () => {
    tableState.reviewStatus = reviewEl.value;
    renderTable();
  });
  if (sortEl) {
    sortEl.addEventListener("change", () => {
      tableState.sort = sortEl.value;
      renderTable();
    });
  }

  document.getElementById("btn-clear-filters").addEventListener("click", () => {
    tableState.search = "";
    tableState.module = "";
    tableState.reviewStatus = "";
    tableState.sort = "word-asc";
    searchEl.value = "";
    moduleEl.value = "";
    reviewEl.value = "";
    if (sortEl) sortEl.value = "word-asc";
    renderTable();
  });

  const exportBtn = document.getElementById("btn-export-csv");
  if (exportBtn) {
    exportBtn.addEventListener("click", () => {
      const rows = sortVocabulary(
        filterVocabulary(VOCABULARY, tableState),
        tableState.sort
      );
      exportVocabularyCsv(rows, "bytebuddy_vocab_table");
    });
  }

  document.querySelectorAll("[data-sort-key]").forEach((th) => {
    th.addEventListener("click", () => {
      const key = th.dataset.sortKey;
      if (TABLE_SORT_KEYS[key]) {
        tableState.sort = TABLE_SORT_KEYS[key];
        if (sortEl) sortEl.value = tableState.sort;
        renderTable();
      }
    });
  });
}

function renderTable() {
  const filtered = sortVocabulary(
    filterVocabulary(VOCABULARY, tableState),
    tableState.sort
  );
  const tbody = document.getElementById("vocab-tbody");
  const countEl = document.getElementById("table-count");

  countEl.textContent = `${filtered.length} row(s) · sorted`;

  tbody.innerHTML = filtered
    .map((entry) => {
      const status = getEffectiveReviewStatus(entry);
      const overridden =
        status !== entry.review_status
          ? ' title="Status saved in this browser (localStorage)"'
          : "";
      const img = `<img class="table-thumb" src="${escapeHtml(entryImageUrl(entry))}" alt="" loading="lazy" /> `;
      return `
        <tr>
          <td class="col-word">${img}<strong>${escapeHtml(entry.word)}</strong></td>
          <td>${escapeHtml(entry.module)}</td>
          <td>${escapeHtml(entry.pos)}</td>
          <td class="col-phonetic">${escapeHtml(entry.phonetic)}</td>
          <td class="col-zh col-zh-emphasis">${escapeHtml(entry.zh_meaning)}</td>
          <td class="col-en">${escapeHtml(entry.en_definition)}${entry.source_apa ? `<br /><span class="source-apa">${escapeHtml(entry.source_apa)}</span>` : ""}</td>
          <td class="col-example">${escapeHtml(entry.example)}</td>
          <td><span class="review-badge ${reviewStatusClass(status)}"${overridden}>${escapeHtml(status)}</span></td>
        </tr>`;
    })
    .join("");
}

document.addEventListener("DOMContentLoaded", () => {
  bindTableFilters();
  renderTable();
});
