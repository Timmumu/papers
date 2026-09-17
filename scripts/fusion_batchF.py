# -*- coding: utf-8 -*-
"""Fusion-depth batch F."""
FB = {}

FB[396] = ('SINGLE',
    'Only point-cloud data drive the DS-gDT joint detection and topology reconstruction; no second measured data type exists.',
    'High',
    '**Fusion depth (AC1):** SINGLE\n\n**Fusion evidence (AC2):**\n- **Data streams:** scaled cable-dome point clouds.\n- **Integration mechanism:** none - three-point normal cylinder fitting with radius-constrained sampling detects components, and the adjacency matrix rebuilds topology (about 51.5% above RANSAC, over 99% joint accuracy).\n- **Why this code:** SINGLE (AC=Single).\n\n**Confidence (AC3):** High.')

FB[398] = ('Aligned',
    'IoT sensors are mirrored into the four-layer DT virtual model (geometric/physical/behavioural/rule-based), and the edge intelligent control device issues navigation and alarms per signal threshold.',
    'High',
    '**Fusion depth (AC1):** Aligned\n\n**Fusion evidence (AC2):**\n- **Data streams:** IoT sensor streams during the eight-step tower-crane climbing cycle (one scaled model + one Xiangyang project).\n- **Integration mechanism:** real-time mapping mirrors sensors into the DT layers, and EICD alarms/navigation act per threshold (dialogues 11.8-12.2 down to 0.8-1.6; errors to zero), while control stays with human operators.\n- **Why this code:** streams share the DT model frame with per-signal inference, so Aligned.\n\n**Confidence (AC3):** High - the IoT-to-DT mapping is explicit.')

FB[401] = ('Fused',
    'UAV detections are projected onto the GeoBIM model through virtual-camera depth rendering and SfM pose correction, so defect localisation depends on imagery, camera geometry and BIM geometry simultaneously.',
    'High',
    '**Fusion depth (AC1):** Fused\n\n**Fusion evidence (AC2):**\n- **Data streams:** UAV imagery with YOLO/R-CNN detections + GeoBIM (BIM+GIS) model geometry (Hong Kong high-rise).\n- **Integration mechanism:** virtual cameras render depth from the GeoBIM, and SfM-corrected poses project detections into the georeferenced twin with dual verification (image + geographic features), reaching 0.49-1.36 cm mean localisation error.\n- **Why this code:** localisation output depends on imagery and model geometry simultaneously, so Fused.\n\n**Confidence (AC3):** High - the virtual-camera depth pipeline is explicit.')

FB[402] = ('Unclear',
    'A conceptual framework extending BIM LoDs to construction-site DTs is validated only through 31 questionnaires and 10 expert interviews; no DT is implemented or tested.',
    'High',
    '**Fusion depth (AC1):** Unclear\n\n**Fusion evidence (AC2):**\n- **Data streams:** framework components (BIM representation, IoT, data storage-integration-analytics, interaction/feedback) with LoD-Graphics/LoD-Information definitions.\n- **Integration mechanism:** none implemented - autonomous feedback and control are future directions.\n- **Why this code:** Unclear (rule 2).\n\n**Confidence (AC3):** High.')

FB[404] = ('Fused',
    'Scale-model sensor feedback, a DNN-PID dynamic-error-compensation controller and RL-tuned parameters are combined in the closed-loop synchronous jacking control, whose command output depends on measured and model streams simultaneously.',
    'High',
    '**Fusion depth (AC1):** Fused\n\n**Fusion evidence (AC2):**\n- **Data streams:** 1:25 scale-model jacking sensors + DNN-PID controller state + PPO-tuned parameters (STM32 platform).\n- **Integration mechanism:** the transfer-learned DNN-PID fuses deviation coupling with sensor feedback to command four actuators, cutting mean synchronisation error to 0.377 mm versus 3.485/0.463/0.709 mm, with a 29% transfer-learning gain.\n- **Why this code:** the control output depends on multiple streams simultaneously in a closed loop, so Fused.\n\n**Confidence (AC3):** High - the control architecture is explicit; validation is scale-model only.')

