# Shen, W et al. (2026) — Reverse digital twin mapping of building envelope anomalies based on UAV infrared point clouds

- **ID:** R111 | **Source:** Scopus | **DOI:** 10.1016/j.measurement.2025.119256
- **Journal:** Measurement: Journal of the International Measurement Confederation
- **Authors:** Shen W.; Wang C.; Zhu C.; Wang D.; Chen Z.

## Abstract summary
As the service life of some buildings increases, some safety hazards may seriously endanger public safety and cause economic losses. Defect detection and management are necessary steps to eliminate potential safety hazards. At present, the inspection of building exterior walls mostly relies on manual inspection, which is highly subjective, risky and has low inspection accuracy. To this end, this study developed an algorithm based on the infrared and point cloud data fusion model of the Point Cloud Reconstruction Network (PCRNet) to increase the depth information of the model and improve its understanding of complex scenes. For the anomaly detection of regular and irregular geometric envelope structures, an automatic anomaly detection algorithm model of geometric envelope structures based on convolutional neural network (CNN) is proposed. By comparing the extracted temperature information…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** Reverse DT envelope anomaly mapping; safety hazards


## Step-3 Deep-Read Coding (Prompt B)
| P DT-subject | Q DfS/DfQ | R codable | U Tier | V Design | W Constr | X Oper | Z DfX | AA Self-improve | AB Methodology | AC Modality | AD Validation | AE QA(0-5) | AF Cluster |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 1 - Digital Model (static, no live data) | 0 | 0 | 1 | Design for Safety (DfS) | None | Perception / Computer Vision | Multi (two or more data types) | Single case study | 4 | Perception / Computer Vision |

| AC1 fusion depth | AC2 fusion evidence | AC3 confidence |
|---|---|---|
| Fused | PCRNet fuses infrared imagery with point-cloud depth information, and a CNN detects anomalies on the fused representation, achieving 92% accuracy and 95.1% F1. | High |

**Key evidence (AG):** Reverse digital twin mapping of building envelope anomalies based on UAV infrared point clouds (Huaqiao U): PCRNet fuses infrared + point cloud data; CNN-based anomaly detection for regular/irregular geometric envelope structures; compares extracted temperature info with labeled abnormal dataset; 299 experimental data points, 92% accuracy, 96.3% precision, 94% recall, 95.1% F1-score, 5.21s detection speed. Static DT mapping — no live data link, no actuation, no learning loop.

*Full-text source: 04c-port*

**AH — strength & gap filled:** Proposes reverse digital twin mapping of building envelope anomalies from UAV infrared point clouds: a PCRNet-based fusion model adds depth information for irregular geometries and a CNN detector classifies thermal anomalies, achieving 92% average accuracy, 96.3% precision, 94% recall and a 95.1% F1 score across 299 data points at 5.21 seconds per item, with anomalies registered into a digital twin model through Mask R-CNN markers for object-oriented management.

**AI — deficiencies & future work:** The dataset covers a single building case, processing still requires manual intervention rather than an end-to-end automated loop, and detection is limited to thermal defects such as thermal bridges and insulation damage, with weak recognition of fine cracks, weathering or mold; field findings also included false alarms from air-conditioner units. Future research targets multi-climate benchmark datasets, multimodal fusion, cloud plus 5G automation and large language model maintenance agents.
