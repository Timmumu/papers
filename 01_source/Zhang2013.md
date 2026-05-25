---
ref: "[16]"
citekey: "Zhang2013"
title: "Building Information Modeling (BIM) and Safety: Automatic Safety Checking of Construction Models and Schedules,"
authors: "S. Zhang, J. Teizer, J.-K. Lee, C. M. Eastman, and M. Venugopal"
year: 2013
doi: "10.1016/j.autcon.2012.05.006"
zotero_key: "9X7JKF5U"
zotero_status: verified
created: "2026-05-25"
tags:
  - Verified
---

# Zhang2013

| Field | Value |
|-------|-------|
| **Ref** | [16] |
| **Title** | Building Information Modeling (BIM) and Safety: Automatic Safety Checking of Construction Models and Schedules, |
| **Authors** | S. Zhang, J. Teizer, J.-K. Lee, C. M. Eastman, and M. Venugopal |
| **DOI** | [10.1016/j.autcon.2012.05.006](https://doi.org/10.1016/j.autcon.2012.05.006) |



## Verified Evidence

### Rule-Based Safety Checking Framework (Section 4–5)
^sec-framework

> Four-stage rule checking process: (1) Rule Translation — OSHA fall protection rules mapped to IF-THEN machine-readable format via table-based parameterization; (2) Model Preparation — parametric BIM model with object types, attributes, spatial structure, schedule linkage; (3) Rule Execution — algorithms identify slab holes (<2″ ignore, 2″–59″ cover, >59″ guardrail), wall openings, and leading edges across 6 fall protection scenarios; (4) Reporting — 4D visualization, quantity take-offs, and schedule integration for safety equipment installation/removal.

**Method:** Object-oriented rule interpretation; 9-step algorithm for fall hazard detection. Implemented in Tekla Structures API. BPMN process map integrates safety checking into design→construction workflow.

**Supports:** LR_GPT.md §3.2 — pioneered BIM-based automatic safety checking [16].

### Results — 100% Detection on Real Models (Section 6)
^sec-results

> "Holes and edges of slabs were 100% successfully detected by the developed rule-checking system. The default prevention equipment (guardrail system and cover) are applied automatically, which proves the robustness and scalability of the implemented algorithms." Tested on both simple sample models and realistic complex models from the construction industry. 4D simulation links safety equipment to construction schedule (Week 8–12 progression). Bill of materials for safety equipment generated.

**Supports:** LR_GPT.md §3.2, §4.2 — demonstrates automated safety checking feasibility.

### Limitations (Section 7.1)
^sec-limitations

> (1) "it may currently not be possible to represent all unsafe conditions in a BIM model on a real-time basis" — static model, no live sensor data; (2) "a manual effort in rule interpretation is now required both in terms of rule translation into machine readable code" — rules must be hand-coded, not learned; (3) Only fall protection implemented — "Many other areas in construction safety and health exist"; (4) IFC schema not yet adapted for safety — needs Model View Definition development.

**Critical assessment:** Level 2 system — identifies hazards and recommends measures, but "final decision can be left with a safety engineer." No autonomous closed-loop control. Rule-based only — cannot handle novel/compound hazards not explicitly encoded.

### Traceability

| LR_GPT.md | Claim | Evidence Block |
|-----------|-------|----------------|
| §3.2 | "pioneered BIM-based automatic safety checking" | `#^sec-framework` |
| §4.2 | rule-based brittleness under novel conditions | `#^sec-limitations` |
| §5.2 | forward-only reasoning paradigm | `#^sec-limitations` |
| Table 2 | DfS automation representative | `#^sec-results` |
