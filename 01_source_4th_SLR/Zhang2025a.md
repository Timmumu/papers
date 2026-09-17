# Zhang, C et al. (2025) — Digital Safety Navigation for Tower Crane Climbing Process from a Systematic Perspective: Risk Identification, Safety Information Requirements, and Related Intelligent Platform

- **ID:** R278 | **Source:** Scopus | **DOI:** 10.1061/JCEMD4.COENG-15772
- **Journal:** Journal of Construction Engineering and Management
- **Authors:** Zhang C.; Zhang W.; Shi Y.; Zhao T.; Zhang Y.

## Abstract summary
The tower crane climbing process is one of the most hazardous operations due to its complexity and technical challenges, making it difficult to ensure both structural and worker safety. To address this issue, this study proposes a systematic control framework based on digital navigation. This framework integrates theoretical risk analysis, safety information requirements, and the practical implementation of a safety intelligent navigation platform (SINP). Key safety-critical points in the tower crane climbing process are identified through process analysis, and worker situation awareness requirements are derived using goal-directed task analysis (GDTA). The SINP is designed to digitally capture safety-related data, assess safety conditions intelligently, and provide automated safety guidance. The platform enables systematic control of tower crane safety through three key functions: (1) r…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** Tower crane climbing safety navigation platform; DT


## Step-3 Deep-Read Coding (Prompt B)
| P DT-subject | Q DfS/DfQ | R codable | U Tier | V Design | W Constr | X Oper | Z DfX | AA Self-improve | AB Methodology | AC Modality | AD Validation | AE QA(0-5) | AF Cluster |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow (one-way physical to virtual) | 0 | 1 | 0 | Design for Safety (DfS) | None | Digital Twin platform (no machine learning) | Multi (two or more data types) | Simulation | 4 | Design for Safety |

| AC1 fusion depth | AC2 fusion evidence | AC3 confidence |
|---|---|---|
| Aligned | IoT sensors are mirrored into the four-layer DT virtual model (geometric/physical/behavioural/rule-based), and the edge intelligent control device issues navigation and alarms per signal threshold. | High |

**Key evidence (AG):** Safety Intelligent Navigation Platform (SINP) for tower crane climbing (HUST): systematic control framework integrating theoretical risk analysis (process analysis of key safety-critical points), GDTA-derived worker situation-awareness requirements, and a 4-layer digital twin virtual model (geometric/physical/behavioral/rule-based) with IoT-based real-time mapping/dataflow; edge intelligent control device (EICD) provides real-time safety navigation + alarms to workers, mobile monitoring for supervisors, cloud remote inspection; validated in indoor functional + outdoor practical experiments (task completion 515-676s→375-444s, errors 1.4-4.8→0, dialogues 11.8→0.8). One-way monitoring→navigation/alarms to humans; no automated actuation and no learning loop.

*Full-text source: 04c-port*

**AH — strength & gap filled:** Fills the gap between passive crane monitoring and proactive climbing-process safety control: the SINP framework couples process-based risk identification for the eight-step climbing cycle with GDTA-derived information requirements, then delivers navigation and alarms through IoT sensors and an edge intelligent control device, cutting dialogue counts from 11.8-12.2 to 0.8-1.6, completion times from 515.6-676.0 to 375.0-444.2 seconds and operational errors to zero in tests.

**AI — deficiencies & future work:** Validated on a scaled tower crane model plus one Xiangyang construction project, so generalizability is limited by the small sample size; impact on situation awareness was not systematically measured and testing scenarios may not capture real-world diversity. Future work includes integrating structural health monitoring and augmented reality into the platform.
