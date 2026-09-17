# Chacón et al. (2024) — Digital twinning of building construction processes. Case study: A reinforced concrete cast-in structure

- **ID:** 3936 | **Source:** Web of Science | **DOI:** 10.1016/j.jobe.2024.108522
- **Journal:** JOURNAL OF BUILDING ENGINEERING
- **Authors:** Chacón, R.; Posada, H.; Ramonell, C.; Jungmann, M.; Hartmann, T.; Khan, R.; Tomar, R.

## Abstract summary
This paper summarizes the findings obtained during the development of information pipelines between a construction site and its corresponding digital twin. The case study is the construction of an office building in which independent information pipelines can track different aspects of the construction process and the aggregate result can assist managers in decision making in the form of a vaster entity: its digital twin. The digital twin prototype is designed as a recipient of information that mirror its physical building and its systems. The paper contributes with a real case in which these pipelines enable continuous monitoring and analysis of various basic parameters during construction. With a varied array of sensors installed, data was collected, organized and transmitted through a knowledge graph-based system to the digital twin dashboard. A dashboard is able to allocate many sour…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** Real DT prototype on office-building site; health & safety potential

## Step-3 Deep-Read Coding (Prompt B) — full text verified via Endnote library (front-matter DOI/title match, coverage re-scan 2026-08-12)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow | 0 | 1 | 0 | Both | None | Other / Mixed | Multi (two or more data types) | Single case study | 4 | BIM-to-Digital-Twin architecture |

**Key evidence (AG):** ASHVIN H2020 DT case study (RC office building, Barcelona): six independent information pipelines (IMU/temp/load sensors, TLS point clouds, equipment tracking) → knowledge-graph system → Unity dashboard with project-specific KPIs (construction safety, quality control, productivity); ML activity recognition (Naïve Bayes/DT/kNN/SVM on equipment sensors); data flows one-way physical→virtual for decision support; conclusions state it "has not permitted to act" on the site — no actuation, no learning loop.

**Strength & gap filled (AH):** Provides a real ASHVIN H2020 pilot of digital twinning during construction of an RC office building in Barcelona: six independent information pipelines (crane hook IMU/GPS tracking with Random Forest activity recognition at 93.27% accuracy, slab post-tensioning strains, laser-scan deflection checks, concrete maturity temperatures, formwork vibration accelerations, mobile-app progress monitoring) feeding a knowledge-graph-based Unity dashboard.

**Deficiencies & future work (AI):** One-way digital shadow: the dashboard informs managers but does not control site operations, technology readiness did not permit acting weekly on extracted insights, and feedback came only after development. Bottlenecks include logistics, privacy, need for specialized crews, sensor fragility, and manual progress updates; automating data collection and treatment is future work.

**Fusion depth (AC1):** Co-present

**Fusion evidence (AC2):**
- **Data streams:** crane-hook IMU/GPS tracking with Random Forest activity recognition (93.27%), slab post-tensioning strains, TLS deflection scans, concrete maturity temperatures, formwork vibration accelerations, mobile-app progress updates.
- **Integration mechanism:** none across pipelines - data converge on a knowledge-graph-based Unity dashboard with project-specific KPIs, but each pipeline is processed independently (ML recognition runs only on equipment sensors).
- **Why this code:** the paper itself calls them six independent information pipelines, which is the spec example signal for Co-present; shared display without registration is not integration (rule 4).

**Confidence (AC3):** High - the independence of the pipelines is stated verbatim in the full text.