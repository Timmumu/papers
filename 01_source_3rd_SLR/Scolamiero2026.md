# Scolamiero et al. (2026) — A BIM-Based Digital Twin Framework for Urban Roads: Integrating MMS and Municipal Geospatial Data for AI-Ready Urban Infrastructure Management

- **ID:** 3713 | **Source:** Scopus | **DOI:** 10.3390/s26030947
- **Journal:** Sensors
- **Authors:** Scolamiero, V.; Boccardo, P.

## Abstract summary
Digital twins (DTs) are increasingly adopted to enhance the monitoring, management, and planning of urban infrastructure. While DT development for buildings is well established, applications to urban road networks remain limited, particularly in integrating heterogeneous geospatial datasets into semantically rich, multi-scale representations. This study presents a methodology for developing a BIM-based DT of urban roads by integrating geospatial data from Mobile Mapping System (MMS) surveys with semantic information from municipal geodatabases. The approach follows a multi-modal (point clouds, imagery, vector data), multi-scale and multi-level framework, where ‘multi-level’ refers to modeling at different scopes—from a city-wide level, offering a generalized representation of the entire road network, to asset-level detail, capturing parametric BIM elements for individual road segments or…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** BIM-based DT of urban roads; defect detection & predictive maintenance

## Step-3 Deep-Read Coding (Prompt B)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 1 - Digital Model (static, no live data) | 0 | 0 | 1 | Design for Safety (DfS) | None | Digital Twin platform (no machine learning) | Multi (two or more data types) | Cross-project (multiple real projects) | 4 | BIM-to-Digital-Twin architecture |

**Key evidence (AG):** BIM-based DT framework for urban roads (Sapienza/Politecnico di Torino): integrates MMS-derived LiDAR point clouds with municipal GIS layers and authoritative geodatabases; multi-scale workflow (city-wide LoD200 to asset-level LoD400) with IFC 4.3 semantic enrichment; geometric accuracy ±3 cm; integrates 45+ km of urban road network; supports multi-scale visualization, asset management, and predictive maintenance. Static DT — no live data link, no actuation, no learning loop (sensor-integrated updates are future work).


**Strength & gap filled (AH):** Delivers a BIM-based digital twin framework for urban roads in Turin integrating MMS LiDAR point clouds, municipal GIS layers and authoritative geodatabases into IFC 4.3 models at LoD200 (city scale) and LoD400 (asset scale), covering about 45 km of network with over 2000 vertical elements and achieving RMSE 3 cm geometric accuracy validated by cloud-to-mesh deviation analysis, creating AI-ready, semantically enriched datasets for maintenance planning.

**Deficiencies & future work (AI):** The twin is a static information model without real-time IoT ingestion, bidirectional communication or automated updates, relying on periodic surveys and semi-automated processing with manual intervention; behavioral and performance indicators are absent and only one urban area was tested, with data governance and privacy unresolved. Future work covers sensor integration, deep learning automation and city-wide scaling.
**Fusion depth (AC1):** Fused

**Fusion evidence (AC2):**
- **Data streams:** MMS LiDAR point clouds + municipal GIS layers + authoritative geodatabases.
- **Integration mechanism:** the multi-scale workflow merges the sources into one semantically enriched IFC model validated by cloud-to-mesh deviation analysis (RMSE 3 cm).
- **Why this code:** the IFC model is a joint product of several data sources, so Fused; static (no live ingestion), hence Medium.

**Confidence (AC3):** Medium - the integration workflow is explicit; no live data link exists.
(full-text source: Endnote)
