# Hussain, M et al. (2024) — Predicting degraded lifting capacity of aging tower cranes: A digital twin-driven approach

- **ID:** R746 | **Source:** Scopus | **DOI:** 10.1016/j.aei.2023.102310
- **Journal:** Advanced Engineering Informatics
- **Authors:** Hussain M.; Ye Z.; Chi H.-L.; Hsu S.-C.

## Abstract summary
Aging tower cranes face an elevated risk of failure, primarily due to structural fatigue and deterioration. Surprisingly, the degradation of aging-induced lifting capacity (LC) remains an unexplored domain. In response to this research gap, this paper introduces a digital twin-driven (DTD) framework and model to predict the degraded LC of aging tower cranes. This framework combines theoretical and numerical analysis of fatigue and degradation behavior in tower cranes with real-time vibration data obtained during cyclic load scenarios on the actual cranes. Machine learning (ML) techniques are employed to develop a model that accurately predicts the degraded LC caused by aging. A scaled-down tower crane prototype is adopted as a demonstrative case to illustrate the feasibility and effectiveness of the DTD framework. The DTD model predicts the degraded LC of the prototype with high accuracy…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** DT-driven prediction of tower crane degraded lifting capacity

## Step-3 Deep-Read Coding (Prompt B)
| P DT-subject | Q DfS/DfQ | R codable | U Tier | V Design | W Constr | X Oper | Z DfX | AA Self-improve | AB Methodology | AC Modality | AD Validation | AE QA(0-5) | AF Cluster |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow (one-way physical to virtual) | 0 | 0 | 1 | Design for Safety (DfS) | None | Other / Mixed | Multi (two or more data types) | Simulation | 3 | Predictive analytics / decision support |

| AC1 fusion depth | AC2 fusion evidence | AC3 confidence |
|---|---|---|
| Fused | Theoretical fatigue analysis and real-time vibration data are fused in the ML lifting-capacity predictor. | Medium |

**Key evidence (AG):** Digital twin-driven prediction of degraded lifting capacity of aging tower cranes (PolyU, Advanced Engineering Informatics 2024): theoretical/numerical fatigue and degradation analysis combined with real-time vibration data from cyclic load scenarios; ML model predicts degraded LC (MSE 0.2253, R2 0.9973; k-5 cross-validation R2 0.9714); degraded load charts for each decade of usage (0-70 years) assist operators in applying safe loads. Scaled-down prototype demonstrator; prediction assists decisions, no actuation.

*Full-text source: browser-oa*

**AH — strength & gap filled:** First DTD model predicting aging-induced degraded lifting capacity with high accuracy (R2 0.9973) and decadal degraded load charts for crane operators.

**AI — deficiencies & future work:** Scaled-down prototype rather than in-service crane; vibration noise/uncertainty handling limited.
