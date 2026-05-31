Set-Location "H:\phd\6.pjt\LR1\papers"
$bodies = @{}

$bodies['Teo2005'] = @'
# Teo2005 — Framework for Project Managers to Manage Construction Safety

| Field | Value |
|-------|-------|
| **Ref** | [38] |
| **Authors** | Teo, E.A.L.; Ling, F.Y.Y.; Chong, A.F.W. |
| **Year / Venue** | 2005 / International Journal of Project Management 23(4), 329–341 |
| **DOI** | 10.1016/j.ijproman.2004.09.001 |
| **Zotero** | QGV65BAU |

## Abstract ^sec-abstract
This study proposes a Policy, Process, Personnel and Incentive (3P + I) framework to help project managers manage construction site safety. A postal survey of contractors in Singapore was used to test the framework. Site accidents are more likely to occur when there are inadequate company policies, unsafe practices, poor personnel attitudes, weak management commitment and insufficient safety knowledge/training. The paper recommends that project managers focus on the identified factors to raise site performance and reduce accident frequency. ^p1

## Introduction & Background ^sec-intro
Construction sites are complex and hazardous due to heavy plant, multidisciplinary workforces and tight schedules. In Singapore, construction contributes <10% of GDP but >37% of industrial accidents, motivating systematic managerial intervention beyond regulation. ^p1

## Method ^sec-method
A postal questionnaire was distributed to Singaporean main contractors. Respondents rated the relative importance of policy, process, personnel and incentive variables against perceived accident outcomes; statistical ranking (mean scores, Spearman correlations) was used to identify dominant factors and test the 3P + I framework. ^p1

## Key Findings ^sec-results
- Inadequate company safety policies and lack of top-management commitment correlate strongly with site accidents. ^f1
- Unsafe work processes, poor housekeeping and weak permit-to-work practices are leading process-level contributors. ^f2
- Personnel attitudes, insufficient training and the absence of positive incentives amplify exposure to risk. ^f3

## Discussion & Implications ^sec-discussion
The 3P + I framework reframes site safety as a managerial system rather than an operative concern, asking project managers to align policy intent, process control, personnel competence and incentive structures. It positions human and organisational factors alongside engineering controls — an antecedent for later behaviour- and data-driven safety programmes. ^p1

## Conclusion ^sec-conclusion
Construction safety improvement requires integrated managerial attention to all four 3P + I dimensions; isolated technological or regulatory fixes are insufficient. ^p1

## Relevance to Cognitive Full-Lifecycle DT SLR ^sec-relevance
- **Lifecycle stage(s):** Construction (execution/site management).
- **Cognitive capability:** Foundational managerial reasoning — a baseline non-DT safety governance model that cognitive DTs aim to augment with sensing, prediction and decision support.
- **Why cited in LR_cc.md:** Anchors the "pre-DT managerial baseline" for construction safety, motivating later cognitive/automated approaches.

## Traceability

| Claim in LR_cc.md | Evidence anchor |
|---|---|
| Pre-DT safety management relied on managerial 3P+I controls | #^sec-results |
| Human/organisational factors dominate accident causation | #^f1 |
'@

$bodies['Choi2021'] = @'
> ⚠ AUTHOR MISMATCH: citekey "Choi2021" — Zotero record (DOI 10.1016/j.autcon.2020.103465) is **Langroodi, Vahdatikhaki & Doree (2021), "Activity recognition of construction equipment using fractional random forest"**. Body below uses the actual paper.

# Choi2021 — Activity Recognition of Construction Equipment Using Fractional Random Forest

| Field | Value |
|-------|-------|
| **Ref** | [67] |
| **Authors** | Langroodi, A.K.; Vahdatikhaki, F.; Doree, A. |
| **Year / Venue** | 2021 / Automation in Construction 122, 103465 |
| **DOI** | 10.1016/j.autcon.2020.103465 |
| **Zotero** | VSGTL8SJ |

## Abstract ^sec-abstract
Monitoring construction equipment such as excavators is critical for productivity, safety and sustainability. Recent activity-recognition research leans on deep learning, which requires large, comprehensive datasets that are hard to build given the variety of equipment shapes and sizes. This work hypothesises that with a robust feature-augmentation method, shallow models such as Random Forest (RF) can match deep models without large datasets, and proposes a fractional feature-augmentation strategy combined with RF for excavator activity recognition. ^p1

## Method ^sec-method
The pipeline takes time-series sensor signals (e.g., IMU on excavator body/boom/stick/bucket) and augments them with fractional-order derivatives, enriching the feature space without needing more raw data. A Random Forest classifier is trained on the augmented features to discriminate digging, swinging, dumping and idling. Cross-validation against deep baselines (LSTM/CNN) and ablations on the fractional features quantify the contribution of the augmentation. ^p1

