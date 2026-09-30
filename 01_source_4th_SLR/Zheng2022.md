# Zheng, Z et al. (2022) — Digital Twin-Based Investigation of a Building Collapse Accident

- **ID:** R800 | **Source:** Scopus | **DOI:** 10.1155/2022/9568967
- **Journal:** Advances in Civil Engineering
- **Authors:** Zheng Z.; Liao W.; Lin J.; Zhou Y.; Zhang C.; Lu X.

## Abstract summary
The collapse of engineering structures can cause significant casualties and have negative social effects. Collapse accident investigation can elucidate the potential causes and mechanisms of the collapse accident, thus remediating future structural collapse and enhancing the resilience. However, there are some obstacles to investigating complicated collapse accidents using conventional methods. For example, the out-syncs between on-site investigation and simulation analysis are intractable and can make discovering the cause of collapse accidents difficult. Hence, a digital twin-based investigation method for collapse accidents was proposed. First, basic virtual digital building models are established using real-world information. Then, after mapping the data from the real world into the virtual space, the corresponding highly realistic multistage models before and after the building coll…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** DT-based investigation of building collapse accident

## Step-3 Deep-Read Coding (Prompt B)
| P DT-subject | Q DfS/DfQ | R codable | U Tier | V Design | W Constr | X Oper | Z DfX | AA Self-improve | AB Methodology | AC Modality | AD Validation | AE QA(0-5) | AF Cluster |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow (one-way physical to virtual) | 0 | 0 | 1 | Design for Safety (DfS) | None | Finite Element Method / physics-based | Multi (two or more data types) | Single case study | 4 | Design for Safety |

| AC1 fusion depth | AC2 fusion evidence | AC3 confidence |
|---|---|---|
| Aligned | Real-world records (drawings, photos, investigation data) are mapped into BIM, FE and physics-engine models that reconstruct the collapse in stages, sharing one building frame while each model analyses its own domain. | Medium |

**Key evidence (AG):** Digital twin-based investigation of a building collapse accident (Tsinghua U): virtual digital building models (BIM, FE model, physics-engine model) built from real-world info; real-world data mapped into virtual space to construct highly realistic multistage models before and after the collapse, synchronized; investigators integrate/update/check models to reveal collapse mechanism; validated on a real collapse accident (columns exceeded critical buckling stress from welding-induced local buckling/plastic deformation). One-way data->model->cause diagnosis; no actuation, no learning loop.

*Full-text source: 04c-port*

**AH — strength & gap filled:** Fills the gap between out-of-sync site investigation and simulation in collapse forensics: a digital twin built from BIM, finite element and physics engine models reconstructs the multistage life cycle of a seven-story hotel retrofitted from a four-story steel frame, reproduces the collapse and matches simulated wreckage with actual debris, showing welding-induced column buckling and plastic deformation caused the failure rather than local buckling alone.

**AI — deficiencies & future work:** A retrospective forensic tool: the accident has already occurred and caused heavy losses, and the twin is built from drawings and records rather than live sensor data. Future research will establish digital twin models for important buildings in advance to perform multihazard simulations and continuously monitor key component mechanical states to prevent disasters.
