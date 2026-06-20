---
ref: ""
citekey: "Xiaoming-Yu2026"
title: "A Digital Twin-Based Method for Degradation Parameter Identification of Electrolytic Capacitors in Full-Bridge Submodules of Unified Power Flow Controllers"
authors: "Xiaoming Yu; Peng Wang; Jun Wang; Zhijun Chen; Ke Zhang; Duicheng Zhao; Jiapeng Shen; Chuyang Wang; Li Zhang"
year: 2026
journal: "Energy Engineering"
doi: "10.32604/ee.2026.073475"
zotero_key: "RP6YVITN"
zotero_status: abstract-grounded
last_verified: "2026-06-15"
tags: ["Bridge", "Digital-Twin", "Monitoring", "Real-Time", "Unsorted", "source: lens"]
---
# Xiaoming-Yu2026 — A Digital Twin-Based Method for Degradation Parameter Identification of Electrolytic Capacitors in Full-Bridge Submodules of Unified Power Flow Controllers

| Field | Value |
|-------|-------|
| **Ref** | — |
| **Authors** | Xiaoming Yu; Peng Wang; Jun Wang; Zhijun Chen; Ke Zhang; Duicheng Zhao; Jiapeng Shen; Chuyang Wang; Li Zhang |
| **Year / Venue** | 2026 · *Energy Engineering* |
| **DOI** | [10.32604/ee.2026.073475](https://doi.org/10.32604/ee.2026.073475) |
| **Zotero** | `RP6YVITN` |
| **Screening** | V1: digital twin \| V2: bridge \| V3: monitoring|optimization|real-time |

## Abstract ^sec-abstract

Electrolytic capacitors in Modular Multilevel Converter-based Unified Power Flow Controllers (MMC-UPFC) are prone to parameter degradation, significantly affecting system reliability. Accurate identification of their degradation parameters—capacitance (C) and equivalent series resistance (ESR)—is essential for equipment health management. This study proposes a non-intrusive degradation parameter identification method for electrolytic capacitors in MMC-UPFC full-bridge submodules based on digital twin technology and an improved intelligent optimization algorithm. First, the degradation mechanism of electrolytic capacitors under long-term operational conditions is systematically analyzed. Second, a high-fidelity digital twin model integrating the main circuit, sampling circuit, and modulation circuit of the full-bridge submodule is established, enabling real-time synchronization between the physical and virtual systems. Third, based on the degradation characteristics of aluminum electrolytic capacitors, a condition monitoring objective function is formulated. An improved Particle Swarm Optimization (PSO) algorithm is proposed, which dynamically adjusts acceleration coefficients to iteratively optimize the monitored capacitance and ESR values, demonstrating superior convergence performance compared to conventional PSO. Verification results validate the effectiveness of the proposed method under various operating conditions. The computational efficiency of the method makes it suitable for quasi-online applications, and the monitoring cycle can be adjusted according to accuracy requirements. This study provides a practical solution for non-intrusive health monitoring of MMC-UPFC systems, contributing to improved equipment health management, extended system lifespan, and enhanced operational reliability in modern Flexible AC Transmission Systems (FACTS).

## Introduction & Background ^sec-intro

Electrolytic capacitors in MMC-based Unified Power Flow Controllers (MMC-UPFC) degrade over time, undermining system reliability. Accurate, non-intrusive identification of their degradation parameters — capacitance (C) and equivalent series resistance (ESR) — is essential for equipment health management.

## Method ^sec-method

The study analyses the long-term degradation mechanism of aluminium electrolytic capacitors, then builds a high-fidelity DT integrating the main, sampling, and modulation circuits of the full-bridge submodule for real-time physical–virtual synchronisation. A condition-monitoring objective function is optimised by an improved Particle Swarm Optimization (PSO) that dynamically adjusts acceleration coefficients to iteratively estimate C and ESR.

## Key Findings ^sec-results

The improved PSO shows superior convergence over conventional PSO and validation confirms effectiveness across various operating conditions. The method is computationally efficient enough for quasi-online use, with an adjustable monitoring cycle to trade off accuracy and frequency.

## Discussion & Implications ^sec-discussion

This is a component-level *predictive-maintenance* DT: a high-fidelity model plus metaheuristic parameter identification for non-intrusive health monitoring. The pattern (high-fidelity DT + optimisation-based parameter inversion for prognostics) generalises to asset-health DTs, though the immediate application is power-electronics rather than built assets.

## Notes ^sec-notes

- **Screening:** Retained — DT + condition monitoring/prognostics; domain-adjacent (FACTS power electronics).
- **Relevance:** Exemplar of *high-fidelity DT + optimisation* for degradation parameter inversion; method transferable to asset prognostics.
- **Source:** Gold OA; PDF available in Zotero library (full body not yet ingested into note).