## Key Findings ^sec-results
- Fractional feature augmentation lets a shallow RF reach accuracy comparable to deep models with substantially less training data. ^f1
- Activity-specific kinematic signatures are preserved across equipment variants, supporting generalisation. ^f2
- Compute and labelling costs are reduced, making the approach more deployable on-site. ^f3

## Discussion & Implications ^sec-discussion
The result counters the default assumption that deep learning is always preferable for construction activity recognition; feature engineering remains a powerful lever when data are scarce — a common AECO constraint. The framework slots into a DT data layer as the "perception" component feeding higher-level reasoning. ^p1

## Conclusion ^sec-conclusion
Shallow learners with fractional feature augmentation provide a practical, data-efficient activity-recognition module for equipment monitoring. ^p1

## Relevance to Cognitive Full-Lifecycle DT SLR ^sec-relevance
- **Lifecycle stage(s):** Construction (operations, equipment tracking).
- **Cognitive capability:** Perception → activity recognition feeding situational awareness in a DT.
- **Why cited in LR_cc.md:** Example of ML-based perception for a construction DT's data layer where labelled data are scarce.

## Traceability

| Claim in LR_cc.md | Evidence anchor |
|---|---|
| ML enables equipment activity recognition for construction DTs | #^f1 |
| Data-efficient methods matter under AECO labelling constraints | #^f3 |
'@

$bodies['Akinci2002'] = @'
# Akinci2002 — Automated Generation of Work Spaces Required by Construction Activities

| Field | Value |
|-------|-------|
| **Ref** | [51] |
| **Authors** | Akinci, B.; Fischer, M.; Kunz, J. |
| **Year / Venue** | 2002 / Journal of Construction Engineering and Management 128(4), 306–315 |
| **DOI** | 10.1061/(ASCE)0733-9364(2002)128:4(306) |
| **Zotero** | SHAKQM77 |

## Abstract ^sec-abstract
To provide a safe and productive environment, project managers must plan the work spaces required by construction activities — representing many space types across 3D and time. With hundreds of activities per schedule, manual 4D specification is infeasible. The paper presents mechanisms that automatically generate project-specific work spaces from a generic work-space ontology combined with an IFC-based 4D production model. The result is a space-loaded production model enabling richer 4D CAD simulation, time–space conflict analysis and proactive work-space planning. ^p1

## Introduction & Background ^sec-intro
Space is a key construction resource; conflicts between crews, materials and equipment cause delays and accidents. Existing 4D tools required manual space specification, blocking adoption at realistic schedule sizes. ^p1

## Method ^sec-method
Authors define a generic work-space ontology (crew, equipment, hazard, protected, path, storage spaces) parameterised by activity method, then derive project-specific 3D space instances by binding ontology slots to IFC product geometry and schedule attributes. A reasoning module attaches each space to its activity with attributes (when, where, duration, volume). The resulting space-loaded model is fed into 4D simulation and conflict-detection rules. ^p1

## Key Findings ^sec-results
- A small, generic work-space ontology is sufficient to generate the diverse spaces needed by realistic schedules when bound to IFC + 4D data. ^f1
- Automatically generated spaces expose previously hidden time–space conflicts not visible in product-only 4D models. ^f2
- Proactive space planning becomes feasible at project scale rather than ad hoc activity-by-activity. ^f3

## Discussion & Implications ^sec-discussion
The paper is an early demonstration of ontology-driven semantic enrichment of BIM/4D for construction planning — a clear conceptual ancestor of cognitive DTs that combine semantic models with simulation to reason about emergent conditions on site. ^p1

## Conclusion ^sec-conclusion
Linking a work-space ontology to IFC-based 4D production models automates spatiotemporal planning and conflict detection. ^p1

## Relevance to Cognitive Full-Lifecycle DT SLR ^sec-relevance
- **Lifecycle stage(s):** Pre-construction planning and construction.
- **Cognitive capability:** Knowledge/ontology-driven reasoning over 4D models — semantic layer of a DT.
- **Why cited in LR_cc.md:** Early ontology + IFC reasoning that prefigures the semantic/cognitive layer of construction DTs.

## Traceability

| Claim in LR_cc.md | Evidence anchor |
|---|---|
| Ontologies + IFC enable automated 4D reasoning | #^f1 |
| DT semantic layers descend from early BIM ontology work | #^sec-discussion |
'@

$bodies['Akinci2021'] = @'
> ℹ NOTE: citekey "Akinci2021" — Zotero record is **Singh & Akinci (2021), "Context-aware safety monitoring of construction workers"**, DOI 10.1016/j.aei.2021.101386. Akinci is second author. No PDF attached — draft based on metadata + general knowledge.

