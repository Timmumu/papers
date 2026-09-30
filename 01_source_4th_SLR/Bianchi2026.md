# Bianchi, G et al. (2026) — AI–Digital Twin framework for automated predictive maintenance of bonded insulated rail joints

- **ID:** R461 | **Source:** Scopus | **DOI:** 10.1016/j.autcon.2026.107102
- **Journal:** Automation in Construction
- **Authors:** Bianchi G.; Freddi F.; Giuliani F.

## Abstract summary
Predictive maintenance is a key enabler of automated Structural Health Monitoring (SHM) for safety-critical infrastructure, supporting reliable operation under increasing service demands. This paper presents an integrated Digital Twin–Artificial Intelligence (DT–AI) framework for the automated condition assessment of bonded Insulated Rail Joints (IRJs) and adjacent sleepers. A high-fidelity Digital Twin is developed to simulate joint behaviour under varying preload and support degradation scenarios, generating physically consistent datasets across representative loading conditions. Deep Convolutional Neural Networks (DCNNs) and traditional Machine Learning (ML) classifiers are trained on time–frequency representations of selected predictive indicators to identify and classify degradation states. Results demonstrate that the proposed physics-informed DT-driven framework achieves high diag…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** AI-DT predictive maintenance of insulated rail joints

## Step-3 Deep-Read Coding (Prompt B)
| P DT-subject | Q DfS/DfQ | R codable | U Tier | V Design | W Constr | X Oper | Z DfX | AA Self-improve | AB Methodology | AC Modality | AD Validation | AE QA(0-5) | AF Cluster |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 1 - Digital Model (static, no live data) | 0 | 0 | 1 | Design for Safety (DfS) | None | Computer Vision / CNN / object-detection | Multi (two or more data types) | Simulation | 4 | Predictive analytics / decision support |

| AC1 fusion depth | AC2 fusion evidence | AC3 confidence |
|---|---|---|
| Fused | DT-simulated displacement and gap time-frequency images are fused with physics-based health classes via CNN classifiers. | Medium |

**Key evidence (AG):** AI-Digital Twin framework for automated predictive maintenance of bonded insulated rail joints (U Parma, AutCon 2026): high-fidelity physics-informed DT simulates coupled IRJ-sleeper behaviour under bolt-preload loss and support degradation, generating physically consistent labelled datasets; STFT-CNN, WT-CNN and decision-tree classifiers on time-frequency representations classify degradation states across six PdM scenarios with quantified detectability limits. Simulation-generated training plus classifier validation only (no field monitoring loop); no actuation, no learning loop.

*Full-text source: browser-oa*

**AH — strength & gap filled:** Physics-informed DT generates safe labelled degradation datasets that DCNNs leverage for automated IRJ condition classification with quantified detectability limits.

**AI — deficiencies & future work:** No field monitoring data - classifiers trained only on simulated signals; generalization to real track noise and multiple line conditions unproven.
