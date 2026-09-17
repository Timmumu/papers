# Liu et al. (2020) — Intelligent tensioning method for prestressed cables based on digital twins and artificial intelligence

- **ID:** 3573 | **Source:** Scopus | **DOI:** 10.3390/s20247006
- **Journal:** Sensors (Switzerland)
- **Authors:** Liu, Z.; Shi, G.; Zhang, A.; Huang, C.

## Abstract summary
In this study, to address the problems of multiple dimensions, large scales, complex tension resource scheduling, and strict quality control requirements in the tensioning process of cables in prestressed steel structures, the technical characteristics of digital twins (DTs) and artificial intelligence (AI) are analyzed. An intelligent tensioning of prestressed cables method driven by the integration of DTs and AI is proposed. Based on the current research status of cable tensioning and DTs, combined with the goal of intelligent tensioning, a fusion mechanism for DTs and AI is established and their integration to drive intelligent tensioning of prestressed cables technology is analyzed. In addition, the key issues involved in the construction of an intelligent control center driven by the integration of DTs and AI are discussed. By considering the construction elements of space and time …

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** DT+AI intelligent tensioning of prestressed cables; safety evaluation

## Step-3 Deep-Read Coding (Prompt B)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 3 - Digital Twin (bidirectional, two-way) | 0 | 1 | 0 | Design for Safety (DfS) | None | Other / Mixed | Multi (two or more data types) | Single case study | 4 | Design for Safety |

**Key evidence (AG):** Intelligent tensioning method for prestressed cables via DT + AI integration (Beijing U Tech): fusion mechanism of DTs and AI for intelligent tensioning; multi-dimensional/multi-scale modeling for visualization; AI control center with closed-loop control framework; sensing equipment + intelligent algorithms for high-fidelity twin model and safety performance evaluation; enables dynamic perception, real-time processing, intelligent diagnosis, and intelligent decision-making. Closed-loop control framework → Tier 3; no learning loop (AI is control/decision, not self-improving).


**Strength & gap filled (AH):** Moves digital twin application beyond reflecting reality toward virtual control of reality for cable tensioning: a fusion mechanism of digital twins and AI with multi-dimensional and multi-scale twin agents, a DBN (RBM pretraining plus BP fine-tuning) predicting cable forces, and a 1:10 wheel-spoke cable truss test where twin correction against sensor strain cut cable-force errors to within 3 percent and DBN-based safety levels guided maintenance under quarter-span live load.

**Deficiencies & future work (AI):** The system is demonstrated only on a 1:10 scale test model rather than a full-scale project, and the authors acknowledge intelligent tensioning research is still preliminary with the DBN trained on historical mining data. Further work calls for deeper digital twin and AI integration and improved information collection and communication for whole-process tensioning control.
**Fusion depth (AC1):** Fused

**Fusion evidence (AC2):**
- **Data streams:** strain-sensor measurements on a 1:10 wheel-spoke cable truss + twin/DBN model outputs.
- **Integration mechanism:** twin correction against sensor strain is the joint step (virtual-real fusion), and DBN-based safety levels guide maintenance under quarter-span live load.
- **Why this code:** the corrected twin output depends on measured and modelled data simultaneously, so Fused; 1:10 scale test only (Medium).

**Confidence (AC3):** Medium - the correction mechanism is explicit, but validation is a scale model.
(full-text source: Endnote)
