# Shariatfar et al. (2026) — When Roads Go Underwater: AI-Enhanced Digital Twin-Driven Flood Resilience for Roadway Serviceability Assessment

- **ID:** 3823 | **Source:** Scopus | **DOI:** 10.1061/JMENEA.MEENG-7046
- **Journal:** Journal of Management in Engineering
- **Authors:** Shariatfar, M.; Yin, Y.; Lee, Y. C.; Choi, K.

## Abstract summary
Extreme flooding poses escalating risks to roadway infrastructure, threatening structural integrity, operational reliability, and public safety. Existing flood-monitoring approaches primarily utilize sparse sensor networks, thus providing limited real-time data and insufficiently capturing indirect flooding impacts on noninundated roadway segments. This gap complicates emergency response, delays evacuation, and undermines postevent recovery efforts. Addressing this critical knowledge gap, this study proposes an advanced predictive decision-support framework leveraging an artificial intelligence (AI)-enhanced digital twin integrated with flood simulations and graph neural network (GNN) modeling. It systematically assesses roadway serviceability during extreme flooding by integrating structural conditions, operational disruptions, historical maintenance records, inundation severity, and re…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** AI-enhanced DT flood resilience of roadways; serviceability & emergency

## Step-3 Deep-Read Coding (Prompt B) — full text verified via Endnote library (front-matter DOI match)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow | 0 | 0 | 1 | Design for Safety (DfS) | None | Graph Neural Network (GNN) | Multi (two or more data types) | Single case study | 4 | Predictive analytics / decision support |

**Key evidence (AG):** AI-enhanced DT framework for roadway serviceability under floods: GAT (graph attention network) couples flood simulation with INRIX traffic-speed data (5-min speed, 6-h flood intervals) to predict segment-level speed/accessibility 45 min ahead (test MSE 0.2602), capturing direct + indirect (rerouting) impacts; GIS/ArcGIS-based 3D DT visualization for emergency decision support. Validated on Hurricane Harvey (Houston, 2 zones); explicitly a "digital twin prototype" — live sensor ingestion "not yet automated", flood scenarios precomputed, no bidirectional feedback/control; offline-trained GNN, no learning loop.

**Strength & gap filled (AH):** Develops an AI-enhanced digital twin for flood-driven roadway serviceability that couples flood simulation with a graph attention network predicting traffic speed 45 minutes ahead from 5-minute INRIX speed data and 6-hour flood intervals, using dynamic edges that appear and disappear with inundation to capture indirect impacts on non-flooded segments; validated on Hurricane Harvey traffic for two Houston zones, with flood edge features reducing prediction MSE.

**Deficiencies & future work (AI):** Flood scenarios are simulated offline with static 6-hour inundation data, live traffic is not yet ingested in real time, and no feedback or alerting loop exists; analysis covered only two Houston zip-code zones, and the model neglects inundation duration, drainage mitigation and non-flood traffic disruptions, with MSE rising after the twelfth interval. Future work targets automated real-time pipelines and broader geographic validation.

**Fusion depth (AC1):** Fused

**Fusion evidence (AC2):**
- **Data streams:** flood simulation grids (6-h intervals) + INRIX 5-min traffic speeds (Hurricane Harvey, two Houston zones).
- **Integration mechanism:** dynamic edges that appear/disappear with inundation couple the two streams inside the GAT, predicting speed 45 min ahead (test MSE 0.2602) and capturing rerouting impacts.
- **Why this code:** the prediction model output depends on two coupled data types simultaneously, so Fused.

**Confidence (AC3):** High - the flood-traffic coupling mechanism is explicit.