---
ref: "[51]"
citekey: "Akinci2002"
title: "Automated generation of work spaces required by construction activities,"
authors: "A. Akinci, M. Fischer, and J. Kunz"
year: 2002
doi: "10.1061/(ASCE)0733-9364(2002)128:4(306)"
zotero_key: "SHAKQM77"
zotero_status: verified
created: "2026-05-25"
tags:
  - Verified
---

# Akinci2002 —Automated Generation of Work Spaces Required by Construction Activities

| Field | Value |
|-------|-------|
| **Ref** | [51] |
| **Authors** | Akinci, B.; Fischer, M.; Kunz, J. |
| **Year / Venue** | 2002 / Journal of Construction Engineering and Management 128(4), 306—15 |
| **DOI** | 10.1061/(ASCE)0733-9364(2002)128:4(306) |
| **Zotero** | SHAKQM77 |

## Abstract ^sec-abstract
To provide a safe and productive environment, project managers must plan the work spaces required by construction activities —representing many space types across 3D and time. With hundreds of activities per schedule, manual 4D specification is infeasible. The paper presents mechanisms that automatically generate project-specific work spaces from a generic work-space ontology combined with an IFC-based 4D production model. The result is a space-loaded production model enabling richer 4D CAD simulation, time–space conflict analysis and proactive work-space planning. ^p1

## Introduction & Background ^sec-intro
Space is a key construction resource; conflicts between crews, materials and equipment cause delays and accidents. Existing 4D tools required manual space specification, blocking adoption at realistic schedule sizes. ^p1

## Method ^sec-method
Authors define a generic work-space ontology (crew, equipment, hazard, protected, path, storage spaces) parameterised by activity method, then derive project-specific 3D space instances by binding ontology slots to IFC product geometry and schedule attributes. A reasoning module attaches each space to its activity with attributes (when, where, duration, volume). The resulting space-loaded model is fed into 4D simulation and conflict-detection rules. ^p1

## Key Findings ^sec-results
- A small, generic work-space ontology is sufficient to generate the diverse spaces needed by realistic schedules when bound to IFC + 4D data. ^f1
- Automatically generated spaces expose previously hidden time–space conflicts not visible in product-only 4D models. ^f2
- Proactive space planning becomes feasible at project scale rather than ad hoc activity-by-activity. ^f3

## Discussion & Implications ^sec-discussion
The paper is an early demonstration of ontology-driven semantic enrichment of BIM/4D for construction planning —a clear conceptual ancestor of cognitive DTs that combine semantic models with simulation to reason about emergent conditions on site. ^p1

## Conclusion ^sec-conclusion
Linking a work-space ontology to IFC-based 4D production models automates spatiotemporal planning and conflict detection. ^p1

## Relevance to Cognitive Full-Lifecycle DT SLR ^sec-relevance
- **Lifecycle stage(s):** Pre-construction planning and construction.
- **Cognitive capability:** Knowledge/ontology-driven reasoning over 4D models —semantic layer of a DT.
- **Why cited in LR_cc.md:** Early ontology + IFC reasoning that prefigures the semantic/cognitive layer of construction DTs.

## Traceability

| Claim in LR_cc.md | Evidence anchor |
|---|---|
| Ontologies + IFC enable automated 4D reasoning | #^f1 |
| DT semantic layers descend from early BIM ontology work | #^sec-discussion |
