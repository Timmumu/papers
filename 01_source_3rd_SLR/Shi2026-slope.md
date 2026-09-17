# Shi et al. (2026) — The Research on the Construction Method of a Slope Digital Twin Model Driven by Surrogate Models

- **ID:** 3966 | **Source:** Web of Science | **DOI:** 10.1155/stc/8782403
- **Journal:** STRUCTURAL CONTROL & HEALTH MONITORING
- **Authors:** Shi, F. S.; Yuan, W.; Qin, X. Z.; Wang, W.; Wang, W.; Niu, Q. H.; Yin, C.; Wang, M.

## Abstract summary
In view of the shortcomings of traditional slope safety monitoring methods, such as low calculation efficiency and poor real-time performance, this paper proposes a digital twin modelling method for slopes based on a surrogate model. Through a stacking integrated learning model combined with a multidimensional error analysis mechanism and adaptive parameter optimisation strategy, a high-precision surrogate model for slope displacement prediction was constructed. Compared with the real displacement data obtained from laboratory experiments and digital image technology (DIC), the prediction error of the optimised surrogate model is reduced from 20% to 5%. In this study, a digital twin system of the Donglingxin landslide was successfully constructed, and the deformation process from 2010 to 2022 was dynamically displayed. The results show that the deformation of the Donglingxin landslide cl…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** Surrogate-model-driven slope DT; landslide deformation prediction

## Step-3 Deep-Read Coding (Prompt B) — full text verified via Endnote library (front-matter DOI/title match, coverage re-scan 2026-08-12)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow | 0 | 0 | 1 | Design for Safety (DfS) | Implemented | Statistical / change-point | Multi (two or more data types) | Single case study | 4 | Predictive analytics / decision support |

**Key evidence (AG):** Slope digital twin driven by an optimised surrogate model (stacking ensemble learning) for landslide safety monitoring: displacement prediction with multidimensional error analysis + adaptive parameter adjustment + model updating/retraining as a dynamic optimisation mechanism that "dynamically self-corrects against the Sim-to-Real gap"; error reduced 20% to 5% (validated with indoor loading + DIC experiments); Donglingxin landslide DT dynamically displays 2010-2022 deformation (acceleration-stabilisation, rate 12.5 to 15.5 to 11.8 mm/y). One-way monitoring to prediction/visualisation; implemented retraining loop but no convergence criterion/metric - AA=Implemented, not Convergence-characterised.

**Strength & gap filled (AH):** Fills the gap between real-time monitoring data and numerical simulation for slope safety: a stacking ensemble surrogate model (BP, RF, XGBoost, SVR, RBF) with multidimensional error analysis and adaptive parameter optimization predicts full-field displacement from limited monitoring points, reducing prediction error from 20 percent to 5 percent and reconstructing the 2010-2022 acceleration-stabilization deformation of the Donglingxin landslide at rates of 12.5-15.5-11.8 mm/y.

**Deficiencies & future work (AI):** Prediction results still differ from laboratory experiments because of numerical-simulation simplification and parameter uncertainty; validation covers one indoor DIC test and a single landslide, the surrogate learns from simulation rather than live sensor feedback, and the digital twin only visualizes and predicts without early-warning actuation or closed-loop control of the physical slope.

**Fusion depth (AC1):** Aligned

**Fusion evidence (AC2):**
- **Data streams:** limited monitoring-point displacement data (2010-2022, 12.5-15.5-11.8 mm/y) + indoor DIC experiment data.
- **Integration mechanism:** the stacking-ensemble surrogate (BP, RF, XGBoost, SVR, RBF) is trained on simulation and used to reconstruct full-field displacement from the monitoring points, with adaptive parameter updating; live sensor feedback is not part of the loop.
- **Why this code:** measured data are mapped onto the surrogate frame while inference runs in the model, so Aligned.

**Confidence (AC3):** Medium - the surrogate-monitoring linkage is explicit; the surrogate itself is simulation-trained.