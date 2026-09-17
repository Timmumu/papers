# -*- coding: utf-8 -*-
"""Fusion-depth batch C."""
FB = {}

FB[158] = ('SINGLE',
    'Only high-precision LiDAR scans of the underground utility tunnel feed the Unreal digital twin; the 4-DoF motion platform adds haptic actuation, not a second data type.',
    'High',
    '**Fusion depth (AC1):** SINGLE\n\n**Fusion evidence (AC2):**\n- **Data streams:** one-time LiDAR-scanned UUT geometry.\n- **Integration mechanism:** none - visual (HMD) and kinematic (motion platform) feedback act on the single reconstructed model; SSQ tests with 17 participants evaluate cybersickness.\n- **Why this code:** SINGLE (AC=Single).\n\n**Confidence (AC3):** High.')

FB[163] = ('Fused',
    'Advanced sensor packages (thermal, RGB, UV, motion) plus LiDAR-derived 3D models are combined with stated real-time data fusion for fire/anomaly detection in two 17-month deployments.',
    'High',
    '**Fusion depth (AC1):** Fused\n\n**Fusion evidence (AC2):**\n- **Data streams:** Raspberry Pi thermal camera, RGB, UV and motion sensors; LiDAR-derived dimensionally accurate Unity/WebGL models; Azure dashboards.\n- **Integration mechanism:** the paper states real-time data fusion of the sensor streams for normal-operational-signature analysis, fire localisation without triangulation and intensity evaluation; a candle flame was detected in under one second.\n- **Why this code:** detection output depends on multiple fused sensor types simultaneously, so Fused; implemented in real buildings.\n\n**Confidence (AC3):** High - real-time data fusion is the paper stated mechanism.')

FB[165] = ('SINGLE',
    'Only vibration recordings (random-vibration FRF on a shaking-table pipe) drive the model-updating and real-time estimation; no second measured data type exists.',
    'High',
    '**Fusion depth (AC1):** SINGLE\n\n**Fusion evidence (AC2):**\n- **Data streams:** FRF/vibration measurements from the MECOS benchmark pipe on a shaking table.\n- **Integration mechanism:** none - Nelder-Mead updating calibrates the FE model, and the Craig-Bampton ROM (62 DOFs, about 450x faster) estimates responses; RMSE 0.0103/0.0266 versus sensors.\n- **Why this code:** SINGLE (AC=Single).\n\n**Confidence (AC3):** High.')

FB[167] = ('Fused',
    'Weather-station variables (temperature, humidity, irradiance, wind) and the UAV-photogrammetry geometric site twin are jointly consumed by SOLWEIG microclimate simulation to produce site-wide heat-risk maps.',
    'High',
    '**Fusion depth (AC1):** Fused\n\n**Fusion evidence (AC2):**\n- **Data streams:** on-site weather station (temperature, humidity, irradiance, wind) + UAV-photogrammetry geometric twin (shadow, sky-view factor, surface-material maps).\n- **Integration mechanism:** SOLWEIG simulation combines the weather streams with the geometric model into spatio-temporal heat-risk maps (mean radiant temperature RMSE 4.21 C, R2 0.93 versus 11.80 C / 0.44 for black-globe).\n- **Why this code:** the risk-map output depends on several weather variables and the geometric twin simultaneously, so Fused.\n\n**Confidence (AC3):** High - the SOLWEIG coupling is explicit.')

FB[168] = ('Fused',
    'Live sensor data are compared against a pre-simulated virtual-sensor fire knowledge base via online DTW similarity measurement, so fire recognition depends on real and simulated data streams simultaneously.',
    'Medium',
    '**Fusion depth (AC1):** Fused\n\n**Fusion evidence (AC2):**\n- **Data streams:** live building-state sensor data + pre-simulated fire-scenario virtual-sensor data.\n- **Integration mechanism:** online DTW with parallel processing matches real against simulated series for fire recognition in 0.88 s, followed by ARET/RRET/safety-margin risk assessment per zone.\n- **Why this code:** recognition output depends on both streams simultaneously, so Fused; validated through simulation of an underground mall (Medium).\n\n**Confidence (AC3):** Medium - the DTW mechanism is explicit, but validation is simulation-only.')

FB[176] = ('Fused',
    'Low-fidelity and high-fidelity RBF surrogates are fused with live inclination and strain sensor inputs (18 test points) to predict stress and deformation in 0.035 s with Gaussian uncertainty quantification.',
    'High',
    '**Fusion depth (AC1):** Fused\n\n**Fusion evidence (AC2):**\n- **Data streams:** large low-fidelity mechanistic data + few high-fidelity statistical samples + live inclination/strain sensors (140 repeated lifts).\n- **Integration mechanism:** the multi-fidelity surrogate fuses the two fidelity levels and consumes live sensor inputs, predicting stress/deformation with R2 above 0.98 and quantifying sensor uncertainty, rendered in WebGL.\n- **Why this code:** a multi-input surrogate whose output depends on several data types simultaneously, so Fused.\n\n**Confidence (AC3):** High - the multi-fidelity fusion is explicit.')

