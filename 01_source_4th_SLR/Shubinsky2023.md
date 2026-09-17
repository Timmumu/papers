# Shubinsky, I.B et al. (2023) — INNOVATIVE METHODS OF ENSURING THE FUNCTIONAL SAFETY OF TRAIN CONTROL SYSTEMS

- **ID:** R700 | **Source:** Scopus | **DOI:** 10.24412/1932-2321-2023-476-909-920
- **Journal:** Reliability: Theory and Applications
- **Authors:** Shubinsky I.B.; Rozenberg E.N.; Schäbe H.

## Abstract summary
The paper examines the specificity of the modern intelligent control systems. The Big Data technology and Data Science algorithms open up great potential in train traffic management based on hazard prevention. An example is given of high reliability and acceptable accuracy of hazardous railway infrastructure failure prediction using methods based on artificial intelligence. A great deal of attention is given to economical methods of ensuring the required levels of functional safety of train control systems. For that purpose, the efficiency of the digital twin-based method was evaluated. It is shown that, under certain conditions, this method allows significantly reducing the cost of a control system while achieving an acceptably high level of functional safety. The method of virtual second channels is based on the same principle of using information redundancy rather than hardware redund…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** DT-based functional safety method for train control systems


## Step-3 Deep-Read Coding (Prompt B)
| P DT-subject | Q DfS/DfQ | R codable | U Tier | V Design | W Constr | X Oper | Z DfX | AA Self-improve | AB Methodology | AC Modality | AD Validation | AE QA(0-5) | AF Cluster |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 3 - Digital Twin (bidirectional, two-way) | 0 | 0 | 1 | Design for Safety (DfS) | None | Digital Twin platform (no machine learning) | Single (one data type) | Conceptual (no test) | 3 | Design for Safety |

| AC1 fusion depth | AC2 fusion evidence | AC3 confidence |
|---|---|---|
| SINGLE | Only control-system states/model outputs are used; no multi-modal data fusion. | Medium |

**Key evidence (AG):** Functional-safety methods for train control systems (NIIAS/TUEV Rheinland, RT&A 2023): a digital twin is defined as a mathematical model + software implementation performing all operating functions of the initial object + verification results; two same-type DTs form a dual external safety circuit so a SIL1/SIL2 control system reaches at least SIL3 (virtual second channels use information redundancy instead of hardware redundancy); evaluated analytically for an axle-counter-based train control system. The twin acts back on the control system as a safety channel -> Tier 3 (analytical safety-case evaluation, no deployed test); no learning loop.

*Full-text source: Endnote*

**AH — strength & gap filled:** Fills the cost/safety trade-off gap for train control: dual digital-twin external circuits (virtual second channels, information redundancy) analytically achieve at least SIL3 for a SIL1/SIL2 axle-counter system, reducing hardware while preserving functional safety.

**AI — deficiencies & future work:** Analytical safety-case evaluation without deployed test or field data; the DT is a software replica of the controller rather than of the physical asset, and acceptability/verification effort for the additional software is delegated to the developer.
