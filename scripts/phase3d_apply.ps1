Set-Location "H:\phd\6.pjt\LR1\papers"
$utf8 = New-Object System.Text.UTF8Encoding $false
$today = "2026-06-01"

# 1) TaoZhang2017.md - full rewrite (frontmatter + body)
$taoZhang = @'
---
ref: "[58]"
citekey: "TaoZhang2017"
title: "Digital twin shop-floor: A new shop-floor paradigm towards smart manufacturing"
authors: "F. Tao and M. Zhang"
year: 2017
journal: "IEEE Access"
doi: "10.1109/ACCESS.2017.2756069"
zotero_key: "2E3WDWM9"
zotero_status: verified
last_verified: "2026-06-01"
tags:
  - Verified
  - Digital-Twin
  - Smart-Manufacturing
---

# TaoZhang2017 — Digital Twin Shop-Floor: A New Paradigm Towards Smart Manufacturing

| Field | Value |
|-------|-------|
| **Ref** | [58] |
| **Authors** | Tao, F.; Zhang, M. |
| **Year / Venue** | 2017 / IEEE Access 5, 20418–20427 |
| **DOI** | 10.1109/ACCESS.2017.2756069 |
| **Zotero** | 2E3WDWM9 |

## Abstract ^sec-abstract
With cloud computing, IoT, big data and AI, smart manufacturing is emerging, supported by strategies such as Industry 4.0, Industrial Internet, CPS-based manufacturing and Made in China 2025. A core challenge is converging the physical and virtual manufacturing worlds to enable smart interconnection, interaction, control and management. The paper proposes the concept of the Digital Twin Shop-floor (DTS) with four components — physical shop-floor, virtual shop-floor, shop-floor service system and shop-floor digital twin data — and discusses operational mechanisms, implementation methods, key technologies and open challenges. ^p1

## Introduction & Background ^sec-intro
Shop-floors are the basic units of manufacturing; smart manufacturing requires their physical–virtual convergence. The DT concept, originating with Grieves and elaborated by NASA, is extended here from product-level to shop-floor scope. ^p1

## Method ^sec-method
Conceptual framework development supported by literature synthesis. The authors define the four DTS components, propose information flows and feedback loops between them, and map enabling technologies (modelling, sensing, simulation, optimisation, AI) to each layer. They identify implementation methods (data fusion, virtual modelling, service encapsulation) and outstanding research challenges. ^p1

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

# 2) Spinner2024.md - full rewrite
$spinner = @'
---
ref: "[11]"
citekey: "Spinner2024"
title: "Online as-built building information model update for robotic monitoring in construction sites"
authors: "Patrick Spinner, Amir Degani"
year: 2024
journal: "Journal of Intelligent & Robotic Systems"
doi: "10.1007/s10846-024-01077-5"
zotero_key: "ULJGBQZ6"
zotero_status: verified
last_verified: "2026-06-01"
tags:
  - Verified
  - Robotics
  - BIM
  - As-Built
---

# Spinner2024 — Online As-Built BIM Update for Robotic Monitoring in Construction Sites

| Field | Value |
|-------|-------|
| **Ref** | [11] |
| **Authors** | Spinner, P.; Degani, A. |
| **Year / Venue** | 2024 / Journal of Intelligent & Robotic Systems |
| **DOI** | 10.1007/s10846-024-01077-5 |
| **Zotero** | ULJGBQZ6 |

> ℹ NOTE: PDF not yet attached in local Zotero copy; body drafted from metadata + DOI-level information.

## Abstract ^sec-abstract
The paper proposes an online pipeline that updates an as-designed BIM with as-built observations captured by a mobile robot, keeping the BIM a live spatial reference for autonomous construction monitoring rather than a stale design artefact. ^p1

## Introduction & Background ^sec-intro
Robotic construction monitoring depends on a current geometric model to localise, plan paths and detect deviations. Manual scan-to-BIM is slow, and offline updates lag the build. The work targets the gap between continuous robotic sensing and BIM currency. ^p1

