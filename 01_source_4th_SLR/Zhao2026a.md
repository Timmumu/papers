# Zhao, S et al. (2026) — Digital twin-enabled simulation system for NATM tunnel construction process considering multi-source uncertainty

- **ID:** R154 | **Source:** Scopus | **DOI:** 10.1016/j.undsp.2025.05.012
- **Journal:** Underground Space (new)
- **Authors:** Zhao S.; Shen Y.; Yin M.; Li T.; Wu W.; Li X.

## Abstract summary
During the construction of new Austrian tunnelling method (NATM) tunnels, inherent multi-source uncertainties may lead to substantial economic losses and project delays. To address this issue, a simulation system enabled by digital twin (DT) technology was developed. Guided by the concept of five-dimensional DT, a four-layer system architecture was established, including perception, transmission, modelling, and alternation layers. An integrated discrete event simulation (DES) model was then developed as the core of the system using structured system analysis. The model accounts for both geological and construction-related uncertainties, including routine delays and accident recovery durations. Geological uncertainties are represented through a stochastic geological modelling approach based on the Markov random field (MRF). Construction-related uncertainties are addressed using a tunnel v…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** NATM tunnel DT process simulation; uncertainty/risk


## Step-3 Deep-Read Coding (Prompt B)
| P DT-subject | Q DfS/DfQ | R codable | U Tier | V Design | W Constr | X Oper | Z DfX | AA Self-improve | AB Methodology | AC Modality | AD Validation | AE QA(0-5) | AF Cluster |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow (one-way physical to virtual) | 0 | 1 | 0 | Design for Safety (DfS) | None | Other / Mixed | Multi (two or more data types) | Single case study | 4 | Predictive analytics / decision support |

| AC1 fusion depth | AC2 fusion evidence | AC3 confidence |
|---|---|---|
| Fused | Stochastic geology (Markov random field), AHP-DEMATEL vulnerability evaluation and delay probability densities are combined inside one discrete-event simulation model whose schedule/safety outputs depend on all inputs. | Medium |

**Key evidence (AG):** DT-enabled simulation system for NATM tunnel construction process considering multi-source uncertainty (Tongji U): five-dimensional DT concept with four-layer architecture (perception, transmission, modelling, alternation); integrated discrete event simulation (DES) model as core; Markov random field (MRF) for stochastic geological modelling; AHP-DEMATEL tunnel vulnerability evaluation + delay probability density functions for construction uncertainties; validated on a real-world tunnel project for schedule estimation, site communication, safe/efficient completion. One-way monitoring->simulation->schedule/safety decision; no actuation, no learning loop.

*Full-text source: 04c-port*

**AH — strength & gap filled:** Fills the gap between theoretical process simulation and on-site tunnel management: a four-layer digital twin couples an AnyLogic discrete event simulation with Markov random field stochastic geology and AHP-DEMATEL vulnerability evaluation, and 2500 Monte Carlo runs on a real NATM tunnel estimate a 78.4 percent probability of finishing within the 1794-day plan, with the average estimated schedule differing from actual by only 9 days (0.50 percent).

**AI — deficiencies & future work:** Geological modelling uses a coarse grid due to sparse data, step durations are recorded manually giving static probability distributions, sensing relies on subjective manual measurement, and the twin exerts only indirect control without real-time feedback to machinery. Future work covers tunnel seismic prediction and GPR data, 24-hour cameras for dynamic parameter updates, IoT sensor networks and unmanned construction.
