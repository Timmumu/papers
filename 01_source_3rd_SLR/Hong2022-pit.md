# Hong et al. (2022) — An Integrated Intelligent Approach for Monitoring and Management of a Deep Foundation Pit in a Subway Station

- **ID:** 3558 | **Source:** Scopus | **DOI:** 10.3390/s22228737
- **Journal:** Sensors
- **Authors:** Hong, C.; Zhang, J.; Chen, W.

## Abstract summary
As the scale of foundation pit projects of subway stations in Shenzhen becomes larger, and the construction constraints become more and more complex, there is an urgent need for intelligent monitoring and safety management of foundation pits. In this study, an integrated intelligent approach for monitoring and management of a deep foundation pit in a subway station was proposed and a case study based on the Waterlands Resort East Station Project of Shenzhen Metro Line 12 was used for validation. The present study first proposed the path of intelligent foundation pit engineering. Based on geotechnical survey and building information modeling, a three-dimensional transparent geological model of foundation pit was constructed. Multi-source sensing technologies were integrated, including micro electromechanical system sensing technology, Brillouin optical frequency domain analysis sensing te…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** Deep foundation pit DT platform; multi-source sensing + ML prediction

## Step-3 Deep-Read Coding (Prompt B)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow (one-way physical to virtual) | 0 | 1 | 0 | Design for Safety (DfS) | None | Other / Mixed | Multi (two or more data types) | Single case study | 4 | BIM-to-Digital-Twin architecture |

**Key evidence (AG):** Integrated intelligent approach for monitoring and management of deep foundation pit in a subway station (Shenzhen Metro Line 12 Waterlands Resort East Station): on-site geological investigation + 3D transparent geology on BIM platform; multi-source sensing (MEMS, BOFDA distributed optical fiber, laser radar, UAV, machine vision) for pit axial force/displacement/strain/temperature; BIM-based intelligent monitoring platform (proprietary cast modeling cloud platform); four ML neural networks predict key pit parameters - GA-BP achieved smallest error on this project; DT app terminal with 3D visualization, full-lifecycle monitoring, predictive analysis + AR combining BIM 3D model with real tunnel scenario. One-way monitoring to prediction to risk management; no actuation, no learning loop.



**Strength & gap filled (AH):** Fills the scarcity of whole-lifecycle intelligent monitoring for deep foundation pits with an integrated approach at Waterlands Resort East Station on Shenzhen Metro Line 12: three-dimensional transparent geology, MEMS, BOFDA distributed fiber, UAV and machine vision sensing, four neural network predictors with GA-BP performing best, plus a BIM monitoring platform and Unity3D digital twin app with AR for construction and maintenance phases.

**Deficiencies & future work (AI):** The monitoring platform currently covers only the foundation pit construction stage, and the app runs only on Android with compatibility still needing improvement; sensor stability differences make the multi-source fusion platform costly and time-consuming, and no explicit future work section is provided beyond these stated gaps.
**Fusion depth (AC1):** Fused

**Fusion evidence (AC2):**
- **Data streams:** MEMS, BOFDA distributed fibre, laser radar, UAV and machine-vision sensing of pit axial force, displacement, strain and temperature (Shenzhen Metro Line 12).
- **Integration mechanism:** sensor streams are combined in the BIM-based monitoring platform where four NNs (GA-BP best) predict key pit parameters, with Unity3D + AR visualisation; the authors explicitly describe it as a multi-source fusion platform.
- **Why this code:** multi-input predictors consume several sensing types jointly, so Fused; implemented on a real station.

**Confidence (AC3):** High - the multi-source fusion platform description is explicit.
(full-text source: Endnote)
