# Ponzo et al. (2024) — DInSAR–SBAS satellite monitoring of infrastructures: how temperature affects the “Ponte della Musica” case study

- **ID:** 3536 | **Source:** Scopus | **DOI:** 10.1007/s13349-023-00751-z
- **Journal:** Journal of Civil Structural Health Monitoring
- **Authors:** Ponzo, F. C.; Auletta, G.; Ielpo, P.; Ditommaso, R.

## Abstract summary
Continuous monitoring of the structural health of strategic structures and transport infrastructures plays a crucial role in providing an effective assessment of the safety conditions and in timely planning of the ordinary and extraordinary maintenance programme. Deformation monitoring and dynamic characteristic identification are some commonly used strategies for this purpose. One of the main challenges of recent years in the field of structural health monitoring is the use of data deriving from satellite interferometry, capable of providing information on structural deformations at a local and territorial scale. Despite the solidity and dependability of satellite-based methods for assessing ground deformation over time, when it comes to structural surveillance, there are certain circumstances under which satellites are incapable of accurately assessing displacements. This is particular…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** Calibrated 3D DT of bridge for thermal-deformation SHM interpretation

## Step-3 Deep-Read Coding (Prompt B) — full text verified via Endnote library (front-matter DOI match)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 1 - Digital Model | 0 | 0 | 1 | Design for Safety (DfS) | None | Finite Element Method / physics-based | Multi (two or more data types) | Single case study | 4 | Predictive analytics / decision support |

**Key evidence (AG):** 3D FEM digital twin (SAP2000) of the "Ponte della Musica" arch bridge (Rome) calibrated against experimental ambient-vibration modal parameters (eigenfrequency error ~2%) and used for thermo-mechanical analyses: correlates air-temperature variation with deck vertical displacement (fmax = 0.0009 + 0.004·ΔT; ±5 °C → ±2 cm) to explain why COSMO-SkyMed X-band DInSAR-SBAS loses the central span (max detectable LOS displacement ~0.8 cm < thermal deformation). One-time calibration with field data, then static what-if thermal analysis; no live data link and no learning loop.

**Strength & gap filled (AH):** Explains a satellite monitoring failure on the Ponte della Musica arch bridge in Rome using a 3D FEM digital twin in SAP2000 calibrated against ambient vibration tests (three experimental eigenfrequencies 0.92, 1.01 and 1.33 Hz reproduced within about 2% error); thermo-mechanical analyses show a most probable plus or minus 5 degrees C variation causes about 2 cm of deck displacement, exceeding the X-band line-of-sight measurement limit of roughly 0.8 cm.

**Deficiencies & future work (AI):** The model is linear and ignores solar radiation and nonlinear constraint effects, so real displacements may be underestimated; satellite and weather data are processed offline with no live monitoring link, and findings need generalization to other bridges. The authors suggest integrating L-band radar, GNSS, TInSAR, optical fibre and LiDAR measurements.

**Fusion depth (AC1):** Aligned

**Fusion evidence (AC2):**
- **Data streams:** experimental ambient-vibration eigenfrequencies (0.92/1.01/1.33 Hz) + COSMO-SkyMed X-band DInSAR-SBAS displacements + air-temperature records.
- **Integration mechanism:** vibration calibrates the FEM twin (about 2% error), and the calibrated twin thermo-mechanical analysis (about 2 cm per plus/minus 5 C) explains why the satellite misses the central span; the streams are used serially, not fused.
- **Why this code:** data types share the bridge-model frame but inference runs per stage and per type, so Aligned.

**Confidence (AC3):** Medium - serial use is clear from the text; a joint inference step is not described.