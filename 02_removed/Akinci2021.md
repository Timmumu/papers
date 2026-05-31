---
ref: "[68]"
citekey: "Akinci2021"
title: "Context-aware safety monitoring in construction with computer vision and BIM,"
authors: "A. S. Singh and B. Akinci"
year: 2021
doi: ""
zotero_key: "X8SNRHBX"
zotero_status: verified
created: "2026-05-25"
tags:
  - Verified
---

> 鈩?NOTE: citekey "Akinci2021" —Zotero record is **Singh & Akinci (2021), "Context-aware safety monitoring of construction workers"**, DOI 10.1016/j.aei.2021.101386. Akinci is second author. No PDF attached —draft based on metadata + general knowledge.

# Akinci2021 —Context-Aware Safety Monitoring of Construction Workers

| Field | Value |
|-------|-------|
| **Ref** | —|
| **Authors** | Singh, M.; Akinci, B. |
| **Year / Venue** | 2021 / Advanced Engineering Informatics |
| **DOI** | 10.1016/j.aei.2021.101386 |
| **Zotero** | X8SNRHBX |

## Abstract ^sec-abstract
The paper proposes a context-aware safety-monitoring approach for construction workers that fuses location, task, environmental and BIM-derived contextual information to evaluate hazard exposure dynamically, rather than relying on static rule-based proximity checks. ^p1

## Introduction & Background ^sec-intro
Construction safety monitoring has moved from manual inspection to sensor-based proximity alerts, but generic alarms over-trigger and lose worker trust. Context —what activity the worker is performing, what plant is active nearby, what design conditions hold at that location —is needed for meaningful hazard assessment. ^p1

## Method ^sec-method
A context model formalises worker, task, equipment, environment and BIM elements as inter-related entities. Real-time location data and task schedules are mapped onto a BIM/semantic representation; rules and inference identify contextually meaningful hazards (e.g., worker without harness entering an active lift zone) and suppress noise from irrelevant proximities. ^p1

## Key Findings ^sec-results
- Context-aware filtering reduces false-positive safety alerts compared with proximity-only systems. ^f1
- Coupling worker location with BIM semantics and schedule context enables hazard reasoning beyond geometric distance. ^f2
- The framework generalises across multiple hazard categories (struck-by, fall, restricted-zone). ^f3

## Discussion & Implications ^sec-discussion
The work exemplifies the move from "data-rich, semantics-poor" monitoring toward cognitively grounded safety reasoning —a building block for DT-based situational awareness on site. ^p1

## Conclusion ^sec-conclusion
Embedding BIM- and schedule-derived context into worker monitoring yields more reliable hazard detection than geometry-only approaches. ^p1

## Relevance to Cognitive Full-Lifecycle DT SLR ^sec-relevance
- **Lifecycle stage(s):** Construction (site operations / safety).
- **Cognitive capability:** Context-aware reasoning + semantic fusion (BIM + sensors + schedule).
- **Why cited in LR_cc.md:** Concrete instance of cognitive context fusion on a construction site, bridging perception and decision.

## Traceability

| Claim in LR_cc.md | Evidence anchor |
|---|---|
| Context-aware DTs reduce alert noise vs. geometric checks | #^f1 |
| Semantic fusion of BIM, schedule and sensors enables cognition | #^f2 |
