# Zhao et al. (2026) — Digital twin-enabled simulation system for NATM tunnel construction process considering multi-source uncertainty

- **ID:** 3972 | **Source:** Web of Science | **DOI:** 10.1016/j.undsp.2025.05.012
- **Journal:** UNDERGROUND SPACE
- **Authors:** Zhao, S. C.; Shen, Y.; Yin, M.; Li, T.; Wu, W.; Li, X. J.

## Abstract summary
During the construction of new Austrian tunnelling method (NATM) tunnels, inherent multi-source uncertainties may lead to substantial economic losses and project delays. To address this issue, a simulation system enabled by digital twin (DT) technology was developed. Guided by the concept of five-dimensional DT, a four-layer system architecture was established, including perception, transmission, modelling, and alternation layers. An integrated discrete event simulation (DES) model was then developed as the core of the system using structured system analysis. The model accounts for both geological and construction-related uncertainties, including routine delays and accident recovery durations. Geological uncertainties are represented through a stochastic geological modelling approach based on the Markov random field (MRF). Construction-related uncertainties are addressed using a tunnel v…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** DT simulation for NATM tunnel construction under uncertainty; safety/schedule

## Step-3 Deep-Read Coding (Prompt B)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow (one-way physical to virtual) | 0 | 1 | 0 | Design for Safety (DfS) | None | Other / Mixed | Multi (two or more data types) | Single case study | 4 | Predictive analytics / decision support |

**Key evidence (AG):** DT-enabled simulation system for NATM tunnel construction process considering multi-source uncertainty (Tongji U): five-dimensional DT concept with four-layer architecture (perception, transmission, modelling, alternation); integrated discrete event simulation (DES) model as core; Markov random field (MRF) for stochastic geological modelling; AHP-DEMATEL tunnel vulnerability evaluation + delay probability density functions for construction uncertainties; validated on a real-world tunnel project for schedule estimation, site communication, safe/efficient completion. One-way monitoring->simulation->schedule/safety decision; no actuation, no learning loop.


**Strength & gap filled (AH):** Fills the gap between theoretical process simulation and on-site tunnel management: a four-layer digital twin couples an AnyLogic discrete event simulation with Markov random field stochastic geology and AHP-DEMATEL vulnerability evaluation, and 2500 Monte Carlo runs on a real NATM tunnel estimate a 78.4 percent probability of finishing within the 1794-day plan, with the average estimated schedule differing from actual by only 9 days (0.50 percent).

**Deficiencies & future work (AI):** Geological modelling uses a coarse grid due to sparse data, step durations are recorded manually giving static probability distributions, sensing relies on subjective manual measurement, and the twin exerts only indirect control without real-time feedback to machinery. Future work covers tunnel seismic prediction and GPR data, 24-hour cameras for dynamic parameter updates, IoT sensor networks and unmanned construction.
**Fusion depth (AC1):** Fused

**Fusion evidence (AC2):**
- **Data streams:** manual step-duration records, MRF stochastic geological model, AHP-DEMATEL vulnerability scores (real NATM tunnel).
- **Integration mechanism:** the AnyLogic DES model consumes the geological and vulnerability inputs jointly, and 2500 Monte Carlo runs estimate a 78.4% probability of on-time completion (estimate within 9 days / 0.50% of actual).
- **Why this code:** the simulation output depends on several data sources simultaneously, so Fused.

**Confidence (AC3):** Medium - the joint DES consumption is explicit; sensing inputs are manual.
(full-text source: Endnote)
