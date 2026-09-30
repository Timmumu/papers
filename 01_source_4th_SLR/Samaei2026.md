# Samaei, S.R et al. (2026) — Field-Validated Digital Twin–Enabled Structural Health Monitoring for Offshore High-Pile Wharves

- **ID:** R123 | **Source:** Scopus | **DOI:** 10.70917/fce-2026-010
- **Journal:** Future Cities and Environment
- **Authors:** Samaei S.R.; Riffat J.

## Abstract summary
Offshore high-pile wharves operate under harsh, variable loads that can mask the earliest signs of deterioration. We present a closed-loop structural health monitoring (SHM) framework that couples multimodal machine/deep learning with a physics-based digital twin (DT). A year-long field deployment at an operating high-pile wharf in Western Asia instrumented six piles with triaxial accelerometers and strain gauges (GPS-synchronized, 100 Hz). After quality control and environmental/operational variability normalization, an unsupervised VAE produces an anomaly score that is fused with a CNN–GNN classifier to yield window-level damage probabilities and pile-by-elevation localization. The DT assimilates these diagnostics through weighted least squares and an EKF, with measurement covariance derived from model uncertainty; “what-if” simulations quantify the structural consequence of candidate …

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** Offshore high-pile wharf SHM with physics DT; safety

## Step-3 Deep-Read Coding (Prompt B)
| P DT-subject | Q DfS/DfQ | R codable | U Tier | V Design | W Constr | X Oper | Z DfX | AA Self-improve | AB Methodology | AC Modality | AD Validation | AE QA(0-5) | AF Cluster |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow (one-way physical to virtual) | 0 | 0 | 1 | Design for Safety (DfS) | Implemented | Other / Mixed | Multi (two or more data types) | Single case study | 4 | Predictive analytics / decision support |

| AC1 fusion depth | AC2 fusion evidence | AC3 confidence |
|---|---|---|
| Fused | VAE anomaly scores are fused with CNN-GNN classifier outputs into window-level damage probabilities, and diagnostics are assimilated with physics via EKF into one twin state. | High |

**Key evidence (AG):** Closed-loop SHM digital twin for offshore high-pile wharves (Islamic Azad U/WSSET, Future Cities and Environment 2026): 12-month field deployment instrumented six piles with triaxial accelerometers and strain gauges (GPS-synchronised, 100 Hz); unsupervised VAE anomaly score fused with CNN-GNN classifier for window-level damage probabilities and pile-by-elevation localisation; DT assimilates diagnostics via weighted least squares + EKF with model-uncertainty-derived covariance; what-if simulations quantify repair consequences; F1 0.95, AUC-ROC 0.98, false-alarm 2-5%, median detection latency ~45 s; online updating reduces frequency bias 4.8%->0.9% and raises mode-shape MAC 0.81->0.92. Monitoring->diagnostics->risk-informed maintenance planning (no actuation); online model updating implemented, no convergence criterion.

*Full-text source: browser-oa*

**AH — strength & gap filled:** Closes the loop between multimodal DL diagnostics and continuous physics-based model updating on a real operating wharf: EKF assimilation with field-derived uncertainty cuts frequency bias to 0.9% and lifts MAC to >=0.92, with 45 s median detection latency and 2-5% false alarms.

**AI — deficiencies & future work:** Single wharf deployment; VAE-CNN-GNN fusion weights and EKF tuning details partially reported; what-if repair scenarios are diagnostic, not actuated; long-term drift under extreme storms unverified.
