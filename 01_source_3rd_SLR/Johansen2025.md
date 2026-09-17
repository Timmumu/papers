# Johansen et al. (2025) — Knowledge graph exploitation to enhance the usability of risk assessment in construction safety planning

- **ID:** 4027 | **Source:** Web of Science | **DOI:** 10.1016/j.aei.2025.103305
- **Journal:** ADVANCED ENGINEERING INFORMATICS
- **Authors:** Johansen, K. W.; Schultz, C.; Teizer, J.

## Abstract summary
Construction projects and their dynamic and yet hazardous work environments face significant challenges. Despite advancements, many proposed solutions for information extraction and utilization remain impractical due to complexity and lack of interoperability. Information is often siloed in proprietary formats, making it difficult to integrate. This issue is evident in the construction safety domain, where advanced risk analysis tools provide detailed insights to hazards but can be overwhelming. Similar challenges exist in cost estimation, schedule evaluation, progress monitoring, and quality compliance checking. Decision-making in construction scheduling struggles to assess how changes impact site safety due to insufficient information and knowledge extraction capabilities, especially when it comes to cross-domain knowledge extraction. This study aims to make safety information accessib…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** KG exploitation on DTs for construction safety planning usability

## Step-3 Deep-Read Coding (Prompt B)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 1 - Digital Model (static, no live data) | 1 | 0 | 0 | Design for Safety (DfS) | None | Ontology / semantic | Multi (two or more data types) | Conceptual (no test) | 3 | Semantic interoperability |

**Key evidence (AG):** Knowledge graph exploitation for construction safety planning (DTU): 4D BIM + automated safety analysis results → ontology + knowledge graph for cross-domain knowledge extraction; query building blocks transform natural language questions into actionable queries; case study shows cross-domain impact of decisions (e.g., crew assignment → safety). Static knowledge representation — no live data link, no actuation, no learning loop (ontology/querying is static).


**Strength & gap filled (AH):** Addresses the cognitive overload and information silos that block adoption of automated safety analysis: a safety ontology and Prolog knowledge graph capture BIM, schedule, and hazard analysis results (about 3,800 nodes and 20,000 edges), and categorized query building blocks turn seven planning questions into queries answered in under one second, revealing cross-domain impacts of crew assignment and delivery changes on safety.

**Deficiencies & future work (AI):** No live site data link: IoT sensor collection, user interfaces, and on-site usability are explicitly out of scope, and the framework is tested only on one high-rise case study. Query translation remains too technical for practitioners, and scalability bottlenecks are expected on larger graphs. Future work adds schedule dependencies, compliance results, real-time location tracking, LLM-based query generation, and game-engine dissemination.
**Fusion depth (AC1):** Fused

**Fusion evidence (AC2):**
- **Data streams:** 4D BIM data, construction schedule data and automated safety-analysis results.
- **Integration mechanism:** the safety ontology + Prolog KG is the joint representation; query building blocks transform natural-language questions into queries that reveal cross-domain impacts (crew assignment to safety), answered in under one second.
- **Why this code:** query outputs depend on three integrated data types simultaneously, so Fused; no live IoT data (out of scope), hence Medium.

**Confidence (AC3):** Medium - the KG integration is explicit, but live data linkage is explicitly out of scope.
(full-text source: Endnote)
