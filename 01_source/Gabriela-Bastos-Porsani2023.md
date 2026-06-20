---
ref: ""
citekey: "Gabriela-Bastos-Porsani2023"
title: "Empirical evaluation of EnergyPlus infiltration model for a case study in a high-rise residential building"
authors: "Gabriela Bastos Porsani; Núria Casquero-Modrego; Juan Bautista Echeverria Trueba; Carlos Fernández Bandera"
year: 2023
journal: "Energy and Buildings"
doi: "10.1016/j.enbuild.2023.113322"
zotero_key: "88SYYGJZ"
zotero_status: abstract-grounded
last_verified: "2026-06-15"
tags: ["Building", "Digital-Twin", "Energy", "Quality", "Real-Time", "Unsorted", "source: lens"]
---
# Gabriela-Bastos-Porsani2023 — Empirical evaluation of EnergyPlus infiltration model for a case study in a high-rise residential building

| Field | Value |
|-------|-------|
| **Ref** | — |
| **Authors** | Gabriela Bastos Porsani; Núria Casquero-Modrego; Juan Bautista Echeverria Trueba; Carlos Fernández Bandera |
| **Year / Venue** | 2023 · *Energy and Buildings* |
| **DOI** | [10.1016/j.enbuild.2023.113322](https://doi.org/10.1016/j.enbuild.2023.113322) |
| **Zotero** | `88SYYGJZ` |
| **Screening** | V1: digital twins \| V2: building|buildings|indoor \| V3: quality|uncertainty|energy|real-time |

## Abstract ^sec-abstract

The European Council has proposed reducing buildings' energy consumption as one way to decarbonization by 2050. Currently, digital twins are used for real-time energy management, but there are discrepancies between predicted and measured energy performance due to uncertainties in building energy models (BEMs). Air leakage is a key parameter that is difficult to obtain and EnergyPlus users often employ a constant value or apply air leakage equations with pre-determined coefficients. This research is a preliminary step in reducing this uncertainty in the author's methodology of BEMs calibration, using EnergyPlus and measured data. The study empirically verifies the ability of the EnergyPlus model's design flow rate to accurately replicate dynamic infiltration values within a zone of a high-rise residential building, where a tracer gas test using CO2 and a blower door test were conducted. Three new methods for calculating Idesign were developed and evaluated. The results were assessed based on the American Society for Testing Material D5157 (Standard Guide for Statistical Evaluation of Indoor Air Quality Models). The models generated with ad-hoc coefficients were compared to those from the literature (EnergyPlus, DOE-2, and BLAST). Among the models with off-the-shelf coefficients, the one with Idesign calculated with in situ data and DOE-2 coefficients demonstrates an accuracy that is only 26% lower than the best model with regression coefficients, which has an R2 value of 0.94 and an NMSE value of 0.02 in the training period.

## Introduction & Background ^sec-intro

**Digital twins** are used for real-time energy management, but discrepancies between predicted and measured energy performance exist due to BEM uncertainties. Air leakage is a key parameter difficult to obtain. The study verifies EnergyPlus air-infiltration modelling for DT calibration.

## Method ^sec-method

Tracer gas test (CO2) and blower door test in a high-rise residential building. Three new methods for calculating Idesign were evaluated against EnergyPlus, DOE-2, and BLAST coefficients.

## Key Findings ^sec-results

The model with in-situ Idesign and DOE-2 coefficients achieved accuracy only 26% lower than the best regression model (R²=0.94, NMSE=0.02).

## Discussion & Implications ^sec-discussion

**Relevant** — a building-energy DT calibration study addressing air-leakage uncertainty. Useful for the DT-energy and calibration strands.

## Notes ^sec-notes

- **Screening:** Retained — DT + BEM + air leakage + calibration (good fit).
- **Relevance:** Cite for DT BEM air-leakage calibration.
- **Source:** Hybrid OA; abstract-grounded, full text pending.