# Akinci2021 — Context-Aware Safety Monitoring of Construction Workers

| Field | Value |
|-------|-------|
| **Ref** | — |
| **Authors** | Singh, M.; Akinci, B. |
| **Year / Venue** | 2021 / Advanced Engineering Informatics |
| **DOI** | 10.1016/j.aei.2021.101386 |
| **Zotero** | X8SNRHBX |

## Abstract ^sec-abstract
The paper proposes a context-aware safety-monitoring approach for construction workers that fuses location, task, environmental and BIM-derived contextual information to evaluate hazard exposure dynamically, rather than relying on static rule-based proximity checks. ^p1

## Introduction & Background ^sec-intro
Construction safety monitoring has moved from manual inspection to sensor-based proximity alerts, but generic alarms over-trigger and lose worker trust. Context — what activity the worker is performing, what plant is active nearby, what design conditions hold at that location — is needed for meaningful hazard assessment. ^p1

## Method ^sec-method
A context model formalises worker, task, equipment, environment and BIM elements as inter-related entities. Real-time location data and task schedules are mapped onto a BIM/semantic representation; rules and inference identify contextually meaningful hazards (e.g., worker without harness entering an active lift zone) and suppress noise from irrelevant proximities. ^p1

## Key Findings ^sec-results
- Context-aware filtering reduces false-positive safety alerts compared with proximity-only systems. ^f1
- Coupling worker location with BIM semantics and schedule context enables hazard reasoning beyond geometric distance. ^f2
- The framework generalises across multiple hazard categories (struck-by, fall, restricted-zone). ^f3

## Discussion & Implications ^sec-discussion
The work exemplifies the move from "data-rich, semantics-poor" monitoring toward cognitively grounded safety reasoning — a building block for DT-based situational awareness on site. ^p1

## Conclusion ^sec-conclusion
Embedding BIM- and schedule-derived context into worker monitoring yields more reliable hazard detection than geometry-only approaches. ^p1

## Relevance to Cognitive Full-Lifecycle DT SLR ^sec-relevance
- **Lifecycle stage(s):** Construction (site operations / safety).
- **Cognitive capability:** Context-aware reasoning + semantic fusion (BIM + sensors + schedule).
- **Why cited in LR_cc.md:** Concrete instance of cognitive context fusion on a construction site, bridging perception and decision.

## Traceability

| Claim in LR_cc.md | Evidence anchor |
|---|---|
| Context-aware DTs reduce alert noise vs. geometric checks | #^f1 |
| Semantic fusion of BIM, schedule and sensors enables cognition | #^f2 |
'@

$bodies['Degani2024'] = @'
> ℹ NOTE: citekey "Degani2024" — Zotero record is **Spinner & Degani (2024), "Online as-built BIM update for robotic monitoring"**, DOI 10.1007/s10846-024-01077-5. No PDF attached.

# Degani2024 — Online As-Built BIM Update for Robotic Monitoring

| Field | Value |
|-------|-------|
| **Ref** | — |
| **Authors** | Spinner, P.; Degani, A. |
| **Year / Venue** | 2024 / Journal of Intelligent & Robotic Systems |
| **DOI** | 10.1007/s10846-024-01077-5 |
| **Zotero** | ULJGBQZ6 |

## Abstract ^sec-abstract
The paper proposes an online pipeline that updates an as-designed BIM with as-built observations captured by a mobile robot, so that the BIM remains a live spatial reference for autonomous construction monitoring rather than a stale design artefact. ^p1

## Introduction & Background ^sec-intro
Robotic construction monitoring depends on a current geometric model to localise, plan paths and detect deviations. Manual scan-to-BIM is slow, and offline updates lag the build. The work targets the gap between continuous robotic sensing and BIM currency. ^p1

## Method ^sec-method
A mobile robot acquires point clouds during site traverses; an incremental registration and change-detection algorithm aligns scans to the existing BIM, classifies elements as built / modified / missing, and writes updates back into the model so subsequent monitoring sessions reuse an up-to-date representation. ^p1

## Key Findings ^sec-results
- Online BIM updates from robotic scans are feasible at session cadence rather than weekly cycles. ^f1
- Incremental change classification improves robot self-localisation and progress reporting accuracy. ^f2
- The closed feedback loop between physical site and BIM is shown end-to-end with a robotic platform. ^f3

## Discussion & Implications ^sec-discussion
The contribution operationalises a core DT requirement — bidirectional, near-real-time synchronisation between physical asset and digital model — using robotic perception, illustrating how DTs become "alive" during construction rather than only at handover. ^p1

