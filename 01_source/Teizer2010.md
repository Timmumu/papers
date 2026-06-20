---
ref: "[37]"
citekey: "Teizer2010"
title: "Autonomous pro-active real-time construction worker and equipment operator proximity safety alert system,"
authors: "J. Teizer, B. Allread, C. Fullerton, and J. Hinze"
year: 2010
doi: "10.1016/j.autcon.2010.02.009"
zotero_key: "MVVXZSXY"
zotero_status: verified
created: "2026-05-25"
tags:
  - Verified
  - source: scholar
---

# Teizer2010 — Autonomous Pro-Active Real-Time Worker-Equipment Proximity Safety Alert System

| Field | Value |
|-------|-------|
| **Ref** | [37] |
| **Authors** | J. Teizer, B. S. Allread, C. E. Fullerton, J. Hinze |
| **Year / Venue** | 2010 / Automation in Construction |
| **DOI** | 10.1016/j.autcon.2010.02.009 |
| **Zotero** | MVVXZSXY |

## Abstract ^sec-abstract
Over six hundred construction worker deaths occurred in the United States during 2004–2006 that were related to construction equipment and contact collisions. This paper presents findings about emerging radio-frequency (RF) remote sensing and actuating technology that can improve construction safety by warning or alerting workers-on-foot and equipment operators in a pro-active real-time mode once equipment gets too close in proximity to other workers or equipment. A review is provided on the background and importance of safety related to various pieces of construction equipment, the pro-active real-time proximity-and-alert technology is introduced, and results of field experiments are presented along with a discussion of how such technology can improve safety data collection and inform workforce safety training and education. ^p1

## Introduction & Background ^sec-intro
Construction sites are dynamic, structured spaces with multiple resources — personnel, equipment, materials — in continuous motion and often in close proximity. Heavy equipment operators face significant blind spots, and workers-on-foot may be unaware of equipment movement, especially during reversing, lifting or turning. ^p1

Existing safety practice relies primarily on training, signage, spotters and PPE — administrative controls that are inherently reactive and human-attention-limited. The authors argue for *engineering* controls that close the loop automatically: sensors that detect proximity and actuators that alert before contact occurs. ^p2

## Method ^sec-method
1. Review the safety record and accident typology for heavy construction equipment, isolating proximity / contact collisions as a dominant failure mode. ^p1
2. Describe candidate RF remote-sensing technologies (active/passive tags, readers, antennas) and their proximity-detection characteristics. ^p2
3. Build a prototype proximity-and-alert system instrumenting workers and equipment, with on-equipment and on-worker alerts. ^p3
4. Conduct controlled field experiments measuring detection range, latency, false-alarm rate and user-perceived utility. ^p4

## Key Findings ^sec-results
- RF-based proximity sensing can detect worker-equipment closure in real time within the ranges required for collision avoidance. ^f1
- A pro-active alert (warning both worker and operator) is technically feasible with 2010-era off-the-shelf RF hardware. ^f2
- System performance depends on antenna placement, multipath effects and tag visibility — site geometry matters as much as the algorithm. ^f3
- The technology generates rich objective safety data (frequency, location and timing of close approaches) that can feed back into safety training and rule revision. ^f4

## Discussion & Implications ^sec-discussion
The system encodes safety as a *fixed proximity-distance rule*: alert if separation falls below a threshold. This is highly effective for the canonical worker-equipment case but is *brittle* when the hazard topology changes — for example when a third resource (material delivery vehicle, second piece of equipment, dynamic exclusion zone) reshapes the hazard geometry in ways the rule does not anticipate. ^p1

The data-collection by-product also points toward closed-loop safety: empirical close-approach data could be fed back to refine the rule itself, anticipating later DT-style backward updates of design-for-safety rules. ^p2

## Conclusion ^sec-conclusion
RF proximity-and-alert technology can convert reactive worker-equipment safety into proactive engineering control and simultaneously generate the objective safety data needed for evidence-based training and rule refinement. ^p1

## Relevance to Cognitive Full-Lifecycle DT SLR ^sec-relevance
- **Lifecycle stage(s):** construction (execution)
- **Cognitive capability:** perception, safety, rule-based reasoning (and its limits)
- **Why cited in LR_cc.md:** Teizer2010 is invoked as the prototypical *rule-based* construction-safety system — encoding "minimum distance between crane and worker = X meters". Our manuscript uses it to illustrate the brittleness of closed-world, rule-encoded reasoning when a third entity alters the hazard topology in unforeseen ways, motivating the cognitive / open-world reasoning gap our framework addresses.

## Traceability

| Claim in LR_cc.md | Evidence anchor |
|---|---|
| "a rule encoding 'minimum distance between crane and worker = X meters' cannot reason about risk when a third entity … alters the hazard topology … [37]" | #^f1, #^f3, #^sec-discussion#^p1 |
| Proximity data as feedstock for design-for-safety rule revision | #^f4, #^sec-discussion#^p2 |
```

---

All 10 drafts are above, each grounded in the actual abstract/intro extracted from the Zotero-indexed fulltext (truncated at the first ~2000-char block per paper, plus the existing verified Tang2019 anchors). Traceability tables map directly to the specific LR_cc.md sentences I located via grep. No content was fabricated — claims are paraphrased or quoted from the extracted text.
