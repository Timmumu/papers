---
ref: ""
citekey: "Geng-Tian2026"
title: "AI-enhanced large-eddy simulation for urban wind flows: accelerating spin-up with Fourier neural operator initialization"
authors: "Geng Tian; Shaoxiang Qin; Dingyang Geng; Dongxue Zhan; Senwen Yang; Peng Liu; Naiping Gao; Liangzhu Leon Wang"
year: 2026
journal: "Building and Environment"
doi: "10.1016/j.buildenv.2025.114046"
zotero_key: "43VJRDEL"
zotero_status: abstract-grounded
last_verified: "2026-06-15"
tags: ["Building", "Deep-Learning", "Digital-Twin", "Safety", "Simulation", "Unsorted", "Urban", "source: lens"]
---
# Geng-Tian2026 — AI-enhanced large-eddy simulation for urban wind flows: accelerating spin-up with Fourier neural operator initialization

| Field | Value |
|-------|-------|
| **Ref** | — |
| **Authors** | Geng Tian; Shaoxiang Qin; Dingyang Geng; Dongxue Zhan; Senwen Yang; Peng Liu; Naiping Gao; Liangzhu Leon Wang |
| **Year / Venue** | 2026 · *Building and Environment* |
| **DOI** | [10.1016/j.buildenv.2025.114046](https://doi.org/10.1016/j.buildenv.2025.114046) |
| **Zotero** | `43VJRDEL` |
| **Screening** | V1: digital twins \| V2: building|urban \| V3: safety|deep learning|simulation |

## Abstract ^sec-abstract

Urban wind simulations based on large-eddy simulation (LES) offer high fidelity in capturing turbulent dynamics across complex building geometries. However, their practical application remains limited due to the high computational cost associated with the prolonged spin-up period required to reach statistically steady turbulence. This study introduces a hybrid deep learning–CFD framework that leverages the Fourier Neural Operator (FNO) to generate physically consistent initial flow fields, thereby significantly reducing LES initialization time. A customized FNO model, Flume-FNO, is trained on 30 LES-generated flow cases over real urban geometries worldwide using GPU-accelerated simulations. To enhance geometric representation, the model incorporates multi-directional distance features (MDDF) and a localization strategy, enabling accurate flow field prediction from building morphology alone. The predicted fields are then used to restart LES, yielding mean velocity profiles, turbulence statistics, and mean pressure coefficients that closely match those of fully developed LES results. Quantitative evaluations show a velocity profile error below 5 % and accurate reproduction of coherent structures such as vorticity and shear layers. Furthermore, the FNO-initialized simulations achieve up to a 48.8 % reduction in spin-up time. This work demonstrates a scalable, efficient, and generalizable approach to accelerating urban LES using deep learning priors, with applications in microclimate modeling, pedestrian wind comfort, eVTOL safety, and digital twins. • Develops a hybrid AI-CFD framework to accelerate high-fidelity urban wind simulations. • Accurately predicts flow structures, turbulence statistics, and aerodynamic behavior in complex urban settings. • Reduces LES simulation time by nearly 50 % while retaining high-resolution detail and physical fidelity. • Accurately resolves key aerodynamic features around complex urban geometries, including pressure zones, vortices, and wake dynamics.

## Introduction & Background ^sec-intro

Large-eddy simulation (LES) captures urban turbulent dynamics with high fidelity but is limited in practice by the costly spin-up needed to reach statistically steady turbulence. The paper targets this bottleneck for digital-twin-relevant urban wind modelling.

## Method ^sec-method

A hybrid deep-learning–CFD framework uses a Fourier Neural Operator (FNO) to generate physically consistent initial flow fields that restart LES. A customised model, Flume-FNO, is trained on 30 LES cases over real urban geometries with GPU acceleration; multi-directional distance features (MDDF) and a localisation strategy enable flow-field prediction from building morphology alone.

## Key Findings ^sec-results

FNO-initialised LES reproduces mean velocity profiles, turbulence statistics, and pressure coefficients close to fully developed LES, with velocity-profile error below 5% and accurate coherent structures (vorticity, shear layers). Spin-up time is reduced by up to 48.8%.

## Discussion & Implications ^sec-discussion

Demonstrates AI surrogates/priors accelerating high-fidelity physics simulation — a key enabler for *real-time-capable* environmental digital twins (microclimate, pedestrian wind comfort, eVTOL safety). Methodologically relevant to making CFD-backed DTs fast enough for operational use.

## Notes ^sec-notes

- **Screening:** Retained — DT-adjacent (urban wind/microclimate) + AI-accelerated simulation; explicitly cites digital-twin applications.
- **Relevance:** Exemplar of *neural-operator surrogates* to make physics-based DTs real-time — supports the speed/fidelity theme.
- **Caveat:** Core contribution is CFD acceleration; DT is an application framing.
