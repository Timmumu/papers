# Zhang et al. (2026) — Digital twin-enabled synchronous jacking control of an aerial building machine using a scale model

- **ID:** 3991 | **Source:** Web of Science | **DOI:** 10.1016/j.autcon.2026.107076
- **Journal:** AUTOMATION IN CONSTRUCTION
- **Authors:** Zhang, L. M.; Zhang, X. P.; Chen, K.; Wang, J. Q.; Ding, L. Y.

## Abstract summary
The aerial building machine (ABM) provides an integrated solution for high-rise construction through its ability to hoist construction platforms, materials, and equipment to elevations of several hundred meters while maintaining high operational adaptability. The jacking process of the ABM depends on coordinated extension and retraction of multiple cylinders. However, high-altitude wind loads and non-uniform stacking loads on the construction platform introduce significant uncertainties that may compromise structural safety. This paper presents the development of an intelligent synchronous control system based on a scaled experimental platform, employing a deep neural network for dynamic error compensation, together with a digital twin framework to improve operational efficiency and human-machine collaboration. Reinforcement learning tuned control parameters, and transfer learning migrat…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** DT synchronous jacking control of aerial building machine; structural safety

## Step-3 Deep-Read Coding (Prompt B)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 3 - Digital Twin (bidirectional, two-way) | 0 | 1 | 0 | Design for Safety (DfS) | Implemented | Reinforcement Learning (RL) | Multi (two or more data types) | Simulation | 4 | Design for Safety |

**Key evidence (AG):** DT-enabled synchronous jacking control of an aerial building machine (ABM) using a scale model (HUST): scale experimental platform; deep neural network (DNN-PID) for dynamic error compensation; reinforcement learning tunes control parameters; transfer learning migrates DNN-PID controller to scale model; DT system for visual presentation of jacking data and equipment states during synchronous control; jacking tests show 0.407 mm synchronization error (max <0.46 mm across 10 conditions), 29% max error reduction with fewer iterations; DNN-PID reduces MSE by 5.87 mm vs traditional PID. Bidirectional closed-loop (monitoring->control) -> Tier 3; implemented RL tuning + transfer learning (implemented learning mechanism, no convergence proof).
(full-text source: Endnote)
