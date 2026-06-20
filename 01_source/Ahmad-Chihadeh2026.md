---
ref: ""
citekey: "Ahmad-Chihadeh2026"
title: "Identification and evaluation of uncertainty sources of materials and sensors for the digital twin road initiative"
authors: "Ahmad Chihadeh; Maria Böttcher; David Crampen; Erik Kamratowsky; Moritz Hagmanns; Jitong Zhao; Sebastian Ullmann; Ventseslav Yordanov; Gustavo Canon Falla; Simon Schäfer; Bassam Alrifaee; Marco Liebscher; Marko Butler; Sabine Leischner; Adrian Fazekas; Wolfgang Graf; Ivo Herle; Viktor Mechtcherine; Alexander Zeißler; Lutz Eckstein; Markus Oeser; Jörg Blankenbach; Michael Kaliske"
year: 2026
journal: "Structure and Infrastructure Engineering"
doi: "10.1080/15732479.2026.2645822"
zotero_key: "9FQ7L8LZ"
zotero_status: verified
last_verified: "2026-06-15"
tags: ["Digital-Twin", "Road", "Unsorted", "source: lens", "identification: databases"]
---
# Ahmad-Chihadeh2026 — Identification and evaluation of uncertainty sources of materials and sensors for the digital twin road initiative

