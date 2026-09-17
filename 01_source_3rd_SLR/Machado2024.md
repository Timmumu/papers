# Machado et al. (2024) — Tunnel performance prediction through degradation inspection and digital twin construction

- **ID:** 3986 | **Source:** Web of Science | **DOI:** 10.1016/j.tust.2023.105544
- **Journal:** TUNNELLING AND UNDERGROUND SPACE TECHNOLOGY
- **Authors:** Machado, L. B.; Futai, M. M.

## Abstract summary
Civil infrastructures inevitably undergo a degradation process due to extended periods of operation, frequent service requests, and weathering. This paper proposes a methodology for predicting necessary interventions and presents a database of inspection information for tunnels. The model developed correlates performance loss, measured by the tunnel serviceability index (TSI), to defects detected through a 2D grid composed of classified unit cells converted into a virtual representation. To support the framework developed, intervention time estimates were compared to stochastic degradation models presented in the literature. A limit analysis was performed using inverse exponential equations, utilizing data from different sources and supported by a digital representation of the analysis structure. This was done to estimate times with unitary inspection data, deterioration mapping control,…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** Inspection DT for tunnel degradation; serviceability & intervention prediction

## Step-3 Deep-Read Coding (Prompt B)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow (one-way physical to virtual) | 0 | 0 | 1 | Design for Safety (DfS) | None | Statistical / change-point | Multi (two or more data types) | Single case study | 4 | Lifecycle / governance |

**Key evidence (AG):** Tunnel performance prediction through degradation inspection and digital twin construction (USP): methodology correlates performance loss (tunnel serviceability index TSI) to defects via 2D grid of classified unit cells converted to virtual representation; inspection DT prototype maps zones with greatest degradation; limit analysis with inverse exponential equations estimates intervention times; railway tunnel for ore transport in northern Brazil; target intervention time 16 years. One-way inspection→TSI mapping→intervention prediction; no actuation and no learning loop (stochastic models are statistical, not learning).


**Strength & gap filled (AH):** Bridges defect-based inspection classification and performance forecasting for tunnel lifecycle management: a 2D classified-cell grid converts visual inspection data into tunnel serviceability index values, inverse exponential limit analysis validated against stochastic literature models yields a 16-year target intervention time, and an inspection digital twin of railway tunnel TL 01 attaches metadata through EleFront with online photo links.

**Deficiencies & future work (AI):** The twin is an initial prototype with manual visual inspection input and no automated synchronization, initial post-construction inspection data were missing so the initial serviceability index could not be computed, and five-year single-point data produce wide eight-year intervention intervals; future work covers automating information input and model creation from point clouds and building performance databases.
**Fusion depth (AC1):** SINGLE

**Fusion evidence (AC2):**
- **Data streams:** visual inspection classifications of tunnel TL 01 mapped onto a 2D grid of unit cells with online photo links (EleFront).
- **Integration mechanism:** none across data types - the grid is converted to tunnel serviceability index values and inverse exponential limit analysis; images serve as documentation attachments.
- **Why this code:** one measured data type (inspection records), so SINGLE. Note: column AC lists Multi because inspection photos and classifications were counted separately; under the fusion-depth rules they are one inspection-records modality.

**Confidence (AC3):** High - the inspection-grid pipeline is explicit in the full text.
(full-text source: Endnote)
