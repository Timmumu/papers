# -*- coding: utf-8 -*-
"""Fusion-depth batch B."""
FB = {}

FB[104] = ('Fused',
    'Video, sensor, BIM and text streams are aligned at component level via Component-ID + timestamp and then jointly processed by a multimodal Transformer for operation-state recognition and short-horizon risk prediction.',
    'High',
    '**Fusion depth (AC1):** Fused\n\n**Fusion evidence (AC2):**\n- **Data streams:** video, sensor, BIM and text streams on a high-rise self-climbing platform project.\n- **Integration mechanism:** Component-ID plus timestamp aligns the four streams; a multimodal Transformer jointly recognises operation states and predicts short-horizon risks, and constraint-encoded policies generate task sequences delivered via AR with acknowledgments (warning lead time 1.8 to 4.6 s; violations cut 52%).\n- **Why this code:** one model whose output depends on multiple aligned data types simultaneously, so Fused; implemented and demonstrated on a real project.\n\n**Confidence (AC3):** High - the Component-ID+timestamp alignment and multimodal Transformer are explicitly described.')

FB[106] = ('Fused',
    'Multi-sensor data (monitoring LiDAR, automated robots, GNSS, drones, SBAS-InSAR) are linked to RBIM through GUID object mapping tables and combined by a cloud platform using weighted-average fusion and conflict detection.',
    'High',
    '**Fusion depth (AC1):** Fused\n\n**Fusion evidence (AC2):**\n- **Data streams:** real-time LiDAR, automated monitoring robots, GNSS, SBAS-InSAR settlement data, 8-phase LiDAR frame-building monitoring.\n- **Integration mechanism:** GUID object mapping tables link physical things to RBIM, and the cloud platform applies weighted-average fusion with conflict detection, achieving consistent millimetre/sub-millimetre settlement precision across monitoring points.\n- **Why this code:** named fusion algorithms (weighted average + conflict detection) combine multiple data types into one settlement estimate, so Fused; implemented and demonstrated.\n\n**Confidence (AC3):** High - the GUID mapping tables and weighted-average fusion are explicit in the full text.')

FB[109] = ('SINGLE',
    'Only crowdsourced smartphone imagery drives the geospatial localisation of vulnerable objects (mean-shift clustering), so a single data type is used.',
    'High',
    '**Fusion depth (AC1):** SINGLE\n\n**Fusion evidence (AC2):**\n- **Data streams:** 135 smartphone photos from five participants.\n- **Integration mechanism:** none needed - localisation via mean-shift clustering operates on imagery only (4.49 m average distance error).\n- **Why this code:** SINGLE (AC=Single).\n\n**Confidence (AC3):** High.')

FB[110] = ('Aligned',
    'Twenty-eight IoT sensing nodes (water pressure, gas leakage, surface temperature) are mapped into a lightweight BIM-GIS platform, and the AI risk model predicts per-asset (valve aging) rather than fusing streams.',
    'Medium',
    '**Fusion depth (AC1):** Aligned\n\n**Fusion evidence (AC2):**\n- **Data streams:** 28 IoT nodes (pressure, gas leakage, surface temperature, under-1-s delay) + BIM0-BIM6 lifecycle models on a 5-month Shanghai Oriental Hub pilot.\n- **Integration mechanism:** sensors are linked to BIM-GIS assets for monitoring and display; the AI risk model predicted one valve aging risk 7 days ahead, but no joint multi-stream inference is described.\n- **Why this code:** streams share the BIM-GIS asset frame while inference stays per asset, so Aligned (downgrade from Fused per rule 5).\n\n**Confidence (AC3):** Medium - platform linkage is clear; joint processing is not stated.')

FB[111] = ('Fused',
    'UAV detections are cross-referenced with GPS-enabled worker IDs to verify authorisation, so the decision output depends on visual detections and GPS identity data simultaneously.',
    'High',
    '**Fusion depth (AC1):** Fused\n\n**Fusion evidence (AC2):**\n- **Data streams:** YOLOv10-LCA UAV detections (mAP50 31.5 to 96.4%) + DeepSORT tracks + GPS-enabled electronic work permits + georegistered 3D reconstruction.\n- **Integration mechanism:** cross-referencing UAV detections with GPS-enabled worker IDs produces the authorisation-verification decision, joining two data types; 3D-TSP routes inspections across 19 Hong Kong sites.\n- **Why this code:** the verification output depends on two data types simultaneously, so Fused; implemented and field-validated.\n\n**Confidence (AC3):** High - the cross-referencing mechanism is explicitly described.')

