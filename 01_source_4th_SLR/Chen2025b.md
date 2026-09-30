# Chen, C et al. (2025) — Digital Twin-Based and Knowledge Graph-Enhanced Emergency Response in Urban Infrastructure Construction

- **ID:** R353 | **Source:** Scopus | **DOI:** 10.3390/app15116009
- **Journal:** Applied Sciences (Switzerland)
- **Authors:** Chen C.; Lu Y.; Wu B.; Lu L.

## Abstract summary
Urban infrastructure construction poses significant risks to surrounding the infrastructure due to ground settlement, structural disturbances, and underground utility disruptions. Traditional risk assessment methods often rely on static models and experience-based decision-making, limiting their ability to adapt to dynamic construction conditions. This study proposes an integrated framework combining digital twin and knowledge graph technologies to enhance real-time risk assessment and emergency response in tunnel construction. The digital twin continuously integrates real-time monitoring data, including settlement measurements, TBM operational parameters, and structural responses, creating a virtual representation of the tunneling environment. Meanwhile, the knowledge graph structures domain knowledge and applies rule-based reasoning to infer potential hazards, detect abnormal condition…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** DT + KG emergency response for tunnel construction

## Step-3 Deep-Read Coding (Prompt B)
| P DT-subject | Q DfS/DfQ | R codable | U Tier | V Design | W Constr | X Oper | Z DfX | AA Self-improve | AB Methodology | AC Modality | AD Validation | AE QA(0-5) | AF Cluster |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 3 - Digital Twin (bidirectional, two-way) | 0 | 1 | 0 | Design for Safety (DfS) | None | Ontology / semantic | Multi (two or more data types) | Single case study | 4 | Predictive analytics / decision support |

| AC1 fusion depth | AC2 fusion evidence | AC3 confidence |
|---|---|---|
| Fused | Settlement, TBM-operational and structural monitoring data are continuously integrated in the DT and jointly reasoned over by a knowledge graph with SWRL rules to infer hazards and mitigation. | High |

**Key evidence (AG):** Tunnel project in China; DT continuously integrates settlement/TBM/structural monitoring; KG rule-based reasoning infers hazards and mitigation; bidirectional DT-KG interaction visualised for decisions; prevention of further structural impact claimed in real emergency.

*Full-text source: 04c-port*

**AH — strength & gap filled:** Addresses the reactive and static gap in tunnel construction emergency response: a digital twin continuously integrating settlement, TBM operational and structural monitoring data is coupled with a knowledge graph using SWRL rule-based reasoning to infer hazards, detect anomalies and suggest mitigations, with inference results visualized back in the twin; deployed on an urban tunnel project in Shanghai where it enabled early anomaly identification.

**AI — deficiencies & future work:** Data quality dependency is acknowledged: sensor noise, loss, calibration drift and delays can misclassify risk levels; the ontology and rules are manually built for Shanghai urban tunnels, limiting scalability; reasoning speed, throughput and prediction accuracy are not quantitatively benchmarked; single-project validation; future work includes confidence metrics, automated rule generation, dynamic learning and stress testing.