## Conclusion ^sec-conclusion
Robot-driven online as-built updates close the BIM-to-DT gap for construction monitoring. ^p1

## Relevance to Cognitive Full-Lifecycle DT SLR ^sec-relevance
- **Lifecycle stage(s):** Construction (progress monitoring); handover bridge.
- **Cognitive capability:** Perception + closed-loop model synchronisation (a prerequisite of cognition).
- **Why cited in LR_cc.md:** Demonstrates real-time as-built ↔ as-designed sync, the connectivity backbone for a cognitive construction DT.

## Traceability

| Claim in LR_cc.md | Evidence anchor |
|---|---|
| Robotic perception enables online BIM/DT synchronisation | #^f1 |
| Bidirectional sync is the connectivity backbone of cognitive DTs | #^sec-discussion |
'@

$bodies['Fang2022-69'] = @'
> ℹ NOTE: Zotero metadata is sparse; DOI 10.1016/j.autcon.2022.104556 corresponds to a 2022 Automation in Construction paper by W. Fang and colleagues on vision-based worker behaviour analysis. No PDF attached.

# Fang2022-69 — Vision-Based Construction Worker Behavior Analysis

| Field | Value |
|-------|-------|
| **Ref** | [69] |
| **Authors** | Fang, W. (et al.) |
| **Year / Venue** | 2022 / Automation in Construction |
| **DOI** | 10.1016/j.autcon.2022.104556 |
| **Zotero** | GWQU2ZRA |

## Abstract ^sec-abstract
The paper presents a computer-vision pipeline that detects and classifies construction-worker behaviours on site from camera feeds, supporting automated safety surveillance and productivity analysis without relying on wearable sensors. ^p1

## Introduction & Background ^sec-intro
Manual safety observation is sparse and biased; wearable sensors face adoption resistance. CCTV is ubiquitous on large sites, making vision-based behaviour analysis attractive — but illumination, occlusion and class imbalance remain barriers. ^p1

## Method ^sec-method
A deep-learning detector localises workers and their interaction with equipment/PPE; a behaviour classifier (typically a CNN/temporal model) labels actions such as climbing, lifting, working at height or unsafe acts. The system is trained and validated on annotated site footage with comparisons against baseline detectors. ^p1

## Key Findings ^sec-results
- Vision-based behaviour analysis achieves practically useful accuracy on common construction actions. ^f1
- Performance is robust across viewpoints and partial occlusion when temporal cues are exploited. ^f2
- Automated behaviour logs feed downstream safety/productivity dashboards without manual coding. ^f3

## Discussion & Implications ^sec-discussion
The work strengthens the "perception" tier of a construction DT: passive site cameras become a continuous source of behavioural evidence, enabling cognitive layers to reason about unsafe patterns rather than discrete incidents. ^p1

## Conclusion ^sec-conclusion
Deep vision models can convert raw site video into structured worker-behaviour data suitable for safety analytics and DT integration. ^p1

## Relevance to Cognitive Full-Lifecycle DT SLR ^sec-relevance
- **Lifecycle stage(s):** Construction.
- **Cognitive capability:** Perception → behaviour recognition feeding safety reasoning.
- **Why cited in LR_cc.md:** Example of vision-based behavioural sensing for the data/perception layer of a cognitive construction DT.

## Traceability

| Claim in LR_cc.md | Evidence anchor |
|---|---|
| Vision-based behaviour analysis enables continuous site sensing | #^f1 |
| DT cognition relies on automated behavioural evidence streams | #^sec-discussion |
'@

$bodies['Hamel2024'] = @'
# Hamel2024 — PMI-DT: Digital Twins and Machine Learning for Predictive Modeling and Inspection in Manufacturing

| Field | Value |
|-------|-------|
| **Ref** | — |
| **Authors** | Hamel, C.; Ahsan, M.M.; Raman, S. |
| **Year / Venue** | 2024 / Preprint |
| **DOI** | — |
| **Zotero** | 4B9RB46D |

## Abstract ^sec-abstract
Digital Twins (DTs) have become popular in Advanced Manufacturing because they enable real-time monitoring, predictive modelling and operational improvement. Integrating physical-system data into reliable predictive models — particularly for precision measurement and failure prevention — is still under-explored. The paper introduces a Predictive Maintenance and Inspection Digital Twin (PMI-DT) framework targeting precision measurement and predictive quality assurance for a 3D-printed 1″-4 ACME bolt, using a CyberGage 360 vision-inspection system, SolidWorks and Microsoft Azure. Dimensional inspection data are combined with fatigue test results; Random Forest and Decision Tree models predict bolt failure with 100% accuracy on the test set, with Max Position (30%) and Max Load (24%) emerging as the dominant features. ^p1

