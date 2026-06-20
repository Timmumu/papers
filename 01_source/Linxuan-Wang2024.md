---
ref: ""
citekey: "Linxuan-Wang2024"
title: "Towards digital-twin-enabled facility management: the natural language processing model for managing facilities in buildings"
authors: "Linxuan Wang; Nanjiang Chen"
year: 2024
journal: "Intelligent Buildings International"
doi: "10.1080/17508975.2024.2370372"
zotero_key: "SNT6NQNK"
zotero_status: abstract-grounded
last_verified: "2026-06-15"
tags: ["Building", "Construction", "Digital-Twin", "Facility-Management", "Knowledge-Graph", "Unsorted", "source: lens", "identification: databases"]
---
# Linxuan-Wang2024 — Towards digital-twin-enabled facility management: the natural language processing model for managing facilities in buildings

| Field | Value |
|-------|-------|
| **Ref** | — |
| **Authors** | Linxuan Wang; Nanjiang Chen |
| **Year / Venue** | 2024 · *Intelligent Buildings International* |
| **DOI** | [10.1080/17508975.2024.2370372](https://doi.org/10.1080/17508975.2024.2370372) |
| **Zotero** | `SNT6NQNK` |
| **Screening** | V1: digital twin|digital-twin \| V2: construction|building|buildings|facility management \| V3: knowledge graph |

## Abstract ^sec-abstract

Facility management is an essential part of the building which encompasses multiple service areas and processes to ensuring optimum functionality of the facility. Digital twin (DT) has been increasingly introduced to the FM domain to facilitate FM tasks such as decision-making. Despite the advancements in DT-enabled FM, there still exists a problem in the disconnections between DT academics and FM practitioners. The emergence of knowledge management can act as a bridge between academics and FM practitioners. To mine knowledge in the DT-enabled FM industry for a better communication between different stakeholders and timely decisions in the case of emergency, this study proposes a natural language processing (NLP)-based approach. A detailed classification of FM-related entities is first presented, which divides the FM into five categories. The NLP model is used to extract entities and knowledge from a large volume of text data. The results indicate that an NLP-based approach can accurately extract FM-related knowledge. The findings of this study not only provide a basis for automatic DT-enabled FM-related knowledge extraction but also support the downstream tasks such as knowledge graph construction and FM-related emergency decision-making.

## Introduction & Background ^sec-intro

**Digital twin (DT)** has been increasingly introduced to FM but disconnections exist between DT academics and FM practitioners. The study proposes an **NLP-based approach** for knowledge extraction in DT-enabled FM to bridge this gap.

## Method ^sec-method

A detailed FM entity classification (five categories). NLP model extracts entities and knowledge from large text volumes to support knowledge graph construction and emergency decision-making.

## Key Findings ^sec-results

NLP-based approach accurately extracts FM-related knowledge, providing a basis for automatic DT-enabled FM knowledge extraction and supporting downstream tasks like KG construction.

## Discussion & Implications ^sec-discussion

**Highly relevant** — NLP + DT + FM + knowledge extraction. Directly informs the semantic-DT and cognitive-DT strands.

## RP Alignment (Self-Improving CDT for DfX) ^sec-rp-alignment

This paper provides evidence for O1's downstream knowledge-graph component. The five-category FM entity classification and NLP extraction pipeline directly prefigure O1's GraphRAG over Neo4j: both convert unstructured text into structured, queryable knowledge graphs linked to building elements.

**O1 relevance:** Linxuan-Wang2024 shows NLP can extract FM entities from text with sufficient accuracy to populate a knowledge graph. O1 extends this from FM-domain text to heterogeneous construction-project records (emails, RFIs, incident reports) and links extracted entities to IFC elements rather than abstract FM categories. The knowledge graph construction is the shared architectural pattern.

**O3 relevance:** The paper's motivation — bridging the gap between DT academics and FM practitioners through structured knowledge — mirrors O3's role in making O2 predictions actionable for design decision-makers. Both systems convert machine reasoning into human-consumable structured knowledge.

**Strategic positioning:** Cite as evidence that NLP→KG pipelines are proven in DT-FM contexts. Position O1's GraphRAG as "Linxuan-Wang2024's NLP→KG paradigm, extended to multimodal construction records with IFC-element grounding."

## Notes ^sec-notes

- **Screening:** Retained — NLP + DT + FM + knowledge extraction (strong fit).
- **Relevance:** High; cite for NLP-DT FM knowledge extraction.
- **Source:** Bronze OA; abstract-grounded, full text pending (PDF in library).