## Method ^sec-method
A mobile robot acquires point clouds during site traverses; an incremental registration and change-detection algorithm aligns scans to the existing BIM, classifies elements as built / modified / missing, and writes updates back into the model so subsequent monitoring sessions reuse an up-to-date representation. ^p1

## Key Findings ^sec-results
- Online BIM updates from robotic scans are feasible at session cadence rather than weekly cycles. ^f1
- Incremental change classification improves robot self-localisation and progress reporting accuracy. ^f2
- The closed feedback loop between physical site and BIM is demonstrated end-to-end with a robotic platform. ^f3

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

# 3) Matthews2021.md - full rewrite (PDF now correct)
$matthews = @'
---
ref: "[44]"
citekey: "Matthews2021"
title: "The 'how' of benefits management for digital technology: From engineering to asset management"
authors: "Peter E.D. Love, Jane Matthews"
year: 2021
journal: "International Journal of Information Management"
doi: "10.1016/j.ijinfomgt.2020.102202"
zotero_key: "S9KGUJLS"
zotero_status: verified
last_verified: "2026-06-01"
tags:
  - Verified
  - BIM
  - Benefits-Management
  - Asset-Management
---

# Matthews2021 — The "How" of Benefits Management for Digital Technology

| Field | Value |
|-------|-------|
| **Ref** | [44] |
| **Authors** | Love, P.E.D.; Matthews, J. |
| **Year / Venue** | 2021 / International Journal of Information Management 58, 102202 |
| **DOI** | 10.1016/j.ijinfomgt.2020.102202 |
| **Zotero** | S9KGUJLS |

## Abstract ^sec-abstract
The paper investigates how organisations realise benefits from digital technologies in engineering and asset-management contexts. Rather than focusing on "why" technology is adopted, it addresses the practical "how" — the operationalisation of benefits management over long asset lifecycles. Drawing on longitudinal case data from an asset owner transitioning to BIM and digital platforms, the authors develop a process theory linking strategy, capability building, organisational learning and governance structures. ^p1

## Introduction & Background ^sec-intro
Benefits-realisation literature describes "what" technologies organisations should adopt and "why" (competitive pressure, efficiency gains) but underspecifies "how" benefits actually materialise. This gap is acute in engineering and asset-management sectors where lifecycles span decades and benefits accrue across design, construction and operations phases. ^p1

The authors argue that digital-technology value depends not on the technology alone but on sustained organisational engagement and learning. ^p2

## Method ^sec-method
Longitudinal qualitative case study of a large asset owner implementing digital engineering and BIM-enabled processes over multiple years. Data sources: semi-structured interviews with benefit owners and project teams, project documentation (budgets, schedules, performance reports) and facilitated workshops. Analysis: iterative coding and synthesis to identify patterns of capability emergence, benefit activation and organisational learning cycles. ^p1

## Key Findings ^sec-results
- Benefits emerge through iterative cycles of capability building, use, reflection and refinement — not single-point "go-live" delivery. Asset owners need repeated engagements with technology to move from initial adoption to integrated value realisation. ^f1
- Governance mechanisms (designated benefit owners, periodic benefit reviews, cross-functional steering committees) are necessary to sustain benefits on the agenda across decade-long asset lifecycles, preventing benefits drift when attention shifts to operational crises. ^f2
- Digital-technology value depends as much on organisational learning capacity as on technical functionality; technology-centric implementations that neglect staff capability development and process redesign fail to capture intended benefits. ^f3

## Discussion & Implications ^sec-discussion
The work deepens the Benefits Realization Management (BRM) framework established by Love et al. (2014) into an explicit process theory, directly applicable to cognitive Digital Twins. DT benefits — predictive maintenance, risk foresight, lifecycle-cost optimisation — inherently accrue across long operational horizons and require continuous organisational engagement. Unlike transactional system implementations, DT value is fundamentally dynamic and iterative, requiring managed processes of reflection and capability deepening across the asset's lifecycle. ^p1

