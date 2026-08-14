---
ref: ""
citekey: "Linjun-Lu2026"
title: "Regional graph-based pavement condition data quality assessment in support of trustworthy highway infrastructure digital twins"
authors: "Linjun Lu; Yuandong Pan; Brian Sheil; Peihang Luo; Ioannis Brilakis"
year: 2026
journal: "Automation in Construction"
doi: "10.1016/j.autcon.2025.106603"
zotero_key: "ZD8U8DJ3"
zotero_status: abstract-grounded
last_verified: "2026-06-15"
tags: ["Digital-Twin", "Highway", "Infrastructure", "Maintenance", "Quality", "Road", "Unsorted", "source: lens", "identification: databases"]
---
# Linjun-Lu2026 — Regional graph-based pavement condition data quality assessment in support of trustworthy highway infrastructure digital twins

| Field | Value |
|-------|-------|
| **Ref** | — |
| **Authors** | Linjun Lu; Yuandong Pan; Brian Sheil; Peihang Luo; Ioannis Brilakis |
| **Year / Venue** | 2026 · *Automation in Construction* |
| **DOI** | [10.1016/j.autcon.2025.106603](https://doi.org/10.1016/j.autcon.2025.106603) |
| **Zotero** | `ZD8U8DJ3` |
| **Screening** | V1: digital twins \| V2: infrastructure|highway|road|pavement \| V3: quality|maintenance |

## Abstract ^sec-abstract

Pavement condition data plays a critical role in highway digital twins (DTs) for intelligent infrastructure management. However, automated condition surveys often contain abnormal measurements that, if left undetected, can distort deterioration modeling and compromise maintenance decision-making. Existing section-level abnormal data identification methods remain limited in accuracy, as they typically rely on statistical thresholds or temporal heuristics and overlook the spatial-temporal dependencies inherent in pavement data. To address this hurdle, this paper introduces a regional graph-based method for section-level data quality assessment. Specifically, it first groups neighboring road sections into homogeneous clusters based on their historical condition patterns. Subsequently, a Graph-Mamba Attention Network (GMAN) is utilized to capture spatial-temporal dependencies and identify abnormal data points within each cluster. A case study on the UK highway network showed that the proposed method significantly outperforms the existing methods, thus signifying its potential to enhance the trustworthiness of pavement data in highway DTs. • Digital twins (DTs) offer a promising solution for intelligent highway infrastructure management. • Data quality remains a critical challenge for trustworthy highway DT applications. • A regional graph-based method is proposed for section-level pavement condition data quality assessment. • The method was validated through a case study using real-world data from the UK highway network. • Experiments show the method outperforms existing approaches in accurately and reliably detecting abnormal data points.

## Introduction & Background ^sec-intro

Pavement condition data is critical for **highway digital twins (DTs)** in intelligent infrastructure management, but automated surveys contain abnormal measurements that, if undetected, distort deterioration modelling and maintenance decisions. Existing section-level identification relies on statistical thresholds/temporal heuristics and overlooks spatial-temporal dependencies.

## Method ^sec-method

A regional graph-based method groups neighbouring road sections into homogeneous clusters by historical condition patterns, then uses a **Graph-Mamba Attention Network (GMAN)** to capture spatial-temporal dependencies and identify abnormal data points within each cluster.

## Key Findings ^sec-results

Validated on the UK highway network, the method significantly outperforms existing approaches in accurately and reliably detecting abnormal data points, enhancing the trustworthiness of pavement data in highway DTs.

## Discussion & Implications ^sec-discussion

Relevant to the **DT data-quality/trustworthiness** and graph-learning strands (infrastructure DT). A concrete data-quality method strengthening DT reliability — useful for the data-trust discussion.

## Notes ^sec-notes

- **Screening:** Retained — highway DT + data quality + graph neural network (good fit).
- **Relevance:** Cite for DT data-quality assurance and spatio-temporal anomaly detection.
- **Source:** Hybrid OA; abstract-grounded, full text pending (PDF in library).
