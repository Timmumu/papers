---
ref: ""
citekey: "Yihao-Ren2025"
title: "Hybrid Local-Feature-Based Approach for Automated Rail Extraction from Lidar Data"
authors: "Yihao Ren; Pan Lu; Chengbo Ai; Amin Keramati"
year: 2025
journal: "Transportation Research Record: Journal of the Transportation Research Board"
doi: "10.1177/03611981241311575"
zotero_key: "453QLA6G"
zotero_status: abstract-grounded
last_verified: "2026-06-15"
tags: ["AI", "Digital-Twin", "Infrastructure", "Quality", "Unsorted", "source: lens", "identification: databases"]
---
# Yihao-Ren2025 — Hybrid Local-Feature-Based Approach for Automated Rail Extraction from Lidar Data

| Field | Value |
|-------|-------|
| **Ref** | — |
| **Authors** | Yihao Ren; Pan Lu; Chengbo Ai; Amin Keramati |
| **Year / Venue** | 2025 · *Transportation Research Record: Journal of the Transportation Research Board* |
| **DOI** | [10.1177/03611981241311575](https://doi.org/10.1177/03611981241311575) |
| **Zotero** | `453QLA6G` |
| **Screening** | V1: digital twins \| V2: infrastructure \| V3: quality|artificial intelligence |

## Abstract ^sec-abstract

; Constructing 3-D rail models from observed lidar point clouds has gained growing interest in the railroad industry: 1) to create digital twins of infrastructure asset inventories; and 2) to continuously monitor infrastructure health conditions. Performance of the existing threshold-based and rules-based extraction methods not only depends on feature-specific properties such as retro-intensity, geometric design rules, and defined feature shapes but also relies on data quality and prior knowledge such as data resolution, scanning angle, and feature orientation. This research proposes a hybrid approach, combining both data-driven filtering algorithms and artificial intelligence (AI) model-based classification approaches for automatically generating 3-D rail models. The main objective is to develop an automatic and computationally efficient procedure for rail 3-D model reconstruction in a massive, noisy, and unevenly distributed railroad scene with high accuracy but without requiring: 1) prior knowledge; 2) high-density point data clouds; or 3) feature-specific global features. In this paper, we develop and compare three hybrid procedures by using data collected by the Federal Railroad Administration (FRA) with a point density of 293 pt/m; 2 ; . Both pointwise and lengthwise evaluations were used to evaluate the robustness of the proposed methods. The pointwise evaluation shows an average precision, recall, f1, and intersection over union (IoU) of 0.989, 0.747, 0.852, and 0.741, respectively. The lengthwise evaluation shows average correctness, completeness, and quality of 99.32%, 94.69%, and 94.06%, respectively. The proposed automated, configuration-independent, and global-feature-free method shows its efficient and effective rail extraction capabilities with low-density point clouds for complicated railroad terrains.;

## Introduction & Background ^sec-intro

Constructing 3D rail models from LiDAR point clouds has gained interest in the railroad industry for creating **digital twins of infrastructure asset inventories** and continuously monitoring infrastructure health. Existing threshold/rule-based methods depend on feature-specific properties, data quality, and prior knowledge.

## Method ^sec-method

A **hybrid approach combining data-driven filtering algorithms and AI model-based classification** for automatic 3D rail-model reconstruction, without requiring prior knowledge, high-density point clouds, or feature-specific global features. Three hybrid procedures are developed and compared using Federal Railroad Administration data (293 pt/m²).

## Key Findings ^sec-results

Pointwise evaluation: average precision 0.989, recall 0.747, F1 0.852, IoU 0.741. Lengthwise evaluation: correctness 99.32%, completeness 94.69%, quality 94.06%. The method is efficient and effective for low-density point clouds in complicated railroad terrains.

## Discussion & Implications ^sec-discussion

**Domain-adjacent** — railroad infrastructure LiDAR+AI for DT asset inventory. Methodologically relevant to the scan-to-DT and point-cloud-processing strands; cite peripherally.

## Notes ^sec-notes

- **Screening:** Retained — LiDAR + AI + rail DT; domain-adjacent.
- **Relevance:** Moderate; cite for hybrid LiDAR-AI rail extraction methodology.
- **Source:** Abstract-grounded; full text pending.
