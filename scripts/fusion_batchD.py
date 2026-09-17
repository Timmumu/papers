# -*- coding: utf-8 -*-
"""Fusion-depth batch D."""
FB = {}

FB[225] = ('SINGLE',
    'Only visual-inspection campaign data (classified unit cells with photo links) feed the 2D grid-to-TSI mapping; the stochastic limit-analysis models are mathematical tools, not a second data type.',
    'High',
    '**Fusion depth (AC1):** SINGLE\n\n**Fusion evidence (AC2):**\n- **Data streams:** visual inspection classifications of tunnel TL 01 mapped onto a 2D grid of unit cells with online photo links (EleFront).\n- **Integration mechanism:** none across data types - the grid is converted to tunnel serviceability index values and inverse exponential limit analysis; images serve as documentation attachments.\n- **Why this code:** one measured data type (inspection records), so SINGLE. Note: column AC lists Multi because inspection photos and classifications were counted separately; under the fusion-depth rules they are one inspection-records modality.\n\n**Confidence (AC3):** High - the inspection-grid pipeline is explicit in the full text.')

FB[226] = ('SINGLE',
    'Only Faro Focus 3D X330 point-cloud data feed the procedural modelling pipeline; parametric/procedural modelling are model-generation steps, not additional measured data types.',
    'High',
    '**Fusion depth (AC1):** SINGLE\n\n**Fusion evidence (AC2):**\n- **Data streams:** laser-scanned point clouds (Faro Focus 3D X330, Coastal Tunnel) with photographic colour only as texture.\n- **Integration mechanism:** none across data types - cleaning, decimation, Poisson reconstruction, MDQ-indexed meshing and the procedural inspection grid all operate on the point cloud.\n- **Why this code:** one measured data type, so SINGLE. Note: column AC lists Multi because modelling stages were counted; under the fusion-depth rules model-generation steps are not distinct data types.\n\n**Confidence (AC3):** High - the single PCD source is explicit in the full text.')

FB[235] = ('Aligned',
    'BIM and GIS spatial/functional data are integrated into one centralized relational database with tailor-made space encoding, sharing a spatial frame, while fire-evacuation crowd simulation runs as a separate benchmark.',
    'High',
    '**Fusion depth (AC1):** Aligned\n\n**Fusion evidence (AC2):**\n- **Data streams:** BIM spatial data + GIS/functional data from several directorates (two University of Turin demonstrators).\n- **Integration mechanism:** the centralised relational database with space encoding provides the shared frame for the 3D map and dashboards; Pathfinder-style crowd simulation assesses evacuation safety separately.\n- **Why this code:** data types share one spatial frame with per-type services, so Aligned.\n\n**Confidence (AC3):** High - the centralised DB integration is explicit.')

FB[238] = ('Fused',
    'Local SMAC-tuned models from six Raspberry Pi edge nodes are fused by performance-weighted one-shot aggregation into a global federated model, with the DT layer orchestrating nodes and topologies.',
    'High',
    '**Fusion depth (AC1):** Fused\n\n**Fusion evidence (AC2):**\n- **Data streams:** local worker-safety (and MNIST) datasets distributed across six Raspberry Pi nodes.\n- **Integration mechanism:** performance-weighted one-shot aggregation fuses the local models into one global model (worker-safety convergence rounds 42 to 18, MAE 0.058 to 0.042), while the DT layer provides observability and orchestration.\n- **Why this code:** the global model is a joint fusion of multi-node data through aggregation, so Fused.\n\n**Confidence (AC3):** High - the aggregation mechanism is explicit.')

FB[239] = ('Fused',
    'Worker-status, weather and structural-parameter records (50,000 samples) are jointly trained into one DNN via federated learning with dynamic node selection, and the DT visualises the fused global model.',
    'High',
    '**Fusion depth (AC1):** Fused\n\n**Fusion evidence (AC2):**\n- **Data streams:** worker status, weather and structural-parameter records across six Raspberry Pi edge nodes.\n- **Integration mechanism:** normal-distribution-based dynamic node selection improves FedAVG aggregation of the multi-domain records into one safety-prediction model (R2 0.978 IID / 0.965 non-IID, 0.551 s inference).\n- **Why this code:** one model trained on multiple data domains simultaneously, so Fused.\n\n**Confidence (AC3):** High - the FL aggregation over multi-domain records is explicit.')

