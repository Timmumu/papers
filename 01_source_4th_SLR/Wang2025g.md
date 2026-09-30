# Wang, K et al. (2025) — Digital twin safety analysis of large-span spatial structure based on airborne LiDAR

- **ID:** R416 | **Source:** Scopus | **DOI:** 10.1016/j.jobe.2025.112126
- **Journal:** Journal of Building Engineering
- **Authors:** Wang K.; Zhang C.; Qian Y.; Huang W.; Yi T.; Wang J.; Huang D.; Zha X.

## Abstract summary
This paper introduces a novel method for assessing the safety of post-construction large-span spatial structures. Initially, a brief overview is provided of the operating principles and measurement equipment associated with airborne Light Detection and Ranging (LiDAR) technology. Subsequently, a methodology for extracting one-dimensional geometric models from point cloud data is described. The proposed safety analysis method is then applied to the retractable roof of the Shenzhen Gymnasium, with a comparison made between two approaches: the LiDAR-based method and the consistent imperfection mode method, in terms of their consideration of the impact of initial geometric imperfections on structural mechanical properties. The research findings reveal that the one-dimensional geometric models extracted from airborne LiDAR measurements can accurately reflect the real-world structural imperfec…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** Airborne LiDAR geometric DT for spatial structure safety

## Step-3 Deep-Read Coding (Prompt B)
| P DT-subject | Q DfS/DfQ | R codable | U Tier | V Design | W Constr | X Oper | Z DfX | AA Self-improve | AB Methodology | AC Modality | AD Validation | AE QA(0-5) | AF Cluster |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 1 - Digital Model (static, no live data) | 0 | 0 | 1 | Design for Safety (DfS) | None | Finite Element Method / physics-based | Single (one data type) | Single case study | 4 | Design for Safety |

| AC1 fusion depth | AC2 fusion evidence | AC3 confidence |
|---|---|---|
| SINGLE | Only LiDAR geometry enters the analysis; no second measured data type. | High |

**Key evidence (AG):** Geometric digital twin from airborne LiDAR for safety analysis of large-span spatial structures (HIT Shenzhen, J Build Eng 2025): one-dimensional geometric models extracted from point clouds capture real initial geometric imperfections of the Shenzhen Gymnasium retractable roof; FE models built from LiDAR measurements represent real structural performance better than the consistent-imperfection-mode method for stability/safety assessment. One-off measurement -> geometric twin -> FE safety analysis; no live data link, no actuation, no learning loop.

*Full-text source: Endnote*

**AH — strength & gap filled:** Fills the initial-imperfection gap in large-span spatial-structure safety analysis: airborne-LiDAR-derived 1D geometric twins capture real imperfections of the Shenzhen Gymnasium roof, and FE models from these twins represent real structural performance better than the consistent-imperfection-mode method.

**AI — deficiencies & future work:** One-off LiDAR survey of one roof; the static geometric twin does not feed a live monitoring loop, and sensitivity to point-cloud density, scanning coverage and member-level defect capture is not fully quantified.
