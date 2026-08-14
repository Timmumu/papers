# Rashidian et al. (2026) — An IFC-based framework for semantic integration of BIM and mobile crowd sensing in real-time evacuation routing

- **ID:** 3892 | **Source:** Web of Science | **DOI:** 10.1016/j.aei.2026.104500
- **Journal:** ADVANCED ENGINEERING INFORMATICS
- **Authors:** Rashidian, M.; Malek, M. R.

## Abstract summary
Emergency evacuation in complex buildings benefits from tight coupling between digital building representations and real-time operational data. While Building Information Modeling (BIM) provides semantically rich indoor descriptions, many evacuation systems still treat sensing technologies and BIM as isolated components, resulting in static or weakly adaptive routing behavior. This paper proposes an IFC-based integration framework that establishes semantic interoperability between BIM entities and mobile crowd sensing (MCS) data to enable real-time, context-aware evacuation routing. IFC models are transformed into a dynamic decision graph in which spaces, exits, and sensors are continuously annotated with live crowd-sensed information. Occupant positions are estimated using Wi-Fi-based indoor localization supported by a two-stage crowdsensing strategy that accounts for both active and si…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** IFC+MCS real-time evacuation routing; DT-like emergency management

## Step-3 Deep-Read Coding (Prompt B)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow (one-way physical to virtual) | 0 | 0 | 1 | Design for Safety (DfS) | None | Ontology / semantic | Multi (two or more data types) | Single case study | 4 | Predictive analytics / decision support |

**Key evidence (AG):** IFC-based framework for semantic integration of BIM and mobile crowd sensing in real-time evacuation routing (KNTU): IFC models transformed into dynamic decision graph with spaces/exits/sensors annotated by live crowd-sensed info; Wi-Fi-based indoor localization with two-stage crowdsensing; multi-criteria shortest-path routing via extended Dijkstra with dynamically updated weights (distance to hazards, travel time, exit availability, route safety index); AHP weight prioritization; implemented in four-story academic building. One-way monitoring→routing guidance; no actuation and no learning loop (Dijkstra is algorithmic, not learning).
(full-text source: Endnote)
