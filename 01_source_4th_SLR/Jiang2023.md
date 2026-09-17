# Jiang, L et al. (2023) — Intelligent control of building fire protection system using digital twins and semantic web technologies

- **ID:** R573 | **Source:** Scopus | **DOI:** 10.1016/j.autcon.2022.104728
- **Journal:** Automation in Construction
- **Authors:** Jiang L.; Shi J.; Wang C.; Pan Z.

## Abstract summary
A fire protection system takes on a critical significance to building operation. This paper describes the use of digital twins (DTs) and semantic web technologies for the intelligent control of building fire protection (BFP) systems in fire accidents. Specifically, a data fusion stage and several information-based control mechanisms are involved in the use of the two technologies. A designed BFP ontology is considered as the semantic model and basis of data fusion between the static building geometric information and the dynamic sensing data. The above information is incorporated into a DT data model, which is considered as the mapping of physical space. Moreover, rule models and process models are developed to achieve intelligent control mechanisms and keep the DT data model synced with the physical space. A case study based on a fire accident simulation was conducted to verify the feas…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** DT + semantic web intelligent control of building fire protection


## Step-3 Deep-Read Coding (Prompt B)
| P DT-subject | Q DfS/DfQ | R codable | U Tier | V Design | W Constr | X Oper | Z DfX | AA Self-improve | AB Methodology | AC Modality | AD Validation | AE QA(0-5) | AF Cluster |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 3 - Digital Twin (bidirectional, two-way) | 0 | 0 | 1 | Design for Safety (DfS) | None | Ontology / semantic | Multi (two or more data types) | Simulation | 4 | Design for Safety |

| AC1 fusion depth | AC2 fusion evidence | AC3 confidence |
|---|---|---|
| Fused | The BFP ontology fuses static BIM geometry with dynamic IoT sensing data into one DT data model, on which rule models trigger BPMN process models for fire-protection control. | Medium |

**Key evidence (AG):** Intelligent control of building fire protection (BFP) system using DT + semantic web technologies (SJTU): BFP ontology fuses static BIM geometric info + dynamic IoT sensing data into DT data model; rule model activates process model (workflow engine) for intelligent control mechanisms; DT data model synced with physical space; fire accident simulation case study demonstrates rapid response and evacuation facilitation; semantic web enables information acquisition/extraction/verification/update. Bidirectional — rule model triggers process model → physical actuation → Tier 3; no ML learning loop (rule-based control).

*Full-text source: 04c-port*

**AH — strength & gap filled:** Fills the gap between BIM and IoT fire monitoring and closed-loop fire protection control: a BFP ontology fuses static BIM geometry with dynamic IoT sensing data into a DT data model, and rule models plus BPMN process models execute intelligent control with update rules keeping virtual and physical spaces synchronized. Three scenarios, sprinkler, fire door, and smoke control, were verified through FDS simulation.

**AI — deficiencies & future work:** Only verified by fire accident simulation; on-site experiments are still needed. The approach assumes IoT terminal data are fully obtainable and well processed, and only three basic fire protection scenarios are investigated. Future work covers a unified hardware-software platform for validation, more fire protection scenarios refined by domain experts, and extension to other system control tasks such as active seismic response control.
