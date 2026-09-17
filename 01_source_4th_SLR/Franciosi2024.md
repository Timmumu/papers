# Franciosi, M et al. (2024) — Digital twins in bridge engineering for streamlined maintenance and enhanced sustainability

- **ID:** R501 | **Source:** Scopus | **DOI:** 10.1016/j.autcon.2024.105834
- **Journal:** Automation in Construction
- **Authors:** Franciosi M.; Kasser M.; Viviani M.

## Abstract summary
Digital twins are evolving to oversee the entire construction life cycle, with a strong emphasis on sustainability across environmental, financial, regulatory, and administrative dimensions. This paper introduces a methodology for managing existing bridges through an adaptable digital twin. The aim of this research is to develop a framework for constructing digital twins that, by enabling structural analysis and “what-if” scenario simulations, supports more reliable maintenance decision-making. Such type of digital twin ensure safety, extend lifespan, and provide a precise database for managing end-of-life processes within a circular “cradle to cradle” framework. This methodology also addresses obsolescence issues related to software evolution and the longer lifespan of a bridge compared to its creator. A case study demonstrates the methodology's effectiveness, showing that digital twins…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** DTs in bridge engineering for maintenance and safety


## Step-3 Deep-Read Coding (Prompt B)
| P DT-subject | Q DfS/DfQ | R codable | U Tier | V Design | W Constr | X Oper | Z DfX | AA Self-improve | AB Methodology | AC Modality | AD Validation | AE QA(0-5) | AF Cluster |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow (one-way physical to virtual) | 0 | 0 | 1 | Design for Safety (DfS) | None | Finite Element Method / physics-based | Multi (two or more data types) | Single case study | 4 | Lifecycle / governance |

| AC1 fusion depth | AC2 fusion evidence | AC3 confidence |
|---|---|---|
| Aligned | RIEGL VZ-2000i laser-scanned geometry is converted to IFC 4.3 BIM, and the SCIA Engineer FE model is updated against DIC measurements, linking scan geometry and measurement data through the shared bridge model. | High |

**Key evidence (AG):** Adaptable digital twin methodology for existing bridge management (HEIG-VD): integrates BIM + IFC (open interoperable formats) + ontology + FE models; laser-scanned 3D model converted to DT via IFC; enables structural analysis and what-if scenario simulations for maintenance decision-making; differential evolution algorithm for optimized FE model; case study demonstrates feasibility; cradle-to-cradle approach for end-of-life. One-way monitoring/analysis→maintenance decisions; no actuation and no learning loop (updates are manual inspection-based).

*Full-text source: 04c-port*

**AH — strength & gap filled:** Establishes an adaptable methodology for existing-bridge digital twins addressing software obsolescence and interoperability: laser-scanned geometry (RIEGL VZ-2000i) converted to IFC 4.3 BIM and enriched from the KUBA database, then imported into SCIA Engineer for what-if corrosion scenarios on the 377.60 m Praz bridge and DE-algorithm FE updating against DIC measurements on the Grandson bridge.

**AI — deficiencies & future work:** Scan-to-BIM remains semi-automated and the DT provides no automatic defect detection; updates come in batch from inspections rather than a real-time link. Future work covers a method to integrate inspection and monitoring results into DTs, extension to new bridges during design, and linking DTs into networks for whole transport corridors.
