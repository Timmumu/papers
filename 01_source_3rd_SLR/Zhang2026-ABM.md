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


**Strength & gap filled (AH):** Fills the gap of closed-loop digital twin control for aerial building machine jacking, validated on a 1:25 scale model of a 380-meter Wuhan project: PPO reinforcement learning tunes PID parameters and a transfer-learned DNN-PID controller with deviation coupling runs on an STM32 platform, reducing mean synchronization error to 0.377 mm versus 3.485, 0.463 and 0.709 mm for competing methods, staying below 0.46 mm across ten loading conditions with a 29 percent gain from transfer learning.

**Deficiencies & future work (AI):** Validated only on a scale model with four electric actuators instead of the real 12-cylinder hydraulic system; preset loading means failure boundaries, wind, actuator saturation, sensor drift and communication latency were not explored, and the twin has a 1-1.5 second delay. Future work targets stress-strain sensors, finite element safety assessment, real ABM operational data and physics-informed neural networks.
**Fusion depth (AC1):** Fused

**Fusion evidence (AC2):**
- **Data streams:** 1:25 scale-model jacking sensors + DNN-PID controller state + PPO-tuned parameters (STM32 platform).
- **Integration mechanism:** the transfer-learned DNN-PID fuses deviation coupling with sensor feedback to command four actuators, cutting mean synchronisation error to 0.377 mm versus 3.485/0.463/0.709 mm, with a 29% transfer-learning gain.
- **Why this code:** the control output depends on multiple streams simultaneously in a closed loop, so Fused.

**Confidence (AC3):** High - the control architecture is explicit; validation is scale-model only.
(full-text source: Endnote)
