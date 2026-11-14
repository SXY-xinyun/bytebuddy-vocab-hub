# -*- coding: utf-8 -*-
"""Add APA7 sources to vocab JS, export Excel, and evidence file exports."""
import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WEB = ROOT / "website" / "js"
EV_DIR = ROOT / "evidence"
SCREEN = EV_DIR / "screenshots"
FILES = EV_DIR / "file_exports"

APA = {
    "prog-algorithm": "Merriam-Webster. (n.d.). Algorithm. In Merriam-Webster.com dictionary. https://www.merriam-webster.com/dictionary/algorithm",
    "prog-debug": "Oxford University Press. (2026). Debug. In Oxford Learner's Dictionaries. https://www.oxfordlearnersdictionaries.com/definition/english/debug_1",
    "prog-syntax": "Cambridge University Press. (2026). Syntax. In Cambridge Dictionary. https://dictionary.cambridge.org/dictionary/english/syntax",
    "prog-variable": "Cambridge University Press. (2026). Variable. In Cambridge Dictionary. https://dictionary.cambridge.org/dictionary/english/variable",
    "prog-function": "Mozilla Foundation. (2026). Function. In MDN Web Docs. https://developer.mozilla.org/en-US/docs/Glossary/Function",
    "prog-loop": "Cambridge University Press. (2026). Loop. In Cambridge Dictionary. https://dictionary.cambridge.org/dictionary/english/loop",
    "prog-compile": "Oracle Corporation. (2026). Compile. In Java documentation glossary. https://docs.oracle.com/javase/",
    "prog-recursion": "Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. H. (2022). Introduction to algorithms (4th ed.). MIT Press.",
    "prog-iteration": "IEEE. (2023). Iteration. In IEEE software engineering vocabulary.",
    "prog-pointer": "International Organization for Standardization. (2018). ISO/IEC 9899:2018 — Programming languages — C.",
    "prog-exception": "Oracle Corporation. (2026). Exceptions. In The Java Tutorials. https://docs.oracle.com/javase/tutorial/essential/exceptions/",
    "prog-polymorphism": "IBM Corporation. (n.d.). Polymorphism. In IBM Think topics. https://www.ibm.com/topics/polymorphism",
    "prog-compiler": "Aho, A. V., Lam, M. S., Sethi, R., & Ullman, J. D. (2007). Compilers: Principles, techniques, and tools (2nd ed.). Pearson.",
    "ai-dataset": "Google. (n.d.). Dataset. In Google for Developers machine learning glossary. https://developers.google.com/machine-learning/glossary",
    "ai-inference": "Google. (n.d.). Inference. In Google for Developers machine learning glossary. https://developers.google.com/machine-learning/glossary",
    "ai-perceptron": "Rosenblatt, F. (1958). The perceptron: A probabilistic model for information storage and organization in the brain. Psychological Review, 65(6), 386–408. https://doi.org/10.1037/h0042519",
    "ai-training": "Google. (n.d.). Training. In Google for Developers machine learning glossary. https://developers.google.com/machine-learning/glossary",
    "ai-overfitting": "Google. (n.d.). Overfitting. In Google for Developers machine learning glossary. https://developers.google.com/machine-learning/glossary",
    "ai-feature": "James, G., Witten, D., Hastie, T., & Tibshirari, R. (2021). An introduction to statistical learning (2nd ed.). Springer. https://doi.org/10.1007/978-1-0716-1417-0",
    "ai-classification": "Google. (n.d.). Classification. In Google for Developers machine learning glossary. https://developers.google.com/machine-learning/glossary",
    "ai-regression": "Google. (n.d.). Regression. In Google for Developers machine learning glossary. https://developers.google.com/machine-learning/glossary",
    "ai-epoch": "PyTorch Foundation. (2026). PyTorch documentation. https://pytorch.org/docs/stable/index.html",
    "ai-hyperparameter": "Goodfellow, I., Bengio, Y., & Courville, A. (2016). Deep learning. MIT Press. http://www.deeplearningbook.org",
    "ai-label": "Google. (n.d.). Label. In Google for Developers machine learning glossary. https://developers.google.com/machine-learning/glossary",
    "ai-gradient": "Goodfellow, I., Bengio, Y., & Courville, A. (2016). Deep learning. MIT Press. http://www.deeplearningbook.org",
    "ai-transformer": "Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., & Polosukhin, I. (2017). Attention is all you need. In Advances in Neural Information Processing Systems (Vol. 30). https://doi.org/10.48550/arXiv.1706.03762",
    "math-matrix": "Strang, G. (2016). Introduction to linear algebra (5th ed.). Wellesley-Cambridge Press.",
    "math-boolean": "Cambridge University Press. (2026). Boolean. In Cambridge Dictionary. https://dictionary.cambridge.org/dictionary/english/boolean",
    "math-proof": "Cambridge University Press. (2026). Proof. In Cambridge Dictionary. https://dictionary.cambridge.org/dictionary/english/proof",
    "math-vector": "Strang, G. (2016). Introduction to linear algebra (5th ed.). Wellesley-Cambridge Press.",
    "math-logarithm": "Stewart, J. (2015). Calculus: Early transcendentals (8th ed.). Cengage Learning.",
    "math-derivative": "Stewart, J. (2015). Calculus: Early transcendentals (8th ed.). Cengage Learning.",
    "math-integral": "Stewart, J. (2015). Calculus: Early transcendentals (8th ed.). Cengage Learning.",
    "math-permutation": "Rosen, K. H. (2019). Discrete mathematics and its applications (8th ed.). McGraw-Hill.",
    "math-proposition": "Rosen, K. H. (2019). Discrete mathematics and its applications (8th ed.). McGraw-Hill.",
    "math-set": "Rosen, K. H. (2019). Discrete mathematics and its applications (8th ed.). McGraw-Hill.",
    "math-eigenvalue": "Strang, G. (2016). Introduction to linear algebra (5th ed.). Wellesley-Cambridge Press.",
    "math-combinatorics": "Rosen, K. H. (2019). Discrete mathematics and its applications (8th ed.). McGraw-Hill.",
    "math-determinant": "Strang, G. (2016). Introduction to linear algebra (5th ed.). Wellesley-Cambridge Press.",
    "lab-terminal": "GitHub, Inc. (2026). About the terminal. In GitHub Docs. https://docs.github.com/",
    "lab-repository": "GitHub, Inc. (2026). About repositories. In GitHub Docs. https://docs.github.com/en/repositories",
    "lab-endpoint": "Mozilla Foundation. (2026). Endpoint. In MDN Web Docs. https://developer.mozilla.org/en-US/docs/Glossary/Endpoint",
    "lab-editor": "JetBrains. (2026). Integrated development environment. https://www.jetbrains.com/",
    "lab-deployment": "GitLab Inc. (2026). Deployment. In GitLab documentation. https://docs.gitlab.com/",
    "lab-framework": "Mozilla Foundation. (2026). Framework. In MDN Web Docs. https://developer.mozilla.org/en-US/docs/Glossary/Framework",
    "lab-branch": "GitHub, Inc. (2026). About branches. In GitHub Docs. https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-branches",
    "lab-commit": "GitHub, Inc. (2026). About commits. In GitHub Docs. https://docs.github.com/en/pull-requests/committing-changes-to-your-project",
    "lab-merge": "GitHub, Inc. (2026). About merge methods. In GitHub Docs. https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges",
    "lab-localhost": "Mozilla Foundation. (2026). Localhost. In MDN Web Docs. https://developer.mozilla.org/en-US/docs/Glossary/Localhost",
    "lab-debugger": "Microsoft Corporation. (2026). Debugger. In Visual Studio documentation. https://learn.microsoft.com/en-us/visualstudio/debugger/",
    "lab-cloud": "National Institute of Standards and Technology. (2011). The NIST definition of cloud computing (SP 800-145). U.S. Department of Commerce. https://doi.org/10.6028/NIST.SP.800-145",
    "lab-container": "Docker, Inc. (2026). What is a container? In Docker documentation. https://docs.docker.com/get-started/overview/",
}


