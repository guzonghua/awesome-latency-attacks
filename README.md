# Awesome Deep Learning Latency Attacks &amp; Defenses [![Awesome](https://awesome.re/badge.svg)](https://awesome.re) [![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](./LICENSE)

A curated, continuously updated collection of papers on **deep learning latency, energy-latency, and timing (availability) attacks and defenses** — spanning object detection and autonomous-driving perception, dynamic/adaptive networks, transformers, and large language &amp; vision-language models (LLMs/VLMs).

This is the companion resource for the survey *“Deep Learning Latency Attacks and Defenses: A Survey from Object Detection to Large Language and Vision-Language Models.”* It currently indexes **76 works** (45 inference-stage attacks, 10 training-stage attacks, 21 defenses).

> 🔎 Prefer a searchable, filterable view? Open the **[interactive table on GitHub Pages](https://guzonghua.github.io/awesome-latency-attacks/)**.

**Table of Contents**
- [Overview](#overview)
- [Unifying Mechanism](#unifying-mechanism)
- [Inference-Stage Attacks](#inference-stage-attacks)
- [Training-Stage Attacks](#training-stage-attacks)
- [Defenses](#defenses)
- [Paper](#paper)
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

|Attack | Venue | Target | Domain | Setting | Paper :page_facing_up: | Code |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Daedalus | arXiv (2019) | Object detection (NMS) | CV / AD | White box (physical) | [paper](https://arxiv.org/abs/1902.02067) | [GitHub](https://github.com/NeuralSec/Daedalus-attack) |
| Sparsity Attacks | IEEE TCAD (2020) | CNNs | CV | White box | [paper](https://arxiv.org/abs/2006.08020) | ✘ |
| Tracker Hijacking | ICLR (2020) | Multi-object tracking | AD | White box | [paper](https://arxiv.org/abs/1905.11026) | ✘ |
| Sponge Examples | EuroS&P (2021) | Transformers + CNNs | CV & NLP | Black & white box | [paper](https://arxiv.org/abs/2006.03463) | [GitHub](https://github.com/iliaishacked/sponge_examples) |
| DeepSloth | ICLR (2021) | Multi-exit CNNs | CV | White box | [paper](https://arxiv.org/abs/2010.02432) | [GitHub](https://github.com/Sanghyun-Hong/DeepSloth) |
| Timing Side-Channel AE | IEICE Trans. (2021) | DNN classifiers (timing oracle) | CV | Black box (timing) | [paper](https://doi.org/10.1587/transfun.2020CIP0022) | ✘ |
| SpikeAttack | ACM/IEEE DAC (2022) | Spiking neural networks | CV | White box | [paper](https://dl.acm.org/doi/pdf/10.1145/3489517.3530443) | ✘ |
| NMTSloth | ESEC/FSE (2022) | Decoder-based NMT | NLP | White box | [paper](https://arxiv.org/abs/2210.03696v1) | [GitHub](https://github.com/SeekingDream/FSE22_NMTSloth) |
| LLMEffiChecker | ACM TOSEM (2022) | LLMs | NLP | Black & white box | [paper](https://arxiv.org/abs/2210.03696) | [GitHub](https://github.com/Cap-Ning/LLMEffiChecker) |
| NICGSlowDown | CVPR (2022) | Decoder-based image captioning | CV | White box | [paper](https://arxiv.org/abs/2203.15859) | [GitHub](https://github.com/SeekingDream/CVPR22_NICGSlowDown) |
| SAME | ACL (2023) | Multi-exit transformers | NLP | White box | [paper](https://arxiv.org/abs/2305.12228) | [GitHub](https://github.com/MatthewCYM/SAME) |
| SlowBERT | ACL Findings (2023) | Multi-exit BERT | NLP | White box | [paper](https://aclanthology.org/2023.findings-acl.602/) | ✘ |
| No-Skim | arXiv (2023) | Skimming language models | NLP | Black & white box | [paper](https://arxiv.org/abs/2312.09494) | ✘ |
| Phantom Sponges | WACV (2023) | Object detection (NMS) | CV / AD | White box | [paper](https://arxiv.org/abs/2205.13618) | [GitHub](https://github.com/AvishagS422/PhantomSponges) |
| SlowLiDAR | CVPR (2023) | 3D LiDAR detection | CV / AD | White box | [paper](https://openaccess.thecvf.com/content/CVPR2023/papers/Liu_SlowLiDAR_Increasing_the_Latency_of_LiDAR-Based_Detection_Using_Adversarial_Examples_CVPR_2023_paper.pdf) | [GitHub](https://github.com/WUSTL-CSPL/SlowLiDAR) |
| WIP Tracker Attack | VehicleSec (2023) | Multi-object tracking | AD | White box (patch) | [paper](https://doi.org/10.14722/vehiclesec.2023.23063) | ✘ |
| Variable-Time Inference | AISec@CCS (2023) | Object detection (NMS timing) | CV | Black box (timing) | [paper](https://doi.org/10.1145/3605764.3623912) | ✘ |
| Overload | CVPR (2024) | Object detection (edge) | CV / AD | White box | [paper](https://arxiv.org/abs/2304.05370) | ✘ |
| Beyond PhantomSponges | ACM WiseML (2024) | Object detection (NMS) | CV / AD | White box | [paper](https://doi.org/10.1145/3649403.3656485) | ✘ |
| SlowTrack | AAAI (2024) | Camera perception (detect+track) | AD | White box | [paper](https://arxiv.org/abs/2312.09520) | [GitHub](https://github.com/eaiers/SlowTrack) |
| SlowPerception | arXiv (2024) | Camera perception (NMS+MOT) | AD | White box (physical, projector) | [paper](https://arxiv.org/abs/2406.05800) | ✘ |
| TPA (Time-aware) | Pattern Recognition Letters (2024) | Detection + segmentation | AD | White box | [paper](https://doi.org/10.1016/j.patrec.2024.01.010) | ✘ |
| Steal Now Attack Later | arXiv (2024) | Object detection | CV | Black box | [paper](https://arxiv.org/abs/2404.15881) | ✘ |
| Energy Attack (multi-exit) | Info. & Software Tech. (2024) | Adaptive multi-exit networks | CV | Grey box | [paper](https://doi.org/10.1016/j.infsof.2024.107653) | ✘ |
| Slowdown Causes (SaTML) | IEEE SaTML (2024) | Language models | NLP | White box | [paper](https://arxiv.org/abs/2305.18926) | ✘ |
| Engorgio | arXiv (2024) | LLMs (output inflation) | NLP | White box + transfer | [paper](https://arxiv.org/abs/2412.19394) | ✘ |
| Verbose Images | ICLR (2024) | Large VLMs | CV+NLP | White box | [paper](https://arxiv.org/abs/2401.11170) | [GitHub](https://github.com/KuofengGao/Verbose_Images) |
| Uniform Inputs | IEEE SPW (2024) | CNNs (sparsity) | CV | Black box | [paper](https://arxiv.org/abs/2403.18587) | [GitHub](https://github.com/and-mill/2024-sponge-example-analysis) |
| DetStorm | IEEE S&P (2025) | Camera perception | AD | White box (physical) | [paper](https://doi.org/10.1109/SP61157.2025.00236) | ✘ |
| Inference-Time Impact Analysis | arXiv (2025) | Full perception (sim.) | AD | Simulation | [paper](https://arxiv.org/abs/2505.03850) | ✘ |
| DDLS Efficiency Attacks | arXiv (2025) | Early-exit / token-pruning / MoE | CV & NLP | White & black box | [paper](https://arxiv.org/abs/2506.17621) | ✘ |
| TTSlow | IEEE TASLP (2025) | Auto-regressive TTS | Speech | White box | [paper](https://arxiv.org/abs/2407.01927) | ✘ |
| Crabs | ACL Findings (2025) | LLMs (DoS) | NLP | Black box | [paper](https://arxiv.org/abs/2412.13879) | ✘ |
| VLMInferSlow | ACL (2025) | VLMs-as-a-service | CV+NLP | Black box | [paper](https://aclanthology.org/2025.acl-long.encyclopedia/) | ✘ |
| Verbose-Text Induction | arXiv (2025) | VLMs | CV+NLP | White box | [paper](https://arxiv.org/abs/2511.16163) | ✘ |
| LingoLoop | arXiv (2025) | Multimodal LLMs | CV+NLP | White box | [paper](https://arxiv.org/abs/2506.14493) | ✘ |
| Bit-Flip NMS Attack | WACV (2025) | Object detection (parameters) | CV / AD | Hardware (Rowhammer) | [paper](https://doi.org/10.1109/WACV61041.2025.00653) | ✘ |
| Timestep-Compressed Attack | AAAI (2025) | Spiking neural networks | CV | White box | [paper](https://arxiv.org/abs/2508.13812) | ✘ |
| CP-FREEZER | AAAI (2026) | Cooperative perception (V2V) | AD | White box (testbed) | [paper](https://ojs.aaai.org/index.php/AAAI/article/download/37082/41044) | ✘ |
| Trajectory-Aware Attack | IEEE TMM (2026) | Multi-object tracking | AD | White box | [paper](https://doi.org/10.1109/TMM.2026.3651102) | ✘ |
| SPLAT | IEEE TCAD (2026) | Multi-exit dynamic networks | CV | Black box | [paper](https://doi.org/10.1109/TCAD.2025.3576320) | ✘ |
| RouteHijack | arXiv (2026) | Mixture-of-experts LLMs | NLP | White box | [paper](https://arxiv.org/abs/2605.02946) | ✘ |
| Misrouter | arXiv (2026) | Mixture-of-experts LLMs | NLP | Black box (input-only) | [paper](https://arxiv.org/abs/2605.04446) | ✘ |
| ReasoningBomb | ACM CCS (2026) | Large reasoning models | NLP | Black box | [paper](https://arxiv.org/abs/2602.00154) | ✘ |
| ThinkTrap | NDSS (2026) | Reasoning LLM APIs | NLP | Black box | [paper](https://www.ndss-symposium.org/ndss2026/) | ✘ |

---

## Training-Stage Attacks

|Attack | Venue | Target | Domain | Setting | Paper :page_facing_up: | Code |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Sponge Poisoning | arXiv / AsiaCCS (2022) | CNNs | CV | Partial control | [paper](https://arxiv.org/abs/2203.08147) | [GitHub](https://github.com/Cinofix/sponge_poisoning_energy_latency_attack) |
| On-Device Sponge Poisoning | ACM SecTL (2023) | On-device DNNs | CV | Partial control | [paper](https://doi.org/10.1145/3591197.3591307) | ✘ |
| Mobile-App Sponge | ACM HotMobile (2023) | Mobile ML models | CV | Partial control | [paper](https://doi.org/10.1145/3572864.3581586) | ✘ |
| SkipSponge | arXiv (2024) | CNNs, GANs (weights) | CV | Full control | [paper](https://arxiv.org/abs/2402.06357) | ✘ |
| Huang et al. (multi-exit) | IEEE Access (2024) | Multi-exit CNNs | CV | Full control | [paper](https://doi.org/10.1109/ACCESS.2024.3370849) | ✘ |
| Sponge Backdoor (OD) | IJCNN (2024) | Object detection (NMS) | CV / AD | Backdoor | [paper](https://doi.org/10.1109/IJCNN60899.2024.10650435) | ✘ |
| DoS Poisoning (LLM) | arXiv (2024) | LLMs (no-EOS) | NLP | Backdoor / poisoning | [paper](https://arxiv.org/abs/2410.10760) | ✘ |
| Sensing-AI Sponge | IEEE GLOBECOM (2025) | Sensing DNNs (IoT) | Sensing | Partial control | [paper](https://doi.org/10.1109/GLOBECOM59602.2025.11432163) | ✘ |
| EvoWeight (FPGA) | IEEE HOST (2025) | FPGA DNN accelerators | CV | Full control | [paper](https://doi.org/10.1109/HOST64725.2025.11050058) | ✘ |
| Reflection Backdoor (VLM-AD) | arXiv (2025) | Driving VLM planner | AD | Backdoor (physical trigger) | [paper](https://arxiv.org/abs/2505.06413) | ✘ |

---

## Defenses

|Defense | Venue | Target | Mechanism | Domain | Paper :page_facing_up: | Code |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| DEE Scheduling | ACM CIKM (2021) | Early-exit networks | Runtime scheduling | CV | [paper](https://doi.org/10.1145/3459637.3482335) | ✘ |
| Certifier Caveat | arXiv (2021) | Certified classifiers | Defense pitfall | CV | [paper](https://arxiv.org/abs/2108.11299) | ✘ |
| Constant-Time NMS | AISec@CCS (2023) | Object detection (NMS) | Bounded execution | CV | [paper](https://doi.org/10.1145/3605764.3623912) | ✘ |
| PSML | arXiv (2023) | Inference serving systems | System / serving control | ML serving | [paper](https://arxiv.org/abs/2307.01292) | ✘ |
| Adaptive Resizing | ACM WiseML (2024) | Object detection (NMS) | Input transformation | AD | [paper](https://doi.org/10.1145/3649403.3656485) | ✘ |
| ADAV Patch Defense | arXiv (2024) | Object detection | Input transformation | AD | [paper](https://arxiv.org/abs/2412.06215) | ✘ |
| Securing AV Perception | IEEE TIV (2024) | AV visual perception | Input transformation | AD | [paper](https://doi.org/10.1109/TIV.2024.3403667) | ✘ |
| Calibration Defense | IEEE SaTML (2024) | Multi-exit models | Robust training | NLP | [paper](https://arxiv.org/abs/2305.18926) | ✘ |
| Sparsity Monitor | IEEE SPW (2024) | CNNs | Runtime monitoring | CV | [paper](https://arxiv.org/abs/2403.18587) | [GitHub](https://github.com/and-mill/2024-sponge-example-analysis) |
| Garrison | ACM/IEEE DAC (2024) | Ensemble inference (GPU) | System / serving control | CV | [paper](https://doi.org/10.1145/3649329.3654810) | ✘ |
| Time-Traveling Defense | arXiv (2024) | Traffic-sign classifiers | Temporal redundancy | AD | [paper](https://arxiv.org/abs/2410.08338) | ✘ |
| Can't Slow Me Down | CVPR (2025) | Edge object detectors | Robust/adaptive training | AD | [paper](https://doi.org/10.1109/CVPR52734.2025.01791) | ✘ |
| DCT Patch Elimination | IEEE RCAR (2025) | Object detection | Input transformation | AD | [paper](https://doi.org/10.1109/RCAR65431.2025.11139457) | ✘ |
| Real-Time LiDAR Defense | ACM CCS (2025) | LiDAR detection | Runtime monitoring | AD | [paper](https://doi.org/10.1145/3719027.3765227) | ✘ |
| LDP Purification | IEEE TrustCom (2025) | VLM visual encoders | Input purification | CV+NLP | [paper](https://doi.org/10.1109/Trustcom66490.2025.00065) | ✘ |
| Pruning Defense | IEEE GLOBECOM (2025) | Sensing DNNs | Architectural sparsity | Sensing | [paper](https://doi.org/10.1109/GLOBECOM59602.2025.11432163) | ✘ |
| BlindSight | arXiv (2025) | VLMs | Architectural sparsity | CV+NLP | [paper](https://arxiv.org/abs/2507.09071) | ✘ |
| PD3F | EMNLP (2025) | LLM serving | Budget enforcement | NLP | [paper](https://arxiv.org/abs/2505.18680) | ✘ |
| SQUAD | arXiv (2026) | Early-exit ensembles | Runtime scheduling | CV | [paper](https://arxiv.org/abs/2601.22711) | ✘ |
| Token-Budget Routing | arXiv (2026) | LLM serving | Budget enforcement | NLP | ✘ | ✘ |
| Conformal Thinking | arXiv (2026) | Reasoning models | Budget enforcement | NLP | [paper](https://arxiv.org/abs/2602.03814) | ✘ |

---

## Paper

The full survey manuscript (LaTeX source + compiled PDF) lives in [`/paper`](./paper):

- [`survey.pdf`](./paper/survey.pdf) — compiled manuscript (ACM Computing Surveys format).
- [`survey.tex`](./paper/survey.tex), [`references.bib`](./paper/references.bib), [`appendix_tables.tex`](./paper/appendix_tables.tex) — source. The appendix tables are generated from [`assets/catalog.json`](./assets/catalog.json) via `gen_tables.py`.

To rebuild: `cd paper && pdflatex survey && bibtex survey && pdflatex survey && pdflatex survey`.

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
@article{latencysurvey2026,
  title   = {Deep Learning Latency Attacks and Defenses: A Survey from Object
             Detection to Large Language and Vision-Language Models},
  author  = {Anonymous Author(s)},
  journal = {ACM Computing Surveys (under review)},
  year    = {2026}
}
```

---

*Legend:* ✘ = no public code located. Found a broken link or missing paper? [Open an issue](../../issues).
