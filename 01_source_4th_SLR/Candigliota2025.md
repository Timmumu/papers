# Candigliota, E et al. (2025) — The Integration of a Multidomain Monitoring Platform with Structural Data: A Building Case Study

- **ID:** R063 | **Source:** Scopus | **DOI:** 10.3390/su17073076
- **Journal:** Sustainability (Switzerland)
- **Authors:** Candigliota E.; Colaneri O.; Gioiella L.; Leggieri V.; Marghella G.; Marzo A.; Mazzarelli S.; Morici M.; Murazzo S.; Seferi R.; Tatì A.; Tripepi C.; Luprano V.A.M.

## Abstract summary
In recent years, innovative Non-Destructive Testing (NDT) techniques, applicable for the assessment of existing civil structures, have become available for in situ analysis on Reinforced Concrete (RC) and masonry structures, but they are still not established for regular inspections, especially after seismic events. The damage assessment of RC buildings after seismic events is a very relevant issue in Italy, where most of the structures built in the last 50 years are RC structures. Furthermore, there is also a growing interest in being able to monitor structural health aspects by storing them on the building’s digital twin. For these reasons, it is necessary to develop an affordable and ready-to-use NDT procedure that provides more accurate indications on the real state of damage of reinforced concrete buildings after seismic events and to integrate these data into an interoperable digit…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** NDT + digital twin for building damage assessment

## Step-3 Deep-Read Coding (Prompt B)
| P DT-subject | Q DfS/DfQ | R codable | U Tier | V Design | W Constr | X Oper | Z DfX | AA Self-improve | AB Methodology | AC Modality | AD Validation | AE QA(0-5) | AF Cluster |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow (one-way physical to virtual) | 0 | 0 | 1 | Design for Safety (DfS) | None | Digital Twin platform (no machine learning) | Multi (two or more data types) | Single case study | 3 | BIM-to-Digital-Twin architecture |

| AC1 fusion depth | AC2 fusion evidence | AC3 confidence |
|---|---|---|
| Fused | NDT results, distributed sensor-node data and BIM geometry are integrated in the LIS platform as one building twin. | Medium |

**Key evidence (AG):** Multidomain monitoring integration (ENEA, Sustainability 2025): affordable NDT procedure for post-earthquake damage assessment of RC buildings; NDT results and distributed sensor nodes inserted into the LIS platform to create the building digital twin for automated monitoring, management and preventive maintenance; QR-code interface simplifies operator workflow; case study on a 2016-earthquake-damaged building in Marche, Italy (MULTICLIMACT). One-way monitoring->twin->maintenance decisions; no actuation, no learning loop.

*Full-text source: browser-oa*

**AH — strength & gap filled:** Delivers an affordable, ready-to-use NDT-plus-LIS procedure that stores post-earthquake damage data in an interoperable building digital twin with distributed sensor nodes and a QR-code interface, supporting automated preventive maintenance.

**AI — deficiencies & future work:** Single building case; the DT stores and visualises data but performs no predictive analytics; long-term sensor reliability and multi-site scalability are not demonstrated.
