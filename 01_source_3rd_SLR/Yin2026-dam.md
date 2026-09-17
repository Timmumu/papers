# Yin et al. (2026) — Topology guided fourier neural operator with decoupled geometric parameterization for dam leakage detection

- **ID:** 3667 | **Source:** Scopus | **DOI:** 10.1016/j.cacaie.2026.100073
- **Journal:** Computer-Aided Civil and Infrastructure Engineering
- **Authors:** Yin, C.; Liang, Y.; Pan, X.; Xu, B.; Zhang, B.

## Abstract summary
Traditional electrical resistivity tomography (ERT) inversion for dam leakage detection faces heavy computational loads and smoothness priors that fail to localize anomalies. This study introduces the Topology-Guided Fourier Neural Operator framework. A Fourier Neural Operator replaces the numerical solver based on the governing equations, speeding up forward potential field simulations. To easily locate anomalies, a decoupled geometric parameterization separates the deterministic defect from the stochastic background. A Navigator network extracts coarse topological priors to initialize a parallel multi-hypothesis workflow. Tested across multiple trials, the framework achieves a 99.7% average success rate and an 89.3% high-fidelity reconstruction rate. It accelerates forward modeling by 345 times and overall inversion by 72 times compared to finite element methods. The method detects uns…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** FNO dam leakage detection for operational DTs; safety monitoring

## Step-3 Deep-Read Coding (Prompt B)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow (one-way physical to virtual) | 0 | 0 | 1 | Design for Safety (DfS) | Implemented | Other / Mixed | Single (one data type) | Simulation | 4 | Predictive analytics / decision support |

**Key evidence (AG):** Topology-guided Fourier Neural Operator (TG-FNO) with decoupled geometric parameterization for dam leakage detection (Chongqing Jiaotong U/HKUST): FNO replaces numerical solver for forward potential-field simulation (345x speedup, mean rel error 3.18%); decoupled geometric parameterization separates deterministic defect from stochastic background; Navigator network extracts coarse topological priors to initialize parallel multi-hypothesis workflow; 99.7% avg inversion success rate, 89.3% high-fidelity reconstruction, 72x overall acceleration vs FEM; robust to 20% noise and 50% data loss, detects unseen low-contrast early leakages, OOD generalization without retraining. One-way ERT->inversion->leakage localization for safety monitoring; implemented operator-learning surrogate (offline-trained), no actuation.


**Strength & gap filled (AH):** Overcomes the conflict between smoothness priors and sharp leakage boundaries in ERT dam monitoring: a topology-guided Fourier neural operator with decoupled geometric parameterization and a Navigator warm start localizes dam leakage with 99.7% success and 89.3% high-fidelity rates, accelerating forward modeling 345-fold and inversion 72-fold versus finite element methods, while remaining stable under 20% noise and 50% data loss.

**Deficiencies & future work (AI):** Evaluation is entirely numerical on synthetic 2D datasets with single circular anomalies; the parameterization restricts detection to predefined shapes, spectral truncation distorts geometry, and the simulation-to-reality gap leaves field deployment untested. Future work adopts level-set representations, synchrosqueezed wavelet transforms, and libraries of condition-specific operators.
**Fusion depth (AC1):** SINGLE

**Fusion evidence (AC2):**
- **Data streams:** ERT potential-field measurements (synthetic 2D datasets with single circular anomalies).
- **Integration mechanism:** none - one modality feeds the Fourier neural operator (345x forward speedup, 99.7% inversion success, robust to 20% noise / 50% loss).
- **Why this code:** SINGLE (AC=Single).

**Confidence (AC3):** High.
(full-text source: Endnote)
