# -*- coding: utf-8 -*-
"""Fusion-depth batch E1."""
FB = {}

FB[315] = ('Aligned',
    'One hundred and twenty embedded strain gauges plus support-reaction, temperature and displacement sensors are mapped onto the web-BIM/Midas twin points, and three-level warnings fire on per-point deviations between measured and simulated stress.',
    'High',
    '**Fusion depth (AC1):** Aligned\n\n**Fusion evidence (AC2):**\n- **Data streams:** 120 strain gauges + support-reaction, temperature and displacement sensors on the Zhanlin Yellow River cable-stayed bridge.\n- **Integration mechanism:** the multi-resolution twin (web-BIM + Midas Civil, 267 elements, 19 launching stages) maps sensors onto model points, and warning levels (L1 11%, L2 20-30%, L3 over 30% deviation) compare measured versus simulated stress per point.\n- **Why this code:** sensors share the model reference frame while warning logic is a per-point comparison, so Aligned (torn with Fused, the lower level chosen per rule 5).\n\n**Confidence (AC3):** High - the deviation-threshold warning mechanism is explicit.')

FB[318] = ('Fused',
    'TEM, GPR and borehole data are converted into point-cloud models of water content, lithology and integrity and jointly classified by a fuzzy cloud probability model into surrounding-rock classes.',
    'High',
    '**Fusion depth (AC1):** Fused\n\n**Fusion evidence (AC2):**\n- **Data streams:** TEM, GPR and borehole geological data (five rock-tunnel projects, 539 exposed-rock records).\n- **Integration mechanism:** KNN interpolation builds per-attribute point clouds, and the fuzzy cloud probability model jointly quantifies uncertainty to classify rock per metre within 30 m (92.95% accuracy) on the iS3 platform.\n- **Why this code:** the classification output depends on three geological data types simultaneously, so Fused.\n\n**Confidence (AC3):** High - the fuzzy cloud fusion is explicit.')

FB[320] = ('Fused',
    'RFID, displacement, soil-pressure and environmental sensing are fused into an 850,141-cell FLAC3D model updated after each excavation step, with Markov-chain risk prediction and a bow-tie model selecting control measures.',
    'High',
    '**Fusion depth (AC1):** Fused\n\n**Fusion evidence (AC2):**\n- **Data streams:** RFID, displacement, soil-pressure and environmental sensors (Wuhan Metro Line 7 air shaft, 15.2 mm max settlement).\n- **Integration mechanism:** the multi-source sensing updates the FE model after each step, and Markov-chain prediction plus the bow-tie model compute risk states and control measures on the updated model.\n- **Why this code:** risk prognosis depends on several sensing types and the updated model simultaneously, so Fused.\n\n**Confidence (AC3):** High - the sensor-to-model updating chain is explicit.')

FB[321] = ('Fused',
    'YOLOv8 UAV imagery, PointNet LiDAR point clouds and LSTM-forecast sensor series are combined through a fuzzy-logic expert knowledge base whose rules assess structural health over all three outputs.',
    'Medium',
    '**Fusion depth (AC1):** Fused\n\n**Fusion evidence (AC2):**\n- **Data streams:** UAV imagery (YOLOv8), LiDAR point clouds (PointNet), LSTM-forecast sensor series (Hedong Bridge).\n- **Integration mechanism:** three perception pipelines feed one fuzzy-logic knowledge base with rule-engine reasoning that produces the automated health assessment (12 mm mid-span displacement, early fatigue risks).\n- **Why this code:** the assessment output depends on three data types simultaneously, so Fused.\n\n**Confidence (AC3):** Medium - the three-pipeline-to-knowledge-base combination is explicit, but no quantitative fusion accuracy is reported.')

FB[322] = ('Unclear',
    'The human-in-the-loop DT framework formalises human cognition, AI and engineering knowledge into a device-model-decision architecture, but validation is qualitative and conceptual only.',
    'High',
    '**Fusion depth (AC1):** Unclear\n\n**Fusion evidence (AC2):**\n- **Data streams:** framework components (human inspection, machine vision, engineering codes, case knowledge).\n- **Integration mechanism:** none demonstrated - operational feasibility and logical consistency only; no numerical tests.\n- **Why this code:** Unclear (rule 1/2).\n\n**Confidence (AC3):** High.')

