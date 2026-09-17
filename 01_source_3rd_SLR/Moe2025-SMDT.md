# Moe et al. (2025) — Safety monitoring digital twin-based centralized model consolidation mechanism using dynamic node selection for multi-worker safety prediction

- **ID:** 3944 | **Source:** Web of Science | **DOI:** 10.1016/j.engappai.2025.112186
- **Journal:** ENGINEERING APPLICATIONS OF ARTIFICIAL INTELLIGENCE
- **Authors:** Moe, S. J. S.; Rizwan, A.; Khan, A. N.; Xu, R. X.; Kim, D. H.

## Abstract summary
The construction industry remains one of the most hazardous sectors, requiring innovative solutions to safeguard workers, especially in complex, dynamic outdoor environments. Digital Twin (DT) technology offers promising capabilities for real-time safety monitoring through virtual replicas of physical systems. However, existing DT frameworks rarely integrate comprehensive safety monitoring via a centralized model consolidation mechanism, such as Federated Learning (FL), which is explicitly tailored for multi-worker scenarios. Addressing this challenge, this paper proposes a FL-based Safety Monitoring Digital Twin (SMDT) framework designed to enhance multi-worker safety in resource-constrained settings. This enables real-time safety monitoring and control by representing on-site workers as virtual objects within a synchronized DT environment. A dynamic node selection mechanism based on cl…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** FL-based Safety Monitoring DT for multi-worker safety prediction

## Step-3 Deep-Read Coding (Prompt B)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow (one-way physical to virtual) | 0 | 1 | 0 | Design for Safety (DfS) | Implemented | Other / Mixed | Multi (two or more data types) | Single case study | 4 | Predictive analytics / decision support |

**Key evidence (AG):** FL-based Safety Monitoring Digital Twin (SMDT) framework for multi-worker safety prediction (Jeju National U): DT platform + central FL server; edge devices (Raspberry Pi) represent workers and IoT nodes; real-world construction safety data (worker status, weather, structural parameters); dynamic node selection mechanism (normal distribution) optimizes global model convergence in FL; DT supports device registration, model creation, real-time control, visualization of FL training, and safety prediction. One-way monitoring→FL aggregation→safety prediction; implemented FL training loop but no convergence criterion.


**Strength & gap filled (AH):** Fills the lack of integrated multi-worker safety monitoring systems by coupling a digital twin platform with federated learning: six Raspberry Pi edge nodes train a DNN on 50,000 records of worker, weather and structural data, and a normal-distribution-based dynamic node selection improves FedAVG aggregation to R2 0.978 under IID and 0.965 under non-IID conditions with 0.551 s average inference delay.

**Deficiencies & future work (AI):** Experiments run in a controlled testbed with emulated sensors rather than an active construction site, the digital twin supports monitoring and control commands but no autonomous actuation, and only general safety prediction is covered; the authors plan field deployment, additional data features, accident-specific models and fairness plus long-term robustness evaluation.
**Fusion depth (AC1):** Fused

**Fusion evidence (AC2):**
- **Data streams:** worker status, weather and structural-parameter records across six Raspberry Pi edge nodes.
- **Integration mechanism:** normal-distribution-based dynamic node selection improves FedAVG aggregation of the multi-domain records into one safety-prediction model (R2 0.978 IID / 0.965 non-IID, 0.551 s inference).
- **Why this code:** one model trained on multiple data domains simultaneously, so Fused.

**Confidence (AC3):** High - the FL aggregation over multi-domain records is explicit.
(full-text source: Endnote)
