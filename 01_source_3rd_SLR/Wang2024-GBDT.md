# Wang et al. (2024) — Development and validation of graphics-based digital twin framework for UAV-aided post-earthquake inspection of high-rise buildings

- **ID:** 4010 | **Source:** Web of Science | **DOI:** 10.1002/tal.2127
- **Journal:** STRUCTURAL DESIGN OF TALL AND SPECIAL BUILDINGS
- **Authors:** Wang, J. J.; Wu, Y. J. B.; Wang, S.; Narazaki, Y.; Liu, H.; Spencer, B. F., Jr.

## Abstract summary
Traditional post-earthquake inspection of civil infrastructure is conducted manually, taking a considerable amount of time and often putting inspectors in harm's way. This problem is exacerbated in modern cities, where millions of people can be left homeless until their residences are deemed safe to reinhabit. Image collection enabled by commercial unmanned aerial vehicles (UAVs) combined with computer vision-based techniques has provided an alternative with high potential for rapid post-earthquake inspection. However, the extracted images of the damage alone are inadequate to evaluate the system-level safety condition of a structure. The quality of the visual information also heavily relies on the effectiveness of the UAV inspection scheme which is susceptible to environmental uncertainties. To this end, a graphics-based digital twin (GBDT) framework is developed for UAV-aided post-eart…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** Graphics-based DT for UAV post-earthquake inspection of high-rises

## Step-3 Deep-Read Coding (Prompt B)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 1 - Digital Model (static, no live data) | 0 | 0 | 1 | Design for Safety (DfS) | None | Finite Element Method / physics-based | Multi (two or more data types) | Simulation | 4 | Perception / Computer Vision |

**Key evidence (AG):** Graphics-based digital twin (GBDT) framework for UAV-aided post-earthquake inspection of high-rise buildings (Guangzhou U/UIUC): FE model + photorealistic computer graphics (CG) model; CG model automatically imports structural components from FE model + adds nonstructural components; GBDT used to evaluate UAV flight schemes for inspection; FE analysis determines earthquake-induced damage locations; three UAV inspection schemes implemented virtually to select best. Static DT for inspection planning — no live data link, no actuation, no learning loop.


**Strength & gap filled (AH):** Fills the gap between image-only damage inspection and system-level planning: the graphics-based digital twin couples a SAP2000 finite element model with a photorealistic Blender computer graphics model of a 45-floor Guangzhou tower, validated against UAV photogrammetry point clouds, and uses earthquake damage hotspots plus environmental constraints to compare three UAV flight schemes, recommending a parallel path that stays within battery life.

**Deficiencies & future work (AI):** A static, offline virtual testbed without live data or actuation; the optimal flight scheme conclusion is case-specific and simplified, damage comes from assumed seismic analysis, and no automated damage detection is yet implemented. Future development includes component-level FE analysis, part and texture libraries for automated CG modeling, multi-UAV path planning, and machine-learning damage detection trained on synthetic images.
**Fusion depth (AC1):** Aligned

**Fusion evidence (AC2):**
- **Data streams:** SAP2000 FE components + Blender CG model + UAV photogrammetry point-cloud validation (45-floor Guangzhou tower).
- **Integration mechanism:** structural components are automatically imported from FE into the CG model, sharing one geometry frame; damage hotspots and environmental constraints then drive the three flight-scheme evaluations.
- **Why this code:** model types share a common geometry reference while analysis runs per stage, so Aligned; no live data.

**Confidence (AC3):** Medium - the FE-to-CG import is explicit; the twin is static.
(full-text source: Endnote)
