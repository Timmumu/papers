---
ref: ""
citekey: "Kaixin-Hu2023"
title: "Semi-automated Generation of Geometric Digital Twin for Bridge Based on Terrestrial Laser Scanning Data"
authors: "Kaixin Hu; Daguang Han; Guocheng Qin; Yin Zhou; Long Chen; Chunli Ying; Tong Guo; Yanhui Liu"
year: 2023
journal: "Advances in Civil Engineering"
doi: "10.1155/2023/6192001"
zotero_key: "8PLQA95G"
zotero_status: verified
last_verified: "2026-06-15"
tags: ["Bridge", "Digital-Twin", "Maintenance", "Point-Cloud", "Quality", "Unsorted", "source: lens", "identification: databases"]
---
# Kaixin-Hu2023 — Semi-automated Generation of Geometric Digital Twin for Bridge Based on Terrestrial Laser Scanning Data

| Field | Value |
|-------|-------|
| **Ref** | — |
| **Authors** | Kaixin Hu; Daguang Han; Guocheng Qin; Yin Zhou; Long Chen; Chunli Ying; Tong Guo; Yanhui Liu |
| **Year / Venue** | 2023 · *Advances in Civil Engineering* |
| **DOI** | [10.1155/2023/6192001](https://doi.org/10.1155/2023/6192001) |
| **Zotero** | `8PLQA95G` |
| **Screening** | V1: digital twin|digital twins \| V2: bridge|site \| V3: quality|point cloud|maintenance |

## Abstract ^sec-abstract

Digital twins (DTs) have a great potential for bridge operation and maintenance. Geometric digital twins (gDTs) are the key component of DTs. At present, a growing number of researchers are using high-precision 3D laser point clouds to generate gDTs. However, for large bridges, such as arch, cable-stayed, and suspension bridges, comprehensive point-cloud collection stations are difficult to set up due to their large span, narrow site, and limited field of vision. Consequently, the complete point clouds of these bridges cannot be easily obtained. Thus, knowing how to process absence point clouds and generate gDTs is an urgent problem. This study proposes a semiautomatic method of extracting geometric information of a bridge’s components in the absence of point clouds. First, an algorithm based on the combination of the iterative polynomial fitting curve and sliding window is developed to extract the arch ring accurately. Second, an improved random sample consensus (RANSAC) algorithm based on distribution density is adopted to extract the cross sections of the arch bridge components, except the arch ring. For cross sections that lack point clouds, a translation strategy is used to supplement the unknown line segment. Finally, for the T-beam, a model alignment method is proposed to best match the characteristic intersections extracted by the improved RANSAC algorithm and the points corresponding to the design model. The quality of the generated models is gauged using a point cloud deviation chromatogram. In addition, the stressed component piers are compared with its design parameters to verify the accuracy of the proposed method. Results show that our method can efficiently and accurately extract geometric information and generate gDT for the bridge.

## Introduction & Background

**Geometric digital twins (gDTs)** are key for bridge O&M. For large bridges, complete point-cloud collection is difficult. The study proposes a semiautomatic method for extracting geometric information in the absence of point clouds.

## Method

Iterative polynomial fitting curve + sliding window extracts arch ring. Improved RANSAC based on distribution density extracts cross sections. Translation strategy supplements missing segments. Model alignment method for T-beam.

## Key Findings

Efficiently and accurately extracts geometric information and generates gDT for bridges. Quality gauged via point cloud deviation chromatogram. Piers compared with design parameters verify accuracy.

## Discussion

**Highly relevant** — a gDT method for bridges with missing point cloud data. Directly informs the scan-to-DT strand.

## Notes

- **Screening:** Retained — gDT + bridge + incomplete point cloud (strong fit).
- **Relevance:** High; cite for geometric DT from incomplete point clouds.
- **Source:** Gold OA; abstract-grounded, full text pending.
