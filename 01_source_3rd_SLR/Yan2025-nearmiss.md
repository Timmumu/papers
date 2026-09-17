# Yan et al. (2025) — Real-Time Digital Twin-Driven 3D Near-Miss Detection System at Construction Sites

- **ID:** 3905 | **Source:** Web of Science | **DOI:** 10.1061/JCEMD4.COENG-15583
- **Journal:** JOURNAL OF CONSTRUCTION ENGINEERING AND MANAGEMENT
- **Authors:** Yan, H. F.; Liu, C. Y.; Yang, X. C.; Feng, K. L.

## Abstract summary
To enhance on-site safety management, detecting near-misses in a timely and accurate manner is crucial. However, traditional monitoring methods that rely on inspectors are time-consuming, labor-intensive, and limited in their ability to detect three-dimensional (3D) incidents. Digital twin technology presents a promising solution by integrating real-time monitoring, simulation and interactivity capabilities in three dimensional virtual environments. Therefore, we propose a real-time digital twin-driven near-miss detection system to facilitate safety management at construction sites. Using advanced stereovision techniques, the system reproduces the construction site as a digital twin model, enabling the real-time 3D monitoring of near-miss events. Additionally, the system incorporates an early warning mechanism to alert workers and managers of potential safety hazards. To demonstrate the …

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** Real-time DT 3D near-miss detection at construction sites

## Step-3 Deep-Read Coding (Prompt B) — full text verified via Endnote library (front-matter DOI match)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow | 0 | 1 | 0 | Design for Safety (DfS) | None | Computer Vision / CNN / object-detection | Multi (two or more data types) | Single case study | 4 | Perception / Computer Vision |

**Key evidence (AG):** Real-time digital-twin-driven 3D near-miss detection at construction sites: drones + binocular cameras feed YOLOv5 detection + Deep SORT tracking + SGM stereo-matching into an Unreal Engine 5.1 DT (BIM static elements + dynamic worker/material/machinery models); collision of user-set protection envelopes (worker cylinder r=1.5 m) triggers 3D near-miss visualisation and an early-warning alert (Heinrich-law threshold 300). Pilot at Foshan steel-beam hoisting site: 1,300 near-misses/month, 1,181 detected (precision 93.8%, recall 96.6%; robust >90%/>95% under exposure tests). One-way monitoring→human warning, no actuation and no learning loop.

**Strength & gap filled (AH):** Fills the gap of three-dimensional near-miss detection at construction sites: drone imagery builds a BIM-based static scene and binocular cameras feed YOLOv5 target recognition, DeepSORT tracking, and SGM stereo matching into an Unreal Engine digital twin with protective envelopes and early warnings, detecting 1181 of 1300 near-misses (93.80% precision, 96.64% recall) in a one-month Foshan steel-hoisting pilot.

**Deficiencies & future work (AI):** Overlapping personnel and machinery cause incomplete information capture, extreme lighting degrades stability (Type S3 precision fell to 73.97% under overexposure), and the vision system works only within about 20 meters, excluding high-rise and large buildings; future work adds multiple perspectives against occlusion and tests update frequencies.

**Fusion depth (AC1):** Fused

**Fusion evidence (AC2):**
- **Data streams:** binocular-camera detections (YOLOv5 + DeepSORT + SGM stereo) + BIM-anchored 3D scene (one-month Foshan steel-hoisting pilot).
- **Integration mechanism:** trajectories and postures are mapped into the twin with protective envelopes, and the transformer predicts future sequences whose collision checks detect near-misses (93.80% precision, 96.64% recall, 1181 of 1300).
- **Why this code:** near-miss output depends on live perception and scene geometry simultaneously, so Fused.

**Confidence (AC3):** High - the perception-to-twin-to-prediction chain is explicit.