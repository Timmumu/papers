# Ellul, C et al. (2024) — Exploring Data for Construction Digital Twins: Building Health and Safety and Progress Monitoring Twins Using the Unreal Gaming Engine

- **ID:** R621 | **Source:** Scopus | **DOI:** 10.3390/buildings14072216
- **Journal:** Buildings
- **Authors:** Ellul C.; Hamilton N.; Pieri A.; Floros G.

## Abstract summary
Although digital twins have been established in manufacturing for a long time, they are only more recently making their way into the urban environment and present a relatively new concept for the construction industry. The concept of a digital twin—a model of the physical environment that has a real-time two-way link between the physical and the digital, with the virtual model changing over time to reflect changes in the real world—lends itself well to the continually changing environment of a construction project. Predictive capabilities built into a twin also have great potential for construction planning—including in supply chain management and waste disposal as well as in the construction process itself. Underpinning this opportunity is location data, which model where something is happening and when and can be used to solve a wide range of problems. In particular, location (the powe…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** Unreal Engine twins for H&S and progress monitoring


## Step-3 Deep-Read Coding (Prompt B)
| P DT-subject | Q DfS/DfQ | R codable | U Tier | V Design | W Constr | X Oper | Z DfX | AA Self-improve | AB Methodology | AC Modality | AD Validation | AE QA(0-5) | AF Cluster |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 3 - Digital Twin (bidirectional, two-way) | 0 | 1 | 0 | Design for Safety (DfS) | None | Digital Twin platform (no machine learning) | Multi (two or more data types) | Cross-project (multiple real projects) | 3 | BIM-to-Digital-Twin architecture |

| AC1 fusion depth | AC2 fusion evidence | AC3 confidence |
|---|---|---|
| Aligned | Location-enabled twins georeference diverse data sources through CesiumJS and place them in Unreal Engine scenes, linking hazard boxes and asset inspection records to site coordinates. | High |

**Key evidence (AG):** Construction digital twin demonstrators (health & safety + progress monitoring) using Unreal Gaming Engine + CesiumJS mapping on a highway project (Skanska/UCL): location data integrates diverse sources; no-code approach for DT development; two case studies demonstrate 4D data presentation; explicitly described as human-in-the-loop DT (two-way communication with manual decision making) — virtual model changes reflect real-world changes, and humans act back on the physical site via decisions. Predictive capabilities discussed but not implemented; no learning loop.

*Full-text source: 04c-port*

**AH — strength & gap filled:** Demonstrates location-enabled construction digital twins on a live Skanska highway project, building health and safety and progress monitoring twins in Unreal Engine 5 with CesiumJS georeferencing. The health and safety twin delivers site walk-throughs, clickable asset inspection records, color-coded hazard and risk boxes, and 1-metre danger-zone alerts around machinery built with no-code Blueprints.

**AI — deficiencies & future work:** The prototypes are proof of concept: only a small subset of live sensor data was explored, no analytics or prediction were incorporated, asset placement was manual with positional errors up to 1 metre, and no formal usability tests were run. Future work includes automated progress quantification, live worker tracking with wearables, analytics, data security and Datasmith scalability trials.
