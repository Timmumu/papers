---
ref: ""
citekey: "Wenbo-Hu2024"
title: "Hybrid Pixel‐Level Crack Segmentation for Ballastless Track Slab Using Digital Twin Model and Weakly Supervised Style Transfer"
authors: "Wenbo Hu; Weidong Wang; Xianhua Liu; Jun Peng; Sicheng Wang; Chengbo Ai; Shi Qiu; Wenjuan Wang; Jin Wang; Qasim Zaheer; Lichang Wang"
year: 2024
journal: "Structural Control and Health Monitoring"
doi: "10.1155/2024/8846470"
zotero_key: "UTKQSJHY"
zotero_status: verified
last_verified: "2026-06-15"
tags: ["Deep-Learning", "Digital-Twin", "Inspection", "Maintenance", "Structural", "Unsorted", "source: lens", "identification: databases"]
---
# Wenbo-Hu2024 — Hybrid Pixel‐Level Crack Segmentation for Ballastless Track Slab Using Digital Twin Model and Weakly Supervised Style Transfer

| Field | Value |
|-------|-------|
| **Ref** | — |
| **Authors** | Wenbo Hu; Weidong Wang; Xianhua Liu; Jun Peng; Sicheng Wang; Chengbo Ai; Shi Qiu; Wenjuan Wang; Jin Wang; Qasim Zaheer; Lichang Wang |
| **Year / Venue** | 2024 · *Structural Control and Health Monitoring* |
| **DOI** | [10.1155/2024/8846470](https://doi.org/10.1155/2024/8846470) |
| **Zotero** | `UTKQSJHY` |
| **Screening** | V1: digital twin \| V2: structural \| V3: deep learning|maintenance|inspection |

## Abstract ^sec-abstract

Crack detection at the pixel level across complex scenarios (structural interference and adverse working conditions) is a critical consideration in the maintenance of ballastless track slab (BTS). Although existing deep learning models achieve acceptable accuracy on cracks with a monotonous background, the ground truth with high labor cost is inevitable and their performance in complex scenarios may fall far below their theoretical bounds or even cause “all‐black images.” A hybrid algorithm based on synthetic data from digital twin model and weakly supervised style transfer is proposed in this paper for addressing the above challenges. The algorithm uses a region‐attention strategy to enable the uncontrolled generative adversarial network (GAN) focusing its attention on weak labels containing crack regions, directly obtaining segmentation results with the same style as the ground truth of the crack forest dataset. In addition, a digital twin model that can simulate the real inspection working conditions is established to generate a synthetic crack dataset, enabling the hybrid algorithm to extract the most discriminative features. The results show that the performance of the hybrid algorithm on inspection images across complex scenarios is nearly 25% higher than that of the DeepLabv3+ network, while the time cost consumed is only 0.5% of the latter. The deployment of the region attention strategy also enables the hybrid algorithm to achieve a mean intersection of union (MIoU) of 79.38%, which is nearly twice as much as that of GAN. It not only eliminates the oversegmentation caused by structures such as rails and fastener systems but also overcomes “all‐black images.” In addition, synthetic data can greatly enlarge the range, type, and number of discriminative crack features compared with data augmentation based on limited real data, thus enhancing the performance of the hybrid algorithm for uncertain inspection data. Particularly, the fully trained hybrid algorithm based on the synthetic dataset shows good adaptability and generalization to adverse working conditions such as uneven lighting, noise, and blur.

## Introduction & Background ^sec-intro

Crack detection for ballastless track slab (BTS) maintenance faces challenges in complex scenarios. A **hybrid algorithm based on synthetic data from a digital twin model** and weakly supervised style transfer is proposed.

## Method ^sec-method

A DT model simulates real inspection conditions to generate synthetic crack datasets. Region-attention strategy focuses weak labels on crack regions; GAN produces segmentation directly. Compared with DeepLabv3+.

## Key Findings ^sec-results

Performance nearly **25% higher than DeepLabv3+** with only 0.5% of the time cost. MIoU of 79.38%, nearly twice GAN alone. Eliminates oversegmentation and "all-black images." Synthetic data greatly enlarges discriminative crack features.

## Discussion & Implications ^sec-discussion

**Domain-adjacent** — a railway-track crack-detection DT methodology. Methodologically relevant to synthetic-data DT for inspection; cite peripherally.

## Notes ^sec-notes

- **Screening:** Retained — DT + crack detection + GAN + railway; domain-adjacent.
- **Relevance:** Moderate; cite for DT-synthetic-data crack detection methodology.
- **Source:** Gold OA; abstract-grounded, full text pending.
