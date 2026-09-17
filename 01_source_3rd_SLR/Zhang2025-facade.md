# Zhang et al. (2025) — AI-empowered digital twin modeling for high-precision building defect management integrating UAV and GeoBIM

- **ID:** 3968 | **Source:** Web of Science | **DOI:** 10.1007/s12273-025-1332-9
- **Journal:** BUILDING SIMULATION
- **Authors:** Zhang, J. H.; Zhao, B. Y.; Yang, G. D.; Zhou, X. K.; Huang, Y. J.; Gao, C. X.; Chen, X.; Chen, B. M.

## Abstract summary
Recent advances in artificial intelligence (AI) and cyber-physical systems have fostered innovative approaches to performance assessment and management of existing building stock. This study presents an AI-assisted digital twin (DT) framework for the automated and high-precision detection of fa & ccedil;ade defects in large-scale buildings. Leveraging unmanned aerial vehicles (UAVs) for visual data acquisition, the proposed framework integrates building information modeling (BIM) and geographic information systems (GIS) into a GeoBIM-assisted DT environment. An end-to-end pipeline is developed for defect localization and semantic registration, in which a virtual building model and camera geometry are constructed using geographic metadata. Synthetic views are generated to simulate real image capture conditions, enabling depth-based inference of each defect's spatial location. This facilit…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** AI+UAV+GeoBIM DT for facade defect management; building health

## Step-3 Deep-Read Coding (Prompt B) — full text verified via Endnote library (front-matter DOI/title match, coverage re-scan 2026-08-12)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow | 0 | 0 | 1 | Design for Quality (DfQ) | None | Perception / Computer Vision | Multi (two or more data types) | Single case study | 4 | Perception / Computer Vision |

**Key evidence (AG):** AI-empowered digital twin framework for high-precision building facade defect management (CUHK): UAV visual data acquisition + deep-learning object detection (YOLO/R-CNN series) for defect detection; GeoBIM (BIM+GIS) environment with end-to-end pipeline for defect localization and semantic registration — virtual building model + camera geometry from geographic metadata, synthetic views simulate capture conditions, depth-based inference of each defect's spatial location, dual-verification (image + geographic features) removes duplicates; defect data projected into georeferenced DT with structural context from GeoBIM; validated on a Hong Kong high-rise. One-way inspection→semantic DT for maintenance; no actuation and no self-improvement loop.

**Strength & gap filled (AH):** Fills the gap of precise 2D-to-3D defect localization with semantic enrichment: a GeoBIM-assisted digital twin registers UAV-detected facade defects onto georeferenced BIM models through SfM pose correction and virtual camera depth rendering, achieving centimeter-level accuracy (mean errors 0.49-1.36 cm versus 1-3 meters for GPS-based methods) and over 80 percent mAP0.5 detection at 30 FPS on a Hong Kong high-rise, including curved and heritage facades.

**Deficiencies & future work (AI):** Operates near real time without continuous streaming or IoT data links, needs substantial computation and memory, and accuracy degrades under extreme occlusion or reflective surfaces. Authors plan to support diverse BIM standards and city-scale asset portfolios, integrate IoT live monitoring and automated UAV deployment, and enrich semantic defect reporting for maintenance scheduling.

**Fusion depth (AC1):** Fused

**Fusion evidence (AC2):**
- **Data streams:** UAV imagery with YOLO/R-CNN detections + GeoBIM (BIM+GIS) model geometry (Hong Kong high-rise).
- **Integration mechanism:** virtual cameras render depth from the GeoBIM, and SfM-corrected poses project detections into the georeferenced twin with dual verification (image + geographic features), reaching 0.49-1.36 cm mean localisation error.
- **Why this code:** localisation output depends on imagery and model geometry simultaneously, so Fused.

**Confidence (AC3):** High - the virtual-camera depth pipeline is explicit.