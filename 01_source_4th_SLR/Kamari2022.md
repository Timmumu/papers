# Kamari, M et al. (2022) — Analyzing Safety Risk Imposed by Jobsite Debris to Nearby Built Environments Using Geometric Digital Twins and Vision-Based Deep Learning

- **ID:** R785 | **Source:** Scopus | **DOI:** 10.1061/(ASCE)CP.1943-5487.0001044
- **Journal:** Journal of Computing in Civil Engineering
- **Authors:** Kamari M.; Kim J.; Ham Y.

## Abstract summary
Extreme wind events can pick up loose and small objects on the ground, and once the objects become airborne, they negatively impact surrounding communities due to the collision impact. In this regard, jobsites and laydown yards that involve construction materials such as gravel piles and crushed rocks could be the main sources of potential windborne debris during extreme wind events. To analyze safety risk and predict the damage imposed by jobsite debris to nearby built environments, a new computer vision-based risk assessment based on geometric digital twins of jobsite debris is proposed for the reliability analysis on glazing systems of dwellings located on nearby jobsites. The impact of a gravel pile in a railroad jobsite on nearby buildings and residential environments was studied based on extreme wind event scenarios, and the failure risk of the building glazing system was computed.…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** Geometric DTs for windborne debris risk to built environments

## Step-3 Deep-Read Coding (Prompt B)
| P DT-subject | Q DfS/DfQ | R codable | U Tier | V Design | W Constr | X Oper | Z DfX | AA Self-improve | AB Methodology | AC Modality | AD Validation | AE QA(0-5) | AF Cluster |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 1 - Digital Model (static, no live data) | 0 | 1 | 0 | Design for Safety (DfS) | None | Perception / Computer Vision | Multi (two or more data types) | Single case study | 4 | Design for Safety |

| AC1 fusion depth | AC2 fusion evidence | AC3 confidence |
|---|---|---|
| Fused | UAV photogrammetry, Street-View CNN segmentation and satellite terrain modelling are combined in one HAZUS-based reliability computation of nearby glazing systems under windborne-debris impact. | High |

**Key evidence (AG):** Vision-based risk assessment of jobsite windborne-debris impact on nearby dwellings: geometric digital twin of a gravel pile built from 45 UAV aerial images (dense point cloud + binarized DSM, volume 63 m³, EM ~4.6%) + semantic segmentation of glazing panels via CNNs (ResNet50 85.0% acc) from Google Street View + satellite terrain modeling; reliability of glazing systems computed with FEMA-HAZUS windborne-missile model (N_adjusted ~237 impacts at 62 m/s, 80 m). Static one-shot reconstruction/analysis — no live data link and no learning loop.

*Full-text source: 04c-port*

**AH — strength & gap filled:** Extends jobsite debris risk assessment to neighboring communities: a geometric digital twin of a railroad jobsite gravel pile built from 45 UAV images (volumetric error about 4.6 percent) feeds a HAZUS-based glazing reliability model together with ResNet50 street-view window segmentation (85.0 percent accuracy), computing failure probability of nearby dwelling glazing systems across 35 to 65 m/s wind scenarios.

**AI — deficiencies & future work:** Relies on static Google Street View and UAV imagery with no live wind or site monitoring; facade occlusion by cars and trees degrades window detection, and performance drops in rain and fog. HAZUS assumptions such as uniform gravel size and persistent wind direction and the lack of validation against real disaster cases remain; collecting such data at scale is future work.
