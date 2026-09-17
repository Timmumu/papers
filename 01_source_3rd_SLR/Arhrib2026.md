# Arhrib et al. (2026) — Serverless 3D Reconstruction and Spatial Anchoring for Cloud-Native Infrastructure Inspection

- **ID:** 3828 | **Source:** Scopus | **DOI:** 10.3390/buildings16122433
- **Journal:** Buildings
- **Authors:** Arhrib, Y.; Alvarez-Taboada, F.; Boulaassal, H.

## Abstract summary
While infrastructure asset management increasingly relies on high-resolution drone imagery, existing workflows suffer from fragmented information management and dependence on costly local processing infrastructure. This paper addresses these limitations by using a cloud-native spatial intelligence hub that converts raw inspection imagery into an interactive and queryable three-dimensional information layer. The system integrates a timeout-resilient orchestration layer for photogrammetry pipelines, a multi-user three-dimensional environment for collaborative review, and a PostGIS-backed spatial database that stores defects as georeferenced anchors. We further introduce a spatial anchoring workflow mapping three-dimensional interactions to world coordinates, retrieving context-relevant images via frustum-based visibility scoring. Evaluated on real inspection datasets, the serverless archit…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** Cloud DT for infrastructure inspection; defects as georeferenced anchors

## Step-3 Deep-Read Coding (Prompt B) — full text via MDPI Buildings (GOLD OA, mdpi-res mirror)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 1 - Digital Model | 0 | 0 | 1 | DfQ | None | Digital Twin platform (no ML) | Multi | Single case study | 4 | Perception / Computer Vision |

**Key evidence (AG):** Cloud-native "Spatial Intelligence Hub": serverless, timeout-resilient orchestration of SfM/MVS photogrammetry, multi-user 3D review environment, PostGIS spatial DB storing defects as georeferenced anchors, frustum-based visibility scoring for image retrieval. Validated on real inspection datasets (reconstruction < 1 h, query < 25 ms). Authors explicitly contrast with passive "Level 1" twins yet the workflow is periodic re-scan, not live data: Tier 1. Strong DfQ relevance: traceable, spatially indexed defect evidence for infrastructure DTs.

**Strength & gap filled (AH):** Addresses fragmented inspection data by replacing desktop photogrammetry with a serverless spatial intelligence hub: timeout-resilient orchestration of SfM/MVS, PostGIS-anchored defect records linked to georeferenced 3D meshes via raycasting and frustum-based image retrieval, end-to-end reconstruction in under one hour, sub-25 ms query latency, and over 90% image retrieval accuracy on two real UAV inspection datasets.

**Deficiencies & future work (AI):** No automated defect detection: annotations are manually created by human inspectors, which the authors call the main bottleneck for scaling; validation covers only two UAV datasets, hyperparameters are not systematically optimized, and the system assumes reliable connectivity. Future work includes automated detection, temporal change monitoring, 3D Gaussian Splatting visualization, and offline capabilities.

**Fusion depth (AC1):** Aligned

**Fusion evidence (AC2):**
- **Data streams:** UAV imagery-derived 3D meshes + georeferenced defect records on two real inspection datasets.
- **Integration mechanism:** defect records are anchored to the georeferenced meshes in PostGIS via raycasting and frustum-based image retrieval, putting imagery geometry and defect annotations in one spatial reference frame (sub-25 ms queries, over 90% retrieval accuracy).
- **Why this code:** the two data types share a spatial (georeferenced) frame while annotation and reconstruction run separately, so Aligned.

**Confidence (AC3):** High - the raycasting/frustum anchoring mechanism is explicit in the full text.