FB[112] = ('Fused',
    'UWB and IMU sensing streams are fused inside the PosTraFormer spatio-temporal network (multi-layer GCNs over trajectory point relations) for 6-D pose estimation and trajectory prediction.',
    'High',
    '**Fusion depth (AC1):** Fused\n\n**Fusion evidence (AC2):**\n- **Data streams:** UWB sensors + IMUs on smart stacking objects; simulated trajectories plus 70 real pose sets for fine-tuning.\n- **Integration mechanism:** PosTraFormer performs spatio-temporal feature fusion of the two streams and predicts 6-D module pose and trajectories (lowest FDE/ADE across four lifting scenarios), shown in the DT platform with collision shields.\n- **Why this code:** an explicit fusion network whose output depends on both sensing types, so Fused.\n\n**Confidence (AC3):** High - the fusion architecture is explicit.')

FB[115] = ('SINGLE',
    'Only the ultrasonic distance sensor stream is actually used in the twin; the MPU-6050 accelerometer/gyroscope readings were excluded because of latency and twitching.',
    'High',
    '**Fusion depth (AC1):** SINGLE\n\n**Fusion evidence (AC2):**\n- **Data streams:** HC-SR04 ultrasonic distance data for safety/clash detection; MPU-6050 inertial readings excluded from the twin.\n- **Integration mechanism:** none - one active sensor stream drives the Unity3D twin over Wi-Fi; control commands run on the same Arduino loop but are actuator actions, not a second data type.\n- **Why this code:** a single data type is effectively used, so SINGLE (AC=Single).\n\n**Confidence (AC3):** High - the MPU-6050 exclusion is stated in the full text.')

FB[118] = ('Fused',
    'The Universal Discontinuity Index fuses physical damage, effective-stress intensity, active-fracture ratio and kinematic feasibility into one probabilistic score feeding a Poisson early-warning model.',
    'High',
    '**Fusion depth (AC1):** Fused\n\n**Fusion evidence (AC2):**\n- **Data streams:** four physical/geometric indicators per tunnel face; DFN-KBT realisations (5300) at El Teniente.\n- **Integration mechanism:** UDi combines the four indicators into a single score that the Poisson-regression model converts into expected block counts (R2 0.93, 95% accuracy), with millisecond updates for the DT workflow.\n- **Why this code:** an explicit fusion index whose output depends on four data components simultaneously, so Fused.\n\n**Confidence (AC3):** High - the UDi fusion formula is the paper core contribution.')

FB[121] = ('Fused',
    'Multi-source sensing (MEMS, BOFDA distributed optical fibre, laser radar, UAV, machine vision) feeds four neural-network predictors on the BIM platform, which the paper itself calls a multi-source fusion platform.',
    'High',
    '**Fusion depth (AC1):** Fused\n\n**Fusion evidence (AC2):**\n- **Data streams:** MEMS, BOFDA distributed fibre, laser radar, UAV and machine-vision sensing of pit axial force, displacement, strain and temperature (Shenzhen Metro Line 12).\n- **Integration mechanism:** sensor streams are combined in the BIM-based monitoring platform where four NNs (GA-BP best) predict key pit parameters, with Unity3D + AR visualisation; the authors explicitly describe it as a multi-source fusion platform.\n- **Why this code:** multi-input predictors consume several sensing types jointly, so Fused; implemented on a real station.\n\n**Confidence (AC3):** High - the multi-source fusion platform description is explicit.')

FB[122] = ('SINGLE',
    'Only RTK-GNSS over LoRa position tracking (1.0 cm median, 2.3 cm 95th percentile) drives the right-time analysis; no second measured data type exists.',
    'High',
    '**Fusion depth (AC1):** SINGLE\n\n**Fusion evidence (AC2):**\n- **Data streams:** RTK-GNSS/LoRa live locations of workers and equipment at a Munich railway staging area.\n- **Integration mechanism:** none - position streams alone feed semi-static/dynamic hazard zones, 99 unauthorised-entry detections and heatmaps in the DTCS module.\n- **Why this code:** SINGLE (AC=Single).\n\n**Confidence (AC3):** High.')

FB[125] = ('SINGLE',
    'Only expert-opinion data (20 indicator-weighting questionnaires, 15 valid case-study questionnaires) drive the maturity assessment; no sensor or operational data are used.',
    'High',
    '**Fusion depth (AC1):** SINGLE\n\n**Fusion evidence (AC2):**\n- **Data streams:** expert questionnaires and interviews feeding 24 maturity indicators.\n- **Integration mechanism:** none - Louvain grouping and the bi-objective aggregation model process one data type (expert judgements); the ACS case only contextualises the assessment.\n- **Why this code:** SINGLE (AC=Single).\n\n**Confidence (AC3):** High.')

