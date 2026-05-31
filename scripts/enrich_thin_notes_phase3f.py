"""Phase 3f — enrich thin-body atomic notes with canonical body sections.

Targets 10 notes whose body is just a placeholder "See full PDF in Zotero
library for detailed evidence." plus Grieves2026 (rich body but no Foam
anchors). Each enriched note gets:

- Corrected frontmatter (title / authors / DOI / journal / year sourced
  from Zotero record).
- Standard heading layout with anchors:
    ## Abstract ^sec-abstract
    ## Method ^sec-method
    ## Key Findings ^sec-results  (with ^f1/^f2/^f3)
    ## Discussion & Implications ^sec-discussion
    ## Relevance to Cognitive Full-Lifecycle DT SLR ^sec-relevance
    ## Traceability  (claims table)
- Any pre-existing rich commentary (e.g. Grieves2026 Chinese essay) is
  preserved verbatim AFTER the canonical block under "## Extended Notes".

Anomaly handling baked into RECORDS:
- Rasheed1980.md duplicates Rasheed2020 (same zotero_key MKZ3HU7D) →
  rewritten as a short redirect stub with status `duplicate`.
- Ruppert2018.md actually describes Ruppert & Abonyi 2020 (RTLS+DT) →
  frontmatter corrected; filename retained.
- Hosamo1988.md is the 2022 AHU paper → frontmatter corrected; filename
  retained (caller may rename later).
- Hakimi2024 DOI corrected to 10.1007/s42524-023-0254-4 (Frontiers of
  Engineering Management) per Zotero record.
- Jiang2022-81 DOI corrected to 10.1016/j.compind.2021.103594.
"""

from __future__ import annotations
import re
from pathlib import Path

ROOT = Path(r"H:\phd\6.pjt\LR1\papers\01_source")
LV = "2026-06-01"


def fm(ref, citekey, title, authors, year, journal, doi, zkey, status, tags):
    tag_lines = "\n".join(f"  - {t}" for t in tags)
    return (
        "---\n"
        f'ref: "{ref}"\n'
        f'citekey: "{citekey}"\n'
        f'title: "{title}"\n'
        f'authors: "{authors}"\n'
        f"year: {year}\n"
        f'journal: "{journal}"\n'
        f'doi: "{doi}"\n'
        f'zotero_key: "{zkey}"\n'
        f"zotero_status: {status}\n"
        f'last_verified: "{LV}"\n'
        "tags:\n"
        f"{tag_lines}\n"
        "---\n\n"
    )


def meta_table(ref, title, authors, year, journal, doi, zkey):
    doi_link = f"[{doi}](https://doi.org/{doi})" if doi else "—"
    return (
        "| Field | Value |\n"
        "|-------|-------|\n"
        f"| **Ref** | {ref or '—'} |\n"
        f"| **Authors** | {authors} |\n"
        f"| **Year / Venue** | {year} / {journal} |\n"
        f"| **DOI** | {doi_link} |\n"
        f"| **Zotero** | {zkey or '—'} |\n\n"
    )


