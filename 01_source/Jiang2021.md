---
ref: "[7]"
citekey: "Jiang2021"
title: "Digital twin and its implementations in the civil engineering sector"
authors: "Feng Jiang, Ling Ma, Tim Broyd, Ke Chen"
year: 2021
journal: "Automation in Construction"
doi: "10.1016/j.autcon.2021.103838"
zotero_key: "LD8ZIQKW"
verification_status: "✅ verified"
last_verified: "2026-05-25"
tags: ["BIM-to-DT", "Lifecycle", "Foundation", "Review"]
---

# Jiang2021 — Digital twin in civil engineering

| Field | Value |
|-------|-------|
| **Ref** | [7] |
| **DOI** | [10.1016/j.autcon.2021.103838](https://doi.org/10.1016/j.autcon.2021.103838) |
| **Zotero Key** | `LD8ZIQKW` |

## Verified Evidence

### DT Definition and Five-Part Structure (Section 2)
^sec-2-definition

> "a DT should use virtual representations to express the physical counterpart. Second, a DT connection requires data transfer from the physical object to the virtual part, but feedback is not mandatory. Third, the virtual part can control the physical counterpart, but this is not mandatory."

**Supports:** LR_GPT.md §1 — "DT extends beyond 3D visualization toward a cyber-physical system capable of monitoring, reasoning, and supporting intervention in physical workflows [2], [7]."

### Lifecycle Scope — O&M Dominance (Section 3)
^sec-3-lifecycle

> "At the O&M stage, DT can contribute substantially to asset management... O&M stage has the most DT application cases."

**Supports:** LR_GPT.md §5.5 — lifecycle continuity, construction-phase models transferred to O&M.

### Model-Centric Approach (Section 2)
^sec-2-modelcentric

> "A BIM model is a digital representation of a built object's physical and functional characteristics. Both a BIM model and a DT require a virtual model."

**Supports:** LR_GPT.md §3.1 — model-centric DT paradigm [1], [7], [10].

## Traceability

| LR_GPT.md | Claim | Evidence |
|-----------|-------|----------|
| §1 | DT extends BIM toward cyber-physical [2], [7] | `#^sec-2-definition` |
| §3.1 | model-centric approach [1], [7], [10] | `#^sec-2-modelcentric` |
| §5.5 | lifecycle continuity [7], [57], [60] | `#^sec-3-lifecycle` |
| §6.1 (RQ1) | model-centric approach [1], [7], [10] | `#^sec-2-modelcentric` |
| Table 2 | BIM-to-DT representative reference | `#^sec-2-definition` |
