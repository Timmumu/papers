# Geng et al. (2025) — Integrating multi-source data for life-cycle risk assessment of bridge networks: a system digital twin framework

- **ID:** 3979 | **Source:** Web of Science | **DOI:** 10.1186/s43065-025-00121-7
- **Journal:** JOURNAL OF INFRASTRUCTURE PRESERVATION AND RESILIENCE
- **Authors:** Geng, Z. H.; Zhang, C.; Jiang, Y. S.; Pugliese, D.; Cheng, M. H.

## Abstract summary
Bridges are critical infrastructure assets that face a variety of stressors throughout their service life, requiring a life-cycle approach to assess their risk profile. Recent advancements in sensing and monitoring technologies provide a powerful data foundation to improve the accuracy of life-cycle risk assessment (LCRA). However, existing works that incorporate data for probabilistic risk assessment typically focus on individual bridges and rely on single-source data, limiting their scope and applicability. To this end, a system digital twin (SDT) framework based on Bayesian network (BN) is proposed to integrate multi-source data for LCRA of bridge networks. Specifically, the SDT can capture correlations and interdependencies across various scales, including within individual components (e.g., multiple failure modes), between components within a system (e.g., bridges along a route), an…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** BN-based system DT; multi-source data; bridge-network risk

## Step-3 Deep-Read Coding (Prompt B) — full text verified via Endnote library (front-matter DOI match)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow | 0 | 0 | 1 | Design for Safety (DfS) | Implemented | Bayesian / probabilistic | Multi (two or more data types) | Single case study | 4 | Predictive analytics / decision support |

**Key evidence (AG):** System digital twin (SDT) for life-cycle risk assessment of bridge networks: Bayesian network (BN) integrates multi-source data (NBI bridge inspections, FDOT traffic/AADT, USGS river gage) to update bridge failure risk (superstructure + scour) over time via automated Bayesian inference (indicator matrix for annual updates; network risk profile trends up as data update reduces uncertainty). Miami-Dade County case: 1,034 bridges, 6,478 nodes, 10,584 edges; 3 flexibility scenarios (new bridge, decommissioning, climate-change flood with CPT recalibration). Updating is implemented Bayesian inference — but authors state framework "has not yet been validated"; CPT refits are manual, no autonomous learning loop.

**Strength & gap filled (AH):** Proposes a Bayesian-network system digital twin for county-scale life-cycle risk assessment of bridge networks, fusing NBI inspection ratings, traffic monitoring and river gage data across 1,034 bridges, 1,261 traffic stations and 10 river gages in Miami-Dade County, with a 6,478-node, 10,584-edge graph capturing component, system and cross-system correlations for scenario-based risk updating.

**Deficiencies & future work (AI):** The framework has not yet been validated with field or laboratory tests, and its large Bayesian network demands 97,484.8 MB of memory just to store conditional probability tables, limiting practical scale-up. Future work includes custom Bayesian networks to cut computation, validation through field coring and lab testing, and adding restoration and resilience modelling.

**Fusion depth (AC1):** Fused

**Fusion evidence (AC2):**
- **Data streams:** NBI inspection ratings, AADT traffic monitoring, river-gage flow data (Miami-Dade County, 1,034 bridges).
- **Integration mechanism:** the BN is the joint inference engine - its risk output depends on inspection, traffic and gage data simultaneously, with an indicator matrix for annual updating.
- **Why this code:** one probabilistic model whose output depends on multiple data types, so Fused.

**Confidence (AC3):** High.