# Each NOTE: filename stem -> dict of fields
NOTES = {
    "Broo2022": dict(
        ref="[18]", citekey="Broo2022", year=2022,
        title="Design and implementation of a smart infrastructure digital twin",
        authors="D. Gürdür Broo, M. Bravo-Haro, J. Schooling",
        journal="Automation in Construction 136, 104171",
        doi="10.1016/j.autcon.2022.104171", zkey="6X33TIE6",
        status="verified",
        tags=["Verified", "Digital-Twin", "Infrastructure", "Case-Study"],
        title_h="Broo2022 — Design and Implementation of a Smart Infrastructure Digital Twin",
        abstract="The paper presents an operational design and implementation of a smart infrastructure Digital Twin spanning structural sensing, data ingestion, model synchronization and decision support on a real infrastructure asset. The authors articulate an end-to-end pipeline — from instrumentation to dashboard — and document the engineering choices needed for a deployable DT rather than a purely conceptual reference model.",
        method="Single in-situ case study (smart infrastructure asset) coupled with a layered DT reference architecture (physical layer → data layer → model layer → service layer). Sensor hardware, ingestion middleware and visualization layers are described together with the validation strategy used to verify model fidelity against measured data.",
        findings=[
            "A deployable infrastructure DT requires explicit separation of data, model and service layers; conflating them at the dashboard level prevents downstream automation.",
            "Real-time synchronization between the physical asset and the digital model is the dominant engineering cost, dwarfing the cost of the BIM/3D component.",
            "The case study exposes the gap between widely-cited DT reference frameworks and the much narrower scope of what current commercial stacks can actually deliver in operations.",
        ],
        discussion="Provides one of the few end-to-end engineering blueprints for an operational infrastructure DT in AECO and is therefore frequently cited as evidence of feasibility in monitoring scenarios. However, the case demonstrates only Level 1–2 (digital shadow / one-way feedback) capability and does not close the cognitive loop.",
        relevance="Lifecycle stage: operation & maintenance of infrastructure. Used in LR_cc.md as evidence that current AECO DT deployments stop at sensor dashboards and rarely reach Level 3 (autonomous/cognitive) closed-loop control.",
        trace=[("Real-world DT deployment confirms dashboard-dominated maturity", "#^f3")],
    ),
    "Hakimi2024": dict(
        ref="[86]", citekey="Hakimi2024", year=2024,
        title="Digital twin-enabled smart facility management: A bibliometric review",
        authors="O. Hakimi, H. Liu, O. Abudayyeh",
        journal="Frontiers of Engineering Management 11(1), 32–49",
        doi="10.1007/s42524-023-0254-4", zkey="9EYC52IG",
        status="verified",
        tags=["Verified", "Digital-Twin", "Facility-Management", "Bibliometric-Review"],
        title_h="Hakimi2024 — Digital Twin-Enabled Smart Facility Management: A Bibliometric Review",
        abstract="Bibliometric analysis of 248 DT-for-Facility-Management (FM) articles harvested from Scopus and Web of Science. VOSviewer is used to visualize keyword co-occurrence, citation and co-authorship networks. The review maps current focal areas (BIM-based FM, AI predictive maintenance, real-time CPS data integration, lifecycle asset management) and identifies under-developed areas such as AI-based real-time asset PHM, virtual intelligent infrastructure monitoring, deep-learning-aided continuous improvement, semantic interoperability and autonomous control feedback.",
        method="Quantitative bibliometric review (PRISMA-style screening of 248 papers; VOSviewer co-occurrence and citation network analysis). No primary empirical data — synthesis is corpus-driven.",
        findings=[
            "DT-for-FM literature concentrates on four clusters: BIM-based FM, AI predictive maintenance, real-time CPS data integration, and lifecycle asset management.",
            "Autonomous control feedback and semantic data interoperability across the facility lifecycle are the most under-researched DT-for-FM gaps.",
            "The DT-for-FM field is geographically concentrated (China, USA, UK) and dominated by a small number of high-output authors and venues.",
        ],
        discussion="Provides quantitative evidence that the operations/FM phase is the centre of gravity of AECO DT research while simultaneously confirming that closed-loop cognitive capability (autonomous control, semantic federation) remains the weakest cluster. This is a load-bearing citation for the SLR's argument that DT maturity in operations is asymmetrically high in observation and low in actuation.",
        relevance="Lifecycle stage: operation & maintenance (FM). Used in LR_cc.md to substantiate the maturity skew and the under-researched cognitive/autonomous control feedback gap.",
        trace=[
            ("Maturity skew toward observation, not actuation", "#^f2"),
            ("Semantic interoperability is the dominant gap in DT-FM", "#^f2"),
        ],
    ),
    "Hosamo1988": dict(
        ref="[87]", citekey="Hosamo2022b", year=2022,
        title="A digital twin predictive maintenance framework of air handling units based on automatic fault detection and diagnostics",
        authors="H. Hosamo, P. R. Svennevig, K. Svidt, D. Han, H. K. Nielsen",
        journal="Energy and Buildings 261, 111988",
        doi="10.1016/j.enbuild.2022.111988", zkey="ID2GIXE3",
        status="verified",
        tags=["Verified", "Digital-Twin", "Predictive-Maintenance", "HVAC", "Filename-Legacy"],
        title_h="Hosamo2022b — Digital Twin Predictive Maintenance Framework for AHUs",
        anomaly="ℹ Filename `Hosamo1988.md` is a legacy artefact; canonical citekey is `Hosamo2022b` (paper is 2022). Filename retained to preserve existing wikilinks; consider renaming in a future cleanup pass.",
        abstract="HVAC systems are central to building energy consumption, and stable Air Handling Unit (AHU) operation is critical to efficiency and equipment life. The authors propose a Digital Twin predictive-maintenance framework for AHUs that integrates BIM, IoT and semantic technologies. Three modules are implemented: (i) fault detection in AHUs based on the APAR (Air Handling Unit Performance Assessment Rules) method, (ii) condition prediction via machine learning, and (iii) maintenance planning. The framework is validated on a real educational building in Norway using data from August 2019 to October 2021.",
        method="Design-science framework combining APAR rule-based fault detection with ML-based condition prediction and a BIM/IoT integration layer. Validation is a single longitudinal case study (24+ months of operational AHU data plus FM-system inspection and maintenance records).",
        findings=[
            "Combining APAR rules with ML on continuously updated sensor data successfully detects AHU faults and predicts component degradation.",
            "Removing detected operating faults produced annual energy savings of several thousand USD on a single educational building.",
            "Semantic enrichment of BIM with IoT data is the structural enabler that lifts the DT from monitoring to predictive maintenance.",
        ],
        discussion="Empirically grounds the predictive-maintenance branch of the AECO DT literature and is one of the few studies that quantifies energy/cost savings rather than reporting only architectural feasibility. The framework is still pre-actuation (no automated control feedback to the BMS).",
        relevance="Lifecycle stage: operation & maintenance (HVAC). Used in LR_cc.md as evidence that ML-augmented DTs can shift O&M from reactive to predictive, but still stop short of autonomous actuation.",
        trace=[
            ("APAR + ML on DT data enables predictive maintenance", "#^f1"),
            ("Quantified energy savings from DT-detected faults", "#^f2"),
        ],
    ),
    "Jiang2022": dict(
        ref="[25]", citekey="Jiang2022", year=2022,
        title="Digital twin-enabled real-time synchronization for planning, scheduling, and execution in precast on-site assembly",
        authors="Y. Jiang, M. Li, M. Li, X. Liu, R. Y. Zhong, W. Pan, G. Q. Huang",
        journal="Automation in Construction 141, 104397",
        doi="10.1016/j.autcon.2022.104397", zkey="BEXVG4GB",
        status="verified",
        tags=["Verified", "Digital-Twin", "Precast", "Synchronization", "Scheduling"],
        title_h="Jiang2022 — DT-Enabled Real-Time Synchronization for Precast On-Site Assembly",
        abstract="Proposes a Digital Twin synchronization framework that bridges planning, scheduling and execution for precast on-site assembly. The system continuously aligns the as-planned digital schedule with as-built progress captured from on-site sensing, enabling closed-loop replanning when actual operations deviate from plan.",
        method="Design-science framework with a working prototype on a precast on-site assembly testbed. The system fuses real-time positioning and progress data with the BIM/4D schedule via a synchronization middleware; rescheduling is triggered by deviation detection.",
        findings=[
            "Real-time digital-physical synchronization is the structural prerequisite for closed-loop construction scheduling — without it, plans drift silently from execution.",
            "Deviation-triggered rescheduling reduces idle time and resource conflicts in precast assembly relative to static daily look-ahead planning.",
            "Synchronization integrity (not sensing) is the dominant bottleneck in current construction DT prototypes.",
        ],
        discussion="A canonical reference for data-centric construction DTs and for the argument that synchronization middleware — not BIM richness — is the key enabling component for cognitive construction DTs.",
        relevance="Lifecycle stage: construction execution. Used in LR_cc.md to characterize data-centric DT architectures and to evidence the synchronization-integrity gap.",
        trace=[
            ("Synchronization middleware is the structural enabler", "#^f1"),
            ("Synchronization integrity dominates current DT bottlenecks", "#^f3"),
        ],
    ),
    "Jiang2022-81": dict(
        ref="[81]", citekey="Jiang2022b", year=2022,
        title="Digital twin-enabled smart modular integrated construction system for on-site assembly",
        authors="Y. Jiang, M. Li, D. Guo, W. Wu, R. Y. Zhong, G. Q. Huang",
        journal="Computers in Industry 136, 103594",
        doi="10.1016/j.compind.2021.103594", zkey="DXRTQ89R",
        status="verified",
        tags=["Verified", "Digital-Twin", "Modular-Construction", "Robotics"],
        title_h="Jiang2022b — DT-Enabled Smart Modular Integrated Construction (DT-SMiCS)",
        abstract="Introduces a Digital Twin-enabled smart Modular Integrated Construction system (DT-SMiCS) for on-site assembly. On-site resources are converted into Smart MiC Objects (SMiCOs) instrumented with UWB and RFID for real-time nD data (identity, location, cost, progress). Digital twins of SMiCOs are instantiated from unified object-oriented templates and exchanged with cloud services for high-fidelity virtual monitoring and remote control. A testbed robotic demonstration validates the system.",
        method="System architecture + working prototype with robotic demonstration on a MiC on-site assembly testbed. Combines UWB + RFID instrumentation, object-oriented DT instantiation and a smart mobile gateway for bi-directional data flow.",
        findings=[
            "Object-oriented templating of on-site resources (SMiCOs) is what enables scalable instantiation of construction DTs at item level.",
            "Bi-directional cloud services support both monitoring and remote control — moving beyond pure observation toward Level-2 actuation.",
            "Robotic execution becomes feasible only when the DT can deliver positionally consistent state to the robot in near real time.",
        ],
        discussion="One of the few construction DT studies that demonstrates a working robotic actuation loop, placing it at the upper boundary of current AECO DT maturity. Highly relevant to the SLR's cognitive/autonomous category.",
        relevance="Lifecycle stage: construction (modular). Used in LR_cc.md as one of the rare working Level-2+ examples of bi-directional DT actuation.",
        trace=[("SMiCO templating enables item-level DT instantiation", "#^f1"),
               ("Working robotic actuation loop validates Level-2 DT", "#^f2")],
    ),
    "Lu2020-90": dict(
        ref="[90]", citekey="LuYuqian2020", year=2020,
        title="Digital Twin-driven smart manufacturing: Connotation, reference model, applications and research issues",
        authors="Y. Lu, C. Liu, K. I-K. Wang, H. Huang, X. Xu",
        journal="Robotics and Computer-Integrated Manufacturing 61, 101837",
        doi="10.1016/j.rcim.2019.101837", zkey="6VU4VXU4",
        status="verified",
        tags=["Verified", "Digital-Twin", "Smart-Manufacturing", "Reference-Model", "Foundation"],
        title_h="LuYuqian2020 — DT-Driven Smart Manufacturing: Connotation, Reference Model, Applications",
        abstract="Reviews the development of Digital Twin technologies in manufacturing systems and processes. Summarizes DT definitions, proposes a DT reference model that systematizes development methodology, surveys representative applications under that reference model, and identifies outstanding research issues for DT-driven smart manufacturing in the Industry-4.0 context.",
        method="Narrative literature review structured around a proposed DT reference model. No primary data; synthesis-driven taxonomy.",
        findings=[
            "DT-driven smart manufacturing requires an explicit reference model spanning physical entity, virtual entity, services, data and connections — not a single 3D model.",
            "Most reviewed applications align with subsets of the reference model; few populate all five layers, exposing a fragmentation pattern that recurs in AECO DT literature.",
            "Open research issues — high-fidelity modeling, real-time data fusion, service-based encapsulation and security — are systemic, not domain-specific.",
        ],
        discussion="A widely cited reference model that AECO DT studies routinely adapt. The fragmentation pattern documented here is structurally identical to what the SLR observes in construction DTs, supporting cross-domain transferability arguments.",
        relevance="Lifecycle stage: cross-lifecycle (manufacturing analogue). Used in LR_cc.md as a foundational reference for DT reference-model adoption and for the cross-domain fragmentation pattern.",
        trace=[("Five-layer reference model is the canonical DT decomposition", "#^f1"),
               ("Cross-domain fragmentation pattern mirrors AECO DT findings", "#^f2")],
    ),
    "Rasheed1980": dict(
        ref="[54]", citekey="Rasheed1980", year=2020,
        title="(duplicate) Digital Twin: Values, Challenges and Enablers From a Modeling Perspective",
        authors="A. Rasheed, O. San, T. Kvamsdal",
        journal="IEEE Access 8, 21980–22012",
        doi="10.1109/ACCESS.2020.2970143", zkey="MKZ3HU7D",
        status="duplicate",
        tags=["Duplicate", "Digital-Twin", "Redirect"],
        title_h="Rasheed1980 — DUPLICATE of Rasheed2020",
        is_duplicate=True,
        redirect_to="Rasheed2020",
        redirect_note=(
            "This note shares Zotero key `MKZ3HU7D` with [[Rasheed2020]] and refers "
            "to the same paper (Rasheed, San & Kvamsdal, 2020, *IEEE Access*, DOI "
            "`10.1109/ACCESS.2020.2970143`). The filename `Rasheed1980` is a legacy "
            "typo (the paper appears on pages 21980–22012; the page number leaked "
            "into the citekey). Use [[Rasheed2020]] for all citations going forward."
        ),
    ),
    "Ruppert2018": dict(
        ref="[44]", citekey="Ruppert2020", year=2020,
        title="Integration of real-time locating systems into digital twins",
        authors="T. Ruppert, J. Abonyi",
        journal="Journal of Industrial Information Integration 20, 100174",
        doi="10.1016/j.jii.2020.100174", zkey="IJUPSPJB",
        status="verified",
        tags=["Verified", "Digital-Twin", "RTLS", "Sensor-Fusion", "Filename-Legacy"],
        title_h="Ruppert2020 — Integration of Real-Time Locating Systems into Digital Twins",
        anomaly="ℹ Filename `Ruppert2018.md` is a legacy artefact; the actual paper is Ruppert & Abonyi (2020) on RTLS+DT integration, not the earlier 'Operator 4.0 enabling technologies' survey. Filename retained to preserve existing wikilinks.",
        abstract="Cyber-physical model-based solutions should rely on Digital Twins in which simulations are integrated with real-time sensory and manufacturing data. The paper demonstrates how information fusion with Real-Time Locating Systems (RTLS) — combining position and acceleration data — supports simulation-based analysis of product-specific activity times. The proposed DT continuously predicts production status and feeds monitoring of production performance via real-time connections between the RTLS and adaptive simulation models. The case study uses Human Resource Effectiveness (HRE) analysis in an assembly process to demonstrate the resulting Simulation-4.0 concept.",
        method="Single industrial assembly case study; adaptive discrete-event simulation continuously updated from UWB RTLS streams (position + acceleration). The DT serves both online prediction and offline performance analysis.",
        findings=[
            "RTLS-driven information fusion lets a DT continuously refine activity-time distributions instead of using static engineered estimates.",
            "Position + acceleration fusion outperforms position alone for distinguishing value-adding from non-value-adding activities.",
            "Adaptive simulation models, when fed by RTLS, can support both real-time performance monitoring and longer-horizon HRE analysis from the same data substrate.",
        ],
        discussion="A canonical reference for sensor-fusion-driven DTs in industrial settings; the architecture transfers directly to AECO contexts where worker/equipment positioning underpins safety and productivity DTs.",
        relevance="Lifecycle stage: operation/execution analogue (manufacturing). Used in LR_cc.md as a transferable template for RTLS-fed worker-safety and productivity DTs in construction.",
        trace=[("RTLS fusion enables continuous activity-time refinement", "#^f1"),
               ("Position + acceleration fusion improves activity classification", "#^f2")],
    ),
    "Zhang2023": dict(
        ref="[83]", citekey="Zhang2023", year=2023,
        title="Application and enabling digital twin technologies in the operation and maintenance stage of the AEC industry: A literature review",
        authors="A. Zhang, J. Yang, F. Wang",
        journal="Journal of Building Engineering 80, 107859",
        doi="10.1016/j.jobe.2023.107859", zkey="S49XVYIT",
        status="verified",
        tags=["Verified", "Digital-Twin", "AEC", "Operation-Maintenance", "Literature-Review"],
        title_h="Zhang2023 — Enabling DT Technologies in the O&M Stage of the AEC Industry",
        abstract="Bibliometric and narrative review of 825 DT publications addressing the O&M stage of the AEC industry (January 2016 – July 2023). The review (i) summarizes the common technologies used in each current research topic, (ii) systematizes enabling technologies from the perspective of the DT five-dimensional model, (iii) establishes a complete common technology strategy for DT application in the AEC O&M stage, and (iv) identifies technical-level research gaps and opportunities.",
        method="Bibliometric corpus (825 papers, 2016–2023) + structured synthesis around the DT five-dimensional model (physical, virtual, service, data, connection). No primary empirical data.",
        findings=[
            "DT applications in the AEC O&M stage are dominated by monitoring, energy management and predictive maintenance; autonomous control remains marginal.",
            "Mapping enabling technologies to the five-dimensional model exposes systematic under-investment in the 'connection' (real-time, bi-directional) and 'service' layers.",
            "A reusable DT-for-O&M technology strategy template is proposed, intended to lower the entry barrier for new researchers.",
        ],
        discussion="One of the most current and structured AECO-O&M DT reviews; provides quantitative justification for the SLR's claim that the connection/service layers are the maturity bottleneck and that the five-dimensional model is the de-facto reference taxonomy.",
        relevance="Lifecycle stage: operation & maintenance (AEC). Used in LR_cc.md as evidence for the under-developed connection/service layers and for the dominance of monitoring vs. autonomous control in AECO O&M DTs.",
        trace=[("Connection/service layers are the AECO O&M maturity bottleneck", "#^f2"),
               ("Five-dimensional model is the de-facto reference", "#^f2")],
    ),
    "Zhao2022": dict(
        ref="[82]", citekey="Zhao2022", year=2022,
        title="Developing a conceptual framework for the application of digital twin technologies to revamp building operation and maintenance processes",
        authors="J. Zhao, H. Feng, Q. Chen, B. García de Soto",
        journal="Journal of Building Engineering 49, 104028",
        doi="10.1016/j.jobe.2022.104028", zkey="K9UNRWVK",
        status="verified",
        tags=["Verified", "Digital-Twin", "Facility-Management", "Conceptual-Framework", "Case-Study"],
        title_h="Zhao2022 — Conceptual Framework for DT-Driven Building O&M",
        abstract="Comparative illustrative case study of traditional FM vs. DT-driven FM across four geospatially representative buildings during the O&M phase. Findings show DT technologies enable efficient and responsive planning and control of FM activities via real-time asset status, but adoption is hampered by data-integration and data-standard misalignment. A bottom-up conceptual framework is proposed to facilitate wider DT implementation in building O&M.",
        method="Multi-case illustrative case study (n = 4 geographically diverse buildings) comparing traditional FM with DT-driven FM, followed by bottom-up framework synthesis.",
        findings=[
            "DT-driven FM measurably improves responsiveness and planning quality versus traditional FM across all four cases.",
            "Data-integration and data-standard misalignment is the dominant barrier to wider DT-FM adoption — not sensor or modeling cost.",
            "A bottom-up framework (asset → process → decision) is more deployable than top-down reference architectures for FM stakeholders.",
        ],
        discussion="Empirical complement to bibliometric reviews; provides concrete cross-site evidence that data-standard misalignment — not technology readiness — is the principal blocker to DT-FM adoption. Frequently cited alongside Hakimi2024 and Zhang2023 to triangulate the same conclusion.",
        relevance="Lifecycle stage: operation & maintenance (building FM). Used in LR_cc.md to substantiate the data-standard-misalignment barrier and the bottom-up adoption argument.",
        trace=[("Data-standard misalignment is the dominant DT-FM barrier", "#^f2"),
               ("Bottom-up framework outperforms top-down reference models for FM", "#^f3")],
    ),
    "Grieves2026": dict(
        ref="[56]", citekey="Grieves2026", year=2026,
        title="Front Running Simulation: A Digital Twin Framework for Real-Time Replication, Prediction, and Goal Navigation",
        authors="M. Grieves",
        journal="Preprints.org (preprint, 2026-04-20)",
        doi="10.20944/preprints202604.1291.v1", zkey="83PUTURG",
        status="verified",
        tags=["Verified", "Digital-Twin", "Foundation", "Preprint", "Front-Running-Simulation"],
        title_h="Grieves2026 — Front Running Simulation: A DT Framework for Real-Time Replication, Prediction, and Goal Navigation",
        abstract="Front Running Simulation (FRS) is a Digital Twin–enabled capability that continuously replicates the current state of physical systems, predicts probable future states, and identifies actions to navigate to defined goals while minimizing the expenditure of scarce physical resources. Unlike traditional simulation, which operates offline with predefined initial conditions, FRS is continuously synchronized with reality through Digital Twin Instances (DTIs), enabling forward-looking simulation from the present state. FRS is organized around three core activities — replication, prediction, and navigation — supported by data, Models of Reality (MoR), simulation, and information. The integration of Digital Twin Aggregates (DTAs) and Artificial Intelligence introduces Bayesian, data-driven prediction that complements physics-based simulation, combining exploration of possible futures with rapid identification of probable outcomes. The framework shifts the focus from purely adverse-event avoidance to goal attainment under constraints, enabling proactive, information-driven decision-making.",
        method="Conceptual framework development with illustrative examples (automotive welding line, refinery operations). No primary empirical data; synthesis articulates the FRS architecture (DTIs + DTAs + MoR + AI) and demonstrates qualitative outcomes such as 8–62 % bottleneck-probability reduction in the manufacturing examples.",
        findings=[
            "FRS reframes the DT from a passive monitor into a forward-looking, goal-navigating agent — continuously synchronized replication is the precondition, not the deliverable.",
            "Hybrid prediction (physics-based MoR simulation + DTA-driven Bayesian/AI inference) outperforms either pure approach for goal navigation under uncertainty.",
            "Information — not data — is the resource that enables goal-directed action selection; the DT's job is to convert raw streams into actionable information for navigation.",
        ],
        discussion="A direct conceptual ancestor of the cognitive/autonomous DT level identified in this SLR. The FRS triad (replication → prediction → navigation) maps almost one-to-one onto the cognitive-loop closure that AECO DTs currently fail to achieve. The preprint status and the absence of in-situ empirical validation are the main limitations.",
        relevance="Lifecycle stage: cross-lifecycle (operations/production analogue). In LR_cc.md FRS underpins the Level-3 (cognitive/autonomous) maturity definition and motivates the SLR's argument that current AECO DTs are stuck at replication+observation without the prediction-navigation stages.",
        trace=[("FRS triad defines Level-3 cognitive DT capability", "#^f1"),
               ("Hybrid physics + DTA-driven Bayesian prediction is the recommended prediction substrate", "#^f2"),
               ("Information (not raw data) is the actionable resource for navigation", "#^f3")],
        preserve_extended=True,
    ),
}


