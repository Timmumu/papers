---
ref: ""
citekey: "Gang-Yu2020"
title: "Prediction of Highway Tunnel Pavement Performance Based on Digital Twin and Multiple Time Series Stacking"
authors: "Gang Yu; Shuang Zhang; Min Hu; Y. Ken Wang"
year: 2020
journal: "Advances in Civil Engineering"
doi: "10.1155/2020/8824135"
zotero_key: "WU2JWWKC"
zotero_status: verified
last_verified: "2026-06-15"
tags: ["BIM", "Building", "Digital-Twin", "Highway", "ML", "Maintenance", "Tunnel", "Unsorted", "source: lens", "identification: databases"]
---
# Gang-Yu2020 — Prediction of Highway Tunnel Pavement Performance Based on Digital Twin and Multiple Time Series Stacking

| Field | Value |
|-------|-------|
| **Ref** | — |
| **Authors** | Gang Yu; Shuang Zhang; Min Hu; Y. Ken Wang |
| **Year / Venue** | 2020 · *Advances in Civil Engineering* |
| **DOI** | [10.1155/2020/8824135](https://doi.org/10.1155/2020/8824135) |
| **Zotero** | `WU2JWWKC` |
| **Screening** | V1: digital twin|bim|building information modeling \| V2: building|tunnel|highway|pavement \| V3: machine learning|neural network|life cycle|maintenance |

## Abstract ^sec-abstract

The existing pavement performance prediction methods are limited to single-factor predictions, which often face the challenges of high cost, low efficiency, and poor accuracy. It is difficult to simultaneously solve the temporal, spatial, and exogenous dependencies between pavement performance data and maintenance, the service life of highways, the environment, and other factors. Digital twin technology based on the building information modeling (BIM) model, combined with machine learning, puts forward a new perspective and method for the accurate and timely prediction of pavement performance. In this paper, we propose a highway tunnel pavement performance prediction approach based on a digital twin and multiple time series stacking (MTSS). This paper (1) establishes an MTSS prediction model with heterogeneous stacking of eXtreme gradient boosting (XGBoost), the artificial neural network (ANN), random forest (RF), ridge regression, and support vector regression (SVR) component learners after exploratory data analysis (EDA); (2) proposes a method based on multiple time series feature extraction to accurately predict the pavement performance change trend, using the highway segment as the minimum computing unit and considering multiple factors; (3) uses grid search with the k-fold cross validation method to optimize hyperparameters to ensure the robustness, stability, and generalization ability of the prediction model; and (4) constructs a digital twin for pavement performance prediction to realize the real-time dynamic evolution of prediction. The method proposed in this study is applied in the life cycle management of the Dalian highway-crossing tunnel in Shanghai, China. A dataset covering 2010–2019 is collected for real-time prediction of the pavement performance. The prediction accuracy evaluation shows that the mean absolute error (MAE) is 0.1314, the root mean squared error (RMSE) is 0.0386, the mean absolute percentage error (MAPE) is 5.10%, and the accuracy is 94.90%. Its overall performance is better than a single model. The results verify that the prediction method based on digital twin and MTSS is feasible and effective in the highway tunnel pavement performance prediction.

## Introduction & Background ^sec-intro

Existing pavement performance prediction is limited to single-factor predictions. **Digital twin** technology based on BIM + machine learning proposes a new method for accurate pavement performance prediction.

## Method ^sec-method

Multiple Time Series Stacking (MTSS) with XGBoost, ANN, RF, ridge regression, SVR. Grid search with k-fold CV for hyperparameter optimization. DT for real-time dynamic evolution of prediction. Applied to Dalian highway-crossing tunnel, Shanghai (2010–2019 data).

## Key Findings ^sec-results

MAE=0.1314, RMSE=0.0386, MAPE=5.10%. DT enables real-time pavement performance prediction.

## Discussion & Implications ^sec-discussion

**Domain-adjacent** — a pavement DT prediction model. Methodologically relevant; cite peripherally.

## Notes ^sec-notes

- **Screening:** Retained — DT + pavement + MTSS; domain-adjacent.
- **Relevance:** Moderate; cite for DT pavement prediction.
- **Source:** Gold OA; abstract-grounded, full text pending (PDF in library).
