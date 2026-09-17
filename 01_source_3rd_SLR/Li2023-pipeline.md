# Li et al. (2023) — 3D laser point cloud-based geometric digital twin for condition assessment of large diameter pipelines

- **ID:** 3839 | **Source:** Scopus | **DOI:** 10.1016/j.tust.2023.105430
- **Journal:** Tunnelling and Underground Space Technology
- **Authors:** Li, M.; Feng, X.; Hu, Q.

## Abstract summary
The increasing aging of underground pipe networks and the lack of effective inspection technologies present considerable challenges for whole life-cycle management of these infrastructures. Modern laser scanning technology offers a cost-effective and safe means to obtain dense and accurate 3D topographic data of the inner surface of pipelines. However, laser scanning point clouds contain substantial noise and outliers, and efficiently extracting valuable information for structural and functional mapping remains in its infancy. This paper presents an innovative method for fast processing point clouds data of large-diameter pipelines, enabling the accurate extraction of geometric features and efficient establishment of geometric digital twin using density-based clustering, fitting and region growing algorithm. Experimental tests were conducted to evaluate the accuracy, efficiency, and feas…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** Geometric DT for pipeline deformation/blockage defect assessment

## Step-3 Deep-Read Coding (Prompt B)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 1 - Digital Model (static, no live data) | 0 | 0 | 1 | Design for Safety (DfS) | None | Other / Mixed | Multi (two or more data types) | Single case study | 4 | Perception / Computer Vision |

**Key evidence (AG):** Geometric digital twin for condition assessment of large-diameter pipelines (Dalian U/Tongji): laser scanning point clouds → density-based clustering + fitting + region growing algorithm → accurate 3D surface mapping; geometric DT enables quantitative assessment of structural deformation (mean error <1 mm) and blockage defects; validated experimentally vs total station. Static DT for condition assessment — no live data link, no actuation, no learning loop.


**Strength & gap filled (AH):** Turns noisy laser point clouds of large-diameter pipelines into a geometric digital twin enabling quantitative condition assessment, closing the gap between raw scanning and deformation measurement: LMedS slice-center fitting, DBSCAN clustering with Gaussian fitting and density-based region growing achieve sub-millimeter mean error against total station truth, with ovality and blockage quantified via OI and VI indicators at only 7 percent of KDE runtime.

**Deficiencies & future work (AI):** Validation is limited to laboratory plexiglass pipe segments rather than in-service networks; the method cannot measure the underwater part of pipes and does not suit bends with curved axes. Future work includes fusing 3D sonar data, AI-based assessment of spalling, corrosion and open joints, and an in-pipe inspection robot to carry the laser scanner.
**Fusion depth (AC1):** SINGLE

**Fusion evidence (AC2):**
- **Data streams:** laser-scanned point clouds (FARO Focus-3D); twelve Leica total-station target points used only to benchmark accuracy; image-based methods appear solely in the related-work discussion.
- **Integration mechanism:** none - the pipeline (density-based clustering, fitting, region growing) processes one data type; mean error under 1 mm versus total station.
- **Why this code:** exactly one measured data type is used, so SINGLE. Note: column AC lists Multi because the total-station validation was counted there; under the fusion-depth rules a validation benchmark is not a second data type.

**Confidence (AC3):** High - the single-modality pipeline and validation-only role of the total station are explicit in the full text.
(full-text source: Endnote)
