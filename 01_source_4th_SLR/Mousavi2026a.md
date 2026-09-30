# Mousavi, V et al. (2026) — A data-driven digital twin model for bridge health monitoring using feature fusion and unsupervised deep learning

- **ID:** R231 | **Source:** Scopus | **DOI:** 10.1016/j.inffus.2025.103534
- **Journal:** Information Fusion
- **Authors:** Mousavi V.; Rashidi M.; Ghazimoghadam S.; Samali B.

## Abstract summary
The progressive degradation of bridge infrastructure poses significant risks to transportation safety, necessitating advanced monitoring and management strategies. Digital Twins (DTs) have emerged as a transformative technology for real-time structural monitoring, offering a dynamic and data-driven representation of physical assets. When combined with Deep Learning (DL), DTs enhance predictive capabilities by leveraging vast amounts of sensor data to detect structural anomalies, optimize maintenance strategies, and improve decision-making processes. This synergy enables a more accurate, automated, and cost-effective approach to infrastructure health monitoring, ensuring timely interventions and prolonged service life. This paper presents a novel data-driven DT framework for real-time bridge damage detection, incorporating two key innovations. First, a Multi-Domain Fusion Autoencoder (MDF…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** MDFA unsupervised DT for bridge damage detection

## Step-3 Deep-Read Coding (Prompt B)
| P DT-subject | Q DfS/DfQ | R codable | U Tier | V Design | W Constr | X Oper | Z DfX | AA Self-improve | AB Methodology | AC Modality | AD Validation | AE QA(0-5) | AF Cluster |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow (one-way physical to virtual) | 0 | 0 | 1 | Design for Safety (DfS) | None | Other / Mixed | Single (one data type) | Cross-project (multiple real projects) | 4 | Predictive analytics / decision support |

| AC1 fusion depth | AC2 fusion evidence | AC3 confidence |
|---|---|---|
| Fused | Raw acceleration is fused with time-, frequency- and wavelet-domain features inside the MDFA autoencoder for one anomaly score. | High |

**Key evidence (AG):** Data-driven digital twin for bridge health monitoring (Western Sydney U, Information Fusion 2026): Multi-Domain Fusion Autoencoder (MDFA) fuses raw acceleration with time-, frequency- and wavelet-domain features for unsupervised anomaly detection; transformer-based GAN generates synthetic damage scenarios; validated on Werrington Bridge (Australia) and S101 Bridge (Austria) - all real damage scenarios identified and localised without retraining, outperforming conventional unsupervised methods. Real-time one-way sensor->detection->maintenance decisions; offline-trained, no actuation, no learning loop.

*Full-text source: browser-oa*

**AH — strength & gap filled:** MDFA multi-domain feature fusion plus transformer-GAN synthetic anomalies detects subtle damage on two real bridges and localises all S101 damage scenarios without retraining.

**AI — deficiencies & future work:** Two bridges only; synthetic-damage evaluation for one; no actuation or online model update; generalisation to other bridge types untested.
