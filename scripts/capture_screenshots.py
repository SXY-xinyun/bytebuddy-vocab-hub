# -*- coding: utf-8 -*-
"""Capture key evidence PNGs via Playwright (local http.server on 8765)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "evidence" / "screenshots"
BASE = "http://127.0.0.1:8765"

SHOTS = [
    ("EV-002_Initial_Browse.png", f"{BASE}/START%20HERE%20-%20Double-click%20to%20Open%20Website.html"),
    ("EV-004_After_Filters.png", f"{BASE}/START%20HERE%20-%20Double-click%20to%20Open%20Website.html"),  # filter applied in script
    ("EV-012_Dashboard_Stats.png", f"{BASE}/START%20HERE%20-%20Double-click%20to%20Open%20Website.html"),
    ("EV-015_Single_Word_Table.png", f"{BASE}/website/table.html"),
    ("EV-013_Review_Flashcard.png", f"{BASE}/website/review.html"),
    ("EV-021_Review_After_Reveal.png", f"{BASE}/website/review.html"),  # after reveal click
]


def main():
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        import subprocess
        import sys
        subprocess.check_call([sys.executable, "-m", "pip", "install", "playwright", "-q"])
        subprocess.check_call([sys.executable, "-m", "playwright", "install", "chromium"])
        from playwright.sync_api import sync_playwright

    OUT.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1280, "height": 900})

        page.goto(SHOTS[0][1], wait_until="networkidle")
        page.screenshot(path=str(OUT / SHOTS[0][0]), full_page=False)

        page.select_option("#filter-module", "Programming")
        page.wait_for_timeout(400)
        page.screenshot(path=str(OUT / SHOTS[1][0]), full_page=False)

        page.select_option("#filter-module", "")
        page.screenshot(path=str(OUT / SHOTS[2][0]), full_page=False)

        page.goto(SHOTS[3][1], wait_until="networkidle")
        page.screenshot(path=str(OUT / SHOTS[3][0]), full_page=True)

        page.goto(SHOTS[4][1], wait_until="networkidle")
        page.screenshot(path=str(OUT / SHOTS[4][0]), full_page=False)
        page.click("#btn-reveal")
        page.wait_for_timeout(300)
        page.screenshot(path=str(OUT / SHOTS[5][0]), full_page=False)

        browser.close()
    print("Saved", len(SHOTS), "screenshots to", OUT)


if __name__ == "__main__":
    main()
