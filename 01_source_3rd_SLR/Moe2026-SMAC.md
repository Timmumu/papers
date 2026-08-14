# Moe et al. (2026) — SMAC-based cooperative hyperparameter optimization for occupational risk assessment in decentralized federated on-device AI networks

- **ID:** 4004 | **Source:** Web of Science | **DOI:** 10.1016/j.aej.2026.05.006
- **Journal:** ALEXANDRIA ENGINEERING JOURNAL
- **Authors:** Moe, S. J. S.; Khan, Q. W.; Nguyen, A. T.; Bibi, M.; Kim, D. H.

## Abstract summary
Decentralized federated learning (DFL) enables peer-to-peer training, but hyperparameter optimization (HPO) in serverless environments remains underexplored. This paper presents a DFL framework featuring a one-shot cooperative HPO mechanism based on Sequential Model-based Algorithm Configuration (SMAC). The architecture employs a Digital Twin (DT) orchestration layer to manage edge nodes and network topologies without centralizing the learning process. Nodes perform independent local SMAC tuning followed by performance-weighted aggregation to derive a global hyperparameter configuration. Evaluated on worker-safety and MNIST datasets using a Raspberry Pi testbed, our approach significantly outperforms fixed settings and Random Search across IID and non-IID conditions (p<0.01p < 0.01 p<0.01). Results demonstrate faster convergence and higher accuracy; specifically, convergence rounds dropp…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** DT orchestration layer for federated worker-safety AI; occupational risk

## Step-3 Deep-Read Coding (Prompt B)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow (one-way physical to virtual) | 0 | 1 | 0 | Design for Safety (DfS) | None | Other / Mixed | Multi (two or more data types) | Single case study | 4 | Predictive analytics / decision support |

**Key evidence (AG):** SMAC-based cooperative hyperparameter optimization for occupational risk assessment in decentralized federated on-device AI networks (Jeju National U): DFL framework with one-shot cooperative HPO (SMAC) + DT orchestration layer to manage edge nodes and network topologies; local SMAC tuning + performance-weighted aggregation; validated on worker-safety and MNIST datasets with Raspberry Pi testbed; convergence rounds reduced 42→18 (worker safety). One-way monitoring→HPO→risk assessment; no actuation and no learning loop (SMAC is hyperparameter optimization, not online learning).
(full-text source: Endnote)
