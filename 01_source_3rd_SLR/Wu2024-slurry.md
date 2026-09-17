# Wu et al. (2024) — Multisource information fusion for real-time prediction and multiobjective optimization of large-diameter slurry shield attitude

- **ID:** 3981 | **Source:** Web of Science | **DOI:** 10.1016/j.ress.2024.110305
- **Journal:** RELIABILITY ENGINEERING & SYSTEM SAFETY
- **Authors:** Wu, X. G.; Wang, J. Y.; Feng, Z. B.; Chen, H. Y.; Li, T. J.; Liu, Y.

## Abstract summary
Abnormal large-diameter slurry shield attitudes (SA) lead to safety and quality problems in shield construction. To achieve intelligent prediction and optimization of the large-diameter slurry SA, a combination of Bayesian optimization categorical boosting (BO-CatBoost) and a multiobjective evolutionary algorithm based on decomposition (MOEAD) is proposed for the prediction and optimization of the tunnel large-diameter slurry SA, as well as the corresponding digital twin framework. Using the Yangtze River large-diameter slurry shield project in Wuhan as an example, data were collected for three soil conditions, namely, silty fine sand, angular gravelly soils and chalky clays, and gravelly soil. The results show that: (1) The R2 values of the three predicted types of soils are all above 0.9, the RMSE values are less than 1.2, and the MAE values are less than 0.9. (2) Based on the results …

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** DT framework for slurry shield attitude prediction/optimization; safety & quality

## Step-3 Deep-Read Coding (Prompt B)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow (one-way physical to virtual) | 0 | 1 | 0 | Design for Safety (DfS) | None | Other / Mixed | Multi (two or more data types) | Single case study | 4 | Predictive analytics / decision support |

**Key evidence (AG):** Multisource information fusion for real-time prediction and multiobjective optimization of large-diameter slurry shield attitude (HUST): BO-CatBoost prediction model (R2 > 0.9, RMSE < 1.2, MAE < 0.9 across 3 soils) + MOEAD multiobjective optimization; SHAP identifies propulsive thrust as most influential; DT framework for SA control; validated on Yangtze River large-diameter slurry shield project (Wuhan). One-way monitoring→prediction→optimization; no actuation and no learning loop (offline-trained).


**Strength & gap filled (AH):** Combines prediction and optimization for large-diameter slurry shield attitude: Bayesian-optimized CatBoost maps 19 construction parameters to six attitude targets with R-squared above 0.9 on three soils of the Yangtze River tunnel in Wuhan, SHAP finds push-group thrust dominant, and MOEAD multiobjective optimization improves attitude by up to 23.436 percent across five scenarios, embedded in a digital twin framework with warnings and parameter recommendations.

**Deficiencies & future work (AI):** The three studied soils are relatively uniform, so complex ground behavior is untested, penetration degree and tool size are ignored, and real-time monitoring data must be imported manually with no autonomous platform link. Future work will add more shield projects and soil types for generalizability and connect the monitoring platform so prediction and optimization run independently.
**Fusion depth (AC1):** Fused

**Fusion evidence (AC2):**
- **Data streams:** 19 construction-parameter streams (Yangtze River slurry shield, three soils).
- **Integration mechanism:** CatBoost jointly consumes the parameters to predict six attitude targets (R2 above 0.9), SHAP ranks push-group thrust as dominant, and MOEAD optimisation improves attitude by up to 23.436%.
- **Why this code:** a multi-input model whose output depends on many parameter streams simultaneously, so Fused.

**Confidence (AC3):** High - the CatBoost input structure is explicit.
(full-text source: Endnote)
