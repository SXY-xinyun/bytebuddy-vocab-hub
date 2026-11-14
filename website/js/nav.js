function navPrefix() {
  return document.body.dataset.navPrefix || "";
}

function browseHref() {
  return document.body.dataset.browseHref || "index.html";
}

function renderSiteNav(active) {
  const prefix = navPrefix();
  const browse = browseHref();
  document.querySelectorAll(".site-nav").forEach((nav) => {
    nav.innerHTML = `
      <a class="nav-link ${active === "browse" ? "is-active" : ""}" href="${browse}">Browse</a>
      <a class="nav-link ${active === "table" ? "is-active" : ""}" href="${prefix}table.html">Table</a>
      <a class="nav-link ${active === "review" ? "is-active" : ""}" href="${prefix}review.html">Review</a>
    `;
  });
}

function renderVersionFooter() {
  document.querySelectorAll("[data-db-version]").forEach((el) => {
    el.textContent =
      typeof VOCAB_DB_VERSION !== "undefined"
        ? VOCAB_DB_VERSION
        : "v1";
  });
}

document.addEventListener("DOMContentLoaded", () => {
  const page = document.body.dataset.page;
  if (page) renderSiteNav(page);
  renderVersionFooter();
});
