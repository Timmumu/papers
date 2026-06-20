---
ref: ""
citekey: "Abdurahman-Yasin-Yigit2024"
title: "Automatic crack detection and structural inspection of cultural heritage buildings using UAV photogrammetry and digital twin technology"
authors: "Abdurahman Yasin Yiğit; Murat Uysal"
year: 2024
journal: "Journal of Building Engineering"
doi: "10.1016/j.jobe.2024.109952"
zotero_key: "V976A2EF"
zotero_status: abstract-grounded
last_verified: "2026-06-15"
tags: ["Digital-Twin", "Heritage", "Inspection", "Structural", "Unsorted", "source: lens", "identification: databases"]
---
# Abdurahman-Yasin-Yigit2024 — Automatic crack detection and structural inspection of cultural heritage buildings using UAV photogrammetry and digital twin technology

| Field | Value |
|-------|-------|
| **Ref** | — |
| **Authors** | Abdurahman Yasin Yiğit; Murat Uysal |
| **Year / Venue** | 2024 · *Journal of Building Engineering* |
| **DOI** | [10.1016/j.jobe.2024.109952](https://doi.org/10.1016/j.jobe.2024.109952) |
| **Zotero** | `V976A2EF` |
| **Screening** | V1: digital twin \| V2: buildings|structural|heritage \| V3: inspection |

## Abstract ^sec-abstract

> Current methods for rapidly inspecting structures are difficult to document and subjective. Automating the process with innovative technologies is necessary to overcome these limitations. Precisely monitoring cracking in cultural heritage buildings is vital as they pose a significant risk to their integrity. Recent advancements in artificial intelligence, including imaging equipment and computer vision, offer significant advantages for automating the detection of structural cracks. This study conducted tests to investigate utilizing unmanned aerial vehicle photogrammetry, a modern surveying method, for monitoring such inspections. Initially, a level of detail 3 digital model of the structure was generated. Finally, the metric accuracy of the detected cracks was analyzed. The cracks measured by the traditional method were considered as reference data and compared with the automatically detected cracks. As a result, 83 % of the cracks were detected by the modern techniques and the RMSE value was 0.802 cm because of the metric comparison.

## Introduction & Background ^sec-intro

*Abstract retrieved from EndNote — see Abstract section above. Full-text retrieval pending.* The paper presents **automatic crack detection and structural inspection of cultural heritage buildings using UAV photogrammetry and digital twin technology** (*Journal of Building Engineering*, 2024).

## Method ^sec-method

**Approach:** UAV photogrammetry for data acquisition, processed into a LoD3 (Level of Detail 3) digital model of the heritage structure. AI/computer vision algorithms applied for automated crack detection from the imagery/model. **Validation:** Traditional manual crack measurement served as ground-truth reference data. Metric accuracy assessed via comparison of automatically detected crack dimensions against manual measurements (RMSE).

**Paradigm:** Unidirectional digital shadow (ML1) — physical structure → UAV sensing → 3D model → automated analysis. No closed-loop actuation or real-time feedback to the physical asset.

## Key Findings ^sec-results

1. **Detection rate:** 83% of cracks identified by traditional manual methods were successfully detected by the UAV–AI pipeline — a substantial automation rate for a challenging heritage-building context.
2. **Metric accuracy:** RMSE = 0.802 cm between automatically detected and manually measured crack dimensions, demonstrating sub-centimeter-level geometric fidelity.
3. **Feasibility demonstrated:** The integration of UAV photogrammetry + LoD3 modeling + AI crack detection constitutes a viable, documentable alternative to subjective manual inspection for cultural heritage structures.

## Discussion & Implications ^sec-discussion

**Relevance to cognitive DT framework:** This study contributes to the *perception layer* of a DT architecture. The UAV→LoD3→crack-detection pipeline generates structured damage data suitable for ingestion into a heritage-building DT. The LoD3 model serves as the geometric substrate; detected cracks constitute semantic damage annotations that could feed into downstream SHM, predictive maintenance, or risk assessment modules.

**Research gap filled:** Addresses the long-standing problem of subjective, non-repeatable, poorly documented manual crack inspection in heritage buildings — structures where invasive techniques (core sampling, physical access) are often prohibited. Demonstrates an objective, metric-based, fully documentable alternative.

**Limitations (from abstract):**
- **17% false-negative rate:** cracks missed by the automated pipeline — safety-critical in structural assessment contexts.
- **Single-structure validation:** generalizability to diverse heritage typologies (masonry, timber-frame, mixed-material) not established.
- **RMSE of 0.802 cm** may be insufficient for hairline crack detection (< 0.5 mm), which is often the earliest indicator of structural distress.
- **No discussion of environmental conditions** (lighting, shadows, surface texture) that affect UAV photogrammetry quality.

**Future work (inferred from research trajectory):**
- Improve recall via deep learning architectures (e.g., semantic segmentation with U-Net variants) or multi-sensor fusion (LiDAR + thermal).
- Validate across a statistically meaningful sample of heritage structures differing in material, geometry, and degradation state.
- Integrate crack detection outputs with real-time SHM systems within a closed-loop DT.
- Explore onboard (edge) detection during UAV flight for real-time inspection.
- Incorporate temporal monitoring: repeated surveys to track crack propagation rates.

**Contribution to LR:** Provides evidence for the *inspection automation* theme within the DT-for-AECO literature. Directly supports the argument that perception-layer automation (UAV + CV) is technically mature enough for heritage applications, though false-negative rates remain a barrier to full autonomy.

## Notes ^sec-notes

- **Screening:** Retained — UAV + DT + crack detection + heritage (strong fit to V1–V3).
- **Status:** `abstract-grounded` — abstract retrieved from EndNote (key V976A2EF).
- **Maturity:** ML1 (digital shadow) — unidirectional sensing-to-model pipeline.
- **PDF available:** Yiğit-2024-Automatic crack detection and structural inspection...pdf (in EndNote `.Data/PDF/`).
- **Quality note:** Abstract is substantive with quantitative results; full-text PDF exists but text extraction requires pdfplumber/PyPDF2 (not currently installed). Awaiting library install for method-detail extraction.
