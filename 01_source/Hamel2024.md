---
ref: "[4]"
citekey: "Hamel2024"
title: "PMI-DT: Leveraging Digital Twins and Machine Learning for Predictive Modeling and Inspection in Manufacturing"
authors: "C. Hamel, M. M. Ahsan, S. Raman"
year: 2024
journal: "arXiv preprint arXiv:2411.01299"
zotero_key: "4B9RB46D"
zotero_status: verified
last_verified: "2026-05-25"
tags: ["Manufacturing", "Verified"]
---

# Hamel2024 —PMI-DT: Digital Twins and Machine Learning for Predictive Modeling and Inspection in Manufacturing

| Field | Value |
|-------|-------|
| **Ref** | —|
| **Authors** | Hamel, C.; Ahsan, M.M.; Raman, S. |
| **Year / Venue** | 2024 / Preprint |
| **DOI** | —|
| **Zotero** | 4B9RB46D |

## Abstract ^sec-abstract
Digital Twins (DTs) have become popular in Advanced Manufacturing because they enable real-time monitoring, predictive modelling and operational improvement. Integrating physical-system data into reliable predictive models —particularly for precision measurement and failure prevention —is still under-explored. The paper introduces a Predictive Maintenance and Inspection Digital Twin (PMI-DT) framework targeting precision measurement and predictive quality assurance for a 3D-printed 1—4 ACME bolt, using a CyberGage 360 vision-inspection system, SolidWorks and Microsoft Azure. Dimensional inspection data are combined with fatigue test results; Random Forest and Decision Tree models predict bolt failure with 100% accuracy on the test set, with Max Position (30%) and Max Load (24%) emerging as the dominant features. ^p1

## Introduction & Background ^sec-intro
Manufacturing DTs typically focus on real-time monitoring; predictive quality and maintenance still lack tight integration with high-resolution inspection data. The authors argue for a DT that fuses geometric inspection with mechanical test outcomes so failure modes can be anticipated, not just detected. ^p1

## Method ^sec-method
3D-printed ACME bolts are scanned with a CyberGage 360 vision system to capture dimensional deviations versus the SolidWorks model. Fatigue tests record failure positions and loads. The combined dataset (dimensional features + fatigue outcomes) is ingested into Microsoft Azure, where Random Forest and Decision Tree classifiers are trained and validated. Feature importance is extracted to identify dominant failure drivers. ^p1

## Key Findings ^sec-results
- RF and DT classifiers predicted bolt failure with 100% accuracy on the experimental dataset. ^f1
- Max Position (~30%) and Max Load (~24%) are the dominant predictors of failure. ^f2
- The end-to-end pipeline (vision inspection 鈫?cloud 鈫?ML 鈫?DT) reduces inspection time and supports proactive QA. ^f3

## Discussion & Implications ^sec-discussion
The PMI-DT illustrates the manufacturing-DT pattern most relevant to AECO: fuse high-fidelity inspection with physics-of-failure data and use ML to convert this into predictive decisions. The architecture transfers well to AECO components (bolts, welds, fa莽ade panels). ^p1

## Conclusion ^sec-conclusion
A cloud-hosted DT that fuses dimensional inspection with fatigue data enables high-accuracy failure prediction and predictive maintenance for manufactured components. ^p1

## Relevance to Cognitive Full-Lifecycle DT SLR ^sec-relevance
- **Lifecycle stage(s):** Manufacturing analogue 鈫?AECO fabrication/QA; predictive maintenance (operation).
- **Cognitive capability:** Predictive ML inside DT (data fusion + failure prediction + feature attribution).
- **Why cited in LR_cc.md:** Cross-domain exemplar of an ML-enabled predictive DT pattern; benchmarks what AECO predictive DTs should aim for.

## Traceability

| Claim in LR_cc.md | Evidence anchor |
|---|---|
| ML-enabled DTs deliver predictive QA/maintenance | #^f1 |
| Feature attribution exposes dominant failure drivers | #^f2 |