FB[247] = ('SINGLE',
    'Only record-based data (83 professional questionnaires and longitudinal maintenance records) calibrate the Quality-Sustainability Integration Index; the BIM-based LCA is model-generated.',
    'High',
    '**Fusion depth (AC1):** SINGLE\n\n**Fusion evidence (AC2):**\n- **Data streams:** survey responses (83 professionals) + maintenance logs (14 Lagos buildings, 847 repair entries) as one records modality.\n- **Integration mechanism:** none across modalities - QSII combines severity, carbon and repair frequency within the records; the BIM-LCA and conceptual DT prototype are model-generated outputs.\n- **Why this code:** one measured data type, so SINGLE (AC=Single).\n\n**Confidence (AC3):** High.')

FB[253] = ('Unclear',
    'A systematic review of 52 papers on ontology/semantic-web integration in BIM-DT construction management; no system is built or tested, so no integration mechanism can be coded.',
    'High',
    '**Fusion depth (AC1):** Unclear\n\n**Fusion evidence (AC2):**\n- **Data streams:** reviewed use cases only (safety management, compliance checking, site monitoring, 4D BIM).\n- **Integration mechanism:** none implemented - the review analyses how semantic tools serve each use case.\n- **Why this code:** Unclear (rule 2).\n\n**Confidence (AC3):** High.')

FB[254] = ('Fused',
    'Multiview UAV imagery, SfM 3D reconstruction and a MobileNetV2-based CNN are combined into one semantic twin in which anomalies are classified and embedded as GIS-compatible damage attributes.',
    'High',
    '**Fusion depth (AC1):** Fused\n\n**Fusion evidence (AC2):**\n- **Data streams:** multiview UAV imagery + SfM 3D reconstruction + CNN classifications (macro-F1 0.81 on 2000 annotated images).\n- **Integration mechanism:** the CNN runs on the reconstructed imagery and anomalies are embedded into the 3D twin linked with maintenance records, cutting inspection time from 3.5 to 1.3 hours on a Taiwan SWC structure.\n- **Why this code:** the semantic-twin output depends on imagery, geometry and model inference simultaneously, so Fused.\n\n**Confidence (AC3):** High - the embedding pipeline is explicit.')

FB[255] = ('Fused',
    'Laser scanning and photogrammetry are fused, and Mask-RCNN detections are mapped into point clouds via COLMAP, ICP alignment and voxel raycasting to enrich the geometric twin with semantic and text information.',
    'High',
    '**Fusion depth (AC1):** Fused\n\n**Fusion evidence (AC2):**\n- **Data streams:** laser-scanned point clouds + photogrammetric imagery + OCR-extracted object IDs.\n- **Integration mechanism:** detections are projected into the point cloud through COLMAP pose estimation, ICP alignment and voxel raycasting, then fitted with RANSAC shapes and OCR text (smoke-alarm mIoU 29.1 to 48.6%; lights 69.4 to 79.9% versus KPConv).\n- **Why this code:** 2D detections and 3D geometry are combined into one joint representation, so Fused.\n\n**Confidence (AC3):** High - the projection/raycasting fusion chain is explicit.')

FB[262] = ('Aligned',
    'Six IoT sensor clusters (PM2.5, CO2, noise, vibration) stream via MQTT/Firebase into Node-RED threshold rules and a shared dashboard, with sensors linked to BIM assets while each rule acts per channel.',
    'High',
    '**Fusion depth (AC1):** Aligned\n\n**Fusion evidence (AC2):**\n- **Data streams:** noise, PM2.5, CO2 and vibration IoT clusters on a Chulalongkorn University auditorium pilot (1-s transmission).\n- **Integration mechanism:** sensors are linked to BIM assets (hybrid LOIN-LOD framework) and rules run per channel in Node-RED with threshold alerts; actuator/HVAC responses are designed but not implemented.\n- **Why this code:** streams share the BIM asset frame while inference stays per channel, so Aligned.\n\n**Confidence (AC3):** High - the MQTT/Firebase/Node-RED linkage is explicit.')

