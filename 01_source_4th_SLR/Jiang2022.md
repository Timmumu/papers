# Jiang, W et al. (2022) — Digital twin: Stability analysis for tower crane hoisting safety with a scale model

- **ID:** R548 | **Source:** Scopus | **DOI:** 10.1016/j.autcon.2022.104257
- **Journal:** Automation in Construction
- **Authors:** Jiang W.; Ding L.; Zhou C.

## Abstract summary
Unsafe hoisting behaviors are the fuse of tower crane overturning safety accident. However, the hoisting operation has a certain degree of randomness and invisibility, and it is extremely dangerous to carry out the experiment on the construction site, which makes the research on the relevant regularity very scarce. To simulate different hoisting behaviors as realistically as possible and analyze their dynamic effects on the tower crane, a digital twin (DT) framework of human–machine interaction construction activities is constructed based on the scale model in this study. Through experimental study, the stability change law of the tower crane with the incremental dynamic load is obtained based on the collapse probability level function. Experiment results show that tilt hoisting is the most dangerous behavior causing the tower crane instability. Tower crane foundation and masts are the m…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** Scale-model DT for tower crane hoisting stability safety


## Step-3 Deep-Read Coding (Prompt B)
| P DT-subject | Q DfS/DfQ | R codable | U Tier | V Design | W Constr | X Oper | Z DfX | AA Self-improve | AB Methodology | AC Modality | AD Validation | AE QA(0-5) | AF Cluster |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow (one-way physical to virtual) | 0 | 1 | 0 | Design for Safety (DfS) | None | Finite Element Method / physics-based | Multi (two or more data types) | Simulation | 4 | Design for Safety |

| AC1 fusion depth | AC2 fusion evidence | AC3 confidence |
|---|---|---|
| Fused | Twenty-Hz scale-model sensors (displacement, tilt etc.) stream through IoT into synchronous FEM/BIM/IDA virtual models that compute real-time dynamic stability analysis and collapse-probability levels. | Medium |

**Key evidence (AG):** DT framework of human-machine hoisting (tower crane, HUST): 1/30 physical scale model (sensors at 20 Hz) as physical entity + synchronous virtual model (FEM, BIM, component IDA) + IoT data flow for real-time dynamic stability analysis; four unsafe hoisting behaviors (vertical/tilt/sudden braking/unloading) compared (scale model vs simulation vs real-model simulation); collapse-probability level function ranks tilt hoisting as most dangerous, foundation/mast most vulnerable for sensor deployment. Lab scale-model experiment; warning to operator via threshold but no actuation and no learning loop (monitoring system design is future work).

*Full-text source: 04c-port*

**AH — strength & gap filled:** Addresses the scarcity of experimental knowledge on unsafe hoisting behavior effects: a human-machine interaction DT built on a 1/30 scale tower crane with 20 Hz sensors synchronizes virtual FEM and BIM models through IoT data flow, and incremental dynamic load analysis yields collapse probability levels (TCL, FCL, MCL, JCL, CCL, RCL) showing tilt hoisting as most dangerous with foundation and masts most vulnerable.

**AI — deficiencies & future work:** Results come from a laboratory scale model under simplified single-behavior conditions; sensor data agree with the virtual model in trend but differ in magnitude due to material property differences. Combined environmental loads and other unsafe behaviors, tower crane structural changes, and component influence weights during instability remain future work, and the unsafe hoisting monitoring system is only planned, not built.
