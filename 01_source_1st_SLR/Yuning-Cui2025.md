---
ref: ""
citekey: "Yuning-Cui2025"
title: "Frequency-Prompted Image Restoration to Enhance Perception in Intelligent Transportation Systems"
authors: "Yuning Cui; Mingyu Liu; Xiongfei Su; Alois Knoll"
year: 2025
journal: "IEEE Transactions on Intelligent Transportation Systems"
doi: "10.1109/tits.2025.3617507"
zotero_key: "RHL8MDAU"
zotero_status: abstract-grounded
last_verified: "2026-06-15"
tags: ["Digital-Twin", "Infrastructure", "Quality", "Unsorted", "source: lens", "identification: databases"]
---
# Yuning-Cui2025 — Frequency-Prompted Image Restoration to Enhance Perception in Intelligent Transportation Systems

| Field | Value |
|-------|-------|
| **Ref** | — |
| **Authors** | Yuning Cui; Mingyu Liu; Xiongfei Su; Alois Knoll |
| **Year / Venue** | 2025 · *IEEE Transactions on Intelligent Transportation Systems* |
| **DOI** | [10.1109/tits.2025.3617507](https://doi.org/10.1109/tits.2025.3617507) |
| **Zotero** | `RHL8MDAU` |
| **Screening** | V1: digital twins \| V2: infrastructure \| V3: quality |

## Abstract ^sec-abstract

High perceptual image quality is crucial for intelligent transportation systems (ITS), including autonomous vehicles, digital twins, and surveillance infrastructure. However, images captured in adverse weather conditions or dynamic environments often suffer from various visibility degradations. To address this issue, image restoration aims to recover missing details and remove distortions from degraded observations, thereby enhancing the usability of visual data in intelligent transportation applications. Inspired by the success of prompt learning in natural language processing, recent studies have explored prompt-based approaches for various image restoration tasks. However, most of these methods operate in the spatial domain. Given the importance of frequency learning in image restoration, particularly in reducing the spectral discrepancy between degraded and sharp image pairs, this study investigates the use of frequency prompts through a plug-and-play mechanism consisting of a prompt generation module and a prompt integration module. Specifically, the prompt generation module encodes frequency information by aggregating pre-defined learnable parameters, guided by the implicitly decomposed spectra of the input features. The learned prompts are then integrated into the feature spectra via dual-dimensional attention, dynamically guiding the reconstruction process and enabling more effective frequency-aware learning. To validate the effectiveness of the proposed plug-in module, we integrate it into both CNN-based and Transformer-based backbones. Extensive experiments demonstrate that the CNN-based variant achieves state-of-the-art performance on 15 datasets across five representative image restoration tasks. Furthermore, it generalizes well to composite degradation scenarios. The Transformer-based model performs competitively with state-of-the-art methods under two all-in-one image restoration settings. Finally, the effectiveness of our models in enhancing perception for ITS is empirically verified.

## Introduction & Background ^sec-intro

High perceptual image quality is crucial for intelligent transportation systems (ITS), including autonomous vehicles, digital twins, and surveillance infrastructure. The paper investigates **frequency prompts for image restoration** via a plug-and-play mechanism to recover missing details from degraded observations.

## Method ^sec-method

A prompt generation module encodes frequency information guided by implicitly decomposed spectra; a prompt integration module incorporates learned prompts into feature spectra via dual-dimensional attention. Integrated into both CNN and Transformer backbones and tested across 15 datasets and five image-restoration tasks.

## Key Findings ^sec-results

The CNN-based variant achieves state-of-the-art performance on 15 datasets; generalises to composite degradation scenarios. The Transformer model performs competitively under all-in-one restoration settings.

## Discussion & Implications ^sec-discussion

**Off-topic** — a pure computer-vision (image restoration) paper where "digital twins" appears only as a motivating application domain. No AECO built-environment content. Recommend exclusion / strong relevance demotion.

## Notes ^sec-notes

- **Screening:** Retained by keyword — image restoration for ITS/DT; **non-AECO (computer vision)**.
- **Relevance:** Very low; recommend exclusion / demotion.
- **Source:** Hybrid OA; abstract-grounded (truncated), full text pending (PDF in library).
