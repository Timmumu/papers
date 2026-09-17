# Ye et al. (2023) — A digital twin approach for tunnel construction safety early warning and management

- **ID:** 3696 | **Source:** Scopus | **DOI:** 10.1016/j.compind.2022.103783
- **Journal:** Computers in Industry
- **Authors:** Ye, Z.; Ye, Y.; Zhang, C.; Zhang, Z.; Li, W.; Wang, X.; Wang, L.; Wang, L.

## Abstract summary
Accidents tend to happen during tunnel construction due to the harsh environmental and geological conditions. Towards high safety risk during tunnel construction, a digital-twin based multi-information intelligent early warning and safety management platform is proposed in this study. At first, a communication line is built inside tunnel through multifunctional base stations. Multi-source information from tunnel construction could be collected and transmitted automatically. Then, dynamic tunnel construction information and surrounding rock conditions are virtual simulated. Meanwhile, four-level early warning and emergency response plan are built to provide judgement on the construction status. At last, application effects of the platform are validated in a deep buried tunnel project, Dongtianshan Tunnel in China, which has extreme weather, harmful gas, and bad geological conditions. A co…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** DT tunnel construction early warning; collapse predicted, personnel saved

## Step-3 Deep-Read Coding (Prompt B)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow (one-way physical to virtual) | 0 | 1 | 0 | Design for Safety (DfS) | None | Digital Twin platform (no machine learning) | Multi (two or more data types) | Single case study | 4 | Design for Safety |

**Key evidence (AG):** Digital-twin based multi-information intelligent early warning and safety management platform for tunnel construction (CUGB/Beijing Jiaotong U): WSN base stations for instruction sending, warning, positioning, information transmission; multi-source sensors (safety, environmental, construction, auxiliary) integrated; four-level early warning and emergency response plan; validated on Dongtianshan Tunnel (deep buried, extreme weather, harmful gas); collapse accident successfully predicted. One-way monitoring→early warning→management; no actuation and no learning loop.


**Strength & gap filled (AH):** Fills the gap of multi-source information transmission and DT-based early warning in deep-buried tunnel construction: multifunctional wireless base stations collect harmful gas, meteorological, deformation, and personnel-positioning data, mirrored in an OpenGL virtual tunnel with a four-level warning and emergency response mechanism, which successfully predicted a collapse at the K0+668 face of the 11.7 km Dongtianshan Tunnel with no casualties.

**Deficiencies & future work (AI):** The virtual simulation lacks detailed display and monitoring of worker behavior, health, and collision risks, and pre-construction risk analysis is not integrated; future work adds more monitoring data types, deeper pre-construction risk analysis, and an improved tunnel construction information database for predictive analysis in the maintenance stage.
**Fusion depth (AC1):** Aligned

**Fusion evidence (AC2):**
- **Data streams:** harmful-gas, meteorological, deformation and personnel-positioning sensors (Dongtianshan Tunnel, 11.7 km).
- **Integration mechanism:** multifunctional WSN base stations mirror the streams into the virtual tunnel, and the four-level warning/emergency mechanism acts on thresholds, successfully predicting a K0+668 face collapse.
- **Why this code:** streams share the tunnel-model frame while warnings run per parameter, so Aligned.

**Confidence (AC3):** High - the virtual-tunnel mapping is explicit.
(full-text source: Endnote)
