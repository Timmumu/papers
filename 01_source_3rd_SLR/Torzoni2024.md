# Torzoni et al. (2024) — A digital twin framework for civil engineering structures

- **ID:** 3878 | **Source:** Web of Science | **DOI:** 10.1016/j.cma.2023.116584
- **Journal:** COMPUTER METHODS IN APPLIED MECHANICS AND ENGINEERING
- **Authors:** Torzoni, M.; Tezzele, M.; Mariani, S.; Manzoni, A.; Willcox, K. E.

## Abstract summary
The digital twin concept represents an appealing opportunity to advance condition-based and predictive maintenance paradigms for civil engineering systems, thus allowing reduced lifecycle costs, increased system safety, and increased system availability. This work proposes a predictive digital twin approach to the health monitoring, maintenance, and management planning of civil engineering structures. The asset-twin coupled dynamical system is encoded employing a probabilistic graphical model, which allows all relevant sources of uncertainty to be taken into account. In particular, the time-repeating observations-to-decisions flow is modeled using a dynamic Bayesian network. Real-time structural health diagnostics are provided by assimilating sensed data with deep learning models. The digital twin state is continually updated in a sequential Bayesian inference fashion. This is then explo…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** Predictive DT for civil structures; DBN updating + maintenance planning

## Step-3 Deep-Read Coding (Prompt B)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 3 - Digital Twin (bidirectional, two-way) | 0 | 0 | 1 | Design for Safety (DfS) | Implemented | Bayesian / probabilistic | Multi (two or more data types) | Simulation | 4 | Predictive analytics / decision support |

**Key evidence (AG):** Predictive digital twin framework for civil engineering structures (Politecnico di Milano/UT Austin): dynamic Bayesian network (dynamic decision network) encodes asset-twin coupled dynamical system; deep learning (convolutional layers) assimilates vibration data for structural health diagnostics; sequential Bayesian inference continually updates digital state; offline learning phase with reduced-order models trains DL models and learns control policy; health-dependent control policy for maintenance planning. Bidirectional — physical→digital assimilation + digital→physical control → Tier 3; implemented Bayesian inference + offline learning, no convergence criterion.


**Strength & gap filled (AH):** Encodes the asset-twin coupled system as a dynamic decision network so data assimilation, uncertainty tracking, prediction, and maintenance planning share one framework: convolution-based deep learning classifies damage location and magnitude from vibration recordings (93.61 percent beam, 91.39 percent bridge accuracy), sequential Bayesian updates track health, and a health-dependent control policy recommends do-nothing, repair, or operation-restriction actions on synthetic cantilever-beam and Hornefors railway bridge cases.

**Deficiencies & future work (AI):** Validated only on noise-corrupted synthetic data from reduced-order physics models, with no real sensing or field deployment; neural networks, transition dynamics, and the control policy are all learned offline, and the fixed transition models made bridge deterioration predictions too optimistic. Future work targets online learning of transition dynamics from past data and reinforcement-learning planning over a finite asset-life horizon.
**Fusion depth (AC1):** Fused

**Fusion evidence (AC2):**
- **Data streams:** vibration recordings (synthetic cantilever beam, Hornefors bridge) + reduced-order physics-model dynamics.
- **Integration mechanism:** the DDN encodes the asset-twin coupled system: DL classifies damage (93.61%/91.39% accuracy) and sequential Bayesian updating tracks health and recommends do-nothing/repair/restrict actions.
- **Why this code:** the control-policy output depends on the data-driven and model-driven components simultaneously, so Fused; synthetic data only (Medium).

**Confidence (AC3):** Medium - the DDN coupling is explicit, but validation uses synthetic data.
(full-text source: Endnote)
