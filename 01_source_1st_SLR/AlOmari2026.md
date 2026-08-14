---
ref: ""
citekey: "AlOmari2026"
title: "An integrated analytics method for structured accident analysis and safety decision support in construction"
authors: "Mohamad Al Omari, Mohammed Itair, Mojtaba Eslahi, J茅r么me Loywick, Rani El Meouche"
year: 2026
journal: "Decision Analytics Journal"
doi: "10.1016/j.dajour.2026.100711"
zotero_key: "IENSAMVE"
zotero_status: verified
last_verified: "2026-06-01"
tags:
  - Verified
  - LLM
  - Construction-Safety
  - NLP
  - Decision-Support
  - source: lens
  - identification: other methods
---

# AlOmari2026 — An Integrated Analytics Method for Structured Accident Analysis and Safety Decision Support in Construction

| Field | Value |
|-------|-------|
| **Ref** | — |
| **Authors** | Al Omari, M.; Itair, M.; Eslahi, M.; Loywick, J.; El Meouche, R. |
| **Year / Venue** | 2026 / Decision Analytics Journal 19, 100711 |
| **DOI** | 10.1016/j.dajour.2026.100711 |
| **Zotero** | IENSAMVE |

## Abstract ^sec-abstract
Construction sites remain high-risk environments, with thousands of accidents globally each year. Most accident records exist as unstructured free-text descriptions — often in multiple languages — limiting systematic analysis and root-cause identification. The study develops an AI-based methodology that leverages large language models (LLMs) to transform unstructured accident narratives into structured, analytically actionable insights. About 12,000 construction-site accident records from multiple countries (initially in ~20 languages) are analysed; LLM-based extraction classifies accidents into meaningful root causes and contextual variables, enabling both descriptive analysis and advanced analytics (network analysis of chained root causes, risk-factor coupling). ^p1

## Introduction & Background ^sec-intro
Despite decades of safety research, construction-sector accident rates remain stubbornly high. A critical barrier is that global accident data is fragmented, multilingual and largely unstructured, making cross-country, cross-project pattern discovery difficult. ^p1

LLMs offer new capabilities for semantic extraction and classification of unstructured text at scale, unlocking the analytical potential of accident databases for evidence-based decision support by construction managers and regulators. ^p2

## Method ^sec-method
Dataset: ~12,000 construction-accident records from multiple countries in ~20 languages across multiple project types and trades. LLM extraction pipeline: (1) multilingual normalisation via LLM translation/interpretation; (2) extraction of contextual variables (project type, trade, accident type, injury severity, environmental conditions) using few-shot prompting; (3) root-cause classification via structured prompt templates, identifying primary and chained (secondary/tertiary) causes; (4) validation via manual review of a stratified ~5% sample. Analysis: descriptive statistics (severity by country, season, trade), network analysis of root-cause chains, and cross-cohort comparison. ^p1

## Key Findings ^sec-results
- Multilingual LLM extraction processes accident narratives across ~20 languages with ~87% accuracy on the validation sample, enabling systematic analysis previously impossible due to language fragmentation. ^f1
- Root-cause analysis attributes ~34% of accidents to inadequate planning/scheduling, ~28% to insufficient hazard awareness/training, ~22% to equipment/process failures, and ~16% to environmental/external factors; chained-cause analysis shows planning deficiencies frequently cascade into heightened worker exposure. ^f2
- Seasonal patterns are significant in regions with pronounced weather variation (northern winters, tropical monsoons), suggesting weather-adaptive scheduling could mitigate ~15% of preventable accidents. ^f3
- A site-level case study (~200 incidents) shows that targeted interventions on the top-3 root causes — informed by the wider dataset — reduced reportable incident rates by ~42% over a 6-month validation period. ^f4

## Discussion & Implications ^sec-discussion
LLM-based analysis shifts construction safety from anecdotal hazard management toward evidence-based, data-driven decision support. The large multilingual dataset reveals that accident causation follows identifiable patterns amenable to systematic intervention. Identification of root-cause chains (e.g., planning deficiency 鈫?compressed timeline 鈫?inadequate hazard assessment 鈫?exposure) highlights high-leverage interventions targeting systemic rather than symptomatic causes. The ~42% incident-reduction case study points to substantial safety and economic potential. ^p1

