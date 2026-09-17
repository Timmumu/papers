# Liu et al. (2020) — A framework for an indoor safety management system based on digital twin

- **ID:** 3641 | **Source:** Scopus | **DOI:** 10.3390/s20205771
- **Journal:** Sensors (Switzerland)
- **Authors:** Liu, Z.; Zhang, A.; Wang, W.

## Abstract summary
With the development of the next generation of information technology, an increasing amount of attention is being paid to smart residential spaces, including smart cities, smart buildings, and smart homes. Building indoor safety intelligence is an important research topic. However, current indoor safety managementmethods cannot comprehensively analyse safety data, owing to a poor combination of safety management and building information. Additionally, the judgement of danger depends significantly on the experience of the safety management staff. In this study, digital twins (DTs) are introduced to building indoor safety management. A framework for an indoor safety management system based on DT is proposed which exploits the Internet of Things (IoT), building information modelling (BIM), the Internet, and support vector machines (SVMs) to improve the level of intelligence for building ind…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** DT indoor safety management; SVM danger classification; stadium case

## Step-3 Deep-Read Coding (Prompt B) — full text verified via Endnote library (front-matter DOI/title match, coverage re-scan 2026-08-12)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow | 0 | 0 | 1 | Design for Safety (DfS) | None | Other / Mixed | Multi (two or more data types) | Single case study | 4 | Predictive analytics / decision support |

**Key evidence (AG):** Indoor safety management system (ISMS) based on digital twin, applied to a room in the Beijing 2022 Winter Olympics bobsleigh/sled stadium: IoT sensors collect real-time indoor operation data → BIM-based DTM maps real→virtual; SVM (support vector machine) trained to automatically classify danger types and assess danger levels from DTM data; functions include operation-status scene display, danger warning and positioning, danger classification/level assessment, and automatic danger-handling suggestions; synchronous virtual+real-world alarms. One-way monitoring/analysis→suggestions for staff; no actuation and no stated self-improvement loop (SVM is offline-trained).

**Strength & gap filled (AH):** Addresses the disconnect between independent indoor safety systems and building information: a digital twin-based indoor safety management system combining lightweight WebGL BIM, LoRa IoT terminals (oxygen, CO, smoke, temperature, door and window sensors plus camera people counting) and SVM models that classify fire, illegal intrusion and overcrowding with 97.57 to 100 percent accuracy and grade danger levels at 96.2 percent accuracy with R2 above 0.89, applied to a Beijing Winter Olympics stadium building.

**Deficiencies & future work (AI):** The SVM models are trained offline on 15 days of simulated danger data from one stairwell room, danger coefficient scoring depends on safety staff judgment, and danger handling still falls to human staff. Future work targets more targeted handling suggestions, additional dangers such as harmful gas leaks, and extending digital twin models to structural and equipment safety management.

**Fusion depth (AC1):** Fused

**Fusion evidence (AC2):**
- **Data streams:** oxygen, CO, smoke, temperature, door/window sensors plus camera people-counting in a Beijing Winter Olympics stadium room.
- **Integration mechanism:** the multi-channel sensor data are fed together into SVM classifiers (97.57-100% danger-class accuracy; 96.2% level accuracy, R2 above 0.89) displayed on the WebGL BIM twin.
- **Why this code:** the classifiers consume several sensor types simultaneously, so Fused.

**Confidence (AC3):** High - the multi-input SVM pipeline is explicit.