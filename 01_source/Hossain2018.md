---
ref: "[20]"
citekey: "Hossain2018"
title: "Design-for-Safety knowledge library for BIM-integrated safety risk reviews,"
authors: "M. A. Hossain, E. L. S. Abbott, D. K. H. Chua, T. Q. Nguyen, and Y. M. Goh"
year: 2018
doi: "10.1016/j.autcon.2018.07.010"
zotero_key: "7JMAKZYT"
zotero_status: verified
created: "2026-05-25"
tags:
  - Verified
  - source: scholar
---

# Hossain2018 — Design-for-Safety knowledge library for BIM-integrated safety risk reviews

| Field | Value |
|-------|-------|
| **Ref** | (ref) |
| **Authors** | Md. Aslam Hossain, Ernest L. S. Abbott, David K. H. Chua, Nguyen Thi Qui, Yang Miang Goh |
| **Year / Venue** | 2018 · *Automation in Construction*, 94, 290–302 |
| **DOI** | [10.1016/j.autcon.2018.07.010](https://doi.org/10.1016/j.autcon.2018.07.010) |
| **Zotero** | `7JMAKZYT` |

## Abstract ^sec-abstract

Many construction fatalities are traceable to design decisions and could have been avoided through proper Design-for-Safety (DfS), yet designers typically have limited construction-safety knowledge and struggle to anticipate how design elements create risk during construction, operation and maintenance. The paper presents a structured, rule-based **DfS knowledge library** and uses it to drive an *intelligent BIM-integrated risk review system* that flags element-level risks and prescribes design features; a complementary risk register tracks residual risk inside BIM. An illustrative case project shows that many risks could have been avoided or eliminated with the DfS library applied at design stage. ^p1

## Introduction & Background ^sec-intro

DfS is a long-standing principle but has lacked operational tooling inside designer-facing software; consequently safety remains a downstream construction-phase concern. ^p1

The work targets the gap between safety knowledge (held by safety professionals and accident databases) and design action (taken in BIM by architects/engineers), proposing a machine-readable rule library as the bridge. ^p2

## Method ^sec-method

1. Codification of DfS knowledge into a **rule-based knowledge library** indexed against design elements and life-cycle phases (construction, operation, maintenance). ^p1
2. Integration with a BIM authoring environment so that, on element selection, the system runs the relevant DfS rules and surfaces hazards with recommended design features. ^p2
3. A **risk-register subsystem** inside BIM to record residual risks for follow-up by downstream stakeholders. ^p3
4. Demonstration on an illustrative case project to evaluate coverage of risks and design-time avoidance. ^p4

## Key Findings ^sec-results

- A structured, rule-based DfS knowledge library can be operationalised inside BIM rather than left as separate documentation. ^f1
- The BIM-integrated risk-review system identifies element-level risks and prescribes corresponding design features. ^f2
- A BIM-resident risk register makes residual risks explicit and trackable across life-cycle phases. ^f3
- On the case project, many identified risks could have been avoided or eliminated had the library been used at design stage. ^f4

## Discussion & Implications ^sec-discussion

The work is an early example of a *reasoning layer* attached to BIM (rules over elements), prefiguring later cognitive-DT proposals in which knowledge graphs and ML models drive automated review of model content. ^p1

By persisting residual risk in BIM, the system extends the model from a geometric artefact to a longitudinal risk record that can be inherited by construction and FM — a clear life-cycle continuity argument. ^p2

## Conclusion ^sec-conclusion

A DfS knowledge library coupled with BIM-integrated risk review and a risk register can shift safety management upstream into design and carry residual risks forward across the life cycle. ^p1

## Relevance to Cognitive Full-Lifecycle DT SLR ^sec-relevance

- **Lifecycle stage(s):** design (primary) → construction → operation/maintenance (via risk register)
- **Cognitive capability:** reasoning (rule-based), safety
- **Why cited in LR_cc.md:** Establishes that adding a rule-based reasoning layer over BIM is feasible and useful for safety, supporting the SLR's claim that "cognitive" extensions of BIM/DT are tractable when the knowledge is well structured, and that lifecycle hand-off (design → construction → FM) can be carried inside the model itself.

## Traceability

| Claim in LR_cc.md | Evidence anchor |
|---|---|
| Rule-based DfS reasoning can be embedded in BIM | #^sec-abstract, #^f1 |
| Element-level automated risk review is feasible | #^f2 |
| Residual-risk register enables life-cycle hand-off | #^f3, #^sec-discussion |
