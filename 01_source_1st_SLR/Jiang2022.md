---
ref: "[25]"
citekey: "Jiang2022"
title: "Digital twin-enabled real-time synchronization for planning, scheduling, and execution in precast on-site assembly"
authors: "Y. Jiang, M. Li, M. Li, X. Liu, R. Y. Zhong, W. Pan, G. Q. Huang"
year: 2022
journal: "Automation in Construction 141, 104397"
doi: "10.1016/j.autcon.2022.104397"
zotero_key: "BEXVG4GB"
zotero_status: verified
last_verified: "2026-06-01"
tags:
  - Verified
  - Digital-Twin
  - Precast
  - Synchronization
  - Scheduling
  - source: scholar
  - identification: other methods
---

# Jiang2022 — DT-Enabled Real-Time Synchronization for Precast On-Site Assembly

| Field | Value |
|-------|-------|
| **Ref** | [25] |
| **Authors** | Y. Jiang, M. Li, M. Li, X. Liu, R. Y. Zhong, W. Pan, G. Q. Huang |
| **Year / Venue** | 2022 / Automation in Construction 141, 104397 |
| **DOI** | [10.1016/j.autcon.2022.104397](https://doi.org/10.1016/j.autcon.2022.104397) |
| **Zotero** | BEXVG4GB |


## Abstract ^sec-abstract
Proposes a Digital Twin synchronization framework that bridges planning, scheduling and execution for precast on-site assembly. The system continuously aligns the as-planned digital schedule with as-built progress captured from on-site sensing, enabling closed-loop replanning when actual operations deviate from plan. ^p1

## Method ^sec-method
Design-science framework with a working prototype on a precast on-site assembly testbed. The system fuses real-time positioning and progress data with the BIM/4D schedule via a synchronization middleware; rescheduling is triggered by deviation detection. ^p1

## Key Findings ^sec-results

- Real-time digital-physical synchronization is the structural prerequisite for closed-loop construction scheduling — without it, plans drift silently from execution. ^f1

- Deviation-triggered rescheduling reduces idle time and resource conflicts in precast assembly relative to static daily look-ahead planning. ^f2

- Synchronization integrity (not sensing) is the dominant bottleneck in current construction DT prototypes. ^f3


## Discussion & Implications ^sec-discussion
A canonical reference for data-centric construction DTs and for the argument that synchronization middleware — not BIM richness — is the key enabling component for cognitive construction DTs. ^p1

## Relevance to Cognitive Full-Lifecycle DT SLR ^sec-relevance
Lifecycle stage: construction execution. Used in LR_cc.md to characterize data-centric DT architectures and to evidence the synchronization-integrity gap. ^p1

## Traceability

| Claim in LR_cc.md | Evidence anchor |
|---|---|

| Synchronization middleware is the structural enabler | #^f1 |

| Synchronization integrity dominates current DT bottlenecks | #^f3 |
