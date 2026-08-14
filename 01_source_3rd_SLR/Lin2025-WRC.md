# Lin et al. (2025) — Digital twin-enabled safety monitoring system for seamless worker-robot collaboration in construction

- **ID:** 3974 | **Source:** Web of Science | **DOI:** 10.1016/j.autcon.2025.106147
- **Journal:** AUTOMATION IN CONSTRUCTION
- **Authors:** Lin, X.; Guo, Z. Y.; Jin, X. X.; Guo, H. L.

## Abstract summary
Worker-robot collaboration (WRC) has emerged as a transformative approach to augmenting the productivity of the construction industry. However, the development of a safety monitoring method or system for stopping robot operations in emergency is imperative, especially for seamless WRC on site. This paper presents a digital twinenabled safety monitoring system for seamless WRC on site, characterized by its comprehensive perception of dynamic entities and dynamic calculation of protective separation distances during seamless WRC. The effectiveness of the proposed system is substantiated through a series of experiments, the result demonstrates its proficiency in mitigating collisions during robot operation in both static and dynamic WRC scenarios. The system achieves an average monitoring rate of 9.8 frames per second, an average reaction latency of 0.177 s, and a positional perception erro…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** DT safety monitoring for worker-robot collaboration; collision mitigation

## Step-3 Deep-Read Coding (Prompt B) — full text verified via Endnote library (front-matter DOI/title match, coverage re-scan 2026-08-12)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 3 - Digital Twin (bidirectional) | 0 | 1 | 0 | Design for Safety (DfS) | None | Perception / Computer Vision | Multi (two or more data types) | Single case study | 4 | Design for Safety |

**Key evidence (AG):** DT-enabled safety monitoring system for seamless worker-robot collaboration (Tsinghua U): depth camera + LiDAR perceive workers/robots/materials → geometric-solid virtual representations in a digital twin; computes separation distance (SD) and dynamic protective separation distance (PSD, per ISO 15066/13855); when SD exceeds PSD the system "accesses the physical actuators of robots to stop it" — explicit virtual→physical control (emergency stop). Experiments: 9.8 FPS, 0.177 s reaction latency, 0.09 m perception error, static+dynamic scenarios. No ML used and no learning loop (predictive motion methods are future work).
