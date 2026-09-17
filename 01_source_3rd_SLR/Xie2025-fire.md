# Xie et al. (2025) — AIoT-powered building digital twin for smart firefighting and super real-time fire forecast

- **ID:** 3927 | **Source:** Web of Science | **DOI:** 10.1016/j.aei.2025.103117
- **Journal:** ADVANCED ENGINEERING INFORMATICS
- **Authors:** Xie, W. K.; Zeng, Y. F.; Zhang, X. N.; Wong, H. Y.; Zhang, T. H.; Wang, Z. L.; Wu, X. Q.; Shi, J. H.; Huang, X. Y.; Xiao, F.; Usmani, A.

## Abstract summary
Complex dynamics inherent of building fire poses big challenges to firefighting and rescue, especially with limited access to critical fire-hazard information. This work proposes the novel AIoT-integrated Digital Twin for the full-scale multi-floor building to manage the dynamics fire information. This system allows for super realtime mapping of actual building fires into accurate and concise digital fire scene at the cloud platform. By developing the ADLSTM-Fire model, we effectively transform discrete sensor-array data into high-dimensional spatiotemporal temperature fields in real-time, and furthermore, forecast future fire development and hazardous regions 60 s in advance. By comparing with benchmark numerical simulations, the Digital Twin system demonstrates the high reliability of super real-time fire-scene reconstruction and the capacity of fire-risk forecasting in supporting fire…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** AIoT DT for smart firefighting; super real-time fire forecast

## Step-3 Deep-Read Coding (Prompt B)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow (one-way physical to virtual) | 0 | 0 | 1 | Design for Safety (DfS) | None | LSTM / RNN (recurrent networks) | Multi (two or more data types) | Single case study | 4 | Design for Safety |

**Key evidence (AG):** AIoT-powered building digital twin for smart firefighting and super real-time fire forecast (PolyU): AIoT-integrated DT maps building fires to digital fire scene; ADLSTM-Fire model transforms discrete sensor-array data into high-dimensional spatiotemporal temperature fields; forecasts fire development and hazardous regions 60s in advance; validated via full-scale building fire experiment; 93% reconstruction accuracy, 92% forecast accuracy. One-way monitoring→forecast→firefighting support; no actuation and no learning loop (offline-trained).


**Strength & gap filled (AH):** Bridges the gap between sparse on-site sensor readings and comprehensive understanding of building fire dynamics: an AIoT-integrated digital twin with LoRa wireless thermometry whose ADLSTM-Fire model reconstructs the full spatiotemporal temperature field from discrete sensor-array data (R2 93%) and forecasts fire development 60 s ahead (R2 92%), validated against CFD benchmarks and full-scale building fire experiments.

**Deficiencies & future work (AI):** The model is offline-trained on numerical simulation data and the advance forecast is less precise than reconstruction, with up to 18% error in one experimental scenario; future work refines ADLSTM-Fire for unfamiliar buildings, adds building layout as an input parameter, enriches datasets with structural and wind factors, optimizes sensor layouts, and tests more building types.
**Fusion depth (AC1):** Aligned

**Fusion evidence (AC2):**
- **Data streams:** LoRa wireless thermometry sensor-array readings + CFD-benchmark temperature fields.
- **Integration mechanism:** ADLSTM-Fire transforms discrete readings into the high-dimensional spatiotemporal field (93% reconstruction, 92% 60-s-ahead forecast R2), validated against CFD and full-scale fire experiments.
- **Why this code:** one measured stream is registered onto the learned field model, so Aligned (single measured type; the CFD fields are model-generated).

**Confidence (AC3):** Medium - the array-to-field mapping is explicit; fusion depth beyond registration is limited.
(full-text source: Endnote)
