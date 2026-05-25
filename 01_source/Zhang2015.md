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
---

# Zhang2015

| Field | Value |
|-------|-------|
| **Ref** | [17] |
| **Title** | Ontology-based semantic modeling of construction safety knowledge: Towards automated safety planning for job hazard analysis (JHA), |
| **Authors** | S. Zhang, F. Boukamp, and J. Teizer |
| **DOI** | [10.1016/j.autcon.2015.02.005](https://doi.org/10.1016/j.autcon.2015.02.005) |



## Verified Evidence

### Construction Safety Ontology — Three Domain Models (Section 5)
^sec-ontology

> Construction Safety Ontology with 3 domain models: (1) Construction Product Model — IFC-based building elements (wall, slab, etc.); (2) Construction Process Model — Task→Activity→Job_Step hierarchy linked to resources; (3) Construction Safety Model — Potential_Hazard→Mitigation_Recommendation→Safety_Measure (Training, PPE, Safe_guard, Protective_Space, Inspection). OWL-based in Protégé. SWRL rules encode OSHA masonry regulations. Pellet reasoner for consistency; Jess rule engine for inference. 11 experts (117 years combined) validated: mean scores 1.45–1.91 on 6-point Likert (1=best).

**Supports:** LR_GPT.md §3.2 — "pioneered ontology-based modeling to formalize Job Hazard Analysis (JHA), enabling machine-readable deduction of spatial conflicts."

### SWRL Rules & BIM Integration (Section 7)
^sec-swrl-bim

> SWRL Rule 1: Limited Access Zone = wall height + 1219mm × wall length (OSHA 1926.706a). SWRL Rule 2: walls >2438mm (8ft) require bracing (OSHA 1926.706b). Prototype JHA Advisor (C#) integrated with Tekla BIM: auto-generates individuals from schedule + ontology → Jess inference → updated OWL → BIM visualization. 4D simulation with safety equipment timeline. Automatic JHA Excel report with 3D snapshots.

### Limitations (Section 8.1)
^sec-limitations

> (1) "JHA knowledge would not be able to consider construction site layout issues, since information such as terrain, site logistics, and construction equipment operation is currently not included"; (2) "it may currently not be possible to update BIM model frequently to reflect current construction site condition and schedule"; (3) "the developed prototype intends to assist human decision-making" — safety expert audit recommended; (4) IFC Construction Mgmt schema lacks safety — needs extension. Single construction method (masonry) validated.

**Critical:** Level 2 system — assists but does not replace human safety judgment. Rule-based only — no probabilistic reasoning or learning.