FB[128] = ('Aligned',
    'Strain-gauge and laser-distance sensor readings are mapped onto BIM elements through Revit Dynamo interpolation, sharing the BIM frame while each sensor channel is processed separately.',
    'High',
    '**Fusion depth (AC1):** Aligned\n\n**Fusion evidence (AC2):**\n- **Data streams:** strain gauges + laser distance sensors on a prototyped aluminium frame; wavelet sym4 denoising (threshold 25, level 6).\n- **Integration mechanism:** bending-moment interpolation maps one sensor onto other Revit locations, refreshing colour-coded deformation at 5 Hz; no joint multi-sensor inference exists.\n- **Why this code:** two sensor types share the BIM model frame but inference stays per location, so Aligned.\n\n**Confidence (AC3):** High - the interpolation mapping is explicit.')

FB[129] = ('Fused',
    'Multi-source risk assessment uses improved D-S evidence theory with conflict weakening and a validity factor to fuse personnel, pipe-sheet, shield and environmental data into one belief-level risk output.',
    'High',
    '**Fusion depth (AC1):** Fused\n\n**Fusion evidence (AC2):**\n- **Data streams:** personnel, pipe-sheet, shield and environmental sensor data in BIM dynamic modelling (Jinan High-Speed Train Depot tunnel).\n- **Integration mechanism:** improved D-S evidence theory fuses the streams, cutting belief-interval length from 0.37 to 0.14, capturing a palm-face collapse with 100% warning accuracy and prediction errors under 1.9 MN / 5.44 mm.\n- **Why this code:** an explicit fusion algorithm whose output depends on multiple sources simultaneously, so Fused.\n\n**Confidence (AC3):** High - the D-S fusion procedure is the paper core mechanism.')

FB[137] = ('Fused',
    'Online map layers (DSM, DEM and aerial photos) are jointly processed to reconstruct the existing road and underpass as one digital twin used for clearance checking.',
    'Medium',
    '**Fusion depth (AC1):** Fused\n\n**Fusion evidence (AC2):**\n- **Data streams:** Digimap DSM, DTM and aerial photography.\n- **Integration mechanism:** road-marking extraction, smoothing-spline alignment (R-square near 1.0) and flattened terrain models combine the map layers into a single reconstructed twin, against which a 5.338 m clearance envelope is clash-checked (M11/Sawbridgeworth Road case).\n- **Why this code:** the reconstructed model depends on several map data layers simultaneously, so Fused.\n\n**Confidence (AC3):** Medium - joint reconstruction is clear, but map layers are all geospatial products of one survey family.')

FB[138] = ('Aligned',
    'Settlement, stress and displacement sensors stream into IFC-extended Revit BIM models with parametric sensor attributes and time-history curves, linking sensors to BIM elements without joint inference.',
    'High',
    '**Fusion depth (AC1):** Aligned\n\n**Fusion evidence (AC2):**\n- **Data streams:** pressure cells, rebar meters, strain gauges and displacement meters (Shikui Road Station, Dalian Metro Line 5).\n- **Integration mechanism:** IFC extension plus Revit parametric sensor models attach each sensor to a BIM element for visualisation and colour-change alarms; inverse analysis decisions (midwall demolition at 12 m) are human-in-the-loop.\n- **Why this code:** sensors share the BIM asset frame while analysis stays per element, so Aligned.\n\n**Confidence (AC3):** High - the IFC sensor-attribute extension is explicit.')

FB[141] = ('Fused',
    'The BFP ontology fuses static BIM geometry with dynamic IoT sensing data into one DT data model, on which rule models trigger BPMN process models for fire-protection control.',
    'Medium',
    '**Fusion depth (AC1):** Fused\n\n**Fusion evidence (AC2):**\n- **Data streams:** static BIM geometry + dynamic IoT sensing data.\n- **Integration mechanism:** the BFP ontology is the joint representation fusing the two types; rule models then activate process models (sprinkler, fire door, smoke control) with update rules synchronising virtual and physical spaces.\n- **Why this code:** an explicit fusion into one ontology-based data model, so Fused; verified through FDS fire simulations rather than live deployment (hence Medium confidence).\n\n**Confidence (AC3):** Medium - the fusion mechanism is explicit, but validation is simulation-only.')

