# Sun et al. (2023) — Intelligent Risk Prognosis and Control of Foundation Pit Excavation Based on Digital Twin

- **ID:** 3994 | **Source:** Web of Science | **DOI:** 10.3390/buildings13010247
- **Journal:** BUILDINGS
- **Authors:** Sun, Z.; Li, H. Y.; Bao, Y.; Meng, X. L.; Zhang, D. L.

## Abstract summary
Timely risk information acquisition and diagnosis during foundation pit excavation (FPE) processes are vital for ensuring the safe and effective construction of underground urban infrastructures. Unfortunately, diverse geological and hydrogeological conditions and complex shapes of the foundation pit create barriers for reliable FPE risk prognosis and control. Furthermore, typical support systems during FPE use temporary measures, which have limited capacity to confront excessive loads, large deformations, and seepage. This study aims to establish an intelligent risk prognosis and control framework based on digital twin (DT) for ensuring safe and effective FPE processes. Previous studies have conducted extensive experimental and numerical analyses for examining unsafe conditions during FPE. How to enable intelligent risk prognosis and control of tedious FPE processes by integrating physi…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** DT intelligent risk prognosis & control of foundation pit excavation

## Step-3 Deep-Read Coding (Prompt B)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 3 - Digital Twin (bidirectional, two-way) | 0 | 1 | 0 | Design for Safety (DfS) | None | Finite Element Method / physics-based | Multi (two or more data types) | Single case study | 4 | Design for Safety |

**Key evidence (AG):** Intelligent risk prognosis and control of foundation pit excavation (FPE) based on DT (Beijing U Tech): physical space (RFID + sensors capture components, environment, personnel) + virtual space (high-fidelity physics-based model); data fusion from physical and virtual space; FE model (FLAC3D) updated with real-time parameters; geometric model updated via point data; risk prognosis and control measures established based on safety state; validated on Wuhan Metro Line. Bidirectional — virtual model updated from physical, control measures from virtual → Tier 3; no learning loop (model updating is manual).


**Strength & gap filled (AH):** Fills the spatiotemporal risk-prognosis gap in foundation pit excavation: a five-component digital twin (physical space, FLAC3D virtual model, twin data, service, connections) fuses RFID, displacement, soil-pressure and environmental sensing to update an 850141-cell finite element model after each step, with Markov-chain risk prediction and a bow-tie model selecting control measures, validated on the Wuhan Metro Line 7 air-shaft pit with 15.2 mm maximum settlement.

**Deficiencies & future work (AI):** The method depends on dense, costly sensor arrays; several displacements are still measured manually with inclinometers, soil is idealized as homogeneous and isotropic, and consolidation over time and groundwater seepage are ignored; future work targets real-time sensing with AI-driven risk prediction, better sensor placement, and seepage and time-dependent effects.
**Fusion depth (AC1):** Fused

**Fusion evidence (AC2):**
- **Data streams:** RFID, displacement, soil-pressure and environmental sensors (Wuhan Metro Line 7 air shaft, 15.2 mm max settlement).
- **Integration mechanism:** the multi-source sensing updates the FE model after each step, and Markov-chain prediction plus the bow-tie model compute risk states and control measures on the updated model.
- **Why this code:** risk prognosis depends on several sensing types and the updated model simultaneously, so Fused.

**Confidence (AC3):** High - the sensor-to-model updating chain is explicit.
(full-text source: Endnote)
