---
ref: "[52]"
citekey: "El-Gohary2016"
title: "Semantic NLP-based information extraction from construction regulatory documents for automated compliance checking"
authors: "J. Zhang and N. M. El-Gohary"
year: 2016
journal: "Journal of Computing in Civil Engineering, 30(2): 04015014"
doi: "10.1061/(ASCE)CP.1943-5487.0000346"
zotero_key: "VDR5RZP3"
zotero_status: verified
created: "2026-05-25"
tags:
  - Verified
  - source: scholar
  - identification: other methods
---

# El-Gohary2016 — Semantic NLP for Automated Compliance Checking

| Field | Value |
|-------|-------|
| **Ref** | [52] |
| **Authors** | J. Zhang, N. M. El-Gohary |
| **Year / Venue** | 2016 / J. Computing in Civil Engineering 30(2):04015014 |
| **DOI** | [10.1061/(ASCE)CP.1943-5487.0000346](https://doi.org/10.1061/(ASCE)CP.1943-5487.0000346) |
| **Zotero** | VDR5RZP3 |

## Abstract ^sec-abstract

Automated regulatory compliance checking (ACC) requires extracting requirements from prose regulations and formalising them as computer-processable rules. This paper proposes a *semantic, rule-based NLP* approach that combines pattern-matching information-extraction (IE) rules and conflict-resolution (CR) rules using both syntactic features (POS tags, phrase-structure-grammar phrasal tags) and semantic features (concepts/relations from a construction-domain ontology). Two innovations — phrase-structure-grammar (PSG) phrasal tags and *separation-and-sequencing of semantic information elements* (SSSIE) — reduce the pattern count needed and boost recall. Tested on the International Building Code, the approach achieves precision 0.97 / recall 0.94 / F1 0.96. ^p1

## Introduction & Background ^sec-intro

US construction projects are governed by hundreds of overlapping regulations (IBC, ADA, OSHA, energy/fire codes, state and municipal codes). Prior ACC systems require manual rule encoding because off-the-shelf NLP cannot handle the complex, recursive sentence structures of regulatory prose. ^p1

The authors target three NLP/IE deficiencies of prior work: (1) shallow syntactic-only matching, (2) absence of a domain ontology to disambiguate domain-specific meaning, (3) rigid information templates that fail on complex sentences. The proposed approach takes a *deeper* semantic angle by binding pattern matching to ontology concepts. ^p2

## Method ^sec-method

Seven-phase pipeline: ^p1
1. **Information representation** — ACC-tuple intermediate plus Horn-clause logic sentences for deductive reasoning. ^p2
2. **Preprocessing** — tokenisation, sentence splitting, dehyphenation, morphological analysis. ^p3
3. **Feature generation** — POS tags (Hepple tagger, 53 symbols), PSG-based phrasal tags (Penn Treebank), gazetteer lists (comparative relations, units, negations), and ontology-based semantic features. ^p4
4. **Target information analysis** — define what semantic elements to extract (subject, compliance attribute, comparative relation, quantity value/unit, restrictions, deontic operators). ^p5
5. **Development of IE + CR rules** — pattern templates over syntactic+semantic features; CR rules resolve overlaps and ambiguities. ^p6
6. **Extraction execution** — applied iteratively to text. ^p7
7. **Evaluation** — against semi-automatically generated gold standard. ^p8

Two specific innovations: PSG phrasal tags compress recursive sentence structure into compact patterns; SSSIE separates each semantic element type into its own extraction pass and then sequences them, dramatically improving recall when one element is grammatically nested inside another. ^p9

## Key Findings ^sec-results

- **Syntactic vs semantic IE** (Section 1203 IBC 2006): semantic IE precision 0.96 / recall 0.92 / F1 0.94 vs syntactic-only 0.85 / 0.81 / 0.83 — a ~13 point F1 lift. ^f1
- **SSSIE vs without SSSIE** (Chapter 19 IBC 2009): SSSIE F1 0.96 vs without-SSSIE F1 0.79 — a ~17 point F1 lift, driven primarily by recall (0.95 vs 0.67). ^f2
- **Generalisation test** on held-out Chapter 19 IBC 2009: average precision 0.969, recall 0.944, F1 0.956. ^f3
- IE rules trained on Chapters 12+23 of IBC 2006 transfer to a new chapter without retraining — evidence the rules capture genuine regulatory-prose structure. ^f4

## Discussion & Implications ^sec-discussion

The authors position semantic NLP as the necessary substrate for ACC at scale: previous BIM-based code-checking efforts (Solibri, SMARTcodes etc.) require manual rule authoring per regulation, which doesn't scale across the ~50 US state code variants. ^p1

The PSG+SSSIE+ontology trio is offered as a generalisable recipe: any regulatory text whose grammar is constrained enough to admit pattern templates can be similarly processed. ^p2

## Conclusion ^sec-conclusion

A semantic-NLP IE pipeline that fuses PSG phrasal tags, an ontology, and SSSIE pattern separation can extract quantitative requirements from US building codes at near-human accuracy (F1 0.96), substantially outperforming syntactic-only baselines and enabling fully automated downstream compliance reasoning. ^p1

## Relevance to Cognitive Full-Lifecycle DT SLR ^sec-relevance

- **Lifecycle stage:** design / pre-construction (compliance pre-check) and construction (inspection-driven re-check).
- **Cognitive capability:** symbolic reasoning + domain-ontology grounding — the *knowledge representation* leg of a cognitive DT.
- **Why cited in LR_cc.md:** El-Gohary2016 anchors the SLR's argument that the cognitive layer of a DT must be able to **consume regulatory text and emit machine-checkable rules**, not just sensor data. It is the canonical reference for the NLP-grounded DfS / ACC pipeline that feeds the DT's reasoning module.

## RP Alignment (Self-Improving CDT for DfX) ^sec-rp-alignment

El-Gohary2016 is the **direct methodological ancestor of O1**. The RP's O1 replaces the 2016 hand-engineered IE pipeline with LLM-based extraction — but inherits the core architectural insight: *semantic features + domain ontology > syntactic-only extraction*.

### O1 Lineage

| Dimension | El-Gohary2016 (2016) | RP O1 (2026) | Evolution |
|---|---|---|---|
| **Method** | Hand-crafted IE rules (PSG + SSSIE) | LLM with structured-output prompting + GraphRAG | Manual patterns → neural semantic reasoning |
| **Ontology** | Construction-domain ontology for disambiguation | Esmaeili/Hallowell + Tixier DfS attribute schema | Single-domain → multi-attribute (safety/quality/sustainability) |
| **Input** | Regulatory prose (IBC chapters) | Emails, RFIs, specs, incident reports, site photos, ESG narratives | Single-genre → heterogeneous multimodal |
| **Scale bottleneck** | ~50 pattern templates per code chapter | Zero-shot via LLM; few-shot for domain adaptation | Does not scale across jurisdictions → scales via pretraining |
| **Validation** | F1 0.96 on IBC | Precision/recall + Cohen's κ on held-out documents | Near-human → expert-parity with audit trail |
| **Output** | ACC tuples → Horn-clause rules | IFC-element-linked JSON with source-span citation | Machine-checkable rules → human-auditable structured attributes |

The F1 0.96 on building-code extraction is the benchmark O1 must match or exceed — but on *unstructured heterogeneous project records*, a much harder task than regulatory prose (which is deliberately precise and formulaic). O1's falsifiability threshold (precision/recall > 0.70, κ > 0.6) reflects this increased difficulty.

### O3 Relevance

El-Gohary2016's ACC pipeline produces *deterministic compliance rules* from regulations. The RP's O3 inverts this: instead of checking design against fixed rules, O3 *modifies the design* to satisfy O2's predicted risk constraints. Both systems convert unstructured text into actionable design constraints — but O3 closes the loop that El-Gohary2016 opens.

### Strategic Positioning

**Cite as:** The canonical demonstration that semantic features + domain ontology are necessary for NLP extraction from AECO text (the "semantic lift" over syntactic-only is ~13 F1 points). **Position O1 as:** "El-Gohary2016's semantic-NLP paradigm, upgraded from hand-crafted IE rules to LLM-based extraction, and extended from single-source regulatory prose to heterogeneous multimodal project records."

## Traceability

| Claim in LR_cc.md | Evidence anchor |
|---|---|
| Semantic NLP can extract building-code requirements with F1 ≥ 0.94 | #^f1, #^f3 |
| Ontology + PSG outperforms syntactic-only IE | #^f1 |
| Manual rule encoding does not scale across US code variants | #^p1 (discussion) |
| ACC pipeline as input to a cognitive DT reasoning module | #^sec-relevance |
