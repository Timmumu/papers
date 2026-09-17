# -*- coding: utf-8 -*-
"""Fusion-depth batch E2."""
FB = {}

FB[357] = ('Fused',
    'YOLOv4-tiny + DeepSORT detections are anchored into the 4D BIM virtual construction site, so danger-zone computation and HoloLens overlays depend on live vision data and BIM geometry simultaneously.',
    'High',
    '**Fusion depth (AC1):** Fused\n\n**Fusion evidence (AC2):**\n- **Data streams:** CCTV video detections (YOLOv4-tiny + DeepSORT) + 4D BIM geometry/state (three quasi-on-site tests).\n- **Integration mechanism:** detected objects are mapped into the BIM-anchored virtual construction site which computes red/yellow/blue danger zones overlaid in HoloLens 2 (96.1% accuracy, 424 ms delay, 11.47 cm alignment error).\n- **Why this code:** the danger-zone output depends on live detections and BIM geometry simultaneously, so Fused.\n\n**Confidence (AC3):** High - the BIM-anchored overlay computation is explicit.')

FB[358] = ('Fused',
    'A BO-GCN-BiLSTM predictor with SHAP interpretation jointly consumes multi-parameter slurry-shield construction data and iteratively keeps slurry pressure within the warning range via bidirectional IoT/5G links.',
    'High',
    '**Fusion depth (AC1):** Fused\n\n**Fusion evidence (AC2):**\n- **Data streams:** multi-parameter slurry-shield construction data (Wuhan Metro Line 12 Yangtze tunnel, six geological types).\n- **Integration mechanism:** the GCN-BiLSTM model fuses the parameter streams to predict tunnel-face stability (average R2 0.935, RMSE 0.162, best of six baselines), and the platform feeds pressure-control guidance back through bidirectional links.\n- **Why this code:** the prediction output depends on multiple data channels simultaneously and feeds a control loop, so Fused.\n\n**Confidence (AC3):** High - the multi-input GCN-BiLSTM is explicit.')

FB[359] = ('Fused',
    'Bayesian-optimised CatBoost maps 19 construction parameters to six attitude targets as one multi-input model, with SHAP identifying dominant factors and MOEAD multi-objective optimisation on the predictions.',
    'High',
    '**Fusion depth (AC1):** Fused\n\n**Fusion evidence (AC2):**\n- **Data streams:** 19 construction-parameter streams (Yangtze River slurry shield, three soils).\n- **Integration mechanism:** CatBoost jointly consumes the parameters to predict six attitude targets (R2 above 0.9), SHAP ranks push-group thrust as dominant, and MOEAD optimisation improves attitude by up to 23.436%.\n- **Why this code:** a multi-input model whose output depends on many parameter streams simultaneously, so Fused.\n\n**Confidence (AC3):** High - the CatBoost input structure is explicit.')

FB[360] = ('Aligned',
    'Multi-channel surveillance video is fused into the BIM static scene through 3D registration and projection, and multi-source IoT sensing data are integrated into the same scene for tunnel operations management.',
    'High',
    '**Fusion depth (AC1):** Aligned\n\n**Fusion evidence (AC2):**\n- **Data streams:** multi-channel surveillance video + BIM static scene + multi-source IoT sensing data.\n- **Integration mechanism:** 3D registration/projection places video streams into the shared 3D scene (virtual-real fusion), while traffic-flow, accident-rescue and facility-management services analyse per source.\n- **Why this code:** streams share one registered scene frame with per-source services, so Aligned.\n\n**Confidence (AC3):** High - the 3D registration mechanism is explicit.')

FB[361] = ('Aligned',
    'Twenty-five surveillance-video channels are 3D-registered into the drone/BIM waterway scene, and multi-source IoT data (AIS, bayonet) are integrated into the same scene for water-safety management.',
    'High',
    '**Fusion depth (AC1):** Aligned\n\n**Fusion evidence (AC2):**\n- **Data streams:** 25 surveillance-video channels + drone tilt-photography/BIM scene + AIS and smart-bayonet IoT data (Changhu-Shen Line).\n- **Integration mechanism:** 3D registration renders the video into the shared scene with 2D/3D linkage, and IoT sources are displayed for facility monitoring, evidence collection and emergency response; online-data-driven scene iteration is future work.\n- **Why this code:** streams share the registered scene frame while analysis stays per source, so Aligned.\n\n**Confidence (AC3):** High - the video 3D-registration mechanism is explicit.')