FB[178] = ('Aligned',
    'BIM-guided UAV image selection, GrabCut pixel-to-component assignment (IoU 0.80-0.90) and pre/post 3D point-cloud change detection all operate on one shared BIM reference frame, with per-stage analyses.',
    'High',
    '**Fusion depth (AC1):** Aligned\n\n**Fusion evidence (AC2):**\n- **Data streams:** UAV imagery (989 images, Turner Hall) + pre/post 3D point clouds + BIM geometry.\n- **Integration mechanism:** the BIM is the shared frame - it guides image selection and receives pixel labels per component, while 3D change detection (std-dev indicator, threshold 0.010) runs as a separate stage.\n- **Why this code:** data types are linked through the BIM frame but inference is per stage and per type, so Aligned.\n\n**Confidence (AC3):** High - the BIM-referenced pipeline is explicit.')

FB[181] = ('Fused',
    'SfM photogrammetry and the building DT/BIM geometry are jointly used to generate occlusion-free metric orthophotos, on which deep-learning semantic segmentation then runs.',
    'Medium',
    '**Fusion depth (AC1):** Fused\n\n**Fusion evidence (AC2):**\n- **Data streams:** SfM reconstruction imagery + building DT/BIM model geometry.\n- **Integration mechanism:** orthophoto generation projects imagery onto the model geometry, so the output depends on both simultaneously; PointRend segmentation reaches 94.22 mIoU on Duff House, St Marys Church and a Stirling house.\n- **Why this code:** the orthophoto is a joint product of imagery and model geometry, so Fused.\n\n**Confidence (AC3):** Medium - the projection mechanism is clear, though one could argue the streams are merely registered (Aligned); Fused retained because the orthophoto output itself is the joint computation.')

FB[183] = ('SINGLE',
    'Only FARO Focus-3D laser-scanned point clouds feed the geometric DT pipeline; the Leica total-station targets serve purely as a validation benchmark, and 3D-sonar fusion is stated as future work.',
    'High',
    '**Fusion depth (AC1):** SINGLE\n\n**Fusion evidence (AC2):**\n- **Data streams:** laser-scanned point clouds (FARO Focus-3D); twelve Leica total-station target points used only to benchmark accuracy; image-based methods appear solely in the related-work discussion.\n- **Integration mechanism:** none - the pipeline (density-based clustering, fitting, region growing) processes one data type; mean error under 1 mm versus total station.\n- **Why this code:** exactly one measured data type is used, so SINGLE. Note: column AC lists Multi because the total-station validation was counted there; under the fusion-depth rules a validation benchmark is not a second data type.\n\n**Confidence (AC3):** High - the single-modality pipeline and validation-only role of the total station are explicit in the full text.')

FB[185] = ('Fused',
    'The residual between the physical SCADA stream (793 dimensions) and the virtual-sensor (DBN) output is the diagnostic signal, so fault diagnosis depends on both streams simultaneously.',
    'Medium',
    '**Fusion depth (AC1):** Fused\n\n**Fusion evidence (AC2):**\n- **Data streams:** real SCADA telemetry (793 dimensions, Lasso/random-forest feature selection) + DBN virtual-sensor predictions (R2 0.987, best of LSTM/XGBoost/SVR).\n- **Integration mechanism:** the residual between physical and virtual sensor is computed continuously and used within a 99% confidence interval to diagnose torsional-vibration faults and pre-warn operators.\n- **Why this code:** the diagnostic output depends on measured and predicted streams simultaneously, so Fused (virtual-real residual comparison).\n\n**Confidence (AC3):** Medium - the residual mechanism is explicit; both streams originate from one SCADA acquisition system.')

FB[194] = ('Fused',
    'Previous-stage FEM results, construction-progress data and temperature data are jointly interpolated with multi-stage laser scans to build one continuous dynamic IFC model between scan stages.',
    'Medium',
    '**Fusion depth (AC1):** Fused\n\n**Fusion evidence (AC2):**\n- **Data streams:** multi-stage laser scans (six scans), previous-stage ABAQUS FEM results, construction progress and temperature data.\n- **Integration mechanism:** the three information sources are combined to fill gaps between scan stages, producing a continuous dynamic parametric IFC/BIM model (15-20 mm BIM-vs-point-cloud accuracy; next-stage shape/force prediction deviations 1.3%/1.5%).\n- **Why this code:** the interpolated model depends on several data types simultaneously, so Fused.\n\n**Confidence (AC3):** Medium - the gap-filling combination is explicit, but temperature/progress data are auxiliary inputs.')

