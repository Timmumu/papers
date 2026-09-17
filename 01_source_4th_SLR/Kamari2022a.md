# Kamari, M et al. (2022) — AI-based risk assessment for construction site disaster preparedness through deep learning-based digital twinning

- **ID:** R937 | **Source:** Web of Science | **DOI:** 10.1016/j.autcon.2021.104091
- **Journal:** AUTOMATION IN CONSTRUCTION
- **Authors:** Kamari, M; Ham, Y

## Abstract summary
Hurricanes are among the most devastating natural disasters in the United States, causing billions of dollars of property damage and insured losses. During extreme wind events, unsecured objects in jobsites can easily become airborne debris, which results in substantial loss to construction projects and neighboring communities. Towards a systematic disaster preparedness in construction jobsites, this paper presents a novel vision-based digital twinning and threat assessment framework. We encode the context of disaster risk into deep-learning architectures to identify and analyze the characteristics and impacts of potential wind-borne debris in construction site digital twin models. Case studies on nine piles of construction materials are presented to demonstrate and discuss the fidelity of the proposed computational modules. The proposed methods are expected to help provide heads up for …

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** Vision-based DT for construction disaster preparedness


## Step-3 Deep-Read Coding (Prompt B)
| P DT-subject | Q DfS/DfQ | R codable | U Tier | V Design | W Constr | X Oper | Z DfX | AA Self-improve | AB Methodology | AC Modality | AD Validation | AE QA(0-5) | AF Cluster |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 1 - Digital Model (static, no live data) | 0 | 1 | 0 | Design for Safety (DfS) | None | Perception / Computer Vision | Multi (two or more data types) | Single case study | 4 | Design for Safety |

| AC1 fusion depth | AC2 fusion evidence | AC3 confidence |
|---|---|---|
| Fused | SfM/MVS photogrammetry reconstructs jobsite point clouds, ResNet50 semantic segmentation runs in 2D and a depth-aware projection fuses the two into 3D semantic segmentations (97.85 to 99.8% accuracy). | High |

**Key evidence (AG):** Vision-based digital twinning and threat assessment for construction site disaster preparedness (Texas A&M): deep learning encodes disaster risk context into construction site digital twin models to identify and analyze potential wind-borne debris characteristics and impacts; case studies on nine piles of construction materials; rapid 2D/3D semantic segmentation for vulnerability flagging. Static DT for risk assessment — no live data link, no actuation, no learning loop.

*Full-text source: 04c-port*

**AH — strength & gap filled:** Systematizes pre-hurricane preparedness beyond error-prone manual checklist inspection: SfM and MVS photogrammetry reconstruct jobsite point clouds, ResNet50 semantic segmentation reaches 98.2 percent accuracy, and a depth-aware projection raises 3D segmentation accuracy from 97.85 to 99.8 percent; volumetric measurement of nine material piles (errors 2.4 to 9.2 percent) feeds kinetic-energy threat heatmaps at hurricane-category wind speeds.

**AI — deficiencies & future work:** Case studies are static snapshots of two jobsites without live data integration. Segmentation is expected to degrade in rain, fog, or dim light and under occlusions and moving objects; volumetric measurement overestimates unstacked piles because RGB cameras cannot see inside them. Building robust machine vision accounting for these challenges is the direction of ongoing research.
