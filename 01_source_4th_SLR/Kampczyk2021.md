# Kampczyk, A et al. (2021) — The fundamental approach of the digital twin application in railway turnouts with innovative monitoring of weather conditions

- **ID:** R669 | **Source:** Scopus | **DOI:** 10.3390/s21175757
- **Journal:** Sensors
- **Authors:** Kampczyk A.; Dybeł K.

## Abstract summary
Improving railway safety depends heavily on the reliability of railway turnouts. The real-ization of effective, reliable and continuous observations for the spatial analysis and evaluation of the technical condition of railway turnouts is one of the factors affecting safety in railway traffic. The mode and scope of monitoring changes in geometric parameters of railway turnouts with asso-ciated indicators needs improvement. The application of digital twins to railway turnouts requires the inclusion of fundamental data indicating their condition along with innovative monitoring of weather conditions. This paper presents an innovative solution for monitoring the status of temperature and other atmospheric conditions. A UbiBot WS1 WIFI wireless temperature logger was used, with an external DS18B20 temperature sensor integrated into an S49 (49E1)-type rail as Tszyn WS1 WIFI. Measurements were…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** DT for railway turnouts with weather monitoring

## Step-3 Deep-Read Coding (Prompt B)
| P DT-subject | Q DfS/DfQ | R codable | U Tier | V Design | W Constr | X Oper | Z DfX | AA Self-improve | AB Methodology | AC Modality | AD Validation | AE QA(0-5) | AF Cluster |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 1 - Digital Model (static, no live data) | 0 | 0 | 1 | Design for Safety (DfS) | None | Digital Twin platform (no machine learning) | Multi (two or more data types) | Single case study | 3 | Design for Safety |

| AC1 fusion depth | AC2 fusion evidence | AC3 confidence |
|---|---|---|
| Fused | Rail temperature, humidity, ambient temperature and light are fused into turnout condition monitoring data. | Low |

**Key evidence (AG):** Fundamental approach to digital twins for railway turnouts with innovative weather monitoring (Sensors 2021): UbiBot WS1 WIFI logger with external DS18B20 sensor embedded in an S49 (49E1) rail (Tszyn WS1 WIFI) measures rail-head temperature, humidity, ambient temperature and light (Jan-May); confirms the TgCWRII second-temperature-difference indicator for turnout monitoring and positions rail-temperature data as a component of turnout DT condition data. Sensing/data-acquisition foundation only - no twin model built.

*Full-text source: browser-oa*

**AH — strength & gap filled:** Rail-embedded wireless temperature sensing (Tszyn WS1 WIFI) provides the environmental data foundation for turnout digital twins and confirms the TgCWRII indicator.

**AI — deficiencies & future work:** Sensing only - no turnout twin model or geometry integration demonstrated.
