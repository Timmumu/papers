---
ref: ""
citekey: "Mateusz-Poszaj-Mazurek2026"
title: "A workflow for LLM-assisted IFC data enrichment to support circular reuse of large-panel building systems in Poland"
authors: "Mateusz Płoszaj-Mazurek; Anna Tofiluk"
year: 2026
journal: "Journal of Building Engineering"
doi: "10.1016/j.jobe.2026.115397"
zotero_key: "2DB37KT5"
zotero_status: abstract-grounded
last_verified: "2026-06-15"
tags: ["AI", "BIM", "Building", "Construction", "Digital-Twin", "Semantic", "Unsorted", "source: lens", "identification: databases"]
---
# Mateusz-Poszaj-Mazurek2026 — A workflow for LLM-assisted IFC data enrichment to support circular reuse of large-panel building systems in Poland

| Field | Value |
|-------|-------|
| **Ref** | — |
| **Authors** | Mateusz Płoszaj-Mazurek; Anna Tofiluk |
| **Year / Venue** | 2026 · *Journal of Building Engineering* |
| **DOI** | [10.1016/j.jobe.2026.115397](https://doi.org/10.1016/j.jobe.2026.115397) |
| **Zotero** | `2DB37KT5` |
| **Screening** | V1: digital twins|bim|building information modelling \| V2: construction|building|buildings|concrete \| V3: semantic|artificial intelligence |

## Abstract ^sec-abstract

This paper examines how artificial intelligence can enhance digital workflows supporting the circular reuse of prefabricated building components. Focusing on Polish large-panel housing systems from the 1970s–1980s and their European counterparts, the study proposes a workflow that integrates Building Information Modelling (BIM), parametric processing and a large language model (LLM) for semantic enrichment of IFC data. The method identifies missing or ambiguous metadata within IFC models and uses LLM-based reasoning, supported by contextual lookup tables and expert oversight, to reconstruct attributes relevant to reuse and circularity assessments. The enriched dataset is then processed through a circularity algorithm and visualised in Grasshopper to evaluate component-level reuse potential. Results show that AI-assisted metadata reconstruction can substantially improve the completeness and interpretability of digital twins for demolition, adaptive reuse and material recovery scenarios. Beyond its technical contribution, the approach emphasises the ethical and cultural importance of stewardship, highlighting how digital tools may support the responsible management of post-war prefabricated heritage and reduce construction waste. This study is among the first to demonstrate how LLMs can semantically enhance IFC models for circularity assessments in prefabricated building systems. • Identifies gaps between computation and material reuse in prefabricated systems • Quantifies technical constraints affecting large-panel concrete reuse • Introduces a workflow linking BIM, IFC and AI for circularity assessment • Uses LLMs to semantically enrich IFC data and improve reuse databases • Supports physics-based and component-level decisions for concrete reuse • Demonstrates AI-assisted metadata reconstruction for legacy prefab buildings

## Introduction & Background ^sec-intro

Circular reuse of prefabricated building components is hampered by missing or ambiguous metadata in legacy models. Focusing on Polish large-panel housing systems (1970s–1980s) and European counterparts, the paper asks how AI can enhance digital workflows that support component-level reuse and circularity assessment.

## Method ^sec-method

The proposed workflow integrates BIM, parametric processing, and a large language model (LLM) for semantic enrichment of IFC data. The LLM, supported by contextual lookup tables and expert oversight, identifies and reconstructs missing/ambiguous IFC attributes relevant to reuse; the enriched dataset is processed by a circularity algorithm and visualised in Grasshopper to evaluate component-level reuse potential.

## Key Findings ^sec-results

AI-assisted metadata reconstruction substantially improves the completeness and interpretability of digital twins for demolition, adaptive reuse, and material-recovery scenarios. The study is among the first to show LLMs semantically enriching IFC models for circularity assessment in prefabricated systems, with attention to ethical/cultural stewardship of post-war heritage.

## Discussion & Implications ^sec-discussion

Directly relevant to the *NLP/LLM × BIM/DT* intersection of this review: it demonstrates LLM-based semantic enrichment of IFC as a route to more complete digital twins, linking data-enrichment to circular-economy decision-making. A concrete case of language models operating on structured building data.

## RP Alignment (Self-Improving CDT for DfX) ^sec-rp-alignment

This paper is direct evidence for O1's technical feasibility — it demonstrates LLM-based semantic enrichment of IFC models, which is a core capability O1 requires.

### O1 Relevance: LLM + IFC = Proven

Mateusz-Poszaj-Mazurek2026 shows that LLMs can reconstruct missing/ambiguous IFC metadata using contextual reasoning. For the RP's O1, this validates the claim that LLMs can operate over structured building data (IFC) — not just free text. O1 extends this from attribute reconstruction (filling in missing IFC fields) to attribute *extraction* (deriving new DfX risk attributes from unstructured project records and linking them to IFC elements).

### Sustainability Head (O2)

The paper's circularity algorithm consuming LLM-enriched IFC data directly prefigures O2's sustainability prediction head. Where Mateusz-Poszaj-Mazurek2026 uses LLM-enriched attributes for reuse-potential scoring, O2's sustainability head uses extracted embodied-carbon attributes (from EPD/ICE) and ESG-narrative features for element-level carbon prediction.

### Strategic Positioning

**Cite as:** Existence-proof that LLMs can semantically enrich IFC models with domain-relevant attributes. **Position O1 as:** "Mateusz-Poszaj-Mazurek2026 + extraction (not just reconstruction) + multimodal (not just IFC metadata) + DfX attributes (not just circularity)."

## Notes ^sec-notes

- **Screening:** Retained — DT + BIM/IFC + LLM/NLP + circular economy (strong topical fit).
- **Relevance:** Key exemplar for *LLM-assisted IFC enrichment* feeding DTs — aligns with this thesis's NLP-for-DT angle.
- **Source:** Hybrid OA; abstract-grounded, full text pending.
