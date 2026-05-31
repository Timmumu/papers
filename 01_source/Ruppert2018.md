---
ref: "[44]"
citekey: "Ruppert2020"
title: "Integration of real-time locating systems into digital twins"
authors: "T. Ruppert, J. Abonyi"
year: 2020
journal: "Journal of Industrial Information Integration 20, 100174"
doi: "10.1016/j.jii.2020.100174"
zotero_key: "IJUPSPJB"
zotero_status: verified
last_verified: "2026-06-01"
tags:
  - Verified
  - Digital-Twin
  - RTLS
  - Sensor-Fusion
  - Filename-Legacy
---

# Ruppert2020 — Integration of Real-Time Locating Systems into Digital Twins

> ℹ Filename `Ruppert2018.md` is a legacy artefact; the actual paper is Ruppert & Abonyi (2020) on RTLS+DT integration, not the earlier 'Operator 4.0 enabling technologies' survey. Filename retained to preserve existing wikilinks.

| Field | Value |
|-------|-------|
| **Ref** | [44] |
| **Authors** | T. Ruppert, J. Abonyi |
| **Year / Venue** | 2020 / Journal of Industrial Information Integration 20, 100174 |
| **DOI** | [10.1016/j.jii.2020.100174](https://doi.org/10.1016/j.jii.2020.100174) |
| **Zotero** | IJUPSPJB |


## Abstract ^sec-abstract
Cyber-physical model-based solutions should rely on Digital Twins in which simulations are integrated with real-time sensory and manufacturing data. The paper demonstrates how information fusion with Real-Time Locating Systems (RTLS) — combining position and acceleration data — supports simulation-based analysis of product-specific activity times. The proposed DT continuously predicts production status and feeds monitoring of production performance via real-time connections between the RTLS and adaptive simulation models. The case study uses Human Resource Effectiveness (HRE) analysis in an assembly process to demonstrate the resulting Simulation-4.0 concept. ^p1

## Method ^sec-method
Single industrial assembly case study; adaptive discrete-event simulation continuously updated from UWB RTLS streams (position + acceleration). The DT serves both online prediction and offline performance analysis. ^p1

## Key Findings ^sec-results

- RTLS-driven information fusion lets a DT continuously refine activity-time distributions instead of using static engineered estimates. ^f1

- Position + acceleration fusion outperforms position alone for distinguishing value-adding from non-value-adding activities. ^f2

- Adaptive simulation models, when fed by RTLS, can support both real-time performance monitoring and longer-horizon HRE analysis from the same data substrate. ^f3


## Discussion & Implications ^sec-discussion
A canonical reference for sensor-fusion-driven DTs in industrial settings; the architecture transfers directly to AECO contexts where worker/equipment positioning underpins safety and productivity DTs. ^p1

## Relevance to Cognitive Full-Lifecycle DT SLR ^sec-relevance
Lifecycle stage: operation/execution analogue (manufacturing). Used in LR_cc.md as a transferable template for RTLS-fed worker-safety and productivity DTs in construction. ^p1

## Traceability

| Claim in LR_cc.md | Evidence anchor |
|---|---|

| RTLS fusion enables continuous activity-time refinement | #^f1 |

| Position + acceleration fusion improves activity classification | #^f2 |
