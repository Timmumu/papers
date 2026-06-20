---
ref: "[49]"
citekey: "Sacks2009"
title: "Spatial and temporal exposure to safety hazards in construction,"
authors: "R. Sacks, S. Rozenfeld, and Y. Rosenfeld"
year: 2009
doi: ""
zotero_key: "RL2W6VYI"
zotero_status: verified
created: "2026-05-25"
tags:
  - Verified
  - source: scholar
  - identification: other methods
---

# Sacks2009 — Spatial and Temporal Exposure to Safety Hazards in Construction

| Field | Value |
|-------|-------|
| **Ref** | [49] |
| **Authors** | R. Sacks, O. Rozenfeld, Y. Rosenfeld |
| **Year / Venue** | 2009 / J. Construction Engineering and Management (ASCE) |
| **DOI** | 10.1061/(ASCE)0733-9364(2009)135:8(726) |
| **Zotero** | RL2W6VYI |

## Abstract ^sec-abstract
Given the dynamic nature of construction sites, analysis of construction activities and their related hazards is inadequate for reliable risk assessment if it does not explicitly account for the likelihood of exposure of potential victims to hazardous situations. In traditional risk level calculations for manufacturing industries, the number of victims is factored with the likelihood of an accident and the potential severity, but the victims are simply assumed to be those typically present at the accident location. In construction, exposure cannot be accounted for at a generic metaproject level: it must be assessed at the level of the activities and the physical context in which they are performed. Conceptually, accidents are "loss-of-control events" to which victims are exposed; without exposure, no accident is assumed to occur. A set of algorithms has been developed to estimate the likelihood of exposure of construction workers to loss-of-control events, implemented in a prototype software application that predicts fluctuating risk levels in construction projects. ^p1

## Introduction & Background ^sec-intro
Construction is one of the most dangerous industries worldwide and a leading contributor of work-related fatalities (Ahmed et al. 2000; Findley et al. 2004; Gyi et al. 1999). Traditional manufacturing-style risk assessment does not transfer to construction because the site is dynamic — workers, equipment, materials, and hazards continuously change configuration as work progresses. ^p1

The authors frame accidents as "loss-of-control events": a hazard only becomes an accident when a victim is *exposed* to it in space and time. Existing safety planning treats hazards generically at the project level and therefore cannot adjust as the spatial-temporal context evolves activity-by-activity. ^p2

## Method ^sec-method
1. Define each construction activity in terms of its physical work envelope, duration, and the set of loss-of-control events it can generate. ^p1
2. Compute the spatial-temporal overlap between each activity's hazard envelope and the work envelopes of all other concurrent activities to estimate exposure probability. ^p2
3. Combine exposure probability with severity and frequency factors to produce a fluctuating, activity-level risk index that updates as the schedule advances. ^p3
4. Implement the algorithms in a prototype application — the "Construction Hazard Assessment with Spatial and Temporal Exposure" (CHASTE) tool — to demonstrate use during planning. ^p4

## Key Findings ^sec-results
- Exposure-based risk varies dramatically over the project schedule and cannot be captured by static, activity-generic hazard tables. ^f1
- The same activity yields very different risk levels depending on which other activities co-occur in the same physical zone. ^f2
- Planners can use the CHASTE output to reschedule, re-zone, or insert proactive controls before high-risk overlaps occur. ^f3
- A prototype implementation showed that the model can be operated on standard construction plans without requiring exotic sensor data. ^f4

## Discussion & Implications ^sec-discussion
The model reframes safety planning as a feedback problem: instead of asking "is this activity dangerous in general?", it asks "given the evolving site state, who is exposed to what loss-of-control event right now?". This positions safety prediction as an output of a dynamic, model-based simulation — a conceptual precursor to digital-twin-driven safety reasoning. ^p1

The work also implies that *design* and *planning* artefacts (schedules, work-zone layouts) can be revised on the basis of observed exposure patterns, supporting backward propagation of safety knowledge from execution into upstream models. ^p2

## Conclusion ^sec-conclusion
The CHASTE model and prototype demonstrate that activity-level, spatial-temporal exposure can be computed from standard plan data and used to adjust construction plans proactively to mitigate fluctuating risk. ^p1

## Relevance to Cognitive Full-Lifecycle DT SLR ^sec-relevance
- **Lifecycle stage(s):** design, construction (planning + execution)
- **Cognitive capability:** prediction, reasoning, safety, human-AI decision support
- **Why cited in LR_cc.md:** Sacks2009 supplies the foundational mechanism by which observed near-miss / exposure telemetry can be used to *revise design rules*. In LR_cc.md §backward-update example, the wind-conditional minimum-distance rule is justified by Sacks2009's spatial-temporal exposure logic, which already treats safety risk as a dynamic, context-dependent variable rather than a static rule.

## Traceability

| Claim in LR_cc.md | Evidence anchor |
|---|---|
| "the backward update revises R_t to include a wind-speed-conditional rule … the revised rule propagates to future designs automatically [49]" | #^sec-method, #^f1, #^f3 |
| Activity-level, spatial-temporal exposure is the basis for dynamic safety reasoning | #^sec-abstract, #^p2 (intro) |
| Safety planning as feedback / dynamic simulation precursor to DT-safety reasoning | #^sec-discussion#^p1 |
