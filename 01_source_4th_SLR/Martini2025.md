# Martini, T et al. (2025) — Digital twin representation of socio-technical systems through a distributed co-simulation approach for crisis management

- **ID:** R062 | **Source:** Scopus | **DOI:** 10.1007/s10669-025-10035-0
- **Journal:** Environment Systems and Decisions
- **Authors:** Martini T.; Boigk M.; Catal F.; Dietze S.; Gerold M.; Lukau E.; Monteforte M.; Neuhäuser S.; Peitzsch S.; Phung W.; Pfennigschmidt S.; Simon M.; Vetter J.Z.; Winter N.; Adams G.; Finger J.; Rosin J.

## Abstract summary
The increasing frequency and severity of significant risks to public safety posed by natural disasters or human-induced events have underscored a critical need for evaluating the vulnerability of urban regions with a focus on their essential infrastructures. This paper presents a novel methodology for the virtual representation of infrastructure vulnerabilities and functional impairments during hazard situations. Thereby, focus is on the mapping of interdependencies among critical infrastructure systems and the cascading effects that can arise from failures within these heterogeneous sectors by means of a digital twin representation. An integration of simulation models for urban infrastructure components, particularly in relation to the built environment and emergency response systems is introduced. Leveraging a modular co-simulation architecture, the framework facilitates the analysis o…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** Urban DT co-simulation for crisis management

## Step-3 Deep-Read Coding (Prompt B)
| P DT-subject | Q DfS/DfQ | R codable | U Tier | V Design | W Constr | X Oper | Z DfX | AA Self-improve | AB Methodology | AC Modality | AD Validation | AE QA(0-5) | AF Cluster |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 1 - Digital Model (static, no live data) | 0 | 0 | 1 | Design for Safety (DfS) | None | Other / Mixed | Multi (two or more data types) | Simulation | 3 | Predictive analytics / decision support |

| AC1 fusion depth | AC2 fusion evidence | AC3 confidence |
|---|---|---|
| Fused | Sector simulation outputs (water/electricity/gas/telecom, buildings, emergency response) are exchanged as events in one co-simulation to compute cascading effects; modules remain loosely coupled simulators rather than a single fused model. | Medium |

**Key evidence (AG):** Digital urban twin for crisis management via modular distributed co-simulation (Fraunhofer SIRIOS): engineering-model simulation modules for water, electricity, gas, telecom, built environment and agent-based emergency response exchange events over a CloudEvents/FROST (SensorThings) event-stream architecture; mapping interdependencies and cascading failures among critical infrastructures; proof-of-concept on urban flooding/heavy-rainfall scenario predicting system states and structural impacts for authorities and training. Scenario-driven co-simulation; no live sensor loop demonstrated, no actuation, no learning loop.

*Full-text source: Endnote*

**AH — strength & gap filled:** Fills the gap between single-sector simulations and real crisis management: a modular event-stream co-simulation maps interdependencies and cascading effects across water, electricity, gas, telecom, built environment and emergency response in one urban digital twin, demonstrated on an urban flooding proof-of-concept for authorities and training.

**AI — deficiencies & future work:** Proof-of-concept covers only a flooding scenario; no live sensor ingestion or real-time operation demonstrated, validation against real crisis data is missing, and assumptions on initial conditions and monitoring availability limit accuracy for large-scale cascading failures.
