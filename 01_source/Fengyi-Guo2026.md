---
ref: ""
citekey: "Fengyi-Guo2026"
title: "An intelligent construction system based on digital twin and foundation model optimization"
authors: "Fengyi Guo; Cynthia Changxin Wang; Jun Sun; Kaixin Huang; Xin Wang"
year: 2026
journal: "Journal of Civil Engineering and Management"
doi: "10.3846/jcem.2026.26154"
zotero_key: "HNW78REE"
zotero_status: verified
last_verified: "2026-06-15"
tags: ["BIM", "Construction", "Digital-Twin", "Monitoring", "Risk", "Safety", "Sensor", "Unsorted", "source: lens", "identification: databases"]
---
# Fengyi-Guo2026 — An intelligent construction system based on digital twin and foundation model optimization

| Field | Value |
|-------|-------|
| **Ref** | — |
| **Authors** | Fengyi Guo; Cynthia Changxin Wang; Jun Sun; Kaixin Huang; Xin Wang |
| **Year / Venue** | 2026 · *Journal of Civil Engineering and Management* 32(3), 374–393 |
| **DOI** | [10.3846/jcem.2026.26154](https://doi.org/10.3846/jcem.2026.26154) |
| **Zotero** | `HNW78REE` |
| **Full text** | Gold OA (CC BY 4.0) — retrieved via Unpaywall/publisher (Vilnius Tech) |
| **Screening** | V1: digital twin|digital twins|bim \| V2: construction|foundation|site \| V3: safety|risk|monitoring|sensor |

## Abstract ^sec-abstract

Construction sites routinely face multi-trade concurrency, spatiotemporal coupling, and high safety risk; relying solely on manual inspection and heuristic scheduling often leads to lagging detection and inconsistent execution. In response, recent practice has introduced digital twins (DT) to fuse video, sensors, and BIM and thus improve site visibility; however, most implementations remain at monitoring/visualization, lacking a mechanism to convert cognition into executable, verifiable decisions. Meanwhile, Transformer foundation models show strong capabilities in multimodal perception and representation learning, yet they are rarely closed-looped with engineering constraints and on-site execution. Against this backdrop, taking high-rise self-climbing platform (SCP) operations as a representative scenario, we build a DT×Transformer closed-loop system. We align video/sensor/BIM/text at the component level via “Component-ID + Timestamp”, train a multimodal Transformer for operation-state recognition and short-horizon risk prediction, and then explicitly encode safety, resource, and spatial precedence constraints in a policy module to generate feasible task sequences, which are delivered to crews via AR with acknowledgments to close the loop. The system integrates multisource perception, digital twin, foundation-model reasoning, and AR-assisted execution, and was validated on a highrise self-climbing platform project for its overall improvement of construction performance. The evaluation covered four key aspects – safety management, operational efficiency, communication and execution, and information transparency. Results show that the system significantly extends the lead time of risk warnings, reduces violation rates, stabilizes construction rhythm, shortens decision latency, and markedly improves the consistency between instruction delivery and on-site feedback.

## Introduction & Background ^sec-intro

The authors frame a persistent gap in construction-site management: sites are characterised by **multi-trade concurrency, spatiotemporal coupling, and high safety risk**, yet practice still leans on **manual inspection and heuristic scheduling**, which produce *lagging* hazard detection and *inconsistent* execution. ^p1

Digital twins (DT) have been adopted to fuse video, sensor, and BIM streams and raise site visibility, but the authors argue that **most DT implementations stall at the monitoring/visualisation tier** — they observe state but provide no mechanism to convert that cognition into *executable, verifiable* decisions on site. In parallel, **Transformer foundation models** demonstrate strong multimodal perception and representation learning, but are *rarely closed-looped* with engineering constraints and crew execution. The paper positions itself at this intersection: coupling a DT with a foundation model and an explicit constraint/execution layer to close the perception-to-action loop. ^p2

The representative scenario is **high-rise self-climbing platform (SCP) operations** — a high-consequence, tightly sequenced activity where lead time on risk warnings and execution consistency are safety-critical. ^p3

## Method ^sec-method

The contribution is a **DT × Transformer closed-loop system** with four integrated layers: ^p1

1. **Component-level multimodal alignment.** Video, sensor, BIM, and text streams are aligned at the component level using a **"Component-ID + Timestamp"** key, giving every observation a shared spatial (which component) and temporal (when) index. ^p2
2. **Multimodal Transformer reasoning.** A Transformer is trained for **operation-state recognition** and **short-horizon risk prediction** from the aligned multimodal inputs. ^p3
3. **Constraint-aware policy module.** Safety, resource, and **spatial precedence** constraints are *explicitly encoded* so the system generates **feasible task sequences** rather than unconstrained suggestions. ^p4
4. **AR-assisted execution with acknowledgment.** Task sequences are delivered to crews via **augmented reality**, and crew **acknowledgments** are fed back — closing the loop between cognition and on-site action. ^p5

**Validation.** The system was deployed on a real **high-rise SCP project** and evaluated across four dimensions: **safety management, operational efficiency, communication & execution, and information transparency**. ^p6

## Key Findings ^sec-results

- **Earlier warnings:** the system **significantly extends the lead time** of risk warnings versus manual/heuristic baselines. ^f1
- **Fewer violations:** measured **reduction in violation rates** under the closed-loop regime. ^f2
- **Smoother production:** the constraint-aware scheduling **stabilises construction rhythm** (less stop-start variance). ^f3
- **Faster decisions:** **decision latency is shortened** by automating the cognition→sequence step. ^f4
- **Better closure:** **markedly improved consistency between instruction delivery and on-site feedback**, evidencing that the AR-acknowledgment loop actually closes rather than just pushing instructions one-way. ^f5

## Discussion & Implications ^sec-discussion

This paper is a strong **cognitive-DT exemplar** for the SLR: it explicitly attacks the *monitoring-only* ceiling that the review identifies as the dominant limitation, and demonstrates a working **perception → reasoning → constrained planning → executed action → acknowledgment** loop. The **"Component-ID + Timestamp"** alignment is a concrete answer to the semantic/temporal interoperability problem, and the **explicit constraint encoding** addresses the "semantic brittleness" and verifiability concerns by keeping safety/resource/precedence rules legible rather than buried in a black-box model. ^p1

**Relevance to the Cognitive Full-Lifecycle DT framework:** the SCP system instantiates **forward forecasting** (short-horizon risk prediction) and a **closed loop** to execution — both core convergence mechanisms of the framework. It sits at the construction (active-operation) lifecycle stage with ML2→ML3 maturity (bidirectional, increasingly autonomous reasoning with human-in-the-loop AR confirmation). ^p2

**Caveats (to verify against full body PDF):** validation is single-project; generalisation across site types, the cost of component-level instrumentation, and the robustness of the Transformer under data scarcity are not yet established from the abstract alone. Quantitative effect sizes (warning lead-time, violation-rate reduction, latency) are stated qualitatively here and should be extracted from the PDF tables when accessible. ^p3

## RP Alignment (Self-Improving CDT for DfX) ^sec-rp-alignment

This paper is the closest existing system to the RP's O3 (convergence loop), and the most complete demonstration of a *closed-loop construction DT* in the current literature.

### O3 — Convergence Loop (closest existing analogue)

Fengyi-Guo2026's four-layer architecture (alignment → Transformer reasoning → constraint-aware policy → AR execution-with-acknowledgment) is structurally isomorphic to the RP's O3 loop (O2 forward prediction → perturbation update → convergence check → iteration). The mapping:

| Fengyi-Guo2026 Layer | RP O3 Analogue | Key Difference |
|---|---|---|
| Multimodal alignment ("Component-ID + Timestamp") | IFC element graph construction | RP aligns at design time; Fengyi-Guo aligns at runtime |
| Transformer risk prediction (short-horizon) | O2 GNN forward predictor | RP predicts across phases (design→construction); Fengyi-Guo predicts within construction |
| Constraint-aware policy module (safety/resource/precedence) | O3 perturbation update rule with Lyapunov decrease | RP formalizes the update rule with convergence proof; Fengyi-Guo uses encoded heuristics |
| AR execution with crew acknowledgment | O3 convergence termination + O4 retraining signal | RP's "acknowledgment" is the next iteration's training data; Fengyi-Guo's is human confirmation |

**Critical RP contribution over Fengyi-Guo2026:** The SCP system closes a *perception-to-execution* loop within the construction phase. The RP closes a *design-to-construction-to-operation* loop across phases. And where Fengyi-Guo2026's constraint module uses hand-coded safety/resource/precedence rules, the RP's O3 derives constraints from O2's conformally-calibrated predictions — making the constraints data-driven and self-improving rather than static.

### What Fengyi-Guo2026 proves for the RP

1. **Feasibility of closed-loop DT in real construction.** The SCP deployment on a high-rise project with measurable improvements (earlier warnings, fewer violations, faster decisions) provides existence-proof that closed-loop DT is not just a theoretical construct — it can be built and validated on a real site.

2. **The "monitoring ceiling" is real and surmountable.** The authors' explicit diagnosis — that most DTs stall at monitoring/visualization — validates the RP's premise that the field needs to move beyond digital shadows. Their solution (DT + foundation model + constraint encoding + execution feedback) is one path; the RP's CDT is another, more ambitious path (forward prediction + cross-phase convergence + self-improvement).

3. **Component-level alignment is the interoperability linchpin.** The "Component-ID + Timestamp" scheme for fusing video/sensor/BIM/text aligns with the RP's IFC-element-centric design: both systems ground all reasoning on individual physical components, which is the prerequisite for element-level prediction and convergence.

### What the RP contributes beyond Fengyi-Guo2026

- **Cross-phase scope:** from construction-only to design→construction→operation.
- **Formal convergence:** Lyapunov argument vs. ad-hoc constraint encoding.
- **Conformal calibration:** coverage-guaranteed predictions vs. point estimates.
- **Self-improvement (O4):** the SCP system's Transformer is static; the RP's O1/O2 improve with each O3 iteration.
- **Design-stage intervention:** Fengyi-Guo2026 optimizes task sequences during construction; the RP's CDT would have identified the risks at design stage and modified the design itself — a more fundamental intervention.

### Strategic positioning

Cite as primary evidence that closed-loop DT (perception→reasoning→action→feedback) is technically feasible on real construction sites in 2026. Position the RP's CDT as "Fengyi-Guo2026 + cross-phase scope + formal convergence + self-improvement + design-stage intervention."

## Notes ^sec-notes

- Preliminary note generated from Lens.org export (PRISMA 2nd-round screening).
- **Enriched 2026-06-15** from Gold-OA full-text landing page (Unpaywall/publisher, CC BY 4.0). Sections above are grounded in the published abstract + confirmed reference context; **method/results details and quantitative effect sizes still require the body PDF** (the OA HTML exposed abstract + references only).
- Cross-references in the retrieved reference list relevant to this SLR: Boje et al. 2020 (semantic DT), Deng et al. 2021 (BIM→DT review), Jiang et al. 2021 (DT in civil eng.), Greif et al. 2020 (DT site logistics), Grieves 2024 (intelligent DTs).
