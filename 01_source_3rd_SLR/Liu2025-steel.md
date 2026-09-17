# Liu et al. (2025) — Intelligent safety control modeling and construction process control of steel mesh frame structures

- **ID:** 3952 | **Source:** Web of Science | **DOI:** 10.1016/j.istruc.2025.109158
- **Journal:** STRUCTURES
- **Authors:** Liu, Z. S.; Ji, C. K.; Zhang, Q. W.

## Abstract summary
In the process of large-span steel structure construction, because its structure has not yet formed a complete system, so its mechanical properties and safety status are not stable, and it is necessary to control the safety of the structure, and the current traditional structural health monitoring (SHM) has the problems of high cost, easy to be interfered, and unpredictable, etc. The digital twin, as a popular technology in the engineering industry, has the characteristics of multidimensionality, high integrative, intelligent and real-time, so it is very necessary to introduce digital twin technology in the construction process. In this paper, a digital twin-driven intelligent safety control method for large-span steel structures is proposed. The digital twin model is constructed by collecting actual engineering data and integrating finite element analysis data. Based on the random fores…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** DT-driven intelligent safety control of large-span steel construction

## Step-3 Deep-Read Coding (Prompt B)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow (one-way physical to virtual) | 0 | 1 | 0 | Design for Safety (DfS) | None | Other / Mixed | Multi (two or more data types) | Single case study | 4 | Predictive analytics / decision support |

**Key evidence (AG):** Digital twin-driven intelligent safety control for large-span steel mesh frame structures (Beijing U Tech): DT model built from actual engineering data + FE analysis; random forest algorithm analyzes influencing factors of overall jacking construction process (jacking height difference and jacking speed most influential); real-time monitoring + fault diagnosis; validated on airport reconstruction project. One-way monitoring→analysis→safety control; no actuation and no learning loop (random forest is offline-trained).


**Strength & gap filled (AH):** Fills the gap of costly experience-based health monitoring for large-span steel mesh frames by combining a digital twin with geometric, finite-element, behavioral and rule models with random forest feature-importance analysis of overall jacking data from an airport project, showing that maximum jacking height difference and jacking speed dominate structural stress, consistent with construction code provisions.

**Deficiencies & future work (AI):** The random forest provides importance ranking rather than prediction accuracy metrics, safety control relies on rule-based alarms and shutdown commands without learning-based updating, and only one airport project validates the method; the authors state data transmission efficiency must improve and plan extension to bridges and high-rise platforms with better sensors and optimized predictive algorithms.
**Fusion depth (AC1):** Fused

**Fusion evidence (AC2):**
- **Data streams:** geometric, FE, behavioural and rule model outputs plus real-time jacking monitoring channels on an airport project.
- **Integration mechanism:** random forest jointly consumes the monitoring channels to compute feature importance, driving rule-based alarms and shutdown commands in the twin.
- **Why this code:** the importance-ranking model depends on multiple data channels simultaneously, so Fused.

**Confidence (AC3):** High - the random-forest analysis is explicit.
(full-text source: Endnote)
