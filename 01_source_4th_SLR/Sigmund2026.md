# Sigmund, Z et al. (2026) — Reducing Latency in Digital Twins: A Framework for Near-Real-Time Progress and Quality Reporting

- **ID:** R014 | **Source:** Scopus | **DOI:** 10.3390/buildings16071448
- **Journal:** Buildings
- **Authors:** Sigmund Z.; Završki I.; Marović I.; Vilibić K.

## Abstract summary
While Digital Twins offer transformative potential, their efficacy for real-time control is constrained by the slow data acquisition and the high computational intensity required to process raw datasets like point clouds. This paper identifies these critical bottlenecks—specifically the latency between data capture and actionable insight—and proposes a refined theoretical framework for near-real-time automated progress monitoring and quality reporting. Building on the findings of the NORMENG project and informing the subsequent AutoGreenTraC project, this research synthesizes state-of-the-art advancements in reality capture, including LIDAR, SfM-MVS, and 360-degree vision. The study highlights a fundamental divergence in stakeholder requirements: the need for millimeter-level precision in quality control versus the demand for high-velocity documentation for progress monitoring. A key inn…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** DT framework for near-real-time progress/quality reporting

## Step-3 Deep-Read Coding (Prompt B)
| P DT-subject | Q DfS/DfQ | R codable | U Tier | V Design | W Constr | X Oper | Z DfX | AA Self-improve | AB Methodology | AC Modality | AD Validation | AE QA(0-5) | AF Cluster |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow (one-way physical to virtual) | 0 | 1 | 0 | Both | None | Perception / Computer Vision | Multi (two or more data types) | Conceptual (no test) | 2 | Perception / Computer Vision |

| AC1 fusion depth | AC2 fusion evidence | AC3 confidence |
|---|---|---|
| Unclear | LiDAR, SfM-MVS and 360-degree streams are discussed within a tiered hierarchy but no fusion mechanism is implemented or tested (framework only). | Low |

**Key evidence (AG):** Technical note (Buildings 2026, U Zagreb): proposes a tiered edge-cloud processing framework for near-real-time automated progress monitoring and quality reporting, synthesising NORMENG field metrics (terrestrial LiDAR, UAS photogrammetry, 360-degree vision); shifts to neural rendering to bypass photogrammetric latency; lightweight edge analysis for immediate safety/progress alarms plus asynchronous high-fidelity DT updates as single source of truth. Framework only - no implementation or empirical validation (informs AutoGreenTraC). One-way sensing->analysis->reporting; no actuation, no learning loop.

*Full-text source: browser-oa*

**AH — strength & gap filled:** Identifies data-acquisition latency and photogrammetric compute as the two bottlenecks and contributes a tiered edge-cloud hierarchy (millisecond safety alarms to asynchronous high-fidelity DT updates) with neural rendering as the latency bypass, grounded in NORMENG field metrics.

**AI — deficiencies & future work:** No implementation or empirical validation; latency targets, neural-rendering pipeline details and DT update scheduling remain future work in AutoGreenTraC.
