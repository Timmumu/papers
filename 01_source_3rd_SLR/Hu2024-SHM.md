# Hu et al. (2024) — An intelligent BIM-enabled digital twin framework for real-time structural health monitoring using wireless IoT sensing, digital signal processing, and structural analysis

- **ID:** 3575 | **Source:** Scopus | **DOI:** 10.1016/j.eswa.2024.124204
- **Journal:** Expert Systems with Applications
- **Authors:** Hu, X.; Olgun, G.; Assaad, R. H.

## Abstract summary
Structural health monitoring (SHM) of civil infrastructure is critically important due to its direct influence on public safety and economic activities. Exiting Building Information Modeling (BIM)-based SHM systems often use offline data processing techniques to analyze and visualize structural health data. Despite some of them adopting Internet of Things (IoT) to enable real-time sensor data collection, sensor data quality still remains uncertain due to a lack of sensor signal preprocessing in those existing systems. Additionally, the IoT-based SHM systems often disregard structural analysis domain knowledge, which is important for accurate and precise SHM. Therefore, there is still a need to improve existing systems and practices by enabling more efficient and reliable data collection and processing as well as providing more representative SHM data visualization in BIM. As such, this p…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** BIM-enabled DT for real-time SHM; IoT+DSP+structural analysis

## Step-3 Deep-Read Coding (Prompt B)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow (one-way physical to virtual) | 0 | 0 | 1 | Design for Safety (DfS) | None | Digital Twin platform (no machine learning) | Multi (two or more data types) | Single case study | 4 | Design for Safety |

**Key evidence (AG):** BIM-enabled digital twin framework for real-time structural health monitoring (NJIT): wireless IoT sensing (strain gauges, laser displacement) + digital signal processing (WT with sym4 kernel optimal) + structural analysis domain knowledge; sensor data interpolation in Revit for visualization of structural behaviors at different locations; DT updating frequency of 5 Hz; validated on prototyped structural frame under bending forces. One-way monitoring→visualization→decision support; no actuation and no learning loop (interpolation is static mapping).


**Strength & gap filled (AH):** Addresses offline processing, uncertain sensor data quality and missing structural-analysis knowledge in BIM-based SHM with a digital twin framework tested on a prototyped aluminum frame at NJIT: Robot Structural Analysis guides sensor placement, Raspberry Pi sensing with strain gauge and laser distance sensor, wavelet sym4 denoising (threshold 25, level 6), and Revit Dynamo color-coded deformation visualization refreshing at 5 Hz from one sensor via bending-moment interpolation.

**Deficiencies & future work (AI):** The strain interpolation requires predefined mathematical representations and fails for live loads with moving locations; only tensile strain is monitored, not shear or torsion, and validation used a small-scale frame in a controlled environment, so the authors will run full-scale laboratory and field tests with additional sensors.
**Fusion depth (AC1):** Aligned

**Fusion evidence (AC2):**
- **Data streams:** strain gauges + laser distance sensors on a prototyped aluminium frame; wavelet sym4 denoising (threshold 25, level 6).
- **Integration mechanism:** bending-moment interpolation maps one sensor onto other Revit locations, refreshing colour-coded deformation at 5 Hz; no joint multi-sensor inference exists.
- **Why this code:** two sensor types share the BIM model frame but inference stays per location, so Aligned.

**Confidence (AC3):** High - the interpolation mapping is explicit.
(full-text source: Endnote)
