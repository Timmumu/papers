# Liu et al. (2022) — Digital Twins-Based Impact Response Prediction of Prestressed Steel Structure

- **ID:** 3669 | **Source:** Scopus | **DOI:** 10.3390/s22041647
- **Journal:** Sensors
- **Authors:** Liu, Z.; Yuan, C.; Sun, Z.; Cao, C.

## Abstract summary
Civil infrastructure O&M requires intelligent monitoring techniques and control methods to ensure safety. Unfortunately, tedious modeling efforts and the rigorous computing requirements of large-scale civil infrastructure have hindered the development of structural research. This study proposes a method for impact response prediction of prestressed steel structures driven by digital twins (DTs) and machine learning (ML). The high-fidelity DTs of a prestressed steel structure were constructed from the perspective of both a physical entity and virtual entity. A prediction of the impact response of prestressed steel structure’s key parts was established based on ML, and a structure response prediction of the parts driven by data was realized. To validate the effectiveness of the proposed prediction method, the authors carried out a case study in an experiment of a pre-stressed steel structu…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** DT+ML impact response prediction of prestressed steel structures

## Step-3 Deep-Read Coding (Prompt B)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow (one-way physical to virtual) | 0 | 0 | 1 | Design for Safety (DfS) | None | Other / Mixed | Multi (two or more data types) | Single case study | 4 | Predictive analytics / decision support |

**Key evidence (AG):** DT-based impact response prediction of prestressed steel structures (Beijing U Tech): high-fidelity DT from 3D laser scanning + BIM + FE simulation; improved BP algorithm predicts structural impact response; perception/transmission/analysis/service layers; validated on prestressed steel structure experiment. One-way monitoring→prediction→safety assessment; no actuation and no learning loop (BP is offline-trained).


**Strength & gap filled (AH):** Addresses the lack of efficient impact response prediction tools for structure O and M: a high-fidelity digital twin combining BIM, 3D laser scanning and ANSYS/LS-DYNA simulation, with an improved LM-BP neural network (14 inputs, 5 outputs) trained on 219 drop-hammer working conditions, achieving R of 0.99293 in training and 0.98766 in testing with 99.7 percent overall accuracy, versus 48 hours of physical testing.

**Deficiencies & future work (AI):** The model outputs single data points of peak cable force and displacement, not time-history responses, and is trained offline without online updating; 5G real-time transmission stability for large structures is an open challenge. Future research covers big data technologies for O and M data and integration with health monitoring and maintenance policy services.
**Fusion depth (AC1):** Aligned

**Fusion evidence (AC2):**
- **Data streams:** 3D laser-scanned geometry + BIM + FE simulation samples (219 drop-hammer conditions).
- **Integration mechanism:** scanning and BIM are merged into one high-fidelity model frame; the LM-BP network (14 inputs, 5 outputs) is trained on FE data alone, and experimental results only verify predictions.
- **Why this code:** geometry sources share the twin frame while inference runs per type, so Aligned.

**Confidence (AC3):** Medium - the shared-frame geometry merging is clear; no joint multi-source inference exists.
(full-text source: Endnote)
