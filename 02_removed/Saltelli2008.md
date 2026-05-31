---
ref: "[47]"
citekey: "Saltelli2008"
title: "Global Sensitivity Analysis: The Primer"
authors: "A. Saltelli, M. Ratto, T. Andres, F. Campolongo, J. Cariboni, D. Gatelli, M. Saisana, S. Tarantola"
year: 2008
journal: "John Wiley & Sons, Chichester (ISBN 978-0-470-05997-5)"
doi: ""
zotero_key: ""
zotero_status: metadata_only
last_verified: "2026-06-01"
tags:
  - Metadata-Only
  - Sensitivity-Analysis
  - Uncertainty-Quantification
  - Reference-Book
---

> 📚 **Reference status.** Canonical textbook — not held as a PDF in this project's Zotero library. Metadata and content summary below are based on the widely-cited Wiley first edition (ISBN 978-0-470-05997-5). Add to Zotero as a `book` item when access is available.

# Saltelli2008 — Global Sensitivity Analysis: The Primer

| Field | Value |
|-------|-------|
| **Ref** | [47] |
| **Authors** | Saltelli, A.; Ratto, M.; Andres, T.; Campolongo, F.; Cariboni, J.; Gatelli, D.; Saisana, M.; Tarantola, S. |
| **Year / Venue** | 2008 / John Wiley & Sons, Chichester |
| **ISBN** | 978-0-470-05997-5 |
| **DOI** | — (book) |

## Abstract ^sec-abstract
*Global Sensitivity Analysis: The Primer* is the standard practitioner reference for variance-based and screening-based global sensitivity analysis (GSA). The book systematizes the distinction between **local** sensitivity analysis (one-at-a-time derivatives evaluated at a nominal point) and **global** sensitivity analysis (sensitivity averaged over the entire input space under specified distributions). It develops the mathematical and computational machinery for the main GSA families — Morris elementary effects (screening), variance-based Sobol' indices (first-order and total-order), FAST/eFAST, and density-based and moment-independent methods — and provides design guidance on sampling, convergence diagnostics and result interpretation. ^p1

## Method ^sec-method
Pedagogical synthesis built around a recurring set of test functions and worked examples. Each method is introduced with its mathematical definition, an algorithmic recipe, and a Monte-Carlo / quasi-Monte-Carlo implementation pattern. The book emphasizes (i) input-distribution specification as a first-class modelling decision, (ii) the difference between *factor prioritisation* (which inputs to investigate) and *factor fixing* (which inputs can be fixed at any value without affecting the output variance), and (iii) the computational cost of each estimator family. ^p1

## Key Findings ^sec-results
- Variance-based Sobol' first-order ($S_i$) and total-order ($S_{T_i}$) indices give an unambiguous, model-free decomposition of output variance and should be the default GSA reporting standard for non-linear, non-monotonic models. ^f1
- Morris elementary-effects screening is the cheapest defensible method for prioritising inputs in high-dimensional models before committing to a full variance-based analysis. ^f2
- Reporting only local (OAT) sensitivities is misleading for non-linear models and is identified as a recurring failure mode in applied modelling. ^f3

## Discussion & Implications ^sec-discussion
The book is the most-cited single source for variance-based GSA across science and engineering and is the de-facto reference cited by UQ tooling (SALib, OpenTURNS, UQLab) and by domain reviews of model uncertainty. Its insistence that GSA should be a routine step in model validation — not an optional post-hoc analysis — has shaped the way uncertainty is reported across simulation-heavy disciplines including Digital Twin engineering. ^p1

## Relevance to Cognitive Full-Lifecycle DT SLR ^sec-relevance
- **Lifecycle stage:** Cross-lifecycle (model validation / uncertainty quantification underpinning prediction in DTs).
- **Cognitive capability:** Provides the mathematical substrate for **confidence-aware prediction** — a precondition for cognitive (Level-3) DTs that must communicate calibrated uncertainty to downstream decision-making.
- **Why cited in LR_cc.md:** Anchors Section 4.3's argument that AECO DTs currently report point predictions without variance-based sensitivity decomposition, and motivates the SLR's recommendation that Sobol'-style GSA become a default DT-validation step.

## Traceability

| Claim in LR_cc.md | Evidence anchor |
|---|---|
| Variance-based Sobol' indices are the default GSA standard | #^f1 |
| Morris screening is the cheap-and-defensible first pass | #^f2 |
| Local OAT sensitivity is misleading for non-linear DT models | #^f3 |
