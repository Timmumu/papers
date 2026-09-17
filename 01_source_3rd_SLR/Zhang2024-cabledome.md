# Zhang et al. (2024) — Joint detection PCD-based method for automatic construction of geometric digital twin in cable dome structure

- **ID:** 3934 | **Source:** Web of Science | **DOI:** 10.1016/j.engstruct.2024.118908
- **Journal:** ENGINEERING STRUCTURES
- **Authors:** Zhang, A. L.; Wang, J.; Zhang, Y. X.; Shangguan, G. H.

## Abstract summary
The geometric digitization of cable dome structures using Point Cloud Datasets (PCD) holds significant importance as it serves as a foundational step in constructing the Digital Twin of such structures. However, accurately detecting the positions of structural joints for effective construction of a geometric digital twin from PCD remains a challenging task. To address this issue, we propose an enhanced algorithm and system solution for joint detection based on target recognition. The method leverages a novel shape estimation model to identify structural components by randomly sampling the minimum set of points from the point cloud. Subsequently, connection joints and their coordinates are determined according to the spatial relationships of the components. This enables the digital reconstruction of the structure based on the topological relationships of the joints, ultimately facilitatin…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** PCD joint detection for geometric DT of cable domes; safety/stability

## Step-3 Deep-Read Coding (Prompt B)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 1 - Digital Model (static, no live data) | 0 | 1 | 0 | Design for Safety (DfS) | None | Perception / Computer Vision | Single (one data type) | Single case study | 4 | Perception / Computer Vision |

**Key evidence (AG):** Joint-detection PCD-based method for automatic construction of geometric digital twin (DS-gDT) in cable dome structures (Beijing U Civil Eng): enhanced target-recognition algorithm with novel shape-estimation model samples minimum point sets to identify structural components; joints determined by component spatial relationships for topological reconstruction of the gDT; validated on scaled cable dome PCD (component segmentation success ~51.5% higher than traditional methods; joint fitting accuracy >99%); enables joint-deviation assessment. Static geometric DT - no live data link, no learning loop.


**Strength & gap filled (AH):** Fills the gap of an automated geometric digital twin method for cable dome structures: DS-gDT detects joints from point cloud data using a three-point normal cylinder fitting model with radius-constrained sampling and double termination criterion, then rebuilds topology via an adjacency matrix, achieving recognition about 51.5 percent above conventional RANSAC, 20.09 percent efficiency gain and above 99 percent joint-coordinate accuracy on a scaled dome.

**Deficiencies & future work (AI):** Static geometric twin only: DS-gDT cannot monitor component stresses or strains or update joint positions in real time, point cloud processing is time-consuming, and clustering accuracy drops when paired regions lack data. Authors plan to extend the method to suspend-dome and reticulated shell structures, build a mechanical twin and quantify how joint deviations affect structural stability.
**Fusion depth (AC1):** SINGLE

**Fusion evidence (AC2):**
- **Data streams:** scaled cable-dome point clouds.
- **Integration mechanism:** none - three-point normal cylinder fitting with radius-constrained sampling detects components, and the adjacency matrix rebuilds topology (about 51.5% above RANSAC, over 99% joint accuracy).
- **Why this code:** SINGLE (AC=Single).

**Confidence (AC3):** High.
(full-text source: Endnote)