FB[265] = ('Aligned',
    'Ambient-vibration modal parameters calibrate the SAP2000 FEM twin, and DInSAR-SBAS displacement observations are then interpreted against the twin thermo-mechanical output, with each stream used in its own stage.',
    'Medium',
    '**Fusion depth (AC1):** Aligned\n\n**Fusion evidence (AC2):**\n- **Data streams:** experimental ambient-vibration eigenfrequencies (0.92/1.01/1.33 Hz) + COSMO-SkyMed X-band DInSAR-SBAS displacements + air-temperature records.\n- **Integration mechanism:** vibration calibrates the FEM twin (about 2% error), and the calibrated twin thermo-mechanical analysis (about 2 cm per plus/minus 5 C) explains why the satellite misses the central span; the streams are used serially, not fused.\n- **Why this code:** data types share the bridge-model frame but inference runs per stage and per type, so Aligned.\n\n**Confidence (AC3):** Medium - serial use is clear from the text; a joint inference step is not described.')

FB[271] = ('Fused',
    'Depth and grayscale images are jointly encoded by a Siamese self-supervised contrastive network (vision transformer, Fourier network, multilevel fusion) with a Bayesian NN to generate probabilistic 3D point clouds.',
    'High',
    '**Fusion depth (AC1):** Fused\n\n**Fusion evidence (AC2):**\n- **Data streams:** grayscale images + depth images (30 image-pairs per rail fastener from a track-inspection vehicle).\n- **Integration mechanism:** multilevel fusion inside the contrastive network combines both channels into one probabilistic point-cloud output (Chamfer distance 0.3926, Hausdorff 1063.79), with RANSAC segmentation downstream.\n- **Why this code:** an explicit multimodal fusion network, so Fused.\n\n**Confidence (AC3):** High - the multilevel fusion architecture is explicit.')

FB[273] = ('Fused',
    'Live Wi-Fi RSSI localisation and the IFC-derived decision graph are jointly consumed by an extended Dijkstra algorithm whose dynamically updated route weights depend on both simultaneously.',
    'High',
    '**Fusion depth (AC1):** Fused\n\n**Fusion evidence (AC2):**\n- **Data streams:** Wi-Fi RSSI crowd localisation (two-stage strategy, 3.02-3.58 m error) + IFC-based dynamic decision graph of spaces/exits/sensors.\n- **Integration mechanism:** live crowd-sensed locations annotate the graph, and extended Dijkstra with AHP weights recomputes evacuation paths, reaching 94-96% in-time evacuation in a four-story academic building.\n- **Why this code:** routing output depends on the measured stream and the semantic graph simultaneously, so Fused.\n\n**Confidence (AC3):** High - the graph annotation + routing mechanism is explicit.')

FB[278] = ('Aligned',
    'BIM and FEM share one digital replica via Parasolid export, and the September-2023 magnitude-6.8 earthquake monitoring records corroborate the FEM results, with analyses run per stage.',
    'High',
    '**Fusion depth (AC1):** Aligned\n\n**Fusion evidence (AC2):**\n- **Data streams:** Revit BIM sensor metadata + MIDAS FEA NX model (278,778 elements) + real-time SHM records (vinchon, M6.8 earthquake).\n- **Integration mechanism:** Parasolid export links BIM and FEM into one replica frame; measured abutment displacement corroborates the FEM finding of a stable central vault, without joint processing.\n- **Why this code:** streams share the BIM-FEM frame while analysis stays per stage, so Aligned.\n\n**Confidence (AC3):** High - the BIM-FEM export chain is explicit.')

