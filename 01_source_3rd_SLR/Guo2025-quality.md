# Guo et al. (2025) — A methodology for sky-space-ground integrated remote sensing monitoring: A digital twin framework for multi-source Data-BIM integration in residential quality monitoring

- **ID:** 3924 | **Source:** Web of Science | **DOI:** 10.1016/j.jobe.2025.111976
- **Journal:** JOURNAL OF BUILDING ENGINEERING
- **Authors:** Guo, M.; Wu, X. L.; Qi, H. H.; Zhang, Y.; Chen, J. J. H.; Wei, Y. X.; Zhang, X. L.; Shang, X. K.

## Abstract summary
This study introduces an innovative data-BIM integrated digital twin framework for the quality monitoring residential developments. The framework amalgamates residential building information modeling (RBIM), surveying sensors and Internet of Things (SSIoT) technologies to establish a multi-faceted and multi-scale monitoring system. Within this framework, RBIM serves as a residential information twin model that aggregates comprehensive life cycle data of residential projects, encompassing design, building, operation, and maintenance. The physical things are linked to cyberspace via SSIoT technology, significantly improving data exchange and processing capabilities. To address the limitations of singular monitoring technology, a BIM collaborative multi-source data monitoring method for residential engineering quality is proposed, utilizing the BIM model alongside the advancement of real-ti…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** Data-BIM DT framework for residential quality monitoring

## Step-3 Deep-Read Coding (Prompt B)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow (one-way physical to virtual) | 0 | 0 | 1 | Design for Quality (DfQ) | None | Digital Twin platform (no machine learning) | Multi (two or more data types) | Single case study | 4 | BIM-to-Digital-Twin architecture |

**Key evidence (AG):** Sky-space-ground integrated remote sensing monitoring DT framework for multi-source Data-BIM integration in residential quality monitoring (Beijing U Civil Eng & Arch, J Building Eng 2025): RBIM (residential building information model) aggregates full-lifecycle project data; SSIoT (surveying sensors + IoT) links physical things to cyberspace; multi-sensor monitoring (monitoring LiDAR, automated monitoring robots, GNSS, drones) with BIM collaborative multi-source data fusion; cloud platform unifies data processing/storage avoiding information islands; experiments: 8-phase LiDAR monitoring of a frame building tracking target-sphere centre displacement to assess building deformation trends, accuracy verification of self-developed LSIIS centre-extraction algorithm vs PCL/ICP/WTLS (Faro + Livox LiDAR), building settlement monitoring analysis with BIM-sensor linkage. One-way monitoring to DT platform for O&M quality management; no actuation, no learning loop.



**Strength & gap filled (AH):** Proposes a sky-space-ground digital twin framework fusing RBIM with SSIoT multi-source sensing, including real-time LiDAR, automated monitoring robots, GNSS and SBAS-InSAR settlement data, linked through GUID object mapping tables and a cloud platform with weighted-average fusion and conflict detection, achieving consistent millimeter and sub-millimeter settlement precision across monitoring points.

**Deficiencies & future work (AI):** The system is limited to integrating and visually presenting multi-source data; heterogeneous format standardization between BIM and point clouds remains a major challenge, and prediction or assessment is absent. Future research will add advanced data analytics and machine learning to predict maintenance needs and potential problems from historical and real-time data.
**Fusion depth (AC1):** Fused

**Fusion evidence (AC2):**
- **Data streams:** real-time LiDAR, automated monitoring robots, GNSS, SBAS-InSAR settlement data, 8-phase LiDAR frame-building monitoring.
- **Integration mechanism:** GUID object mapping tables link physical things to RBIM, and the cloud platform applies weighted-average fusion with conflict detection, achieving consistent millimetre/sub-millimetre settlement precision across monitoring points.
- **Why this code:** named fusion algorithms (weighted average + conflict detection) combine multiple data types into one settlement estimate, so Fused; implemented and demonstrated.

**Confidence (AC3):** High - the GUID mapping tables and weighted-average fusion are explicit in the full text.
(full-text source: Endnote)
