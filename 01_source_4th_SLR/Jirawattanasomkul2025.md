# Jirawattanasomkul, T et al. (2025) — Digital twin-based structural health monitoring and measurements of dynamic characteristics in balanced cantilever bridge

- **ID:** R321 | **Source:** Scopus | **DOI:** 10.1016/j.rcns.2025.08.001
- **Journal:** Resilient Cities and Structures
- **Authors:** Jirawattanasomkul T.; Hang L.; Srivaranun S.; Likitlersuang S.; Jongvivatsakul P.; Yodsudjai W.; Thammarak P.

## Abstract summary
This study developed a digital twin (DT) and structural health monitoring (SHM) system for a balanced cantilever bridge, utilizing advanced measurement techniques to enhance accuracy. Vibration and dynamic strain measurements were obtained using accelerometers and piezo-resistive strain gauges, capturing low-magnitude dynamic strains during operational vibrations. 3D-LiDAR scanning and Ultrasonic Pulse Velocity (UPV) tests captured the bridge's as-is geometry and modulus of elasticity. The resulting detailed 3D point cloud model revealed the structure's true state and highlighted discrepancies between the as-designed and as-built conditions. Dynamic properties, including modal frequencies and shapes, were extracted from the strain and acceleration measurements, providing critical insights into the bridge's structural behavior. The neutral axis depth, indicating stress distribution and po…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** Balanced-cantilever bridge DT + SHM measurements

## Step-3 Deep-Read Coding (Prompt B)
| P DT-subject | Q DfS/DfQ | R codable | U Tier | V Design | W Constr | X Oper | Z DfX | AA Self-improve | AB Methodology | AC Modality | AD Validation | AE QA(0-5) | AF Cluster |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow (one-way physical to virtual) | 0 | 0 | 1 | Design for Safety (DfS) | None | Finite Element Method / physics-based | Multi (two or more data types) | Single case study | 4 | Predictive analytics / decision support |

| AC1 fusion depth | AC2 fusion evidence | AC3 confidence |
|---|---|---|
| Fused | LiDAR geometry, UPV modulus and dynamic strain/acceleration measurements are fused in the calibrated as-is bridge model. | High |

**Key evidence (AG):** Digital twin-based SHM for a balanced cantilever bridge (Chulalongkorn/KU/AIT, Resilient Cities and Structures 2025): accelerometers and piezo-resistive strain gauges capture operational dynamic strains; 3D-LiDAR scanning and UPV tests capture as-is geometry and elastic modulus revealing as-designed vs as-built discrepancies; modal frequencies/shapes and neutral-axis depth extracted; good agreement between measurements and the as-is model validates the twin; baseline established for future inspection and predictive maintenance. Campaign-based field measurements feeding the twin; no actuation, no learning loop.

*Full-text source: browser-oa*

**AH — strength & gap filled:** As-is LiDAR/UPV characterisation plus dynamic strain/modal measurement validates a balanced-cantilever twin that exposes as-designed vs as-built discrepancies.

**AI — deficiencies & future work:** Campaign-based measurements rather than continuous streaming; baseline twin only - damage scenarios and predictive maintenance remain future work.
