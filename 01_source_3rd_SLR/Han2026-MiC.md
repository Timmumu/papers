# Han et al. (2026) — Digital twin-driven pose estimation and trajectory prediction for modular integrated construction on-site stacking via spatio-temporal feature fusion modeling

- **ID:** 3765 | **Source:** Scopus | **DOI:** 10.1016/j.compind.2026.104501
- **Journal:** Computers in Industry
- **Authors:** Han, Y.; Sun, K.; Zhao, Z.; Yu, Y.; Huang, G. Q.

## Abstract summary
High stacking precision is essential to prevent structural collisions, reduce safety accidents, and enhance project efficiency in modular integrated construction. However, current stacking precision is constrained by delayed hoisting control, limited perception, and fragmented information sharing. Therefore, this paper proposes a digital twin-driven pose estimation and trajectory prediction system via spatio-temporal feature fusion modeling, leveraging real-time information from high-fidelity digital twins. First, physical entities are transformed into smart stacking objects that combine static inherent properties with real-time dynamic activities captured by Ultra-Wideband sensors and Inertial Measurement Units. Then, a digital twin of stacking operations is used to interact with their physical counterparts in real time, enabling seamless mapping and visualization of the stacking proces…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** DT-driven pose/trajectory prediction for MiC stacking; collision prevention

## Step-3 Deep-Read Coding (Prompt B)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow (one-way physical to virtual) | 0 | 1 | 0 | Design for Safety (DfS) | None | Transformer / Large Language Model (LLM) | Multi (two or more data types) | Single case study | 4 | Predictive analytics / decision support |

**Key evidence (AG):** Digital twin-driven pose estimation and trajectory prediction for modular integrated construction (MiC) on-site stacking (PolyU): UWB sensors + IMUs capture real-time dynamic activities of smart stacking objects; DT of stacking operations interacts with physical counterparts in real time for seamless mapping/visualization; PosTraFormer network (spatio-temporal feature fusion of trajectory point relations) for 6-D module pose estimation and trajectory prediction to provide stacking guidance; comparative experiments + case studies show higher trajectory prediction performance. One-way monitoring/prediction→guidance for crane operators; no actuation and no learning loop (PosTraFormer is offline-trained).


**Strength & gap filled (AH):** Targets delayed hoisting control and fragmented information in modular integrated construction stacking: a DT platform (DTPTS) fusing UWB and IMU sensing with a PosTraFormer spatio-temporal network whose multi-layer GCNs model trajectory point relations, achieving the lowest FDE and ADE across four lifting scenarios (0.0417 and 0.0476 in lifting) and on a real PolyU site case after fine-tuning (0.0277 and 0.0319), with protective collision shields in the twin.

**Deficiencies & future work (AI):** PosTraFormer has the largest parameter count (5661.7K) and lowest speed (288.8 frames per second) among tested models, and training relies on simulated trajectories because stacking datasets are scarce, with only 70 real pose sets for fine-tuning; no explicit future work is stated, so data collection and lightweight deployment remain unaddressed.
**Fusion depth (AC1):** Fused

**Fusion evidence (AC2):**
- **Data streams:** UWB sensors + IMUs on smart stacking objects; simulated trajectories plus 70 real pose sets for fine-tuning.
- **Integration mechanism:** PosTraFormer performs spatio-temporal feature fusion of the two streams and predicts 6-D module pose and trajectories (lowest FDE/ADE across four lifting scenarios), shown in the DT platform with collision shields.
- **Why this code:** an explicit fusion network whose output depends on both sensing types, so Fused.

**Confidence (AC3):** High - the fusion architecture is explicit.
(full-text source: Endnote)
