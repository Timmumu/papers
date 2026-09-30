# Mutawa, A.M et al. (2023) — Digital Twin of a Data Center at an Educational Institution

- **ID:** R869 | **Source:** Scopus | **DOI:** 10.36909/jer.15973
- **Journal:** Journal of Engineering Research (Kuwait)
- **Authors:** Mutawa A.M.; Tolba A.S.

## Abstract summary
Digital twins are among the most important trends of the fourth industrial revolution. They present a crucial tool for protecting critical mission systems and the development of new services, products, and processes. This paper presents the first digital twin for a data center. The rapid growth of the Internet of things and the areas of modeling and simulation results in high demand for the development of data center digital twins (DCDT) to ensure the safety/protection of critical and costly mission infrastructure and guarantee business continuity, enhance efficiency, and sustain development. This paper presents the design and implementation of a digital twin for a university data center. Different sensory data like temperature, humidity, smoke, and water leakage are analyzed using an intelligent event detection approach, which detects abnormalities using an Extreme Learning Machine (ELM…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** Data center DT with smoke/leakage safety detection

## Step-3 Deep-Read Coding (Prompt B)
| P DT-subject | Q DfS/DfQ | R codable | U Tier | V Design | W Constr | X Oper | Z DfX | AA Self-improve | AB Methodology | AC Modality | AD Validation | AE QA(0-5) | AF Cluster |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 3 - Digital Twin (bidirectional, two-way) | 0 | 0 | 1 | Design for Safety (DfS) | None | Other / Mixed | Multi (two or more data types) | Single case study | 3 | Design for Safety |

| AC1 fusion depth | AC2 fusion evidence | AC3 confidence |
|---|---|---|
| Fused | Temperature/humidity/smoke/leakage streams are fused for ELM abnormal event detection. | Medium |

**Key evidence (AG):** Digital twin of a university data center (Kuwait University, Journal of Engineering Research 2023): temperature, humidity, smoke and water-leakage sensor streams analysed by an Extreme Learning Machine using the minimum ratio between successive real-time streams for abnormal event detection; outperforms LVQ and RBF classifiers; GSM alerts staff and, in urgent cases, actuators are activated via microcontrollers (server shutdown, fire extinguishing, standby AC). Virtual-to-physical actuation -> Tier 3.

*Full-text source: browser-oa*

**AH — strength & gap filled:** ELM-based abnormal event detection with actuator response (server shutdown, extinguishing, standby AC) in a working data center.

**AI — deficiencies & future work:** Single data center; detection thresholds and false-alarm behaviour partially reported.