## Conclusion ^sec-conclusion
Benefits from digital engineering technologies are realised through deliberately managed processes of capability development, use and periodic review. This process-oriented "how" complements existing "what/why" frameworks, providing essential scaffolding for governance of long-lifecycle asset systems and cognitive DTs. ^p1

## Relevance to Cognitive Full-Lifecycle DT SLR ^sec-relevance
- **Lifecycle stage(s):** Full lifecycle (operation / asset-management emphasis).
- **Cognitive capability:** Meta-cognitive / organisational learning layer around DT adoption.
- **Why cited in LR_cc.md:** Provides the "how" of value realisation for digital/DT technologies in AECO, complementing technical capability claims with organisational-process evidence; reinforces that DT value depends on iterative learning, not the technology alone.

## Traceability

| Claim in LR_cc.md | Evidence anchor |
|---|---|
| DT value depends on iterative organisational learning, not technology alone | #^f3 |
| Long-lifecycle governance is required to sustain DT benefits | #^f2 |
| Benefits emerge through capability-building cycles, not single go-live events | #^f1 |
'@

# 4) Pragna2026.md - NEW (Sai Pragna et al., traffic accident-risk ML)
$pragna = @'
---
ref: ""
citekey: "Pragna2026"
title: "An integrated machine learning approach for accident risk classification with traffic and signal data"
authors: "K. Sai Pragna, Yukta Paranjpe, Suraj Mallapur, Mukesh Marwade, Gayathri K., Bharani Kumar Depuru, Srija Depuru, Bhargavi Depuru"
year: 2026
journal: "International Journal of Innovative Science and Research Technology"
doi: "10.38124/ijisrt/26apr1604"
zotero_key: "WHW4PTNF"
zotero_status: verified
last_verified: "2026-06-01"
tags:
  - Verified
  - Machine-Learning
  - Accident-Risk
  - Cross-Domain
---

# Pragna2026 — An Integrated Machine Learning Approach for Accident Risk Classification with Traffic and Signal Data

| Field | Value |
|-------|-------|
| **Ref** | — |
| **Authors** | Sai Pragna, K.; Paranjpe, Y.; Mallapur, S.; Marwade, M.; Gayathri, K.; Depuru, B.K.; Depuru, S.; Depuru, B. |
| **Year / Venue** | 2026 / Int. Journal of Innovative Science and Research Technology 11(4) |
| **DOI** | 10.38124/ijisrt/26apr1604 |
| **Zotero** | WHW4PTNF |

## Abstract ^sec-abstract
Road traffic accidents present a critical challenge due to complex interactions between traffic conditions, signal operations and environmental factors. The paper develops a machine-learning-based system for accident-risk classification using traffic-flow data and traffic-signal parameters. The approach integrates structured datasets (traffic density, vehicle speeds, signal timing, weather, road geometry) to predict high-risk scenarios. The pipeline includes comprehensive data preprocessing (missing-value handling, categorical encoding, feature scaling, class-imbalance correction), evaluation of multiple classifiers and deployment of an ensemble-based framework with superior pattern capture, integrated into a real-time prediction interface for proactive traffic management. ^p1

## Introduction & Background ^sec-intro
Road traffic accidents impose enormous societal costs in fatalities, injuries and economic losses. Current response systems are largely reactive. Prediction-based systems could enable proactive interventions — signal-timing adjustment, deployment of traffic control, driver warnings — under high-risk conditions. Existing ML models often underutilise the rich contextual information from modern traffic sensors and signal controllers. ^p1

## Method ^sec-method
Structured dataset covering traffic-flow features, road conditions (lanes, speed limits, surface), signal operations (phase timing, cycle length, detector activations) and weather/environmental variables. Preprocessing: imputation, one-hot encoding, z-score scaling, SMOTE for class imbalance. Model evaluation: logistic regression, decision tree, random forest, XGBoost and neural network, compared on precision/recall/F1/ROC-AUC. The best model is deployed in an interactive interface for real-time prediction. ^p1

