# Kamari et al. (2022) — Analyzing Safety Risk Imposed by Jobsite Debris to Nearby Built Environments Using Geometric Digital Twins and Vision-Based Deep Learning

- **ID:** 3644 | **Source:** Scopus | **DOI:** 10.1061/(ASCE)CP.1943-5487.0001044
- **Journal:** Journal of Computing in Civil Engineering
- **Authors:** Kamari, M.; Kim, J.; Ham, Y.

## Abstract summary
Extreme wind events can pick up loose and small objects on the ground, and once the objects become airborne, they negatively impact surrounding communities due to the collision impact. In this regard, jobsites and laydown yards that involve construction materials such as gravel piles and crushed rocks could be the main sources of potential windborne debris during extreme wind events. To analyze safety risk and predict the damage imposed by jobsite debris to nearby built environments, a new computer vision-based risk assessment based on geometric digital twins of jobsite debris is proposed for the reliability analysis on glazing systems of dwellings located on nearby jobsites. The impact of a gravel pile in a railroad jobsite on nearby buildings and residential environments was studied based on extreme wind event scenarios, and the failure risk of the building glazing system was computed.…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** Geometric DTs of jobsite debris; glazing failure risk of nearby buildings

## Step-3 Deep-Read Coding (Prompt B) — full text verified via Endnote library (front-matter DOI/title match, coverage re-scan 2026-08-12)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 1 - Digital Model | 0 | 1 | 0 | Design for Safety (DfS) | None | Perception / Computer Vision | Multi (two or more data types) | Single case study | 4 | Design for Safety |

**Key evidence (AG):** Vision-based risk assessment of jobsite windborne-debris impact on nearby dwellings: geometric digital twin of a gravel pile built from 45 UAV aerial images (dense point cloud + binarized DSM, volume 63 m³, EM ~4.6%) + semantic segmentation of glazing panels via CNNs (ResNet50 85.0% acc) from Google Street View + satellite terrain modeling; reliability of glazing systems computed with FEMA-HAZUS windborne-missile model (N_adjusted ~237 impacts at 62 m/s, 80 m). Static one-shot reconstruction/analysis — no live data link and no learning loop.

**Strength & gap filled (AH):** Extends jobsite debris risk assessment to neighboring communities: a geometric digital twin of a railroad jobsite gravel pile built from 45 UAV images (volumetric error about 4.6 percent) feeds a HAZUS-based glazing reliability model together with ResNet50 street-view window segmentation (85.0 percent accuracy), computing failure probability of nearby dwelling glazing systems across 35 to 65 m/s wind scenarios.

**Deficiencies & future work (AI):** Relies on static Google Street View and UAV imagery with no live wind or site monitoring; facade occlusion by cars and trees degrades window detection, and performance drops in rain and fog. HAZUS assumptions such as uniform gravel size and persistent wind direction and the lack of validation against real disaster cases remain; collecting such data at scale is future work.

**Fusion depth (AC1):** Fused

**Fusion evidence (AC2):**
- **Data streams:** 45 UAV images (dense point cloud + binarised DSM, volume error about 4.6%), Google Street View imagery (ResNet50, 85.0%), satellite terrain data.
- **Integration mechanism:** the three sources jointly feed the FEMA-HAZUS windborne-missile model that computes glazing reliability (about 237 adjusted impacts at 62 m/s over 80 m), so the output depends on all of them simultaneously.
- **Why this code:** a joint multi-source reliability computation, so Fused.

**Confidence (AC3):** High - the HAZUS computation chain is explicit.