# Laksono, N.B et al. (2026) — A knowledge-based approach to UAV path planning for bridge maintenance in a digital twin environment

- **ID:** R246 | **Source:** Scopus | **DOI:** 10.1016/j.knosys.2026.116950
- **Journal:** Knowledge-Based Systems
- **Authors:** Laksono N.B.; Latief Y.; Trigunarsyah B.; Sunkuk K.; Suaryana N.

## Abstract summary
Unmanned aerial vehicles (UAVs) are increasingly used for bridge inspection to reduce hazardous access and improve scalability. Routes are often manual or coverage-driven, and the collected imagery is not always comparable or aligned with maintenance decision needs. This study proposes a knowledge-based UAV path planning approach that converts maintenance intent into executable and repeatable inspection routes. The method integrates element-level maintenance knowledge from field inspection and maintenance records encoded as priority weights and viewing requirements with BIM derived bridge geometry to generate candidate viewpoints and element specific inspection patterns for substructure and superstructure. Viewpoints are evaluated using a maintenance-weighted utility function. A case study on a conventional concrete box-girder toll-road bridge compares the approach with three baselines m…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** Knowledge-based UAV planning in bridge DT; maintenance safety

## Step-3 Deep-Read Coding (Prompt B)
| P DT-subject | Q DfS/DfQ | R codable | U Tier | V Design | W Constr | X Oper | Z DfX | AA Self-improve | AB Methodology | AC Modality | AD Validation | AE QA(0-5) | AF Cluster |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 1 - Digital Model (static, no live data) | 0 | 0 | 1 | Design for Safety (DfS) | None | Ontology / semantic | Multi (two or more data types) | Single case study | 3 | Design for Safety |

| AC1 fusion depth | AC2 fusion evidence | AC3 confidence |
|---|---|---|
| Fused | Maintenance priority weights and BIM geometry are fused in the maintenance-weighted viewpoint utility function. | Medium |

**Key evidence (AG):** Knowledge-based UAV path planning in a digital-twin environment (U Indonesia/RMIT/Kyung Hee, Knowledge-Based Systems 2026 preprint): maintenance records encoded as element-level priority weights and viewing requirements; BIM-derived geometry generates candidate viewpoints and element-specific patterns; maintenance-weighted utility evaluates routes; box-girder toll-road bridge case compares favourably against manual, coverage-only and robustness-proxy baselines with cycle-to-cycle repeatability. Static BIM+knowledge planning (no live link); no actuation, no learning loop; preprint not peer-reviewed.

*Full-text source: browser-oa*

**AH — strength & gap filled:** Converts maintenance intent into repeatable UAV routes via knowledge-encoded priority weights and BIM geometry, outperforming coverage-only and robustness-proxy baselines.

**AI — deficiencies & future work:** Preprint (not peer-reviewed); single case study; UAV feasibility (battery, GNSS denial under decks) treated lightly; no field flight validation.
