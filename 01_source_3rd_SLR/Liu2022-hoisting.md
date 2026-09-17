# Liu et al. (2022) — Digital Twin‐Based Risk Control during Prefabricated Building Hoisting Operations

- **ID:** 3560 | **Source:** Scopus | **DOI:** 10.3390/s22072522
- **Journal:** Sensors
- **Authors:** Liu, Z.; Li, A.; Sun, Z.; Shi, G.; Meng, X.

## Abstract summary
Prefabricated buildings have advantages when it comes to environmental protection. However, the dynamics and complexity of building hoisting operations bring significant safety risks. Existing research on hoisting safety risk lacks a real‐time information interaction mechanism and lacks scientific control decision‐making tools based on considering the correlation between safety risks. Digital twin (DT) has the advantage of real‐time interaction. This paper presents a safety risk control framework for controlling prefabricated building hoisting operations based on DT. In the case of considering the correlation of the safety risk index of hoisting, the safety risk hierarchy model of hoisting is defined in the process of building the DT model. The authors have established a Bayesian network model into the process of the integrated analysis of the digital twin mechanism model and monitoring …

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** DT+BN risk control for prefab hoisting operations

## Step-3 Deep-Read Coding (Prompt B)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow (one-way physical to virtual) | 0 | 1 | 0 | Design for Safety (DfS) | None | Bayesian / probabilistic | Multi (two or more data types) | Single case study | 4 | Predictive analytics / decision support |

**Key evidence (AG):** DT-based risk control framework for prefabricated building hoisting (Beijing U Tech): DEMATEL-ISM establishes hierarchical safety risk model considering correlation between risk factors; Bayesian network visualizes decision analysis process for risk control; real-time data interaction with DT model; key degree of indirect inducement variables calculated by probability; validated on a large prefabricated building project. One-way monitoring→analysis→decision support; no actuation and no learning loop (Bayesian network is offline-inferred).


**Strength & gap filled (AH):** Elevates prefabricated hoisting digital twin research from static expert-based risk scoring to the essence of safety risk: a DEMATEL-ISM hierarchical risk model embedded in the twin, with Bayesian network reasoning via EM-trained parameters computing the key degree of indirect inducement factors when a direct factor such as sling angle turns dangerous, verified on a 71,172 square meter Tianjin prefabricated project with RFID, IMU, crane black box and LoRa sensing.

**Deficiencies & future work (AI):** The training sample set is very limited (three integrated time points, expert-copied and expanded) and no intelligent decision system or automatic actuation exists; integration with hoisting risk assessment and prediction methods remains open. Future research will expand data samples to improve accuracy and enhance the BIM platform visualization and functional modules.
**Fusion depth (AC1):** Fused

**Fusion evidence (AC2):**
- **Data streams:** RFID, IMU, crane black-box and LoRa sensing on a 71,172 m2 Tianjin prefabricated project.
- **Integration mechanism:** the multi-source sensing streams are combined in the DT, and the DEMATEL-ISM + BN model reasons jointly over them to compute risk-control priorities.
- **Why this code:** the BN risk output depends on several sensor streams simultaneously, so Fused; training samples are limited and expert-copied (Medium).

**Confidence (AC3):** Medium - the BN reasoning is explicit, but data provenance is limited (three time points, expert-copied).
(full-text source: Endnote)
