# Sresakoolchai, J et al. (2023) — Railway infrastructure maintenance efficiency improvement using deep reinforcement learning integrated with digital twin based on track geometry and component defects

- **ID:** R677 | **Source:** Scopus | **DOI:** 10.1038/s41598-023-29526-8
- **Journal:** Scientific Reports
- **Authors:** Sresakoolchai J.; Kaewunruen S.

## Abstract summary
Railway maintenance is a complex and complicated task in the railway industry due to the number of its components and relationships. Ineffective railway maintenance results in excess cost, defective railway structure and components, longer possession time, poorer safety, and lower passenger comfort. Of the three main maintenance approaches, predictive maintenance is the trendy one, and is proven that it provides the highest efficiency. However, the implementation of predictive maintenance for the railway industry cannot be done without an efficient tool. Normally, railway maintenance is corrective when some things fail or preventive when maintenance is routine. A novel approach using an integration between deep reinforcement learning and digital twin is proposed in this study to improve the efficiency of railway maintenance which other techniques such as supervised and unsupervised learn…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** DRL + DT for railway maintenance efficiency

## Step-3 Deep-Read Coding (Prompt B)
| P DT-subject | Q DfS/DfQ | R codable | U Tier | V Design | W Constr | X Oper | Z DfX | AA Self-improve | AB Methodology | AC Modality | AD Validation | AE QA(0-5) | AF Cluster |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow (one-way physical to virtual) | 0 | 0 | 1 | Design for Safety (DfS) | Implemented | Reinforcement Learning (RL) | Multi (two or more data types) | Single case study | 4 | Predictive analytics / decision support |

| AC1 fusion depth | AC2 fusion evidence | AC3 confidence |
|---|---|---|
| Fused | Track geometry, component defects and maintenance activities are jointly encoded in the RL state/action/reward of one DT-trained policy. | High |

**Key evidence (AG):** Deep RL (Advantage Actor-Critic) integrated with a digital twin for railway maintenance efficiency (Birmingham, Sci Rep 2023): DT built from four years of real field data over 30 km; track geometry parameters, component defects and maintenance activities form states/actions; rewards from maintenance costs and occurring defects; trained policy reduces maintenance activities by 21% and occurring defects by 68%, improving safety and passenger comfort. Maintenance-policy recommendations to decision-makers (no automated track actuation); RL training loop implemented but no convergence criterion.

*Full-text source: Endnote*

**AH — strength & gap filled:** Fills the efficiency gap of railway predictive maintenance: A2C reinforcement learning on a 30-km four-year field-data DT cuts maintenance activities by 21% and occurring defects by 68%, with track geometry treated per-parameter and seven independent actions.

**AI — deficiencies & future work:** The RL policy is trained on historical four-year data and validated by simulation of maintenance policy, not by live closed-loop control of actual maintenance operations; convergence of A2C training is not analysed, and reward design (cost vs safety weighting) is not fully explored.
