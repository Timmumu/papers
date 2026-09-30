# Zhang, XN et al. (2024) — AIoT-enabled digital twin system for smart tunnel fire safety management

- **ID:** R918 | **Source:** Web of Science | **DOI:** 10.1016/j.dibe.2024.100381
- **Journal:** DEVELOPMENTS IN THE BUILT ENVIRONMENT
- **Authors:** Zhang, XN; Jiang, YS; Wu, XQ; Nan, ZJ; Jiang, YQ; Shi, JH; Zhang, YX; Huang, XY; Huang, GGQ

## Abstract summary
High traffic flow in a confined tunnel makes fire safety a critical issue. This paper proposed a digital twin framework for tunnel fire safety management in real-time, driven by dynamic sensor data and AIoT technologies. A deep learning model trained by the Transformer network and simulation dataset is used to predict real-time fire location and size. Then, the AI model is integrated into a 3D digital twin platform developed by the game engine Unity 3D. The performance of the proposed digital twin framework is demonstrated using numerical experiments and large-scale tunnel fire tests. Results show that the established AI model achieved promising accuracy in predicting fire location and power for both numerical and experimental data. The digital twin platform can also visualize the 3D fire scene that supports evacuation, firefighting, and emergency rescue. This research demonstrates the f…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** AIoT digital twin for smart tunnel fire safety management

## Step-3 Deep-Read Coding (Prompt B)
| P DT-subject | Q DfS/DfQ | R codable | U Tier | V Design | W Constr | X Oper | Z DfX | AA Self-improve | AB Methodology | AC Modality | AD Validation | AE QA(0-5) | AF Cluster |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow (one-way physical to virtual) | 0 | 0 | 1 | Design for Safety (DfS) | None | Transformer / Large Language Model (LLM) | Multi (two or more data types) | Simulation | 3 | Design for Safety |

| AC1 fusion depth | AC2 fusion evidence | AC3 confidence |
|---|---|---|
| Fused | Dynamic sensor data and simulation-trained Transformer outputs are fused in the 3D fire twin. | Medium |

**Key evidence (AG):** AIoT-enabled digital twin system for smart tunnel fire safety management (PolyU/HKU, Developments in the Built Environment 2024): Transformer deep learning model trained on simulation data predicts real-time fire location and size from dynamic sensor data; integrated into a Unity 3D digital twin platform visualizing the 3D fire scene to support evacuation, firefighting and emergency rescue; demonstrated with numerical experiments and large-scale tunnel fire tests. Prediction + visualization, no actuation.

*Full-text source: browser-oa*

**AH — strength & gap filled:** Transformer-based fire source prediction validated on large-scale tunnel fire tests and visualized in a Unity 3D twin.

**AI — deficiencies & future work:** Numerical + large-scale tests but no continuous live tunnel deployment described.
