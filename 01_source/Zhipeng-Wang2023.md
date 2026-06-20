---
ref: ""
citekey: "Zhipeng-Wang2023"
title: "Self-Attentive Local Aggregation Learning With Prototype Guided Regularization for Point Cloud Semantic Segmentation of High-Speed Railways"
authors: "Zhipeng Wang; Yixuan Geng; Limin Jia; Yong Qin; Yuanyuan Chai; Lei Tong; Keyan Liu"
year: 2023
journal: "IEEE Transactions on Intelligent Transportation Systems"
doi: "10.1109/tits.2023.3281352"
zotero_key: "QZG8MSP5"
zotero_status: abstract-grounded
last_verified: "2026-06-15"
tags: ["Construction", "Deep-Learning", "Digital-Twin", "Point-Cloud", "Railway", "Semantic", "Unsorted", "source: lens"]
---
# Zhipeng-Wang2023 — Self-Attentive Local Aggregation Learning With Prototype Guided Regularization for Point Cloud Semantic Segmentation of High-Speed Railways

| Field | Value |
|-------|-------|
| **Ref** | — |
| **Authors** | Zhipeng Wang; Yixuan Geng; Limin Jia; Yong Qin; Yuanyuan Chai; Lei Tong; Keyan Liu |
| **Year / Venue** | 2023 · *IEEE Transactions on Intelligent Transportation Systems* |
| **DOI** | [10.1109/tits.2023.3281352](https://doi.org/10.1109/tits.2023.3281352) |
| **Zotero** | `QZG8MSP5` |
| **Screening** | V1: digital twins \| V2: construction|railway \| V3: semantic|deep learning|point cloud |

## Abstract ^sec-abstract

Point cloud semantic segmentation for railway infrastructures is an essential step towards establishing railway digital twins. Deep learning-based methods have shown great potential in this field compared to traditional methods that rely on hand-crafted features. However, deep learning-based methods for railway point clouds still face typical challenges that need to be addressed. In this regard, we propose a novel learning framework named SALAProNet, which consists of a set of effective and concise modular solutions. The first challenge addressed is the massive data scale of railway point clouds, which makes it difficult to directly process large-scale point clouds due to memory limitations. To solve this problem, we adapt efficient random sampling in the network and propose the Self-Attentive Aggregation (SAA) module based on an attention mechanism to greatly expand the receptive field, which covers the unsampled points and successfully retains information in a high-dimensional feature space. The second challenge is fine-grained segmentation, where we propose the Local Geometry Embedding (LGE) module to embed local geometry. With the help of context information provided by SAA, the network can perform fine-grained segmentation for railway infrastructures. The third challenge is the insufficient generalization ability of the network, where we propose a Prototype Guided Regularization (PGR) method to guide the network to segment the point cloud among railways with different construction standards. This method enhances the network’s interpretability and improves its generalization ability. We have validated our proposed framework through experiments on different datasets, and it outperforms state-of-the-art approaches.

## Introduction & Background

Point cloud semantic segmentation for railway infrastructures is essential for establishing **railway digital twins**. SALAProNet framework proposed with modular solutions for massive data, fine-grained segmentation, and generalization.

## Method

Self-Attentive Aggregation (SAA) expands receptive field. Local Geometry Embedding (LGE) for fine-grained segmentation. Prototype Guided Regularization (PGR) for cross-standard generalization.

## Key Findings

Outperforms state-of-the-art on different datasets. Addresses all three railway point-cloud segmentation challenges.

## Discussion

**Domain-adjacent** — railway point-cloud segmentation for DT. Methodologically relevant; cite peripherally.

## Notes

- **Screening:** Retained — point cloud + DT + railway; domain-adjacent.
- **Relevance:** Moderate; cite for railway point-cloud DT segmentation.
- **Source:** Abstract-grounded; full text pending.
