# Han et al. (2025) — Enhancing worker monitoring and management on large-scale construction sites with UAVs and digital twin modeling

- **ID:** 3959 | **Source:** Web of Science | **DOI:** 10.1016/j.autcon.2025.106108
- **Journal:** AUTOMATION IN CONSTRUCTION
- **Authors:** Han, M. Q.; Zhang, J. H.; Huang, Y. J.; Xu, J. W.; Chen, X.; Chen, B. M.

## Abstract summary
Monitoring large-scale work sites is challenging, particularly in vast outdoor areas. Unmanned aerial vehicles (UAVs) provide an effective solution for site monitoring and worker management. This paper introduces a UAV-based framework integrated with digital twin (DT) modeling to enhance real-time data management and worker authorization verification. The pretrained YOLO-LCA model improved detection accuracy from 31.5% to 96.4%. The framework combines multi-object tracking with 3D site reconstruction, enabling precise global registration and situational awareness. Cross-referencing UAV detections with GPS-enabled worker IDs ensures that only authorized personnel are present, effectively identifying unapproved workers. The proposed framework has undergone large-scale validation across multiple construction projects in Hong Kong, demonstrating significant potential for modernizing work sit…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** UAV+DT worker monitoring & authorization; operational safety

## Step-3 Deep-Read Coding (Prompt B)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow (one-way physical to virtual) | 0 | 1 | 0 | Design for Safety (DfS) | Implemented | Perception / Computer Vision | Multi (two or more data types) | Single case study | 4 | Design for Safety |

**Key evidence (AG):** UAV-based framework for worker monitoring and management on large-scale construction sites (CUHK): pretrained YOLO-LCA model (detection accuracy improved 31.5%→96.4%) + multi-object tracking + 3D site reconstruction for precise global registration and situational awareness; cross-referencing UAV detections with GPS-enabled worker IDs for authorization verification; large-scale validation across multiple construction projects in Hong Kong; continuous UAV data collection enables iterative model retraining, improving detection robustness. One-way monitoring→authorization verification→decision support; implemented retraining loop but no convergence criterion.


**Strength & gap filled (AH):** Addresses the lack of real-time worker authorization verification in large open construction sites: a UAV digital twin framework at CUHK combining YOLOv10-LCA detection (mAP50 raised from 31.5 to 96.4 percent, 3 ms inference), DeepSORT tracking, georegistered 3D site reconstruction and GPS electronic work permits, validated across Hong Kong construction projects with 19 inspection sites routed by 3D-TSP within a 41-minute flight limit.

**Deficiencies & future work (AI):** The system relies on a single UAV constrained by battery endurance, and its detector drops to 41.5 to 47.1 percent mAP50 on public UAV datasets, so generalization remains limited; future work includes multi-UAV cooperation, resilience in adverse weather and low light, extra sensors such as infrared and LiDAR, and broader training datasets.
**Fusion depth (AC1):** Fused

**Fusion evidence (AC2):**
- **Data streams:** YOLOv10-LCA UAV detections (mAP50 31.5 to 96.4%) + DeepSORT tracks + GPS-enabled electronic work permits + georegistered 3D reconstruction.
- **Integration mechanism:** cross-referencing UAV detections with GPS-enabled worker IDs produces the authorisation-verification decision, joining two data types; 3D-TSP routes inspections across 19 Hong Kong sites.
- **Why this code:** the verification output depends on two data types simultaneously, so Fused; implemented and field-validated.

**Confidence (AC3):** High - the cross-referencing mechanism is explicitly described.
(full-text source: Endnote)