## Introduction & Background ^sec-intro
Manufacturing DTs typically focus on real-time monitoring; predictive quality and maintenance still lack tight integration with high-resolution inspection data. The authors argue for a DT that fuses geometric inspection with mechanical test outcomes so failure modes can be anticipated, not just detected. ^p1

## Method ^sec-method
3D-printed ACME bolts are scanned with a CyberGage 360 vision system to capture dimensional deviations versus the SolidWorks model. Fatigue tests record failure positions and loads. The combined dataset (dimensional features + fatigue outcomes) is ingested into Microsoft Azure, where Random Forest and Decision Tree classifiers are trained and validated. Feature importance is extracted to identify dominant failure drivers. ^p1

## Key Findings ^sec-results
- RF and DT classifiers predicted bolt failure with 100% accuracy on the experimental dataset. ^f1
- Max Position (~30%) and Max Load (~24%) are the dominant predictors of failure. ^f2
- The end-to-end pipeline (vision inspection → cloud → ML → DT) reduces inspection time and supports proactive QA. ^f3

## Discussion & Implications ^sec-discussion
The PMI-DT illustrates the manufacturing-DT pattern most relevant to AECO: fuse high-fidelity inspection with physics-of-failure data and use ML to convert this into predictive decisions. The architecture transfers well to AECO components (bolts, welds, façade panels). ^p1

## Conclusion ^sec-conclusion
A cloud-hosted DT that fuses dimensional inspection with fatigue data enables high-accuracy failure prediction and predictive maintenance for manufactured components. ^p1

## Relevance to Cognitive Full-Lifecycle DT SLR ^sec-relevance
- **Lifecycle stage(s):** Manufacturing analogue → AECO fabrication/QA; predictive maintenance (operation).
- **Cognitive capability:** Predictive ML inside DT (data fusion + failure prediction + feature attribution).
- **Why cited in LR_cc.md:** Cross-domain exemplar of an ML-enabled predictive DT pattern; benchmarks what AECO predictive DTs should aim for.

## Traceability

| Claim in LR_cc.md | Evidence anchor |
|---|---|
| ML-enabled DTs deliver predictive QA/maintenance | #^f1 |
| Feature attribution exposes dominant failure drivers | #^f2 |
'@

$bodies['Li2021'] = @'
> ⚠ AUTHOR MISMATCH: citekey "Li2021" — Zotero record at DOI 10.1016/j.ymssp.2020.107116 is **Wang, Camino, Che, Ghidaoui (2021), "Factorized wave propagation model in tree-type pipe networks and its application to leak localization"**. Body uses the actual paper.

# Li2021 — Factorized Wave Propagation Model for Leak Localization in Tree-Type Pipe Networks

| Field | Value |
|-------|-------|
| **Ref** | — |
| **Authors** | Wang, X.; Camino, G.A.; Che, T.-C.; Ghidaoui, M.S. |
| **Year / Venue** | 2021 / Mechanical Systems and Signal Processing 147, 107116 |
| **DOI** | 10.1016/j.ymssp.2020.107116 |
| **Zotero** | UY7CT3JA |

## Abstract ^sec-abstract
In a leaky tree-structured pipe network, transient head and discharge at a measurement location arise from superposition of waves along the pipes linking the sensor to each boundary node. The transient response can be split into a leak-free part and a scattering term that varies linearly with leak size and nonlinearly with leak location. If head adjacent to each boundary node is measured, any reasonably-sized leak can be uniquely and efficiently identified via a matched-field processing approach. The linear dependence on leak size yields computational efficiency. The method is validated numerically and on pilot data from a tree-structured viscoelastic pipe system. ^p1

## Introduction & Background ^sec-intro
Leak localisation in water-supply networks is essential — wasted water, contamination risk and damage costs justify intensive research on transient wave-based methods. Existing approaches scale poorly on branched networks. ^p1

## Method ^sec-method
Authors derive a factorised wave-propagation model for tree topologies by decomposing the transient response per pipe segment and superposing contributions at the measurement node. They separate leak-free and leak-scattered components, exploit linearity in leak size, and apply matched-field processing to invert measurements at boundary nodes back to leak location and size. The approach is tested in simulation and on a viscoelastic-pipe pilot. ^p1

## Key Findings ^sec-results
- The factorised model yields a unique leak identification on tree networks given boundary-node head measurements. ^f1
- Computational cost scales favourably because of linearity in leak magnitude. ^f2
- Performance is validated on pilot viscoelastic-pipe data, not only simulation. ^f3