FB[324] = ('SINGLE',
    'Only orientation-sensor data (XSens MTw on boom, stick and bucket) drive the forward-kinematic DT updates; vision references in the text are background literature, not an implemented data source.',
    'High',
    '**Fusion depth (AC1):** SINGLE\n\n**Fusion evidence (AC2):**\n- **Data streams:** orientation sensors on the backhoe boom/stick/bucket (15 configurations, 0.06 m mean separation error).\n- **Integration mechanism:** none - forward kinematics maps one sensor type into the 3D twin, and proximity monitoring applies preset safety buffers with audio-visual warnings.\n- **Why this code:** one measured data type, so SINGLE. Note: column AC lists Multi; under the fusion-depth rules the forward-kinematic model and warning zones are computations over one sensor modality.\n\n**Confidence (AC3):** High - the single sensor type is explicit in the full text.')

FB[329] = ('Fused',
    'Multisource heterogeneous data are semantically linked in an ontology-based four-layer model in GraphDB, and SPARQL iterative deviation computation reasons over the linked data to identify quality defect triggers.',
    'High',
    '**Fusion depth (AC1):** Fused\n\n**Fusion evidence (AC2):**\n- **Data streams:** quality standards, quality data, defect triggers and construction processes linked in GraphDB (prefabricated composite-slab case).\n- **Integration mechanism:** the ontology links the heterogeneous sources into one graph, and iterative deviation computation flags triggers exceeding tolerances (4.63 mm misalignment, 2.9 mm flatness deviation; 100% identification accuracy in 371 s).\n- **Why this code:** trigger identification depends on multiple linked data types simultaneously, so Fused.\n\n**Confidence (AC3):** High - the ontology + SPARQL deviation mechanism is explicit.')

FB[331] = ('Unclear',
    'A scoping review plus Research-through-Design proposal outlines a BIM-DT-DSS safety framework, with no prototype, sensor integration or live data link.',
    'High',
    '**Fusion depth (AC1):** Unclear\n\n**Fusion evidence (AC2):**\n- **Data streams:** framework components (data/information streams, KPIs, real-time interfaces) only.\n- **Integration mechanism:** none implemented - ML-based optimisation is future work.\n- **Why this code:** Unclear (rule 2).\n\n**Confidence (AC3):** High.')

FB[332] = ('Unclear',
    'The BDTP architecture with BPMN workflows and digital/human agents connected via APIs is a Design-Science conceptual framework; implementation, KPIs and AI/ML are future work.',
    'High',
    '**Fusion depth (AC1):** Unclear\n\n**Fusion evidence (AC2):**\n- **Data streams:** questionnaire/interview-derived requirements (Living Labs) mapped onto five cross-cutting domains.\n- **Integration mechanism:** none deployed - property-graph data model and API connections are proposed.\n- **Why this code:** Unclear (rule 2).\n\n**Confidence (AC3):** High.')

FB[333] = ('Fused',
    'A dynamic decision network couples convolutional DL damage diagnostics with sequential Bayesian state inference, so the health-tracking output depends on the measured (synthetic) vibration stream and the learned dynamics simultaneously.',
    'Medium',
    '**Fusion depth (AC1):** Fused\n\n**Fusion evidence (AC2):**\n- **Data streams:** vibration recordings (synthetic cantilever beam, Hornefors bridge) + reduced-order physics-model dynamics.\n- **Integration mechanism:** the DDN encodes the asset-twin coupled system: DL classifies damage (93.61%/91.39% accuracy) and sequential Bayesian updating tracks health and recommends do-nothing/repair/restrict actions.\n- **Why this code:** the control-policy output depends on the data-driven and model-driven components simultaneously, so Fused; synthetic data only (Medium).\n\n**Confidence (AC3):** Medium - the DDN coupling is explicit, but validation uses synthetic data.')

FB[334] = ('Unclear',
    'A review plus methodology proposal for physical digital twins of nuraghi masonry lists possible mechanical and multiphysical modelling roads, with no twin built or validated.',
    'High',
    '**Fusion depth (AC1):** Unclear\n\n**Fusion evidence (AC2):**\n- **Data streams:** proposed inputs (3D surveys, historical documentation, laboratory tests).\n- **Integration mechanism:** none implemented - approaches are under investigation for future structural studies.\n- **Why this code:** Unclear (rule 2).\n\n**Confidence (AC3):** High.')