FB[405] = ('Aligned',
    'DHT11, MPU6050, wind and laser displacement sensors stream over MQTT to the Unreal prototype for dataflow verification and threshold alarms, sharing the twin frame while each channel is checked separately.',
    'Medium',
    '**Fusion depth (AC1):** Aligned\n\n**Fusion evidence (AC2):**\n- **Data streams:** DHT11, MPU6050, wind and laser displacement sensors on a 1:100 rotation-construction prototype.\n- **Integration mechanism:** MQTT carries the streams into the Unreal twin which verifies dataflow and triggers threshold alarms per channel; the full bridge DT was not yet deployed when the paper was written.\n- **Why this code:** streams share the twin frame with per-channel processing, so Aligned.\n\n**Confidence (AC3):** Medium - the prototype dataflow is explicit; the final system is design-stage.')

FB[408] = ('Fused',
    'UAV imagery, SfM photogrammetry reconstruction and GIS-oriented registration are combined to project instance-segmentation masks onto the DT surface and convert them into metric crack/spalling measures.',
    'High',
    '**Fusion depth (AC1):** Fused\n\n**Fusion evidence (AC2):**\n- **Data streams:** 6996 high-resolution UAV facade images (62,187 instances) + photogrammetry reconstruction + GIS-oriented registration (Hong Kong logistics building).\n- **Integration mechanism:** masks are projected from image space onto the twin surface via photogrammetry and registration, then converted to crack width/length and spalling area graded per BS ISO 15686-7:2017 at centimetre-level accuracy.\n- **Why this code:** the metric severity output depends on imagery and geometry simultaneously, so Fused.\n\n**Confidence (AC3):** High - the mask-projection pipeline is explicit.')

FB[412] = ('Fused',
    'RGB-D image+depth and IMU motion streams are fused and analysed by YOLOv5/Faster-RCNN/HRNet to drive the Unity virtual entity, whose rule model computes dangerous/warning/safe zones for collision warnings.',
    'High',
    '**Fusion depth (AC1):** Fused\n\n**Fusion evidence (AC2):**\n- **Data streams:** RGB-D image + depth + IMU motion on a 1:24 scaled excavator case.\n- **Integration mechanism:** the paper states multi-sensor fusion of RGB-D and IMU, with multi-modal analysis driving the twin; TTC+SO rule zones (600 mm danger, 1200 mm warning) trigger helmet/tri-colour-light warnings at 96.4%/95.3% precision and 0.13 s delay.\n- **Why this code:** warning output depends on multiple fused sensor types simultaneously, so Fused.\n\n**Confidence (AC3):** High - the stated multi-sensor fusion and zone computation are explicit.')

FB[413] = ('Fused',
    'Stochastic geology (Markov random field), AHP-DEMATEL vulnerability evaluation and delay probability densities are combined inside one discrete-event simulation model whose schedule/safety outputs depend on all inputs.',
    'Medium',
    '**Fusion depth (AC1):** Fused\n\n**Fusion evidence (AC2):**\n- **Data streams:** manual step-duration records, MRF stochastic geological model, AHP-DEMATEL vulnerability scores (real NATM tunnel).\n- **Integration mechanism:** the AnyLogic DES model consumes the geological and vulnerability inputs jointly, and 2500 Monte Carlo runs estimate a 78.4% probability of on-time completion (estimate within 9 days / 0.50% of actual).\n- **Why this code:** the simulation output depends on several data sources simultaneously, so Fused.\n\n**Confidence (AC3):** Medium - the joint DES consumption is explicit; sensing inputs are manual.')