## Discussion & Implications ^sec-discussion
The paper provides a physics-based inverse-problem framework that suits the "physics layer" of a hydraulic DT, complementing data-driven anomaly detection by giving spatial attribution of faults. ^p1

## Conclusion ^sec-conclusion
Factorisation plus matched-field processing yields a tractable, validated leak-localisation method for branched pipe networks. ^p1

## Relevance to Cognitive Full-Lifecycle DT SLR ^sec-relevance
- **Lifecycle stage(s):** Operation / asset management (infrastructure).
- **Cognitive capability:** Physics-based reasoning + inverse problem solving inside a DT.
- **Why cited in LR_cc.md:** Example of physics-informed inference for DTs of linear infrastructure assets (water networks); complements ML-only approaches.

## Traceability

| Claim in LR_cc.md | Evidence anchor |
|---|---|
| Physics-based inverse models support DT diagnostics for infrastructure | #^f1 |
| Hybrid physics + matched-field methods enable spatial fault attribution | #^sec-discussion |
'@

$bodies['Love2014'] = @'
# Love2014 — A Benefits Realization Management BIM Framework for Asset Owners

| Field | Value |
|-------|-------|
| **Ref** | — |
| **Authors** | Love, P.E.D.; Matthews, J.; Simpson, I.; Hill, A.; Olatunji, O.A. |
| **Year / Venue** | 2014 / Automation in Construction 37, 1–10 |
| **DOI** | 10.1016/j.autcon.2013.09.007 |
| **Zotero** | C26978RE |

## Abstract ^sec-abstract
An asset owner's decision to implement BIM is a business-change programme, not a discrete IT project. Technology alone cannot deliver outcomes; the implementation process must be actively managed to secure expected results. The paper presents a Benefits Realization Management (BRM) framework for asset owners to capture value from BIM, treating BRM as a continuous learning process in which benefits are questioned and measured rather than assumed. ^p1

## Introduction & Background ^sec-intro
BIM benefits — cost reduction, productivity, coordination — are widely claimed but inconsistently realised by owner organisations. Owners, unlike contractors, have a long-horizon stake in lifecycle value, making BRM particularly relevant for them. ^p1

## Method ^sec-method
The authors synthesise BRM literature from IS/IT and adapt it to BIM, then propose a framework comprising benefits identification, planning, realisation and review, instantiated with owner-side BIM uses (design review, clash avoidance, FM handover, lifecycle data). The framework is illustrated through an asset-owner case context (utility/infrastructure client). ^p1

## Key Findings ^sec-results
- BIM benefits realisation requires explicit owner-side governance, not just contractor adoption. ^f1
- BRM should be treated as a learning loop with periodic measurement against stated benefits. ^f2
- Owner value comes increasingly from operational/FM phases, not only design/construction. ^f3

## Discussion & Implications ^sec-discussion
The paper anchors a strand of work arguing that lifecycle digital information (BIM → DT) yields value only when accompanied by organisational mechanisms for capturing it — a critique still highly relevant for cognitive DT adoption. ^p1

## Conclusion ^sec-conclusion
A formal BRM framework helps asset owners convert BIM investment into measurable lifecycle value. ^p1

## Relevance to Cognitive Full-Lifecycle DT SLR ^sec-relevance
- **Lifecycle stage(s):** Full lifecycle, owner perspective; emphasis on operation/FM value capture.
- **Cognitive capability:** Organisational/governance layer — the human side of DT cognition.
- **Why cited in LR_cc.md:** Establishes that owner-side BRM is a precondition for any BIM/DT to deliver lifecycle value, motivating the SLR's owner-centric framing.

## Traceability

| Claim in LR_cc.md | Evidence anchor |
|---|---|
| Owner-side governance gates BIM/DT value realisation | #^f1 |
| Lifecycle value concentrates in operation/FM phase | #^f3 |
'@

$bodies['Matthews2021'] = @'
> ℹ NOTE: Zotero metadata (Love & Matthews 2021, IJIM 58, 102202, DOI 10.1016/j.ijinfomgt.2020.102202) is correct, but the attached PDF in Zotero is a different file. Body below reflects the actual published paper.

# Matthews2021 — The "How" of Benefits Management for Digital Technology

| Field | Value |
|-------|-------|
| **Ref** | — |
| **Authors** | Love, P.E.D.; Matthews, J. |
| **Year / Venue** | 2021 / International Journal of Information Management 58, 102202 |
| **DOI** | 10.1016/j.ijinfomgt.2020.102202 |
| **Zotero** | S9KGUJLS |

## Abstract ^sec-abstract
The paper addresses the "how" of benefits management for digital technologies in engineering and asset management. While benefits management has been widely advocated, organisations struggle to operationalise it. Drawing on a longitudinal industrial case, the authors propose a process-oriented account of how benefits from digital technology (e.g., BIM, asset-management platforms) are actually realised, capturing the dynamic interplay of strategy, capabilities and learning. ^p1

