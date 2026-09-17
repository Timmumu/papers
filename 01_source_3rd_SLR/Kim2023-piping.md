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

**Strength & gap filled (AH):** Fills the gap for structures under simultaneous seismic and arbitrary loads: a 3D-printed MECOS benchmark pipe on a shaking table with an actuator, an updated ANSYS finite element model, and a Craig-Bampton reduced order model (62 DOFs, about one percent of the 7,428-DOF model) yield about 450 times faster calculation, enabling real-time estimation of unmeasured responses and loads with RMSE 0.0103 and 0.0266 versus sensors.

**Deficiencies & future work (AI):** Validated only on a small laboratory-scale 3D-printed pipe, with verification against the finite element model rather than in-service plant data; sensor noise, measurement uncertainty, and scale effects are not addressed, and no explicit future work is stated beyond the expectation that continuous development will transfer the system to ports, shipbuilding, power generation, and manufacturing.

**Fusion depth (AC1):** SINGLE

**Fusion evidence (AC2):**
- **Data streams:** FRF/vibration measurements from the MECOS benchmark pipe on a shaking table.
- **Integration mechanism:** none - Nelder-Mead updating calibrates the FE model, and the Craig-Bampton ROM (62 DOFs, about 450x faster) estimates responses; RMSE 0.0103/0.0266 versus sensors.
- **Why this code:** SINGLE (AC=Single).

**Confidence (AC3):** High.