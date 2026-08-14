---
ref: "[97]"
citekey: "Abdar2021"
title: "A review of uncertainty quantification in deep learning: Techniques, applications and challenges"
authors: "M. Abdar, F. Pourpanah, S. Hussain, D. Rezazadegan, L. Liu, M. Ghavamzadeh, P. Fieguth, X. Cao, A. Khosravi, U. R. Acharya, V. Makarenkov, S. Nahavandi"
year: 2021
journal: "Information Fusion"
volume: "76"
pages: "243-297"
doi: "10.1016/j.inffus.2021.05.008"
zotero_key: "HWPU8ZWP"
zotero_status: verified
created: "2026-05-31"
tags:
  - Uncertainty-Quantification
  - Deep-Learning
  - Bayesian
  - Ensembles
  - Review
  - Verified
  - source: scholar
  - identification: other methods
---

# Abdar2021

| Field | Value |
|-------|-------|
| **Ref** | [97] |
| **Title** | A review of uncertainty quantification in deep learning: Techniques, applications and challenges |
| **Authors** | Abdar, Pourpanah, Hussain, Rezazadegan, L. Liu, Ghavamzadeh, Fieguth, X. Cao, Khosravi, Acharya, Makarenkov, Nahavandi |
| **Venue** | Information Fusion, vol. 76, pp. 243-297, 2021 |
| **DOI** | 10.1016/j.inffus.2021.05.008 |
| **Zotero** | HWPU8ZWP (verified, full text PDF) |

## Abstract
^sec-abstract

> Uncertainty quantification (UQ) plays a pivotal role in the reduction of uncertainties during optimization and decision-making, and has been applied to solve many real-world problems. Bayesian approximation and ensemble learning techniques are two of the most widely used UQ methods in deep learning. This paper presents a comprehensive review of UQ methods used in recent deep-learning models, including techniques based on Bayesian Neural Networks (BNN), Monte Carlo Dropout, variational inference, deep ensembles, Gaussian processes hybrids, evidential deep learning, and conformal prediction. Applications surveyed include computer vision, NLP, medical imaging, and remote sensing. Challenges identified include calibration, computational cost, distinguishing aleatoric vs epistemic uncertainty, scalability to large models, and standard benchmarks. The paper articulates a research roadmap toward trustworthy AI.

## Core Claims
^sec-claims

- ① UQ in DL splits cleanly into **aleatoric** (data noise) and **epistemic** (model ignorance) — both are needed for safety-critical decisions.
- ② **Bayesian approximation** (BNN, MC-Dropout, VI) and **ensembles** are the two dominant families; evidential and conformal methods are emerging.
- ③ Calibration (e.g., Expected Calibration Error) is a persistent weakness — high accuracy does **not** imply trustworthy probabilities.
- ④ Computational cost is the principal barrier to deploying full Bayesian DL in real-time applications; lightweight approximations (last-layer Laplace, deep ensembles distilled to a single net) are pragmatic substitutes.

## Method
- Narrative survey covering 2015–2021 literature.
- Taxonomic organization by UQ technique and by application domain.

## Relevance to Cognitive DT (LR_cc.md Sec 4.3 + 6.2)
- Cited in [LR_cc.md Sec 4.3](LR_cc.md) as one of the only two studies (with [98] [[Grenyer2021]]) that explicitly model uncertainty in a DT pipeline — directly evidencing the 2.9% UQ-adoption gap claim.
- Cited again in [Sec 6.2](LR_cc.md) recommending Bayesian DL / evidential nets / conformal prediction as mature methods to be **adapted to construction contexts**.

## Limitations Noted
- AECO / construction applications are absent from the surveyed domains — confirming the LR_cc.md gap.
- Most surveyed methods evaluated on standard ML benchmarks (ImageNet, CIFAR), not multimodal site data.

## RP Alignment (Self-Improving CDT for DfX) ^sec-rp-alignment

Abdar2021 is the foundational UQ reference justifying the RP's methodological choice of **conformal prediction** as the calibration layer for O2's forward predictor.

### O2 — Why Conformal Prediction?

The review identifies five UQ families for deep learning. The RP's choice of conformal prediction (MAPIE library) over alternatives is justified by the specific requirements of a construction DT forward predictor:

| UQ Family | Strength | Why NOT chosen for O2 |
|---|---|---|
| Bayesian NN (BNN) | Full posterior over parameters | Computational cost prohibitive for GNN over large IFC graphs; MCMC does not scale to industrial BIM |
| MC-Dropout | Lightweight, drop-in | Calibration quality depends on dropout rate hyperparameter; no formal coverage guarantee |
| Deep Ensembles | SOTA calibration on benchmarks | Requires training 5–10 independent GNNs — infeasible on single-project data volumes |
| Evidential DL | Single-pass uncertainty | Immature; few open-source implementations; not tested on graph data |
| **Conformal Prediction** | Distribution-free, coverage guarantee, model-agnostic | ✅ Chosen: wraps any trained predictor with valid marginal coverage; computationally negligible |

The critical property for O2 is **coverage guarantee**: the conformal wrapper guarantees $P(y \in \hat{C}_\alpha(x)) \geq 1 - \alpha$ regardless of the underlying GNN's distribution. This is essential because:
1. O3's convergence argument requires bounded forward-operator error.
2. The falsifiability statement for O2 requires verifiable calibration (ECE deviation < 10 pp).
3. Construction-safety decisions carry asymmetric costs (false negatives cost more than false positives) — conformal prediction can be adapted to class-conditional coverage.

### Aleatoric vs. Epistemic Uncertainty — Direct RP Application

Abdar2021's taxonomy maps directly to the uncertainty sources identified in Ahmad-Chihadeh2026 (CRC/TRR 339 Digital Twin Road):
- **Aleatoric uncertainty** (irreducible data noise) → sensor noise, environmental variability, human reporting inconsistency in incident narratives
- **Epistemic uncertainty** (model ignorance) → limited training projects, unseen element configurations, novel construction methods

The RP's O2 must distinguish these: aleatoric uncertainty sets the *floor* for achievable prediction accuracy; epistemic uncertainty should *decrease* as O4 retrains on O3 iteration logs. This is a testable prediction of the self-improvement claim.

### The Calibration Gap in Construction DT

Abdar2021's finding that "high accuracy does NOT imply trustworthy probabilities" is directly relevant. If O2's GNN achieves 85% defect prediction accuracy with an ECE of 0.15, the raw probabilities are unreliable for O3's perturbation decisions. Conformal prediction fixes this by outputting *prediction sets* with guaranteed coverage, allowing O3 to make decisions with known uncertainty bounds.

### Strategic Positioning

**Cite as:** The authoritative UQ survey establishing that (a) UQ is essential for safety-critical DL, (b) multiple mature methods exist, and (c) none have been applied to AECO/construction. **Position O2 as:** "First application of conformal prediction to element-level DfX forecasting in a construction DT — motivated by Abdar2021's finding that calibration, not just accuracy, determines real-world trustworthiness."

## Traceability

| LR_cc.md | Claim | Evidence Block |
|----------|-------|----------------|
| Sec 4.3 | 2/70 DT studies model UQ | #^sec-abstract |
| Sec 6.2 | Bayesian DL, evidential, conformal as adaptable methods | #^sec-claims |
