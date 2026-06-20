---
ref: "[53]"
citekey: "Schleich2017"
title: "Shaping the digital twin for design and production engineering,"
authors: "J. B. Schleich, N. Anwer, L. Mathieu, and S. Wartzack"
year: 2017
doi: "10.1016/j.cirp.2017.04.040"
zotero_key: "MNQ7TJ9H"
zotero_status: verified
created: "2026-05-25"
tags:
  - Verified
  - source: scholar
  - identification: other methods
---

# Schleich2017 — Shaping the Digital Twin for Design and Production Engineering

| Field | Value |
|-------|-------|
| **Ref** | [53] |
| **Authors** | B. Schleich, N. Anwer, L. Mathieu, S. Wartzack |
| **Year / Venue** | 2017 / CIRP Annals — Manufacturing Technology |
| **DOI** | 10.1016/j.cirp.2017.04.040 |
| **Zotero** | MNQ7TJ9H |

## Abstract ^sec-abstract
In today's highly competitive markets, the ambitions for shortening time-to-market and increasing product development performance fuel the application of sophisticated virtual product models, frequently referred to as digital twins. Enabled by the digitalization of manufacturing, cyber-physical production systems, model-based system engineering, and the growing endeavour for data gathering and processing, these models are increasingly enriched with production and operation data. Current approaches to the implementation of digital twins lack a conceptual basis, which hinders applicability of the digital twin vision to various activities in design and production engineering. This paper proposes a comprehensive reference model that serves as a digital twin of the physical product in design and production engineering, defining key model properties (scalability, interoperability, expansibility, fidelity) and lifecycle operations (composition, decomposition, conversion, evaluation). ^p1

## Introduction & Background ^sec-intro
Virtual product models have moved from CAD geometry through PLM toward "digital twins" intended to mirror a physical artefact across its lifecycle. The authors observe that despite intense industrial interest, the digital twin is being used as a buzzword without a shared conceptual basis, particularly for *design* and *production engineering* activities, where geometric and dimensional variation must be represented faithfully. ^p1

They argue that without a reference model and well-defined operations, digital twins cannot support the early, efficient assessment of design decisions or predict the consequences of design and process choices on product behaviour without resorting to costly physical mock-ups. ^p2

## Method ^sec-method
1. Survey existing digital twin definitions and identify the lack of a conceptual reference model for design/production engineering. ^p1
2. Propose a reference model in which the digital twin is an *evolving* set of linked models (geometry, behaviour, tolerances, manufacturing process) rather than a single static 3D file. ^p2
3. Define four key properties the model must satisfy: scalability, interoperability, expansibility, and fidelity. ^p3
4. Define four lifecycle operations on the model: composition, decomposition, conversion, and evaluation, illustrated with skin model shapes for geometrical variations. ^p4

## Key Findings ^sec-results
- A digital twin in design/production is best understood as a *family* of related models, not a single artefact. ^f1
- Fidelity is task-dependent: the same physical product needs different model abstractions for tolerance analysis, simulation, and operations. ^f2
- The four operations (composition / decomposition / conversion / evaluation) make explicit what users actually *do* with a digital twin throughout the lifecycle. ^f3
- Skin model shapes are a concrete representation enabling realistic geometric variation analysis inside the digital twin. ^f4

## Discussion & Implications ^sec-discussion
By insisting on conceptual rigour, the paper provides one of the first explicit "shapes" of a DT for engineering. The reference model anticipates the lifecycle continuity that DTs are now expected to deliver: design intent and as-manufactured data must be represented together, with operations to convert between abstraction levels on demand. ^p1

The framework is manufacturing-centric but maps cleanly onto AECO: many AECO DT efforts re-invent these properties (scalability, fidelity) without acknowledging the precision-manufacturing lineage that motivated them. ^p2

## Conclusion ^sec-conclusion
The paper supplies a conceptual reference model and operation set that anchor the otherwise diffuse digital-twin discourse, particularly for the design and production-engineering stages of the product lifecycle. ^p1

## Relevance to Cognitive Full-Lifecycle DT SLR ^sec-relevance
- **Lifecycle stage(s):** design, production engineering
- **Cognitive capability:** reasoning, prediction, model fidelity
- **Why cited in LR_cc.md:** Schleich2017 is cited as evidence that the DT paradigm was *initially conceptualized for aerospace and precision manufacturing*. It provides the conceptual reference model that AECO DT work later adapts, motivating our argument that BIM-only practice in AECO lacks the model-property and operation rigour already standard in manufacturing DTs.

## Traceability

| Claim in LR_cc.md | Evidence anchor |
|---|---|
| "DT paradigm — initially conceptualized for aerospace and precision manufacturing [53]" | #^sec-abstract, #^sec-intro#^p1 |
| Need for a conceptual basis / reference model for DTs | #^sec-method, #^f1, #^f3 |
