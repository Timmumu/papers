# Gao et al. (2024) — Bridge Digital Twin for Practical Bridge Operation and Maintenance by Integrating GIS and BIM

- **ID:** 3876 | **Source:** Web of Science | **DOI:** 10.3390/buildings14123731
- **Journal:** BUILDINGS
- **Authors:** Gao, Y.; Xiong, G. Y.; Hu, Z. Y.; Chai, C. Z.; Li, H. J.

## Abstract summary
As an emerging technology, digital twin (DT) is increasingly valued in bridge management for its potential to optimize asset operation and maintenance (O&M). However, traditional bridge management systems (BMS) and existing DT applications typically rely on standalone building information modeling (BIM) or geographic information system (GIS) platforms, with limited integration between BIM and GIS or consideration for their underlying graph structures. This study addresses these limitations by developing an integrated DT system that combines WebGIS, WebBIM, and graph algorithms within a three-layer architecture. The system design includes a common data environment (CDE) to address cross-platform compatibility, enabling real-time monitoring, drone-enabled inspection, maintenance planning, traffic diversion, and logistics optimization. Additionally, it features an adaptive data structure in…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** Integrated WebGIS+WebBIM DT; defect modeling, maintenance, safety

## Step-3 Deep-Read Coding (Prompt B)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow (one-way physical to virtual) | 0 | 0 | 1 | Design for Safety (DfS) | None | Digital Twin platform (no machine learning) | Multi (two or more data types) | Single case study | 4 | Lifecycle / governance |

**Key evidence (AG):** Integrated bridge DT system (Cardiff U): combines WebGIS (Cesium), WebBIM (Xeokit), and graph algorithms (Neo4j) in a three-layer architecture with a common data environment (CDE); enables real-time monitoring, drone-enabled inspection, maintenance planning, traffic diversion, and logistics optimization; adaptive data structure with JSON-based bridge defect information modeling and triple-based roadmap graphs; SHM system flags structural issues and triggers alerts/traffic redirection; defects from drone inspection inform maintenance planning. One-way monitoring→analysis→decision support; no actuation and no learning loop.
(full-text source: Endnote)
