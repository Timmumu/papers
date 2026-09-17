# Stergiopoulos et al. (2025) — Enhancing Urban Heatwave Response Planning via a Graph-Based Digital Twin Approach: Spatial Dependency Risk Analysis in Vienna City

- **ID:** 3768 | **Source:** Scopus | **DOI:** 10.1109/ACCESS.2025.3580334
- **Journal:** IEEE Access
- **Authors:** Stergiopoulos, G.; Leventopoulos, S. A.; Karamousadakis, M.; Schuster, B.; Gritzalis, D.

## Abstract summary
Urban heatwaves pose an escalating threat to cities, requiring advanced planning strategies. This paper presents a graph-based digital twin approach to model spatial dependencies in heatwave risk for urban areas. Using Vienna’s city center as a case study, we integrate (i) high-resolution spatial data from Google on heat hazard, (ii) spatial population distribution from Vienna Open Data and (iii) META’s Vienna population datasets alongside (iv) critical road infrastructure from OpenStreetMaps, into a graph network model that captures cumulative risk paths that help determine the most critical city blocks needing intervention and the optimal allocation of resources for routing first responders to reach critical locations of sensitive populations. Our Spatial Dependency Risk Analysis identifies how the distribution of vulnerable population needing first aid in one location together with he…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** Graph-based DT for heatwave risk & first-responder routing; Vienna

## Step-3 Deep-Read Coding (Prompt B) — full text verified via Endnote library (front-matter DOI/title match, coverage re-scan 2026-08-12)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow | 0 | 0 | 1 | Design for Safety (DfS) | None | Graph Neural Network (GNN) | Multi (two or more data types) | Single case study | 4 | Predictive analytics / decision support |

**Key evidence (AG):** Graph-based digital twin for urban heatwave response planning (Vienna city center, Horizon PANTHEON): integrates Google Solar API real-time heat-index data + spatial population distribution/vulnerability (Vienna Open Data, META) + critical road infrastructure (OpenStreetMap) into a graph network model; Spatial Dependency Risk Analysis captures cumulative risk paths, identifies critical junctions (e.g., node 683 "cold spot") and automatically plans ambulance/first-responder routes from cooling spots to high-risk hotspots (<=15 min patrol). One-way planning/decision-support tool; graph-based dependency analysis (no ML training loop), no actuation and no learning loop; future work adds real-time data and transfer to other cities.

**Strength & gap filled (AH):** Extends GIS-based heatwave vulnerability mapping into a graph-based urban digital twin: Google Solar API heat-index data, Vienna open population datasets and OpenStreetMap roads are fused into a dependency-risk graph whose centrality analysis identifies cumulative risk paths and critical blocks, including cold-spot node 683, and plans first-responder ambulance routes from cooling spots to high-risk populations, with sensitivity checks showing Spearman correlations near 0.8.

**Deficiencies & future work (AI):** The tool supports planning rather than real-time emergency operations, with no live sensor feeds, no actuation, and validation limited to Vienna city center; the authors plan alignment with EU regulations including NIS2, integration of Copernicus real-time streams, downscaled or locally calibrated solar data, and extension to compound events such as power outages and floods.

**Fusion depth (AC1):** Fused

**Fusion evidence (AC2):**
- **Data streams:** Google Solar API heat-index data + Vienna Open Data population/vulnerability + OpenStreetMap critical roads.
- **Integration mechanism:** the three sources are fused into a spatial dependency-risk graph; centrality analysis identifies cumulative risk paths and critical junctions (node 683 cold spot) and plans ambulance routes from cooling spots to hotspots.
- **Why this code:** the graph is a joint representation whose analyses depend on all sources simultaneously, so Fused.

**Confidence (AC3):** High - the graph fusion is explicit.