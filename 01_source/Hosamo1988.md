---
ref: "[87]"
citekey: "Hosamo2022b"
title: "A digital twin predictive maintenance framework of air handling units based on automatic fault detection and diagnostics"
authors: "H. Hosamo, P. R. Svennevig, K. Svidt, D. Han, H. K. Nielsen"
year: 2022
journal: "Energy and Buildings 261, 111988"
doi: "10.1016/j.enbuild.2022.111988"
zotero_key: "ID2GIXE3"
zotero_status: verified
last_verified: "2026-06-01"
tags:
  - Verified
  - Digital-Twin
  - Predictive-Maintenance
  - HVAC
  - Filename-Legacy
---

# Hosamo2022b — Digital Twin Predictive Maintenance Framework for AHUs

> ℹ Filename `Hosamo1988.md` is a legacy artefact; canonical citekey is `Hosamo2022b` (paper is 2022). Filename retained to preserve existing wikilinks; consider renaming in a future cleanup pass.

| Field | Value |
|-------|-------|
| **Ref** | [87] |
| **Authors** | H. Hosamo, P. R. Svennevig, K. Svidt, D. Han, H. K. Nielsen |
| **Year / Venue** | 2022 / Energy and Buildings 261, 111988 |
| **DOI** | [10.1016/j.enbuild.2022.111988](https://doi.org/10.1016/j.enbuild.2022.111988) |
| **Zotero** | ID2GIXE3 |


## Abstract ^sec-abstract
HVAC systems are central to building energy consumption, and stable Air Handling Unit (AHU) operation is critical to efficiency and equipment life. The authors propose a Digital Twin predictive-maintenance framework for AHUs that integrates BIM, IoT and semantic technologies. Three modules are implemented: (i) fault detection in AHUs based on the APAR (Air Handling Unit Performance Assessment Rules) method, (ii) condition prediction via machine learning, and (iii) maintenance planning. The framework is validated on a real educational building in Norway using data from August 2019 to October 2021. ^p1

## Method ^sec-method
Design-science framework combining APAR rule-based fault detection with ML-based condition prediction and a BIM/IoT integration layer. Validation is a single longitudinal case study (24+ months of operational AHU data plus FM-system inspection and maintenance records). ^p1

## Key Findings ^sec-results

- Combining APAR rules with ML on continuously updated sensor data successfully detects AHU faults and predicts component degradation. ^f1

- Removing detected operating faults produced annual energy savings of several thousand USD on a single educational building. ^f2

- Semantic enrichment of BIM with IoT data is the structural enabler that lifts the DT from monitoring to predictive maintenance. ^f3


## Discussion & Implications ^sec-discussion
Empirically grounds the predictive-maintenance branch of the AECO DT literature and is one of the few studies that quantifies energy/cost savings rather than reporting only architectural feasibility. The framework is still pre-actuation (no automated control feedback to the BMS). ^p1

## Relevance to Cognitive Full-Lifecycle DT SLR ^sec-relevance
Lifecycle stage: operation & maintenance (HVAC). Used in LR_cc.md as evidence that ML-augmented DTs can shift O&M from reactive to predictive, but still stop short of autonomous actuation. ^p1

## Traceability

| Claim in LR_cc.md | Evidence anchor |
|---|---|

| APAR + ML on DT data enables predictive maintenance | #^f1 |

| Quantified energy savings from DT-detected faults | #^f2 |
