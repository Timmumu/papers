# Zhu et al. (2022) — Intelligent Prediction of Prestressed Steel Structure Construction Safety Based on BP Neural Network

- **ID:** 4039 | **Source:** Web of Science | **DOI:** 10.3390/app12031442
- **Journal:** APPLIED SCIENCES-BASEL
- **Authors:** Zhu, H. L.; Wang, Y. S.

## Abstract summary
In the construction process of a prestressed steel structure, it is a point of research interest to obtain the safety state of the structure according to the design parameters and working conditions of the structure. The intelligent prediction of structural construction safety provides the basis for safety control. This study proposes an intelligent prediction method of structural construction safety based on a back propagation (BP) neural network. Firstly, the correlation mechanism of structural construction safety performance parameters is established, which involves structural design parameters and mechanical parameters. According to the basic principle of a BP neural network, the relationship between design parameters and mechanical parameters is captured. The virtual model of a structure construction process is established based on digital twins (DTs). The DTs and BP neural network …

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** DT+BP NN for prestressed steel construction safety prediction

## Step-3 Deep-Read Coding (Prompt B)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow (one-way physical to virtual) | 0 | 1 | 0 | Design for Safety (DfS) | None | Other / Mixed | Multi (two or more data types) | Single case study | 4 | Predictive analytics / decision support |

**Key evidence (AG):** Intelligent prediction of prestressed steel structure construction safety based on BP neural network (South China U Tech): DT virtual model of construction process; BP neural network captures relationship between design parameters and mechanical parameters; working conditions set in twin model to obtain mechanical parameters, then safety performance evaluated; applied to string beam construction; predicted results verified against on-site measured data. One-way monitoring->BP prediction->safety assessment; no actuation, no learning loop.


**Strength & gap filled (AH):** Establishes a correlation mechanism between structural design parameters and mechanical parameters and fuses it with a four-level geometry-physics-behavior-rule digital twin, training a BP neural network on finite element samples to intelligently predict construction safety of a string beam. Predicted vertical displacement and lower-chord cable stress were verified against field measurements, providing a basis for safety control.

**Deficiencies & future work (AI):** The BP network is trained only on finite element simulation data, only two mechanical parameters are predicted, and validation covers a single string beam of one convention center roof; no online updating from live monitoring is implemented. Future research will combine mechanical with design parameters to find key safety factors and consider more realistic conditions.
**Fusion depth (AC1):** Aligned

**Fusion evidence (AC2):**
- **Data streams:** FE-derived design/mechanical parameter samples + on-site string-beam verification measurements.
- **Integration mechanism:** the four-level geometry-physics-behaviour-rule twin links design and mechanical parameters, the BP network is trained on FE samples, and field measurements verify predictions.
- **Why this code:** measured data are mapped onto the model frame for verification, so Aligned.

**Confidence (AC3):** Medium - the verification linkage is explicit; no joint multi-source inference exists.
(full-text source: Endnote)
