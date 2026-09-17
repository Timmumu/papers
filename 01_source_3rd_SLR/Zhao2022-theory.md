# Zhao et al. (2022) — An Established Theory of Digital Twin Model for Tunnel Construction Safety Assessment

- **ID:** 3923 | **Source:** Web of Science | **DOI:** 10.3390/app122312256
- **Journal:** APPLIED SCIENCES-BASEL
- **Authors:** Zhao, Y. H.; Wang, N. Q.; Liu, Z. S.

## Abstract summary
In traditional construction safety assessment, it is difficult to describe the safety status of different construction stages. To solve this problem, this paper proposes a digital twin modeling theory for construction safety assessment. Firstly, this paper analyzes the requirements of a digital twin model. Secondly, the required information is collected by IoT. Finally, the DT model is established based on the collected information. This DT model analyzes the collected information by ML, which aims to conducting the assessments of construction safety. To verify this method, this paper analyzes the vault settlement during tunnel construction. The analysis results show that the DT model can predict the settlement value with high accuracy. Moreover, the safety state is assessed dynamically based on the settlement value by DT.

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** DT model theory for tunnel construction safety assessment; settlement prediction

## Step-3 Deep-Read Coding (Prompt B)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow (one-way physical to virtual) | 0 | 1 | 0 | Design for Safety (DfS) | None | LSTM / RNN (recurrent networks) | Multi (two or more data types) | Single case study | 3 | Predictive analytics / decision support |

**Key evidence (AG):** Digital twin model theory for tunnel construction safety assessment (Beijing U Tech): IoT + smart sensors collect project data; DT built combining BIM + Midas + LSTM ML algorithm; black-box/gray-box/white-box hierarchical data processing; vault (arch crown) settlement predicted with high accuracy and dynamic safety-state assessment during tunnel construction. One-way monitoring->prediction->assessment; no actuation, no learning loop (LSTM offline-trained).


**Strength & gap filled (AH):** Fills the gap of static risk assessment that cannot track dynamic tunnel construction: a digital twin theory fuses IoT-collected data into geometry, physics and knowledge models (BIM, Midas, LSTM) with black-box, gray-box and white-box accuracy levels, and LSTM prediction of vault settlement (RMSE 0.0929 mm, maximum error about 0.135 mm) drives displacement-level safety grading against a 120 mm design limit.

**Deficiencies & future work (AI):** Only vault settlement is verified, on a single Grade-V rock tunnel section with data collected once per day, so real-time continuous mapping is not demonstrated and assessment of other risk types remains theoretical. Authors state they will verify the method across as many security risk categories as possible to strengthen the theory.
**Fusion depth (AC1):** Fused

**Fusion evidence (AC2):**
- **Data streams:** IoT + smart-sensor project data on a Grade-V rock tunnel section.
- **Integration mechanism:** the twin fuses sensor data into geometry, physics and knowledge models, and LSTM predicts vault settlement (RMSE 0.0929 mm) graded against the 120 mm design limit.
- **Why this code:** the prediction output depends on multiple sensor channels simultaneously, so Fused.

**Confidence (AC3):** High - the fused twin construction is explicit; only vault settlement is verified.
(full-text source: Endnote)
