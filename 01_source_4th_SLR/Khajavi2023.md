# Khajavi, S.H et al. (2023) — Digital Twin for Safety and Security: Perspectives on Building Lifecycle

- **ID:** R723 | **Source:** Scopus | **DOI:** 10.1109/ACCESS.2023.3278267
- **Journal:** IEEE Access
- **Authors:** Khajavi S.H.; Tetik M.; Liu Z.; Korhonen P.; Holmstrom J.

## Abstract summary
As digital twins are gaining importance in various industries, research on their impact, use cases, and implementation in the field of construction is accelerating. In this study, we examine the impact of digital twins on building safety and security throughout their lifecycle, utilizing two state-of-the-art use cases for fire and anomaly detection. The solution employs advanced sensors, 3D visualizations for detecting safety and security threats, and data analysis to predict potential future threats. Using the data that was collected over a seventeen-month period, we present an implementation architecture for safety and security digital twins in buildings, explore the benefits and shortcomings of such a system, and discuss the learnings applicable to different lifecycle stages of a building. This paper contributes to the creation and study of a digital twin for fire safety, analyzing it…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** DT for building safety and security lifecycle; fire


## Step-3 Deep-Read Coding (Prompt B)
| P DT-subject | Q DfS/DfQ | R codable | U Tier | V Design | W Constr | X Oper | Z DfX | AA Self-improve | AB Methodology | AC Modality | AD Validation | AE QA(0-5) | AF Cluster |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow (one-way physical to virtual) | 0 | 0 | 1 | Design for Safety (DfS) | None | Digital Twin platform (no machine learning) | Multi (two or more data types) | Single case study | 4 | Design for Safety |

| AC1 fusion depth | AC2 fusion evidence | AC3 confidence |
|---|---|---|
| Fused | Advanced sensor packages (thermal, RGB, UV, motion) plus LiDAR-derived 3D models are combined with stated real-time data fusion for fire/anomaly detection in two 17-month deployments. | High |

**Key evidence (AG):** Real-world building digital twin for fire safety and anomaly detection (17 months of data, two use cases): advanced sensors + dimensionally-accurate 3D model + thermal camera sensors with real-time data fusion; features early fire/anomaly detection, fire localization and intensity evaluation, real-time incident data sharing, and fire-propagation simulation; data analysis predicts potential future threats. One-way sensing→visualization/simulation for operators; no automated actuation (integrating access-control actuation suggested as future work) and no learning loop.

*Full-text source: 04c-port*

**AH — strength & gap filled:** Fills the scarce real-world evidence gap on building safety DTs with two 17-month deployments: an office and a grain drying facility using Raspberry Pi sensor packages (thermal, RGB, UV, motion sensors), LiDAR-derived dimensionally accurate 3D models in Unity and WebGL, and Azure dashboards; normal operational signature analysis detects anomalies, localizes fires without triangulation, and a candle flame was detected in under one second.

**AI — deficiencies & future work:** Monitoring only with no actuation or closed control of building systems. Validation is limited to the use phase, with no case studies from other lifecycle phases, and no quantitative comparison of detection speed and accuracy against conventional fire detection methods. Cost, lack of adoption knowledge, and manual 3D model generation remain obstacles; these comparisons and lifecycle studies are future research.
