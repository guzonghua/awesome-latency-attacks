#!/usr/bin/env python3
"""Regenerate README.md tables from assets/catalog.json.

Usage: python gen_site.py   (run from repo root)

The interactive index.html reads assets/catalog.json directly at load time, so
this script only updates the static README tables and catalog-derived counts.
"""
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parent
CATALOG_PATH = ROOT / "assets" / "catalog.json"
README_PATH = ROOT / "README.md"


def md_link(url: str, label: str) -> str:
    return f"[{label}]({url})" if url else "✘"


def sort_by_year(rows: Iterable[dict]) -> list[dict]:
    return sorted(rows, key=lambda row: row["year"])


def attack_table(rows: Iterable[dict]) -> str:
    out = [
        "|Attack | Venue | Target | Domain | Setting | Paper :page_facing_up: | Code |",
        "| :--- | :---: | :---: | :---: | :---: | :---: | :---: |",
    ]
    for row in sort_by_year(rows):
        venue = f"{row['venue']} ({row['year']})"
        out.append(
            "| {name} | {venue} | {target} | {app} | {setting} | {paper} | {code} |".format(
                name=row["name"],
                venue=venue,
                target=row["target"],
                app=row["app"],
                setting=row["setting"],
                paper=md_link(row.get("paper", ""), "paper"),
                code=md_link(row.get("code", ""), "GitHub"),
            )
        )
    return "\n".join(out)


def defense_table(rows: Iterable[dict]) -> str:
    out = [
        "|Defense | Venue | Target | Mechanism | Domain | Paper :page_facing_up: | Code |",
        "| :--- | :---: | :---: | :---: | :---: | :---: | :---: |",
    ]
    for row in sort_by_year(rows):
        venue = f"{row['venue']} ({row['year']})"
        out.append(
            "| {name} | {venue} | {target} | {kind} | {app} | {paper} | {code} |".format(
                name=row["name"],
                venue=venue,
                target=row["target"],
                kind=row["type"],
                app=row["app"],
                paper=md_link(row.get("paper", ""), "paper"),
                code=md_link(row.get("code", ""), "GitHub"),
            )
        )
    return "\n".join(out)


def replace_section_table(readme: str, heading: str, table: str) -> str:
    pattern = re.compile(
        rf"(## {re.escape(heading)}\n\n)(.*?)(\n\n---)",
        re.DOTALL,
    )
    updated, count = pattern.subn(lambda match: f"{match.group(1)}{table}{match.group(3)}", readme, count=1)
    if count != 1:
        raise RuntimeError(f"Could not find exactly one README table section for {heading}")
    return updated


def update_counts(readme: str, catalog: dict) -> str:
    inf = len(catalog["inference_attacks"])
    train = len(catalog["training_attacks"])
    defenses = len(catalog["defenses"])
    total = inf + train + defenses
    counts = (
        f"**{total} works** "
        f"({inf} inference-stage attacks, {train} training-stage attacks, {defenses} defenses)"
    )
    updated, count = re.subn(
        r"\*\*\d+ works\*\* "
        r"\(\d+ inference-stage attacks, \d+ training-stage attacks, \d+ defenses\)",
        counts,
        readme,
        count=1,
    )
    if count != 1:
        raise RuntimeError("Could not update README catalog counts")
    return updated


def build_readme(readme: str, catalog: dict) -> str:
    readme = update_counts(readme, catalog)
    readme = replace_section_table(
        readme,
        "Inference-Stage Attacks",
        attack_table(catalog["inference_attacks"]),
    )
    readme = replace_section_table(
        readme,
        "Training-Stage Attacks",
        attack_table(catalog["training_attacks"]),
    )
    readme = replace_section_table(
        readme,
        "Defenses",
        defense_table(catalog["defenses"]),
    )
    return readme


def main() -> None:
    catalog = json.loads(CATALOG_PATH.read_text())
    current = README_PATH.read_text()
    updated = build_readme(current, catalog)
    if updated != current:
        README_PATH.write_text(updated)
        print("Updated README.md from assets/catalog.json")
    else:
        print("README.md is already up to date")


if __name__ == "__main__":
    main()
