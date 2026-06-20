---
ref: ""
citekey: "Shi-Qiu2023"
title: "Fine-Grained Point Cloud Semantic Segmentation of Complex Railway Bridge Scenes from UAVs Using Improved DGCNN"
authors: "Shi Qiu; Xianhua Liu; Jun Peng; Weidong Wang; Jin Wang; Sicheng Wang; Jianping Xiong; Wenbo Hu"
year: 2023
journal: "Structural Control and Health Monitoring"
doi: "10.1155/2023/3733799"
zotero_key: "YQ47YXFC"
zotero_status: abstract-grounded
last_verified: "2026-06-15"
tags: ["Bridge", "Digital-Twin", "Infrastructure", "Point-Cloud", "Quality", "Railway", "Semantic", "Unsorted", "source: lens"]
---
# Shi-Qiu2023 — Fine-Grained Point Cloud Semantic Segmentation of Complex Railway Bridge Scenes from UAVs Using Improved DGCNN

| Field | Value |
|-------|-------|
| **Ref** | — |
| **Authors** | Shi Qiu; Xianhua Liu; Jun Peng; Weidong Wang; Jin Wang; Sicheng Wang; Jianping Xiong; Wenbo Hu |
| **Year / Venue** | 2023 · *Structural Control and Health Monitoring* |
| **DOI** | [10.1155/2023/3733799](https://doi.org/10.1155/2023/3733799) |
| **Zotero** | `YQ47YXFC` |
| **Screening** | V1: digital twin \| V2: infrastructure|bridge|railway \| V3: quality|semantic|point cloud |

## Abstract ^sec-abstract

Automatic semantic segmentation of point clouds in railway bridge scenes is a crucial step in the digitization process and is required for a variety of subapplications including digital twin reconstruction and component geometric quality verification. This paper details a method for reliably and effectively segmenting point clouds acquired from complex railway bridge scenes by unmanned aerial vehicles (UAVs). The method involves segmenting seven common infrastructure elements in railway bridge point clouds using an improved DGCNN after processing low-quality point clouds from UAVs with a score-based denoising algorithm. The segmentation performance of the network is measured by averaging the intersection to union ratio between the segmentation results and the true labels of different elements, i.e., the mean intersection over union (mIoU). The proposed method is evaluated on three different scenes of railway bridges and achieved mIoU values of 99.18%, 90.76%, and 85.84%, respectively, at three levels of complexity ranging from easy to difficult. The results demonstrate that the proposed method captures the most discriminative features from low-quality point clouds, allowing for the accurate and efficient digital representation of railway bridge scenes.

## Introduction & Background ^sec-intro

Automatic semantic segmentation of point clouds in railway bridge scenes is crucial for digitization including **digital twin reconstruction** and component geometric quality verification.

## Method ^sec-method

Improved DGCNN segments seven common infrastructure elements after score-based denoising of low-quality UAV point clouds. Evaluated on three complexity levels.

## Key Findings ^sec-results

mIoU values of 99.18%, 90.76%, and 85.84% at easy to difficult complexity levels. Method captures discriminative features from low-quality point clouds for accurate DT representation.

## Discussion & Implications ^sec-discussion

**Domain-adjacent** — a railway bridge point-cloud segmentation for DT. Methodologically relevant to scan-to-DT; cite peripherally.

## Notes ^sec-notes

- **Screening:** Retained — point cloud + DT + railway bridge; domain-adjacent.
- **Relevance:** Moderate; cite for point-cloud DT segmentation.
- **Source:** Gold OA; abstract-grounded, full text pending (PDF in library).
