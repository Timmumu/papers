# Franciosi et al. (2024) — Digital twins in bridge engineering for streamlined maintenance and enhanced sustainability

- **ID:** 3493 | **Source:** Scopus | **DOI:** 10.1016/j.autcon.2024.105834
- **Journal:** Automation in Construction
- **Authors:** Franciosi, M.; Kasser, M.; Viviani, M.

## Abstract summary
Digital twins are evolving to oversee the entire construction life cycle, with a strong emphasis on sustainability across environmental, financial, regulatory, and administrative dimensions. This paper introduces a methodology for managing existing bridges through an adaptable digital twin. The aim of this research is to develop a framework for constructing digital twins that, by enabling structural analysis and “what-if” scenario simulations, supports more reliable maintenance decision-making. Such type of digital twin ensure safety, extend lifespan, and provide a precise database for managing end-of-life processes within a circular “cradle to cradle” framework. This methodology also addresses obsolescence issues related to software evolution and the longer lifespan of a bridge compared to its creator. A case study demonstrates the methodology's effectiveness, showing that digital twins…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** Adaptable bridge DT; what-if simulations; safety & lifespan

## Step-3 Deep-Read Coding (Prompt B)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow (one-way physical to virtual) | 0 | 0 | 1 | Design for Safety (DfS) | None | Finite Element Method / physics-based | Multi (two or more data types) | Single case study | 4 | Lifecycle / governance |

**Key evidence (AG):** Adaptable digital twin methodology for existing bridge management (HEIG-VD): integrates BIM + IFC (open interoperable formats) + ontology + FE models; laser-scanned 3D model converted to DT via IFC; enables structural analysis and what-if scenario simulations for maintenance decision-making; differential evolution algorithm for optimized FE model; case study demonstrates feasibility; cradle-to-cradle approach for end-of-life. One-way monitoring/analysis→maintenance decisions; no actuation and no learning loop (updates are manual inspection-based).


**Strength & gap filled (AH):** Establishes an adaptable methodology for existing-bridge digital twins addressing software obsolescence and interoperability: laser-scanned geometry (RIEGL VZ-2000i) converted to IFC 4.3 BIM and enriched from the KUBA database, then imported into SCIA Engineer for what-if corrosion scenarios on the 377.60 m Praz bridge and DE-algorithm FE updating against DIC measurements on the Grandson bridge.

**Deficiencies & future work (AI):** Scan-to-BIM remains semi-automated and the DT provides no automatic defect detection; updates come in batch from inspections rather than a real-time link. Future work covers a method to integrate inspection and monitoring results into DTs, extension to new bridges during design, and linking DTs into networks for whole transport corridors.
**Fusion depth (AC1):** Aligned

**Fusion evidence (AC2):**
- **Data streams:** laser-scanned point clouds (RIEGL VZ-2000i) + DIC measurements (Grandson bridge) + KUBA database enrichment.
- **Integration mechanism:** scan-to-BIM conversion provides the shared IFC model frame; DE-algorithm FE updating consumes DIC measurements in a separate calibration stage, and what-if corrosion scenarios run in SCIA Engineer.
- **Why this code:** data types are linked via the common IFC/BIM frame while inference runs per stage and per type, so Aligned.

**Confidence (AC3):** High - scan-to-IFC and DE-updating mechanisms are explicit.
(full-text source: Endnote)
