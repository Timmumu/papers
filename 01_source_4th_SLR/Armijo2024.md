# Armijo, A et al. (2024) — Integration of Railway Bridge Structural Health Monitoring into the Internet of Things with a Digital Twin: A Case Study

- **ID:** R794 | **Source:** Scopus | **DOI:** 10.3390/s24072115
- **Journal:** Sensors
- **Authors:** Armijo A.; Zamora-Sánchez D.

## Abstract summary
Structural health monitoring (SHM) is critical for ensuring the safety of infrastructure such as bridges. This article presents a digital twin solution for the SHM of railway bridges using low-cost wireless accelerometers and machine learning (ML). The system architecture combines on-premises edge computing and cloud analytics to enable efficient real-time monitoring and complete storage of relevant time-history datasets. After train crossings, the accelerometers stream raw vibration data, which are processed in the frequency domain and analyzed using machine learning to detect anomalies that indicate potential structural issues. The digital twin approach is demonstrated on an in-service railway bridge for which vibration data were collected over two years under normal operating conditions. By learning allowable ranges for vibration patterns, the digital twin model identifies abnormal sp…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** Railway bridge SHM IoT with DT case study


## Step-3 Deep-Read Coding (Prompt B)
| P DT-subject | Q DfS/DfQ | R codable | U Tier | V Design | W Constr | X Oper | Z DfX | AA Self-improve | AB Methodology | AC Modality | AD Validation | AE QA(0-5) | AF Cluster |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow (one-way physical to virtual) | 0 | 0 | 1 | Design for Safety (DfS) | Implemented | Other / Mixed | Single (one data type) | Single case study | 4 | Predictive analytics / decision support |

| AC1 fusion depth | AC2 fusion evidence | AC3 confidence |
|---|---|---|
| SINGLE | Only ambient-vibration time series from wireless accelerometers feed the analytics; FEM-calibrated synthetic damage is model-generated training data, not a second measured data type. | High |

**Key evidence (AG):** 2-year in-service railway bridge pilot; unsupervised clustering of normal vibration + FEM-calibrated synthetic damage + LightGBM classifier (ROC-AUC 0.9999); periodic retraining of the model on accumulated data = implemented learning loop, but no convergence criterion/metric.

*Full-text source: 04c-port*

**AH — strength & gap filled:** Demonstrates an operational digital twin for railway bridge SHM: low-cost wireless accelerometers (about EUR 300), hybrid edge-cloud processing with real-time FFT, unsupervised clustering of normal vibration, FEM-calibrated synthetic damage data, and a LightGBM classifier reaching ROC-AUC 0.9999 on two years of in-service vibration data from a bridge in the Basque Country.

**AI — deficiencies & future work:** Detection is anomaly-based rather than damage localization or quantification, which the authors list as future work; validation is limited to one short-span bridge pilot, and analytics still rely on middleware plus cloud, with plans to move FFT and inference onto energy-harvesting edge sensors and to extend to wind towers and broader production deployments.
