# Kim et al. (2023) — Constructing a digital twin for estimating the response and load of a piping system subjected to seismic and arbitrary loads

- **ID:** 3916 | **Source:** Web of Science | **DOI:** 10.12989/sss.2023.31.3.275
- **Journal:** SMART STRUCTURES AND SYSTEMS
- **Authors:** Kim, D.; Kim, G.; Kwag, S.; Eem, S.

## Abstract summary
In recent years, technological developments have rapidly increased the number of complex structures and equipment in the industrial. Accordingly, the prognostics and health monitoring (PHM) technology has become significant. The safety assessment of industrial sites requires data obtained by installing a number of sensors in the structure. Therefore, digital twin technology, which forms the core of the Fourth Industrial Revolution, is attracting attention in the safety field. The research on digital twin technology of structures subjected to seismic loads has been conducted recently. Hence, this study proposes a digital twin system that estimates the responses and arbitrary load in real time by utilizing the minimum sensor to a pipe that receives a seismic and arbitrary load. To construct the digital twin system, a finite-element model was created considering the dynamic characteristics …

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** DT estimating piping response/load under seismic; real-time ROM

## Step-3 Deep-Read Coding (Prompt B) — full text verified via Endnote library (front-matter DOI match)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow | 0 | 0 | 1 | Design for Safety (DfS) | Mentioned only | Finite Element Method / physics-based | Single (one data type) | Simulation | 4 | Predictive analytics / decision support |

**Key evidence (AG):** Real-time DT of a piping system (MECOS-benchmark pipe on shaking table) for PHM: FE model updated via random-vibration FRF matching (Nelder-Mead stiffness/damping calibration), then Craig-Bampton ROM reduces 7,428 to 62 DOFs (~1%, ~450x faster) for Newmark-β real-time estimation of unmeasured-point responses and seismic+arbitrary loads; validated vs FE model/sensors (RMSE 0.0103/0.0266). Model updating is a one-time calibration step during DT construction, not an ongoing self-improvement loop; one-way sensing→estimation, no actuation.
