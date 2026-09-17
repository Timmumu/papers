# Trofymchuk, O.M et al. (2025) — Hybrid Numerical Method for the Evaluation of the Seismic Protection of Buildings Based on Digital Twins

- **ID:** R325 | **Source:** Scopus | **DOI:** 10.1007/s10958-025-07858-2
- **Journal:** Journal of Mathematical Sciences (United States)
- **Authors:** Trofymchuk O.M.; Kaliukh I.I.; Berchun Y.O.; Marienkov M.G.; Khymenko B.O.; Tytarenko V.A.; Vapnichna V.V.

## Abstract summary
We present the results of numerical and experimental investigations of vibration of a residential building and its seismic protection by means of rubber isolators made in Ukraine from natural rubber. The numerical studies of vertical oscillations of the building with rubber supports on the level of reinforced-concrete grid were performed with the help of dynamic digital twins developed on the basis of the finite-element method. The numerical studies of the vibrations of digital twins were carried out according to the records of soil vibration accelerations obtained under the effects of railway trains, as well as for the effects determined according to the accelerograms of earthquakes. The numerical analysis of buildings on seismic supports with regard for the seismic loads was performed with evaluation of the factors of safety against overturning of the residential building. We show that…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** FEM dynamic twins for building seismic protection


## Step-3 Deep-Read Coding (Prompt B)
| P DT-subject | Q DfS/DfQ | R codable | U Tier | V Design | W Constr | X Oper | Z DfX | AA Self-improve | AB Methodology | AC Modality | AD Validation | AE QA(0-5) | AF Cluster |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow (one-way physical to virtual) | 1 | 0 | 1 | Design for Safety (DfS) | None | Finite Element Method / physics-based | Multi (two or more data types) | Single case study | 4 | Design for Safety |

| AC1 fusion depth | AC2 fusion evidence | AC3 confidence |
|---|---|---|
| Fused | Recorded railway/earthquake accelerations and IoT vibration records drive the FEM twin in one dynamic analysis workflow. | High |

**Key evidence (AG):** Hybrid numerical method for evaluating seismic protection of buildings using dynamic FEM digital twins (NAS Ukraine et al., J Math Sci 2025): digital twins of the Pid Dubom residential complex (Lviv, Vrancea earthquake zone) driven by recorded soil-vibration accelerations from railway traffic and earthquake accelerograms; IoT sensor networks (cloud, online mode) feed the models; rubber isolators with nonlinear stiffness justified against Eurocode 8/DBN; overturning safety factors evaluated. One-way monitoring/records->FEM twin->protection design and safety assessment; no actuation, no learning loop.

*Full-text source: Endnote*

**AH — strength & gap filled:** Fills the seismic-plus-railway-vibration protection gap: dynamic FEM digital twins driven by recorded railway/earthquake accelerations and IoT monitoring justify nonlinear rubber isolators for the Pid Dubom complex per Eurocode 8/DBN, including overturning safety factors.

**AI — deficiencies & future work:** The DT modelling depends on recorded accelerations and manual non-destructive survey campaigns rather than a permanently live loop; friction effects give only a factor-1.5 estimate; robustness across other soil/building configurations is not quantified.
