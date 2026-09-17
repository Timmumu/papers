# Han et al. (2026) — Construction Path of Shanghai Oriental Hub Municipal Pipeline Full Cycle Digital Twin Platform

- **ID:** 3926 | **Source:** Web of Science | **DOI:** 10.1155/adce/8916300
- **Journal:** ADVANCES IN CIVIL ENGINEERING
- **Authors:** Han, F.; An, Y. J.

## Abstract summary
In view of the current status and main problems of the construction of municipal pipelines in Shanghai Oriental Hub, based on the digital twin technology, this paper proposes and constructs a full-cycle digital twin platform for municipal pipelines in the digital era, and discusses the implementation path of the platform construction. On the premise of clarifying the planning and management mechanism of underground pipelines, based on the establishment of a data standard system and safety control scheme, based on building information modeling, IoT perception, artificial intelligence, and other technologies, the deep integration of municipal pipelines and digital twin technology in the whole life cycle of planning, construction, operation and maintenance (O&M) is promoted, which plays an important role in promoting the intensive and efficient construction and safe operation of municipal p…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** Full-cycle municipal pipeline DT platform; safe operation focus

## Step-3 Deep-Read Coding (Prompt B) — full text verified via Endnote library (front-matter DOI/title match, coverage re-scan 2026-08-12)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow | 1 | 1 | 1 | Both | None | Other / Mixed | Multi (two or more data types) | Single case study | 4 | Lifecycle / governance |

**Key evidence (AG):** Full-cycle municipal pipeline DT platform (Shanghai Oriental Hub): BIM0–BIM6 full-phase connection + lightweight BIM-GIS, 28 IoT sensing nodes (water pressure, gas leakage, surface temp, <1 s delay) with 5-month pilot; addresses planning collision risks, construction rework, and delayed leakage detection; AI risk model predicted a valve aging risk 7 days in advance (verified on-site); 36.4% O&M cost reduction. One-way IoT→platform monitoring/decision support, no actuation and no self-improvement loop.

**Strength & gap filled (AH):** Fills the gap between macro city-level twin frameworks and single-phase pipeline platforms with a full-cycle BIM0 to BIM6 plus lightweight BIM-GIS architecture for the Shanghai Oriental Hub; a 5-month pilot deployed 28 IoT nodes (pressure, gas leakage, surface temperature) with under 1 s delay, raising planning collision detection from 68 to 97 percent and predicting one valve aging risk 7 days in advance.

**Deficiencies & future work (AI):** The pilot covers only water supply and gas pipelines, lacking power and communication monitoring modules, and its data is not yet connected to Pudong Airport systems for cross-node emergency linkage; multi-type pipeline adaptability and cross-departmental data interface standards are stated as future work.

**Fusion depth (AC1):** Aligned

**Fusion evidence (AC2):**
- **Data streams:** 28 IoT nodes (pressure, gas leakage, surface temperature, under-1-s delay) + BIM0-BIM6 lifecycle models on a 5-month Shanghai Oriental Hub pilot.
- **Integration mechanism:** sensors are linked to BIM-GIS assets for monitoring and display; the AI risk model predicted one valve aging risk 7 days ahead, but no joint multi-stream inference is described.
- **Why this code:** streams share the BIM-GIS asset frame while inference stays per asset, so Aligned (downgrade from Fused per rule 5).

**Confidence (AC3):** Medium - platform linkage is clear; joint processing is not stated.