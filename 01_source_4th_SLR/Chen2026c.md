# Chen, R et al. (2026) — Digital Twin-Enabled Robust Parallel Control of Construction Engineering Equipment Under Uncertainty

- **ID:** R303 | **Source:** Scopus | **DOI:** 10.3390/buildings16101982
- **Journal:** Buildings
- **Authors:** Chen R.; Xu H.; Zhang L.; Rong J.; Wei C.; Chang H.; Zhang H.

## Abstract summary
This paper proposes a digital twin framework for robust parallel control of the mobile gin pole in ultra-high voltage (UHV) transmission line construction, aiming to improve safety and operational efficiency under uncertain conditions. The new framework integrates kinetic analysis, machine learning models, and multi-objective optimization algorithms to address the challenges of heavy-lifting operations in complex terrains. The method conducts finite-element kinetic analysis based on the actual structure of the mobile gin pole. A Tyrannosaurus Rex Optimization Algorithm (TROA) is employed to enhance the performance of the Extra Randomized Trees (ET) model for predicting key parameters such as maximum axial stress and shear stress. The framework leverages the Non-Dominated Sorting Genetic Algorithm III (NSGA-III) to optimize safety and efficiency metrics by adjusting key control parameters…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** Gin pole robust parallel-control DT; lifting safety

## Step-3 Deep-Read Coding (Prompt B)
| P DT-subject | Q DfS/DfQ | R codable | U Tier | V Design | W Constr | X Oper | Z DfX | AA Self-improve | AB Methodology | AC Modality | AD Validation | AE QA(0-5) | AF Cluster |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 3 - Digital Twin (bidirectional, two-way) | 0 | 1 | 0 | Design for Safety (DfS) | Mentioned only | Other / Mixed | Multi (two or more data types) | Single case study | 4 | Design for Safety |

| AC1 fusion depth | AC2 fusion evidence | AC3 confidence |
|---|---|---|
| Aligned | Live operational data and the TROA-ET/FEM surrogate coexist in the DT parallel-control architecture over bidirectional 4G/MQTT links, but the surrogate is offline-trained and no joint inference across streams is stated. | Medium |

**Key evidence (AG):** Mobile gin pole (UHV construction): FEM kinetic analysis + TROA-ET surrogate (R2 0.9642) + NSGA-III safety-efficiency optimisation embedded in DT parallel-control architecture; bidirectional 4G/MQTT link (CANopen control commands) on real 110 kV project; safety risk -32.3%; surrogate is offline-trained, no online learning.

*Full-text source: 04c-port*

**AH — strength & gap filled:** Addresses robust parallel control of construction equipment under uncertainty: a mobile gin pole digital twin for UHV construction embeds finite-element kinetic analysis with a TROA-ET surrogate model (R2 0.9642) and NSGA-III safety-efficiency optimisation within a DT parallel-control architecture supported by bidirectional 4G and MQTT links.

**AI — deficiencies & future work:** The available record states no explicit future work; validation is documented only for the mobile gin pole application, and whether the TROA-ET surrogate is updated online, transferred to other equipment types, or tested against field disturbances beyond the stated scenario is not established.
