# Song, C et al. (2026) — Simultaneous Digital Twin: Chaining Climbing-Robot, Defect Segmentation, and Model Updating for Building Facade Inspection

- **ID:** R381 | **Source:** Scopus | **DOI:** 10.3390/buildings16030646
- **Journal:** Buildings
- **Authors:** Song C.; Lu C.; Shi Y.; He A.; Lin J.; Ma Z.

## Abstract summary
The rapid deterioration of building facades presents substantial safety hazards in urban environments, necessitating advanced, automated inspection solutions. While computer vision (CV) and deep learning (DL) techniques have shown promise for defect analysis, critical gaps remain in achieving real-time, quantitative, and generalizable damage assessment suitable for robotic deployment. Current methods often lack precise metric quantification, struggle with diverse material appearances, and are computationally intensive for on-site processing. To address these limitations, this paper introduces a fully automated, end-to-end inspection framework integrating a wall-climbing robot, a real-time vision-based analysis system, and a digital twin management platform. The primary contributions are threefold: (1) a novel, fully integrated robotic framework for autonomous navigation, multi-sensor dat…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** Climbing-robot facade inspection with real-time DT platform


## Step-3 Deep-Read Coding (Prompt B)
| P DT-subject | Q DfS/DfQ | R codable | U Tier | V Design | W Constr | X Oper | Z DfX | AA Self-improve | AB Methodology | AC Modality | AD Validation | AE QA(0-5) | AF Cluster |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow (one-way physical to virtual) | 0 | 1 | 0 | Design for Safety (DfS) | None | Perception / Computer Vision | Multi (two or more data types) | Single case study | 4 | Perception / Computer Vision |

| AC1 fusion depth | AC2 fusion evidence | AC3 confidence |
|---|---|---|
| Fused | RGB camera imagery, RTK-GNSS and IMU localisation are combined so skeletonization and PCA can convert segmentations into metric crack length and centre measurements on the building facade. | Medium |

**Key evidence (AG):** Simultaneous digital twin framework for building facade inspection (Tsinghua U): wall-climbing robot (negative pressure adhesion) with RGB camera + penetrating sensors; real-time vision-based defect segmentation (mAP 0.775) and metric quantification (length error 1.140 cm, center error 0.826 cm); cloud-based DT platform for quantitative defect visualization, spatiotemporal traceability, and data-driven project management; on-site inspection cycle latency 2.8-4.8s; validated on real building projects. One-way monitoring→DT→decision support; no actuation and no learning loop.

*Full-text source: 04c-port*

**AH — strength & gap filled:** Addresses the gap between robotic facade inspection and quantitative, real-time damage assessment: a negative-pressure wall-climbing robot with RTK-GNSS and IMU localization feeds a lightweight YOLO12 segmentation model (0.775 mAP) whose skeletonization and PCA quantification reach 1.140 cm length error and 0.826 cm center error, all mapped into a cloud digital twin with 2.8-4.8 s response cycles on a Tongzhou Beijing building.

**AI — deficiencies & future work:** The adhesion mechanism cannot handle highly rough surfaces and only surface cracks and spalling are analyzed, leaving UWB radar and infrared subsurface data unused; validation is limited to laboratory specimens and one residential building, and future work targets robot hardware adaptation to complex facades plus subsurface defect characterization through multi-modal cross-validation.