FB[414] = ('Fused',
    'WIM vehicle data (six million vehicles, Gaussian mixture + MCMC sampling) and structural responses jointly train Transformer encoder-decoder models that predict bridge responses across the regional network.',
    'High',
    '**Fusion depth (AC1):** Fused\n\n**Fusion evidence (AC2):**\n- **Data streams:** WIM vehicle loads + field structural responses of three Jiangsu bridges.\n- **Integration mechanism:** traffic load links the physical and digital spaces, and Transformers predict responses with R2 0.9970-0.9999, outperforming LSTM/BiLSTM/BiGRU and validated by field vehicle tests.\n- **Why this code:** the prediction output depends on vehicle-load and response data simultaneously, so Fused.\n\n**Confidence (AC3):** High - the Transformer architecture is explicit.')

FB[416] = ('Fused',
    'IoT multi-sensor project data are fused into BIM+Midas+LSTM twin models with black/gray/white-box processing levels, and the LSTM predicts vault settlement for dynamic safety grading.',
    'High',
    '**Fusion depth (AC1):** Fused\n\n**Fusion evidence (AC2):**\n- **Data streams:** IoT + smart-sensor project data on a Grade-V rock tunnel section.\n- **Integration mechanism:** the twin fuses sensor data into geometry, physics and knowledge models, and LSTM predicts vault settlement (RMSE 0.0929 mm) graded against the 120 mm design limit.\n- **Why this code:** the prediction output depends on multiple sensor channels simultaneously, so Fused.\n\n**Confidence (AC3):** High - the fused twin construction is explicit; only vault settlement is verified.')

FB[418] = ('Aligned',
    'Real-world records (drawings, photos, investigation data) are mapped into BIM, FE and physics-engine models that reconstruct the collapse in stages, sharing one building frame while each model analyses its own domain.',
    'Medium',
    '**Fusion depth (AC1):** Aligned\n\n**Fusion evidence (AC2):**\n- **Data streams:** design drawings, site records and debris evidence mapped into BIM + FE + physics-engine models (seven-story hotel collapse).\n- **Integration mechanism:** the multistage models are built from and cross-checked against the mapped real-world data in one building frame, revealing welding-induced column buckling; analyses run per model stage.\n- **Why this code:** sources share the building-model frame with per-stage inference, so Aligned.\n\n**Confidence (AC3):** Medium - the forensic mapping is explicit; joint computation across models is not described.')

FB[420] = ('Unclear',
    'A modelling study of prefabricated-construction DTs describes measuring sensors and factor-analysed risk indicators, but the authors state the work lacks a demonstrated live sensor-to-twin data link.',
    'High',
    '**Fusion depth (AC1):** Unclear\n\n**Fusion evidence (AC2):**\n- **Data streams:** displacement/rotation-torque measuring sensors (described) + 130 risk-case records (Cronbach alpha 0.8-0.9, KMO, 65.02% variance).\n- **Integration mechanism:** none demonstrated - sensor monitoring and factor analysis are described side by side without an implemented linkage.\n- **Why this code:** Unclear (rule 1 - no demonstrated integration).\n\n**Confidence (AC3):** High - the missing live link is acknowledged by the authors.')

FB[421] = ('Aligned',
    'BP-network training samples come from FE working-condition simulation, and predicted displacement/stress are verified against on-site measurements, sharing the structural model frame without joint inference.',
    'Medium',
    '**Fusion depth (AC1):** Aligned\n\n**Fusion evidence (AC2):**\n- **Data streams:** FE-derived design/mechanical parameter samples + on-site string-beam verification measurements.\n- **Integration mechanism:** the four-level geometry-physics-behaviour-rule twin links design and mechanical parameters, the BP network is trained on FE samples, and field measurements verify predictions.\n- **Why this code:** measured data are mapped onto the model frame for verification, so Aligned.\n\n**Confidence (AC3):** Medium - the verification linkage is explicit; no joint multi-source inference exists.')

FB[423] = ('Fused',
    'Deformation, seepage, stress and environmental monitoring information are aggregated by a multi-dimensional cloud model with improved CRITIC weighting into one five-grade dam safety status.',
    'High',
    '**Fusion depth (AC1):** Fused\n\n**Fusion evidence (AC2):**\n- **Data streams:** deformation, seepage, stress and environment monitoring of the 131 m Jiangya dam, integrated via extended IFC entities (IfcDSMSystem/IfcMonitoringItem/IfcSensorAssembly).\n- **Integration mechanism:** multi-rule cloud reasoning evaluates monitoring points and the multi-dimensional cloud model with improved CRITIC aggregates them into a five-grade safety status (January-September 2019 continuous evaluation).\n- **Why this code:** the aggregated status depends on all monitoring types simultaneously, so Fused.\n\n**Confidence (AC3):** High - the cloud-model aggregation is explicit.')

