# Machado, L.B et al. (2025) — Automated procedural modeling for tunnel inspection and digital twin development

- **ID:** R099 | **Source:** Scopus | **DOI:** 10.1016/j.tust.2025.106929
- **Journal:** Tunnelling and Underground Space Technology
- **Authors:** Machado L.B.; Poncetti B.L.; de Assis L.S.; Futai M.M.

## Abstract summary
The creation of structured informational models improves understanding of tunnel behavior throughout its service life and enables faster detection of defects, which is critical for hazard assessment and infrastructure safety. Recent studies highlight the importance of automation and 3D reconstruction in overcoming the limitations of manual tunnel inspection and data management. Technologies such as Point Cloud Data (PCD) and advanced modeling techniques have enhanced inspection processes and model generation. However, significant challenges persist in the development of Digital Twins (DT), particularly in the integration of heterogeneous data sources. This paper presents a methodology that combines parametric modeling technics with field data to develop an automated procedural modeling framework for tunnel inspection Digital Twins that integrates heterogeneous data and optimizes lifecycl…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** Procedural tunnel inspection DT; defect detection safety

## Step-3 Deep-Read Coding (Prompt B)
| P DT-subject | Q DfS/DfQ | R codable | U Tier | V Design | W Constr | X Oper | Z DfX | AA Self-improve | AB Methodology | AC Modality | AD Validation | AE QA(0-5) | AF Cluster |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 1 - Digital Model (static, no live data) | 0 | 0 | 1 | Design for Safety (DfS) | None | Other / Mixed | Multi (two or more data types) | Single case study | 4 | Perception / Computer Vision |

| AC1 fusion depth | AC2 fusion evidence | AC3 confidence |
|---|---|---|
| SINGLE | Only Faro Focus 3D X330 point-cloud data feed the procedural modelling pipeline; parametric/procedural modelling are model-generation steps, not additional measured data types. | High |

**Key evidence (AG):** Automated procedural modeling for tunnel inspection and digital twin development (USP): parametric modeling + field data → automated procedural modeling framework for tunnel inspection DT; PCD from Faro Focus 3D X330 laser scanner; Mesh Decimation Quality (MDQ) index evaluates mesh quality during decimation; procedural inspection grid identifies defects and classifies areas; Coastal Tunnel (Brazil) case study. Static DT for inspection — no live data link, no actuation, no learning loop.

*Full-text source: 04c-port*

**AH — strength & gap filled:** Automates tunnel inspection digital twin creation from heterogeneous field data: point clouds from a Faro Focus 3D X330 scan of the Coastal Tunnel are cleaned and decimated, meshed by Poisson reconstruction in Grasshopper, with the new MDQ index guiding mesh quality, and metadata attached via EleFront; digital inspection took about 18 minutes versus 46 minutes manual and located a leakage the visual survey missed.

**AI — deficiencies & future work:** The model is static with no real-time synchronization, digital inspection missed fine shrinkage cracks, portal overexposure prevents accurate color extraction, internet access is required for server connection, and point cloud density depends on scanning equipment; the authors plan additional information layers and UAV or ROV LiDAR acquisition for hard-to-reach tunnels.
