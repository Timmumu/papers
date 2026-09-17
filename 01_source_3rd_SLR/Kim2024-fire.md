# Kim et al. (2024) — Advanced fire emergency management based on potential fire risk assessment with informative digital twins

- **ID:** 3999 | **Source:** Web of Science | **DOI:** 10.1016/j.autcon.2024.105722
- **Journal:** AUTOMATION IN CONSTRUCTION
- **Authors:** Kim, Y. J.; Kim, H.; Ha, B.; Kim, W. T.

## Abstract summary
Modern large complex buildings, with their vast expanses and multipurpose usability, present diverse fire- spread scenarios, necessitating precise awareness of fire situations. Despite numerous studies integrating building information models with IoT and AI technologies to provide contextual information, there may be limitations in recognizing potential risks under dynamic fire behaviors during urgent situations. This paper presents a fire emergency management system based on an informative digital twin (IDT) to provide instantaneous fire situational information. Utilizing IDT, the system gathers building-specific fire scenario knowledge for immediate fire recognition. Leveraging this knowledge, the IDT assesses building fire risks and shares safety information on egress routes and zones with fire-related applications. A simulation case study revealed a fire recognition processing time o…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** Informative DT fire emergency management; evacuation risk

## Step-3 Deep-Read Coding (Prompt B)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow (one-way physical to virtual) | 0 | 0 | 1 | Design for Safety (DfS) | None | Statistical / change-point | Multi (two or more data types) | Single case study | 4 | Design for Safety |

**Key evidence (AG):** Informative digital twin (IDT) based fire emergency management system (Sehan U/KUT): cloud-edge-device layers; edge-layer IDT built with object-oriented design gathers/processes building state data; fire recognition via online DTW similarity measurement between real and simulated virtual sensor data; risk assessment with ARET/RRET/SM metrics per zone; case study shows 0.88s fire recognition processing time and 65s evacuation time reduction. One-way monitoring→fire recognition→risk assessment; no actuation and no learning loop (DTW is similarity matching, not learning).


**Strength & gap filled (AH):** Bridges pre-simulated fire knowledge and real-time emergency response: an edge-layer informative digital twin on a cloud-edge-device architecture compares live sensor data against a pre-simulated fire knowledge base using online DTW with parallel processing, recognizing fire scenarios in 0.88 s versus over eight hours of CFD; zone-based ARET, RRET, and safety margin assessment cut evacuation time by 65 s and injuries by 406 in a Hoehyeon underground mall simulation.

**Deficiencies & future work (AI):** Validated through simulation only, with no real fire deployment. Risk assessment considers just three fire risk factors and assumes average walking speed, ignoring obstacles, blocked paths, age, and disability; recognition accuracy depends on the completeness of the knowledge base, and computing and network resources may be strained as buildings and sensors scale. Future work covers generative-AI scenario generation and personalized risk assessment.
**Fusion depth (AC1):** Fused

**Fusion evidence (AC2):**
- **Data streams:** live building-state sensor data + pre-simulated fire-scenario virtual-sensor data.
- **Integration mechanism:** online DTW with parallel processing matches real against simulated series for fire recognition in 0.88 s, followed by ARET/RRET/safety-margin risk assessment per zone.
- **Why this code:** recognition output depends on both streams simultaneously, so Fused; validated through simulation of an underground mall (Medium).

**Confidence (AC3):** Medium - the DTW mechanism is explicit, but validation is simulation-only.
(full-text source: Endnote)
