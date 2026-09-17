# Zhao et al. (2026) — From instance segmentation to physical quantification: High-resolution UAV-based dataset for façade defect assessment

- **ID:** 4017 | **Source:** Web of Science | **DOI:** 10.1016/j.autcon.2026.106980
- **Journal:** AUTOMATION IN CONSTRUCTION
- **Authors:** Zhao, B. Y.; Zhang, J. H.; Huang, Y. J.; Chen, X.; Chen, B. M.

## Abstract summary
High-rise building fa & ccedil;ade inspection is essential but hazardous and labor-intensive. Although UAV imaging and defect segmentation methods can recognize defects, most studies stop at 2D masks and lack the scale and instance structure needed for grade quantification. Public fa & ccedil;ade datasets remain scarce, often low-resolution, crack-only, and annotated for semantic segmentation. This paper introduces CUBIT-InSeg, a high-resolution UAV building fa & ccedil;ade defect instance segmentation dataset. It contains 6996 images at 4800 & times; 3200 with 62,187 annotated instances of two safety-critical defects, cracks and spalling, in realistic multi-instance scenes. Over 80 models were benchmarked under a unified protocol, and transferability was assessed via zero-shot testing on two cross-domain datasets. A deployment workflow was further demonstrated that registers defects to …

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** UAV facade defect dataset + as-is DT registration; severity evaluation

## Step-3 Deep-Read Coding (Prompt B) — full text verified via Endnote library (front-matter DOI/title match, coverage re-scan 2026-08-12)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow | 0 | 0 | 1 | Design for Quality (DfQ) | None | Perception / Computer Vision | Multi (two or more data types) | Single case study | 4 | Perception / Computer Vision |

**Key evidence (AG):** CUBIT-InSeg: high-resolution UAV façade-defect instance segmentation dataset (6996 images @4800x3200, 62,187 instances of cracks/spalling) with 80+ models benchmarked and zero-shot transferability on two cross-domain datasets; deployment workflow registers defects to an as-is digital twin — integrates instance-level segmentation + photogrammetry-based reconstruction + GIS-oriented registration to project defect masks from image space onto the DT surface, converting to metric measures (crack width/length, spalling area) for standard-aligned severity (SI) assessment; validated on a multi-storey logistics building in HK. One-way inspection→DT for severity evaluation; no actuation and no learning loop.

**Strength & gap filled (AH):** Fills the gap between pixel-level defect recognition and physical severity quantification: CUBIT-InSeg provides 6996 high-resolution 4800x3200 UAV facade images with 62,187 crack and spalling instances, benchmarks over 80 models and zero-shot transfer on two cross-domain datasets, then converts masks into crack width, length and spalling area registered onto a digital twin with centimetre-level accuracy, graded per BS ISO 15686-7:2017 on a Hong Kong logistics building.

**Deficiencies & future work (AI):** Quantification depends on an approximately equal-distance imaging assumption that weakens in complex geometries with occlusion, the dataset covers only cracks and spalling from one regional context on concrete facades, and no temporal defect progression data exists. Future work will extend defect categories, facade materials and environments, reduce distance dependence and add repeated observations for deterioration analysis.

**Fusion depth (AC1):** Fused

**Fusion evidence (AC2):**
- **Data streams:** 6996 high-resolution UAV facade images (62,187 instances) + photogrammetry reconstruction + GIS-oriented registration (Hong Kong logistics building).
- **Integration mechanism:** masks are projected from image space onto the twin surface via photogrammetry and registration, then converted to crack width/length and spalling area graded per BS ISO 15686-7:2017 at centimetre-level accuracy.
- **Why this code:** the metric severity output depends on imagery and geometry simultaneously, so Fused.

**Confidence (AC3):** High - the mask-projection pipeline is explicit.