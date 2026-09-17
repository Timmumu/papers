# Aroquipa et al. (2025) — Methodological framework for integrating structural health monitoring and digital-twin models for seismic assessment of heritage buildings: Case study of Basilica Maria Auxiliadora, Lima, Peru

- **ID:** 3975 | **Source:** Web of Science | **DOI:** 10.1016/j.istruc.2025.110115
- **Journal:** STRUCTURES
- **Authors:** Aroquipa, H.; Hurtado, A.; Angel, C.

## Abstract summary
This study proposes a methodological framework for integrating structural health monitoring (SHM) systems with numerical digital twin (DT) models for the seismic assessment of heritage structures. This approach is being implemented within smart cities, focusing on intelligent circular resilience. The process begins in the physical world by recording data through strategically placed sensors distributed throughout the evaluated structures. Afterwards, the virtual world refers to the development of numerical models that capture the structural performance of the building while considering specific features to simulate the original one. The interconnection of both sides requires exhaustive and detailed cross-validation to ensure an established level of reliability, often based on the expected accuracy and limitations. Nevertheless, extending this process to heritage buildings demands a more …

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** SHM-DT framework, damage levels, early warning; heritage basilica

## Step-3 Deep-Read Coding (Prompt B)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 1 - Digital Model (static, no live data) | 0 | 0 | 1 | Design for Safety (DfS) | None | Finite Element Method / physics-based | Multi (two or more data types) | Conceptual (no test) | 4 | BIM-to-Digital-Twin architecture |

**Key evidence (AG):** Methodological framework for integrating SHM with numerical DT models for seismic assessment of heritage buildings (Basilica Maria Auxiliadora, Lima): numerical models in 3DEC and SAP2000 (modal + time-history of 34 seismic ground-motion records) identify susceptible zones and recommended sensor locations; sensor deployment and validation against experimental models are explicitly future work - no DT implemented, no live data link, no learning loop. 

**Strength & gap filled (AH):** Provides a methodology for integrating SHM with numerical DT models for seismic assessment of heritage buildings: a LiDAR-derived BIM of the Basilica Maria Auxiliadora in Lima fed calibrated SAP2000 and 3DEC models (about 4500 block elements, 161000 contact zones), modal analysis with 220 modes, time-history analysis reproducing the 2007 Pisco earthquake crack patterns, and 25 sensor control points selected via intensity-duration-frequency plots.

**Deficiencies & future work (AI):** No sensors are yet deployed: the study covers only Building Virtualization and part of sensor data analysis, so the EWS and DT feedback loop remain pending; validation relies on historical damage reports and analytical consistency, with future research to include experimental models, tri-axial sensor installation, and ambient-vibration calibration of the numerical model.


**Fusion depth (AC1):** Aligned

**Fusion evidence (AC2):**
- **Data streams:** 3D LiDAR point-cloud survey of the Basilica Maria Auxiliadora + BIM geometry + 3DEC/SAP2000 FEM models.
- **Integration mechanism:** the point-cloud survey is converted into a BIM that is linked to the FEM models through an explicit BIM-FEM linking process, sharing one building geometry frame, while each model analyses separately (modal with 220 modes, time-history of 34 records); sensor deployment is future work.
- **Why this code:** geometry sources share the BIM frame but analysis stays per model, so Aligned.

**Confidence (AC3):** Medium - the BIM-FEM linking process is explicit, but no live sensor data exists yet.
Source: Endnote library (front-matter DOI verified).
