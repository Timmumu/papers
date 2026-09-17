# Jiang, W et al. (2024) — Early-warning of unsafe hoisting operations: An integration of digital twin and knowledge graph

- **ID:** R895 | **Source:** Scopus | **DOI:** 10.1016/j.dibe.2024.100490
- **Journal:** Developments in the Built Environment
- **Authors:** Jiang W.; Liu Y.; Chen K.; Liu Y.; Ding L.

## Abstract summary
Unsafe hoisting operations have been consistently associated with numerous safety incidents involving tower cranes. Currently, the predominant measures to mitigate these operations center around comprehensive training and education, emphasizing standardized protocols prior to hoisting activities. Despite concerted efforts in this direction, a conspicuous research gap persists in early-warning mechanisms during the construction phase. This paper aims to address this gap by proposing an innovative early-warning methodology, inspired by the principles of digital twin and knowledge graph. We firstly introduce a digital twin framework designed to mirror the real-time operational status of the tower crane. This framework enables the immediate detection of deviations or infractions as they occur. Subsequently, we develop a knowledge graph capable of promptly identifying unsafe hoisting operatio…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** DT + knowledge graph early warning of unsafe hoisting


## Step-3 Deep-Read Coding (Prompt B)
| P DT-subject | Q DfS/DfQ | R codable | U Tier | V Design | W Constr | X Oper | Z DfX | AA Self-improve | AB Methodology | AC Modality | AD Validation | AE QA(0-5) | AF Cluster |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow (one-way physical to virtual) | 0 | 1 | 0 | Design for Safety (DfS) | None | Ontology / semantic | Multi (two or more data types) | Simulation | 4 | Design for Safety |

| AC1 fusion depth | AC2 fusion evidence | AC3 confidence |
|---|---|---|
| Fused | Real-time multi-sensor states mirrored in the DT are jointly reasoned over by a standards-derived knowledge graph to identify unsafe hoisting operations and trigger early warnings. | Medium |

**Key evidence (AG):** Early-warning of unsafe hoisting operations via DT + knowledge graph (HUST): DT framework mirrors real-time operational status of tower crane (lifting, luffing, rotation); knowledge graph identifies unsafe hoisting operations by leveraging real-time data from the DT; scaled-down tower crane replica in lab; warning rate >70%, false alarm rate <20%. One-way monitoring→KG analysis→early warning; no actuation and no learning loop (KG is rule-based).

*Full-text source: 04c-port*

**AH — strength & gap filled:** Fills the construction-phase early-warning gap for unsafe hoisting operations: a DT mirrors a 1:80 scaled tower crane through STM32 boards, three 9-axis IMUs, two laser sensors, and MQTT, and a standards-derived knowledge graph built from seven standards and 86 accident reports identifies safety events, achieving over 70 percent warning accuracy with under 20 percent false alarms and Theil consistency below 0.1.

**AI — deficiencies & future work:** Validated only on a scaled-down crane in the laboratory, neglecting dynamic site environments and operator-specific habits; mapping suffers cumulative errors, and events like untested lifting and reverse operation show low accuracy or elevated false alarms requiring manual verification. Future work: analyzing consistency disparity sources, developing a more comprehensive mapping framework, and collecting real-world hoisting data.
