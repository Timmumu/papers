# Pan et al. (2022) — Enriching geometric digital twins of buildings with small objects by fusing laser scanning and AI-based image recognition

- **ID:** 3989 | **Source:** Web of Science | **DOI:** 10.1016/j.autcon.2022.104375
- **Journal:** AUTOMATION IN CONSTRUCTION
- **Authors:** Pan, Y. D.; Braun, A.; Brilakis, I.

## Abstract summary
This paper addresses the challenge of enriching geometric digital twins of buildings, with a particular emphasis on capturing small but important entities from the electrical and the fire-safety domain, such as signs, sockets, switches, smoke alarms, etc. Unlike most previous research that focussed on structural elements and processed laser point clouds and images separately, we propose a novel method that fuses laser scanning and photogrammetry methods to capture the relevant objects, recognise them in 2D images and then map these to a 3D space. The considered object classes include electrical elements (light switch, light, speaker, socket, elevator button), safety elements (emergency switch, smoke alarm, fire extinguisher, escape sign), plumbing system elements (pipes), and other objects with useful information (door sign, board). Semantic information like class labels is extracted by …

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** Enriching geometric DTs with fire-safety objects; condition monitoring

## Step-3 Deep-Read Coding (Prompt B)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 1 - Digital Model (static, no live data) | 0 | 0 | 1 | Design for Safety (DfS) | None | Perception / Computer Vision | Multi (two or more data types) | Single case study | 4 | Perception / Computer Vision |

**Key evidence (AG):** Enriching geometric digital twins of buildings with small objects (TUM/Cambridge): fuses laser scanning + photogrammetry; AI-based image segmentation (deep learning) detects small objects (electrical, fire-safety, plumbing); AI-based text detection/recognition extracts object IDs; semantic info mapped to 3D point cloud → enriched DT with geometric + semantic + text info; comprehensive case study. Static DT for facility management — no live data link, no actuation, no learning loop.


**Strength & gap filled (AH):** Fills the gap of enriching geometric building twins with electrical and fire-safety objects that prior scan-to-BIM methods ignored: a mostly automated pipeline fusing laser scanning and photogrammetry, with Mask-RCNN detections mapped into point clouds via COLMAP, ICP alignment and voxel raycasting, then RANSAC shape fitting and OCR text extraction, raising mIoU for smoke alarms from 29.1% to 48.6% and lights from 69.4% to 79.9% versus KPConv.

**Deficiencies & future work (AI):** Validation is limited to TUM office interiors with a manually labelled dataset; detection is weaker for objects that vary across buildings and many classes like furniture remain missing; only simple geometric primitives are fitted, point-cloud registration stays manual, and the photogrammetric step needs enough overlapping images. Future work adds more classes, CAD-level shapes, and joint 2D and 3D deep learning.
**Fusion depth (AC1):** Fused

**Fusion evidence (AC2):**
- **Data streams:** laser-scanned point clouds + photogrammetric imagery + OCR-extracted object IDs.
- **Integration mechanism:** detections are projected into the point cloud through COLMAP pose estimation, ICP alignment and voxel raycasting, then fitted with RANSAC shapes and OCR text (smoke-alarm mIoU 29.1 to 48.6%; lights 69.4 to 79.9% versus KPConv).
- **Why this code:** 2D detections and 3D geometry are combined into one joint representation, so Fused.

**Confidence (AC3):** High - the projection/raycasting fusion chain is explicit.
(full-text source: Endnote)
