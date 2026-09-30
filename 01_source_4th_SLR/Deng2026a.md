# Deng, R et al. (2026) — Safety risk perception of high-rise building construction process based on digital twin technology

- **ID:** R071 | **Source:** Scopus | **DOI:** 10.1504/IJCIS.2026.155961
- **Journal:** International Journal of Critical Infrastructures
- **Authors:** Deng R.; Zhou L.

## Abstract summary
A safety risk perception method of high-rise building construction process based on digital twin technology is proposed to address the problems of low recall rate, low perception accuracy, and long perception time in traditional risk perception. Firstly, the improved grey relational analysis method is used to screen the factors affecting construction safety. Secondly, the dimension of the influencing factor data is reduced through local linear embedding method. Finally, a security risk perception architecture based on digital twin technology is constructed, establishing a bidirectional mapping between physical construction space and virtual information space, defining construction risk index, and introducing coupling influence terms between factors to achieve security risk perception. The experimental results show that the recall rate of the influencing factors of the proposed method ran…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** DT risk perception for high-rise construction safety

## Step-3 Deep-Read Coding (Prompt B)
| P DT-subject | Q DfS/DfQ | R codable | U Tier | V Design | W Constr | X Oper | Z DfX | AA Self-improve | AB Methodology | AC Modality | AD Validation | AE QA(0-5) | AF Cluster |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow (one-way physical to virtual) | 0 | 1 | 0 | Design for Safety (DfS) | None | Statistical / change-point | Multi (two or more data types) | Simulation | 3 | Predictive analytics / decision support |

| AC1 fusion depth | AC2 fusion evidence | AC3 confidence |
|---|---|---|
| Fused | Grey-relational factor screening, LLE-reduced multi-source construction data and coupling influence terms are combined into a single construction risk index that drives hierarchical early warning. | Medium |

**Key evidence (AG):** Safety risk perception method for high-rise construction based on DT (Chongqing Polytechnic, IJCIS 2026): improved grey relational analysis screens safety influence factors; local linear embedding reduces factor-data dimension; DT architecture establishes a bidirectional mapping between physical construction space and virtual information space, defining a construction risk index with coupling influence terms; multi-level early warning thresholds embeddable in the existing site monitoring platform; experiments (incl. immersive-VR scenario data with EEG/eye-tracking plus sensor data) give recall 96.57-99.06%, accuracy 96.76-97.89%, perception time 0.62-0.87 s. One-way monitoring->risk perception->early warning; no actuation and no learning loop.

*Full-text source: Endnote*

**AH — strength & gap filled:** Fills the recall/accuracy/latency gaps of previous safety-perception methods (dual-attention, BIM+GIS, multi-class AdaBoost): grey-relational screening plus LLE plus a coupling-risk DT index reaches 96.57-99.06% recall, 96.76-97.89% accuracy and 0.62-0.87 s perception time.

**AI — deficiencies & future work:** Experiments rely on simulated/VR scenario data and multi-source construction data rather than a full live high-rise deployment; grey-relational factor screening depends on expert weighting, and the mapping to an existing site monitoring platform is described as feasible but not demonstrated end-to-end on site.
