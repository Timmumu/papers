# Meschini et al. (2022) — Toward cognitive digital twins using a BIM-GIS asset management system for a diffused university

- **ID:** 3720 | **Source:** Scopus | **DOI:** 10.3389/fbuil.2022.959475
- **Journal:** Frontiers in Built Environment
- **Authors:** Meschini, S.; Pellegrini, L.; Locatelli, M.; Accardo, D.; Tagliabue, L. C.; Di Giuda, G. M.; Avena, M.

## Abstract summary
The integrated use of building information modeling (BIM) and geographic information system (GIS) is promising for the development of asset management systems (AMSs) for operation and maintenance (O&M) in smart university campuses. The combination of BIM-GIS with cognitive digital twins (CDTs) can further facilitate the management of complex systems such as university building stock. CDTs enable buildings to behave as autonomous entities, dynamically reacting to environmental changes. Timely decisions based on the actual conditions of buildings and surroundings can be provided, both in emergency scenarios or when optimized and adaptive performances are required. The research aims to develop a BIM-GIS-based AMS for improving user experience and enabling the optimal use of resources in the O&M phase of an Italian university. Campuses are complex assets, mainly diffused with buildings sprea…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** BIM-GIS AMS toward cognitive DTs; fire crowd-simulation safety

## Step-3 Deep-Read Coding (Prompt B) — full text verified via Endnote library (front-matter DOI/title match, coverage re-scan 2026-08-12)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 1 - Digital Model | 0 | 0 | 1 | Design for Safety (DfS) | Mentioned only | Digital Twin platform (no machine learning) | Multi (two or more data types) | Cross-project (multiple real projects) | 3 | BIM-to-Digital-Twin architecture |

**Key evidence (AG):** BIM-GIS-based asset management system (AMS app) for the diffused University of Turin campus (two demonstrator buildings): web platform with interactive 3D map + analytical dashboards for real-time visualization of the asset stock from a centralized database integrating spatial/functional data; crowd simulations (Pathfinder-style) assess fire-emergency safety and evacuation time as a benchmark; cognitive digital twins are framed as the long-term future objective — no live sensor/IoT data flow yet (sensor deployment and ML-based automated analysis are future work). Static visualisation platform toward future CDTs; one-way, no learning loop.

**Strength & gap filled (AH):** Addresses fragmented document-based management of a diffused university asset: a BIM-GIS web platform integrates spatial and functional data from several directorates into a centralized relational database with a tailor-made space encoding, feeding an interactive 3D map with analytical dashboards for two University of Turin demonstrator buildings, plus crowd simulation to assess fire evacuation safety levels.

**Deficiencies & future work (AI):** No IoT sensors or live data feed the app yet, formats remain authoring-based rather than open standards, and no AI or ML processing exists, so the cognitive digital twin is aspirational; future work includes IoT networks, AI and AR/VR integration, whole-asset fire risk mapping and active wayfinding for evacuation.

**Fusion depth (AC1):** Aligned

**Fusion evidence (AC2):**
- **Data streams:** BIM spatial data + GIS/functional data from several directorates (two University of Turin demonstrators).
- **Integration mechanism:** the centralised relational database with space encoding provides the shared frame for the 3D map and dashboards; Pathfinder-style crowd simulation assesses evacuation safety separately.
- **Why this code:** data types share one spatial frame with per-type services, so Aligned.

**Confidence (AC3):** High - the centralised DB integration is explicit.