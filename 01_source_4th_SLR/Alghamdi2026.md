# Alghamdi, M et al. (2026) — Hazard- and Fairness-Aware Evacuation with Grid-Interactive Energy Management: A Digital-Twin Controller for Life Safety and Sustainability

- **ID:** R263 | **Source:** Scopus | **DOI:** 10.3390/su18010133
- **Journal:** Sustainability (Switzerland)
- **Authors:** Alghamdi M.; Abadleh A.; Mnasri S.; Alrashidi M.; Alkhazi I.S.; Alghamdi A.; Albelwi S.

## Abstract summary
The paper introduces a real-time digital-twin controller that manages evacuation routes while operating GEEM for emergency energy management during building fires. The system consists of three interconnected parts which include (i) a physics-based hazard surrogate for short-term smoke and temperature field prediction from sensor data (ii), a router system that manages path updates for individual users and controls exposure and network congestion (iii), and an energy management system that regulates the exchange between PV power and battery storage and diesel fuel and grid electricity to preserve vital life-safety operations while reducing both power usage and environmental carbon output. The system operates through independent modules that function autonomously to preserve operational stability when sensors face delays or communication failures, and it meets Industry 5.0 requirements thr…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** Hazard-aware evacuation DT controller; life safety

## Step-3 Deep-Read Coding (Prompt B)
| P DT-subject | Q DfS/DfQ | R codable | U Tier | V Design | W Constr | X Oper | Z DfX | AA Self-improve | AB Methodology | AC Modality | AD Validation | AE QA(0-5) | AF Cluster |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 3 - Digital Twin (bidirectional, two-way) | 0 | 0 | 1 | Design for Safety (DfS) | None | Other / Mixed | Multi (two or more data types) | Simulation | 4 | Design for Safety |

| AC1 fusion depth | AC2 fusion evidence | AC3 confidence |
|---|---|---|
| Fused | Predicted hazard fields, congestion estimates and energy states are fused in one receding-horizon routing-plus-dispatch controller. | Medium |

**Key evidence (AG):** Hazard- and fairness-aware evacuation digital-twin controller with grid-interactive emergency energy management (U Tabuk, Sustainability 2026): physics-based advection-diffusion-decay surrogate predicts smoke/temperature fields from sensor data; router manages per-user path updates with exposure caps and fairness weights for vulnerable occupants; receding-horizon energy dispatcher regulates PV/battery/diesel/grid to sustain life-safety loads; auditable policy knobs; co-simulation across layouts outperforms AI/RL baselines on T95/worst-case exposure and event energy/CO2 while meeting all constraints. Twin actively dispatches energy resources (virtual-to-physical control) -> Tier 3; co-simulation validation only; no learning loop.

*Full-text source: browser-oa*

**AH — strength & gap filled:** Jointly optimises evacuation routing fairness and emergency energy dispatch with an auditable surrogate-based controller that beats AI/RL baselines on worst-case egress and event emissions.

**AI — deficiencies & future work:** Co-simulation only (no hardware/real building); surrogate fidelity vs FDS not fully quantified; human compliance with routing guidance assumed.
