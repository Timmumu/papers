# Yang, B et al. (2025) — Prediction and optimization of structural performance of prefabricated bridges based on physical information neural network (PINN) and BlM

- **ID:** R488 | **Source:** Scopus | **DOI:** 10.1007/s44163-025-00245-5
- **Journal:** Discover Artificial Intelligence
- **Authors:** Yang B.; Han Z.; Yang M.

## Abstract summary
This study presents an innovative performance prediction and optimization method for prefabricated bridge structures, which integrates the strengths of Physical Information Neural Network (PINN) and Building Information Modeling (BIM). By combining the computational power of PINN for solving structural mechanics problems with BIM’s data management and modeling capabilities in construction engineering, a multi-layer, multi-dimensional intelligent framework for prediction and optimization is developed. BIM models provide crucial data, including geometric details, material properties, and construction process information, which are used to create a digital twin of the bridge. Leveraging PINN’s robust fitting ability, physical laws such as stress, strain, and equilibrium equations are incorporated into the neural network to predict the bridge’s performance under various operational condition…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** PINN+BIM digital twin for prefabricated bridge performance


## Step-3 Deep-Read Coding (Prompt B)
| P DT-subject | Q DfS/DfQ | R codable | U Tier | V Design | W Constr | X Oper | Z DfX | AA Self-improve | AB Methodology | AC Modality | AD Validation | AE QA(0-5) | AF Cluster |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 1 - Digital Model (static, no live data) | 1 | 0 | 0 | Both | None | Other / Mixed | Multi (two or more data types) | Simulation | 3 | Predictive analytics / decision support |

| AC1 fusion depth | AC2 fusion evidence | AC3 confidence |
|---|---|---|
| Fused | BIM geometry/material/process data and PINN physics constraints are fused in one predictive-optimisation model. | Medium |

**Key evidence (AG):** PINN + BIM framework for prediction and optimisation of prefabricated-bridge structural performance (Anhui Vocational Colleges/ZSTU, Discover AI 2025): BIM provides geometry, material and construction-process data to build a digital twin; PINN embeds stress/strain/equilibrium physics into the network; optimisation algorithms refine design against safety, cost and environmental criteria; experiments show superior accuracy and generalisation vs traditional methods. Design-time simulation twin; no live data link, no actuation, no learning loop.

*Full-text source: Endnote*

**AH — strength & gap filled:** Fills the data-scarce prediction gap in prefabricated-bridge design: PINN physics constraints on BIM-derived twin data yield more accurate, generalisable performance prediction and multi-objective (safety/cost/environment) design optimisation than traditional methods.

**AI — deficiencies & future work:** Numerical/experimental validation on generic prefabricated-bridge configurations rather than a real project; PINN training cost and mesh/physics completeness for complex nonlinear cases are not addressed; optimisation-to-design integration is not automated.
