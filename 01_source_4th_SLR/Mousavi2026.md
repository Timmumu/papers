# Mousavi, V et al. (2026) — Deep reinforcement learning-based decision support system for optimal maintenance planning in bridge digital twins

- **ID:** R057 | **Source:** Scopus | **DOI:** 10.1016/j.engappai.2026.115649
- **Journal:** Engineering Applications of Artificial Intelligence
- **Authors:** Mousavi V.; Rashidi M.; Ghazimoghadam S.; Mohammadi M.; Samali B.

## Abstract summary
Bridge infrastructures are inevitably exposed to a wide range of deterioration mechanisms and external damages over their service life, which can gradually impair structural integrity, compromise functionality, and increase safety risks. These challenges, coupled with the growing complexity of infrastructure systems and limited financial resources, highlight the need for implementing intelligent and proactive asset management solutions. To address these needs, this paper presents a Reinforcement Learning-based Decision Support System (RL-DSS) framework for bridge maintenance optimization, leveraging a Multi-Objective Deep Centralized Multi-Agent Actor-Critic (MO-DCMAC) algorithm that is designed for application within bridge Digital Twin environments. The proposed RL-DSS implements a three-objective MO-DCMAC framework that models maintenance cost, structural failure risk, and serviceabil…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** RL-DSS for bridge maintenance inside bridge DT

## Step-3 Deep-Read Coding (Prompt B)
| P DT-subject | Q DfS/DfQ | R codable | U Tier | V Design | W Constr | X Oper | Z DfX | AA Self-improve | AB Methodology | AC Modality | AD Validation | AE QA(0-5) | AF Cluster |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow (one-way physical to virtual) | 0 | 0 | 1 | Design for Safety (DfS) | Implemented | Reinforcement Learning (RL) | Multi (two or more data types) | Cross-project (multiple real projects) | 4 | Predictive analytics / decision support |

| AC1 fusion depth | AC2 fusion evidence | AC3 confidence |
|---|---|---|
| Fused | Maintenance cost, structural failure risk and serviceability are fused in one vector-valued reward with linear scalarization for MO-DCMAC training in bridge DT environments. | High |

**Key evidence (AG):** RL-based decision support system for bridge maintenance inside digital-twin environments (Western Sydney U, EngAppAI 2026): multi-objective deep centralized multi-agent actor-critic (MO-DCMAC) models maintenance cost, structural failure risk and serviceability as a vector-valued reward with fixed linear utility; evaluated on three real bridge case studies vs established rule-based policies, achieving highest overall utility by penalizing high-frequency site visits and balancing intervention cost with risk mitigation. Maintenance-policy recommendations to asset managers (no automated actuation); RL training loop implemented but no convergence criterion.

*Full-text source: browser-oa*

**AH — strength & gap filled:** Brings multi-objective deep RL into bridge digital twins: vector-valued reward (cost, failure risk, serviceability) with linear utility outperforms rule-based policies across three real bridge case studies, yielding fewer but more impactful interventions.

**AI — deficiencies & future work:** Fixed linear utility function prevents adaptive preference trade-offs; RL convergence not characterised; policies are recommendations (no closed-loop actuation) and case studies are retrospective.
