# Yan et al. (2026) — Digital twin-enabled 3D near-misses prediction method based on trajectories and postures for proactive construction safety management

- **ID:** 3909 | **Source:** Web of Science | **DOI:** 10.1108/ECAM-05-2025-0732
- **Journal:** ENGINEERING CONSTRUCTION AND ARCHITECTURAL MANAGEMENT
- **Authors:** Yan, H. F.; Liu, C. Y.; Yang, X. C.; Li, X. L.; Li, J. Q.

## Abstract summary
Purpose This paper aims to develop a proactive construction safety management framework capable of predicting near-miss incidents by leveraging Digital Twin (DT) technology. The Digital Twin (DT) framework focuses on integrating environmental and human-related risk factors - particularly the trajectories and behaviors of workers - before accidents occur.Design/methodology/approach The paper proposes a computer vision-based digital twin framework that integrates real-time data on workers' movements, postures, and interactions to construct a dynamic 3D model of the construction site. Deep learning algorithms are employed to predict human trajectories and behaviors, while collision detection techniques are used to identify potential near-miss scenarios. Field validation was conducted in three high-risk zones: forklift paths, floor openings, and material lifting areas.Findings The proposed f…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** DT 3D near-miss prediction from trajectories/postures; proactive safety

## Step-3 Deep-Read Coding (Prompt B) — full text verified via Endnote library (front-matter DOI/title match, coverage re-scan 2026-08-12)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow | 0 | 1 | 0 | Design for Safety (DfS) | None | Transformer / Large Language Model (LLM) | Multi (two or more data types) | Single case study | 4 | Predictive analytics / decision support |

**Key evidence (AG):** Computer-vision-based digital twin framework for proactive near-miss prediction (Harbin IT): integrates real-time worker trajectories, postures and interactions into a dynamic 3D construction-site model; non-autoregressive transformer predicts future movement sequences (human motion model trained on Human3.6M dataset, inverse kinematics for joint angles) + collision detection identifies potential near-misses with early warnings; field-validated in three high-risk zones (forklift paths, floor openings, material lifting). One-way perception to prediction to early warning for safety managers; no actuation and no self-improvement loop (model is offline-trained).

**Strength & gap filled (AH):** Extends near-miss management from 2D detection to in-process 3D prediction: YOLOv5, SGBM, DeepSORT and MediaPipe keypoints feed a non-autoregressive transformer that forecasts worker trajectories (ADE 0.134) and postures (ADE 0.501), reconstructed by an LBFGS inverse-kinematics solver in Unreal Engine, predicting near-misses with 93.32% precision and 96.08% recall across forklift, floor-opening, and material-lifting zones.

**Deficiencies & future work (AI):** The motion prediction model is trained on the Human3.6M laboratory dataset, creating a generalization gap to real construction postures; occlusions, lighting variability, and camera positioning limit reliability, and validation covered only three relatively simple high-risk zones. Future work adds more sensor types, lightweight edge-distributed architectures, domain-adaptive learning, and broader site validation.

**Fusion depth (AC1):** Fused

**Fusion evidence (AC2):**
- **Data streams:** camera-based trajectories and postures + BIM-anchored Unreal scene (forklift, floor-opening, material-lifting zones).
- **Integration mechanism:** the transformer forecasts trajectories (ADE 0.134) and postures (ADE 0.501), an LBFGS inverse-kinematics solver reconstructs them in the twin, and collision checks predict near-misses (93.32% precision, 96.08% recall).
- **Why this code:** prediction output depends on perception data and scene geometry simultaneously, so Fused.

**Confidence (AC3):** High - the pipeline is explicit.