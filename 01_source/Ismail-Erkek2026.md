---
ref: ""
citekey: "Ismail-Erkek2026"
title: "Explainable digital twin–driven ensemble anomaly detection framework for cyber-physical infrastructure security"
authors: "Ismail Erkek; Erdal Irmak"
year: 2026
journal: "International Journal of Information Security"
doi: "10.1007/s10207-026-01274-6"
zotero_key: "HHX4S7FQ"
zotero_status: abstract-grounded
last_verified: "2026-06-15"
tags: ["CPS", "Deep-Learning", "Digital-Twin", "Infrastructure", "Monitoring", "Sensor", "Unsorted", "source: lens"]
---
# Ismail-Erkek2026 — Explainable digital twin–driven ensemble anomaly detection framework for cyber-physical infrastructure security

| Field | Value |
|-------|-------|
| **Ref** | — |
| **Authors** | Ismail Erkek; Erdal Irmak |
| **Year / Venue** | 2026 · *International Journal of Information Security* |
| **DOI** | [10.1007/s10207-026-01274-6](https://doi.org/10.1007/s10207-026-01274-6) |
| **Zotero** | `HHX4S7FQ` |
| **Screening** | V1: digital twin|cyber-physical \| V2: infrastructure \| V3: deep learning|monitoring|sensor|anomaly |

## Abstract ^sec-abstract

Abstract ; Cyber-physical infrastructures require early and trustworthy detection of abnormal behavior caused by cyber intrusions, sensor manipulation, and operational faults. This study proposes an explainable digital twin–driven ensemble anomaly detection framework for cyber-physical infrastructure security. The core of the framework is a physics-informed, hybrid regression-based digital twin that estimates expected nominal system behavior by combining historical operational data with plant-specific process relationships. Deviations between physical measurements and digital twin outputs are transformed into anomaly-sensitive features and analyzed by a heterogeneous ensemble of unsupervised detectors, including Isolation Forest, Elliptic Envelope, One-Class Support Vector Machine, and Local Outlier Factor. Their binary outputs are fused through a weighted voting strategy to improve robustness against heterogeneous anomaly patterns and to reduce false alarms. To support transparent decision making, a SHAP-based explainability layer is integrated for global and local feature attribution and root-cause interpretation. The framework is validated on a hydroelectric power plant digital twin using controlled fault-injection scenarios. The digital twin prediction layer demonstrates low error before deviation calculation, confirming its suitability as a nominal behavioral reference. In addition, the proposed ensemble is benchmarked against deep learning baselines, including a dense autoencoder and an LSTM autoencoder, and shows a more favorable balance in terms of F1-score, false alarm rate, and accuracy. The results indicate that the proposed approach provides a robust, interpretable, and practically reliable anomaly detection framework for cybersecurity-oriented monitoring of critical cyber-physical infrastructure.

## Introduction & Background ^sec-intro

Cyber-physical infrastructures need early, trustworthy detection of abnormal behaviour from cyber intrusions, sensor manipulation, and operational faults. The study proposes an explainable digital-twin-driven ensemble anomaly-detection framework for CPS security.

## Method ^sec-method

The core is a physics-informed, hybrid regression-based DT estimating nominal system behaviour from historical data plus plant-specific process relationships. Deviations between measurements and DT outputs become anomaly-sensitive features analysed by an unsupervised ensemble (Isolation Forest, Elliptic Envelope, One-Class SVM, Local Outlier Factor), fused via weighted voting. A SHAP-based explainability layer provides global/local attribution and root-cause interpretation. Validation uses a hydroelectric power-plant DT with controlled fault injection.

## Key Findings ^sec-results

The DT prediction layer shows low error as a nominal reference; the ensemble outperforms deep-learning baselines (dense and LSTM autoencoders) on the balance of F1-score, false-alarm rate, and accuracy — a robust, interpretable anomaly-detection framework.

## Discussion & Implications ^sec-discussion

A strong exemplar of **explainable, physics-informed DT for anomaly detection** — relevant to the cognitive-DT (interpretability, hybrid models) and DT-security themes. Domain is hydroelectric CPS (infrastructure-adjacent).

## Notes ^sec-notes

- **Screening:** Retained — DT + anomaly detection + explainability (XAI/SHAP); CPS infrastructure.
- **Relevance:** Cite for explainable physics-informed DT and ensemble anomaly detection.
- **Source:** PDF available in Zotero library (full body not yet ingested).
