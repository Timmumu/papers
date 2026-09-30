# Milašinović, M et al. (2023) — Failure Conditions Assessment of Complex Water Systems Using Fuzzy Logic

- **ID:** R624 | **Source:** Scopus | **DOI:** 10.1007/s11269-022-03420-w
- **Journal:** Water Resources Management
- **Authors:** Milašinović M.; Ivetić D.; Stojković M.; Savić D.

## Abstract summary
Climate change, energy transition, population growth and other natural and anthropogenic impacts, combined with outdated (unfashionable) infrastructure, can force Dam and Reservoir Systems (DRS) operation outside of the design envelope (adverse operating conditions). Since there is no easy way to redesign or upgrade the existing DRSs to mitigate against all the potential failure situations, Digital Twins (DT) of DRSs are required to assess system’s performance under various what-if scenarios. The current state of practice in failure modelling is that failures (system’s not performing at the expected level or not at all) are randomly created and implemented in simulation models. That approach helps in identifying the riskiest parts (subsystems) of the DRS (risk-based approach), but does not consider hazards leading to failures, their occurrence probabilities or subsystem failure exposure.…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** DT failure assessment of dam and reservoir systems

## Step-3 Deep-Read Coding (Prompt B)
| P DT-subject | Q DfS/DfQ | R codable | U Tier | V Design | W Constr | X Oper | Z DfX | AA Self-improve | AB Methodology | AC Modality | AD Validation | AE QA(0-5) | AF Cluster |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 1 - Digital Model (static, no live data) | 0 | 0 | 1 | Design for Safety (DfS) | None | Other / Mixed | Multi (two or more data types) | Single case study | 3 | Predictive analytics / decision support |

| AC1 fusion depth | AC2 fusion evidence | AC3 confidence |
|---|---|---|
| Fused | Hazard severity and subsystem reliability are fused via fuzzy logic into the SD model failure simulation. | Medium |

**Key evidence (AG):** Fuzzy-logic failure scenario generator coupled with a system dynamics (SD) model for dam and reservoir system digital twins (Water Resources Management 2023): causal failure generation uses hazard severity and subsystem reliability as fuzzy inputs, producing failure magnitudes on a normalized scale; coupled failure-implementation framework is generic for any DRS; 10-year simulation of the Pirot DRS (Serbia) shows rare hazards + outdated infrastructure can cut performance by 50%, revealing hidden failure risks and supporting maintenance prioritization. Offline what-if simulation (no live data link).

*Full-text source: browser-oa*

**AH — strength & gap filled:** Causal fuzzy failure generator overcomes random-failure practice in dam-reservoir DTs and exposes hidden failure risks (50% performance drop in the Pirot case).

**AI — deficiencies & future work:** SD model fidelity not quantified; fuzzy rules expert-derived; only one DRS case and offline simulation.
