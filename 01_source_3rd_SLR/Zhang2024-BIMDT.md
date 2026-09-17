# Zhang et al. (2024) — Research on Building Process Optimization Framework Based on BIM-DT

- **ID:** 3885 | **Source:** Web of Science | **DOI:** 10.17559/TV-20240115001267
- **Journal:** TEHNICKI VJESNIK-TECHNICAL GAZETTE
- **Authors:** Zhang, Y. M.; Shang, K. J.

## Abstract summary
Aiming at the problems of low integration of enterprises in various parts of the construction process, low productivity, serious waste of resources, and poor construction safety, this project constructs a framework for optimizing the construction process based on BIM-DT through an in-depth analysis of the characteristics and development status of the digital twin technology and BIM technology. The framework is a complete cycle system, including data management system, BIM modeling system, and digital twin model, which are integrated with each stage of survey and design, construction preparation, construction, and operation and maintenance, respectively. Finally, in the empirical study, the construction phase is taken as the object of study, and the data management system is constructed to comprehensively demonstrate the realization process of each system, and the BP neural network is uti…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** BIM-DT building process optimization incl. construction safety; fault diagnosis

## Step-3 Deep-Read Coding (Prompt B) — full text verified via Endnote library (front-matter DOI/title match, coverage re-scan 2026-08-12)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow | 0 | 1 | 0 | Design for Safety (DfS) | None | Other / Mixed | Multi (two or more data types) | Single case study | 3 | Lifecycle / governance |

**Key evidence (AG):** Building process optimization framework based on BIM-DT (whole lifecycle: survey/design, construction preparation, construction, O&M): integrates data management system + BIM modelling system + digital twin model with real-time feedback; in the empirical study the construction phase data management system is built and a BP neural network is used for construction fault diagnosis (avg 99% accuracy vs CNN 90.23%, SVM 89.19%, PSO 88.35%; 9 fault types incl. construction joints, grouting, pouring sequence). One-way monitoring→fault diagnosis/safety; framework is partly conceptual (stage integration with BIM-DT model not described in detail — acknowledged), no actuation and no learning loop.

**Strength & gap filled (AH):** Builds a whole-lifecycle construction process optimization framework integrating a data management system, BIM modelling system, and Flexsim digital twin across survey, design, construction, and operation phases, feeding detected problems back to the BIM model to eliminate information islands. A BP neural network diagnoses eight construction fault types with 99 percent average accuracy versus 90.23, 89.19, and 88.35 percent for CNN, SVM, and PSO baselines.

**Deficiencies & future work (AI):** The framework is mostly conceptual; the paper does not describe in detail how each construction stage integrates and upgrades with the BIM-DT model, and the empirical study covers only the construction phase. Future research will focus on applying each stage of the framework in practice.

**Fusion depth (AC1):** Fused

**Fusion evidence (AC2):**
- **Data streams:** construction-phase monitoring data feeding fault diagnosis in the data-management + BIM + Flexsim framework.
- **Integration mechanism:** the BP network jointly consumes the data channels to diagnose nine fault types (99% average accuracy versus CNN 90.23%, SVM 89.19%, PSO 88.35%), with problems fed back to the BIM model.
- **Why this code:** a multi-input diagnosis model, so Fused; the wider framework integration remains partly conceptual (Medium).

**Confidence (AC3):** Medium - the BP diagnosis is explicit; stage integration of the framework is not detailed.