# Arias-Ferreiro, G et al. (2026) — Integrated Air–Ground Robotic System for Autonomous Post-Blast Operations in GNSS-Denied Tunnels

- **ID:** R420 | **Source:** Scopus | **DOI:** 10.3390/rs18081133
- **Journal:** Remote Sensing
- **Authors:** Arias-Ferreiro G.; Montes-Grova M.A.; Pérez-Grau F.J.; Noriega-del-Rivero S.; Herguedas R.; Lázaro M.T.; Castelruiz-Aguirre A.; Fernandez J.C.J.; Karahan M.; Alonso-Cepeda A.

## Abstract summary
Post-blast operations in tunnel construction represent a critical bottleneck due to mandatory downtime and hazardous environmental conditions. This study addresses these challenges by developing and validating an integrated cyber–physical architecture that coordinates an autonomous Unmanned Aerial Vehicle (UAV) and an Autonomous Wheel Loader (AWL) under the supervision of a Digital Twin acting as central operational digital interface. Specifically, this technology was designed to access the tunnel, evaluate post-blasting conditions, and initiate operations during mandatory exclusion periods for personnel. The system was validated in a realistic, Global Navigation Satellite System (GNSS)-denied tunnel environment emulating post-detonation visibility constraints. The results demonstrate that the aerial agent successfully navigated and mapped the excavation front in less than 8 min, establi…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** Air-ground robotic post-blast tunnel ops under DT supervision

## Step-3 Deep-Read Coding (Prompt B)
| P DT-subject | Q DfS/DfQ | R codable | U Tier | V Design | W Constr | X Oper | Z DfX | AA Self-improve | AB Methodology | AC Modality | AD Validation | AE QA(0-5) | AF Cluster |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 3 - Digital Twin (bidirectional, two-way) | 0 | 1 | 0 | Design for Safety (DfS) | None | Perception / Computer Vision | Multi (two or more data types) | Simulation | 4 | Perception / Computer Vision |

| AC1 fusion depth | AC2 fusion evidence | AC3 confidence |
|---|---|---|
| Fused | LiDAR, thermal and inertial streams are fused for SLAM, and robot statuses are fused in the DT orchestration layer. | Medium |

**Key evidence (AG):** Integrated air-ground robotic system for autonomous post-blast operations (ACCIONA/CATEC/TECNALIA, Remote Sensing 2026): digital twin acts as central operational digital interface coordinating a UAV (LiDAR-thermal-inertial SLAM, maps 500 m tunnel <8 min in zero visibility) and an autonomous wheel loader for debris removal in GNSS-denied tunnels; shared coordinate frame handed to ground machinery; operations start 50-80% earlier, 100% elimination of human exposure, 8% daily time saving, ROI 1-7 months. Twin orchestrates autonomous machines (virtual-to-physical) -> Tier 3; validated in a realistic emulated tunnel environment (not production); no learning loop.

*Full-text source: browser-oa*

**AH — strength & gap filled:** DT-orchestrated UAV-AWL team starts post-blast operations 50-80% earlier and eliminates human exposure in GNSS-denied tunnels, with ROI of 1-7 months.

**AI — deficiencies & future work:** Validated in an emulated realistic tunnel, not production blasting cycles; debris-removal autonomy details limited; comms in deep tunnels unaddressed.
