# Armijo et al. (2024) — Integration of Railway Bridge Structural Health Monitoring into the Internet of Things with a Digital Twin: A Case Study

- **ID:** 3662 | **Source:** Scopus | **DOI:** 10.3390/s24072115
- **Journal:** Sensors
- **Authors:** Armijo, A.; Zamora-Sánchez, D.

## Abstract summary
Structural health monitoring (SHM) is critical for ensuring the safety of infrastructure such as bridges. This article presents a digital twin solution for the SHM of railway bridges using low-cost wireless accelerometers and machine learning (ML). The system architecture combines on-premises edge computing and cloud analytics to enable efficient real-time monitoring and complete storage of relevant time-history datasets. After train crossings, the accelerometers stream raw vibration data, which are processed in the frequency domain and analyzed using machine learning to detect anomalies that indicate potential structural issues. The digital twin approach is demonstrated on an in-service railway bridge for which vibration data were collected over two years under normal operating conditions. By learning allowable ranges for vibration patterns, the digital twin model identifies abnormal sp…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** DT SHM, anomaly detection, damage warnings; 2-yr pilot

## Step-3 Deep-Read Coding (Prompt B) — full text via MDPI Sensors (GOLD OA, mdpi-res mirror)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow | 0 | 0 | 1 | DfS | Implemented | Other / Mixed (LightGBM + clustering + FEM calibration) | Single | Single case study | 4 | Predictive analytics / decision support |

**Key evidence (AG):** Railway-bridge SHM DT: low-cost wireless MEMS accelerometers, on-prem edge + cloud analytics. Seven-step methodology: characterisation, deployment, preprocessing, unsupervised learning of normal vibration clusters, FE-model calibration, synthetic damage generation, supervised LightGBM (validation ROC-AUC 0.9999), and continuous learning via periodic retraining on accumulated data. Two-year in-service pilot, no maintenance required. Learning loop is implemented (scheduled retraining) but no convergence analysis. One-way physical-to-virtual only: warnings go to humans, no actuation.

**Strength & gap filled (AH):** Demonstrates an operational digital twin for railway bridge SHM: low-cost wireless accelerometers (about EUR 300), hybrid edge-cloud processing with real-time FFT, unsupervised clustering of normal vibration, FEM-calibrated synthetic damage data, and a LightGBM classifier reaching ROC-AUC 0.9999 on two years of in-service vibration data from a bridge in the Basque Country.

**Deficiencies & future work (AI):** Detection is anomaly-based rather than damage localization or quantification, which the authors list as future work; validation is limited to one short-span bridge pilot, and analytics still rely on middleware plus cloud, with plans to move FFT and inference onto energy-harvesting edge sensors and to extend to wind towers and broader production deployments.

**Fusion depth (AC1):** SINGLE

**Fusion evidence (AC2):**
- **Data streams:** wireless-accelerometer ambient-vibration time series (two years, Basque Country bridge).
- **Integration mechanism:** none - clustering of normal vibration plus a LightGBM classifier (ROC-AUC 0.9999) operate on the one measured type; FEM-calibrated synthetic damage data are model-generated training labels, not a second measured data type.
- **Why this code:** only one data type is used, so SINGLE (AC=Single).

**Confidence (AC3):** High - the single vibration modality is explicit.