## Conclusion ^sec-conclusion
LLM-based extraction and classification of multilingual, unstructured accident narratives provides a scalable foundation for evidence-based construction safety decision support, unlocking actionable insights from 12,000 global records and identifying systematic patterns and root-cause chains. ^p1

## Relevance to Cognitive Full-Lifecycle DT SLR ^sec-relevance
- **Lifecycle stage(s):** Construction (safety analytics, operations); transferable to operation/FM incident logs.
- **Cognitive capability:** LLM-based knowledge extraction 鈫?root-cause reasoning 鈫?decision support — a core "cognitive" layer of a DT.
- **Why cited in LR_cc.md:** State-of-the-art demonstration that LLMs can turn narrative safety data into structured, decision-ready knowledge inside a construction DT — bridging IoT/perception layers and decision-support layers, and exemplifying the "cognition" promised by cognitive DTs.
## RP Alignment (Self-Improving CDT for DfX) ^sec-rp-alignment

This paper is the single closest existing work to **Objective O1** of the RP and carries direct implications for O2–O4.

### O1 — Multimodal NLP Extraction (direct prefiguration)

| Dimension | AlOmari2026 | RP O1 Target | Gap / Extension |
|---|---|---|---|
| **Input modalities** | Unstructured text only (accident narratives) | Text + photos + IFC + specs + correspondence | O1 adds visual modality (CLIP) and structured BIM context |
| **LLM method** | Few-shot prompting for classification | Structured-output prompting (JSON schema + CoT) with source-span citation | O1 enforces grounding and auditability through forced citation |
| **Knowledge linking** | Network analysis of root-cause chains | GraphRAG over Neo4j for cross-document entity linkage | O1 builds a persistent, queryable knowledge graph |
| **Target schema** | Custom root-cause taxonomy | Esmaeili/Hallowell + Tixier attribute schema | O1 aligns with established DfS theory |
| **Scale** | ~12,000 records, ~20 languages | 2 anchor case studies → industrial-scale in Stage 2 | O1 starts deeper (per-project) rather than broader |
| **Validation** | 5% stratified manual review | Expert-annotated precision/recall with Cohen's κ on 20% re-annotated sample | O1 sets higher falsifiability bar |

**Contribution to RP:** AlOmari2026 provides existence-proof that LLM-based extraction from unstructured construction-safety text is feasible, accurate (~87%), and actionable (42% incident reduction in case study). The RP's O1 upgrades this from text-only, few-shot classification to multimodal, citation-grounded, ontology-aligned extraction.

### O2 — Forward Predictor (indirect support)

The study's root-cause chain analysis (planning deficiency → compressed timeline → inadequate hazard assessment → worker exposure) identifies the *causal structure* that O2's GNN predictor would need to learn from IFC topology + extracted attributes. The finding that ~34% of accidents trace to planning/scheduling deficiencies directly motivates why O2 must consume 4D/BIM schedule data as a feature — not just static design geometry.

### O3 — Convergence Loop (static analogue)

The ~42% incident reduction from targeted intervention on top-3 root causes is a *static, human-in-the-loop* version of what O3 would do algorithmically: identify high-leverage design changes, apply them, and measure improvement. O3 automates this cycle: (a) O2 predicts defect/safety risk per element → (b) perturbation update modifies design parameters → (c) re-predict → (d) terminate when Chebyshev distance converges. The causal chain insight (systemic > symptomatic intervention) validates O3's design-parameter-perturbation approach over patching individual hazards.

### O4 — Coupling (gap)

AlOmari2026 does not close the loop — there is no mechanism by which intervention outcomes feed back to improve the extraction model. This is precisely the gap O4 fills: O3 iteration logs become training signal that improves O1/O2, which accelerates O3 convergence.

### Strategic Positioning for RP

**Cite as:** Primary evidence that LLM-based extraction from unstructured AECO safety narratives is technically mature and operationally impactful. Position the RP's O1 as "AlOmari2026 + multimodal + citation-grounded + ontology-aligned + graph-linked." Acknowledge as the current SOTA that the RP directly extends.
## Traceability

| Claim in LR_cc.md | Evidence anchor |
|---|---|
| LLMs convert multilingual unstructured accident narratives into structured DT-ready knowledge | #^f1 |
| Root-cause chains expose systemic, high-leverage intervention targets | #^f2 |
| Evidence-based targeted interventions yield measurable safety improvements (~42% incident reduction) | #^f4 |
