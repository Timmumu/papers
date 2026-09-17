# Hekmatnejad et al. (2025) — Toward intelligent tunnel construction: The universal discontinuity index for rapid probabilistic prediction of progressive batch rock-block failure—A theoretical, numerical, and experimental validation framework

- **ID:** 3813 | **Source:** Scopus | **DOI:** 10.1016/j.tust.2025.107017
- **Journal:** Tunnelling and Underground Space Technology
- **Authors:** Hekmatnejad, A.; Bajolvand, M.; Pan, P.; Emery, X.; Pena, A.; Prado, J.; Taheri, A.

## Abstract summary
The safe, cost-effective advance of deep tunnels increasingly hinges on real-time forecasts of structurally controlled rock-block failure—capabilities that lie beyond classic Key-Block Theory (KBT) and remain computationally prohibitive for full-physics numerical models. We introduce the Universal Discontinuity Index (UDi), a single probabilistic score that fuses four physically grounded components—physical damage, effective‐stress intensity, active-fracture ratio, and kinematic feasibility—into a scalable indicator of block instability. The index embodies a complete-system view: it treats the fracture network, local stress field, and block release kinematics as an integrated, dynamically updating subsystem within a Digital-Twin (DT) workflow. Three levels of validation are presented. (i) Theoretical equivalence: UDi's kinematic term reproduces Warburton's vector criteria while providing…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** UDi probabilistic rock-block failure prediction in DT workflow; tunnel safety

## Step-3 Deep-Read Coding (Prompt B)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow (one-way physical to virtual) | 0 | 1 | 0 | Design for Safety (DfS) | None | Statistical / change-point | Multi (two or more data types) | Cross-project (multiple real projects) | 4 | Predictive analytics / decision support |

**Key evidence (AG):** Universal Discontinuity Index (UDi) for probabilistic rock-block failure prediction in tunnels (Pontificia Universidad Catolica de Chile): single probabilistic score fusing physical damage, effective-stress intensity, active-fracture ratio, and kinematic feasibility; embedded in Poisson-regression early-warning model converting index updates to expected block counts; validated via DFN-KBT engine (5300 realizations) at El Teniente mine (R2 = 0.93); millisecond updates for real-time DT workflow. One-way monitoring→prediction→early warning; no actuation and no learning loop (UDi is a static probabilistic index, not self-improving).


**Strength & gap filled (AH):** Bridges the gap between deterministic block theory and hours-long high-fidelity simulations with the Universal Discontinuity Index, a probabilistic score fusing physical damage, effective stress intensity, active fracture ratio and kinematic feasibility; it reproduced progressive batch failure in milliseconds versus BPDEM and FDEM, and on 52 El Teniente faces with 5300 DFN-KBT realizations predicted unstable block counts at R2 of 0.93 and 95 percent accuracy, feeding a Poisson early-warning model.

**Deficiencies & future work (AI):** The closed-loop digital twin workflow remains a design proposal rather than a deployed system, and the field validation used simplified inputs: uniform friction angle of 32 degrees, tensile strength of 17 MPa, Kirsch-based stress and a kinematic-only weighting; the authors plan spatio-temporal point process and Bayesian hierarchical models for clustered failures.
**Fusion depth (AC1):** Fused

**Fusion evidence (AC2):**
- **Data streams:** four physical/geometric indicators per tunnel face; DFN-KBT realisations (5300) at El Teniente.
- **Integration mechanism:** UDi combines the four indicators into a single score that the Poisson-regression model converts into expected block counts (R2 0.93, 95% accuracy), with millisecond updates for the DT workflow.
- **Why this code:** an explicit fusion index whose output depends on four data components simultaneously, so Fused.

**Confidence (AC3):** High - the UDi fusion formula is the paper core contribution.
(full-text source: Endnote)
