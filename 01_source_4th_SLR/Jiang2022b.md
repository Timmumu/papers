# Jiang, H et al. (2022) — Monitoring System for the Construction of Arch Cover Method Subway Station Based on DT and IoT

- **ID:** R850 | **Source:** Scopus | **DOI:** 10.1155/2022/1875196
- **Journal:** Journal of Sensors
- **Authors:** Jiang H.; Jiang A.

## Abstract summary
Aiming at the problems of safety and monitoring beyond the existing experience in the construction of the subway stations with arch cover method in Dalian, China, combined with the real-time monitoring requirements of intelligent construction status, a multi-information construction monitoring system based on digital twin(DT) and Internet of Things(IoT) is proposed, and the digital twin 3D architecture is established. First, on the basis of the IoT monitoring experience of tunnel, the installation plan of the automatic monitoring device of the arch cover method subway station is clarified, and the sensor arrangement is carried out. Then, based on the Revit platform, the establishment of the main structure model of the station and the BIM parametric modeling technology of the sensors are realized, and the monitoring properties of the sensors are expanded. Finally, through the design of th…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** DT + IoT monitoring of arch cover subway station


## Step-3 Deep-Read Coding (Prompt B)
| P DT-subject | Q DfS/DfQ | R codable | U Tier | V Design | W Constr | X Oper | Z DfX | AA Self-improve | AB Methodology | AC Modality | AD Validation | AE QA(0-5) | AF Cluster |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow (one-way physical to virtual) | 0 | 1 | 0 | Design for Safety (DfS) | None | Digital Twin platform (no machine learning) | Multi (two or more data types) | Single case study | 3 | Design for Safety |

| AC1 fusion depth | AC2 fusion evidence | AC3 confidence |
|---|---|---|
| Aligned | Settlement, stress and displacement sensors stream into IFC-extended Revit BIM models with parametric sensor attributes and time-history curves, linking sensors to BIM elements without joint inference. | High |

**Key evidence (AG):** DT+IoT multi-information monitoring system for arch-cover method subway station construction (Shikui Road Station, Dalian Metro Line 5): automatic sensor network (settlement, stress, etc.) → IFC extension + Revit BIM parametric sensor models → BIM database visualization with time-history curves and color-change early-warning; "Construction Control Based on Data Analysis" uses monitored data as control value for decisions, but the loop is human-in-the-loop (feedback to decision-makers), not automated actuation; no ML, no self-improvement.

*Full-text source: 04c-port*

**AH — strength & gap filled:** Provides automatic monitoring for arch cover method subway stations, rare in the literature, via a DT and IoT system at Shikui Road Station of Dalian Metro Line 5: pressure cells, rebar meters, strain gauges and displacement meters stream into a Revit secondary-developed BIM platform with IFC-extended sensor attributes and color-change alarms; lining pressure rises after temporary support removal informed inverse analysis that set midwall demolition at 12 m.

**AI — deficiencies & future work:** The system is only applied to one station project, sensor equipment still needs anticorrosion and anti-interference development, and the numerical analysis model must be improved for true two-way mapping between digital and physical worlds; future work includes prediction algorithms, web, GIS, 5G and blockchain integration for multi-station unified management.
