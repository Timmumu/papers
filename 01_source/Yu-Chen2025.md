---
ref: ""
citekey: "Yu-Chen2025"
title: "Automated dimension estimation of bridge components using semantic segmentation and geometric fitting of point cloud data"
authors: "Yu Chen; Chao Lin; Xianfeng Li; Shiori Kubo; Tatsuro Yamane; Pang-jo Chun"
year: 2025
journal: "Engineering Structures"
doi: "10.1016/j.engstruct.2025.120837"
zotero_key: "6PN66QDF"
zotero_status: abstract-grounded
last_verified: "2026-06-15"
tags: ["Bridge", "Deep-Learning", "Infrastructure", "Point-Cloud", "Safety", "Semantic", "Structural", "Unsorted", "source: lens"]
---
# Yu-Chen2025 — Automated dimension estimation of bridge components using semantic segmentation and geometric fitting of point cloud data

| Field | Value |
|-------|-------|
| **Ref** | — |
| **Authors** | Yu Chen; Chao Lin; Xianfeng Li; Shiori Kubo; Tatsuro Yamane; Pang-jo Chun |
| **Year / Venue** | 2025 · *Engineering Structures* |
| **DOI** | [10.1016/j.engstruct.2025.120837](https://doi.org/10.1016/j.engstruct.2025.120837) |
| **Zotero** | `6PN66QDF` |
| **Screening** | V1: digital-twin \| V2: infrastructure|bridge|structural|structure \| V3: safety|semantic|deep learning|point cloud |

## Abstract ^sec-abstract

Accurate estimation of dimensions for bridge components is essential for maintaining infrastructure and ensuring safety. This study proposes an automated framework that integrates deep learning-based semantic segmentation with geometric analysis for bridge component dimension estimation from point cloud data. The framework comprises two main stages: (1) a semantic segmentation module based on the PointNet++ architecture with MSG, enhanced with the improved structure-oriented concept (SOC) for improved component recognition, and (2) a geometric processing pipeline that incorporates voxel-based downsampling, RANSAC plane fitting, and multi-stage filtering for robust dimension extraction. The improved SOC mechanism effectively utilizes the inherent spatial relationships of bridge components, significantly enhancing segmentation accuracy in complex structural contexts. The geometric processing pipeline employs an adaptive region-growing algorithm for component isolation, followed by principal component analysis for orientation alignment and dimension calculation. Validation experiments conducted on two bridge datasets of varying scales demonstrated the effectiveness of the framework, achieving an overall relative percentage error (RPE) of 5.05% and a strong correlation (Pearson r = 0.904) between predicted and actual measurements. The method consistently performed well across various components, across two datasets the framework achieved mean relative errors of 2.6 % (length) and 5.2 % (width) for smaller bridges and 6.9 % (length) and 5.5 % (width) for larger bridges, confirming both accuracy and scalability. Statistical Bland–Altman analysis showed minimal systematic bias, underscoring the method’s practical value for automated bridge inspection and digital-twin applications. • Proposed a robust framework for automated bridge component dimension estimation. • Achieved 5.05% RPE with strong scalability across small and large bridge structures. • Integrated multi-stage geometric processing pipeline for noise reduction and accuracy. • Validated framework using two diverse datasets with annotated bridge point clouds. • Adaptive parameter selection ensures consistency across varying structural scales.

## Introduction & Background ^sec-intro

Accurate estimation of bridge-component dimensions is essential for infrastructure maintenance and safety. The study proposes an automated framework integrating **deep-learning semantic segmentation with geometric analysis** for bridge-component dimension estimation from point-cloud data.

## Method ^sec-method

Two stages: (1) PointNet++ (MSG) semantic segmentation enhanced with an improved structure-oriented concept (SOC); (2) a geometric pipeline with voxel downsampling, RANSAC plane fitting, multi-stage filtering, adaptive region-growing, and PCA for orientation/dimension. Validated on two bridge datasets.

## Key Findings ^sec-results

Overall relative percentage error 5.05% with strong correlation (Pearson r = 0.904); mean relative errors 2.6%/5.2% (length/width) for smaller bridges and 6.9%/5.5% for larger; Bland–Altman shows minimal systematic bias — demonstrating accuracy and scalability for automated bridge inspection and **digital-twin applications**.

## Discussion & Implications ^sec-discussion

Relevant to the **scan-to-DT / point-cloud + deep learning** strand for bridges. A concrete data-acquisition/processing exemplar feeding infrastructure DTs.

## Notes ^sec-notes

- **Screening:** Retained — point cloud + DL segmentation + bridge DT (good fit).
- **Relevance:** Cite for automated point-cloud dimension extraction enabling bridge DTs.
- **Source:** Hybrid OA; abstract-grounded, full text pending.
