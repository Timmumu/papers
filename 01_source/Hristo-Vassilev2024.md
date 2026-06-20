---
ref: ""
citekey: "Hristo-Vassilev2024"
title: "Uncertainty-aware point cloud segmentation for infrastructure projects using Bayesian deep learning"
authors: "Hristo Vassilev; Marius Laska; Jörg Blankenbach"
year: 2024
journal: "Automation in Construction"
doi: "10.1016/j.autcon.2024.105419"
zotero_key: "IRMQ64IM"
zotero_status: abstract-grounded
last_verified: "2026-06-15"
tags: ["Asset-Management", "Construction", "Digital-Twin", "Infrastructure", "Predictive", "Quality", "Semantic", "Unsorted", "source: lens"]
---
# Hristo-Vassilev2024 — Uncertainty-aware point cloud segmentation for infrastructure projects using Bayesian deep learning

| Field | Value |
|-------|-------|
| **Ref** | — |
| **Authors** | Hristo Vassilev; Marius Laska; Jörg Blankenbach |
| **Year / Venue** | 2024 · *Automation in Construction* |
| **DOI** | [10.1016/j.autcon.2024.105419](https://doi.org/10.1016/j.autcon.2024.105419) |
| **Zotero** | `IRMQ64IM` |
| **Screening** | V1: digital twins \| V2: construction|infrastructure|asset management \| V3: quality|semantic|predictive|uncertainty |

## Abstract ^sec-abstract

Reliable traffic infrastructure is a key factor for any country's economy. However, aging bridges often require renovation or reconstruction. Promising approaches for enhancing asset management and cost reduction are digital twins and predictive maintenance strategies. However, the creation of geometric-semantic as-is models as a basis for digital twins currently involves labor-intensive manual data capture and modeling. Modern deep learning models, such as Kernel Point Convolution (KPConv) show promising results in reducing the time needed to create digital twins by semantically segmenting point cloud data but have so far been hindered by the lack of a reliable quality measure, which can predict when the model's prediction can be trusted. This is especially viable in the construction industry, where objects and sensors may vary widely between projects and contractors. In this work, we present Bayesian neural networks, implemented through Variational Inference and Monte-Carlo dropout as approaches to conducting inference with KPConv, which show improvements in the confidence estimation and out-of-domain (OOD) detection in the scans of typical infrastructure point clouds. When confronted with different domain shifts to the test data, such as a change of scanning device and introduction of unseen classes the proposed model showed a 25.3% decrease in expected calibration error (ECE) and a 4.82 increase in OOD detection in terms of outlier-intersection-over-union (O-IoU) on average with respect to a deterministic baseline.

## Introduction & Background ^sec-intro

Aging bridges require renovation. **Digital twins** and predictive maintenance are promising but creating geometric-semantic as-is models involves labor-intensive manual capture. Bayesian neural networks with KPConv are proposed for semantic segmentation with confidence estimation.

## Method ^sec-method

Bayesian neural networks via Variational Inference and Monte-Carlo dropout for KPConv, providing confidence estimation and out-of-domain (OOD) detection for infrastructure point cloud segmentation.

## Key Findings ^sec-results

When confronted with domain shifts (different scanning device, unseen classes), the model showed **25.3% decrease in ECE** and a 4.82 increase in OOD detection vs deterministic baseline.

## Discussion & Implications ^sec-discussion

**Highly relevant** — Bayesian DL + point cloud + DT + bridge infrastructure. Directly informs the scan-to-DT and uncertainty-quantification strands.

## Notes ^sec-notes

- **Screening:** Retained — Bayesian DL + KPConv + point cloud + DT bridge (strong fit).
- **Relevance:** High; cite for Bayesian point-cloud segmentation for DT.
- **Source:** Hybrid OA; abstract-grounded, full text pending.
