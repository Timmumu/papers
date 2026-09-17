# Chang, X et al. (2026) — A transformer-based surrogate modeling strategy for tunnel digital twin in full-field displacement prediction under adjacent tunnel construction

- **ID:** R219 | **Source:** Scopus | **DOI:** 10.1016/j.aei.2025.104045
- **Journal:** Advanced Engineering Informatics
- **Authors:** Chang X.; Fan H.; Fu Y.; Han C.; Wang H.; Mao J.

## Abstract summary
Accurately predicting ground settlement and tunnel lining deformation is essential for ensuring the safety and efficiency of shield tunnel projects, especially in urban areas affected by adjacent excavations. Rapid and reliable forecasts of tunnel behavior support proactive design decisions and risk mitigation. However, most existing surrogate models offer limited predictive resolution and accuracy, as they predict responses only at sparse monitoring points and ignore spatial information, which restricts their applicability in building comprehensive digital twin (DT) systems for full-field simulation. To address these limitations, this study proposes a DT framework for predicting ground settlement and lining deformation in shield tunnels affected by adjacent excavation. A hybrid surrogate model, called the Dual-Fusion Swin-Table Transformer Network (DF-STTN), is developed by combining Sw…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** DF-STTN tunnel DT surrogate; settlement safety


## Step-3 Deep-Read Coding (Prompt B)
| P DT-subject | Q DfS/DfQ | R codable | U Tier | V Design | W Constr | X Oper | Z DfX | AA Self-improve | AB Methodology | AC Modality | AD Validation | AE QA(0-5) | AF Cluster |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow (one-way physical to virtual) | 0 | 1 | 0 | Design for Safety (DfS) | Implemented | Transformer / Large Language Model (LLM) | Multi (two or more data types) | Single case study | 4 | Predictive analytics / decision support |

| AC1 fusion depth | AC2 fusion evidence | AC3 confidence |
|---|---|---|
| Fused | The DF-STTN hybrid surrogate fuses Swin-Transformer spatial fields with TabTransformer non-spatial parameters via a dual-stage fusion module, and a GA model-updating procedure joins sparse laboratory test data with the FE-trained model. | High |

**Key evidence (AG):** DT framework for predicting ground settlement and lining deformation of shield tunnels under adjacent excavation (NTU/Southeast U): hybrid surrogate model DF-STTN (Swin Transformer + TabTransformer) for full-field displacement prediction from spatial + non-spatial inputs; trained on high-fidelity FE data, then updated/validated on laboratory-scale tunnel excavation tests via a genetic-algorithm model-updating procedure that iteratively refines soil parameters using sparse test data (minimizing prediction error); outperforms convolution-based and single-fusion models; spatial info (3 measurement points) improves accuracy. One-way prediction with implemented GA-based model updating - no convergence criterion, no actuation.

*Full-text source: 04c-port*

**AH — strength & gap filled:** Fills the sparse-point surrogate gap for tunnel digital twins: the DF-STTN hybrid surrogate, pairing Swin Transformer and TabTransformer with dual-stage fusion, predicts full-field ground settlement and lining deformation for shield tunnels under adjacent excavation, trained on 1000 parametric finite-element samples and reaching R2 0.9898 and 0.9951, outperforming six baseline networks, with genetic-algorithm back-analysis estimating soil parameters within 4 percent error.

**AI — deficiencies & future work:** Validation rests on a scaled laboratory testbed with simplified boundary conditions, not field monitoring; time-dependent processes like consolidation and creep are ignored, settlement and lining deformation are modeled separately, and no real-time sensor link exists; future work targets field monitoring data, spatio-temporal Transformers, layered soil and groundwater, coupled models and continuous model updating.