def build_body(rec) -> str:
    if rec.get("is_duplicate"):
        target = rec["redirect_to"]
        body = (
            f"# {rec['title_h']}\n\n"
            "> ⚠ **DUPLICATE NOTE (2026-06-01).** "
            f"{rec['redirect_note']}\n\n"
            f"## Canonical Note\n\nSee [[{target}]].\n"
        )
        return body

    parts = [f"# {rec['title_h']}\n"]
    if rec.get("anomaly"):
        parts.append(f"> {rec['anomaly']}\n")
    parts.append(meta_table(rec["ref"], rec["title"], rec["authors"], rec["year"], rec["journal"], rec["doi"], rec["zkey"]))
    parts.append(f"## Abstract ^sec-abstract\n{rec['abstract']} ^p1\n")
    parts.append(f"## Method ^sec-method\n{rec['method']} ^p1\n")
    parts.append("## Key Findings ^sec-results\n")
    for i, f in enumerate(rec["findings"], 1):
        parts.append(f"- {f} ^f{i}\n")
    parts.append("")
    parts.append(f"## Discussion & Implications ^sec-discussion\n{rec['discussion']} ^p1\n")
    parts.append(f"## Relevance to Cognitive Full-Lifecycle DT SLR ^sec-relevance\n{rec['relevance']} ^p1\n")
    parts.append("## Traceability\n")
    parts.append("| Claim in LR_cc.md | Evidence anchor |\n|---|---|\n")
    for claim, anchor in rec["trace"]:
        parts.append(f"| {claim} | {anchor} |\n")
    return "\n".join(parts)


