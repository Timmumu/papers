# -*- coding: utf-8 -*-
"""Fusion-depth coding (after AC data modality).

FD  : code      -> Co-present | Aligned | Fused | SINGLE | Unclear
FDEV: evidence  -> one-sentence justification (mechanism from full text)
FDCF: confidence -> High | Medium | Low
Keyed by paper index n. Only full-coded (P=Q=R=Yes) papers.
"""
FD = {}
FDEV = {}
FDCF = {}

# ---- Batch 1 (first 10 full-coded papers) ----
FD[6] = 'Fused'
FDEV[6] = 'Deployed LiDAR+radar+camera fusion validated with RTK-GNSS at lane-level accuracy at a real work zone (joint multi-sensor deployment feeding conflict metrics).'
FDCF[6] = 'Medium'

FD[7] = 'Unclear'
FDEV[7] = 'Perspective paper defining next-gen CPS/DT; the bidirectional-control scenarios are illustrative only and no data-integration mechanism is implemented.'
FDCF[7] = 'High'

FD[13] = 'Unclear'
FDEV[13] = 'Four-layer fire-safety framework validated only through a thematic analysis and an FM-professional questionnaire; the layer integration mechanism is not implemented.'
FDCF[13] = 'High'

FD[14] = 'Aligned'
FDEV[14] = 'Each video segment is timestamped and the custom Grafana plugin cross-references RTSP video streams with time-series sensor data stored in MySQL, giving video and beacon data a shared temporal frame (inference still runs on sensor series only).'
FDCF[14] = 'High'

FD[19] = 'Unclear'
FDEV[19] = 'Standardisation position paper (CEN/TC 442/WG 9); the two illustrative DT cases are management/visualisation platforms and no data-integration mechanism is specified.'
FDCF[19] = 'High'

FD[20] = 'Aligned'
FDEV[20] = 'Smart Twins 4.0 links physical formworks to their virtual BIM counterparts through automatic database integration (RFID UHF tags read on Android, Firebase, Web-based Revit/Dynamo BIM), i.e. a shared object identity between tag data and BIM elements.'
FDCF[20] = 'Medium'

FD[21] = 'Aligned'
FDEV[21] = 'Defect records are anchored to georeferenced 3D meshes in PostGIS via raycasting and frustum-based image retrieval, putting imagery-derived geometry and defect annotations in one spatial reference frame.'
FDCF[21] = 'High'

FD[22] = 'SINGLE'
FDEV[22] = 'Only ambient-vibration time series from wireless accelerometers feed the analytics; FEM-calibrated synthetic damage is model-generated training data, not a second measured data type.'
FDCF[22] = 'High'

FD[23] = 'Aligned'
FDEV[23] = 'The LiDAR point-cloud survey is converted into a BIM that is linked to the 3DEC/SAP2000 FEM models through an explicit BIM-FEM linking process, sharing one building geometry frame while each model analyses separately.'
FDCF[23] = 'Medium'

FD[35] = 'Unclear'
FDEV[35] = 'Conceptual resilience framework for critical infrastructure; no implementation, prototype or case evaluation, so no integration mechanism can be identified.'
FDCF[35] = 'High'

# ---- Detailed note blocks (FDN) for atomic notes ----
FDN = {}

FDN[6] = ('**Fusion depth (AC1):** Fused\n\n**Fusion evidence (AC2):**\n'
    '- **Data streams:** LiDAR, radar and camera data deployed together at a real work zone.\n'
    '- **Integration mechanism:** the multisensor fusion deployment is validated against RTK-GNSS at lane-level accuracy and feeds TTC/PET conflict metrics; the predictive Digital Shadow + Digital Sibling framework with C-V2X warnings is proposed but not implemented.\n'
    '- **Why this code:** jointly deployed and jointly validated multi-sensor streams make the safety output depend on all three types simultaneously, so Fused.\n\n'
    '**Confidence (AC3):** Medium - the full text is the arXiv OA preprint (staged from the Endnote attachment), reporting deployment lessons rather than a peer-reviewed validation.')

FDN[7] = ('**Fusion depth (AC1):** Unclear\n\n**Fusion evidence (AC2):**\n'
    '- **Data streams:** illustrative scenario inputs only (wearable IMU motion capture, postural tracking, case-based near-miss records).\n'
    '- **Integration mechanism:** none implemented - the two-way mapping between virtual models and the physical facility is defined conceptually, and ML training of movement data is only suggested.\n'
    '- **Why this code:** Unclear (rule 2 - perspective paper with no implementation).\n\n'
    '**Confidence (AC3):** High.')

FDN[13] = ('**Fusion depth (AC1):** Unclear\n\n**Fusion evidence (AC2):**\n'
    '- **Data streams:** 37 reviewed studies plus 66 FM-professional questionnaire responses.\n'
    '- **Integration mechanism:** none implemented - the four-layer framework (physical/virtual/application/user-interaction) and its data fusion and feedback are conceptual, validated only by thematic analysis and survey.\n'
    '- **Why this code:** Unclear (rule 2).\n\n'
    '**Confidence (AC3):** High.')