FB[143] = ('Fused',
    'Twenty-Hz scale-model sensors (displacement, tilt etc.) stream through IoT into synchronous FEM/BIM/IDA virtual models that compute real-time dynamic stability analysis and collapse-probability levels.',
    'Medium',
    '**Fusion depth (AC1):** Fused\n\n**Fusion evidence (AC2):**\n- **Data streams:** 20 Hz scale-model sensor data on a 1/30 tower crane; FEM, BIM and component IDA virtual models.\n- **Integration mechanism:** IoT data flow synchronises the virtual models with measured states, and incremental dynamic load analysis computes collapse-probability levels (TCL/FCL/MCL/JCL/CCL/RCL) that rank unsafe hoisting behaviours; sensor-vs-model trends are compared directly.\n- **Why this code:** the stability output depends on measured sensor states and model responses simultaneously, so Fused; lab-scale only (Medium).\n\n**Confidence (AC3):** Medium - the synchronisation mechanism is clear, but validation is a laboratory scale model.')

FB[144] = ('Fused',
    'Real-time multi-sensor states mirrored in the DT are jointly reasoned over by a standards-derived knowledge graph to identify unsafe hoisting operations and trigger early warnings.',
    'Medium',
    '**Fusion depth (AC1):** Fused\n\n**Fusion evidence (AC2):**\n- **Data streams:** three 9-axis IMUs, two laser sensors and STM32 board telemetry from a 1:80 scaled tower crane.\n- **Integration mechanism:** the DT mirrors all sensor channels, and the KG (seven standards, 86 accident reports) performs joint rule reasoning over the integrated states, achieving over 70% warning accuracy and under 20% false alarms.\n- **Why this code:** warning decisions depend on several sensor streams simultaneously through KG reasoning, so Fused; lab-only validation (Medium).\n\n**Confidence (AC3):** Medium - the KG reasoning over integrated states is explicit, but validation is laboratory-scale.')

FB[148] = ('Fused',
    'BIM, schedule and automated safety-analysis results are integrated into one Prolog knowledge graph (about 3,800 nodes, 20,000 edges) whose cross-domain queries answer planning questions over all three data types simultaneously.',
    'Medium',
    '**Fusion depth (AC1):** Fused\n\n**Fusion evidence (AC2):**\n- **Data streams:** 4D BIM data, construction schedule data and automated safety-analysis results.\n- **Integration mechanism:** the safety ontology + Prolog KG is the joint representation; query building blocks transform natural-language questions into queries that reveal cross-domain impacts (crew assignment to safety), answered in under one second.\n- **Why this code:** query outputs depend on three integrated data types simultaneously, so Fused; no live IoT data (out of scope), hence Medium.\n\n**Confidence (AC3):** Medium - the KG integration is explicit, but live data linkage is explicitly out of scope.')

FB[154] = ('Fused',
    'SfM/MVS photogrammetry reconstructs jobsite point clouds, ResNet50 semantic segmentation runs in 2D and a depth-aware projection fuses the two into 3D semantic segmentations (97.85 to 99.8% accuracy).',
    'High',
    '**Fusion depth (AC1):** Fused\n\n**Fusion evidence (AC2):**\n- **Data streams:** jobsite imagery (SfM/MVS point clouds) + ResNet50 2D segmentations.\n- **Integration mechanism:** depth-aware projection maps 2D labels onto the 3D point cloud, raising 3D segmentation accuracy from 97.85% to 99.8%; volumetric measurements (2.4-9.2% error) then feed kinetic-energy threat heatmaps.\n- **Why this code:** the 3D segmentation output depends on imagery and depth geometry simultaneously, so Fused.\n\n**Confidence (AC3):** High - the depth-aware projection mechanism is explicit.')

FB[155] = ('Fused',
    'UAV photogrammetry, Street-View CNN segmentation and satellite terrain modelling are combined in one HAZUS-based reliability computation of nearby glazing systems under windborne-debris impact.',
    'High',
    '**Fusion depth (AC1):** Fused\n\n**Fusion evidence (AC2):**\n- **Data streams:** 45 UAV images (dense point cloud + binarised DSM, volume error about 4.6%), Google Street View imagery (ResNet50, 85.0%), satellite terrain data.\n- **Integration mechanism:** the three sources jointly feed the FEMA-HAZUS windborne-missile model that computes glazing reliability (about 237 adjusted impacts at 62 m/s over 80 m), so the output depends on all of them simultaneously.\n- **Why this code:** a joint multi-source reliability computation, so Fused.\n\n**Confidence (AC3):** High - the HAZUS computation chain is explicit.')
