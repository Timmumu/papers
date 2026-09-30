# Stylianou, M et al. (2026) — Disaster evacuation of the old city of Nicosia

- **ID:** R310 | **Source:** Scopus | **DOI:** 10.1016/j.pdisas.2026.100557
- **Journal:** Progress in Disaster Science
- **Authors:** Stylianou M.; Demetriou M.; Aristidou A.

## Abstract summary
Historic urban centers face unique evacuation challenges due to dense morphology, limited network redundancy, and cultural heritage constraints that restrict infrastructural modification. This study presents an exploratory, decision-support analysis of evacuation dynamics in the walled Old Town of Nicosia, Cyprus, using a high-fidelity digital twin and a hybrid agent-based simulation framework integrating pedestrian and vehicular movement. Rather than modeling a specific hazard, the study evaluates how structural stressors commonly produced by disasters, including exit closures, road blockages, and shelter saturation, influence evacuation clearance, congestion formation, and overall system robustness. Controlled simulation experiments examine the sensitivity of evacuation performance to network disruptions, the effectiveness of existing and expanded shelter configurations, and the role o…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** Nicosia old-town evacuation DT; disaster safety

## Step-3 Deep-Read Coding (Prompt B)
| P DT-subject | Q DfS/DfQ | R codable | U Tier | V Design | W Constr | X Oper | Z DfX | AA Self-improve | AB Methodology | AC Modality | AD Validation | AE QA(0-5) | AF Cluster |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 1 - Digital Model (static, no live data) | 0 | 0 | 1 | Design for Safety (DfS) | None | Agent-based model (ABM) | Multi (two or more data types) | Simulation | 4 | Design for Safety |

| AC1 fusion depth | AC2 fusion evidence | AC3 confidence |
|---|---|---|
| Fused | Spatial geometry, traffic counts and density observations are fused to calibrate pedestrian and vehicle agents on layered navigation meshes. | Medium |

**Key evidence (AG):** Disaster evacuation of Nicosia Old Town (U Cyprus, Progress in Disaster Science 2026): high-fidelity geo-referenced 3D digital twin of the walled city with layered pedestrian/vehicle navigation meshes (one-way restrictions, pedestrian-only segments, six gates); hybrid agent-based simulation; controlled stress experiments (gate closures, blockages, shelter saturation) reveal high sensitivity to a few critical exits and long-tailed delays; hazard-agnostic exploratory decision support. Static model + simulation; no live data link, no actuation, no learning loop.

*Full-text source: browser-oa*

**AH — strength & gap filled:** First city-scale evacuation study of a walled heritage core with six gates and a buffer zone, showing shelter expansion without adaptive guidance can worsen congestion.

**AI — deficiencies & future work:** Hazard-agnostic (no specific hazard process); simulation without real incident validation; behavioral parameters approximated from traffic counts.
