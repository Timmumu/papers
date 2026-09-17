# Shariatfar, M et al. (2026) — When Roads Go Underwater: AI-Enhanced Digital Twin-Driven Flood Resilience for Roadway Serviceability Assessment

- **ID:** R217 | **Source:** Scopus | **DOI:** 10.1061/JMENEA.MEENG-7046
- **Journal:** Journal of Management in Engineering
- **Authors:** Shariatfar M.; Yin Y.; Lee Y.-C.; Choi K.

## Abstract summary
Extreme flooding poses escalating risks to roadway infrastructure, threatening structural integrity, operational reliability, and public safety. Existing flood-monitoring approaches primarily utilize sparse sensor networks, thus providing limited real-time data and insufficiently capturing indirect flooding impacts on noninundated roadway segments. This gap complicates emergency response, delays evacuation, and undermines postevent recovery efforts. Addressing this critical knowledge gap, this study proposes an advanced predictive decision-support framework leveraging an artificial intelligence (AI)-enhanced digital twin integrated with flood simulations and graph neural network (GNN) modeling. It systematically assesses roadway serviceability during extreme flooding by integrating structural conditions, operational disruptions, historical maintenance records, inundation severity, and re…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** AI+DT flood resilience for roadway serviceability


## Step-3 Deep-Read Coding (Prompt B)
| P DT-subject | Q DfS/DfQ | R codable | U Tier | V Design | W Constr | X Oper | Z DfX | AA Self-improve | AB Methodology | AC Modality | AD Validation | AE QA(0-5) | AF Cluster |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow (one-way physical to virtual) | 0 | 0 | 1 | Design for Safety (DfS) | None | Graph Neural Network (GNN) | Multi (two or more data types) | Single case study | 4 | Predictive analytics / decision support |

| AC1 fusion depth | AC2 fusion evidence | AC3 confidence |
|---|---|---|
| Fused | A graph attention network couples flood simulation with INRIX 5-minute traffic-speed data, so segment-level speed and accessibility predictions depend on both data types simultaneously. | High |

**Key evidence (AG):** AI-enhanced DT framework for roadway serviceability under floods: GAT (graph attention network) couples flood simulation with INRIX traffic-speed data (5-min speed, 6-h flood intervals) to predict segment-level speed/accessibility 45 min ahead (test MSE 0.2602), capturing direct + indirect (rerouting) impacts; GIS/ArcGIS-based 3D DT visualization for emergency decision support. Validated on Hurricane Harvey (Houston, 2 zones); explicitly a "digital twin prototype" — live sensor ingestion "not yet automated", flood scenarios precomputed, no bidirectional feedback/control; offline-trained GNN, no learning loop.

*Full-text source: 04c-port*

**AH — strength & gap filled:** Develops an AI-enhanced digital twin for flood-driven roadway serviceability that couples flood simulation with a graph attention network predicting traffic speed 45 minutes ahead from 5-minute INRIX speed data and 6-hour flood intervals, using dynamic edges that appear and disappear with inundation to capture indirect impacts on non-flooded segments; validated on Hurricane Harvey traffic for two Houston zones, with flood edge features reducing prediction MSE.

**AI — deficiencies & future work:** Flood scenarios are simulated offline with static 6-hour inundation data, live traffic is not yet ingested in real time, and no feedback or alerting loop exists; analysis covered only two Houston zip-code zones, and the model neglects inundation duration, drainage mitigation and non-flood traffic disruptions, with MSE rising after the twelfth interval. Future work targets automated real-time pipelines and broader geographic validation.
