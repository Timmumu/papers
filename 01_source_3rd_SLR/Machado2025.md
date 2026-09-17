# Machado et al. (2025) — Automated procedural modeling for tunnel inspection and digital twin development

- **ID:** 3965 | **Source:** Web of Science | **DOI:** 10.1016/j.tust.2025.106929
- **Journal:** TUNNELLING AND UNDERGROUND SPACE TECHNOLOGY
- **Authors:** Machado, L. B.; Poncetti, B. L.; de Assis, L. S.; Futai, M. M.

## Abstract summary
The creation of structured informational models improves understanding of tunnel behavior throughout its service life and enables faster detection of defects, which is critical for hazard assessment and infrastructure safety. Recent studies highlight the importance of automation and 3D reconstruction in overcoming the limitations of manual tunnel inspection and data management. Technologies such as Point Cloud Data (PCD) and advanced modeling techniques have enhanced inspection processes and model generation. However, significant challenges persist in the development of Digital Twins (DT), particularly in the integration of heterogeneous data sources. This paper presents a methodology that combines parametric modeling technics with field data to develop an automated procedural modeling framework for tunnel inspection Digital Twins that integrates heterogeneous data and optimizes lifecycl…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** Automated procedural modeling for tunnel inspection DT; defect detection

## Step-3 Deep-Read Coding (Prompt B)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 1 - Digital Model (static, no live data) | 0 | 0 | 1 | Design for Safety (DfS) | None | Other / Mixed | Multi (two or more data types) | Single case study | 4 | Perception / Computer Vision |

**Key evidence (AG):** Automated procedural modeling for tunnel inspection and digital twin development (USP): parametric modeling + field data → automated procedural modeling framework for tunnel inspection DT; PCD from Faro Focus 3D X330 laser scanner; Mesh Decimation Quality (MDQ) index evaluates mesh quality during decimation; procedural inspection grid identifies defects and classifies areas; Coastal Tunnel (Brazil) case study. Static DT for inspection — no live data link, no actuation, no learning loop.


**Strength & gap filled (AH):** Automates tunnel inspection digital twin creation from heterogeneous field data: point clouds from a Faro Focus 3D X330 scan of the Coastal Tunnel are cleaned and decimated, meshed by Poisson reconstruction in Grasshopper, with the new MDQ index guiding mesh quality, and metadata attached via EleFront; digital inspection took about 18 minutes versus 46 minutes manual and located a leakage the visual survey missed.

**Deficiencies & future work (AI):** The model is static with no real-time synchronization, digital inspection missed fine shrinkage cracks, portal overexposure prevents accurate color extraction, internet access is required for server connection, and point cloud density depends on scanning equipment; the authors plan additional information layers and UAV or ROV LiDAR acquisition for hard-to-reach tunnels.
**Fusion depth (AC1):** SINGLE

**Fusion evidence (AC2):**
- **Data streams:** laser-scanned point clouds (Faro Focus 3D X330, Coastal Tunnel) with photographic colour only as texture.
- **Integration mechanism:** none across data types - cleaning, decimation, Poisson reconstruction, MDQ-indexed meshing and the procedural inspection grid all operate on the point cloud.
- **Why this code:** one measured data type, so SINGLE. Note: column AC lists Multi because modelling stages were counted; under the fusion-depth rules model-generation steps are not distinct data types.

**Confidence (AC3):** High - the single PCD source is explicit in the full text.
(full-text source: Endnote)
