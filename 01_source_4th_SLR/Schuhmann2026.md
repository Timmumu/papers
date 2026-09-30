# Schuhmann, F et al. (2026) — Tackling the Complexity of Emergency Response Systems: Creating Transport-Focused Digital Twins

- **ID:** R308 | **Source:** Scopus | **DOI:** 10.3390/smartcities9020036
- **Journal:** Smart Cities
- **Authors:** Schuhmann F.; Sturm M.; Zacher T.; Lienkamp M.

## Abstract summary
Highlights: What are the main findings? The proposed framework builds transport-focused digital twins of emergency response systems, combining multiple data sources. The combination of real-time traffic data, GPS data from emergency vehicles (EVs), and road network information enables precise network analysis, e.g., identifying bottlenecks where EVs are affected by traffic. Our data shows that more favorable traffic conditions and more spacious road structures are positively associated with improved EV progress in urban environments. The agent-based, mesoscopic model of the Munich Fire Department shows good results in validation compared to historical incident data. What is the implication of the main finding? Digital twins can be used to assess the impact of the transport system on the emergency response system and to systematically simulate future ‘what-if’ scenarios. Our data suggests…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** Emergency-response transport DT; what-if safety scenarios

## Step-3 Deep-Read Coding (Prompt B)
| P DT-subject | Q DfS/DfQ | R codable | U Tier | V Design | W Constr | X Oper | Z DfX | AA Self-improve | AB Methodology | AC Modality | AD Validation | AE QA(0-5) | AF Cluster |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow (one-way physical to virtual) | 0 | 0 | 1 | Design for Safety (DfS) | None | Agent-based model (ABM) | Multi (two or more data types) | Single case study | 4 | Predictive analytics / decision support |

| AC1 fusion depth | AC2 fusion evidence | AC3 confidence |
|---|---|---|
| Fused | Real-time traffic speed, EV GPS and road-network data are fused in the regression/criticality indicator feeding the ABM. | High |

**Key evidence (AG):** Transport-focused digital twin of emergency response systems (TUM, Smart Cities 2026): combines real-time traffic data, emergency-vehicle GPS trajectories and road-network information; regression of EV speed on traffic speed plus a combined criticality indicator identifies bottleneck edges; agent-based mesoscopic model of the Munich Fire Department calibrated on recorded trajectories and validated against historical incident data; what-if scenarios for mobility-transition planning. One-way data->analysis->planning support; no actuation, no learning loop.

*Full-text source: browser-oa*

**AH — strength & gap filled:** Links real-time traffic with EV GPS to pinpoint bottlenecks and a validated agent-based Munich Fire Department model, enabling evidence-based what-if planning for the mobility transition.

**AI — deficiencies & future work:** Single city case; EV fleet penetration limited; agent model mesoscopic; recommendations for action explicitly deferred pending more data.
