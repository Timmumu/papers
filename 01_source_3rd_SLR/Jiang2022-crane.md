# Jiang et al. (2022) — Digital twin: Stability analysis for tower crane hoisting safety with a scale model

- **ID:** 3572 | **Source:** Scopus | **DOI:** 10.1016/j.autcon.2022.104257
- **Journal:** Automation in Construction
- **Authors:** Jiang, W.; Ding, L.; Zhou, C.

## Abstract summary
Unsafe hoisting behaviors are the fuse of tower crane overturning safety accident. However, the hoisting operation has a certain degree of randomness and invisibility, and it is extremely dangerous to carry out the experiment on the construction site, which makes the research on the relevant regularity very scarce. To simulate different hoisting behaviors as realistically as possible and analyze their dynamic effects on the tower crane, a digital twin (DT) framework of human–machine interaction construction activities is constructed based on the scale model in this study. Through experimental study, the stability change law of the tower crane with the incremental dynamic load is obtained based on the collapse probability level function. Experiment results show that tilt hoisting is the most dangerous behavior causing the tower crane instability. Tower crane foundation and masts are the m…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** DT of tower-crane hoisting stability; scale-model experiments

## Step-3 Deep-Read Coding (Prompt B) — full text verified via Endnote library (front-matter DOI/title match, coverage re-scan 2026-08-12)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow | 0 | 1 | 0 | Design for Safety (DfS) | None | Finite Element Method / physics-based | Multi (two or more data types) | Simulation | 4 | Design for Safety |

**Key evidence (AG):** DT framework of human-machine hoisting (tower crane, HUST): 1/30 physical scale model (sensors at 20 Hz) as physical entity + synchronous virtual model (FEM, BIM, component IDA) + IoT data flow for real-time dynamic stability analysis; four unsafe hoisting behaviors (vertical/tilt/sudden braking/unloading) compared (scale model vs simulation vs real-model simulation); collapse-probability level function ranks tilt hoisting as most dangerous, foundation/mast most vulnerable for sensor deployment. Lab scale-model experiment; warning to operator via threshold but no actuation and no learning loop (monitoring system design is future work).

**Strength & gap filled (AH):** Addresses the scarcity of experimental knowledge on unsafe hoisting behavior effects: a human-machine interaction DT built on a 1/30 scale tower crane with 20 Hz sensors synchronizes virtual FEM and BIM models through IoT data flow, and incremental dynamic load analysis yields collapse probability levels (TCL, FCL, MCL, JCL, CCL, RCL) showing tilt hoisting as most dangerous with foundation and masts most vulnerable.

**Deficiencies & future work (AI):** Results come from a laboratory scale model under simplified single-behavior conditions; sensor data agree with the virtual model in trend but differ in magnitude due to material property differences. Combined environmental loads and other unsafe behaviors, tower crane structural changes, and component influence weights during instability remain future work, and the unsafe hoisting monitoring system is only planned, not built.

**Fusion depth (AC1):** Fused

**Fusion evidence (AC2):**
- **Data streams:** 20 Hz scale-model sensor data on a 1/30 tower crane; FEM, BIM and component IDA virtual models.
- **Integration mechanism:** IoT data flow synchronises the virtual models with measured states, and incremental dynamic load analysis computes collapse-probability levels (TCL/FCL/MCL/JCL/CCL/RCL) that rank unsafe hoisting behaviours; sensor-vs-model trends are compared directly.
- **Why this code:** the stability output depends on measured sensor states and model responses simultaneously, so Fused; lab-scale only (Medium).

**Confidence (AC3):** Medium - the synchronisation mechanism is clear, but validation is a laboratory scale model.