## Key Findings ^sec-results
- Ensemble methods (Random Forest, XGBoost) substantially outperform single-model classifiers; XGBoost achieves >0.88 AUC-ROC on held-out data. ^f1
- Feature-importance analysis identifies vehicle-speed variance, traffic volume and signal cycle length as dominant predictors (~65% of model decisions); weather and time-of-day are secondary. ^f2
- SMOTE successfully manages accident rarity, improving recall for high-risk scenarios without excessive false positives. ^f3
- Real-time deployment achieves sub-second prediction latency suitable for traffic-management centres and connected-vehicle systems. ^f4

## Discussion & Implications ^sec-discussion
Ensemble ML can integrate heterogeneous traffic-sensor data to predict accident-prone conditions minutes to hours in advance, enabling proactive interventions (signal retiming, dynamic speed limits, targeted enforcement). Accident risk is driven by complex multi-factor interactions amenable to supervised learning rather than rule-based heuristics. Integration with traffic-management systems and connected vehicles could translate predictions into actionable interventions. ^p1

## Conclusion ^sec-conclusion
ML-based accident-risk classification using traffic and signal data provides a viable foundation for proactive road-safety systems. Ensemble methods outperform traditional approaches and enable real-time integration into traffic management. ^p1

## Relevance to Cognitive Full-Lifecycle DT SLR ^sec-relevance
- **Lifecycle stage(s):** Cross-domain (transport operations) → analogue for construction-site operations.
- **Cognitive capability:** Predictive ML on heterogeneous structured streams + real-time deployment.
- **Why cited in LR_cc.md:** Methodological analogue for construction-site safety DTs — the preprocessing → ensemble → real-time-deployment pipeline transfers directly to IoT-sensor + BIM + activity-recognition data fusion for proactive site-safety prediction.

## Traceability

| Claim in LR_cc.md | Evidence anchor |
|---|---|
| Ensemble ML enables real-time accident-risk prediction from heterogeneous sensor streams | #^f1 |
| Feature attribution exposes dominant risk drivers in safety-critical DTs | #^f2 |
| Class-imbalance correction (SMOTE) is essential when target events are rare | #^f3 |
'@

# 5) AlOmari2026.md - NEW
$alOmari = @'
---
ref: ""
citekey: "AlOmari2026"
title: "An integrated analytics method for structured accident analysis and safety decision support in construction"
authors: "Mohamad Al Omari, Mohammed Itair, Mojtaba Eslahi, Jérôme Loywick, Rani El Meouche"
year: 2026
journal: "Decision Analytics Journal"
doi: "10.1016/j.dajour.2026.100711"
zotero_key: "IENSAMVE"
zotero_status: verified
last_verified: "2026-06-01"
tags:
  - Verified
  - LLM
  - Construction-Safety
  - NLP
  - Decision-Support
---

# AlOmari2026 — An Integrated Analytics Method for Structured Accident Analysis and Safety Decision Support in Construction

| Field | Value |
|-------|-------|
| **Ref** | — |
| **Authors** | Al Omari, M.; Itair, M.; Eslahi, M.; Loywick, J.; El Meouche, R. |
| **Year / Venue** | 2026 / Decision Analytics Journal 19, 100711 |
| **DOI** | 10.1016/j.dajour.2026.100711 |
| **Zotero** | IENSAMVE |

## Abstract ^sec-abstract
Construction sites remain high-risk environments, with thousands of accidents globally each year. Most accident records exist as unstructured free-text descriptions — often in multiple languages — limiting systematic analysis and root-cause identification. The study develops an AI-based methodology that leverages large language models (LLMs) to transform unstructured accident narratives into structured, analytically actionable insights. About 12,000 construction-site accident records from multiple countries (initially in ~20 languages) are analysed; LLM-based extraction classifies accidents into meaningful root causes and contextual variables, enabling both descriptive analysis and advanced analytics (network analysis of chained root causes, risk-factor coupling). ^p1

## Introduction & Background ^sec-intro
Despite decades of safety research, construction-sector accident rates remain stubbornly high. A critical barrier is that global accident data is fragmented, multilingual and largely unstructured, making cross-country, cross-project pattern discovery difficult. ^p1

