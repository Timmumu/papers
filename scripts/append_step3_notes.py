"""Append Step-3 deep-read sections to atomic notes for batch 2."""
import os

OUT = r'h:\phd\6.pjt\LR1\papers\01_source_3rd_SLR'

NOTES = {
'Aragon2025.md': ('MDPI Applied Sciences (GOLD OA, mdpi-res mirror)',
    'Tier 1 - Digital Model', '0/0/1', 'DfS', 'None', 'Digital Twin platform (no ML)', 'Multi', 'Cross-project', '3', 'Lifecycle / governance',
    'Position paper seeking a European definition of DTs for construction and infrastructure management (CEN/TC 442/WG 9, ISO 23247, ISO 19650). Two illustrative cases: Bidebieta-Basauri railway station DT management system and UPM civil-engineering school DT (COVID occupancy/safety protocols). Both are management/visualisation platforms with real-time information integration but no analytics or learning loop; safety appears only as a secondary use case. Value for this review: standardisation landscape and definition gap.'),
'Arhrib2026.md': ('MDPI Buildings (GOLD OA, mdpi-res mirror)',
    'Tier 1 - Digital Model', '0/0/1', 'DfQ', 'None', 'Digital Twin platform (no ML)', 'Multi', 'Single case study', '4', 'Perception / Computer Vision',
    'Cloud-native "Spatial Intelligence Hub": serverless, timeout-resilient orchestration of SfM/MVS photogrammetry, multi-user 3D review environment, PostGIS spatial DB storing defects as georeferenced anchors, frustum-based visibility scoring for image retrieval. Validated on real inspection datasets (reconstruction < 1 h, query < 25 ms). Authors explicitly contrast with passive "Level 1" twins yet the workflow is periodic re-scan, not live data: Tier 1. Strong DfQ relevance: traceable, spatially indexed defect evidence for infrastructure DTs.'),
'Armijo2024.md': ('MDPI Sensors (GOLD OA, mdpi-res mirror)',
    'Tier 2 - Digital Shadow', '0/0/1', 'DfS', 'Implemented', 'Other / Mixed (LightGBM + clustering + FEM calibration)', 'Single', 'Single case study', '4', 'Predictive analytics / decision support',
    'Railway-bridge SHM DT: low-cost wireless MEMS accelerometers, on-prem edge + cloud analytics. Seven-step methodology: characterisation, deployment, preprocessing, unsupervised learning of normal vibration clusters, FE-model calibration, synthetic damage generation, supervised LightGBM (validation ROC-AUC 0.9999), and continuous learning via periodic retraining on accumulated data. Two-year in-service pilot, no maintenance required. Learning loop is implemented (scheduled retraining) but no convergence analysis. One-way physical-to-virtual only: warnings go to humans, no actuation.'),
'Chan2025.md': ('MDPI Sensors (GOLD OA, mdpi-res mirror)',
    'Tier 2 - Digital Shadow', '0/0/1', 'DfS', 'None', 'Finite Element Method / physics-based', 'Multi', 'Single case study', '4', 'Design for Safety',
    'Risk mitigation of a 120-year-old heritage RC bridge in Australia (heritage constraints: non-invasive methods only). Ambient vibration testing + laser displacement monitoring; DT structural model validated against field data; what-if simulations for overweight vehicles and foundation scour; six-phase Incident Response Framework (detection, DT-based assessment, containment, recovery, documentation). Model is validated/updated manually; no learning mechanism.'),
'Chen2025-KG.md': ('MDPI Applied Sciences (GOLD OA, mdpi-res mirror)',
    'Tier 3 - Digital Twin (bidirectional)', '0/1/0', 'DfS', 'None', 'Ontology / semantic', 'Multi', 'Single case study', '4', 'Predictive analytics / decision support',
    'DT + knowledge-graph framework for emergency response in urban tunnel construction. DT continuously integrates real-time settlement, TBM operational parameters and structural responses; KG structures domain knowledge and applies rule-based reasoning to infer hazards, detect anomalies and suggest mitigation. Bidirectional DT-KG interaction: real-world data informs reasoning; inference results visualised in the DT for decision support. Applied to a real tunnel project in China; early anomaly identification prevented further structural impact. Rule-based, no learning update.'),
'Chen2026-ginpole.md': ('MDPI Buildings (GOLD OA, mdpi-res mirror)',
    'Tier 3 - Digital Twin (bidirectional)', '0/1/0', 'DfS', 'Mentioned only', 'Other / Mixed (TROA-ET + NSGA-III + FEM)', 'Multi', 'Single case study', '4', 'Design for Safety',
    'DT-enabled robust parallel control of a mobile gin pole in UHV transmission-line construction. FEM kinetic analysis converted into a TROA-optimised Extra-Trees surrogate (R2 0.9642 for max axial/shear stress); NSGA-III co-optimises safety and efficiency; embedded in a DT parallel-control architecture (perception, prediction, guidance). Real 110 kV project with bidirectional 4G/MQTT link over CANopen (data + control commands); safety risk reduced up to 32.3%, efficiency +42.7%. Surrogate is offline-trained; self-improvement only framed as architecture potential.'),
'ElDin2022.md': ('MDPI Buildings (GOLD OA, mdpi-res mirror)',
    'Unclear', '1/1/1', 'Both', 'None', 'Digital Twin platform (no ML)', 'Multi', 'Conceptual (no test)', '3', 'BIM-to-Digital-Twin architecture',
    'Systematic review of 229 publications on DTs in the AEC industry, finding a lack of standardisation; then proposes a conceptual framework for DT development for construction assets built on ISO 19650 information-management specifications (CDE-centric). No implementation or experiment; DfS/DfQ appear as application potential. Useful as the ISO 19650 anchoring reference for the review.'),
}

for slug, (src, tier, vwx, z, aa, ab, ac, ad, ae, af, ag) in NOTES.items():
    path = os.path.join(OUT, slug)
    v, w, x = vwx.split('/')
    sec = f"""
## Step-3 Deep-Read Coding (Prompt B) — full text via {src}

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | {tier} | {v} | {w} | {x} | {z} | {aa} | {ab} | {ac} | {ad} | {ae} | {af} |

**Key evidence (AG):** {ag}
"""
    open(path, 'a', encoding='utf-8').write(sec)
    print('updated', slug)