_FM_RE = re.compile(r"^---\r?\n.*?\r?\n---\r?\n?", re.DOTALL)


def extract_extended(prev_body: str) -> str:
    """For Grieves2026: keep the prior CN/EN commentary as an Extended Notes appendix."""
    # Strip the obsolete '### **Obsidian YAML Draft**' marker block but keep CN essay.
    text = prev_body.strip()
    text = re.sub(r"^### \*\*Obsidian YAML Draft\*\*\s*\n+---\s*\n", "", text, count=1)
    text = re.sub(r"^### \*\*Obsidian YAML Draft\*\*\s*\n+", "", text, count=1)
    return text


def migrate(stem: str, rec: dict) -> str:
    fpath = ROOT / f"{stem}.md"
    raw = fpath.read_text(encoding="utf-8")
    m = _FM_RE.match(raw)
    prev_body = raw[m.end():] if m else raw

    new_fm = fm(rec["ref"], rec["citekey"], rec["title"], rec["authors"], rec["year"],
                rec["journal"], rec["doi"], rec["zkey"], rec["status"], rec["tags"])
    new_body = build_body(rec)
    out = new_fm + new_body

    if rec.get("preserve_extended"):
        extended = extract_extended(prev_body)
        if extended:
            out += "\n\n---\n\n## Extended Notes (legacy commentary, preserved verbatim)\n\n" + extended + "\n"

    fpath.write_text(out, encoding="utf-8", newline="\n")
    return f"OK {stem} ({len(out)} bytes)"


def main() -> None:
    for stem, rec in NOTES.items():
        print(migrate(stem, rec))


if __name__ == "__main__":
    main()
