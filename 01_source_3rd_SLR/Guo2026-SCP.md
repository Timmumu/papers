# Guo et al. (2026) — AN INTELLIGENT CONSTRUCTION SYSTEM BASED ON DIGITAL TWIN AND FOUNDATION MODEL OPTIMIZATION

- **ID:** 3977 | **Source:** Web of Science | **DOI:** 10.3846/jcem.2026.26154
- **Journal:** JOURNAL OF CIVIL ENGINEERING AND MANAGEMENT
- **Authors:** Guo, F. Y.; Wang, C. C.; Sun, J.; Huang, K. X.; Wang, X.

## Abstract summary
Construction sites routinely face multi-trade concurrency, spatiotemporal coupling, and high safety risk; relying solely on manual inspection and heuristic scheduling often leads to lagging detection and inconsistent execution. In response, recent practice has introduced digital twins (DT) to fuse video, sensors, and BIM and thus improve site visibility; however, most implementations remain at monitoring/visualization, lacking a mechanism to convert cognition into executable, verifiable decisions. Meanwhile, Transformer foundation models show strong capabilities in multimodal perception and representation learning, yet they are rarely closed-looped with engineering constraints and on-site execution. Against this backdrop, taking high-rise self-climbing platform (SCP) operations as a representative scenario, we build a DT & times;Transformer closed-loop system. We align video/sensor/BIM/t…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** DT×Transformer closed-loop for SCP operations; risk prediction, AR execution

## Step-3 Deep-Read Coding (Prompt B)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 3 - Digital Twin (bidirectional, two-way) | 0 | 1 | 0 | Design for Safety (DfS) | None | Transformer / Large Language Model (LLM) | Multi (two or more data types) | Single case study | 4 | Design for Safety |

**Key evidence (AG):** DT x Transformer closed-loop intelligent construction system for high-rise self-climbing platform (HUST/UNSW): video/sensor/BIM/text aligned at component level via Component-ID+Timestamp; multimodal Transformer for operation-state recognition and short-horizon risk prediction; policy module encodes safety/resource/spatial precedence constraints to generate feasible task sequences delivered to crews via AR with acknowledgments to close the loop; validated on high-rise SCP project (extends risk-warning lead time, reduces violation rates, shortens decision latency). Bidirectional closed-loop (DT->reasoning->AR execution) -> Tier 3; no learning loop.


**Strength & gap filled (AH):** Closes the perception-to-execution gap on a real high-rise self-climbing platform project: Component-ID plus timestamp aligns video, sensor, BIM and text streams; a multimodal Transformer recognizes operation states and predicts short-horizon risks; constraint-encoded policies generate feasible task sequences delivered via AR with acknowledgments, raising warning lead time from 1.8 to 4.6 seconds and cutting violations by 52 percent.

**Deficiencies & future work (AI):** High-resolution perception and large-model inference raise computational and maintenance costs, edge computing depends on stable power and network, AR execution relies on worker adaptation, and validation covers a single SCP project with confidential raw data. Future research targets model compression, lightweight deployment and adaptive zoning for scalability.
**Fusion depth (AC1):** Fused

**Fusion evidence (AC2):**
- **Data streams:** video, sensor, BIM and text streams on a high-rise self-climbing platform project.
- **Integration mechanism:** Component-ID plus timestamp aligns the four streams; a multimodal Transformer jointly recognises operation states and predicts short-horizon risks, and constraint-encoded policies generate task sequences delivered via AR with acknowledgments (warning lead time 1.8 to 4.6 s; violations cut 52%).
- **Why this code:** one model whose output depends on multiple aligned data types simultaneously, so Fused; implemented and demonstrated on a real project.

**Confidence (AC3):** High - the Component-ID+timestamp alignment and multimodal Transformer are explicitly described.
(full-text source: Endnote)
