---
ref: ""
citekey: "Hao-yang-Zhao2026"
title: "Reverse Variational Autoencoder: A probabilistic inference framework for structural health monitoring and inverse analysis in engineering"
authors: "Hao-yang Zhao; Chen Wang; Jian-sheng Fan"
year: 2026
journal: "Reliability Engineering & System Safety"
doi: "10.1016/j.ress.2025.111938"
zotero_key: "6PRWDF3D"
zotero_status: abstract-grounded
last_verified: "2026-06-15"
tags: ["Bridge", "Deep-Learning", "Digital-Twin", "Monitoring", "Sensor", "Structural", "Unsorted", "source: lens", "identification: databases"]
---
# Hao-yang-Zhao2026 — Reverse Variational Autoencoder: A probabilistic inference framework for structural health monitoring and inverse analysis in engineering

| Field | Value |
|-------|-------|
| **Ref** | — |
| **Authors** | Hao-yang Zhao; Chen Wang; Jian-sheng Fan |
| **Year / Venue** | 2026 · *Reliability Engineering & System Safety* |
| **DOI** | [10.1016/j.ress.2025.111938](https://doi.org/10.1016/j.ress.2025.111938) |
| **Zotero** | `6PRWDF3D` |
| **Screening** | V1: digital twin \| V2: bridge|structural|structure \| V3: deep learning|monitoring|sensor|structural health monitoring |

## Abstract ^sec-abstract

• Proposed RVAE: A Bayesian deep learning framework for efficient inverse analysis. • RVAE incorporates causality by reversing the VAE compression-decompression structure. • RVAE reveals multiple possible solutions with high accuracy and efficiency. • RVAE outperforms traditional methods, achieving 1,000x faster inverse analysis. • RVAE offers flexibility with label-free inversion and adaptable prediction ranges. Inverse analysis in structural engineering involves inferring uncertain parameters from limited external observations, which is crucial for structural health monitoring and maintenance. However, real-world applications often face under-constrained problems with multiple possible solutions due to sparse measurements. This study proposes a Bayesian deep learning-based framework, termed Reverse Variational Auto-Encoder (RVAE), to fulfill efficient probabilistic structural inverse analysis. The RVAE framework modifies the original VAE structure to consider the causality relationship underlying inverse problems, enabling a semi-supervised learning paradigm for label-agnostic scenarios. The effectiveness of the RVAE framework is validated through a grid structure experiment. The implemented model successfully reveals all possible solutions for bending amplitudes, strains, and node displacements, with root-mean-squared reconstruction errors of 1.21 %, 2.77 %, and 1.36 %, respectively. A comparative analysis is conducted between mainstream inversion algorithms and RVAE. The results demonstrate that while all the other inversion algorithms achieve low reconstruction errors, they provide single-solution estimation, thus highlighting RVAE's capability to provide the most comprehensive information. RVAE's capability for real-time probabilistic estimation of structural parameters is further discussed and demonstrated in a full-scale bridge tower experiment, where it utilizes multi-sensor data to infer critical structural parameters, showing strong adaptability to noisy, incomplete, and heterogeneous monitoring inputs. In summary, RVAE tackles the challenges of large-scale parameter inversion in engineering structures by enabling efficient probabilistic inference under sparse observations. It supports semi-supervised learning in label-agnostic scenarios and real-time prediction of multiple plausible solutions, thereby fulfilling the synchronous updating requirements of digital twin systems.

## Introduction & Background ^sec-intro

Inverse analysis in structural engineering infers uncertain parameters from limited observations — crucial for structural health monitoring (SHM) — but real-world applications are often under-constrained with multiple possible solutions due to sparse measurements.

## Method ^sec-method

A Bayesian deep-learning framework, **Reverse Variational Auto-Encoder (RVAE)**, modifies the VAE structure to respect inverse-problem causality, enabling semi-supervised, label-agnostic probabilistic inverse analysis. Validated on a grid-structure experiment and a full-scale bridge-tower experiment with multi-sensor data.

## Key Findings ^sec-results

RVAE reveals all possible solutions for bending amplitudes, strains, and node displacements (RMS reconstruction errors 1.21%/2.77%/1.36%), achieving ~1000× faster inverse analysis than traditional methods while uniquely providing multi-solution probabilistic estimates rather than single-point estimates; strong adaptability to noisy data.

## Discussion & Implications ^sec-discussion

Relevant to the **probabilistic/ML-enabled DT for SHM** strand — efficient real-time probabilistic parameter estimation aligns with cognitive-DT (uncertainty-aware) requirements. A strong methodological citation for DT-SHM inverse analysis.

## Notes ^sec-notes

- **Screening:** Retained — Bayesian DL + structural inverse analysis/SHM (good fit).
- **Relevance:** Cite for probabilistic DT/SHM inverse analysis (RVAE).
- **Source:** Hybrid OA; abstract-grounded, full text pending.
