---
ref: "[31]"
citekey: "Uhlemann2017"
title: "The Digital Twin: Realizing the cyber-physical production system for industry 4.0,"
authors: "M. Uhlemann, C. Lehmann, and R. Steinhilper"
year: 2017
doi: "10.1016/j.procir.2016.11.152"
zotero_key: "7XF73XIE"
zotero_status: verified
created: "2026-05-25"
tags:
  - Verified
---

# Uhlemann2017 — The Digital Twin: Realizing the Cyber-Physical Production System for Industry 4.0

| Field | Value |
|-------|-------|
| **Ref** | [31] |
| **Authors** | T. H.-J. Uhlemann, C. Lehmann, R. Steinhilper |
| **Year / Venue** | 2017 / Procedia CIRP, vol. 61, pp. 335–340 (24th CIRP Conf. on Life Cycle Engineering) |
| **DOI** | [10.1016/j.procir.2016.11.152](https://doi.org/10.1016/j.procir.2016.11.152) |
| **Zotero** | 7XF73XIE |

## Abstract ^sec-abstract
Current approaches to manufacturing process planning spend roughly 74 % of total time on acquiring a sufficient data basis of relevant process information and on developing feasible layout options, and fully automated planning is still uncommon. Deficits remain in fully automated acquisition of underlying process data — a key element of Industry 4.0 — and in evaluating, quantifying, and analyzing the gathered data. Because most planning is conducted manually, theoretical evaluation is lacking and benchmarking is difficult; existing simulation-based analysis is bounded by complexity that defies manual control. The paper therefore calls for research on automated data acquisition and selection, and on near real-time evaluation and analysis of high-volume process data, framing the *Digital Twin* as the means to realize the cyber-physical production system (CPPS) for Industry 4.0. ^p1

## Introduction & Background ^sec-intro
Industry 4.0 reframes manufacturing as a network of cyber-physical systems in which the digital and physical layers must remain continuously synchronized. The authors observe that, despite this vision, planning practice is still dominated by manual data collection and human-mediated decision making, which dominates the time budget and bottlenecks scalability. ^p1

They argue that the Digital Twin — a digital representation continuously fed by real-time process data — is the operational instantiation of the CPPS concept and the missing link between sensor-rich shop floors and automated planning. ^p2

## Method ^sec-method
The paper is a conceptual / position contribution: it analyzes current planning practice, quantifies the time share dedicated to data acquisition (≈74 %), reviews the limitations of simulation-only evaluation in complex systems, and derives requirements for a Digital Twin that supports near real-time multi-source data acquisition, selection, evaluation, and feedback to the planning loop. ^p1

It then sketches the Digital Twin as the building block that turns the CPPS vision into an implementable architecture for Industry 4.0 manufacturing, identifying open research needs around automated data acquisition, selection, and evaluation. ^p2

## Key Findings ^sec-results
- About 74 % of planning time is currently spent acquiring the necessary data basis, demonstrating the magnitude of the automation gap. ^f1
- Manual planning prevents systematic theoretical evaluation and benchmarking of planning outcomes. ^f2
- Existing simulation-based analyses cannot scale to the complexity of modern manufacturing systems without continuous, automated data inputs. ^f3
- The Digital Twin is positioned as the concrete realization of the CPPS for Industry 4.0, requiring automated, near real-time data acquisition and evaluation. ^f4

## Discussion & Implications ^sec-discussion
The paper consolidates the framing — widely reused thereafter — that the Digital Twin is not "yet another simulation" but the synchronization layer between physical processes and their digital counterparts. The authors implicitly demand sub-batch latency: if data is not assimilated in near real time, the DT degrades to a planning-time model and loses its CPPS role. ^p1

This framing is foundational for downstream construction-DT literature that aspires to real-time hazard checking, progress monitoring, and adaptive scheduling, because it sets the bar for what counts as a DT versus a digital shadow. ^p2

## Conclusion ^sec-conclusion
Realizing Industry 4.0 requires moving from manual, simulation-augmented planning to a Digital-Twin-based CPPS in which data acquisition, evaluation, and feedback are automated and near real-time. ^p1

## Relevance to Cognitive Full-Lifecycle DT SLR ^sec-relevance
- **Lifecycle stage(s):** construction (operations / production analog), operation
- **Cognitive capability:** perception (automated data acquisition), real-time evaluation, decision support
- **Why cited in LR_cc.md:** Uhlemann et al. is part of the citation cluster [28]–[31] used in §3.4 to support the SLR's claim that real-time DT performance is widely *asserted* in the manufacturing-DT literature; the SLR contrasts this with the construction-DT subset where end-to-end latency budgets are rarely disclosed.

## Traceability

| Claim in LR_cc.md | Evidence anchor |
|---|---|
| §3.4: "A majority of studies in the perception and data-assimilation clusters report 'real-time' performance … [28]–[31]" | #^sec-abstract, #^f3, #^f4 |
| §2/§3 framing: DT as the operational realization of CPPS / Industry 4.0 | #^p2 (intro), #^f4 |
| Motivation for automated, near real-time data assimilation | #^f1, #^p1 (discussion) |
