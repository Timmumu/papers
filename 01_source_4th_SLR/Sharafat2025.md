# Sharafat, A et al. (2025) — Digital Twin-Driven Stability Optimization Framework for Large Underground Caverns

- **ID:** R399 | **Source:** Scopus | **DOI:** 10.3390/app15084481
- **Journal:** Applied Sciences (Switzerland)
- **Authors:** Sharafat A.; Tanoli W.A.; Zubair M.U.; Mazher K.M.

## Abstract summary
With rapid urbanization, the utilization of underground space has become an important part of infrastructure. However, the stability of underground spaces such as large caverns remains a key challenge in civil engineering throughout the lifecycle of a project. Traditional methods of stability assessment rely on static models and periodic monitoring and often fail to capture real-time changes in rock behavior, leading to potential safety risks and, in severe cases, even the collapse of underground infrastructure. To address this challenge, this study introduces a digital twin (DT) framework to improve stability assessments and monitor deformations in underground structures. The framework enables the continuous monitoring and adaptive optimization of rock support systems by combining real-time sensor data with virtual simulations. A five-dimensional DT framework comprises physical objects,…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** DT-driven stability optimization of large underground caverns


## Step-3 Deep-Read Coding (Prompt B)
| P DT-subject | Q DfS/DfQ | R codable | U Tier | V Design | W Constr | X Oper | Z DfX | AA Self-improve | AB Methodology | AC Modality | AD Validation | AE QA(0-5) | AF Cluster |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow (one-way physical to virtual) | 0 | 1 | 0 | Design for Safety (DfS) | None | Finite Element Method / physics-based | Multi (two or more data types) | Single case study | 4 | Design for Safety |

| AC1 fusion depth | AC2 fusion evidence | AC3 confidence |
|---|---|---|
| Fused | Extensometers, load cells and prism-target measurements jointly feed the FEM models that trigger rock-support adjustments on the Neelum Jhelum powerhouse cavern. | Medium |

**Key evidence (AG):** Digital twin-driven stability optimization framework for large underground caverns (Hanyang U): five-dimensional DT framework (physical objects, virtual objects, service systems, DT data, interconnections) with six modules (structure, geology, material, behavior, performance, environment); IFC standards for interoperability; seven-step methodology (geological assessment, virtual modeling, BIM-based design, construction, real-time monitoring, optimization); case study demonstrates improved deformation monitoring and rock support efficiency. One-way monitoring→optimization→stability management; no actuation and no learning loop (optimization is rule-based, not learning).

*Full-text source: 04c-port*

**AH — strength & gap filled:** Proposes a five-dimensional digital twin framework with six modules and a seven-step methodology for large underground cavern stability, adding IFC extensions (new entities and property sets for geotechnical monitoring, excavation sequence and convergence) and validated on the Neelum Jhelum hydropower powerhouse cavern where 52 extensometers, load cells and 24 prism targets feed FEM models to trigger rock support adjustments in near real time.

**AI — deficiencies & future work:** Evaluation metrics are comparative estimates rather than measured outcomes, convergence station readings were collected manually on a weekly basis until obstructed, and reflective targets had to be replaced mid-project; real-time processing of large geotechnical datasets demands high-performance computing and validation covers only one geological setting. Future research targets enhanced automation, predictive analytics and wider environments.
