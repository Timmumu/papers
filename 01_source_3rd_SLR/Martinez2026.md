# Martinez et al. (2026) — Integration of building information modelling and digital twin in mechanized tunnelling construction

- **ID:** 3877 | **Source:** Web of Science | **DOI:** 10.1108/ECAM-01-2025-0031
- **Journal:** ENGINEERING CONSTRUCTION AND ARCHITECTURAL MANAGEMENT
- **Authors:** Martinez, E.; Stauch, F.; de Soto, B. G.; Sacks, R.

## Abstract summary
PurposeThis study explores the integration of monitored data from Tunnel Boring Machine (TBM) operations into a digital twin framework to generate real-time status information for mechanized tunnelling. The study investigates the potential benefits that can be derived in terms of lean operations and reduced waste of rework.Design/methodology/approachUsing a design science research approach within a case study of a tunnelling project, the researchers developed, tested and refined the Digital Twin Construction (DTC) system and observed use cases of its application. The empirical data collected was analyzed to draw conclusions concerning the feasibility of the integration of TBM excavation data into a digital twin and the impacts of its use in improving flow and avoiding rework by reducing uncertainty.FindingsThe study identifies key technical challenges, such as imperfect data interoperabi…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** BIM+DT integration in mechanized tunnelling; rework reduction, lean

## Step-3 Deep-Read Coding (Prompt B)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow (one-way physical to virtual) | 0 | 1 | 0 | Design for Quality (DfQ) | None | Digital Twin platform (no machine learning) | Multi (two or more data types) | Single case study | 4 | Lifecycle / governance |

**Key evidence (AG):** Integration of BIM and digital twin in mechanized tunnelling construction (Implenia/NYU/Technion): design-science case study of a TBM tunnelling project; computational design algorithm automates TBM excavation-data integration into a Digital Twin Construction (DTC) system; DT generates real-time status of the tunnel physical state in short cycles; 90% reduction in DT modelling time; supports lean design/construction (bracketry design, reducing rework/uncertainty); challenges: data interoperability, standardized modelling. One-way data->DT->decision support for lean workflows; no actuation, no learning loop.


**Strength & gap filled (AH):** Integrates TBM excavation data into a BIM as-built model through a Dynamo computational design algorithm on a 2.4 km French tunnelling project, automatically placing segments from corrected TPC and VMT positioning, embedding segment manufacturing traceability and no-drill zones, and cutting ring modelling time from 15 to 20 minutes to 1 minute, a cycle time reduction above 90 percent supporting bracketry design and clash detection.

**Deficiencies & future work (AI):** A single case study limits generalizability; parametric objects are tailored to project-specific proprietary systems, manual steps remain due to imperfect data interoperability and missing tunnel IFC standards, and no benchmark control project allows quantifying operational savings. Future research will evaluate adaptability across projects, scalability, and standardized IFC integration.
**Fusion depth (AC1):** Aligned

**Fusion evidence (AC2):**
- **Data streams:** TPC/VMT TBM positioning, segment manufacturing traceability and no-drill-zone data (2.4 km French tunnelling project).
- **Integration mechanism:** the computational design algorithm places segments automatically into the BIM as-built model (ring modelling 15-20 min down to 1 min), linking each data stream to model elements; lean analyses run on the model.
- **Why this code:** streams share the BIM element frame with per-stream processing, so Aligned.

**Confidence (AC3):** Medium - the automatic placement is explicit; joint inference beyond model assembly is not described.
(full-text source: Endnote)
