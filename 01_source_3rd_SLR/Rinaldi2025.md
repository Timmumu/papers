# Rinaldi et al. (2025) — Physics-informed computational framework for assessing the seismic behavior of the Prince Moulay Abdellah Dam

- **ID:** 3983 | **Source:** Web of Science | **DOI:** 10.1016/j.rineng.2025.106914
- **Journal:** RESULTS IN ENGINEERING
- **Authors:** Rinaldi, C.; Bendarma, A.; Potenza, F.; Gattulli, V.

## Abstract summary
Dams in seismically active regions require rigorous structural assessment to ensure safety and protect downstream communities. To address this challenge, the present study integrates Building Information Modeling (BIM), Finite Element Method (FEM) modeling, and real-time structural health monitoring into a novel framework for seismic evaluation of the Prince Moulay Abdellah Dam in the Agadir region of Morocco. A detailed BIM-based digital replica of the dam was developed to ensure seamless interoperability with FEM simulations and incorporation of on-site sensor data. This integrated approach captured different displacement patterns during the magnitude 6.8 earthquake on September 8, 2023. The dam abutments experienced noticeable increases in longitudinal displacement, while the central vault remained largely stable. The FEM analysis corroborated the field measurements, indicating that c…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** BIM+FEM+real-time SHM digital replica of dam; seismic safety

## Step-3 Deep-Read Coding (Prompt B)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow (one-way physical to virtual) | 0 | 0 | 1 | Design for Safety (DfS) | None | Finite Element Method / physics-based | Multi (two or more data types) | Single case study | 4 | Design for Safety |

**Key evidence (AG):** BIM-FEM-real-time monitoring framework for seismic assessment of Prince Moulay Abdellah Dam (Sapienza U): BIM digital replica interoperable with FEM simulations; real-time SHM sensor data captured during magnitude 6.8 earthquake (Sept 8, 2023); FEM analysis corroborated field measurements (abutments showed increased longitudinal displacement, central vault stable); BIM enables efficient monitoring data management. One-way monitoring→FEM validation→safety assessment; no actuation and no learning loop.


**Strength & gap filled (AH):** Integrates BIM, FEM and real-time monitoring to assess seismic behavior of the Prince Moulay Abdellah Dam in Morocco: a Revit model with sensor metadata feeds a MIDAS FEA NX 3D soil-structure model (278,778 tetrahedral elements) via Parasolid export, and response-spectrum analyses show maximum tensile stresses around 12% and compressive stresses around 85% of allowable limits at 0.5 g; vinchon records from the September 2023 magnitude 6.8 earthquake confirm abutments displace more than the stable central vault.

**Deficiencies & future work (AI):** Analyses remain linear-elastic with soil parameters taken from literature and an assumed 30 MPa concrete strength due to missing data, so nonlinear joint behavior is uncharacterized; monitoring data cannot be shared, and no automated live BIM-FEM coupling exists yet. Future research targets automatic interoperability, nonlinear fracture modelling at joints, and early warning systems for other dams.
**Fusion depth (AC1):** Aligned

**Fusion evidence (AC2):**
- **Data streams:** Revit BIM sensor metadata + MIDAS FEA NX model (278,778 elements) + real-time SHM records (vinchon, M6.8 earthquake).
- **Integration mechanism:** Parasolid export links BIM and FEM into one replica frame; measured abutment displacement corroborates the FEM finding of a stable central vault, without joint processing.
- **Why this code:** streams share the BIM-FEM frame while analysis stays per stage, so Aligned.

**Confidence (AC3):** High - the BIM-FEM export chain is explicit.
(full-text source: Endnote)
