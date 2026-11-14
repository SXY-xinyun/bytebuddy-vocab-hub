const REVIEW_STORAGE_KEY = "cs_vocab_review_overrides_v17";

function getReviewOverrides() {
  try {
    const raw = localStorage.getItem(REVIEW_STORAGE_KEY);
    return raw ? JSON.parse(raw) : {};
  } catch {
    return {};
  }
}

function getEffectiveReviewStatus(entry) {
  const overrides = getReviewOverrides();
  return overrides[entry.id] ?? entry.review_status;
}

function setReviewOverride(entryId, status) {
  const overrides = getReviewOverrides();
  overrides[entryId] = status;
  localStorage.setItem(REVIEW_STORAGE_KEY, JSON.stringify(overrides));
}

function clearReviewOverride(entryId) {
  const overrides = getReviewOverrides();
  delete overrides[entryId];
  localStorage.setItem(REVIEW_STORAGE_KEY, JSON.stringify(overrides));
}

const REVIEW_STATUSES = ["New", "Learning", "Mastered"];

function reviewStatusClass(status) {
  return `status-${status.toLowerCase()}`;
}

function exportReviewProgressJson() {
  const payload = {
    exported: new Date().toISOString(),
    overrides: getReviewOverrides(),
  };
  downloadTextFile(
    "bytebuddy_review_progress.json",
    JSON.stringify(payload, null, 2),
    "application/json"
  );
}

function clearAllReviewOverrides() {
  localStorage.removeItem(REVIEW_STORAGE_KEY);
}
