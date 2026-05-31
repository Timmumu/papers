---
ref: "[56]"
citekey: "Vickers2017"
title: "Digital twin: Mitigating unpredictable, undesirable emergent behavior in complex systems,"
authors: "M. Grieves and J. Vickers"
year: 2017
doi: ""
zotero_key: "UXYJS9VB"
zotero_status: verified
created: "2026-05-25"
tags:
  - Verified
---

# Vickers2017 — Digital Twin: Mitigating Unpredictable, Undesirable Emergent Behavior in Complex Systems

| Field | Value |
|-------|-------|
| **Ref** | [56] |
| **Authors** | M. Grieves, J. Vickers |
| **Year / Venue** | 2017 / Transdisciplinary Perspectives on Complex Systems, Springer, pp. 85–113 |
| **DOI** | 10.1007/978-3-319-38756-7_4 |
| **Zotero** | UXYJS9VB |

## Abstract ^sec-abstract
The chapter develops the *Digital Twin* concept as a vehicle for mitigating unpredictable, undesirable emergent behavior in complex systems. Grieves and Vickers trace the historical progression from information being inseparable from the physical object, through standardized measurement, to CAD descriptions, to dynamic simulations that capture not only form but behavior over time. They argue that the modern Digital Twin — increasingly *actionable* rather than merely descriptive — provides the analytical lens needed to anticipate emergent behavior that complex systems otherwise express only in operation. ^p1

## Introduction & Background ^sec-intro
The authors start from a historical observation: until standardized measurement (mid-1800s), information about physical objects was effectively bound to those objects, and interchangeable manufacturing was impossible. CAD eventually stripped a static digital representation away from the physical object, and in the last decades that representation has become dynamic, time-dependent, and able to simulate physical forces and behavior. ^p1

They then position the Digital Twin as the next step in this trajectory: a continuously updated, behavior-capable digital counterpart of the physical system that can be queried and exercised independently of the physical object, while remaining linked to it. ^p2

The chapter is also concerned with *complex systems* whose interactions produce emergent behavior — behavior that cannot be predicted from component specifications alone — and frames the DT as a means to surface, study, and ultimately mitigate such behavior before it causes harm. ^p3

## Method ^sec-method
The chapter is conceptual / theoretical rather than empirical. The authors construct the argument in three moves: (1) a historical narrative of how information became separable from objects; (2) a refinement of the DT definition (physical twin, virtual twin, and the data/process links between them) building on Grieves' earlier formulations; and (3) a discussion of how the DT can be used as an instrument to detect and mitigate emergent behavior in complex engineered systems. ^p1

Illustrative use cases — including aerospace and complex industrial systems — are used to ground the discussion of what "actionable" means in practice for prediction, what-if exploration, and operational decision support. ^p2

## Key Findings ^sec-results
- The DT is framed as the *actionable* successor to static CAD models and stand-alone simulations: it represents form, behavior, and behavior-over-time. ^f1
- Complex systems exhibit emergent behavior that component-level specs cannot predict; this is the gap the DT is positioned to close. ^f2
- A DT must couple a physical twin with a virtual twin via data and process links, and is most useful when used continuously over the asset's life. ^f3
- Treating the DT as an instrument for *mitigation* of emergent behavior reframes it from a documentation artifact to a risk-management tool. ^f4

## Discussion & Implications ^sec-discussion
This chapter is one of the foundational references for the modern DT discourse and supplies the canonical Grieves model (physical, virtual, link) that downstream taxonomies extend. Its emphasis on emergent behavior in complex systems makes it especially relevant for AECO, where projects are sociotechnical complex systems with unique site, schedule, and crew configurations. ^p1

The chapter does not provide an implementation blueprint or specific algorithms; it is a conceptual scaffold that later domain-specific work (manufacturing, infrastructure, construction) must operationalize. ^p2

## Conclusion ^sec-conclusion
Digital Twins, defined as continuously linked, actionable virtual counterparts of physical systems, provide a principled mechanism to anticipate and mitigate the unpredictable, undesirable emergent behavior characteristic of complex systems. ^p1

## Relevance to Cognitive Full-Lifecycle DT SLR ^sec-relevance
- **Lifecycle stage(s):** design, construction, operation, decommission (lifecycle-wide framing)
- **Cognitive capability:** prediction, reasoning, risk anticipation (theoretical scaffold)
- **Why cited in LR_cc.md:** Grieves & Vickers is one of the three theoretical pillars (alongside Tao's 5D framework and Sepasgozar's DT/DS/DM taxonomy) used in §3.4 to construct the SLR's three-level DT maturity classification.

## Traceability

| Claim in LR_cc.md | Evidence anchor |
|---|---|
| §3.4: "Drawing on the Grieves DT model [56], Tao's five-dimensional framework [30], and the DT–DS–DM taxonomy [72]…" | #^sec-abstract, #^f3 |
| Conceptual basis for distinguishing observation vs. action in DTs | #^f1, #^f4 |
| Motivation for treating AECO projects as complex systems requiring DT-based foresight | #^p3 (intro), #^p1 (discussion) |
