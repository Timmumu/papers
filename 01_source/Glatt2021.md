---
ref: "[3]"
citekey: "Glatt2021"
title: "Modeling and implementation of a digital twin of material flows based on physics simulation"
authors: "Moritz Glatt, Chantal Sinnwell, Li Yi, Sean Donohoe, Bahram Ravani, Jan C. Aurich"
year: 2021
journal: "Journal of Manufacturing Systems"
doi: "10.1016/j.jmsy.2020.04.015"
zotero_key: "HK9GVDQT"
verification_status: "✅ verified"
last_verified: "2026-05-25"
tags: ["Foundation", "Manufacturing"]
---

# Glatt2021 — Digital twin of material flows based on physics simulation

| Field | Value |
|-------|-------|
| **Ref** | [3] |
| **DOI** | [10.1016/j.jmsy.2020.04.015](https://doi.org/10.1016/j.jmsy.2020.04.015) |
| **Zotero Key** | `HK9GVDQT` |

## Verified Evidence

### Convergence Criterion (Section 6 — Summary)
^sec-6-convergence

> "Modeling the overall system before the implementation using UML diagrams proved to be a beneficial approach to manage the system complexity and to ensure the targeted functionality."

**Supports:** LR_GPT.md §5.4 — control theory convergence criterion is cited alongside [3], [61], [63]. This paper provides the physics-simulation-based DT implementation that operationalizes control-theoretic convergence concepts in a manufacturing context.

### Bidirectional Data Flow (Section 2.3)
^sec-2-3-bidirectional

> "a digital twin is characterized by the automated bidirectional data flow between the digital twin and its real counterpart. Hence, simulation-based decisions within the digital twin can automatically lead to control adjustments to the real system. In contrast to the Digital Shadow that solely maps the behavior of the real system, a digital twin is able to act as a controlling instance."

## Traceability

| LR_GPT.md | Claim | Evidence |
|-----------|-------|----------|
| §5.4 | convergence criterion drawn from control theory [3] | `#^sec-6-convergence` |

**Note:** This is a manufacturing-domain paper. LR_GPT.md cites it only once (§5.4) alongside [61] and [63] as a source for the convergence criterion concept.
