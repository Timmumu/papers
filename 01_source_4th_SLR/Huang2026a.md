# Huang, C et al. (2026) — Research on an intelligent monitoring system for the entire tunnel construction process based on IoT and digital twin

- **ID:** R339 | **Source:** Scopus | **DOI:** 10.1051/ijmqe/2025014
- **Journal:** International Journal of Metrology and Quality Engineering
- **Authors:** Huang C.; Wan L.; Shi G.; Sun H.; Wang J.; Zhang C.

## Abstract summary
There are high-risk problems, such as peripheral rock instability and palm face collapse, during tunnel construction, and the traditional monitoring methods are difficult to meet the safety management needs due to sparse data and lagging response. This paper proposes an intelligent monitoring system for the whole process of tunnel construction based on Internet of Things (IoT) and digital twin, which integrates a multi-source sensor network, BIM dynamic modeling, and risk intelligent analysis. The system realizes an all-around perception of environment, equipment, and surrounding rock status through real-time fusion of heterogeneous data, and uses digital twin technology for 3D visualization and risk trend prediction. It adopts the improved D-S evidence theory for multi-source risk assessment, and improves the early warning accuracy through the effectiveness factor and conflict weakening…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** IoT + DT tunnel construction monitoring; risk warning

## Step-3 Deep-Read Coding (Prompt B)
| P DT-subject | Q DfS/DfQ | R codable | U Tier | V Design | W Constr | X Oper | Z DfX | AA Self-improve | AB Methodology | AC Modality | AD Validation | AE QA(0-5) | AF Cluster |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow (one-way physical to virtual) | 0 | 1 | 0 | Design for Safety (DfS) | None | Digital Twin platform (no machine learning) | Multi (two or more data types) | Single case study | 4 | Design for Safety |

| AC1 fusion depth | AC2 fusion evidence | AC3 confidence |
|---|---|---|
| Fused | Multi-source risk assessment uses improved D-S evidence theory with conflict weakening and a validity factor to fuse personnel, pipe-sheet, shield and environmental data into one belief-level risk output. | High |

**Key evidence (AG):** IoT+Digital Twin intelligent monitoring system for tunnel construction (Zhejiang Songyang): multi-source sensor network (environment, equipment, surrounding rock) + BIM dynamic modeling + risk intelligent analysis using improved D-S evidence theory (multi-source risk assessment with effectiveness factor and conflict weakening strategy); 100% monitoring coverage and 100% warning accuracy; captures palm face collapse and enclosing rock deformation time-sequence. One-way monitoring→risk assessment→early warning; no actuation and no learning loop (D-S evidence theory is rule-based fusion, not learning).

*Full-text source: 04c-port*

**AH — strength & gap filled:** Targets sparse and lagging manual tunnel monitoring with an IoT plus digital twin system on a shield tunnel beneath the Jinan High-Speed Train Depot: multi-source fusion of personnel, pipe-sheet, shield and environmental data into BIM dynamic modeling, improved D-S evidence theory with conflict weakening and a validity factor cutting belief interval length 0.37 to 0.14, capturing a palm face collapse; prediction errors under 1.9 MN thrust and 5.44 mm settlement.

**AI — deficiencies & future work:** Sensing equipment is exposed to humidity, dust and vibration, so measurements can drift and regular calibration is required, and future validation will quantify mean-time-to-failure and accuracy decline in real tunnel conditions; the authors also plan to optimize the fusion and prediction algorithms and extend the system to mine tunneling and urban underground space.
