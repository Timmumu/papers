# Lv et al. (2026) — Automating digitalization of engineered slopes to support interactive digital twin visualization

- **ID:** 3894 | **Source:** Web of Science | **DOI:** 10.1016/j.autcon.2025.106564
- **Journal:** AUTOMATION IN CONSTRUCTION
- **Authors:** Lv, Y. H.; Pang, Y. E.; Ju, L. Y.; Xu, W. F.; Liang, Z. Y.; He, J.; Zhang, L. M.

## Abstract summary
Slope safety management is transitioning toward the digital twin paradigm, where digital models serve as a base plate for the development of further applications. This paper presents an automated solution to creating digital models for engineered slope digital twins. Utilizing city-scale point cloud, the proposed approach creates lightweight BIM models of engineered slopes consisting of drainage channels and slope topography. The proposed approach leverages a convolutional neural network (CNN) model, DrainNet, for fine-scale drainage channel delineation in images, an automated parametric modeling pipeline for scalable BIM reconstruction, and a web-based digital twin for interactive visualization. Experiments demonstrate that DrainNet achieves state-ofthe-art 81.26 % Dice with only 0.28 M parameters on a domain-knowledge-incorporated dataset containing 1226 annotated images. The proposed …

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** Automated slope digital models + web DT; slope safety management

## Step-3 Deep-Read Coding (Prompt B)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 1 - Digital Model (static, no live data) | 0 | 0 | 1 | Design for Safety (DfS) | None | Perception / Computer Vision | Multi (two or more data types) | Single case study | 4 | BIM-to-Digital-Twin architecture |

**Key evidence (AG):** Automated digitalization of engineered slopes for interactive digital twin visualization (HKUST): city-scale LiDAR point clouds → DrainNet (CNN, 81.26% Dice) for drainage channel delineation → automated parametric BIM modeling (Grasshopper, 9x faster than Dynamo) → web-based digital twin platform for interactive visualization and asset management. Static BIM models for visualization — no live data link, no actuation, no learning loop.
(full-text source: Endnote)
