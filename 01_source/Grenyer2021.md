---
ref: "[98]"
citekey: "Grenyer2021"
title: "A systematic review of multivariate uncertainty quantification for engineering systems"
authors: "A. Grenyer, J. A. Erkoyuncu, Y. Zhao, R. Roy"
year: 2021
journal: "CIRP Journal of Manufacturing Science and Technology"
volume: "33"
pages: "188-208"
doi: "10.1016/j.cirpj.2021.03.004"
zotero_key: "NLAZ35NI"
zotero_status: verified
created: "2026-05-31"
tags:
  - Uncertainty-Quantification
  - Multivariate
  - Engineering-Systems
  - Systematic-Review
  - Verified
  - source: scholar
---

# Grenyer2021

| Field | Value |
|-------|-------|
| **Ref** | [98] |
| **Title** | A systematic review of multivariate uncertainty quantification for engineering systems |
| **Authors** | A. Grenyer, J. A. Erkoyuncu, Y. Zhao, R. Roy |
| **Venue** | CIRP Journal of Manufacturing Science and Technology, vol. 33, pp. 188-208, May 2021 |
| **DOI** | 10.1016/j.cirpj.2021.03.004 |
| **Zotero** | NLAZ35NI (verified, full text PDF) |

## Abstract
^sec-abstract

> Engineering systems increasingly rely on integrated, multi-sensor, multi-physics models, where uncertainty arises in many correlated variables simultaneously. This paper presents a systematic review of multivariate uncertainty quantification (UQ) methods, contrasting them with the dominant univariate practice. The authors classify methods along three axes: representation (probability boxes, copulas, polynomial chaos, Dempster-Shafer evidence theory), propagation (Monte Carlo, surrogate models, polynomial chaos expansion), and aggregation (joint vs marginal, sensitivity analysis). Application domains covered include manufacturing, aerospace, structural engineering, and prognostics & health management. Open challenges identified: tractable joint distributions in high dimensions, dependence modelling, computational cost of propagation, and lack of standard benchmarks for comparison.

## Core Claims
^sec-claims

- ① **Multivariate** UQ is materially different from stacked univariate UQ — ignoring dependence leads to mis-estimation of system-level risk.
- ② **Copulas, polynomial chaos, and Dempster-Shafer** are the three mature representations; each has trade-offs in expressiveness vs computability.
- ③ Surrogate-assisted Monte Carlo is the dominant propagation strategy for expensive engineering models.
- ④ Engineering UQ lacks **standard benchmarks**, hampering systematic comparison — a gap directly mirrored in AECO DT (see LR_cc.md Sec 4.3).

## Method
- PRISMA-style systematic review of UQ methods in engineering systems literature.
- Three-axis classification (representation / propagation / aggregation).

## Relevance to Cognitive DT (LR_cc.md Sec 4.3 + 6.2)
- Cited in [LR_cc.md Sec 4.3](LR_cc.md) as the second of two studies that explicitly model uncertainty in a DT-relevant pipeline (paired with [97] [[Abdar2021]]).
- Cited again in [Sec 6.2](LR_cc.md) as evidence that mature UQ methodologies exist in adjacent engineering disciplines and can be adapted to construction DT.

## Limitations Noted
- AECO / construction-specific case studies are absent.
- Computational cost of full multivariate propagation remains a barrier for online DT use.
- No common benchmark dataset hinders reproducibility.

## Traceability

| LR_cc.md | Claim | Evidence Block |
|----------|-------|----------------|
| Sec 4.3 | Multivariate UQ in engineering DT | #^sec-abstract |
| Sec 6.2 | Adaptable UQ methods from adjacent fields | #^sec-claims |