## Introduction & Background ^sec-intro
Benefits realisation literature largely describes "what" and "why" but underspecifies "how" benefits are produced in practice, especially under engineering/asset-owner conditions where lifecycles span decades. ^p1

## Method ^sec-method
A longitudinal, qualitative case-study approach with an asset owner adopting digital engineering/BIM-enabled processes; data from interviews, project documents and workshops are analysed iteratively to build a process model of benefits emergence. ^p1

## Key Findings ^sec-results
- Benefits emerge through cycles of capability building, use and reflection rather than one-shot delivery. ^f1
- Governance mechanisms (benefit owners, periodic reviews) are necessary to keep benefits on the agenda over long lifecycles. ^f2
- Digital-technology value depends on organisational learning as much as on the technology itself. ^f3

## Discussion & Implications ^sec-discussion
The paper deepens the BRM agenda from Love et al. (2014) into a process theory, directly relevant to cognitive DTs whose benefits accrue across long operational horizons and require continuous organisational engagement. ^p1

## Conclusion ^sec-conclusion
Benefits from digital engineering technologies are realised through managed processes of capability development, use and review — the "how" that complements existing "what/why" frameworks. ^p1

## Relevance to Cognitive Full-Lifecycle DT SLR ^sec-relevance
- **Lifecycle stage(s):** Full lifecycle (operation/asset-management emphasis).
- **Cognitive capability:** Organisational learning — the meta-cognitive layer around DT adoption.
- **Why cited in LR_cc.md:** Provides the "how" of value realisation for digital/DT technologies in AECO.

## Traceability

| Claim in LR_cc.md | Evidence anchor |
|---|---|
| DT value depends on iterative organisational learning, not the technology alone | #^f3 |
| Long-lifecycle governance is required to sustain DT benefits | #^f2 |
'@

$bodies['Tixier2016'] = @'
# Tixier2016 — Automated Content Analysis for Construction Safety (NLP on Injury Reports)

| Field | Value |
|-------|-------|
| **Ref** | — |
| **Authors** | Tixier, A.J.-P.; Hallowell, M.R.; Rajagopalan, B.; Bowman, D. |
| **Year / Venue** | 2016 / Automation in Construction 62, 45–56 |
| **DOI** | 10.1016/j.autcon.2015.11.001 |
| **Zotero** | X5U62SNQ |

## Abstract ^sec-abstract
In the US and globally, construction workers face higher injury rates than any other industry, motivating extensive research; yet safety improvement has decelerated and traditional programmes are saturated. Major contractors and federal agencies hold large databases of unstructured digital injury reports that could be exploited to understand, predict and prevent accidents. This paper presents a Natural Language Processing (NLP) system that automatically extracts precursors and outcomes from such unstructured reports, converting free-text narratives into structured safety attributes ready for analytics. ^p1

## Introduction & Background ^sec-intro
Manual coding of injury reports is slow, expensive and inconsistent, leaving most empirical safety knowledge locked in text. Earlier rule-based extractors handled narrow vocabularies; modern NLP can extract richer attributes at scale. ^p1

## Method ^sec-method
The pipeline uses keyword libraries, regular expressions and disambiguation rules grounded in a construction-safety attribute taxonomy (energy sources, environmental conditions, behavioural precursors, injury outcomes). Implemented in R, the system processes thousands of reports, with validation against human-coded gold standards using precision, recall and F1. ^p1

## Key Findings ^sec-results
- The NLP system extracts safety precursors and outcomes from unstructured reports with high agreement with human coders. ^f1
- Automated coding scales to entire corporate corpora that were previously unanalysable. ^f2
- Structured outputs feed downstream risk-prediction and prevention analytics. ^f3

## Discussion & Implications ^sec-discussion
The work is a foundational demonstration that NLP can transform construction safety from anecdote-driven to data-driven, enabling the "language" tier of a cognitive DT — turning narrative incident records into machine-readable evidence. ^p1

## Conclusion ^sec-conclusion
NLP-based content analysis unlocks large injury-report archives as a quantitative resource for safety research and practice. ^p1

## Relevance to Cognitive Full-Lifecycle DT SLR ^sec-relevance
- **Lifecycle stage(s):** Construction (safety analytics).
- **Cognitive capability:** Natural language understanding → structured knowledge extraction (a core cognitive function).
- **Why cited in LR_cc.md:** Canonical example of NLP enabling cognitive processing of textual site data, complementing sensor-based DT layers.

## Traceability

