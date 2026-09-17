# Kim et al. (2024) — Spatio-temporal heat risk analysis in construction: Digital twin-enabled monitoring

- **ID:** 3938 | **Source:** Web of Science | **DOI:** 10.1016/j.autcon.2024.105805
- **Journal:** AUTOMATION IN CONSTRUCTION
- **Authors:** Kim, Y.; Ham, Y.

## Abstract summary
To effectively mitigate heat risks, it is crucial to pinpoint areas of high vulnerability and assess the severity of heat-related threats to construction workers. This paper advances the understanding of heat risks in construction by mapping the associated risks across time and space to support informed decision-making. This paper presents a framework for heat risk monitoring, enabled by a construction site digital twin. This framework leverages geometric modeling, incorporates real-time weather data from a weather station, and utilizes computational simulations for assessing spatio-temporal heat risks. Its effectiveness was validated through a case study in Stephenville, Texas, USA, where it demonstrated superior fidelity when compared to using the conventional black-globe thermometer. Moreover, the results substantiated that incorporating the spatio-temporal variability of heat risks e…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** DT-enabled spatio-temporal heat risk monitoring for workers

## Step-3 Deep-Read Coding (Prompt B)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow (one-way physical to virtual) | 0 | 1 | 0 | Design for Safety (DfS) | None | Other / Mixed | Multi (two or more data types) | Single case study | 4 | Design for Safety |

**Key evidence (AG):** Digital twin-enabled heat risk monitoring for construction workers (Texas A&M): geometric digital twin of construction site + real-time weather station data + computational simulations for spatio-temporal heat risk analysis; case study in Stephenville, Texas, shows superior fidelity vs black-globe thermometer; near-real-time heat risk maps enable targeted interventions. One-way monitoring→simulation→risk maps; no actuation and no learning loop (microclimate simulation is physics-based, not learning).


**Strength & gap filled (AH):** Overcomes the point-measurement limits of black-globe thermometers: UAV photogrammetry builds a geometric site twin, an on-site weather station streams temperature, humidity, irradiance, and wind, and SOLWEIG microclimate simulation with shadow, sky view factor, and surface material maps yields site-wide heat risk maps; in Stephenville, Texas, the simulation method estimated mean radiant temperature with RMSE 4.21 C and R2 0.93 versus 11.80 C and 0.44 for the black-globe method.

**Deficiencies & future work (AI):** The geometric virtual model is not synchronized between UAV image updates, so same-day erected structures and moving equipment are missed; surface temperature simulation overestimates by up to 23.6 C for asphalt, and manual material registration is labor-intensive. UAV infrared thermography is computationally demanding at site scale. Future research targets integrating biometric sensors for individualized worker heat risk assessment.
**Fusion depth (AC1):** Fused

**Fusion evidence (AC2):**
- **Data streams:** on-site weather station (temperature, humidity, irradiance, wind) + UAV-photogrammetry geometric twin (shadow, sky-view factor, surface-material maps).
- **Integration mechanism:** SOLWEIG simulation combines the weather streams with the geometric model into spatio-temporal heat-risk maps (mean radiant temperature RMSE 4.21 C, R2 0.93 versus 11.80 C / 0.44 for black-globe).
- **Why this code:** the risk-map output depends on several weather variables and the geometric twin simultaneously, so Fused.

**Confidence (AC3):** High - the SOLWEIG coupling is explicit.
(full-text source: Endnote)
