---
ref: "[17]"
citekey: "Zhang2015"
title: "Ontology-based semantic modeling of construction safety knowledge: Towards automated safety planning for job hazard analysis (JHA),"
authors: "S. Zhang, F. Boukamp, and J. Teizer"
year: 2015
doi: "10.1016/j.autcon.2015.02.005"
zotero_key: "GPNWB45Y"
zotero_status: verified
created: "2026-05-25"
tags:
  - Verified
  - source: scholar
  - identification: other methods
---

# Zhang2015 — Ontology-Based Semantic Modeling of Construction Safety Knowledge for JHA

| Field | Value |
|-------|-------|
| **Ref** | [17] |
| **Authors** | S. Zhang, F. Boukamp, J. Teizer |
| **Year / Venue** | 2015 / Automation in Construction, vol. 52, pp. 29–41 |
| **DOI** | [10.1016/j.autcon.2015.02.005](https://doi.org/10.1016/j.autcon.2015.02.005) |
| **Zotero** | GPNWB45Y |

## Abstract ^sec-abstract
Construction safety knowledge and project-specific information are scattered and fragmented, and despite advances in IT a link between safety management and information models has been missing. The paper investigates a new approach to organize, store, and re-use construction safety knowledge through a *Construction Safety Ontology* formalizing safety management knowledge. The ontology comprises three main domain models — Construction Product Model, Construction Process Model, and Construction Safety Model — and is evaluated through one-on-one expert interviews. Interaction with BIM is explored, and a prototype application of ontology-based job hazard analysis (JHA) and visualization illustrates applicability and effectiveness. The ontology enables more effective inquiry of safety knowledge and is positioned as the first step toward automated safety planning for JHA using BIM. ^p1

## Introduction & Background ^sec-intro
The authors observe that roughly 90 % of workplace injuries trace back to gaps between safety knowledge and project execution. Safety knowledge is dispersed across regulations, standards, manuals, and tacit expert experience, while project information lives in BIM and schedules; there is no shared semantic layer that lets one reason across both. ^p1

JHA — the systematic identification of hazards associated with each job step — is therefore manual, expert-dependent, and difficult to keep in sync with evolving designs. The paper proposes ontology engineering as the appropriate response, because ontologies provide a formal, machine-interpretable representation that can be shared across tools and inferred over. ^p2

## Method ^sec-method
1. **Three-domain ontology.** Construction Product Model (IFC-based building elements), Construction Process Model (Task→Activity→Job_Step hierarchy linked to resources), Construction Safety Model (Potential_Hazard → Mitigation_Recommendation → Safety_Measure: Training, PPE, Safe_guard, Protective_Space, Inspection). ^p1
2. **Encoding & reasoning.** OWL ontology in Protégé; SWRL rules encode OSHA masonry regulations; Pellet reasoner for consistency checks; Jess rule engine for inference. ^p2
3. **Expert evaluation.** 11 experts (117 years combined experience) rated ontology constructs on a 6-point Likert scale (1=best), yielding mean scores of 1.45–1.91. ^p3
4. **BIM integration prototype ("JHA Advisor", C#).** Generates ontology individuals from schedule + ontology, runs Jess inference, writes updated OWL back, and visualizes safety equipment in Tekla; produces 4D simulation and an automatic Excel JHA report with 3D snapshots. ^p4

Representative SWRL rules: Limited Access Zone = wall height + 1219 mm × wall length (OSHA 1926.706a); walls > 2438 mm (8 ft) require bracing (OSHA 1926.706b). ^p5

## Key Findings ^sec-results
- A three-domain Construction Safety Ontology can formalize fragmented safety knowledge in a machine-interpretable form. ^f1
- SWRL/OWL with a rule engine can encode prescriptive safety regulations (OSHA masonry) and infer hazards from BIM-derived individuals. ^f2
- Expert evaluation (n=11, 117 yrs combined experience) returned mean scores 1.45–1.91 on a 6-point scale, supporting the ontology's validity. ^f3
- The JHA Advisor prototype demonstrates end-to-end ontology→BIM→4D visualization and auto-generated JHA reports, evidencing operational feasibility. ^f4

## Discussion & Implications ^sec-discussion
The ontology is a *semantic* counterpart to Zhang2013's rule engine: where Zhang2013 detects geometric fall hazards directly from a BIM model, Zhang2015 makes the *knowledge* about hazards explicit, sharable, and inferable. This is the move from rule-checking to knowledge-based reasoning. ^p1

Limitations noted by the authors include scope (masonry; specific regulation excerpts), reliance on accurate scheduling and BIM data, and the open challenge of keeping the ontology synchronized with regulatory updates and lessons learned from incidents. ^p2

## Conclusion ^sec-conclusion
A formal Construction Safety Ontology provides the semantic backbone needed to make JHA automatable and re-usable across projects, and integrates naturally with BIM and 4D scheduling. ^p1

## Relevance to Cognitive Full-Lifecycle DT SLR ^sec-relevance
- **Lifecycle stage(s):** design, construction (planning)
- **Cognitive capability:** semantic reasoning, knowledge representation, automated hazard inference
- **Why cited in LR_cc.md:** Zhang2015 is the SLR's canonical citation for "ontology-based modeling to formalize JHA" (§3.2) and is reused in both the Semantic Interoperability and DfS clusters; it also exemplifies the forward-only reasoning limitation the SLR critiques in §5.

## Traceability

| Claim in LR_cc.md | Evidence anchor |
|---|---|
| §3.2: "Zhang et al. [17] pioneered ontology-based modeling to formalize JHA, enabling machine-readable deduction of spatial conflicts…" | #^sec-abstract, #^f1, #^f2 |
| Cluster rows "Semantic interoperability & ontologies" and "Design-for-Safety (DfS) automation" both include [17] | #^p1 (method), #^f4 |
| §5: brittleness of forward-only rule bases when confronting novel compound risks | #^p2 (discussion) |
