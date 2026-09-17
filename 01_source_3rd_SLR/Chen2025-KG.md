# Chen et al. (2025) — Digital Twin-Based and Knowledge Graph-Enhanced Emergency Response in Urban Infrastructure Construction

- **ID:** 3911 | **Source:** Web of Science | **DOI:** 10.3390/app15116009
- **Journal:** APPLIED SCIENCES-BASEL
- **Authors:** Chen, C.; Lu, Y. Y.; Wu, B.; Lu, L. H.

## Abstract summary
Urban infrastructure construction poses significant risks to surrounding the infrastructure due to ground settlement, structural disturbances, and underground utility disruptions. Traditional risk assessment methods often rely on static models and experience-based decision-making, limiting their ability to adapt to dynamic construction conditions. This study proposes an integrated framework combining digital twin and knowledge graph technologies to enhance real-time risk assessment and emergency response in tunnel construction. The digital twin continuously integrates real-time monitoring data, including settlement measurements, TBM operational parameters, and structural responses, creating a virtual representation of the tunneling environment. Meanwhile, the knowledge graph structures domain knowledge and applies rule-based reasoning to infer potential hazards, detect abnormal condition…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** Real-time risk assessment, hazard inference, tunnel project applied

## Step-3 Deep-Read Coding (Prompt B) — full text via MDPI Applied Sciences (GOLD OA, mdpi-res mirror)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 3 - Digital Twin (bidirectional) | 0 | 1 | 0 | DfS | None | Ontology / semantic | Multi | Single case study | 4 | Predictive analytics / decision support |

**Key evidence (AG):** DT + knowledge-graph framework for emergency response in urban tunnel construction. DT continuously integrates real-time settlement, TBM operational parameters and structural responses; KG structures domain knowledge and applies rule-based reasoning to infer hazards, detect anomalies and suggest mitigation. Bidirectional DT-KG interaction: real-world data informs reasoning; inference results visualised in the DT for decision support. Applied to a real tunnel project in China; early anomaly identification prevented further structural impact. Rule-based, no learning update.

**Strength & gap filled (AH):** Addresses the reactive and static gap in tunnel construction emergency response: a digital twin continuously integrating settlement, TBM operational and structural monitoring data is coupled with a knowledge graph using SWRL rule-based reasoning to infer hazards, detect anomalies and suggest mitigations, with inference results visualized back in the twin; deployed on an urban tunnel project in Shanghai where it enabled early anomaly identification.

**Deficiencies & future work (AI):** Data quality dependency is acknowledged: sensor noise, loss, calibration drift and delays can misclassify risk levels; the ontology and rules are manually built for Shanghai urban tunnels, limiting scalability; reasoning speed, throughput and prediction accuracy are not quantitatively benchmarked; single-project validation; future work includes confidence metrics, automated rule generation, dynamic learning and stress testing.

**Fusion depth (AC1):** Fused

**Fusion evidence (AC2):**
- **Data streams:** settlement monitoring, TBM operational data, structural monitoring series on a Shanghai urban tunnel project.
- **Integration mechanism:** the DT continuously integrates the three streams, and a KG using SWRL rule-based reasoning performs joint hazard inference, anomaly detection and mitigation suggestions, with results visualised back in the twin.
- **Why this code:** the reasoning output depends on multiple data streams simultaneously, so Fused; implemented and demonstrated in a real emergency.

**Confidence (AC3):** High - the DT-KG coupling and SWRL reasoning are concretely described in the full text.