# Levine et al. (2022) — Post-Earthquake Building Evaluation Using UAVs: A BIM-Based Digital Twin Framework

- **ID:** 3712 | **Source:** Scopus | **DOI:** 10.3390/s22030873
- **Journal:** Sensors
- **Authors:** Levine, N. M.; Spencer, B. F.

## Abstract summary
Computer vision has shown potential for assisting post-earthquake inspection of buildings through automatic damage detection in images. However, assessing the safety of an earthquake-damaged building requires considering this damage in the context of its global impact on the structural system. Thus, an inspection must consider the expected damage progression of the associated component and the component’s contribution to structural system performance. To address this issue, a digital twin framework is proposed for post-earthquake building evaluation that integrates unmanned aerial vehicle (UAV) imagery, component identification, and damage evaluation using a Building Information Model (BIM) as a reference platform. The BIM guides selection of optimal sets of images for each building component. Then, if damage is identified, each image pixel is assigned to a specific BIM component, using …

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** BIM-based DT framework for post-earthquake building evaluation

## Step-3 Deep-Read Coding (Prompt B) — full text verified via Endnote library (front-matter DOI match)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow | 0 | 0 | 1 | Design for Safety (DfS) | None | Computer Vision / CNN / object-detection | Multi (two or more data types) | Single case study | 4 | Perception / Computer Vision |

**Key evidence (AG):** BIM-based digital twin framework for post-earthquake building evaluation from UAV surveys: BIM guides automatic selection of optimal images per damage-sensitive component; GrabCut+nearest-neighbour segmentation assigns image pixels to BIM components (IoU 0.80–0.90); 3D point-cloud change detection (pre/post) identifies damaged nonstructural walls (std-dev indicator, threshold 0.010, correct at moderate-severe levels); damage tied to BIM to link with fragility curves + structural analysis for global safety. Example 1 = real Turner Hall RC frame; Example 2 = synthetic graphics. Framework not fully validated end-to-end (future PBGM work); one-way inspection pipeline, no learning loop.
