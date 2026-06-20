---
ref: ""
citekey: "Jinzhi-Wang2026"
title: "Research on the construction method of intelligent operation and maintenance system for electric power pipeline equipment by fusion of digital twin and AI"
authors: "Jinzhi Wang"
year: 2026
journal: "Ingegneria Sismica"
doi: "10.65102/is2026625"
zotero_key: "DGQ22SIW"
zotero_status: abstract-grounded
last_verified: "2026-06-15"
tags: ["Construction", "Deep-Learning", "Digital-Twin", "Energy", "Infrastructure", "Maintenance", "Pipeline", "Predictive", "Unsorted", "source: lens"]
---
# Jinzhi-Wang2026 — Research on the construction method of intelligent operation and maintenance system for electric power pipeline equipment by fusion of digital twin and AI

| Field | Value |
|-------|-------|
| **Ref** | — |
| **Authors** | Jinzhi Wang |
| **Year / Venue** | 2026 · *Ingegneria Sismica* |
| **DOI** | [10.65102/is2026625](https://doi.org/10.65102/is2026625) |
| **Zotero** | `DGQ22SIW` |
| **Screening** | V1: digital twin|digital twins \| V2: construction|infrastructure|pipeline \| V3: predictive|deep learning|energy|maintenance |

## Abstract ^sec-abstract

The study builds a digital twin infrastructure for electrical assembly line equipment that includes data collection, transmission and management. Facing multiple sources of data such as electrical quantity and equipment status, data characterization is used for unification. On this basis, two sets of AI diagnosis schemes are introduced. On the one hand, the ID3 decision tree algorithm is utilized to mine interpretable diagnostic rules from historical fault attribute data to achieve fast initial diagnosis. On the other hand, a deep learning model based on bi-directional Long Short-Term Memory Network (LSTM-Bi-RNN) is constructed for the temporal data with backward and forward dependency of equipment operation to realize more accurate predictive diagnosis. The decision tree model constructed based on 9 types of faults and 12-dimensional attributes generates 9 corresponding inference rules, such as heavy gas + three-phase DC resistance imbalance + high no-load loss → disconnection, light gas + chromatographic high-energy discharge + high oil temperature → joint open weld. The LSTM-Bi-RNN model achieves fast convergence in about 300 iterations, and the recognition accuracy reaches about 92%. The diagnostic F1 breaks through 95% in the test of multiple types of timing data such as voltage and current, and the running rate reaches 14.62s for 5000 current data, leading RNN, BiRNN, and comparative models such as VGG and ResNet. Dynamically mapping the physical state of equipment through digital twins and then handing it over to the fusion AI model for analysis is an effective way that can improve the automation of operation and maintenance decisions.

## Introduction & Background ^sec-intro

The study builds a **digital-twin infrastructure for electrical assembly-line equipment** covering data collection, transmission, and management, unifying multi-source data (electrical quantities, equipment status) via data characterisation.

## Method ^sec-method

Two AI diagnosis schemes are introduced: an **ID3 decision tree** mining interpretable diagnostic rules from historical fault-attribute data for fast initial diagnosis, and a **bidirectional LSTM (LSTM-Bi-RNN)** for temporal equipment data for accurate predictive diagnosis.

## Key Findings ^sec-results

The decision tree (9 fault types, 12-dimensional attributes) generates 9 inference rules; LSTM-Bi-RNN converges in ~300 iterations with ~92% accuracy and >95% F1, processing 5000 current data in 14.62 s, outperforming RNN, BiRNN, VGG, and ResNet. DT-driven physical-state mapping plus fusion AI improves O&M decision automation.

## Discussion & Implications ^sec-discussion

**Domain-adjacent** — a manufacturing/electrical-equipment DT with interpretable + deep-learning diagnosis. Outside AECO built-environment but methodologically relevant to the cognitive-DT (hybrid interpretable + DL diagnosis) theme; cite peripherally for DT-AI fault diagnosis.

## Notes ^sec-notes

- **Screening:** Retained by keyword — DT + AI fault diagnosis; **manufacturing domain (non-AECO)**.
- **Relevance:** Low–moderate; methodological cross-reference only; consider demotion.
- **Source:** Abstract-grounded; full text pending.
