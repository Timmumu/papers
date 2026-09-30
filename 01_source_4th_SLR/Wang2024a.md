# Wang, J et al. (2024) — Development and validation of graphics-based digital twin framework for UAV-aided post-earthquake inspection of high-rise buildings

- **ID:** R599 | **Source:** Scopus | **DOI:** 10.1002/tal.2127
- **Journal:** Structural Design of Tall and Special Buildings
- **Authors:** Wang J.; Wu Y.; Wang S.; Narazaki Y.; Liu H.; Spencer B.F., Jr.

## Abstract summary
Traditional post-earthquake inspection of civil infrastructure is conducted manually, taking a considerable amount of time and often putting inspectors in harm's way. This problem is exacerbated in modern cities, where millions of people can be left homeless until their residences are deemed safe to reinhabit. Image collection enabled by commercial unmanned aerial vehicles (UAVs) combined with computer vision-based techniques has provided an alternative with high potential for rapid post-earthquake inspection. However, the extracted images of the damage alone are inadequate to evaluate the system-level safety condition of a structure. The quality of the visual information also heavily relies on the effectiveness of the UAV inspection scheme which is susceptible to environmental uncertainties. To this end, a graphics-based digital twin (GBDT) framework is developed for UAV-aided post-eart…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** Graphics-based DT for UAV post-earthquake inspection

## Step-3 Deep-Read Coding (Prompt B)
| P DT-subject | Q DfS/DfQ | R codable | U Tier | V Design | W Constr | X Oper | Z DfX | AA Self-improve | AB Methodology | AC Modality | AD Validation | AE QA(0-5) | AF Cluster |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 1 - Digital Model (static, no live data) | 0 | 0 | 1 | Design for Safety (DfS) | None | Finite Element Method / physics-based | Multi (two or more data types) | Simulation | 4 | Perception / Computer Vision |

| AC1 fusion depth | AC2 fusion evidence | AC3 confidence |
|---|---|---|
| Aligned | The FE model and the photorealistic CG model share one imported building geometry (SAP2000 to Blender), so the two model types are aligned by component, while UAV flight-scheme evaluation runs on the coupled model. | Medium |

**Key evidence (AG):** Graphics-based digital twin (GBDT) framework for UAV-aided post-earthquake inspection of high-rise buildings (Guangzhou U/UIUC): FE model + photorealistic computer graphics (CG) model; CG model automatically imports structural components from FE model + adds nonstructural components; GBDT used to evaluate UAV flight schemes for inspection; FE analysis determines earthquake-induced damage locations; three UAV inspection schemes implemented virtually to select best. Static DT for inspection planning — no live data link, no actuation, no learning loop.

*Full-text source: 04c-port*

**AH — strength & gap filled:** Fills the gap between image-only damage inspection and system-level planning: the graphics-based digital twin couples a SAP2000 finite element model with a photorealistic Blender computer graphics model of a 45-floor Guangzhou tower, validated against UAV photogrammetry point clouds, and uses earthquake damage hotspots plus environmental constraints to compare three UAV flight schemes, recommending a parallel path that stays within battery life.

**AI — deficiencies & future work:** A static, offline virtual testbed without live data or actuation; the optimal flight scheme conclusion is case-specific and simplified, damage comes from assumed seismic analysis, and no automated damage detection is yet implemented. Future development includes component-level FE analysis, part and texture libraries for automated CG modeling, multi-UAV path planning, and machine-learning damage detection trained on synthetic images.
