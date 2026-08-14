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
