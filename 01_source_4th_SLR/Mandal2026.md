# Mandal, D et al. (2026) — FlowsDT: A geospatial digital twin for navigating urban flood dynamics

- **ID:** R065 | **Source:** Scopus | **DOI:** 10.1016/j.compenvurbsys.2026.102414
- **Journal:** Computers, Environment and Urban Systems
- **Authors:** Mandal D.; Zou L.; Wadhwa A.; Wilkho R.S.; Cai Z.; Zhou B.; Ye X.; Newman G.; Gharaibeh N.; Güneralp B.

## Abstract summary
Communities worldwide increasingly confront flood hazards intensified by climate change, urban expansion, and environmental degradation. Addressing these challenges requires real-time flood analysis, precise flood forecasting, and robust risk communications with stakeholders to implement efficient mitigation strategies. Recent advances in hydrodynamic modeling and digital twins afford new opportunities for high-resolution flood simulation and visualization at the street and basement levels. Focusing on Galveston City, a barrier island in Texas, U.S., this study created a geospatial digital twin supported by 1D-2D coupled hydrodynamic models to strengthen urban resilience to pluvial and fluvial flooding. The objectives include: (1) developing a Geospatial Digital Twin (FlowsDT-Galveston) incorporating topography, hydrography, and infrastructure; (2) validating the twin using historical fl…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** Geospatial urban flood DT; resilience/safety

## Step-3 Deep-Read Coding (Prompt B)
| P DT-subject | Q DfS/DfQ | R codable | U Tier | V Design | W Constr | X Oper | Z DfX | AA Self-improve | AB Methodology | AC Modality | AD Validation | AE QA(0-5) | AF Cluster |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 1 - Digital Model (static, no live data) | 0 | 0 | 1 | Design for Safety (DfS) | None | Finite Element Method / physics-based | Multi (two or more data types) | Single case study | 4 | Predictive analytics / decision support |

| AC1 fusion depth | AC2 fusion evidence | AC3 confidence |
|---|---|---|
| Fused | LiDAR topography, land cover and storm-sewer geometries are fused in the coupled 1D-2D hydrodynamic model. | High |

**Key evidence (AG):** FlowsDT-Galveston geospatial digital twin (Texas A&M, Comput Environ Urban Syst 2026): 1D-2D coupled PCSWMM hydrodynamic models over LiDAR topography, land cover and storm-sewer geometry elevate the urban twin to LoD4 (underground network); validated with historical flood events and social sensing; simulates 2/10/25/50/100-yr scenarios - buildings inundated >1 ft +5.7%, roads +6.7%; supports proactive flood management and urban planning. Scenario-simulation twin; real-time sensor integration only described as potential; no actuation, no learning loop.

*Full-text source: browser-oa*

**AH — strength & gap filled:** Elevates urban flood digital twins to LoD4 by coupling 1D storm-sewer and 2D surface-flow models, validated against historical floods and social sensing across five return periods for street/basement-level risk mapping.

**AI — deficiencies & future work:** No real-time sensor integration yet (potential only); social-sensing validation is coarse; 4D immersive visualisation is described but an interactive stakeholder interface is not delivered.
