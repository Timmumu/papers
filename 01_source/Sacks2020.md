---
ref: "[32]"
citekey: "Sacks2020"
title: "Construction with digital twin information systems,"
authors: "R. Sacks, I. Brilakis, P. Pikas, H. Xie, and M. Girolami"
year: 2020
doi: "10.1017/dce.2020.16"
zotero_key: "FBV29DAQ"
zotero_status: verified
created: "2026-05-25"
tags:
  - Verified
---

# Sacks2020 — Construction with Digital Twin Information Systems

| Field | Value |
|-------|-------|
| **Ref** | [32] |
| **Authors** | R. Sacks, I. Brilakis, E. Pikas, H. S. Xie, M. Girolami |
| **Year / Venue** | 2020 / Data-Centric Engineering (Cambridge) |
| **DOI** | 10.1017/dce.2020.16 |
| **Zotero** | FBV29DAQ |

## Abstract ^sec-abstract
The concept of a "digital twin" as a model for data-driven management and control of physical systems has emerged over the past decade in the domains of manufacturing, production, and operations. In the context of buildings and civil infrastructure, the notion of a digital twin remains ill-defined, with little or no consensus among researchers and practitioners of the ways in which digital twin processes and data-centric workflows should be adapted to construction. The paper proposes the concept of "Digital Twin Construction" (DTC) — a mode of construction in which all information needed for production planning and control is contained in a continuously updated digital twin of the project status (PSI/PSK) and the project intent (PII/PIK), and decisions are taken on the basis of automated project performance control (APPC). ^p1

## Introduction & Background ^sec-intro
Manufacturing has steadily moved toward data-centric production control, supported by the Plan-Do-Check-Act (PDCA) cycle and lean transformation–flow–value (TFV) theory. Construction has not made the same transition: production data are still captured manually, asynchronously, and at low resolution, and the BIM model is treated as a static handover artefact rather than a live information base. ^p1

The authors argue that the term "digital twin" has been imported into construction loosely, often used as a synonym for an as-built BIM, and that this conflation obscures what is required for genuine closed-loop, data-driven construction control. They therefore define DTC as a *mode of construction*, not merely a software artefact. ^p2

## Method ^sec-method
1. Synthesise definitions of digital twin from manufacturing, aerospace and infrastructure domains and contrast them with current BIM and Automated Project Performance Control (APPC) practice. ^p1
2. Specify the DTC information layers: Project Intent Information / Knowledge (PII/PIK) and Project Status Information / Knowledge (PSI/PSK), with explicit data flows between them. ^p2
3. Map the DTC concept onto lean construction (TFV), PDCA control, and Industry-4.0 technologies (IoT, BLE/UWB/RFID positioning, complex event processing, AI). ^p3
4. Illustrate the framework with construction scenarios (progress monitoring, quality control, safety, logistics) to show where current systems fall short of true DTC. ^p4

## Key Findings ^sec-results
- Current "DT" implementations in construction are mostly Levels 1–2 (digital model / digital shadow) — data flows from physical to digital but rarely back. ^f1
- Genuine DTC requires automated, continuous updating of both PSI and PIK so that *intent* can be revised, not only *status* monitored. ^f2
- Lean principles (TFV) and DTC are mutually reinforcing: DTC operationalises flow and value measurement that lean has long advocated but rarely measured continuously. ^f3
- Governance and human-in-the-loop authority are unresolved: it is unclear who acts on automated decisions and under which accountability regime. ^f4
- Validation of construction DTs to date is fragile — algorithms tested in controlled sites generalise poorly to multi-subcontractor, weather-variable, real-world conditions. ^f5

## Discussion & Implications ^sec-discussion
DTC reframes construction management as a cyber-physical control loop. This shift exposes deep gaps: data schemas spanning design intent and field telemetry, standards for bidirectional updates, and policies for who may override automated decisions. The authors flag lifecycle continuity and governance as prerequisites that the AECO sector has barely begun to address. ^p1

The framework deliberately positions human judgement inside the loop, anticipating that fully autonomous closed-loop construction control will be neither technically nor legally acceptable in the near term. ^p2

## Conclusion ^sec-conclusion
Digital Twin Construction is presented as a coherent target state for data-centric construction, requiring continuous bidirectional integration of project intent and project status, supported by lean principles and Industry-4.0 technologies — and demanding new governance and validation practices. ^p1

## Relevance to Cognitive Full-Lifecycle DT SLR ^sec-relevance
- **Lifecycle stage(s):** design → construction → handover (full-lifecycle continuity)
- **Cognitive capability:** reasoning, prediction, autonomy, human-AI, safety, governance
- **Why cited in LR_cc.md:** Sacks2020 is one of the few sources in our corpus that explicitly addresses *lifecycle continuity and governance* and *human-in-the-loop* considerations in construction DTs, and it documents the *validation fragility* of single-site DT studies. These three roles map directly to the three places it is cited in the manuscript.

## Traceability

| Claim in LR_cc.md | Evidence anchor |
|---|---|
| "Lifecycle continuity & governance … [32]" (taxonomy table) | #^sec-abstract, #^sec-discussion#^p1 |
| "Algorithms validated under controlled conditions … face unquantified risks … [32]" | #^f5, #^sec-discussion#^p1 |
| "Only two studies … [18], [32] mention human-in-the-loop considerations" | #^f4, #^sec-discussion#^p2 |
