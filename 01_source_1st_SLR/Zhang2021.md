---
ref: "[19]"
citekey: "Zhang2021"
title: "A BIM-data mining integrated digital twin framework for advanced project management,"
authors: "Y. Pan and L. Zhang"
year: 2021
doi: "10.1016/j.autcon.2021.103564"
zotero_key: "YGJSXUXV"
zotero_status: verified
created: "2026-05-25"
tags:
  - Verified
  - source: scholar
  - identification: other methods
---

# Zhang2021 — A BIM–Data Mining Integrated Digital Twin Framework for Advanced Project Management

| Field | Value |
|-------|-------|
| **Ref** | [19] |
| **Authors** | Y. Pan, L. Zhang |
| **Year / Venue** | 2021 / Automation in Construction, vol. 124, Art. no. 103564 |
| **DOI** | [10.1016/j.autcon.2021.103564](https://doi.org/10.1016/j.autcon.2021.103564) |
| **Zotero** | YGJSXUXV |

## Abstract ^sec-abstract
Targeting smart construction project management, the paper presents a closed-loop Digital Twin framework that integrates BIM, IoT, and data mining (DM). IoT connects the physical and cyber worlds to capture real-time data for modeling and analysis; DM techniques inside the virtual model discover hidden knowledge in the collected data. The DT is verified on a practical BIM-based project: from large IoT inspection data, 4D visualization and task-centered / worker-centered process models are built as the virtual model to simulate both task execution and worker cooperation. The high-fidelity virtual model is then investigated with process mining and time-series analysis. Results show that bottlenecks in the current process can be foreseen using a *fuzzy miner*, while finished tasks in the next phase can be predicted with a multivariate ARIMAX model, enabling tactic decision-making that prevents failure in advance and rationally arranges work and staffing. ^p1

## Introduction & Background ^sec-intro
The construction industry struggles to convert the streams of as-built and operational data produced by modern BIM-IoT deployments into project-management decisions: data is collected but seldom mined for predictive insight. ^p1

The authors propose closing this loop with a DT that pairs the BIM-as-virtual-twin with a data-mining layer, so that observation is followed by inference and inference informs action — a concrete instance of the cognitive DT vision in a project-management setting. ^p2

## Method ^sec-method
1. **Architecture.** Closed-loop DT integrating BIM (geometric/semantic backbone), IoT (real-time inspection data), and data mining (knowledge discovery). ^p1
2. **Virtual model construction.** 4D visualization plus task-centered and worker-centered process models simulating task execution and crew cooperation. ^p2
3. **Process mining.** A *fuzzy miner* extracts process models from event logs to foresee bottlenecks in the current execution. ^p3
4. **Predictive analytics.** A multivariate ARIMAX time-series model predicts the number of finished tasks in the next phase, conditioned on observed covariates. ^p4
5. **Validation.** The framework is demonstrated on a practical BIM-based project with large inspection datasets from IoT devices. ^p5

## Key Findings ^sec-results
- Possible bottlenecks in the current construction process can be foreseen using fuzzy-miner process discovery. ^f1
- ARIMAX time-series modeling can predict the number of finished tasks in the next phase from past task execution data. ^f2
- The combined fuzzy-miner + ARIMAX pipeline enables tactic decision-making that prevents failures in advance and rationally arranges work and staffing. ^f3
- Closed-loop integration of BIM + IoT + DM is operationally feasible on a real BIM-based project, validating the framework on representative inspection data. ^f4

## Discussion & Implications ^sec-discussion
This paper exemplifies the *data-centric* maturity tier of construction DTs: rather than merely visualizing sensor data on top of BIM, it derives forward-looking insights (bottlenecks, task throughput) and turns them into management actions. It is therefore one of the cleaner published cases of a Level-3 DT loop in AECO. ^p1

The principal limitations are single-project validation, dependency on inspection-data quality and BIM completeness, and the absence of explicit uncertainty quantification on the ARIMAX predictions. ^p2

## Conclusion ^sec-conclusion
A closed-loop DT framework integrating BIM, IoT, and data mining can move construction project management from descriptive monitoring to predictive, tactic decision-making. ^p1

## Relevance to Cognitive Full-Lifecycle DT SLR ^sec-relevance
- **Lifecycle stage(s):** construction (project execution and management)
- **Cognitive capability:** prediction, process discovery, decision support
- **Why cited in LR_cc.md:** Zhang2021 is the canonical "Predictive analytics & decision support" cluster reference in §3.2 and provides empirical support for the SLR's argument that closed-loop, predictive DTs are technically feasible in construction project management.

## Traceability

| Claim in LR_cc.md | Evidence anchor |
|---|---|
| §3.2 cluster row "Predictive analytics & decision support" lists [19] | #^sec-abstract, #^f2, #^f3 |
| §3.4 maturity model: evidence that Level-3 closed-loop DTs are emerging | #^f1, #^f3, #^p1 (discussion) |
| §5.2 / §5.5 references to data-driven DT for project management | #^f4, #^p1 (intro) |
