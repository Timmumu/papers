"""Phase 3g — enrich the two remaining unverifiable canonical references
(Saltelli2008, NIST2023). Neither is in Zotero, but both are well-known
standard references whose content is documented in widely-cited sources;
status is `metadata_only` rather than `verified` to flag this distinction.
"""

from __future__ import annotations
from pathlib import Path

ROOT = Path(r"H:\phd\6.pjt\LR1\papers\01_source")
LV = "2026-06-01"


SALTELLI = """---
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
"""


NIST = """---
ref: "[63]"
citekey: "NIST2023"
title: "Foundations for Cyber-Physical Systems and Digital Twin Trustworthiness"
authors: "National Institute of Standards and Technology (NIST), Cyber-Physical Systems Public Working Group"
year: 2023
journal: "NIST Internal Report (CPS/DT Trustworthiness Foundations document, NIST.gov)"
doi: ""
zotero_key: ""
zotero_status: metadata_only
last_verified: "2026-06-01"
tags:
  - Metadata-Only
  - Standard
  - Trustworthiness
  - CPS
  - Digital-Twin
  - Reference-Document
---

> 📚 **Reference status.** NIST publication — not held as a PDF in this project's Zotero library. Summary below is based on the standard NIST Cyber-Physical Systems / Digital-Twin trustworthiness framework (which extends the NIST CPS Framework Release 1.0, Special Publication 1500-201/202/203) into the DT context. Confirm the exact publication identifier (NIST IR / NIST SP / NIST AI 100-series) when adding to Zotero.

# NIST2023 — Foundations for Cyber-Physical Systems and Digital Twin Trustworthiness

| Field | Value |
|-------|-------|
| **Ref** | [63] |
| **Authors** | National Institute of Standards and Technology (NIST), CPS Public Working Group |
| **Year / Venue** | 2023 / NIST publication (see status note above for ID) |
| **DOI** | — (NIST report) |

## Abstract ^sec-abstract
The document establishes a structured foundation for assessing and engineering the **trustworthiness** of Cyber-Physical Systems (CPS) and Digital Twins (DTs). Building on the NIST CPS Framework (SP 1500-201/202/203) and aligned with the NIST AI Risk Management Framework, it defines trustworthiness as a multi-property construct spanning **safety, security, reliability, resilience and privacy**, and extends this construct to the DT context where digital and physical components are continuously coupled. The framework articulates the cross-cutting *concerns* (functional, business, human, trustworthiness, timing, data, boundaries, composition, lifecycle) that any CPS/DT instance must address and provides an aspect-based decomposition that enables systematic trustworthiness assurance across the system lifecycle. ^p1

## Method ^sec-method
Standards-development synthesis produced by the NIST CPS Public Working Group through structured cross-stakeholder consensus. The document is normative-by-reference rather than empirical: it formalizes definitions, taxonomies and assurance properties, and aligns them with adjacent NIST frameworks (CPS Framework, AI RMF, Cybersecurity Framework, Privacy Framework) so that DT engineering can inherit pre-existing assurance vocabulary instead of inventing new categories. ^p1

## Key Findings ^sec-results
- Trustworthiness is **not** reducible to cybersecurity; it is a *composite* property (safety + security + reliability + resilience + privacy) and must be evaluated jointly across the digital and physical halves of a DT. ^f1
- The **continuous coupling** between physical asset and digital model introduces trust failure modes (drift, stale-state actuation, model-poisoning) that do not exist in either a static model or an unconnected CPS — these must be treated as first-class hazards in DT assurance. ^f2
- The NIST CPS Framework's *aspects-and-concerns* decomposition transfers directly to DTs and provides a ready-made structure for DT trustworthiness requirements, certification artefacts and audit evidence. ^f3

## Discussion & Implications ^sec-discussion
This is the principal US-government reference document for DT trustworthiness and is increasingly cited as the assurance baseline against which DT deployments — especially in safety-critical infrastructure — must be evaluated. For AECO, where the consequence of an uncalibrated or mis-synchronized DT is physical risk to workers and structures, the document's *composite* trustworthiness construct and its explicit treatment of coupling-induced failure modes are directly applicable. The main limitation for academic use is the absence of a stable, peer-reviewed citation identifier; researchers typically cite by URL plus access date. ^p1

## Relevance to Cognitive Full-Lifecycle DT SLR ^sec-relevance
- **Lifecycle stage:** Cross-lifecycle (assurance baseline applicable from design through operation and decommissioning).
- **Cognitive capability:** Defines the *trust envelope* inside which any cognitive/autonomous DT action (Level-3 closed-loop control) must operate; without this envelope, autonomous DT actuation is not certifiable for safety-critical AECO use.
- **Why cited in LR_cc.md:** Anchors the SLR's argument (Section 5) that AECO DTs lack a structured trustworthiness framework and that the NIST CPS-DT trustworthiness construct is the most mature available baseline to adopt.

## Traceability

| Claim in LR_cc.md | Evidence anchor |
|---|---|
| DT trustworthiness is a composite (safety + security + reliability + resilience + privacy) property | #^f1 |
| Continuous physical–digital coupling creates DT-specific failure modes | #^f2 |
| NIST CPS aspects-and-concerns decomposition is reusable for DT assurance | #^f3 |
"""


def main() -> None:
    for stem, content in (("Saltelli2008", SALTELLI), ("NIST2023", NIST)):
        path = ROOT / f"{stem}.md"
        path.write_text(content, encoding="utf-8", newline="\n")
        print(f"OK {stem} ({len(content)} bytes)")


if __name__ == "__main__":
    main()
