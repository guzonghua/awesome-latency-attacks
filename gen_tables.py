#!/usr/bin/env python3
"""Generate LaTeX appendix tables AND GitHub markdown tables from catalog.json.

Usage: python gen_tables.py   (run from repo root)
"""
import json, html
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PAPER_DIR = ROOT / "paper"

cat = json.load(open(PAPER_DIR / "catalog.json"))

# ---------------- LaTeX ----------------
def tex_escape(s):
    return (s.replace("&", "\\&").replace("%", "\\%").replace("_", "\\_")
             .replace("#", "\\#"))

def tex_link(url, label):
    if not url:
        return r"\ding{55}"  # x mark
    return r"\href{%s}{%s}" % (url, label)

def latex_attack_table(rows, caption, label):
    out = []
    out.append(r"\begin{table*}[t]")
    out.append(r"  \caption{%s}" % caption)
    out.append(r"  \label{%s}" % label)
    out.append(r"  \footnotesize")
    out.append(r"  \setlength{\tabcolsep}{4pt}")
    out.append(r"  \begin{tabularx}{\textwidth}{L{2.5cm} L{2.3cm} X L{1.5cm} L{2.2cm} >{\centering\arraybackslash}p{0.9cm} >{\centering\arraybackslash}p{0.9cm}}")
    out.append(r"    \toprule")
    out.append(r"    \textbf{Attack} & \textbf{Venue (Year)} & \textbf{Target} & \textbf{Domain} & \textbf{Setting} & \textbf{Paper} & \textbf{Code} \\")
    out.append(r"    \midrule")
    for r in rows:
        venue = "%s (%s)" % (r["venue"], r["year"])
        out.append("    %s & %s & %s & %s & %s & %s & %s \\\\" % (
            tex_escape(r["name"]), tex_escape(venue), tex_escape(r["target"]),
            tex_escape(r["app"]), tex_escape(r["setting"]),
            tex_link(r["paper"], r"\faFilePdf"), tex_link(r["code"], r"\faGithub")))
        out.append(r"    \addlinespace[1pt]")
    out.append(r"    \bottomrule")
    out.append(r"  \end{tabularx}")
    out.append(r"\end{table*}")
    return "\n".join(out)

def latex_defense_table(rows, caption, label):
    out = []
    out.append(r"\begin{table*}[t]")
    out.append(r"  \caption{%s}" % caption)
    out.append(r"  \label{%s}" % label)
    out.append(r"  \footnotesize")
    out.append(r"  \setlength{\tabcolsep}{4pt}")
    out.append(r"  \begin{tabularx}{\textwidth}{L{2.5cm} L{2.3cm} X L{2.5cm} L{1.5cm} >{\centering\arraybackslash}p{0.9cm} >{\centering\arraybackslash}p{0.9cm}}")
    out.append(r"    \toprule")
    out.append(r"    \textbf{Defense} & \textbf{Venue (Year)} & \textbf{Target} & \textbf{Mechanism} & \textbf{Domain} & \textbf{Paper} & \textbf{Code} \\")
    out.append(r"    \midrule")
    for r in rows:
        venue = "%s (%s)" % (r["venue"], r["year"])
        out.append("    %s & %s & %s & %s & %s & %s & %s \\\\" % (
            tex_escape(r["name"]), tex_escape(venue), tex_escape(r["target"]),
            tex_escape(r["type"]), tex_escape(r["app"]),
            tex_link(r["paper"], r"\faFilePdf"), tex_link(r["code"], r"\faGithub")))
        out.append(r"    \addlinespace[1pt]")
    out.append(r"    \bottomrule")
    out.append(r"  \end{tabularx}")
    out.append(r"\end{table*}")
    return "\n".join(out)

inf = sorted(cat["inference_attacks"], key=lambda r: r["year"])
tr  = sorted(cat["training_attacks"], key=lambda r: r["year"])
de  = sorted(cat["defenses"], key=lambda r: r["year"])

latex = []
latex.append("%% AUTO-GENERATED appendix tables (gen_tables.py). Do not edit by hand.")
latex.append(latex_attack_table(inf, "Inference-stage latency, energy, and timing attacks on deep learning. \\faFilePdf~links to the paper; \\faGithub~links to released code (\\ding{55}~= none located).", "tab:cat-inference"))
latex.append("")
latex.append(latex_attack_table(tr, "Training-stage (poisoning / backdoor / weight) latency and energy attacks.", "tab:cat-training"))
latex.append("")
latex.append(latex_defense_table(de, "Defenses against latency, energy, and timing attacks, by control mechanism.", "tab:cat-defenses"))
open(PAPER_DIR / "appendix_tables.tex", "w").write("\n".join(latex) + "\n")
print("Wrote appendix_tables.tex (%d inf, %d train, %d def)" % (len(inf), len(tr), len(de)))

# ---------------- Markdown ----------------
def md_link(url, label):
    return "[%s](%s)" % (label, url) if url else "\u2718"

def md_attack_table(rows):
    out = ["|Attack | Venue | Target | Domain | Setting | Paper :page_facing_up: | Code |",
           "| :--- | :---: | :---: | :---: | :---: | :---: | :---: |"]
    for r in rows:
        venue = "%s (%s)" % (r["venue"], r["year"])
        out.append("| %s | %s | %s | %s | %s | %s | %s |" % (
            r["name"], venue, r["target"], r["app"], r["setting"],
            md_link(r["paper"], "paper"), md_link(r["code"], "GitHub")))
    return "\n".join(out)

def md_defense_table(rows):
    out = ["|Defense | Venue | Target | Mechanism | Domain | Paper :page_facing_up: | Code |",
           "| :--- | :---: | :---: | :---: | :---: | :---: | :---: |"]
    for r in rows:
        venue = "%s (%s)" % (r["venue"], r["year"])
        out.append("| %s | %s | %s | %s | %s | %s | %s |" % (
            r["name"], venue, r["target"], r["type"], r["app"],
            md_link(r["paper"], "paper"), md_link(r["code"], "GitHub")))
    return "\n".join(out)

json.dump({"inf_md": md_attack_table(inf), "tr_md": md_attack_table(tr),
           "de_md": md_defense_table(de),
           "counts": {"inf": len(inf), "tr": len(tr), "de": len(de)}},
          open(PAPER_DIR / "_md_fragments.json", "w"))
print("Wrote markdown fragments")
