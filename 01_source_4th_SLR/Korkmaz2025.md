# Korkmaz, M et al. (2025) — A Digital Twin Approach to Sustainable Disaster Management: Case of Cayirova

- **ID:** R185 | **Source:** Scopus | **DOI:** 10.3390/su17219626
- **Journal:** Sustainability (Switzerland)
- **Authors:** Korkmaz M.; Akyildiz Y.E.; Demirkesen S.; Toprak S.; Nowak P.; Ciftci B.

## Abstract summary
Disaster management requires the development of effective technologies for managing both pre-and post-disaster processes. Therefore, utilizing effective tools and techniques to mitigate the disaster risks or lower the adversarial impacts is essential. Over the last decade, digital twin (DT) applications have found a wider implementation area for varying purposes, but most importantly, they are utilized for simulating disaster impacts. This study aims to develop an open-source digital twin (DT) framework for earthquake disaster management in the Cayirova district of Kocaeli, Türkiye, one of the country’s most seismically active regions. The primary objective is to enhance local resilience by integrating multi-source data into a unified digital environment that supports risk assessment, response planning, and recovery coordination. The digital model developed using QGIS (3.40.9 Bratislava)…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** District-level earthquake disaster DT; resilience

## Step-3 Deep-Read Coding (Prompt B)
| P DT-subject | Q DfS/DfQ | R codable | U Tier | V Design | W Constr | X Oper | Z DfX | AA Self-improve | AB Methodology | AC Modality | AD Validation | AE QA(0-5) | AF Cluster |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 1 - Digital Model (static, no live data) | 0 | 0 | 1 | Design for Safety (DfS) | None | Digital Twin platform (no machine learning) | Multi (two or more data types) | Conceptual (no test) | 3 | Lifecycle / governance |

| AC1 fusion depth | AC2 fusion evidence | AC3 confidence |
|---|---|---|
| Aligned | Geospatial, environmental, transport, utility and demographic layers are combined in one QGIS/InfraWorks database rather than analytically fused. | Medium |

**Key evidence (AG):** Open-source district-level digital twin for earthquake disaster management (Gebze Technical U, Sustainability 2025): QGIS + Autodesk InfraWorks model of Cayirova district integrating geospatial, environmental, transportation, utility and demographic data as a unified 2D/3D digital database supporting risk assessment, response planning and recovery coordination; first district-level open-source DT in Cayirova. Static digital model/database - expected future use for seismic risk assessment; no simulation results, no live data, no actuation, no learning loop.

*Full-text source: browser-oa*

**AH — strength & gap filled:** Provides the first open-source district-level DT database for earthquake disaster management in Cayirova, unifying geospatial and building data for faster data-driven emergency decisions.

**AI — deficiencies & future work:** Digital model/database only - no risk analysis results or simulation shown; expected benefits (resilience, logistics) are unquantified; maintenance of the open data model over time unspecified.
