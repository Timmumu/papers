# Johansen, K.W et al. (2025) — Knowledge graph exploitation to enhance the usability of risk assessment in construction safety planning

- **ID:** R215 | **Source:** Scopus | **DOI:** 10.1016/j.aei.2025.103305
- **Journal:** Advanced Engineering Informatics
- **Authors:** Johansen K.W.; Schultz C.; Teizer J.

## Abstract summary
Construction projects and their dynamic and yet hazardous work environments face significant challenges. Despite advancements, many proposed solutions for information extraction and utilization remain impractical due to complexity and lack of interoperability. Information is often siloed in proprietary formats, making it difficult to integrate. This issue is evident in the construction safety domain, where advanced risk analysis tools provide detailed insights to hazards but can be overwhelming. Similar challenges exist in cost estimation, schedule evaluation, progress monitoring, and quality compliance checking. Decision-making in construction scheduling struggles to assess how changes impact site safety due to insufficient information and knowledge extraction capabilities, especially when it comes to cross-domain knowledge extraction. This study aims to make safety information accessib…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** KG + DT for construction safety planning risk

## Step-3 Deep-Read Coding (Prompt B)
| P DT-subject | Q DfS/DfQ | R codable | U Tier | V Design | W Constr | X Oper | Z DfX | AA Self-improve | AB Methodology | AC Modality | AD Validation | AE QA(0-5) | AF Cluster |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 1 - Digital Model (static, no live data) | 1 | 0 | 0 | Design for Safety (DfS) | None | Ontology / semantic | Multi (two or more data types) | Conceptual (no test) | 3 | Semantic interoperability |

| AC1 fusion depth | AC2 fusion evidence | AC3 confidence |
|---|---|---|
| Fused | BIM, schedule and automated safety-analysis results are integrated into one Prolog knowledge graph (about 3,800 nodes, 20,000 edges) whose cross-domain queries answer planning questions over all three data types simultaneously. | Medium |

**Key evidence (AG):** Knowledge graph exploitation for construction safety planning (DTU): 4D BIM + automated safety analysis results → ontology + knowledge graph for cross-domain knowledge extraction; query building blocks transform natural language questions into actionable queries; case study shows cross-domain impact of decisions (e.g., crew assignment → safety). Static knowledge representation — no live data link, no actuation, no learning loop (ontology/querying is static).

*Full-text source: 04c-port*

**AH — strength & gap filled:** Addresses the cognitive overload and information silos that block adoption of automated safety analysis: a safety ontology and Prolog knowledge graph capture BIM, schedule, and hazard analysis results (about 3,800 nodes and 20,000 edges), and categorized query building blocks turn seven planning questions into queries answered in under one second, revealing cross-domain impacts of crew assignment and delivery changes on safety.

**AI — deficiencies & future work:** No live site data link: IoT sensor collection, user interfaces, and on-site usability are explicitly out of scope, and the framework is tested only on one high-rise case study. Query translation remains too technical for practitioners, and scalability bottlenecks are expected on larger graphs. Future work adds schedule dependencies, compliance results, real-time location tracking, LLM-based query generation, and game-engine dissemination.
