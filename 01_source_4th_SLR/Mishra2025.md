# Mishra, N et al. (2025) — EDGE EMPOWERED DIGITAL TWIN ARCHITECTURE FOR REAL-TIME STRUCTURAL HEALTH MONITORING OF SMART BRIDGES

- **ID:** R558 | **Source:** Scopus | **DOI:** 10.70102/afts.2025.1834.178
- **Journal:** Archives for Technical Sciences
- **Authors:** Mishra N.; Soy A.

## Abstract summary
Urban infrastructure, especially smart bridges, is growing rapidly, requiring effective solutions to ensure structural integrity. Conventional Structural Health Monitoring (SHM) systems have limitations in scalability, speed, and accuracy. This paper presents a new edge-enabled digital twin platform for real-time SHM of smart bridges, combining IoT, cloud computing, and edge computing. The architecture offers a high-performance, decentralized scheme of continuous monitoring to facilitate real-time detection and forecasting of structural failure by integrating the sensors on the bridges and the edge devices. The fundamental approach uses an Autoencoder-based anomaly detection, in which Autoencoders are trained to learn to recreate sensor information, and learn to behave normally by modeling the structural behavior of the bridge. In the case of real-time monitoring, the differences between…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** Edge-empowered DT for real-time SHM of smart bridges

## Step-3 Deep-Read Coding (Prompt B)
| P DT-subject | Q DfS/DfQ | R codable | U Tier | V Design | W Constr | X Oper | Z DfX | AA Self-improve | AB Methodology | AC Modality | AD Validation | AE QA(0-5) | AF Cluster |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow (one-way physical to virtual) | 0 | 0 | 1 | Design for Safety (DfS) | None | Other / Mixed | Multi (two or more data types) | Simulation | 3 | Predictive analytics / decision support |

| AC1 fusion depth | AC2 fusion evidence | AC3 confidence |
|---|---|---|
| Fused | Edge-processed sensor streams and the autoencoder reconstruction are fused into one anomaly decision. | Low |

**Key evidence (AG):** Edge-empowered digital twin architecture for real-time bridge SHM (Kalinga U, Archives for Technical Sciences 2025): IoT + edge + cloud decentralised scheme; autoencoder-based anomaly detection compares reconstructed vs measured sensor data at the edge to flag structural problems and initiate maintenance actions; evaluated on five indicators (accuracy, processing time, energy, scalability, false-alarm rate) and reported better than traditional SHM. Architecture-level evaluation without a full real-bridge deployment; no actuation, no learning loop.

*Full-text source: browser-oa*

**AH — strength & gap filled:** Edge placement of autoencoder anomaly detection lowers latency/energy and false alarms versus cloud-only SHM, with explicit five-indicator evaluation.

**AI — deficiencies & future work:** Evaluation appears architectural/simulated without a full bridge deployment; autoencoder training data and false-alarm statistics limited.
