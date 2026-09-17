# Ugliotti et al. (2025) — Spatial Insights for Building Resilience: The Territorial Risk Management & Analysis Across Scale Framework for Bridging Scales in Multi-Hazard Assessment

- **ID:** 3836 | **Source:** Scopus | **DOI:** 10.3390/smartcities8010027
- **Journal:** Smart Cities
- **Authors:** Ugliotti, F. M.; Daud, M.; Iacono, E.

## Abstract summary
Highlights: What are the main findings? The TERIMAAS framework successfully integrates BIM, GIS, and IoT data to enhance multi-hazard risk assessment, bridging scales from territorial impacts to individual structures. A public building case study in a critical natural hazards area in northwest Italy demonstrates real-time flood risk assessment to improve resilience and disaster management strategies. What is the implication of the main finding? The scalable approach equips different types of stakeholders with actionable insights for enhancing critical infrastructure resilience against evolving environmental risks. Policy-makers and asset managers gain a dynamic decision-making tool, fostering proactive disaster preparedness and optimised resource allocation. In an era of increasingly abundant and granular spatial and temporal data, the traditional divide between environmental GIS and bui…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** TERIMAAS BIM+GIS+IoT multi-hazard framework; flood risk of building

## Step-3 Deep-Read Coding (Prompt B)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow (one-way physical to virtual) | 0 | 0 | 1 | Design for Safety (DfS) | None | Digital Twin platform (no machine learning) | Multi (two or more data types) | Single case study | 4 | Lifecycle / governance |

**Key evidence (AG):** TERIMAAS framework for territorial risk management and analysis across scale (Politecnico di Torino): centralized PostGIS repository harmonizes BIM + GIS + IoT data; real-time IoT-derived information updates vulnerability and risk scores; GIS spatial analysis assesses risk scores for each hazard type; BIM data refines assessment with building/functional characteristics; flood risk case study in northwest Italy; dynamic risk assessments adapt to changing conditions. One-way monitoring→risk assessment→decision support; no actuation and no learning loop (risk scores are rule-based, not learning).


**Strength & gap filled (AH):** Bridges the GIS-territorial to BIM-building scale divide for multi-hazard assessment: the TERIMAAS framework centralizes BIM, GIS, and real-time IoT streams in a PostGIS repository that dynamically updates hazard, vulnerability, and risk scores, demonstrated on a flood risk case study of a public building in northwest Italy, giving stakeholders near real-time territorial and building-level risk views.

**Deficiencies & future work (AI):** Demonstrates only flood risk on one public building, so transfer to other hazards and regions is unproven; the approach needs substantial data infrastructure and expertise, and the centralized repository raises privacy, security, and single-point-of-failure concerns. Future work includes decentralized storage, multi-hazard modules, open-source BIM tooling, and AI-based extreme-event forecasting.
**Fusion depth (AC1):** Fused

**Fusion evidence (AC2):**
- **Data streams:** BIM building data + GIS territorial layers + real-time IoT information (flood case, northwest Italy).
- **Integration mechanism:** the centralized PostGIS repository updates hazard, vulnerability and risk scores from all three sources, giving stakeholders near-real-time territorial and building-level risk views.
- **Why this code:** risk-score outputs depend on the three data types simultaneously, so Fused (beyond shared storage per rule 3).

**Confidence (AC3):** Medium - the score-update mechanism is explicit, but the computation is rule-based and single-hazard.
(full-text source: Endnote)