FB[283] = ('Unclear',
    'A document-analysis-based risk systematisation for construction DTs proposes a ten-step risk-treatment procedure and custom risk matrix, with no implemented system or data integration.',
    'High',
    '**Fusion depth (AC1):** Unclear\n\n**Fusion evidence (AC2):**\n- **Data streams:** 32 analysed studies mapped onto five risk categories.\n- **Integration mechanism:** none implemented - conceptual framework only.\n- **Why this code:** Unclear (rule 2).\n\n**Confidence (AC3):** High.')

FB[292] = ('Fused',
    'MMS-derived LiDAR point clouds, municipal GIS layers and authoritative geodatabases are integrated into IFC 4.3 semantic models (LoD200/LoD400) covering about 45 km of road network with 3 cm RMSE accuracy.',
    'Medium',
    '**Fusion depth (AC1):** Fused\n\n**Fusion evidence (AC2):**\n- **Data streams:** MMS LiDAR point clouds + municipal GIS layers + authoritative geodatabases.\n- **Integration mechanism:** the multi-scale workflow merges the sources into one semantically enriched IFC model validated by cloud-to-mesh deviation analysis (RMSE 3 cm).\n- **Why this code:** the IFC model is a joint product of several data sources, so Fused; static (no live ingestion), hence Medium.\n\n**Confidence (AC3):** Medium - the integration workflow is explicit; no live data link exists.')

FB[297] = ('Unclear',
    'An AHP + Bayesian-network underground-space planning model is presented with five-dimensional DT visualisation, but all evidence comes from simulations and assumed probabilities, with no deployed sensor network.',
    'High',
    '**Fusion depth (AC1):** Unclear\n\n**Fusion evidence (AC2):**\n- **Data streams:** assumed AHP weight vectors and BN probabilities; simulation outputs (21.897 mm settlement).\n- **Integration mechanism:** none demonstrated - real-time monitoring is asserted but not implemented.\n- **Why this code:** Unclear (rule 1/2).\n\n**Confidence (AC3):** High.')

FB[298] = ('Fused',
    'Extensometers, load cells and prism-target measurements jointly feed the FEM models that trigger rock-support adjustments on the Neelum Jhelum powerhouse cavern.',
    'Medium',
    '**Fusion depth (AC1):** Fused\n\n**Fusion evidence (AC2):**\n- **Data streams:** 52 extensometers, load cells and 24 prism targets + IFC-extended geological/BIM data.\n- **Integration mechanism:** the monitoring streams are combined in the FEM-based stability models whose outputs trigger support adjustments in near real time, via the five-dimensional DT framework.\n- **Why this code:** the stability decision depends on several measured streams simultaneously, so Fused.\n\n**Confidence (AC3):** Medium - the sensor-to-FEM feed is explicit, but evaluation metrics are comparative estimates.')

FB[299] = ('Fused',
    'A graph attention network couples flood simulation with INRIX 5-minute traffic-speed data, so segment-level speed and accessibility predictions depend on both data types simultaneously.',
    'High',
    '**Fusion depth (AC1):** Fused\n\n**Fusion evidence (AC2):**\n- **Data streams:** flood simulation grids (6-h intervals) + INRIX 5-min traffic speeds (Hurricane Harvey, two Houston zones).\n- **Integration mechanism:** dynamic edges that appear/disappear with inundation couple the two streams inside the GAT, predicting speed 45 min ahead (test MSE 0.2602) and capturing rerouting impacts.\n- **Why this code:** the prediction model output depends on two coupled data types simultaneously, so Fused.\n\n**Confidence (AC3):** High - the flood-traffic coupling mechanism is explicit.')

