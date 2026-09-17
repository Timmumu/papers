# Granzner et al. (2023) — Data-Driven Condition Assessment and Life Cycle Analysis Methods for Dynamically and Fatigue-Loaded Railway Infrastructure Components

- **ID:** 4026 | **Source:** Web of Science | **DOI:** 10.3390/infrastructures8110162
- **Journal:** INFRASTRUCTURES
- **Authors:** Granzner, M.; Strauss, A.; Reiterer, M.; Cao, M. S.; Novák, D.

## Abstract summary
Railway noise barrier constructions are subjected to high aerodynamic loads during the train passages, and the knowledge of their actual structural condition is relevant to assure safety for railway users and to create a basis for forecasting. This paper deals with deterministic and probabilistic approaches for the condition assessment and prediction of the remaining lifetime of railway noise barriers that are embedded in a safety concept that takes into account the damage consequence classes. These approaches are combined into a holistic assessment concept, in other words, a progressive four-stage model in which the information content increases with each model stage and thus successively increases the accuracy of the determined structural conditions at the time of observation and the forecast of the remaining service life of the structure. The analytical methods used in the first stage…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** 4-stage concept incl. FE-based DT; safety concept & remaining-life

## Step-3 Deep-Read Coding (Prompt B) — full text verified via Endnote library (front-matter DOI match)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 1 - Digital Model | 0 | 0 | 1 | Design for Safety (DfS) | Mentioned only | Finite Element Method / physics-based | Multi (two or more data types) | Simulation | 4 | Predictive analytics / decision support |

**Key evidence (AG):** Four-stage holistic condition-assessment and life-cycle framework for fatigue-loaded railway noise barriers (ÖBB): Stage I standard fatigue calc; IIa/b/c visual-condition classes + action-side (axle-load) and resistance-side (bolt-preload) monitoring; Stage III FEM digital twin (Abaqus, ideal vs displaced-baseplate vs inclined-bolt installation conditions) calibrating stress-range/lifetime (PL0 gives 772 N/mm2 stress range vs 71 N/mm2 normative — 4x accelerated fatigue); Stage IV probabilistic approach with Bayesian updating of condition/lifetime (prior visual + likelihood monitoring/DT → posterior ZKM). DT is an offline numerical model; Bayesian updating described/demonstrated as assessment procedure, not an autonomous self-improving loop.

**Strength & gap filled (AH):** Combines deterministic and probabilistic methods into a four-stage holistic condition-assessment concept for fatigue-loaded railway noise barriers: standard fatigue calculations, visual condition classes linked with monitoring data, finite-element digital twin studies of bolt-post installation conditions, and Bayesian updating of reliability and remaining service life, grounded in large-scale fatigue tests with Austrian Federal Railways.

**Deficiencies & future work (AI):** No new data were created or analyzed in the study; the framework builds on prior experiments and model stages, and the digital twin stage remains offline without a live monitoring link. No explicit future work is stated, leaving integration into operator maintenance planning and validation on instrumented structures open.

**Fusion depth (AC1):** Unclear

**Fusion evidence (AC2):**
- **Data streams:** prior fatigue-test results, visual condition classes, FEM twin stage, Bayesian updating formulas - no new data were created or analysed.
- **Integration mechanism:** none live - the FEM twin and Bayesian stage are offline assessment procedures.
- **Why this code:** Unclear (rules 2/6).

**Confidence (AC3):** High.