def inject_apa(path: Path):
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    out = []
    current_id = None
    in_block = False
    has_source = False
    i = 0
    while i < len(lines):
        line = lines[i]
        m = re.search(r'id:\s*"([^"]+)"', line)
        if m:
            current_id = m.group(1)
            in_block = True
            has_source = False
        if in_block and "source_apa:" in line:
            has_source = True
        if in_block and re.match(r"\s*\},?\s*$", line) and current_id:
            if not has_source and current_id in APA:
                apa = APA[current_id].replace("\\", "\\\\").replace('"', '\\"')
                indent = "    "
                out.append(f'{indent}source_apa: "{apa}",\n')
            current_id = None
            in_block = False
        out.append(line)
        i += 1
    path.write_text("".join(out), encoding="utf-8")


def load_entries_from_js():
    import subprocess

    dump = ROOT / "scripts" / "dump_vocab.mjs"
    r = subprocess.run(
        ["node", dump.name],
        capture_output=True,
        text=True,
        cwd=str(ROOT / "scripts"),
    )
    if r.returncode != 0:
        raise SystemExit(r.stderr or r.stdout)
    return json.loads(r.stdout)


def export_excel(entries):
    from openpyxl import Workbook
    from openpyxl.styles import Font, Alignment

    wb = Workbook()
    ws = wb.active
    ws.title = "Vocabulary"
    headers = [
        "id", "word", "module", "pos", "phonetic",
        "en_definition", "zh_meaning", "example", "review_status", "source_apa",
    ]
    ws.append(headers)
    for h in ws[1]:
        h.font = Font(bold=True)
    for e in sorted(entries, key=lambda x: (x["module"], x["word"])):
        ws.append([e.get(h, "") for h in headers])
    for row in ws.iter_rows(min_row=2, max_row=ws.max_row):
        for cell in row:
            cell.alignment = Alignment(wrap_text=True, vertical="top")
    ws.column_dimensions["A"].width = 18
    ws.column_dimensions["B"].width = 14
    ws.column_dimensions["C"].width = 16
    ws.column_dimensions["F"].width = 40
    ws.column_dimensions["G"].width = 36
    ws.column_dimensions["J"].width = 52
    out = ROOT / "ByteBuddy_Vocabulary_Database.xlsx"
    wb.save(out)
    return out


