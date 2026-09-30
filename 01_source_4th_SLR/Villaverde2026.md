# Villaverde, I et al. (2026) — A Digital Twin-Driven System for Road Maintenance: Integrating UAVs and AMRs for Automated Inspection and Measurement

- **ID:** R129 | **Source:** Scopus | **DOI:** 10.3390/infrastructures11040124
- **Journal:** Infrastructures
- **Authors:** Villaverde I.; Sallé D.; Montes-Grova M.A.; Jiménez-Cámara P.; Castelruiz-Aguirre A.; Pastorelly N.; Jimenez Fernandez J.C.; Stipanovic I.; Skaric S.; Rodik D.

## Abstract summary
Road maintenance remains one of the most resource-intensive and hazardous operations in infrastructure management. Traditional inspection practices rely heavily on manual labour and discrete procedures, often resulting in limited scalability, operator exposure to traffic hazards, and inefficiencies in data collection. This paper presents a novel automated methodology that integrates Unmanned Aerial Vehicles (UAVs) and autonomous mobile robots (AMRs) to enable automated inspection and measurement of road assets through a digital twin (DT) system. The system leverages data fusion and real-time synchronisation between field agents and a centralised digital twin to monitor the retro-reflectivity of vertical and horizontal signage, detect obstacles and vegetation, and support data-driven maintenance planning. A case study conducted on the Italian highway network demonstrated improvements in o…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** UAV+AMR road maintenance DT; operational safety

## Step-3 Deep-Read Coding (Prompt B)
| P DT-subject | Q DfS/DfQ | R codable | U Tier | V Design | W Constr | X Oper | Z DfX | AA Self-improve | AB Methodology | AC Modality | AD Validation | AE QA(0-5) | AF Cluster |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow (one-way physical to virtual) | 0 | 0 | 1 | Design for Safety (DfS) | None | Perception / Computer Vision | Multi (two or more data types) | Single case study | 4 | Design for Safety |

| AC1 fusion depth | AC2 fusion evidence | AC3 confidence |
|---|---|---|
| Aligned | UAV and AMR measurements are geo-registered and merged via MQTT/Node-RED into ontology-based KPI dashboards, sharing a geospatial frame while KPI analytics run per asset type. | Medium |

**Key evidence (AG):** Digital twin-driven system for road maintenance (TECNALIA): UAV + AMR integration for automated inspection and measurement of road assets; data fusion and real-time synchronisation between field agents and centralised DT; retro-reflectivity monitoring of signage, obstacle/vegetation detection; supports data-driven maintenance planning; case study on Italian highway network. One-way monitoring→DT→maintenance planning; no actuation and no learning loop.

*Full-text source: 04c-port*

**AH — strength & gap filled:** Demonstrates an operational UAV plus AMR inspection workflow synchronized with a cloud digital twin: a UAV with YOLOX detection, UPerNet segmentation, and LiDAR retro-reflectivity analysis covers vertical signage and vegetation, while an AMR measures horizontal markings, with MQTT and Node-RED data fusion into ontology-based KPI dashboards, validated at the A24 motorway Gran Sasso Nord site in central Italy, with sub-10-cm AMR navigation repeatability.

**AI — deficiencies & future work:** Validated only in clear daylight conditions, with sensor accuracy unproven in rain, fog, or low light and the Jetson Orin GPU running near capacity, limiting model complexity; EU regulation 2022/1426 currently bars fully autonomous AMR operation on open roads, and the twin only reports conditions without actuation. Future work covers sensor redundancy, adverse-weather training, predictive maintenance, automated work orders, and compliance-by-design.