FB[195] = ('Fused',
    'Depth-camera 32-point skeletons, LiDAR/URDF robot models and ArUco/QR material tags are combined into geometric-solid virtual representations on which separation-distance and protective-separation-distance computation runs jointly.',
    'High',
    '**Fusion depth (AC1):** Fused\n\n**Fusion evidence (AC2):**\n- **Data streams:** Azure Kinect depth-camera skeletons (14 capsule representations), LiDAR + URDF/encoder robot state, ArUco/QR tags with IFC data for materials.\n- **Integration mechanism:** the three streams are combined into one geometric-solid twin, and SD/PSD computation (ISO 15066/13855) over the fused scene triggers emergency stops at 9.8 FPS, 0.177 s reaction, 0.09 m error.\n- **Why this code:** the safety-decision output depends on all three data types simultaneously, so Fused.\n\n**Confidence (AC3):** High - the multi-stream twin composition is explicit.')

FB[196] = ('Aligned',
    'CO, temperature and humidity readings are dynamically mapped onto the corresponding spatial components of a 3D BIM model, linking each sensor channel to BIM elements while actuation stays in the WSN control node.',
    'High',
    '**Fusion depth (AC1):** Aligned\n\n**Fusion evidence (AC2):**\n- **Data streams:** Zigbee WSN nodes (MQ-7 CO, DHT-11 temperature/humidity) in a Taipei parking garage.\n- **Integration mechanism:** readings map onto matching BIM components for real-time colour display; the safety loop (ventilator + alarm, 1-2 s) is executed directly by the WSN control node, bypassing the twin.\n- **Why this code:** sensor channels share the BIM asset frame but inference/actuation stays per stream, so Aligned.\n\n**Confidence (AC3):** High - the BIM component mapping is explicit.')

FB[203] = ('Fused',
    'RFID, IMU, crane black-box and LoRa sensing data jointly feed a DEMATEL-ISM hierarchical risk model and Bayesian-network reasoning that computes key degrees of indirect inducement factors.',
    'Medium',
    '**Fusion depth (AC1):** Fused\n\n**Fusion evidence (AC2):**\n- **Data streams:** RFID, IMU, crane black-box and LoRa sensing on a 71,172 m2 Tianjin prefabricated project.\n- **Integration mechanism:** the multi-source sensing streams are combined in the DT, and the DEMATEL-ISM + BN model reasons jointly over them to compute risk-control priorities.\n- **Why this code:** the BN risk output depends on several sensor streams simultaneously, so Fused; training samples are limited and expert-copied (Medium).\n\n**Confidence (AC3):** Medium - the BN reasoning is explicit, but data provenance is limited (three time points, expert-copied).')

FB[204] = ('Fused',
    'Twenty-six days of integrated multi-source site records are jointly mined by Apriori association rules and complex-network analysis to identify risk-factor coupling relationships.',
    'Medium',
    '**Fusion depth (AC1):** Fused\n\n**Fusion evidence (AC2):**\n- **Data streams:** integrated IoT + BIM hoisting records (26 days) on a large prefabricated project.\n- **Integration mechanism:** Apriori mining (support 0.5, confidence 0.6) over the combined records plus weighted complex-network degree centrality produce the coupled risk-factor structure shown in the DT for guidance.\n- **Why this code:** the mined coupling structure depends on multiple data sources simultaneously, so Fused.\n\n**Confidence (AC3):** Medium - joint mining is explicit; validation data samples are acknowledged as insufficient.')

FB[205] = ('Fused',
    'Sensor strain measurements correct the twin (cutting cable-force errors to within 3%) and a DBN predicts cable forces, so the safety-evaluation output depends on measured and model streams simultaneously.',
    'Medium',
    '**Fusion depth (AC1):** Fused\n\n**Fusion evidence (AC2):**\n- **Data streams:** strain-sensor measurements on a 1:10 wheel-spoke cable truss + twin/DBN model outputs.\n- **Integration mechanism:** twin correction against sensor strain is the joint step (virtual-real fusion), and DBN-based safety levels guide maintenance under quarter-span live load.\n- **Why this code:** the corrected twin output depends on measured and modelled data simultaneously, so Fused; 1:10 scale test only (Medium).\n\n**Confidence (AC3):** Medium - the correction mechanism is explicit, but validation is a scale model.')

