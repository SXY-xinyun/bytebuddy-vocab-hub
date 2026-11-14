let deck = [];
let index = 0;
let revealed = false;

function buildReviewDeck() {
  const module = document.getElementById("review-module")?.value || "";
  const status = document.getElementById("review-status")?.value ?? "New";
  deck = sortVocabulary(
    filterVocabulary(VOCABULARY, {
      search: "",
      module,
      reviewStatus: status,
    }),
    "word-asc"
  );
  index = 0;
  revealed = false;
  renderFlashcard();
}

function renderFlashcard() {
  const card = document.getElementById("flashcard");
  const meta = document.getElementById("flash-meta");
  const empty = document.getElementById("review-empty");
  if (!card) return;

  if (deck.length === 0) {
    card.hidden = true;
    empty.hidden = false;
    meta.textContent = "0 cards";
    return;
  }

  card.hidden = false;
  empty.hidden = true;
  const entry = deck[index];
  meta.textContent = `Card ${index + 1} of ${deck.length} · ${entry.module}`;

  const img = entryImageUrl(entry);
  card.innerHTML = `
    <img class="flash-icon" src="${escapeHtml(img)}" alt="" width="72" height="72" />
    <h2 class="flash-word">${escapeHtml(entry.word)}</h2>
    <p class="flash-phonetic">${escapeHtml(entry.phonetic)}</p>
    <button type="button" class="btn-listen" data-speak="${escapeHtml(entry.word)}">🔊</button>
    <div class="flash-body ${revealed ? "is-revealed" : ""}">
      ${
        revealed
          ? `<p class="card-zh flash-zh-reveal">${escapeHtml(entry.zh_meaning)}</p>
             <p class="card-en">${escapeHtml(entry.en_definition)}</p>
             ${entry.source_apa ? `<p class="source-apa">Source (APA 7): ${escapeHtml(entry.source_apa)}</p>` : ""}
             <blockquote class="card-example">“${escapeHtml(entry.example)}”</blockquote>`
          : `<p class="flash-hint">Tap “Reveal” to show Chinese meaning, English definition &amp; example</p>`
      }
    </div>
  `;
  bindSpeakButtons(card);
}

function bindReviewControls() {
  document.getElementById("review-module")?.addEventListener("change", buildReviewDeck);
  document.getElementById("review-status")?.addEventListener("change", buildReviewDeck);

  document.getElementById("btn-reveal")?.addEventListener("click", () => {
    revealed = true;
    renderFlashcard();
  });

  document.getElementById("btn-prev")?.addEventListener("click", () => {
    if (deck.length === 0) return;
    index = (index - 1 + deck.length) % deck.length;
    revealed = false;
    renderFlashcard();
  });

  document.getElementById("btn-next")?.addEventListener("click", () => {
    if (deck.length === 0) return;
    index = (index + 1) % deck.length;
    revealed = false;
    renderFlashcard();
  });

  document.querySelectorAll("[data-mark-review]").forEach((btn) => {
    btn.addEventListener("click", () => {
      const entry = deck[index];
      if (!entry) return;
      const status = btn.dataset.markReview;
      if (status === entry.review_status) clearReviewOverride(entry.id);
      else setReviewOverride(entry.id, status);
      buildReviewDeck();
    });
  });
}

document.addEventListener("DOMContentLoaded", () => {
  bindReviewControls();
  buildReviewDeck();
});