FB[335] = ('Fused',
    'BIM, GIS and real-time IoT streams are harmonised in a PostGIS repository where rule-based vulnerability and risk scores are computed jointly over the three sources for multi-hazard assessment.',
    'Medium',
    '**Fusion depth (AC1):** Fused\n\n**Fusion evidence (AC2):**\n- **Data streams:** BIM building data + GIS territorial layers + real-time IoT information (flood case, northwest Italy).\n- **Integration mechanism:** the centralized PostGIS repository updates hazard, vulnerability and risk scores from all three sources, giving stakeholders near-real-time territorial and building-level risk views.\n- **Why this code:** risk-score outputs depend on the three data types simultaneously, so Fused (beyond shared storage per rule 3).\n\n**Confidence (AC3):** Medium - the score-update mechanism is explicit, but the computation is rule-based and single-hazard.')

FB[340] = ('Aligned',
    'UAV and AMR measurements are geo-registered and merged via MQTT/Node-RED into ontology-based KPI dashboards, sharing a geospatial frame while KPI analytics run per asset type.',
    'Medium',
    '**Fusion depth (AC1):** Aligned\n\n**Fusion evidence (AC2):**\n- **Data streams:** UAV YOLOX detections, UPerNet segmentation, LiDAR retro-reflectivity (vertical assets) + AMR measurements of horizontal markings (A24 Gran Sasso Nord).\n- **Integration mechanism:** field agents are synchronised with the centralised DT and fused into ontology-based KPI dashboards with sub-10-cm AMR repeatability; no joint inference beyond KPIs is described.\n- **Why this code:** streams share the georeferenced ontology frame while analytics stay per asset, so Aligned (torn with Fused, lower level chosen per rule 5).\n\n**Confidence (AC3):** Medium - the data-fusion-into-dashboards description is explicit; joint computation depth is limited.')

FB[343] = ('Aligned',
    'The FE model and the photorealistic CG model share one imported building geometry (SAP2000 to Blender), so the two model types are aligned by component, while UAV flight-scheme evaluation runs on the coupled model.',
    'Medium',
    '**Fusion depth (AC1):** Aligned\n\n**Fusion evidence (AC2):**\n- **Data streams:** SAP2000 FE components + Blender CG model + UAV photogrammetry point-cloud validation (45-floor Guangzhou tower).\n- **Integration mechanism:** structural components are automatically imported from FE into the CG model, sharing one geometry frame; damage hotspots and environmental constraints then drive the three flight-scheme evaluations.\n- **Why this code:** model types share a common geometry reference while analysis runs per stage, so Aligned; no live data.\n\n**Confidence (AC3):** Medium - the FE-to-CG import is explicit; the twin is static.')

FB[347] = ('Aligned',
    'Human VR task plans and the robot status are synchronised bidirectionally in the process-level DT, sharing one robot-state frame, while sensing, motion planning and execution run in their own stages.',
    'High',
    '**Fusion depth (AC1):** Aligned\n\n**Fusion evidence (AC2):**\n- **Data streams:** human VR high-level task plans/trajectory guidance + KUKA robot state via ros_control/PID (drywall installation case).\n- **Integration mechanism:** bidirectional communication synchronises the VR view with the robot state for supervision; SBT/motion planning and physical execution are separate stages of the loop.\n- **Why this code:** the two streams share the robot-state frame with per-stage processing, so Aligned.\n\n**Confidence (AC3):** High - the bidirectional synchronisation is explicit.')

FB[349] = ('Fused',
    'BIM shop-drawing geometry, AprilTag vision localisation and sensed as-built data are combined in the robot motion-planning loop, whose adaptation output depends on all three simultaneously, with as-built data written back to BIM.',
    'High',
    '**Fusion depth (AC1):** Fused\n\n**Fusion evidence (AC2):**\n- **Data streams:** Rhino BIM geometry + AprilTag/vision localisation + sensed as-built data (KUKA KR120, drywall + block pick-and-place).\n- **Integration mechanism:** robot-proposed adaptations resolve parent and nearby-object deviations by combining BIM, sensing and current state, and sensed as-built data are written back into the BIM, closing the loop (100% success at 10 mm gaps).\n- **Why this code:** motion-planning output depends on multiple data types simultaneously and the loop is bidirectional, so Fused.\n\n**Confidence (AC3):** High - the BIM-sensing closed loop is explicit.')

FB[354] = ('Unclear',
    'A review plus conceptual prefabricated-building DT framework with a construction-service-bus architecture; no system is implemented or validated.',
    'High',
    '**Fusion depth (AC1):** Unclear\n\n**Fusion evidence (AC2):**\n- **Data streams:** reviewed application examples (hoisting management, safety monitoring, predictive analytics).\n- **Integration mechanism:** none implemented - closed-loop control and AI learning are future directions.\n- **Why this code:** Unclear (rule 2).\n\n**Confidence (AC3):** High.')
