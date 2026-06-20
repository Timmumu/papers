---
ref: ""
citekey: "Vahid-Mousavi2025"
title: "Transformer-based time-series GAN for data augmentation in bridge digital twins"
authors: "Vahid Mousavi; Maria Rashidi; Shayan Ghazimoghadam; Masoud Mohammadi; Bijan Samali; Joshua Devitt"
year: 2025
journal: "Automation in Construction"
doi: "10.1016/j.autcon.2025.106208"
zotero_key: "MR7KZQ29"
zotero_status: abstract-grounded
last_verified: "2026-06-15"
tags: ["Bridge", "Deep-Learning", "Digital-Twin", "Infrastructure", "Monitoring", "Quality", "Sensor", "Structural", "Unsorted", "source: lens"]
---
# Vahid-Mousavi2025 — Transformer-based time-series GAN for data augmentation in bridge digital twins

| Field | Value |
|-------|-------|
| **Ref** | — |
| **Authors** | Vahid Mousavi; Maria Rashidi; Shayan Ghazimoghadam; Masoud Mohammadi; Bijan Samali; Joshua Devitt |
| **Year / Venue** | 2025 · *Automation in Construction* |
| **DOI** | [10.1016/j.autcon.2025.106208](https://doi.org/10.1016/j.autcon.2025.106208) |
| **Zotero** | `MR7KZQ29` |
| **Screening** | V1: digital twins \| V2: infrastructure|bridge|structural \| V3: quality|deep learning|monitoring|sensor |

## Abstract ^sec-abstract

Recent advancements in AI-based Digital Twins (DTs) have substantially influenced bridge monitoring and maintenance, especially through Deep Learning (DL) for sensor-based damage detection. However, the effectiveness of DL models is constrained by the extensive training data they require, which is often costly and time-consuming to collect in bridge infrastructure contexts. To address this data scarcity, this paper proposes a data augmentation strategy employing a transformer-based time-series Wasserstein generative adversarial network with gradient penalty (TTS-WGAN-GP) to generate synthetic acceleration data. The synthetic data's fidelity is validated through similarity metrics and frequency domain analysis, showing close alignment with real acceleration signals for damage detection. Results demonstrate that this method achieves high-quality synthetic data with superior computational efficiency compared to existing approaches, improving dataset balancing and potentially enhancing the performance of data-driven models in DTs. This approach reduces dependence on extensive data collection, supporting reliable bridge health monitoring applications. • Development of a GAN model for generating synthetic bridge acceleration data. • Introduction of a new similarity metric for assessing synthetic data quality in bridge damage detection. • Comparative analysis of the proposed model against existing GAN methods in structural health monitoring (SHM) • Application of the proposed model to generate synthetic acceleration signals based on real-world data from the Werrington Bridge.

## Introduction & Background ^sec-intro

AI-based DTs have substantially influenced bridge monitoring and maintenance, especially through DL for sensor-based damage detection. However, DL model effectiveness is constrained by extensive, costly training data. A **transformer-based time-series Wasserstein GAN with gradient penalty (TTS-WGAN-GP)** is proposed for data augmentation.

## Method ^sec-method

TTS-WGAN-GP generates synthetic acceleration data validated through similarity metrics and frequency-domain analysis against real signals. Applied to real-world data from the Werrington Bridge.

## Key Findings ^sec-results

High-quality synthetic data with superior computational efficiency vs existing approaches, improving dataset balancing and potentially enhancing data-driven DT model performance. Reduces dependence on extensive data collection for bridge SHM.

## Discussion & Implications ^sec-discussion

**Highly relevant** — a GAN-based data-augmentation method for bridge DT SHM, addressing the critical data-scarcity problem. Directly informs the AI-for-DT and SHM strands.

## Notes ^sec-notes

- **Screening:** Retained — GAN + data augmentation + bridge DT + SHM (strong fit).
- **Relevance:** High; cite for TTS-WGAN-GP synthetic data generation for DT-SHM.
- **Source:** Hybrid OA; abstract-grounded, full text pending.
