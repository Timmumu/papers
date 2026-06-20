---
ref: "[92]"
citekey: "Pereira2025"
title: "BIM for Safety: Applying Real-Time Monitoring Technologies to Prevent Falls from Height in Construction"
authors: "F. Pereira, M. de las Nieves González García, J. Poças Martins"
year: 2025
journal: "Applied Sciences"
volume: "15"
issue: "4"
article: "2218"
doi: "10.3390/app15042218"
zotero_key: "EWGI4UA4"
zotero_status: verified
created: "2026-05-31"
tags:
  - BIM
  - Safety
  - Falls-from-Height
  - Real-time-Monitoring
  - Computer-Vision
  - PRISMA
  - Verified
  - source: scholar
  - identification: other methods
---

# Pereira2025

| Field | Value |
|-------|-------|
| **Ref** | [92] |
| **Title** | BIM for Safety: Applying Real-Time Monitoring Technologies to Prevent Falls from Height in Construction |
| **Authors** | F. Pereira, M. de las Nieves González García, J. Poças Martins |
| **Venue** | Applied Sciences, vol. 15, no. 4, Art. no. 2218, 2025 |
| **DOI** | 10.3390/app15042218 |
| **Zotero** | EWGI4UA4 (verified, full text PDF, 19 pp.) |

## Abstract
^sec-abstract

> There are significant risks in the construction sector, with falls from height identified as a greater hazard than in most other industries. Efforts to improve working conditions and reduce accident rates have driven research into real-time monitoring technologies to reduce the risk of falls. The main objective of this research is to review existing real-time monitoring technologies, identify the most relevant, and analyse their benefits and impact on reducing workplace accidents in the construction sector. A systematic review was conducted using PRISMA methodology to investigate the use of real-time monitoring technologies in the construction industry. Only studies specifically investigating real-time fall risk assessment were included. Of the initial 446 articles reviewed, 39 were considered highly relevant. Various wireless and computer vision technologies were identified for real-time worker monitoring, often integrated with BIM to improve workplace safety. The findings suggest that a combination of technologies may produce more effective results for worker monitoring; however, further research is needed to verify the applicability of these technologies on construction sites.

## Core Claims
^sec-claims

- ① Falls from height are the leading cause of fatal construction accidents and remain unsolved despite decades of safety regulation.
- ② Real-time monitoring technologies (wireless sensing, RFID/UWB tags, wearable IMUs, and computer-vision) are converging with BIM platforms to enable proactive fall-risk assessment.
- ③ A **combination** of technologies (sensor fusion + CV + BIM context) consistently outperforms any single modality but raises integration, calibration, and privacy challenges.
- ④ Few systems are validated on real, occlusion-rich construction sites — most evidence stems from controlled lab or pilot conditions.

## Method
- PRISMA-driven systematic review.
- 446 candidate articles screened → 39 included (specifically real-time fall-risk assessment).
- Inclusion limited to peer-reviewed studies investigating BIM-integrated or BIM-adjacent real-time fall monitoring.

## Relevance to Cognitive DT (LR_cc.md Sec 3.2)
- Provides empirical support for the **Perception, registration & computer vision** thematic cluster (n=12) in [Table 2](LR_cc.md).
- Documents the Level-1/Level-2 maturity gap: most reviewed systems *detect & visualize* falls but do not autonomously revise safety rules → reinforces LR_cc.md's argument that current DT-for-Safety stays at ML2.

## Limitations Noted
- Heterogeneous evaluation metrics across the 39 studies prevent meta-analysis.
- Site-scale validation is rare; lab-to-field generalization gap.
- Privacy and worker-acceptance concerns are largely unaddressed.

## Traceability

| LR_cc.md | Claim | Evidence Block |
|----------|-------|----------------|
| Table 2 (Perception cluster) | Sensor + CV + BIM integration for safety | #^sec-abstract |
| Sec 3.4 | Hazard detection at Level-2 maturity | #^sec-claims |