FB[300] = ('Fused',
    'PCRNet fuses infrared imagery with point-cloud depth information, and a CNN detects anomalies on the fused representation, achieving 92% accuracy and 95.1% F1.',
    'High',
    '**Fusion depth (AC1):** Fused\n\n**Fusion evidence (AC2):**\n- **Data streams:** UAV infrared images + point-cloud depth/geometry data (299 experimental data points).\n- **Integration mechanism:** PCRNet fusion adds depth information for irregular geometries, the CNN classifies thermal anomalies (96.3% precision, 94% recall), and Mask R-CNN markers register anomalies into the twin.\n- **Why this code:** an explicit IR + point-cloud fusion network, so Fused.\n\n**Confidence (AC3):** High - the PCRNet fusion is explicit.')

FB[302] = ('Aligned',
    'Monitoring-point displacements are mapped onto the surrogate-model full-field predictions for the Donglingxin landslide, sharing the model frame, while the surrogate itself learns from simulation rather than live sensor feedback.',
    'Medium',
    '**Fusion depth (AC1):** Aligned\n\n**Fusion evidence (AC2):**\n- **Data streams:** limited monitoring-point displacement data (2010-2022, 12.5-15.5-11.8 mm/y) + indoor DIC experiment data.\n- **Integration mechanism:** the stacking-ensemble surrogate (BP, RF, XGBoost, SVR, RBF) is trained on simulation and used to reconstruct full-field displacement from the monitoring points, with adaptive parameter updating; live sensor feedback is not part of the loop.\n- **Why this code:** measured data are mapped onto the surrogate frame while inference runs in the model, so Aligned.\n\n**Confidence (AC3):** Medium - the surrogate-monitoring linkage is explicit; the surrogate itself is simulation-trained.')

FB[308] = ('Fused',
    'RGB camera imagery, RTK-GNSS and IMU localisation are combined so skeletonization and PCA can convert segmentations into metric crack length and centre measurements on the building facade.',
    'Medium',
    '**Fusion depth (AC1):** Fused\n\n**Fusion evidence (AC2):**\n- **Data streams:** RGB camera imagery (YOLO12, 0.775 mAP) + RTK-GNSS/IMU robot localisation; UWB radar and infrared data are noted but unused.\n- **Integration mechanism:** localisation and segmentation are combined to produce metric defect quantification (1.140 cm length, 0.826 cm centre error) in the cloud DT with 2.8-4.8 s cycles.\n- **Why this code:** metric quantification depends on imagery and positioning simultaneously, so Fused.\n\n**Confidence (AC3):** Medium - the localisation-segmentation combination is explicit, but subsurface channels are unused.')

FB[309] = ('SINGLE',
    'Only vibration signals (plus auxiliary temperature on the test rig) drive the CycleGAN-augmented CNN-ResNet fault classifier; the gear-dynamics virtual entity generates training data, not a second measured type.',
    'High',
    '**Fusion depth (AC1):** SINGLE\n\n**Fusion evidence (AC2):**\n- **Data streams:** about 400 measured vibration samples (X/Y domain) from an RV-reducer test rig; CycleGAN-generated data are model outputs.\n- **Integration mechanism:** none - the CycleGAN maps simulated faultless vibration to the physical domain for augmentation, and CNN-ResNet classifies wear/crack/pitting/normal (98.86% with augmentation versus 32.5%).\n- **Why this code:** one measured data type, so SINGLE (AC=Single).\n\n**Confidence (AC3):** High.')

FB[313] = ('Fused',
    'Google Solar API heat-index data, Vienna population/vulnerability data and OpenStreetMap road infrastructure are fused into one dependency-risk graph whose centrality analysis plans responder routes.',
    'High',
    '**Fusion depth (AC1):** Fused\n\n**Fusion evidence (AC2):**\n- **Data streams:** Google Solar API heat-index data + Vienna Open Data population/vulnerability + OpenStreetMap critical roads.\n- **Integration mechanism:** the three sources are fused into a spatial dependency-risk graph; centrality analysis identifies cumulative risk paths and critical junctions (node 683 cold spot) and plans ambulance routes from cooling spots to hotspots.\n- **Why this code:** the graph is a joint representation whose analyses depend on all sources simultaneously, so Fused.\n\n**Confidence (AC3):** High - the graph fusion is explicit.')
