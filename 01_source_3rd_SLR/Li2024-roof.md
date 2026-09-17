# Li et al. (2024) — Automated generation and semantic segmentation of roof orthophoto for digital twin -based monitoring of slated roofs

- **ID:** 3661 | **Source:** Scopus | **DOI:** 10.1016/j.autcon.2024.105725
- **Journal:** Automation in Construction
- **Authors:** Li, J.; Tao, B.; Bosché, F.; Lu, C. X.; Wilson, L.

## Abstract summary
Roofs are one of the building elements most exposed to environment-induced deterioration, and their deterioration can rapidly result in potential safety hazards to occupants or even buildings’ failure. In pursuit of cost-effective, efficient and pro-active building roof monitoring, this paper presents a computing pipeline for: 1. Automated roof orthophoto generation that uses as input the 3D reconstruction from structure-from-motion photogrammetry and the building's Digital Twin (DT) model, and outputs occlusion-free panel orthophotos with metric resolution. 2. Automated orthophoto semantic segmentation using deep learning to extract visible roof sub-components from the orthophotos. Various segmentation models are tested and contrasted. The approaches are validated with three real case studies of traditional buildings with slated pitched roofs. The proposed approach employs a generic pip…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** DT-based roof monitoring; orthophoto + segmentation; deterioration hazards

## Step-3 Deep-Read Coding (Prompt B) — full text verified via Endnote library (front-matter DOI/title match, coverage re-scan 2026-08-12)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 1 - Digital Model | 0 | 0 | 1 | Design for Quality (DfQ) | None | Perception / Computer Vision | Multi (two or more data types) | Cross-project (multiple real projects) | 4 | Perception / Computer Vision |

**Key evidence (AG):** DT-based monitoring pipeline for slated pitched roofs (University of Edinburgh / Historic Environment Scotland): (1) automated occlusion-free roof-panel orthophoto generation from SfM photogrammetry + the building DT/BIM model; (2) deep-learning semantic segmentation of orthophotos into slates/leadwork/other (PointRend+Focal Loss best, background corrected to 100%); validated on 3 real traditional buildings (Duff House, St Mary's Church, ...). Outputs are semantically linked to DT/digital logbook elements for future defect detection and epoch comparison; processing pipeline is static/offline — no live data link and no learning loop.

**Strength & gap filled (AH):** Fills the gap of automated condition monitoring for pitched slated roofs, for which no prior orthophoto or segmentation work existed: a pipeline generating occlusion-free metric panel orthophotos from SfM reconstruction plus the building DT model, then deep-learning semantic segmentation into slate, leadwork and other, with PointRend plus background label correction reaching 94.22 mIoU and 100 percent background accuracy, validated on Duff House, St Marys Church and a Stirling house.

**Deficiencies & future work (AI):** Stage C defect detection is not implemented; segmentation still confuses leadwork and other classes, generalization drops sharply on unseen buildings, and occlusions such as chimneys can survive the median merging as shadows. Future work covers more roof data, SAM-based segmentation, defect detection in the semantic segments, and populating and maintaining the roof digital logbook.

**Fusion depth (AC1):** Fused

**Fusion evidence (AC2):**
- **Data streams:** SfM reconstruction imagery + building DT/BIM model geometry.
- **Integration mechanism:** orthophoto generation projects imagery onto the model geometry, so the output depends on both simultaneously; PointRend segmentation reaches 94.22 mIoU on Duff House, St Marys Church and a Stirling house.
- **Why this code:** the orthophoto is a joint product of imagery and model geometry, so Fused.

**Confidence (AC3):** Medium - the projection mechanism is clear, though one could argue the streams are merely registered (Aligned); Fused retained because the orthophoto output itself is the joint computation.