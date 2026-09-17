# Liu et al. (2025) — Structural safety risk prediction method for terminal building steel roof construction considering spatial and temporal variations

- **ID:** 3969 | **Source:** Web of Science | **DOI:** 10.1016/j.jcsr.2024.109126
- **Journal:** JOURNAL OF CONSTRUCTIONAL STEEL RESEARCH
- **Authors:** Liu, Z. S.; Ji, C. K.; Shi, G. L.; Mo, Y. C.

## Abstract summary
In the field of aviation, terminal building renovation and expansion projects frequently involve complex construction processes and the structure is in a non-static state during the construction process, resulting in significant safety risks accompanying these processes. In order to visualize and efficiently demonstrate the construction of airport terminal building renovation and expansion, and to provide a rapid decision-making analysis tool for the control of structural safety risks, a digital twin model for safety risk prediction of steel mesh frame structures is proposed. On this basis, taking the construction situation of an airport as an example, sensors were installed according to the results of the analysis of the finite element model, and a prediction model was established using the height parameters of twelve hydraulic jacks, the ambient temperature data and the stress data, in…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** DT safety risk prediction for terminal steel roof construction; 98% stress accuracy

## Step-3 Deep-Read Coding (Prompt B)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow (one-way physical to virtual) | 0 | 1 | 0 | Design for Safety (DfS) | None | Other / Mixed | Multi (two or more data types) | Single case study | 4 | Predictive analytics / decision support |

**Key evidence (AG):** Structural safety risk prediction for terminal building steel roof construction (Beijing U Tech): DT model + FE analysis → sensor installation (hydraulic jacks, temperature, stress); XGBoost prediction model for stress changes of key rods (98% accuracy); compared GA-BPNN, RF, XGBoost; validated on airport renovation project. One-way monitoring→prediction→risk management; no actuation and no learning loop (XGBoost is offline-trained).


**Strength & gap filled (AH):** Fills the gap between finite-element simulation and next-moment stress prediction during overall jacking of an airport terminal steel mesh roof: a digital twin built with Midas/Gen life-and-death element analysis guides sensor placement on twelve hydraulic jacks and key bars, and an XGBoost model predicts key-bar stress with 98 percent accuracy and validation R2 of 0.9919, outperforming GA-BPNN and random forest.

**Deficiencies & future work (AI):** The training set uses real site monitoring values with error superposition, the model is offline-trained on one project with only four days of jacking data, and no automated warning integration exists; the authors plan multi-source sensor fusion with real-time monitoring systems and evaluation of generalization across different steel structures and construction conditions.
**Fusion depth (AC1):** Fused

**Fusion evidence (AC2):**
- **Data streams:** hydraulic jack data, temperature and stress sensors on twelve jacks and key bars; Midas/Gen life-and-death element analysis for placement.
- **Integration mechanism:** the multi-sensor channels jointly feed XGBoost (validation R2 0.9919), outperforming GA-BPNN and random forest on an airport terminal steel-roof jacking project.
- **Why this code:** a multi-input model whose output depends on several sensor types simultaneously, so Fused.

**Confidence (AC3):** High - the XGBoost input structure is explicit.
(full-text source: Endnote)