FDN[14] = ('**Fusion depth (AC1):** Aligned\n\n**Fusion evidence (AC2):**\n'
    '- **Data streams:** Wi-Fi/LoRa beacon time series (temperature, humidity, CO2, TVOC) + RTSP surveillance video on a firefighter training tower.\n'
    '- **Integration mechanism:** each video segment is timestamped and stored by the Video Management Module, and the custom Grafana plugin cross-references RTSP streams with MySQL sensor time series, giving both a shared temporal frame; the ML forecasting pipeline (SVR/RF/Huber/GPR) runs on sensor series only.\n'
    '- **Why this code:** the two data types are linked by a shared timestamp frame while inference stays per type, so Aligned.\n\n'
    '**Confidence (AC3):** High - the timestamped video-to-MySQL synchronisation is described verbatim in the full text.')

FDN[19] = ('**Fusion depth (AC1):** Unclear\n\n**Fusion evidence (AC2):**\n'
    '- **Data streams:** the two illustrative DT cases (Bidebieta-Basauri station, UPM school) are management/visualisation platforms with real-time information integration.\n'
    '- **Integration mechanism:** none specified - the paper is a CEN/TC 442/WG 9 standardisation position paper and gives no data-integration mechanism for the cases.\n'
    '- **Why this code:** Unclear (rule 6 - the text is silent on the integration mechanism).\n\n'
    '**Confidence (AC3):** High.')

FDN[20] = ('**Fusion depth (AC1):** Aligned\n\n**Fusion evidence (AC2):**\n'
    '- **Data streams:** RFID UHF tag readings on Android devices + Web-based Revit/Dynamo BIM models of metallic formwork.\n'
    '- **Integration mechanism:** Smart Twins 4.0 links physical formworks to their virtual BIM counterparts through automatic database integration (Firebase), i.e. a shared object identity between tag data and BIM elements; 151 panels were inspected with 100% external and 98% internal defects.\n'
    '- **Why this code:** tag data and BIM share a common object-identity frame while analysis stays per type, so Aligned.\n\n'
    '**Confidence (AC3):** Medium - the automatic database integration is explicit, but the paper does not describe a joint inference step.')

FDN[21] = ('**Fusion depth (AC1):** Aligned\n\n**Fusion evidence (AC2):**\n'
    '- **Data streams:** UAV imagery-derived 3D meshes + georeferenced defect records on two real inspection datasets.\n'
    '- **Integration mechanism:** defect records are anchored to the georeferenced meshes in PostGIS via raycasting and frustum-based image retrieval, putting imagery geometry and defect annotations in one spatial reference frame (sub-25 ms queries, over 90% retrieval accuracy).\n'
    '- **Why this code:** the two data types share a spatial (georeferenced) frame while annotation and reconstruction run separately, so Aligned.\n\n'
    '**Confidence (AC3):** High - the raycasting/frustum anchoring mechanism is explicit in the full text.')

FDN[22] = ('**Fusion depth (AC1):** SINGLE\n\n**Fusion evidence (AC2):**\n'
    '- **Data streams:** wireless-accelerometer ambient-vibration time series (two years, Basque Country bridge).\n'
    '- **Integration mechanism:** none - clustering of normal vibration plus a LightGBM classifier (ROC-AUC 0.9999) operate on the one measured type; FEM-calibrated synthetic damage data are model-generated training labels, not a second measured data type.\n'
    '- **Why this code:** only one data type is used, so SINGLE (AC=Single).\n\n'
    '**Confidence (AC3):** High - the single vibration modality is explicit.')

FDN[23] = ('**Fusion depth (AC1):** Aligned\n\n**Fusion evidence (AC2):**\n'
    '- **Data streams:** 3D LiDAR point-cloud survey of the Basilica Maria Auxiliadora + BIM geometry + 3DEC/SAP2000 FEM models.\n'
    '- **Integration mechanism:** the point-cloud survey is converted into a BIM that is linked to the FEM models through an explicit BIM-FEM linking process, sharing one building geometry frame, while each model analyses separately (modal with 220 modes, time-history of 34 records); sensor deployment is future work.\n'
    '- **Why this code:** geometry sources share the BIM frame but analysis stays per model, so Aligned.\n\n'
    '**Confidence (AC3):** Medium - the BIM-FEM linking process is explicit, but no live sensor data exists yet.')

FDN[35] = ('**Fusion depth (AC1):** Unclear\n\n**Fusion evidence (AC2):**\n'
    '- **Data streams:** requirements-analysis inputs for critical-infrastructure crisis management (DLR framework).\n'
    '- **Integration mechanism:** none implemented - the virtual replica/clones/toolbox/control-center model and the resilience learning cycle are conceptual.\n'
    '- **Why this code:** Unclear (rule 2).\n\n'
    '**Confidence (AC3):** High.')

# ---- Loader for coding batches (all remaining 141 papers) ----
import importlib
for _mod in ('fusion_batchA', 'fusion_batchB', 'fusion_batchC',
             'fusion_batchD', 'fusion_batchE1', 'fusion_batchE2', 'fusion_batchF'):
    _m = importlib.import_module(_mod)
    for _n, (_c, _e, _cf, _note) in _m.FB.items():
        FD[_n] = _c
        FDEV[_n] = _e
        FDCF[_n] = _cf
        FDN[_n] = _note
