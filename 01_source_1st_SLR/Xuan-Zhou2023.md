---
ref: ""
citekey: "Xuan-Zhou2023"
title: "A fuzzy-set-based joint distribution adaptation method for regression and its application to online damage quantification for structural digital twin"
authors: "Xuan Zhou; Claudio Sbarufatti; Marco Giglio; Leiting Dong"
year: 2023
journal: "Mechanical Systems and Signal Processing"
doi: "10.1016/j.ymssp.2023.110164"
zotero_key: "R8634BL6"
zotero_status: abstract-grounded
last_verified: "2026-06-15"
tags: ["Digital-Twin", "Simulation", "Structural", "Unsorted", "source: lens", "identification: databases"]
---
# Xuan-Zhou2023 — A fuzzy-set-based joint distribution adaptation method for regression and its application to online damage quantification for structural digital twin

| Field | Value |
|-------|-------|
| **Ref** | — |
| **Authors** | Xuan Zhou; Claudio Sbarufatti; Marco Giglio; Leiting Dong |
| **Year / Venue** | 2023 · *Mechanical Systems and Signal Processing* |
| **DOI** | [10.1016/j.ymssp.2023.110164](https://doi.org/10.1016/j.ymssp.2023.110164) |
| **Zotero** | `R8634BL6` |
| **Screening** | V1: digital twin \| V2: structural \| V3: simulation |

## Abstract ^sec-abstract

Online damage quantification suffers from insufficient labeled data that weakens its accuracy. In this context, adopting the domain adaptation on historical labeled data from similar structures/damages or simulated digital twin data to assist the current diagnosis task would be beneficial. However, most domain adaptation methods are designed for classification and cannot efficiently address damage quantification, a regression problem with continuous real-valued labels. This study first proposes a novel domain adaptation method, the Online Fuzzy-set-based Joint Distribution Adaptation for Regression, to address this challenge. By converting the continuous real-valued labels to fuzzy class labels via fuzzy sets, the marginal and conditional distribution discrepancy are simultaneously measured to achieve the domain adaptation for the damage quantification task. Thanks to the superiority of the proposed method, a state-of-the-art online damage quantification framework based on domain adaptation is presented. Finally, the framework has been comprehensively demonstrated with a damaged helicopter panel, in which three types of damage domain adaptations (across different damage locations, across different damage types, and from simulation to experiment) are all conducted, proving the accuracy of damage quantification can be significantly improved in a realistic environment. It is expected that the proposed approach to be applied to the fleet-level digital twin considering the individual differences.

## Introduction & Background ^sec-intro

Online damage quantification suffers from insufficient labeled data. Domain adaptation on historical labeled data from similar structures or simulated **digital twin** data can assist. Most domain adaptation methods are for classification, not regression.

## Method ^sec-method

A novel **Online Fuzzy-set-based Joint Distribution Adaptation for Regression** converts continuous labels to fuzzy class labels, simultaneously measuring marginal and conditional distribution discrepancy. Demonstrated on a damaged helicopter panel.

## Key Findings ^sec-results

Three types of damage domain adaptations (across locations, types, and simulation-to-experiment) significantly improve damage quantification accuracy. Applicable to fleet-level DT considering individual differences.

## Discussion & Implications ^sec-discussion

**Off-topic** — a helicopter-panel damage-detection DT methodology. No AECO content; recommend exclusion.

## Notes ^sec-notes

- **Screening:** Retained by keyword — DT + domain adaptation; **non-AECO (aerospace)**.
- **Relevance:** Very low; recommend exclusion / demotion.
- **Source:** Hybrid OA; abstract-grounded, full text pending.