FB[426] = ('Fused',
    'Multi-sensor monitoring data and a Blender parametric twin feed an RBF neural network for online stress and deformation prediction, with a motion model for real-time state mapping.',
    'Medium',
    '**Fusion depth (AC1):** Fused\n\n**Fusion evidence (AC2):**\n- **Data streams:** multi-sensor jacking monitoring on a 186.3 m Wuhan building + parametric Blender twin (98.48% auto-generation accuracy).\n- **Integration mechanism:** the RBF network consumes the monitoring channels to predict stress (within 0.1%) and deformation (within 6%) online, and the motion model maps states in real time; five major accidents were avoided.\n- **Why this code:** the prediction output depends on multiple monitoring channels simultaneously, so Fused.\n\n**Confidence (AC3):** Medium - the multi-input ANN is explicit; no autonomous decision-making exists.')

FB[427] = ('Fused',
    'A BP neural network is trained on construction-phase data to diagnose nine fault types (construction joints, grouting, pouring sequence), so diagnosis depends on multiple input channels simultaneously.',
    'Medium',
    '**Fusion depth (AC1):** Fused\n\n**Fusion evidence (AC2):**\n- **Data streams:** construction-phase monitoring data feeding fault diagnosis in the data-management + BIM + Flexsim framework.\n- **Integration mechanism:** the BP network jointly consumes the data channels to diagnose nine fault types (99% average accuracy versus CNN 90.23%, SVM 89.19%, PSO 88.35%), with problems fed back to the BIM model.\n- **Why this code:** a multi-input diagnosis model, so Fused; the wider framework integration remains partly conceptual (Medium).\n\n**Confidence (AC3):** Medium - the BP diagnosis is explicit; stage integration of the framework is not detailed.')

FB[428] = ('Fused',
    'Four IMU sensors and two GNSS receivers are fused in an Euler-based kinematic model refined by social-spider-algorithm optimisation to estimate excavator pose, which then drives BIM-based collision-risk assessment.',
    'High',
    '**Fusion depth (AC1):** Fused\n\n**Fusion evidence (AC2):**\n- **Data streams:** four IMUs + two GNSS receivers on an excavator (bucket-tip error cut from 64.59 to 24.61 mm) + BIM of buried utilities.\n- **Integration mechanism:** the kinematic model fuses IMU and GNSS into one 3D pose estimate, and the pose plus utility BIM compute collision risk with 30/50 cm warning zones in Unity (1760 m Shandong pipe project, 0.05 s sampling).\n- **Why this code:** pose output depends on two fused sensor types and then joins BIM geometry for risk decisions, so Fused.\n\n**Confidence (AC3):** High - the IMU+GNSS fusion and BIM coupling are explicit.')

FB[429] = ('Aligned',
    'TBM excavation data (corrected TPC and VMT positioning, segment traceability, no-drill zones) are automatically mapped into the Dynamo as-built BIM model, sharing one tunnel-model frame with per-data processing.',
    'Medium',
    '**Fusion depth (AC1):** Aligned\n\n**Fusion evidence (AC2):**\n- **Data streams:** TPC/VMT TBM positioning, segment manufacturing traceability and no-drill-zone data (2.4 km French tunnelling project).\n- **Integration mechanism:** the computational design algorithm places segments automatically into the BIM as-built model (ring modelling 15-20 min down to 1 min), linking each data stream to model elements; lean analyses run on the model.\n- **Why this code:** streams share the BIM element frame with per-stream processing, so Aligned.\n\n**Confidence (AC3):** Medium - the automatic placement is explicit; joint inference beyond model assembly is not described.')
