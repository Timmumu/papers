# Xiong, C et al. (2026) — Edge-cloud collaborative digital twin for vibration anomaly detection and localization in high-rise buildings

- **ID:** R405 | **Source:** Scopus | **DOI:** 10.1016/j.engstruct.2025.122061
- **Journal:** Engineering Structures
- **Authors:** Xiong C.; Zhu H.; Huang J.; Chen K.; Lai W.; Xie L.; Mei L.

## Abstract summary
Vibration accidents of high-rise buildings are frequently reported around the globe and the downtime of high-rise buildings for accident investigation can lead to substantial social and economic losses for stakeholders. This research developed an edge-cloud collaborative framework for vibration anomaly detection and vibration source localization. Firstly, a high-precision vibration sensor with wireless time synchronization and edge computing capability is introduced. Secondly, a vibration anomaly detection algorithm is proposed based on edge computing of sensor nodes. Thirdly, a vibration source localization algorithm is proposed based on cloud computing of a structural dynamics digital twin model. Finally, the effectiveness of the proposed methods is validated through a case study of a 17-story high-rise building, and the results indicate that vibration anomaly events can be reliably de…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** Edge-cloud DT for high-rise vibration anomaly detection

## Step-3 Deep-Read Coding (Prompt B)
| P DT-subject | Q DfS/DfQ | R codable | U Tier | V Design | W Constr | X Oper | Z DfX | AA Self-improve | AB Methodology | AC Modality | AD Validation | AE QA(0-5) | AF Cluster |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow (one-way physical to virtual) | 0 | 0 | 1 | Design for Safety (DfS) | None | Digital Twin platform (no machine learning) | Multi (two or more data types) | Single case study | 4 | Design for Safety |

| AC1 fusion depth | AC2 fusion evidence | AC3 confidence |
|---|---|---|
| Aligned | Wireless time-synchronised smart-sensor vibration data are mapped onto the cloud MDOF flexural-shear twin updated by SSI-COV and PSO, which then localises vibration sources by spectrum matching. | Medium |

**Key evidence (AG):** Edge-cloud collaborative digital twin for vibration anomaly detection and localization in high-rise buildings (Shenzhen U): wireless time-synchronized smart sensor (WTSS) with edge computing for anomaly detection; cloud server runs structural dynamics DT model for vibration source localization; BIM-based management platform for visualization; validated on 17-story high-rise teaching building with harmonic excitation tests. One-way monitoring→detection→localization; no actuation and no learning loop.

*Full-text source: 04c-port*

**AH — strength & gap filled:** Fills the gap of edge-cloud collaborative intelligence for vibration anomaly detection and localization in high-rise buildings: a wireless time-synchronized smart sensor with LoRa chain synchronization below 20 microseconds and edge STFT anomaly detection, plus a cloud MDOF flexural-shear digital twin updated by SSI-COV and PSO that localizes sources via spectrum amplitude feature matching, validated on a 17-story building under 82.9 N shaking-table excitation.

**AI — deficiencies & future work:** Localization reaches only zonal level with about one floor of error because adjacent-floor signatures are similar; the method covers only single-frequency steady-state excitations, edge nodes run only basic signal processing, and validation used one building with five sensors. Future work targets floor-specific identification, multi-source non-stationary vibration, and deep learning at the edge.
