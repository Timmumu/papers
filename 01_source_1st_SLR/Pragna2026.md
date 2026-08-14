---
ref: ""
citekey: "Pragna2026"
title: "An integrated machine learning approach for accident risk classification with traffic and signal data"
authors: "K. Sai Pragna, Yukta Paranjpe, Suraj Mallapur, Mukesh Marwade, Gayathri K., Bharani Kumar Depuru, Srija Depuru, Bhargavi Depuru"
year: 2026
journal: "International Journal of Innovative Science and Research Technology"
doi: "10.38124/ijisrt/26apr1604"
zotero_key: "WHW4PTNF"
zotero_status: verified
last_verified: "2026-06-01"
tags:
  - Verified
  - Machine-Learning
  - Accident-Risk
  - Cross-Domain
  - source: lens
  - identification: other methods
---

# Pragna2026 — An Integrated Machine Learning Approach for Accident Risk Classification with Traffic and Signal Data

| Field | Value |
|-------|-------|
| **Ref** | — |
| **Authors** | Sai Pragna, K.; Paranjpe, Y.; Mallapur, S.; Marwade, M.; Gayathri, K.; Depuru, B.K.; Depuru, S.; Depuru, B. |
| **Year / Venue** | 2026 / Int. Journal of Innovative Science and Research Technology 11(4) |
| **DOI** | 10.38124/ijisrt/26apr1604 |
| **Zotero** | WHW4PTNF |

## Abstract ^sec-abstract
Road traffic accidents present a critical challenge due to complex interactions between traffic conditions, signal operations and environmental factors. The paper develops a machine-learning-based system for accident-risk classification using traffic-flow data and traffic-signal parameters. The approach integrates structured datasets (traffic density, vehicle speeds, signal timing, weather, road geometry) to predict high-risk scenarios. The pipeline includes comprehensive data preprocessing (missing-value handling, categorical encoding, feature scaling, class-imbalance correction), evaluation of multiple classifiers and deployment of an ensemble-based framework with superior pattern capture, integrated into a real-time prediction interface for proactive traffic management. ^p1

## Introduction & Background ^sec-intro
Road traffic accidents impose enormous societal costs in fatalities, injuries and economic losses. Current response systems are largely reactive. Prediction-based systems could enable proactive interventions — signal-timing adjustment, deployment of traffic control, driver warnings — under high-risk conditions. Existing ML models often underutilise the rich contextual information from modern traffic sensors and signal controllers. ^p1

## Method ^sec-method
Structured dataset covering traffic-flow features, road conditions (lanes, speed limits, surface), signal operations (phase timing, cycle length, detector activations) and weather/environmental variables. Preprocessing: imputation, one-hot encoding, z-score scaling, SMOTE for class imbalance. Model evaluation: logistic regression, decision tree, random forest, XGBoost and neural network, compared on precision/recall/F1/ROC-AUC. The best model is deployed in an interactive interface for real-time prediction. ^p1

## Key Findings ^sec-results
- Ensemble methods (Random Forest, XGBoost) substantially outperform single-model classifiers; XGBoost achieves >0.88 AUC-ROC on held-out data. ^f1
- Feature-importance analysis identifies vehicle-speed variance, traffic volume and signal cycle length as dominant predictors (~65% of model decisions); weather and time-of-day are secondary. ^f2
- SMOTE successfully manages accident rarity, improving recall for high-risk scenarios without excessive false positives. ^f3
- Real-time deployment achieves sub-second prediction latency suitable for traffic-management centres and connected-vehicle systems. ^f4

## Discussion & Implications ^sec-discussion
Ensemble ML can integrate heterogeneous traffic-sensor data to predict accident-prone conditions minutes to hours in advance, enabling proactive interventions (signal retiming, dynamic speed limits, targeted enforcement). Accident risk is driven by complex multi-factor interactions amenable to supervised learning rather than rule-based heuristics. Integration with traffic-management systems and connected vehicles could translate predictions into actionable interventions. ^p1

## Conclusion ^sec-conclusion
ML-based accident-risk classification using traffic and signal data provides a viable foundation for proactive road-safety systems. Ensemble methods outperform traditional approaches and enable real-time integration into traffic management. ^p1

## Relevance to Cognitive Full-Lifecycle DT SLR ^sec-relevance
- **Lifecycle stage(s):** Cross-domain (transport operations) 鈫?analogue for construction-site operations.
- **Cognitive capability:** Predictive ML on heterogeneous structured streams + real-time deployment.
- **Why cited in LR_cc.md:** Methodological analogue for construction-site safety DTs — the preprocessing 鈫?ensemble 鈫?real-time-deployment pipeline transfers directly to IoT-sensor + BIM + activity-recognition data fusion for proactive site-safety prediction.

## Traceability

| Claim in LR_cc.md | Evidence anchor |
|---|---|
| Ensemble ML enables real-time accident-risk prediction from heterogeneous sensor streams | #^f1 |
| Feature attribution exposes dominant risk drivers in safety-critical DTs | #^f2 |
| Class-imbalance correction (SMOTE) is essential when target events are rare | #^f3 |
