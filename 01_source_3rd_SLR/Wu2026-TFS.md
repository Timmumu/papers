# Wu et al. (2026) — Knowledge-data driven digital twin platform: intelligent prediction and control of tunnel face stability during large-diameter slurry shield construction

- **ID:** 3988 | **Source:** Web of Science | **DOI:** 10.1016/j.engappai.2026.114029
- **Journal:** ENGINEERING APPLICATIONS OF ARTIFICIAL INTELLIGENCE
- **Authors:** Wu, X. G.; Lei, Y.; Su, F. M.; Li, T. J.; Liu, Y.

## Abstract summary
Large diameter shield construction (LDSS) safety is particularly important. To ensure safe excavation in LDSS projects, this paper proposed a digital twin (DT) platform integrated with knowledge-data driven method to achieve prediction and control of tunnel face stability (TFS) during LDSS construction. The DT platform enables acquisition of physical data and expert knowledge, facilitating bidirectional synchronization between physical entities and virtual counterparts. DT platform utilizes Bayesian Optimization (BO), Graph Convolutional Network (GCN), Bidirectional Long Short-Term Memory (BiLSTM) networks, and SHapley Additive exPlanations (SHAP), driven by physical data, together with expert knowledge, to achieve knowledge-data driven prediction and control of Tunnel Face Stability (TFS) during LDSS construction. A case study of Wuhan Metro Line 12 construction demonstrates the platfor…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** Knowledge-data DT platform for tunnel face stability prediction/control

## Step-3 Deep-Read Coding (Prompt B)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 3 - Digital Twin (bidirectional, two-way) | 0 | 1 | 0 | Design for Safety (DfS) | Implemented | Graph Neural Network (GNN) | Multi (two or more data types) | Single case study | 4 | Predictive analytics / decision support |

**Key evidence (AG):** Knowledge-data driven digital twin platform for tunnel face stability (TFS) prediction and control in large-diameter slurry shield construction (HUST): bidirectional synchronization between physical entity and virtual model; BO-GCN-BiLSTM + SHAP for TFS prediction (avg R2 0.935, RMSE 0.162 across 6 geological types); expert knowledge integration; control of TFS by maintaining slurry pressure within optimal range; validated on Wuhan Metro Line 12. Bidirectional — prediction→control → Tier 3; implemented BO-GCN-BiLSTM, no convergence criterion.


**Strength & gap filled (AH):** Closes the gap between data-driven TFS models and operational control by embedding a BO-GCN-BiLSTM predictor and SHAP interpretation in a digital twin platform with bidirectional IoT and 5G links: on the Wuhan Metro Line 12 Yangtze tunnel it predicts slurry pressure across six geological types with average R-squared 0.935 and RMSE 0.162, outperforming six baselines, and iteratively keeps slurry pressure within the warning range.

**Deficiencies & future work (AI):** Generalization to abrupt or unseen geological transitions is limited because the model learns only from historical data, it lacks physical interpretability, and expert-based parameter selection remains subjective; control instructions are executed by human operators rather than automated actuation. Future research will embed geological priors and governing physical equations into the network so it can self-correct on sudden ground changes.
**Fusion depth (AC1):** Fused

**Fusion evidence (AC2):**
- **Data streams:** multi-parameter slurry-shield construction data (Wuhan Metro Line 12 Yangtze tunnel, six geological types).
- **Integration mechanism:** the GCN-BiLSTM model fuses the parameter streams to predict tunnel-face stability (average R2 0.935, RMSE 0.162, best of six baselines), and the platform feeds pressure-control guidance back through bidirectional links.
- **Why this code:** the prediction output depends on multiple data channels simultaneously and feeds a control loop, so Fused.

**Confidence (AC3):** High - the multi-input GCN-BiLSTM is explicit.
(full-text source: Endnote)