FB[366] = ('Aligned',
    'The LoRa temperature-sensor array is mapped onto the spatiotemporal building-fire field learned by ADLSTM-Fire, so measured readings and the model field share one spatiotemporal frame while inference runs in the model.',
    'Medium',
    '**Fusion depth (AC1):** Aligned\n\n**Fusion evidence (AC2):**\n- **Data streams:** LoRa wireless thermometry sensor-array readings + CFD-benchmark temperature fields.\n- **Integration mechanism:** ADLSTM-Fire transforms discrete readings into the high-dimensional spatiotemporal field (93% reconstruction, 92% 60-s-ahead forecast R2), validated against CFD and full-scale fire experiments.\n- **Why this code:** one measured stream is registered onto the learned field model, so Aligned (single measured type; the CFD fields are model-generated).\n\n**Confidence (AC3):** Medium - the array-to-field mapping is explicit; fusion depth beyond registration is limited.')

FB[368] = ('Aligned',
    'Wireless time-synchronised smart-sensor vibration data are mapped onto the cloud MDOF flexural-shear twin updated by SSI-COV and PSO, which then localises vibration sources by spectrum matching.',
    'Medium',
    '**Fusion depth (AC1):** Aligned\n\n**Fusion evidence (AC2):**\n- **Data streams:** WTSS vibration records (LoRa synchronisation under 20 microseconds) + edge STFT anomaly features.\n- **Integration mechanism:** sensor data update the cloud twin, and source localisation compares measured spectra against twin feature amplitudes (zonal, about one-floor error) on a 17-story building under 82.9 N excitation.\n- **Why this code:** one measured stream is registered onto the model frame for matching, so Aligned.\n\n**Confidence (AC3):** Medium - the SSI-COV/PSO updating and matching are explicit; only one sensor modality exists.')

FB[372] = ('Fused',
    'BIM and the oblique-photogrammetry real-scene 3D model are fused by rigid-body SVD registration plus JSON semantic mapping, and 60 sensors (vibration, displacement, strain, temperature) are integrated into the fused model.',
    'High',
    '**Fusion depth (AC1):** Fused\n\n**Fusion evidence (AC2):**\n- **Data streams:** IFC BIM sub-models + real-scene 3D Tiles photogrammetry model + 60 sensor series (Nanjing Museum Old Hall).\n- **Integration mechanism:** rigid-body SVD registration and JSON semantic mapping fuse BIM and reality-mesh into one model, into which the sensor data are integrated for Cesium-based monitoring visualisation.\n- **Why this code:** the fused BIM-mesh product depends on two geometry sources simultaneously and then absorbs sensor data, so Fused.\n\n**Confidence (AC3):** High - the SVD registration + JSON mapping fusion is explicit.')

FB[376] = ('Fused',
    'Real-time worker trajectories, postures and interactions are integrated into the BIM-anchored Unreal twin, and a non-autoregressive transformer jointly predicts future movements and collision near-misses.',
    'High',
    '**Fusion depth (AC1):** Fused\n\n**Fusion evidence (AC2):**\n- **Data streams:** binocular-camera detections (YOLOv5 + DeepSORT + SGM stereo) + BIM-anchored 3D scene (one-month Foshan steel-hoisting pilot).\n- **Integration mechanism:** trajectories and postures are mapped into the twin with protective envelopes, and the transformer predicts future sequences whose collision checks detect near-misses (93.80% precision, 96.64% recall, 1181 of 1300).\n- **Why this code:** near-miss output depends on live perception and scene geometry simultaneously, so Fused.\n\n**Confidence (AC3):** High - the perception-to-twin-to-prediction chain is explicit.')

FB[377] = ('Fused',
    'Worker trajectories (YOLOv5/SGBM/DeepSORT/MediaPipe) and BIM scene geometry jointly feed a non-autoregressive transformer plus inverse-kinematics reconstruction for 3D near-miss prediction.',
    'High',
    '**Fusion depth (AC1):** Fused\n\n**Fusion evidence (AC2):**\n- **Data streams:** camera-based trajectories and postures + BIM-anchored Unreal scene (forklift, floor-opening, material-lifting zones).\n- **Integration mechanism:** the transformer forecasts trajectories (ADE 0.134) and postures (ADE 0.501), an LBFGS inverse-kinematics solver reconstructs them in the twin, and collision checks predict near-misses (93.32% precision, 96.08% recall).\n- **Why this code:** prediction output depends on perception data and scene geometry simultaneously, so Fused.\n\n**Confidence (AC3):** High - the pipeline is explicit.')

