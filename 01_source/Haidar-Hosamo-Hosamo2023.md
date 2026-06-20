---
ref: ""
citekey: "Haidar-Hosamo-Hosamo2023"
title: "Improving building occupant comfort through a digital twin approach: A Bayesian network model and predictive maintenance method"
authors: "Haidar Hosamo Hosamo; Henrik Kofoed Nielsen; Dimitrios Kraniotis; Paul Ragnar Svennevig; Kjeld Svidt"
year: 2023
journal: "Energy and Buildings"
doi: "10.1016/j.enbuild.2023.112992"
zotero_key: "CFSUJAEW"
zotero_status: abstract-grounded
last_verified: "2026-06-15"
tags: ["BIM", "Building", "Digital-Twin", "ML", "Ontology", "Predictive", "Quality", "Unsorted", "source: lens", "identification: databases"]
---
# Haidar-Hosamo-Hosamo2023 — Improving building occupant comfort through a digital twin approach: A Bayesian network model and predictive maintenance method

| Field | Value |
|-------|-------|
| **Ref** | — |
| **Authors** | Haidar Hosamo Hosamo; Henrik Kofoed Nielsen; Dimitrios Kraniotis; Paul Ragnar Svennevig; Kjeld Svidt |
| **Year / Venue** | 2023 · *Energy and Buildings* |
| **DOI** | [10.1016/j.enbuild.2023.112992](https://doi.org/10.1016/j.enbuild.2023.112992) |
| **Zotero** | `CFSUJAEW` |
| **Screening** | V1: digital twin|bim|building information modeling \| V2: building|buildings \| V3: quality|ontology|predictive|machine learning |

## Abstract ^sec-abstract

This study introduces a Bayesian network model to evaluate the comfort levels of occupants of two non-residential Norwegian buildings based on data collected from satisfaction surveys and building performance parameters. A Digital Twin approach is proposed to integrate building information modeling (BIM) with real-time sensor data, occupant feedback, and a probabilistic model of occupant comfort to detect and predict HVAC issues that may impact comfort. The study also uses 200000 points as historical data of various sensors to understand the previous building systems’ behavior. The study also presents new methods for using BIM as a visualization platform and for predictive maintenance to identify and address problems in the HVAC system. For predictive maintenance, nine machine learning algorithms were evaluated using metrics such as ROC, accuracy, F1-score, precision, and recall, where Extreme Gradient Boosting (XGB) was the best algorithm for prediction. XGB is on average 2.5% more accurate than Multi-Layer Perceptron (MLP), and up to 5% more accurate than the other models. Random Forest is around 96% faster than XGBoost while being relatively easier to implement. The paper introduces a novel method that utilizes several standards to determine the remaining useful life of HVAC, leading to a potential increase in its lifetime by at least 10% and resulting in significant cost savings. The result shows that the most important factors that affect occupant comfort are poor air quality, lack of natural light, and uncomfortable temperature. To address the challenge of applying these methods to a wide range of buildings, the study proposes a framework using ontology graphs to integrate data from different systems, including FM, CMMS, BMS, and BIM. This study’s results provide insight into the factors that influence occupant comfort, help to expedite identifying equipment malfunctions and point towards potential solutions, leading to more sustainable and energy-efficient buildings.

## Introduction & Background ^sec-intro

A **Digital Twin approach** integrates BIM with real-time sensor data, occupant feedback, and a probabilistic BN model of occupant comfort to detect and predict HVAC issues. Uses 200,000 historical sensor data points.

## Method ^sec-method

Nine ML algorithms evaluated (ROC, accuracy, F1, precision, recall) for predictive maintenance. XGB best algorithm (2.5% more accurate than MLP, up to 5% over others). Random Forest ~96% faster than XGBoost. Ontology graphs integrate FM, CMMS, BMS, and BIM data. Novel method uses standards to determine HVAC remaining useful life (+10% lifetime).

## Key Findings ^sec-results

Most important occupant comfort factors: poor air quality, lack of natural light, uncomfortable temperature. Framework generalisable to multiple buildings via ontology graphs.

## Discussion & Implications ^sec-discussion

**Very highly relevant** — a comprehensive BN-ML-DT occupant comfort framework with 9-algorithm comparison and ontology integration. Landmark citation for DT-FM.

## Notes ^sec-notes

- **Screening:** Retained — BN + ML + DT + comfort + ontology (exceptional fit).
- **Relevance:** Highest; cite for ML-DT comfort framework.
- **Source:** Hybrid OA; abstract-grounded, full text pending (PDF in library).