FB[207] = ('Aligned',
    'BIM, 3D laser scanning and ANSYS/LS-DYNA share one high-fidelity twin geometry, while the improved BP predictor is trained offline on FE working-condition samples and field data serve verification only.',
    'Medium',
    '**Fusion depth (AC1):** Aligned\n\n**Fusion evidence (AC2):**\n- **Data streams:** 3D laser-scanned geometry + BIM + FE simulation samples (219 drop-hammer conditions).\n- **Integration mechanism:** scanning and BIM are merged into one high-fidelity model frame; the LM-BP network (14 inputs, 5 outputs) is trained on FE data alone, and experimental results only verify predictions.\n- **Why this code:** geometry sources share the twin frame while inference runs per type, so Aligned.\n\n**Confidence (AC3):** Medium - the shared-frame geometry merging is clear; no joint multi-source inference exists.')

FB[208] = ('Fused',
    'LoRa IoT terminals (oxygen, CO, smoke, temperature, door/window sensors, camera people-counting) are jointly classified by SVM models into fire, illegal-intrusion and overcrowding dangers with danger-level grading.',
    'High',
    '**Fusion depth (AC1):** Fused\n\n**Fusion evidence (AC2):**\n- **Data streams:** oxygen, CO, smoke, temperature, door/window sensors plus camera people-counting in a Beijing Winter Olympics stadium room.\n- **Integration mechanism:** the multi-channel sensor data are fed together into SVM classifiers (97.57-100% danger-class accuracy; 96.2% level accuracy, R2 above 0.89) displayed on the WebGL BIM twin.\n- **Why this code:** the classifiers consume several sensor types simultaneously, so Fused.\n\n**Confidence (AC3):** High - the multi-input SVM pipeline is explicit.')

FB[210] = ('Fused',
    'Hydraulic-jack, temperature and stress sensor readings from the jacking process are fed together into an XGBoost model (with FE-guided sensor placement) predicting key-bar stress with 98% accuracy.',
    'High',
    '**Fusion depth (AC1):** Fused\n\n**Fusion evidence (AC2):**\n- **Data streams:** hydraulic jack data, temperature and stress sensors on twelve jacks and key bars; Midas/Gen life-and-death element analysis for placement.\n- **Integration mechanism:** the multi-sensor channels jointly feed XGBoost (validation R2 0.9919), outperforming GA-BPNN and random forest on an airport terminal steel-roof jacking project.\n- **Why this code:** a multi-input model whose output depends on several sensor types simultaneously, so Fused.\n\n**Confidence (AC3):** High - the XGBoost input structure is explicit.')

FB[211] = ('Fused',
    'Multi-channel overall-jacking monitoring data are jointly analysed by a random-forest model that ranks jacking height difference and jacking speed as the dominant factors for structural stress.',
    'High',
    '**Fusion depth (AC1):** Fused\n\n**Fusion evidence (AC2):**\n- **Data streams:** geometric, FE, behavioural and rule model outputs plus real-time jacking monitoring channels on an airport project.\n- **Integration mechanism:** random forest jointly consumes the monitoring channels to compute feature importance, driving rule-based alarms and shutdown commands in the twin.\n- **Why this code:** the importance-ranking model depends on multiple data channels simultaneously, so Fused.\n\n**Confidence (AC3):** High - the random-forest analysis is explicit.')

FB[219] = ('Aligned',
    'Real-world topography, infrastructure, traffic, transit and disaster data are manually integrated into one georeferenced Cities:Skylines simulation scene, with no automated calibration or live link.',
    'Medium',
    '**Fusion depth (AC1):** Aligned\n\n**Fusion evidence (AC2):**\n- **Data streams:** Brevard County topography, infrastructure, economic, traffic, transit and disaster statistics; 120,000 simulated agents.\n- **Integration mechanism:** the data are imported into one geospatially referenced simulation scene (shared spatial frame), but the paper states the integration process is manual and intermittent (human-based data flow).\n- **Why this code:** sources share a spatial frame while processing stays per layer, so Aligned; torn with Co-present, Aligned was retained because the scene itself is spatially registered.\n\n**Confidence (AC3):** Medium - manual/internittent integration is explicit; the geospatial frame is real but weakly maintained.')

FB[221] = ('SINGLE',
    'Only Hong Kong territory-wide LiDAR survey data (up to 0.1 m resolution) are used; the DrainNet input images and the slope topography are both derived products of that single survey.',
    'High',
    '**Fusion depth (AC1):** SINGLE\n\n**Fusion evidence (AC2):**\n- **Data streams:** LiDAR survey data only - DrainNet delineates channels in images derived from the LiDAR dataset (1226 annotated images), and topography comes from the same survey.\n- **Integration mechanism:** none across independent data types - the CNN delineation and parametric BIM reconstruction are two processing steps over one source modality.\n- **Why this code:** exactly one measured data type is used, so SINGLE. Note: column AC lists Multi because the derived image and topography products were counted separately; under the fusion-depth rules derived products of one survey are not distinct data types.\n\n**Confidence (AC3):** High - the single LiDAR source is stated explicitly (the paper contrasts it with traditional imagery).')
