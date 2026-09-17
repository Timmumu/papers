# Luleci, F et al. (2024) — Community Twin Ecosystem for Disaster Resilient Communities

- **ID:** R767 | **Source:** Scopus | **DOI:** 10.3390/smartcities7060137
- **Journal:** Smart Cities
- **Authors:** Luleci F.; Sevim A.; Ozguven E.E.; Catbas F.N.

## Abstract summary
Highlights: What are the main findings? COWINE captures the intricate, multidimensional, and interconnected dynamics of communities leveraging Digital Twin technology, allowing for detailed disaster resilience planning and collaboration among stakeholders. The case study in Brevard County, Florida, demonstrates COWINE’s capability as a collaborative Digital Twin-based ecosystem to identify vulnerable areas and aid in the execution of preventive and adaptive strategies in order to enhance resource allocation efficiency before, during, and after a disaster. What is the implication of the main finding? COWINE’s ability to model complex urban dynamics and support decision-making through stakeholder collaboration highlights its potential to transform community disaster resilience management, offering a scalable and transferable approach to proactive disaster planning and response. The use of …

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** Community twin ecosystem for disaster-resilient communities


## Step-3 Deep-Read Coding (Prompt B)
| P DT-subject | Q DfS/DfQ | R codable | U Tier | V Design | W Constr | X Oper | Z DfX | AA Self-improve | AB Methodology | AC Modality | AD Validation | AE QA(0-5) | AF Cluster |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 1 - Digital Model (static, no live data) | 0 | 0 | 1 | Design for Safety (DfS) | None | Digital Twin platform (no machine learning) | Multi (two or more data types) | Single case study | 3 | Other |

| AC1 fusion depth | AC2 fusion evidence | AC3 confidence |
|---|---|---|
| Aligned | Real-world topography, infrastructure, traffic, transit and disaster data are manually integrated into one georeferenced Cities:Skylines simulation scene, with no automated calibration or live link. | Medium |

**Key evidence (AG):** COWINE community DT ecosystem for disaster-resilient communities built on Cities:Skylines simulation engine with integrated real-world data (Brevard County FL pilot: topography, infrastructure, traffic, transit, disaster stats, 120k simulated agents); five-dimensional DT framing; collaborative stakeholder/public use-case for tornado preparedness/response/recovery with resilience-property analysis (vulnerability, robustness, redundancy, resourcefulness). Explicitly NOT real-time: "manual data-integration process", "human-based (manual) intermittent data flow", no automated calibration (future mods); no ML and no learning loop — descriptive, simulation-based.

*Full-text source: 04c-port*

**AH — strength & gap filled:** Fills the gap between conceptual community-resilience digital twins and functional visualization: COWINE uses Cities:Skylines as simulation engine integrated with real-world topography, infrastructure, economic, traffic and disaster data for a Brevard County Florida pilot region, with interactive visualizations and a tornado case study demonstrating collaborative before-during-after resilience planning among stakeholders.

**AI — deficiencies & future work:** Data flow is not real-time but manual and intermittent, assets are uniform with no deterioration models, and there is no traffic crash or fuel consumption simulation; the tornado scenario is demonstrative rather than validated, and the authors list future work on mods for real-time data flow, deterioration tracking and empirical validation.
