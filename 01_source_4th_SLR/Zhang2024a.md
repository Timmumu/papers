# Zhang, Y et al. (2024) — Research on Building Process Optimization Framework Based on BIM-DT

- **ID:** R579 | **Source:** Scopus | **DOI:** 10.17559/TV-20240115001267
- **Journal:** Tehnicki Vjesnik
- **Authors:** Zhang Y.; Shang K.

## Abstract summary
Aiming at the problems of low integration of enterprises in various parts of the construction process, low productivity, serious waste of resources, and poor construction safety, this project constructs a framework for optimizing the construction process based on BIM-DT through an in-depth analysis of the characteristics and development status of the digital twin technology and BIM technology. The framework is a complete cycle system, including data management system, BIM modeling system, and digital twin model, which are integrated with each stage of survey and design, construction preparation, construction, and operation and maintenance, respectively. Finally, in the empirical study, the construction phase is taken as the object of study, and the data management system is constructed to comprehensively demonstrate the realization process of each system, and the BP neural network is uti…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** BIM-DT building process optimization framework


## Step-3 Deep-Read Coding (Prompt B)
| P DT-subject | Q DfS/DfQ | R codable | U Tier | V Design | W Constr | X Oper | Z DfX | AA Self-improve | AB Methodology | AC Modality | AD Validation | AE QA(0-5) | AF Cluster |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow (one-way physical to virtual) | 0 | 1 | 0 | Design for Safety (DfS) | None | Other / Mixed | Multi (two or more data types) | Single case study | 3 | Lifecycle / governance |

| AC1 fusion depth | AC2 fusion evidence | AC3 confidence |
|---|---|---|
| Fused | A BP neural network is trained on construction-phase data to diagnose nine fault types (construction joints, grouting, pouring sequence), so diagnosis depends on multiple input channels simultaneously. | Medium |

**Key evidence (AG):** Building process optimization framework based on BIM-DT (whole lifecycle: survey/design, construction preparation, construction, O&M): integrates data management system + BIM modelling system + digital twin model with real-time feedback; in the empirical study the construction phase data management system is built and a BP neural network is used for construction fault diagnosis (avg 99% accuracy vs CNN 90.23%, SVM 89.19%, PSO 88.35%; 9 fault types incl. construction joints, grouting, pouring sequence). One-way monitoring→fault diagnosis/safety; framework is partly conceptual (stage integration with BIM-DT model not described in detail — acknowledged), no actuation and no learning loop.

*Full-text source: 04c-port*

**AH — strength & gap filled:** Builds a whole-lifecycle construction process optimization framework integrating a data management system, BIM modelling system, and Flexsim digital twin across survey, design, construction, and operation phases, feeding detected problems back to the BIM model to eliminate information islands. A BP neural network diagnoses eight construction fault types with 99 percent average accuracy versus 90.23, 89.19, and 88.35 percent for CNN, SVM, and PSO baselines.

**AI — deficiencies & future work:** The framework is mostly conceptual; the paper does not describe in detail how each construction stage integrates and upgrades with the BIM-DT model, and the empirical study covers only the construction phase. Future research will focus on applying each stage of the framework in practice.
