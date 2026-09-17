# Di Marco, G (2026) — A Digital Twin With Material Characterisation and LLM as High-Level Orchestrator via Few-Shot In-Context Learning for Closed-Loop Control in Robotic Adaptive 3DCP

- **ID:** R938 | **Source:** Web of Science | **DOI:** 10.1155/stc/8514242
- **Journal:** STRUCTURAL CONTROL & HEALTH MONITORING
- **Authors:** Di Marco, G

## Abstract summary
The industrialisation of 3D concrete printing (3DCP) is impeded by the lack of universal standards, a situation exacerbated by the process's sensitivity to multiple interdependent parameters and environmental conditions, which can introduce structural defects and performance inconsistencies. Starting from the definition of 3DCP as a cyberphysical production system (CPPS), this exploratory study proposes adopting a hybrid standardisation method that optimises structural performance, or concrete grade. By following the DSR/ASTM V&V research framework and based on the preliminary characterisation of materials, a computational digital twin is implemented, including a compressive strength predictive model connected to the simulation of the adaptive 3DCP process. Accounting for the anisotropic behaviour of 3D-printed concrete (3DPC), the predictive model determines the 3DPC grade based on prel…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** Computational DT for adaptive 3D concrete printing quality


## Step-3 Deep-Read Coding (Prompt B)
| P DT-subject | Q DfS/DfQ | R codable | U Tier | V Design | W Constr | X Oper | Z DfX | AA Self-improve | AB Methodology | AC Modality | AD Validation | AE QA(0-5) | AF Cluster |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 1 - Digital Model (static, no live data) | 0 | 1 | 0 | Both | Mentioned only | Other / Mixed | Multi (two or more data types) | Simulation | 3 | Predictive analytics / decision support |

| AC1 fusion depth | AC2 fusion evidence | AC3 confidence |
|---|---|---|
| Fused | Material characterisation, process parameters and environmental factors with Monte Carlo uncertainty are fused in one strength-prediction model. | Medium |

**Key evidence (AG):** Computational digital twin with material characterisation for robotic adaptive 3D concrete printing (XJTLU, Struct Control Health Monit 2026): Grasshopper parametric workflow implements a compressive-strength predictive model with Monte Carlo uncertainty propagation (1000 samples), optimising process parameters to maximise parallel strength and guarantee grade M20 at the 5th percentile (design-for-safety); variance in parallel structural strength reduced by 25% with 90% confidence of M20, reducing anisotropy; a pretrained LLM acting as high-level orchestrator for closed-loop control via few-shot in-context learning is proposed/PoC-described but the closed loop is not demonstrated on the physical cell (no test-bed experimental data). Virtual-testing validation; no live physical link; learning mechanism mentioned only.

*Full-text source: Endnote*

**AH — strength & gap filled:** Fills the standardisation gap for 3DCP: a computational DT with material characterisation and Monte Carlo uncertainty propagation optimises process parameters to maximise parallel strength (variance -25%, 90% confidence of M20), prioritising the 5th-percentile design-for-safety criterion, with an LLM proposed as closed-loop orchestrator.

**AI — deficiencies & future work:** No physical test-bed experiments: validation is virtual (Monte Carlo); the LLM closed-loop orchestration is proposed/PoC-described and not demonstrated on the robotic cell; few-shot prompt robustness and physical actuation safety are open questions.
