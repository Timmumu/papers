# Zou et al. (2024) — Digital Twin Construction Method for Monitoring Operation Status of Building Machine Jacking Operation

- **ID:** 3951 | **Source:** Web of Science | **DOI:** 10.3390/buildings14082318
- **Journal:** BUILDINGS
- **Authors:** Zou, Y. Q.; Wang, Z. L.; Pan, H.; Liao, F.; Tu, W. L.; Sun, Z. C.

## Abstract summary
In the construction of super high-rise buildings, building machines (BMs) are increasingly replacing traditional climbing frames. Building machine jacking operation (BMJO) is a high-difficulty and high-risk stage in the construction of the top mold system. To guarantee the operational safety of the BMJO and to enhance its intelligent control level, a digital twin (DT)-based monitoring method for the operation status of the BMJO is proposed. Firstly, a DT framework for monitoring the operation status of the BMJO is presented, taking into account the operational characteristics of the BM and the requirements of real-time monitoring. The functions of each part are then elaborated in detail. Secondly, the virtual twin model is created using Blender's geometric node group function; artificial neural network technology is used to enable online prediction of the structural performance of the BM…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** DT monitoring of building machine jacking operation; ANN prediction

## Step-3 Deep-Read Coding (Prompt B)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow (one-way physical to virtual) | 0 | 1 | 0 | Design for Safety (DfS) | None | Other / Mixed | Multi (two or more data types) | Single case study | 4 | Design for Safety |

**Key evidence (AG):** DT construction method for monitoring operation status of building machine jacking operation (BMJO) (Hubei U Tech): DT framework with layered architecture; Blender geometric node group creates parametric virtual model; ANN enables online prediction of structural performance; motion model realizes real-time state mapping; real BM project validates system (quantitative monitoring, evaluation, early warning, real-time prediction of operational posture; high accuracy, fast analysis). One-way monitoring->prediction->early warning; no actuation, no learning loop.


**Strength & gap filled (AH):** Proposes a five-layer digital twin framework for building machine jacking operations, creating parametric twin models in Blender geometric node groups (98.48 percent auto-generation accuracy) and an RBF neural network for online stress and deformation prediction with relative errors within 0.1 percent and 6 percent respectively, verified on a 186.3 m Wuhan building where five major accidents were avoided and jacking efficiency rose 19.75 percent.

**Deficiencies & future work (AI):** Predicted structural performance and motion are only displayed on the platform without autonomous decision-making, and prediction correctness depends on sensor data accuracy. Future research will adopt deep learning for data correction, reinforcement learning for autonomous control, and cloud and blockchain strategies for data storage, cleaning, and security.
**Fusion depth (AC1):** Fused

**Fusion evidence (AC2):**
- **Data streams:** multi-sensor jacking monitoring on a 186.3 m Wuhan building + parametric Blender twin (98.48% auto-generation accuracy).
- **Integration mechanism:** the RBF network consumes the monitoring channels to predict stress (within 0.1%) and deformation (within 6%) online, and the motion model maps states in real time; five major accidents were avoided.
- **Why this code:** the prediction output depends on multiple monitoring channels simultaneously, so Fused.

**Confidence (AC3):** Medium - the multi-input ANN is explicit; no autonomous decision-making exists.
(full-text source: Endnote)
