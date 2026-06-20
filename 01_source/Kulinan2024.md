---
ref: "[93]"
citekey: "Kulinan2024"
title: "Advancing construction site workforce safety monitoring through BIM and computer vision integration"
authors: "A. S. Kulinan, M. Park, P. P. W. Aung, G. Cha, S. Park"
year: 2024
journal: "Automation in Construction"
volume: "158"
article: "105227"
doi: "10.1016/j.autcon.2023.105227"
zotero_key: "P52VFZEH"
zotero_status: verified
created: "2026-05-31"
tags:
  - BIM
  - Computer-Vision
  - Safety
  - Workforce-Monitoring
  - Deep-Learning
  - Verified
  - source: scholar
---

# Kulinan2024

| Field | Value |
|-------|-------|
| **Ref** | [93] |
| **Title** | Advancing construction site workforce safety monitoring through BIM and computer vision integration |
| **Authors** | A. S. Kulinan, M. Park, P. P. W. Aung, G. Cha, S. Park |
| **Venue** | Automation in Construction, vol. 158, Art. no. 105227, Feb. 2024 |
| **DOI** | 10.1016/j.autcon.2023.105227 |
| **Zotero** | P52VFZEH (verified, full text PDF) |

## Abstract
^sec-abstract

> Workforce safety remains a primary concern on construction sites, where workers face hazards from equipment, falls, and confined-space operations. This study reviews and synthesizes how the integration of Building Information Modeling (BIM) and computer vision (CV) can advance real-time workforce safety monitoring. The authors map state-of-the-art CV pipelines (object detection, pose estimation, tracking) onto BIM-anchored spatial contexts to identify hazardous worker–environment interactions. They classify approaches by sensing modality (RGB, RGB-D, thermal), DL architecture (CNN, Transformer, YOLO family), and BIM coupling strategy (offline registration, online streaming). The review highlights persistent gaps: dataset scarcity for site-specific PPE and posture classes, occlusion robustness, calibration drift between BIM and live video, and an absence of end-to-end uncertainty quantification.

## Core Claims
^sec-claims

- ① Combining **CV-based worker localization** with **BIM-anchored hazard zones** enables spatially-aware risk reasoning unavailable to either modality alone.
- ② Pose-estimation and action-recognition models can flag unsafe behaviours (improper PPE, dangerous postures, proximity to moving equipment) but require curated construction-domain datasets.
- ③ End-to-end calibration between as-built BIM and on-site cameras is the dominant integration bottleneck; most reviewed systems assume static rigid registration.
- ④ Few works expose model confidence to downstream safety logic — a UQ gap relevant to [LR_cc.md Sec 4.3](LR_cc.md).

## Method
- Narrative + structured literature review across 2018–2023.
- Taxonomy along three axes: sensing modality, DL architecture, BIM coupling.

## Relevance to Cognitive DT (LR_cc.md Table 2 Perception cluster)
- Directly supports the **Perception, registration & computer vision (n=12)** cluster in [Table 2](LR_cc.md).
- Confirms the LR_cc.md observation that DT systems remain unidirectional and deterministic (Sec 4.3).

## Limitations Noted
- Sparse public construction-site datasets covering PPE, posture and dynamic hazards.
- BIM-to-video calibration drift over the construction lifecycle is unsolved.
- No explicit uncertainty propagation in reviewed pipelines.

## Traceability

| LR_cc.md | Claim | Evidence Block |
|----------|-------|----------------|
| Table 2 (Perception cluster) | BIM + CV workforce safety monitoring | #^sec-abstract |
| Sec 4.3 (UQ gap) | Lack of confidence exposure in safety CV | #^sec-claims |