FB[379] = ('Fused',
    'SHAP-selected multi-parameter shield monitoring feeds the ABC-NSGA-III hybrid optimiser, whose six-objective output is fed back into the DT to guide tunnelling parameter adjustment.',
    'Medium',
    '**Fusion depth (AC1):** Fused\n\n**Fusion evidence (AC2):**\n- **Data streams:** multi-parameter shield-tunnelling monitoring (100 rings, Shanghai Airport Link Line).\n- **Integration mechanism:** SHAP identifies 16 key parameters, ABC-NSGA-III jointly optimises six attitude objectives (32.02% overall optimisation, 2.21-17.13% deviation reduction), and results feed back to guide operations.\n- **Why this code:** the optimisation output depends on multiple monitoring channels simultaneously, so Fused; operators still filter the recommendations (Medium).\n\n**Confidence (AC3):** Medium - the multi-objective optimisation is explicit; the loop is human-machine collaborative.')

FB[382] = ('Aligned',
    'Vibration, tilt, light, air-quality and water-detection sensors are synchronised to a LOD 400 BIM model via Autodesk Forge API and WebSockets, with two-tier anomaly detection running per channel.',
    'High',
    '**Fusion depth (AC1):** Aligned\n\n**Fusion evidence (AC2):**\n- **Data streams:** five IoT sensor types on a solar-powered noise-barrier tunnel (Wansan Tunnel, 17-day demonstration).\n- **Integration mechanism:** Forge API + WebSockets attach the sensor streams to BIM elements for dashboard visualisation; device alerts and post-processed trend analysis act per channel.\n- **Why this code:** streams share the BIM asset frame with per-channel inference, so Aligned.\n\n**Confidence (AC3):** High - the Forge/WebSocket synchronisation is explicit.')

FB[386] = ('Aligned',
    'Multi-source sensors (safety, environmental, construction, auxiliary) are integrated into an OpenGL virtual tunnel with four-level early warnings, linked to the tunnel model while warnings fire per parameter.',
    'High',
    '**Fusion depth (AC1):** Aligned\n\n**Fusion evidence (AC2):**\n- **Data streams:** harmful-gas, meteorological, deformation and personnel-positioning sensors (Dongtianshan Tunnel, 11.7 km).\n- **Integration mechanism:** multifunctional WSN base stations mirror the streams into the virtual tunnel, and the four-level warning/emergency mechanism acts on thresholds, successfully predicting a K0+668 face collapse.\n- **Why this code:** streams share the tunnel-model frame while warnings run per parameter, so Aligned.\n\n**Confidence (AC3):** High - the virtual-tunnel mapping is explicit.')

FB[388] = ('SINGLE',
    'Only electrical-resistivity-tomography data drive the TG-FNO forward model and leakage inversion; all validation uses synthetic ERT datasets.',
    'High',
    '**Fusion depth (AC1):** SINGLE\n\n**Fusion evidence (AC2):**\n- **Data streams:** ERT potential-field measurements (synthetic 2D datasets with single circular anomalies).\n- **Integration mechanism:** none - one modality feeds the Fourier neural operator (345x forward speedup, 99.7% inversion success, robust to 20% noise / 50% loss).\n- **Why this code:** SINGLE (AC=Single).\n\n**Confidence (AC3):** High.')

FB[389] = ('Aligned',
    'UAV photogrammetry models, radar obstacle detection, RTK/IMU attitude, force feedback and eye-tracking are all shown in one geolocated 5G teleoperation platform, sharing the scene frame while each stage processes its own data.',
    'High',
    '**Fusion depth (AC1):** Aligned\n\n**Fusion evidence (AC2):**\n- **Data streams:** UAV tilt-photography 3D model (0.6 cm error), video, radar, RTK/IMU attitude, force/sound feedback, eye-tracking (Hulunbuir open-pit bulldozer teleoperation).\n- **Integration mechanism:** the real-time platform displays the streams in one georeferenced scene for the human operator; anterior-time edge detection (0.923 precision) and blade-trajectory generation run as separate stages.\n- **Why this code:** streams share the geolocated scene frame while processing stays per stage, so Aligned.\n\n**Confidence (AC3):** High - the multi-stage platform structure is explicit.')
