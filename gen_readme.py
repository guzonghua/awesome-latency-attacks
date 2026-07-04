#!/usr/bin/env python3
import json
f = json.load(open("/home/user/workspace/paper/_md_fragments.json"))
c = f["counts"]
total = c["inf"] + c["tr"] + c["de"]

readme = f"""# Awesome Deep Learning Latency Attacks &amp; Defenses [![Awesome](https://awesome.re/badge.svg)](https://awesome.re) [![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](./LICENSE)

<p align="center">
  <a href="https://guzonghua.github.io/awesome-latency-attacks/">
    <img src="https://img.shields.io/badge/%F0%9F%8C%90_View_the_Interactive_Site-20808D?style=for-the-badge" alt="View the interactive site" height="34">
  </a>
</p>

A curated, continuously updated collection of papers on **deep learning latency, energy-latency, and timing (availability) attacks and defenses** — spanning object detection and autonomous-driving perception, dynamic/adaptive networks, transformers, and large language &amp; vision-language models (LLMs/VLMs).

This is the companion resource for the survey *“Deep Learning Latency Attacks and Defenses: A Cross-Domain Survey.”* It currently indexes **{total} works** ({c['inf']} inference-stage attacks, {c['tr']} training-stage attacks, {c['de']} defenses).

> 🔎 Prefer a searchable, filterable view? Open the **[interactive table on GitHub Pages](https://guzonghua.github.io/awesome-latency-attacks/)**.

**Table of Contents**
- [Overview](#overview)
- [Unifying Mechanism](#unifying-mechanism)
- [Inference-Stage Attacks](#inference-stage-attacks)
- [Training-Stage Attacks](#training-stage-attacks)
- [Defenses](#defenses)
- [How to Contribute](#how-to-contribute)
- [Citation](#citation)

---

## Overview

<div align="center"><img src="./assets/overview.jpg" width="95%" /></div>

Latency attacks are **availability** attacks: rather than corrupting a prediction, the adversary inflates the inference-time computation, energy, or wall-clock latency of a model so a real-time consumer (a vehicle controller, an interactive service, a battery-powered sensor) misses its deadline or exhausts its resources — often while the prediction itself remains nominally correct.

## Unifying Mechanism

<div align="center"><img src="./assets/mechanism.png" width="92%" /></div>

Every attack family below shares one mechanism we call **intermediate-work amplification**: the adversary forces some downstream stage (NMS, self-attention, autoregressive decoding, expert routing) to process *more* intermediate objects, tokens, or steps than a benign input would generate. Because those stages have **super-linear worst-case complexity**, a modest increase in count produces a disproportionate cost increase. The natural cross-domain defense is a **work budget** — an enforced cap on intermediate objects/tokens per unit time.

---

## Inference-Stage Attacks

{f["inf_md"]}

---

## Training-Stage Attacks

{f["tr_md"]}

---

## Defenses

{f["de_md"]}

---

## How to Contribute

Contributions are welcome! To add a paper:

1. Fork the repo and edit [`assets/catalog.json`](./assets/catalog.json) — add an entry to `inference_attacks`, `training_attacks`, or `defenses`.
2. Run `python gen_site.py` to regenerate `README.md` and `index.html` from the catalog (single source of truth).
3. Open a pull request.

Each entry should include: `name`, `venue`, `year`, `target`, `app` (domain), `setting` (or `type` for defenses), `paper` URL, and `code` URL (leave `""` if none).

Please keep entries to **peer-reviewed or arXiv-hosted** works with verifiable links, and preserve chronological ordering by year.

---

## Citation

If you find this resource useful, please cite the survey:

```bibtex
@article{{gu2026latencysurvey,
  title   = {{Deep Learning Latency Attacks and Defenses: A Cross-Domain Survey}},
  author  = {{Gu, Zonghua and Gao, Zeyu and Saremi, Amin}},
  journal = {{ACM Computing Surveys (under review)}},
  year    = {{2026}}
}}
```

---

*Legend:* ✘ = no public code located. Found a broken link or missing paper? [Open an issue](../../issues).
"""
open("/home/user/workspace/companion_site/README.md", "w").write(readme)
print("Wrote README.md (%d chars)" % len(readme))
