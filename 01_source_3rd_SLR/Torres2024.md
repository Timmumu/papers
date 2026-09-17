# Torres et al. (2024) — Building Digital Twins to Overcome Digitalization Barriers for Automating Construction Site Management

- **ID:** 3935 | **Source:** Web of Science | **DOI:** 10.3390/buildings14072238
- **Journal:** BUILDINGS
- **Authors:** Torres, J.; San-Mateos, R.; Lasarte, N.; Mediavilla, A.; Sagarna, M.; León, I.

## Abstract summary
Construction sites are highly unpredictable environments involving a wide variety of stakeholders with complex information exchanges, which lead to the well-known inefficiencies and unproductivity of the construction sector. The adoption of Building Digital Twins (BDT) in the construction site is a promising solution to this issue, by automating data acquisition and knowledge extraction processes and providing what-if scenario simulation capabilities. Furthermore, the current research sets the principles to define, replicate, and scale-up the architecture of a Building Digital Twin Platform (BDTP), conceived as a scalar ecosystem, which allows to seamlessly manage on-site construction processes, integrating cross-cutting domains for the construction site optimization (Progress monitoring, Quality control, Operational Health and Safety, Equipment control, and Production planning). The sta…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** Building DT platform for site mgmt incl. OHS & quality control domains

## Step-3 Deep-Read Coding (Prompt B) — full text verified via Endnote library (front-matter DOI/title match, coverage re-scan 2026-08-12)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 1 - Digital Model | 0 | 1 | 0 | Both | Mentioned only | Digital Twin platform (no machine learning) | Multi (two or more data types) | Conceptual (no test) | 3 | BIM-to-Digital-Twin architecture |

**Key evidence (AG):** Building Digital Twin Platform (BDTP) architecture to overcome digitalization barriers for automating construction site management (TECNALIA, DSR + PDCA + Living Labs): diagnoses on-site inefficiencies and barriers via questionnaires/interviews; proposes standardized BPMN workflows with the DT as a service-oriented actor, modelling five cross-cutting domains (progress monitoring, quality control, OHS, equipment control, production planning) with digital/human agents connected via APIs; property-graph data model and use cases. Conceptual framework only — implementation, KPIs and AI/ML are "in the long-term"/future ("could be seamlessly implemented"); no deployed data link, no learning loop.

**Strength & gap filled (AH):** Fills the gap between conceptual digital twins and on-site construction management: a Design Science Research study, grounded in the H2020 BIM2TWIN project, uses Living Lab questionnaires and interviews to rank on-site inefficiencies and digitalization barriers, then derives PDCA-classified user requirements and standardized BPMN workflows covering progress monitoring, quality control, health and safety, equipment control, and production planning.

**Deficiencies & future work (AI):** Remains a conceptual architecture with no implemented platform, live sensor link, or field validation; real-time data acquisition, AI-driven knowledge extraction, and closed-loop correction are described only as future scenarios. Authors propose multi-site BDT portfolios with a broker, a Digital Twin Federator across city-scale DTs, and KPIs feeding automated learning as future work.

**Fusion depth (AC1):** Unclear

**Fusion evidence (AC2):**
- **Data streams:** questionnaire/interview-derived requirements (Living Labs) mapped onto five cross-cutting domains.
- **Integration mechanism:** none deployed - property-graph data model and API connections are proposed.
- **Why this code:** Unclear (rule 2).

**Confidence (AC3):** High.