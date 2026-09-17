# Luleci et al. (2024) — Community Twin Ecosystem for Disaster Resilient Communities

- **ID:** 3606 | **Source:** Scopus | **DOI:** 10.3390/smartcities7060137
- **Journal:** Smart Cities
- **Authors:** Luleci, F.; Sevim, A.; Ozguven, E. E.; Catbas, F. N.

## Abstract summary
Highlights: What are the main findings? COWINE captures the intricate, multidimensional, and interconnected dynamics of communities leveraging Digital Twin technology, allowing for detailed disaster resilience planning and collaboration among stakeholders. The case study in Brevard County, Florida, demonstrates COWINE’s capability as a collaborative Digital Twin-based ecosystem to identify vulnerable areas and aid in the execution of preventive and adaptive strategies in order to enhance resource allocation efficiency before, during, and after a disaster. What is the implication of the main finding? COWINE’s ability to model complex urban dynamics and support decision-making through stakeholder collaboration highlights its potential to transform community disaster resilience management, offering a scalable and transferable approach to proactive disaster planning and response. The use of …

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** Community Twin Ecosystem for disaster resilience; tornado scenarios

## Step-3 Deep-Read Coding (Prompt B) — full text verified via Endnote library (front-matter DOI match)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 1 - Digital Model | 0 | 0 | 1 | Design for Safety (DfS) | None | Digital Twin platform (no machine learning) | Multi (two or more data types) | Single case study | 3 | Other |

**Key evidence (AG):** COWINE community DT ecosystem for disaster-resilient communities built on Cities:Skylines simulation engine with integrated real-world data (Brevard County FL pilot: topography, infrastructure, traffic, transit, disaster stats, 120k simulated agents); five-dimensional DT framing; collaborative stakeholder/public use-case for tornado preparedness/response/recovery with resilience-property analysis (vulnerability, robustness, redundancy, resourcefulness). Explicitly NOT real-time: "manual data-integration process", "human-based (manual) intermittent data flow", no automated calibration (future mods); no ML and no learning loop — descriptive, simulation-based.

**Strength & gap filled (AH):** Fills the gap between conceptual community-resilience digital twins and functional visualization: COWINE uses Cities:Skylines as simulation engine integrated with real-world topography, infrastructure, economic, traffic and disaster data for a Brevard County Florida pilot region, with interactive visualizations and a tornado case study demonstrating collaborative before-during-after resilience planning among stakeholders.

**Deficiencies & future work (AI):** Data flow is not real-time but manual and intermittent, assets are uniform with no deterioration models, and there is no traffic crash or fuel consumption simulation; the tornado scenario is demonstrative rather than validated, and the authors list future work on mods for real-time data flow, deterioration tracking and empirical validation.

**Fusion depth (AC1):** Aligned

**Fusion evidence (AC2):**
- **Data streams:** Brevard County topography, infrastructure, economic, traffic, transit and disaster statistics; 120,000 simulated agents.
- **Integration mechanism:** the data are imported into one geospatially referenced simulation scene (shared spatial frame), but the paper states the integration process is manual and intermittent (human-based data flow).
- **Why this code:** sources share a spatial frame while processing stays per layer, so Aligned; torn with Co-present, Aligned was retained because the scene itself is spatially registered.

**Confidence (AC3):** Medium - manual/internittent integration is explicit; the geospatial frame is real but weakly maintained.