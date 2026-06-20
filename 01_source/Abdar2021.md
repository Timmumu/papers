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

## Traceability

| LR_cc.md | Claim | Evidence Block |
|----------|-------|----------------|
| Sec 4.3 | 2/70 DT studies model UQ | #^sec-abstract |
| Sec 6.2 | Bayesian DL, evidential, conformal as adaptable methods | #^sec-claims |
