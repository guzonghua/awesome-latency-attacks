# Contributing

Thanks for helping keep this catalog of deep learning latency, energy-latency, and timing (availability) attacks and defenses up to date! Contributions of new papers, corrected metadata, and fixed links are all welcome.

## The catalog is the single source of truth

Everything — the `README.md` tables, the interactive [GitHub Pages site](https://guzonghua.github.io/awesome-latency-attacks/), and the LaTeX appendix in the paper — is generated from **[`assets/catalog.json`](./assets/catalog.json)**. You only edit that one file.

## Adding a paper

1. **Fork** this repository and create a branch.
2. Open [`assets/catalog.json`](./assets/catalog.json) and add an entry to the correct array:
   - `inference_attacks` — attacks applied at inference time (input perturbations, physical triggers, timing side-channels).
   - `training_attacks` — poisoning, backdoor, or weight-level attacks that persist after training.
   - `defenses` — any mitigation, hardening, or monitoring technique.
3. Use this schema (keep keys in this order; use `""` when a field is unknown):

   **Attacks**
   ```json
   {
     "name": "ShortName",
     "venue": "CVPR",
     "year": 2025,
     "target": "Object detection (NMS)",
     "app": "CV / AD",
     "setting": "White box",
     "paper": "https://arxiv.org/abs/...",
     "code": "https://github.com/...",
     "cite": "bibtexkey2025"
   }
   ```

   **Defenses** — replace `"setting"` with `"type"` (the control mechanism, e.g. `Budget enforcement`, `Input transformation`, `Runtime monitoring`).

4. **Regenerate** the README and LaTeX tables:
   ```bash
   python gen_tables.py    # rebuilds paper/appendix_tables.tex
   python gen_readme.py    # rebuilds README.md
   ```
   The interactive `index.html` needs no regeneration — it reads `assets/catalog.json` directly at load time.
5. Open a **pull request** describing the paper you added.

## Guidelines

- **Verifiable links only.** Prefer the official venue or arXiv page. Confirm DOIs/arXiv IDs resolve.
- **Peer-reviewed or arXiv-hosted** works only. No blog posts or unverifiable claims.
- **Chronological order.** Entries are sorted by `year`; keep new rows in roughly the right place (the generators also sort).
- **Domain tags** (`app`): use `CV`, `NLP`, `Speech`, `AD` (autonomous driving), `Sensing`, `CV+NLP`, or combinations like `CV / AD`.
- **One paper per entry.** If a work spans attack and defense, add it to both arrays.

## Reporting issues

Found a broken link, a wrong venue/year, or a missing paper you don't have time to add? [Open an issue](../../issues) with the details and we'll handle it.
