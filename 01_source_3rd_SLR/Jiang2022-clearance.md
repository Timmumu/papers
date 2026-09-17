# Jiang et al. (2022) — Underpass clearance checking in highway widening projects using digital twins

- **ID:** 3930 | **Source:** Web of Science | **DOI:** 10.1016/j.autcon.2022.104406
- **Journal:** AUTOMATION IN CONSTRUCTION
- **Authors:** Jiang, F.; Ma, L.; Broyd, T.; Chen, K.; Luo, H. B.

## Abstract summary
Main road widening can reduce the clearance of the low-level underpass road, restricting the passage of vehicles and leading to collisions with structures. Therefore, checking the clearance of the underpass road effectively should be considered at the design stage. This paper describes a digital twin approach for checking the clearance of underpass roads in highway widening projects using online map data. The underpass road digital twin and BIM model of the newly widened road based on the existing main road digital twin are created to assist the clearance check and redesign. The proposed method presented a cost-effective clearance check for underpass roads in road widening design without field surveys and was successfully implemented in an underpass road in the UK. In future research, more digital twin methods for overpasses, bridges, tunnels, and traffic safety facilities should be empl…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** DT clearance checking for underpasses; collision prevention at design

## Step-3 Deep-Read Coding (Prompt B)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 1 - Digital Model (static, no live data) | 1 | 0 | 0 | Design for Safety (DfS) | None | Digital Twin platform (no machine learning) | Multi (two or more data types) | Single case study | 3 | Design for Safety |

**Key evidence (AG):** Digital twin approach for underpass clearance checking in highway widening projects (UCL/HUST): online map data (DSM, DEM, aerial photos) → digital twin of existing main road + underpass road → BIM model of widened road; clearance check and redesign at preliminary design stage; cost-effective without field surveys; implemented on a UK underpass road. One-way design-stage analysis→clearance check; no live data link, no actuation, no learning loop.


**Strength & gap filled (AH):** Fills the gap of preliminary clearance checking without field surveys: a digital twin method reconstructing the existing main road and underpass road from online map data (Digimap DSM, DTM and aerial photos) via road-marking extraction, smoothing-spline alignment fitting at R-square near 1.0, and flattened terrain models; clash detection of a 5.338 m clearance envelope in the M11 and Sawbridgeworth Road case caught insufficient clearance and guided redesign of underpass vertical alignment.

**Deficiencies & future work (AI):** Accuracy was not compared with field survey data, which the authors admit is needed to evaluate the method, and only underpass roads are handled; future research will validate through field surveys, focus groups and expert interviews, and extend the approach to overpasses, bridges, tunnels and traffic safety facilities.
**Fusion depth (AC1):** Fused

**Fusion evidence (AC2):**
- **Data streams:** Digimap DSM, DTM and aerial photography.
- **Integration mechanism:** road-marking extraction, smoothing-spline alignment (R-square near 1.0) and flattened terrain models combine the map layers into a single reconstructed twin, against which a 5.338 m clearance envelope is clash-checked (M11/Sawbridgeworth Road case).
- **Why this code:** the reconstructed model depends on several map data layers simultaneously, so Fused.

**Confidence (AC3):** Medium - joint reconstruction is clear, but map layers are all geospatial products of one survey family.
(full-text source: Endnote)