| Field | Value |
|-------|-------|
| **Ref** | — |
| **Authors** | Ahmad Chihadeh; Maria Böttcher; David Crampen; Erik Kamratowsky; Moritz Hagmanns; Jitong Zhao; Sebastian Ullmann; Ventseslav Yordanov; Gustavo Canon Falla; Simon Schäfer; Bassam Alrifaee; Marco Liebscher; Marko Butler; Sabine Leischner; Adrian Fazekas; Wolfgang Graf; Ivo Herle; Viktor Mechtcherine; Alexander Zeißler; Lutz Eckstein; Markus Oeser; Jörg Blankenbach; Michael Kaliske |
| **Year / Venue** | 2026 · *Structure and Infrastructure Engineering* |
| **DOI** | [10.1080/15732479.2026.2645822](https://doi.org/10.1080/15732479.2026.2645822) |
| **Zotero** | `9FQ7L8LZ` |
| **Screening** | V1: digital twin \| V2: road \| V3: uncertainty |

## Abstract ^sec-abstract

> The Digital Twin Road initiative aims to improve road infrastructure monitoring and maintenance through real-time data integration, computational modelling, and predictive analytics. However, the reliability of such digital twins is significantly affected by uncertainties in both material properties and sensor data. This paper provides a comprehensive evaluation of uncertainty sources within the CRC/TRR 339 - Digital Twin Road project. Material-related uncertainties stem from the intrinsic variability of asphalt, concrete, and soil due to production methods, environmental exposure, and construction practices. These include aleatoric uncertainties from natural variability and epistemic uncertainties from knowledge gaps. Sensor-related uncertainties arise from limitations in sensor technology, calibration, environmental influences, and data processing algorithms. Detailed case studies, including weigh-in-motion systems, drone-mounted laser scanning, and smart materials such as mineral-impregnated carbon-fibre (MCF) reinforced low-clinker concrete, illustrate how uncertainties accumulate and propagate across the Digital Twin Road framework. The classification of uncertainty into aleatoric and epistemic categories is discussed. Understanding these uncertainty sources is essential for improving the predictive accuracy and ensuring a robust representation of real-world road systems.

## Introduction & Background ^sec-intro

*Abstract unavailable from the Lens export; inferred from title/venue only — confirm at full-text review (PDF is available in the Zotero library).* The paper identifies and evaluates uncertainty sources of materials and sensors for the "digital twin road" initiative (*Structure and Infrastructure Engineering*, 2026).

## Method ^sec-method

**Approach:** Systematic uncertainty-source identification and classification within the CRC/TRR 339 Digital Twin Road project (Germany). Conceptual framework grounded in the aleatoric–epistemic uncertainty taxonomy. **Material uncertainties** traced to intrinsic variability of asphalt, concrete, and soil (production methods, environmental exposure, construction practices). **Sensor uncertainties** traced to hardware limitations, calibration drift, environmental interference, and data-processing algorithms. **Case-study validation** using three representative DT-Road subsystems: (1) weigh-in-motion (WIM) systems for traffic loading, (2) drone-mounted laser scanning for geometric surveys, and (3) smart materials — mineral-impregnated carbon-fibre (MCF) reinforced low-clinker concrete — as an example of novel material sensing.

**Paradigm:** Analytical/framework paper — no new empirical data; contribution is taxonomical and methodological.

## Key Findings ^sec-results

1. **Dual-source uncertainty framework:** Material-related uncertainties (aleatoric: natural variability; epistemic: knowledge gaps in production/construction) and sensor-related uncertainties (technology limitations, calibration, environmental noise, algorithmic bias) are the two dominant uncertainty vectors in road DTs.
2. **Uncertainty propagation illustrated:** WIM systems, drone LiDAR, and MCF-concrete case studies demonstrate how uncertainties from multiple sources compound across the DT data pipeline, from physical sensing to model prediction.
3. **Taxonomic contribution:** Provides a structured, transferable classification of uncertainty types (aleatoric vs. epistemic, material vs. sensor) applicable beyond road infrastructure to other civil DT domains.
4. **Practical implication:** Understanding and quantifying these uncertainties is prerequisite for trustworthy predictive accuracy in DT-based road asset management.

## Discussion & Implications ^sec-discussion

**Relevance to cognitive DT framework:** This paper directly addresses one of the most under-theorized dimensions in AECO-DT research — *uncertainty quantification (UQ)* . While the DT literature is rich in architecture descriptions and proof-of-concept demonstrations, systematic treatment of how uncertainties propagate from physical sensing through to model prediction is rare. This paper fills that gap for the road-infrastructure subdomain.

**Research gap filled:** Bridges the UQ gap identified in the LR — specifically, the need for structured frameworks to classify, trace, and mitigate uncertainties in DT data pipelines. The aleatoric–epistemic taxonomy (tracing back to Der Kiureghian & Ditlevsen 2009) is appropriately applied to the DT-for-roads context.

**Limitations (from abstract):**
- **Framework paper without quantitative UQ:** the case studies illustrate uncertainty sources but do not present numerical UQ results (e.g., sensitivity indices, propagated error bounds).
- **Road-specific scope:** findings are contextualized within the CRC/TRR 339 project; transferability to building, bridge, or tunnel DTs requires adaptation.
- **Sensor scope limited to three types:** WIM, drone LiDAR, and MCF — other sensor modalities common in civil infrastructure (fiber optics, accelerometers, corrosion sensors) not addressed.

**Future work (inferred):**
- Quantitative UQ: propagate identified uncertainties through a full DT model to assess predictive reliability.
- Extend framework to other infrastructure types (bridges, tunnels).
- Integrate UQ into DT governance/decision-support: how should uncertainty bounds inform maintenance decisions?
- Develop standardized uncertainty metadata schemas for DT data ingestion.

**Contribution to LR:** Foundational reference for the *data trustworthiness* and *UQ* gap in the cognitive DT framework. Supports the argument that a cognitive DT requires not just data integration but explicit uncertainty-awareness.

## Notes ^sec-notes

- **Screening:** Retained — DT + infrastructure + sensor/material uncertainty (strong fit to UQ gap in LR).
- **Status:** `abstract-grounded` — abstract retrieved from EndNote (key 9FQ7L8LZ).
- **Maturity:** Conceptual/framework — no DT maturity level applicable (taxonomical contribution).
- **PDF available:** In EndNote `.Data/PDF/`.
- **Priority:** HIGH — directly addresses the UQ gap identified in the LR framework.
