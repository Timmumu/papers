# Tian, FH et al. (2026) — Defect Trigger Identification in a Construction Digital Twin Using Quality Linked Data and Iterative Deviation Computation

- **ID:** R927 | **Source:** Web of Science | **DOI:** 10.1061/JCEMD4.COENG-18029
- **Journal:** JOURNAL OF CONSTRUCTION ENGINEERING AND MANAGEMENT
- **Authors:** Tian, FH; Zeng, NS; Li, ZR; Ge, QZ; Wang, Q; Li, QM

## Abstract summary
Current quality management in construction faces several challenges, including insufficient precision in control, unclear allocation of quality responsibilities, and a lack of long-term management mechanisms. As the industry shifts from a problem-solving after occurrence approach to a proactive paradigm, identification of potential quality defects and risks has become a primary prerequisite. This study introduces the concept of quality defect triggers, detectable, modelable, and controllable precursors to quality issues that operationalize risk factors and can be visualized within a construction digital twin (DT). Building on an exploration of their evolutionary mechanisms, the study develops an integrated framework that combines ontology and linked data technologies to identify quality defect triggers through multisource heterogeneous data integration, comprising three core components: …

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** Quality defect triggers in construction digital twin

## Step-3 Deep-Read Coding (Prompt B)
| P DT-subject | Q DfS/DfQ | R codable | U Tier | V Design | W Constr | X Oper | Z DfX | AA Self-improve | AB Methodology | AC Modality | AD Validation | AE QA(0-5) | AF Cluster |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow (one-way physical to virtual) | 0 | 1 | 0 | Design for Quality (DfQ) | None | Ontology / semantic | Multi (two or more data types) | Single case study | 4 | Semantic interoperability |

| AC1 fusion depth | AC2 fusion evidence | AC3 confidence |
|---|---|---|
| Fused | Multisource heterogeneous data are semantically linked in an ontology-based four-layer model in GraphDB, and SPARQL iterative deviation computation reasons over the linked data to identify quality defect triggers. | High |

**Key evidence (AG):** Quality defect trigger identification in a construction digital twin (Southeast U): evolution-mechanism + ontology-based four-layer semantic model (quality standards / quality data / defect triggers / construction processes) implemented in GraphDB for semantic linkage of multisource heterogeneous data; an iterative deviation-computation engine (process logic + rule constraints) identifies potential quality defect triggers and visualises them in the DT; validated on a real prefabricated composite-slab installation case + comparative experiments + expert evaluation. One-way data integration→reasoning→identification/visualisation for proactive quality management; no actuation, no self-improvement loop.

*Full-text source: 04c-port*

**AH — strength & gap filled:** Fills the granularity gap between abstract quality risk and concrete defects: a quality-defect-trigger concept with an evolution-mechanism, ontology-based four-layer semantic model and GraphDB linked-data pipeline uses SPARQL deviation computation to flag triggers exceeding tolerance thresholds, identifying a 4.63 mm x-axis misalignment and 2.9 mm seam-flatness deviation in a prefabricated composite-slab installation while reaching 100 percent identification accuracy in 371 s.

**AI — deficiencies & future work:** The framework depends on high-quality real-time data, lacks a standardized defect-trigger grading and remediation system, offers limited BIM and mobile-platform integration and weak visualization, and management-related and human-related triggers remain under-detected; future work targets data robustness, multiplatform DT integration, grading models, and reinforcement learning or large language model support.
