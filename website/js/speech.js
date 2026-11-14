let speakingUtterance = null;

function speakWord(text) {
  if (!window.speechSynthesis) {
    alert("Text-to-speech is not supported in this browser.");
    return;
  }
  window.speechSynthesis.cancel();
  const utter = new SpeechSynthesisUtterance(text);
  utter.lang = "en-GB";
  utter.rate = 0.92;
  speakingUtterance = utter;
  window.speechSynthesis.speak(utter);
}

function bindSpeakButtons(root) {
  root.querySelectorAll("[data-speak]").forEach((btn) => {
    btn.addEventListener("click", (e) => {
      e.stopPropagation();
      speakWord(btn.dataset.speak);
      btn.classList.add("pulse-once");
      setTimeout(() => btn.classList.remove("pulse-once"), 400);
    });
  });
}

function defaultModuleImage(module) {
  const map = {
    Programming: "assets/images/module-programming.svg",
    "AI & ML": "assets/images/module-ai.svg",
    "Maths & Logic": "assets/images/module-maths.svg",
    "Lab & Tools": "assets/images/module-lab.svg",
  };
  return siteAsset(map[module] || "assets/images/module-programming.svg");
}

function entryImageUrl(entry) {
  if (entry.image_url) {
    const u = entry.image_url;
    if (/^(https?:|data:)/i.test(u)) return u;
    return siteAsset(u);
  }
  return defaultModuleImage(entry.module);
}
