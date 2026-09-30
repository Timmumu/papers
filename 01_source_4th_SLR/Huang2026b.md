# Huang, Z et al. (2026) — Lifecycle updating of rockfill dam deformation models via dependence-aware sequential Bayesian inference with posterior-guided continual surrogate learning

- **ID:** R347 | **Source:** Scopus | **DOI:** 10.1016/j.cacaie.2026.100169
- **Journal:** Computer-Aided Civil and Infrastructure Engineering
- **Authors:** Huang Z.; Ma G.; Zhang Y.; Zhang G.; Ai Z.; Cui Y.; Zhou W.

## Abstract summary
Rockfill dams exhibit pronounced stage-dependent deformation during construction, impoundment, and long-term operation, requiring monitoring-updated deformation models for lifecycle prediction and digital twin-based safety assessment. However, existing updating methods are often deterministic and stage-isolated, while conventional probabilistic approaches insufficiently capture dependence among mechanically related constitutive parameters. For multi-stage lifecycle analysis, these methods also lack cross-stage adaptability and often require repeated finite-element simulations or full surrogate retraining, leading to high computational cost. This study proposes a dependence-aware sequential probabilistic framework with posterior-guided continual surrogate learning for dynamic updating of rockfill dam deformation models. The framework progressively assimilates monitoring data to track life…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** Rockfill dam Bayesian surrogate DT; safety assessment

## Step-3 Deep-Read Coding (Prompt B)
| P DT-subject | Q DfS/DfQ | R codable | U Tier | V Design | W Constr | X Oper | Z DfX | AA Self-improve | AB Methodology | AC Modality | AD Validation | AE QA(0-5) | AF Cluster |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow (one-way physical to virtual) | 0 | 0 | 1 | Design for Safety (DfS) | Implemented | Bayesian / probabilistic | Multi (two or more data types) | Single case study | 4 | Predictive analytics / decision support |

| AC1 fusion depth | AC2 fusion evidence | AC3 confidence |
|---|---|---|
| Fused | Monitoring data, copula-structured priors and FE-informed surrogate samples are fused in sequential Bayesian posterior updates. | High |

**Key evidence (AG):** Lifecycle updating of rockfill dam deformation models (Wuhan U, CACAIE 2026): dependence-aware sequential Bayesian inference with Gaussian-Copula priors progressively assimilates monitoring data across construction/impoundment/operation stages; deep neural surrogate continually refined via posterior-guided FE samples, historical replay and Fisher-weighted regularisation; on the 303 m Lianghekou dam global relative settlement prediction error falls 37.4%->9.7% with 45.8% surrogate-updating cost reduction. Monitoring->updating->uncertainty-informed safety assessment (no actuation); continual surrogate learning implemented, no convergence criterion.

*Full-text source: browser-oa*

**AH — strength & gap filled:** Copula-dependence sequential Bayesian updating plus continual surrogate learning halves the surrogate cost and cuts dam settlement error from 37.4% to 9.7%.

**AI — deficiencies & future work:** Single dam case; copula structure empirical; continual-learning forgetting bounds not proven; predictions for extreme future stages remain uncertain.
