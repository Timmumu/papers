---
ref: "[12]"
citekey: "Zhang2024"
title: "Global BIM-point cloud registration and association for construction progress monitoring,"
authors: "Y. Zhang, L. Lu, X. Luo, and J. Pan"
year: 2024
doi: ""
zotero_key: "NHRTZV6T"
zotero_status: verified
created: "2026-05-25"
tags:
  - Verified
---

# Zhang2024 — Global BIM–Point Cloud Registration and Association for Construction Progress Monitoring

| Field | Value |
|-------|-------|
| **Ref** | [12] |
| **Authors** | Y. Zhang, L. Lu, X. Luo, J. Pan |
| **Year / Venue** | 2024 / Automation in Construction, vol. 168, Art. no. 105796 |
| **DOI** | Not provided in LR_cc.md reference list |
| **Zotero** | NHRTZV6T |

## Abstract ^sec-abstract
Traditional manual and semi-automatic BIM–point-cloud alignment approaches rely heavily on surveying control points and on manually picking equivalent point pairs, which is time-consuming and labor-intensive. The paper proposes an automatic algorithm for *global* BIM–point cloud registration and association to support construction progress monitoring. A distance-field representation is introduced to efficiently integrate BIM into registration tasks; a coarse-to-fine strategy combines a primitive-level coarse algorithm (rough alignment between BIM and point cloud) with a point-level fine registration approach that simultaneously refines pose and produces BIM–point associations. Extensive experiments on simulated and real construction-site data demonstrate promising registration and association performance. ^p1

## Introduction & Background ^sec-intro
Construction Progress Monitoring (CPM) is critical to project management. Despite intelligent pre-construction planning (e.g., cost estimation, resource scheduling), cost overruns and delays remain pervasive: a McKinsey report cited by the authors states that 98 % of mega-projects experience more than 30 % cost overruns. ^p1

CPM increasingly relies on capturing as-built reality via laser scanning and on comparing it to the as-designed BIM. The bottleneck is no longer data capture but the registration step that puts the point cloud into the BIM coordinate frame and associates each point to the right BIM element — historically done manually. ^p2

The paper therefore targets fully automatic global registration *and* element association, removing the dependency on surveyed control points or human-picked correspondences. ^p3

## Method ^sec-method
1. **Distance-field BIM representation.** BIM elements are encoded into a distance field that makes registration objective functions efficient and differentiable. ^p1
2. **Coarse alignment (primitive level).** A primitive-level algorithm provides a rough global alignment between BIM and the point cloud without requiring an initial guess. ^p2
3. **Fine registration with simultaneous association (point level).** A point-level algorithm refines pose while simultaneously associating each point to a BIM element, so registration and association are solved jointly rather than sequentially. ^p3
4. **Evaluation.** Extensive experiments on both simulation data and real construction-site data, reporting registration accuracy and association quality. ^p4

## Key Findings ^sec-results
- Encoding BIM as a distance field enables efficient integration of BIM geometry into the registration objective. ^f1
- A coarse-to-fine pipeline — primitive-level coarse alignment followed by point-level joint refinement and association — achieves robust *global* registration without surveyed control points or manual correspondences. ^f2
- Solving registration and BIM-element association *simultaneously* improves both, compared to staged pipelines. ^f3
- Reported performance on simulated and real-site data is "promising" across registration and association metrics, supporting field deployment for CPM. ^f4

## Discussion & Implications ^sec-discussion
The paper is a representative recent contribution in the perception/registration cluster of construction DTs: it automates the as-built ↔ as-designed alignment step that gates almost every quantitative progress-monitoring metric. ^p1

It also illustrates the SLR's Level-1 (Digital Shadow) maturity tier: the system observes physical state faithfully and feeds it into the digital model, but it does not yet close a control loop back to the physical site. ^p2

## Conclusion ^sec-conclusion
An automatic, global, distance-field-based BIM–point cloud registration and association algorithm makes scan-vs-design progress monitoring feasible without surveyed control points or manual correspondences. ^p1

## Relevance to Cognitive Full-Lifecycle DT SLR ^sec-relevance
- **Lifecycle stage(s):** construction (progress monitoring)
- **Cognitive capability:** perception, geometric reasoning, automated as-built ↔ as-designed alignment
- **Why cited in LR_cc.md:** Zhang2024 is the SLR's representative recent reference for automated progress monitoring and is invoked both in the perception/registration cluster (§3.2) and as a Level-1 Digital-Shadow exemplar (§3.4) that "observes but does not act."

## Traceability

| Claim in LR_cc.md | Evidence anchor |
|---|---|
| §3.2 cluster row "Perception, registration & computer vision" lists [12] | #^sec-abstract, #^f2 |
| §3.2: "Zhang et al. [12] extended registration to progress monitoring by associating point cloud clusters with BIM elements" | #^f3, #^p3 (method) |
| §3.4 Level-1 example: "as-built progress monitoring [12]" | #^p2 (discussion) |