def export_csv_json(entries):
    SCREEN.mkdir(parents=True, exist_ok=True)
    FILES.mkdir(parents=True, exist_ok=True)
    csv_path = FILES / "EV-007_CSV_Export.csv"
    fields = [
        "id", "word", "module", "pos", "phonetic",
        "en_definition", "zh_meaning", "example", "review_status", "source_apa",
    ]
    with csv_path.open("w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        for e in sorted(entries, key=lambda x: x["word"]):
            w.writerow(e)
    json_path = FILES / "EV-014_Review_Progress.json"
    json_path.write_text(
        json.dumps(
            {
                "exported": "2026-10-24T12:00:00.000Z",
                "note": "Sample export for evidence portfolio; overrides empty at initial state.",
                "overrides": {},
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    (EV_DIR / "README.txt").write_text(
        "Evidence folder\n"
        "===============\n"
        "screenshots/     PNG files named EV-00x_....png (capture from website)\n"
        "file_exports/    EV-007 CSV and EV-014 JSON (generated from database)\n\n",
        encoding="utf-8",
    )
    (SCREEN / "SCREENSHOTS_NEEDED.txt").write_text(
        "Screenshots are NOT auto-generated. Capture from the website and save here using names in Database Evidence Log (1).xlsx Evidence Index.\n",
        encoding="utf-8",
    )
    return csv_path, json_path


def main():
    for f in ("words.js", "vocab-extra.js"):
        inject_apa(WEB / f)
    entries = load_entries_from_js()
    print("Entries:", len(entries))
    print("Excel:", export_excel(entries))
    csv_p, json_p = export_csv_json(entries)
    print("CSV:", csv_p)
    print("JSON:", json_p)


if __name__ == "__main__":
    main()
