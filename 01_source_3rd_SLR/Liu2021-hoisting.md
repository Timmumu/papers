# Liu et al. (2021) — Digital twin-based safety risk coupling of prefabricated building hoisting

- **ID:** 3602 | **Source:** Scopus | **DOI:** 10.3390/s21113583
- **Journal:** Sensors
- **Authors:** Liu, Z.; Meng, X.; Xing, Z.; Jiang, A.

## Abstract summary
Safety management in hoisting is the key issue to determine the development of prefabricated building construction. However, the security management in the hoisting stage lacks a truly effective method of information physical fusion, and the safety risk analysis of hoisting does not consider the interaction of risk factors. In this paper, a hoisting safety risk management framework based on digital twin (DT) is presented. The digital twin hoisting safety risk coupling model is built. The proposed model integrates the Internet of Things (IoT), Building Information Modeling (BIM), and a security risk analysis method combining the Apriori algorithm and complex network. The real-time perception and virtual–real interaction of multi-source information in the hoisting process are realized, the association rules and coupling relationship among hoisting safety risk factors are mined, and the tim…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** DT safety risk coupling of prefab hoisting; Apriori+complex network

## Step-3 Deep-Read Coding (Prompt B) — full text verified via Endnote library (front-matter DOI/title match, coverage re-scan 2026-08-12)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow | 0 | 1 | 0 | Design for Safety (DfS) | None | Statistical / change-point | Multi (two or more data types) | Single case study | 4 | Predictive analytics / decision support |

**Key evidence (AG):** DT-based safety risk coupling framework for prefabricated building hoisting (Beijing U Tech, Sensors 2021): integrates IoT + BIM with Apriori algorithm (association-rule mining among hoisting risk factors) + complex network analysis of risk-factor coupling relationships, built as a DT coupling model; real-time perception and virtual-real interaction of multi-source hoisting information, with BIM visual display to guide on-site hoisting; validated on a large-scale prefabricated project, identifying key control factors. One-way monitoring/analysis→visual guidance for managers; no actuation and no learning loop (early-warning uses mined rules, not self-updating).

**Strength & gap filled (AH):** Fills the coupling-analysis vacancy in hoisting safety: a digital twin framework combining IoT and BIM with Apriori association-rule mining (support 0.5, confidence 0.6, lift-ranked rules) mapped into a weighted complex network whose degree centrality identifies key risk nodes such as illegal operation and poor safety-protection wearing, validated on a large prefabricated project using 26 days of integrated site records.

**Deficiencies & future work (AI):** Validation data samples are acknowledged as insufficient, the mined rules lack an intelligent evaluation system, and single-project results cannot transfer to other projects without recalibration; no automated control loop is implemented. Future work integrates this coupling method with other prefabricated hoisting safety twin services.

**Fusion depth (AC1):** Fused

**Fusion evidence (AC2):**
- **Data streams:** integrated IoT + BIM hoisting records (26 days) on a large prefabricated project.
- **Integration mechanism:** Apriori mining (support 0.5, confidence 0.6) over the combined records plus weighted complex-network degree centrality produce the coupled risk-factor structure shown in the DT for guidance.
- **Why this code:** the mined coupling structure depends on multiple data sources simultaneously, so Fused.

**Confidence (AC3):** Medium - joint mining is explicit; validation data samples are acknowledged as insufficient.