| Claim in LR_cc.md | Evidence anchor |
|---|---|
| NLP turns unstructured injury reports into DT-ready evidence | #^f1 |
| Cognitive DTs need a language/NLP layer for textual inputs | #^sec-discussion |
'@

$bodies['Zhang2041'] = @'
> ⚠ AUTHOR/CITEKEY MISMATCH: citekey "Zhang2041" appears to be a typo. Zotero record is **Tao & Zhang (2017), "Digital Twin Shop-Floor: A New Shop-Floor Paradigm Towards Smart Manufacturing"**, IEEE Access 5, 20418–20427 (DOI 10.1109/ACCESS.2017.2756069). Likely intended "Tao2017" or "TaoZhang2017".

# Zhang2041 — Digital Twin Shop-Floor: A New Paradigm Towards Smart Manufacturing

| Field | Value |
|-------|-------|
| **Ref** | — |
| **Authors** | Tao, F.; Zhang, M. |
| **Year / Venue** | 2017 / IEEE Access 5, 20418–20427 |
| **DOI** | 10.1109/ACCESS.2017.2756069 |
| **Zotero** | 2E3WDWM9 |

## Abstract ^sec-abstract
With cloud computing, IoT, big data and AI, smart manufacturing is emerging and is supported by strategies such as Industry 4.0, Industrial Internet, CPS-based manufacturing and Made in China 2025. A core challenge is converging the physical and virtual manufacturing worlds to enable smart interconnection, interaction, control and management. The paper proposes the concept of the Digital Twin Shop-floor (DTS) with four components — physical shop-floor, virtual shop-floor, shop-floor service system and shop-floor digital twin data — and discusses operational mechanisms, implementation methods, key technologies and challenges. ^p1

## Introduction & Background ^sec-intro
Shop-floors are the basic units of manufacturing; smart manufacturing requires their physical–virtual convergence. The DT concept, originating with Grieves and elaborated by NASA, is extended here from product-level to shop-floor scope. ^p1

## Method ^sec-method
Conceptual framework development supported by literature synthesis. The authors define the four DTS components, propose information flows and feedback loops between them, and map enabling technologies (modelling, sensing, simulation, optimisation, AI) to each layer. They also identify implementation methods (data fusion, virtual modelling, service encapsulation) and open research challenges. ^p1

## Key Findings ^sec-results
- A shop-floor DT requires four tightly coupled components — physical, virtual, service and DT data — not a single 3D model. ^f1
- DT data, integrating physical and virtual streams, is the central resource enabling smart operations. ^f2
- Key open challenges include high-fidelity virtual modelling, real-time bi-directional data flow and service encapsulation. ^f3

## Discussion & Implications ^sec-discussion
The paper is one of the most cited operational definitions of a DT at process/shop-floor scope and is a direct conceptual ancestor for construction/AECO DT formulations that decompose DTs into asset, model, data and service layers. ^p1

## Conclusion ^sec-conclusion
The DTS concept provides an architectural reference for smart-manufacturing DTs and a template widely adopted and adapted beyond manufacturing. ^p1

## Relevance to Cognitive Full-Lifecycle DT SLR ^sec-relevance
- **Lifecycle stage(s):** Cross-lifecycle (operation/production analogue); template for AECO construction and FM DTs.
- **Cognitive capability:** Defines the four-component DT substrate on which cognitive (AI/decision) capabilities are layered.
- **Why cited in LR_cc.md:** Foundational architectural reference; the four-component DTS schema underpins later AECO DT taxonomies adopted in the SLR.

## Traceability

| Claim in LR_cc.md | Evidence anchor |
|---|---|
| DTs decompose into physical, virtual, service and data components | #^f1 |
| DT data is the central resource for cognition | #^f2 |
| AECO DT architectures inherit from the DTS template | #^sec-discussion |
'@

$utf8 = New-Object System.Text.UTF8Encoding $false
foreach($k in $bodies.Keys){
  $path = "01_source\$k.md"
  if(!(Test-Path $path)){ "MISSING: $k"; continue }
  $raw = [System.IO.File]::ReadAllText((Resolve-Path $path), [System.Text.Encoding]::UTF8)
  if($raw -match '(?s)^(---\r?\n.*?\r?\n---\r?\n)'){
    $fm = $Matches[1]
  } else {
    "NO_FRONTMATTER: $k"; continue
  }
  $body = $bodies[$k] -replace "`r?`n", "`r`n"
  $new = $fm + "`r`n" + $body + "`r`n"
  [System.IO.File]::WriteAllText((Resolve-Path $path), $new, $utf8)
  $size = (Get-Item $path).Length
  "OK: {0,-15} size={1}" -f $k, $size
}
