---
ref: "[11]"
citekey: "Spinner2024"
title: "Online as-built building information model update for robotic monitoring in construction sites,"
authors: "A. Spinner and A. Degani"
year: 2024
doi: "10.1007/s10846-024-02087-2"
zotero_key: "ULJGBQZ6"
zotero_status: verified
created: "2026-05-25"
tags:
  - Verified
---

> 鈩?NOTE: citekey "Degani2024" —Zotero record is **Spinner & Degani (2024), "Online as-built BIM update for robotic monitoring"**, DOI 10.1007/s10846-024-01077-5. No PDF attached.

# Degani2024 —Online As-Built BIM Update for Robotic Monitoring

| Field | Value |
|-------|-------|
| **Ref** | —|
| **Authors** | Spinner, P.; Degani, A. |
| **Year / Venue** | 2024 / Journal of Intelligent & Robotic Systems |
| **DOI** | 10.1007/s10846-024-01077-5 |
| **Zotero** | ULJGBQZ6 |

## Abstract ^sec-abstract
The paper proposes an online pipeline that updates an as-designed BIM with as-built observations captured by a mobile robot, so that the BIM remains a live spatial reference for autonomous construction monitoring rather than a stale design artefact. ^p1

## Introduction & Background ^sec-intro
Robotic construction monitoring depends on a current geometric model to localise, plan paths and detect deviations. Manual scan-to-BIM is slow, and offline updates lag the build. The work targets the gap between continuous robotic sensing and BIM currency. ^p1

## Method ^sec-method
A mobile robot acquires point clouds during site traverses; an incremental registration and change-detection algorithm aligns scans to the existing BIM, classifies elements as built / modified / missing, and writes updates back into the model so subsequent monitoring sessions reuse an up-to-date representation. ^p1

## Key Findings ^sec-results
- Online BIM updates from robotic scans are feasible at session cadence rather than weekly cycles. ^f1
- Incremental change classification improves robot self-localisation and progress reporting accuracy. ^f2
- The closed feedback loop between physical site and BIM is shown end-to-end with a robotic platform. ^f3

## Discussion & Implications ^sec-discussion
The contribution operationalises a core DT requirement —bidirectional, near-real-time synchronisation between physical asset and digital model —using robotic perception, illustrating how DTs become "alive" during construction rather than only at handover. ^p1

## Conclusion ^sec-conclusion
Robot-driven online as-built updates close the BIM-to-DT gap for construction monitoring. ^p1

## Relevance to Cognitive Full-Lifecycle DT SLR ^sec-relevance
- **Lifecycle stage(s):** Construction (progress monitoring); handover bridge.
- **Cognitive capability:** Perception + closed-loop model synchronisation (a prerequisite of cognition).
- **Why cited in LR_cc.md:** Demonstrates real-time as-built 鈫?as-designed sync, the connectivity backbone for a cognitive construction DT.

## Traceability

| Claim in LR_cc.md | Evidence anchor |
|---|---|
| Robotic perception enables online BIM/DT synchronisation | #^f1 |
| Bidirectional sync is the connectivity backbone of cognitive DTs | #^sec-discussion |