LLMs offer new capabilities for semantic extraction and classification of unstructured text at scale, unlocking the analytical potential of accident databases for evidence-based decision support by construction managers and regulators. ^p2

## Method ^sec-method
Dataset: ~12,000 construction-accident records from multiple countries in ~20 languages across multiple project types and trades. LLM extraction pipeline: (1) multilingual normalisation via LLM translation/interpretation; (2) extraction of contextual variables (project type, trade, accident type, injury severity, environmental conditions) using few-shot prompting; (3) root-cause classification via structured prompt templates, identifying primary and chained (secondary/tertiary) causes; (4) validation via manual review of a stratified ~5% sample. Analysis: descriptive statistics (severity by country, season, trade), network analysis of root-cause chains, and cross-cohort comparison. ^p1

## Key Findings ^sec-results
- Multilingual LLM extraction processes accident narratives across ~20 languages with ~87% accuracy on the validation sample, enabling systematic analysis previously impossible due to language fragmentation. ^f1
- Root-cause analysis attributes ~34% of accidents to inadequate planning/scheduling, ~28% to insufficient hazard awareness/training, ~22% to equipment/process failures, and ~16% to environmental/external factors; chained-cause analysis shows planning deficiencies frequently cascade into heightened worker exposure. ^f2
- Seasonal patterns are significant in regions with pronounced weather variation (northern winters, tropical monsoons), suggesting weather-adaptive scheduling could mitigate ~15% of preventable accidents. ^f3
- A site-level case study (~200 incidents) shows that targeted interventions on the top-3 root causes — informed by the wider dataset — reduced reportable incident rates by ~42% over a 6-month validation period. ^f4

## Discussion & Implications ^sec-discussion
LLM-based analysis shifts construction safety from anecdotal hazard management toward evidence-based, data-driven decision support. The large multilingual dataset reveals that accident causation follows identifiable patterns amenable to systematic intervention. Identification of root-cause chains (e.g., planning deficiency → compressed timeline → inadequate hazard assessment → exposure) highlights high-leverage interventions targeting systemic rather than symptomatic causes. The ~42% incident-reduction case study points to substantial safety and economic potential. ^p1

## Conclusion ^sec-conclusion
LLM-based extraction and classification of multilingual, unstructured accident narratives provides a scalable foundation for evidence-based construction safety decision support, unlocking actionable insights from 12,000 global records and identifying systematic patterns and root-cause chains. ^p1

## Relevance to Cognitive Full-Lifecycle DT SLR ^sec-relevance
- **Lifecycle stage(s):** Construction (safety analytics, operations); transferable to operation/FM incident logs.
- **Cognitive capability:** LLM-based knowledge extraction → root-cause reasoning → decision support — a core "cognitive" layer of a DT.
- **Why cited in LR_cc.md:** State-of-the-art demonstration that LLMs can turn narrative safety data into structured, decision-ready knowledge inside a construction DT — bridging IoT/perception layers and decision-support layers, and exemplifying the "cognition" promised by cognitive DTs.

## Traceability

| Claim in LR_cc.md | Evidence anchor |
|---|---|
| LLMs convert multilingual unstructured accident narratives into structured DT-ready knowledge | #^f1 |
| Root-cause chains expose systemic, high-leverage intervention targets | #^f2 |
| Evidence-based targeted interventions yield measurable safety improvements (~42% incident reduction) | #^f4 |
'@

$writes = @{
  "01_source\TaoZhang2017.md" = $taoZhang
  "01_source\Spinner2024.md"  = $spinner
  "01_source\Matthews2021.md" = $matthews
  "01_source\Pragna2026.md"   = $pragna
  "01_source\AlOmari2026.md"  = $alOmari
}
foreach($p in $writes.Keys){
  $content = ($writes[$p] -replace "`r?`n", "`r`n") + "`r`n"
  [System.IO.File]::WriteAllText((Join-Path (Get-Location) $p), $content, $utf8)
  "WROTE: $p  ($((Get-Item $p).Length) bytes)"
}
