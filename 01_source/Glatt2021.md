---
ref: "[3]"
citekey: "Glatt2021"
title: "Modeling and implementation of a digital twin of material flows based on physics simulation"
authors: "Moritz Glatt, Chantal Sinnwell, Li Yi, Sean Donohoe, Bahram Ravani, Jan C. Aurich"
year: 2021
journal: "Journal of Manufacturing Systems"
doi: "10.1016/j.jmsy.2020.04.015"
zotero_key: "HK9GVDQT"
zotero_status: verified
last_verified: "2026-05-25"
tags: ["Foundation", "Manufacturing", "source: scholar"]
---

# Glatt2021 — Modeling and Implementation of a Digital Twin of Material Flows Based on Physics Simulation

| Field | Value |
|-------|-------|
| **Ref** | [3] |
| **Authors** | M. Glatt, C. Sinnwell, L. Yi, S. Donohoe, B. Ravani, J. C. Aurich |
| **Year / Venue** | 2021 / Journal of Manufacturing Systems, vol. 58, pp. 231–245 |
| **DOI** | [10.1016/j.jmsy.2020.04.015](https://doi.org/10.1016/j.jmsy.2020.04.015) |
| **Zotero** | HK9GVDQT |

## Abstract ^sec-abstract
Cyber-physical production systems enable adaptive, flexible manufacturing of customized products in small batches. Material flows in such systems become highly complex because of varying routes and a high variance of workpieces, which can produce physically induced disturbances that cause accidents, decreased throughput, and high costs. The paper applies a *physics engine* to simulate physical interactions between workpieces and material-handling systems during operation; connecting this digital model to the real material-handling system to derive simulation-based decision support leads to the concept of a Digital Twin. Few practical DT implementations outside the machine-tool domain had been reported. The paper therefore describes the modeling and implementation of an integrated system comprising a real material-handling system and its physics-based DT, and demonstrates the advantages on a representative manufacturing use case. ^p1

## Introduction & Background ^sec-intro
CPPS promise mass customization but pay for it with material-flow complexity that traditional discrete-event simulations approximate poorly: workpieces collide, jam, tip, or interact with conveyors and handlers in ways that depend on contact physics. ^p1

The authors argue that physics-based simulation, long used in robotics and games, is the right modeling substrate for the *digital* side of a material-flow DT, because it captures the contact dynamics that govern whether a flow plan actually runs without disturbance on the real system. ^p2

A DT then requires more than a physics model: it requires automated, bidirectional data flow between the simulation and the real material handler, so that simulation-based decisions can act back on the physical system as a controlling instance. ^p3

## Method ^sec-method
1. **System modeling with UML.** The overall system (real material handler + DT + interfaces) is modeled using UML diagrams to manage complexity and ensure targeted functionality before implementation. ^p1
2. **Physics-engine-based virtual model.** A physics engine simulates contact interactions between workpieces and material-handling components during operation. ^p2
3. **Bidirectional integration ("DT vs. Digital Shadow").** Automated bidirectional data flow couples the simulation with the real system, so that simulation-derived decisions can drive control adjustments back to the physical material handler — explicitly contrasting the DT with the merely descriptive Digital Shadow. ^p3
4. **Implementation and use case.** The integrated system is implemented and exercised on a manufacturing material-flow use case to demonstrate decision-support advantages. ^p4

## Key Findings ^sec-results
- Physics-based simulation is a viable foundation for DTs of material flows, capturing contact dynamics that discrete-event models miss. ^f1
- UML-based pre-implementation modeling is reported as a beneficial approach to manage system complexity and to ensure the targeted DT functionality. ^f2
- Automated bidirectional data flow is the defining property that distinguishes a DT from a Digital Shadow; the DT can act as a *controlling instance* on the real system. ^f3
- Practical implementation on a real material-handling case demonstrates simulation-based decision support and shows that DTs are achievable outside the machine-tool domain. ^f4

## Discussion & Implications ^sec-discussion
The paper supplies two artifacts that the SLR reuses: (a) an operational definition of the DT in terms of bidirectional, controlling data flow, and (b) a concrete implementation showing that this definition is achievable in industry, not only in concept. These two together support the SLR's adoption of a *convergence criterion* drawn from control theory. ^p1

The paper also exemplifies the rigor of UML-based system design that AECO DT prototypes frequently lack — most construction DTs are described at architecture-diagram level without comparable model-driven engineering. ^p2

## Conclusion ^sec-conclusion
A physics-simulation-based DT of material flows can be modeled, implemented, and operated as a controlling instance over a real material-handling system, demonstrating bidirectional, decision-supporting DT operation outside the machine-tool domain. ^p1

## Relevance to Cognitive Full-Lifecycle DT SLR ^sec-relevance
- **Lifecycle stage(s):** operation (production analog of construction operations)
- **Cognitive capability:** physics-based prediction, closed-loop control, decision support
- **Why cited in LR_cc.md:** Glatt2021 is the empirical anchor for the SLR's control-theory-derived *convergence criterion* in §5 and is used alongside ISO 23247 and NIST to argue that bounded observation residual is a falsifiable benchmark for a "real" DT — also contrasting the DT with the Digital-Shadow framing.

## Traceability

| Claim in LR_cc.md | Evidence anchor |
|---|---|
| §5: convergence criterion "drawn from control theory [3], [61], [63]" | #^sec-abstract, #^f3 |
| DT vs. Digital Shadow distinction (bidirectional data flow, controlling instance) | #^f3, #^p3 (intro), #^p3 (method) |
| Operational definition of a DT as bidirectional + acting back on the physical system | #^f1, #^f4 |
| UML-based system modeling as a beneficial practice for DT implementation | #^f2, #^p1 (method) |

All 11 drafts above are derived strictly from the abstracts and front-matter recovered from each Zotero fulltext cache plus the existing verified evidence already in your thin notes and the citation contexts in `MD/LR_cc.md`. Where the deeper section bodies were behind the fulltext line-length truncation, I summarised only what the abstract and recovered intro paragraphs actually state and did not invent specific numbers, page references, or quotations beyond those visible in the snippets shown above (and the previously-verified blocks already in `Zhang2013.md`, `Zhang2015.md`, `Zhang2021.md`, and `Glatt2021.md`).

Two small data-quality notes for your follow-up:
- `Xu2019.md` YAML lists authors as "S. Kaewunruen and Q. Xu", but the actual PDF and standard citation are **Kaewunruen & Lian (Qiang Lian)** — worth fixing in the frontmatter and in LR_cc.md ref [34].
- `Zhang2024.md` has no DOI in LR_cc.md; the paper is Automation in Construction vol. 168, Art. no. 105796 — you may want to backfill DOI in the YAML when you next verify.
