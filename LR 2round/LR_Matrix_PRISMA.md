# LR_Matrix — PRISMA 2020 Full Reconciliation (Round 2)
## Cognitive Full-Lifecycle Digital Twin Framework for the AECO Industry

> **Companion document to LR.md (Round 2)**
> Round-2 reconciliation of the **748 records** identified from the Lens.org search
> (single source), screened down to **424 records retained for full-text review**.
> **Last updated:** 20 Jun 2026 (identification tagging + duplicate merge + Phase 1–4 tripartite update)
>
> ### Status Tags (Round 2)
> | Emoji | PRISMA Stage | Count |
> |:---:|---|:---:|
> | 🟢 | **RETAINED** for full-text review (→ atomic notes in `01_source/`) | 424 |
> | 🔴 | **EXCLUDED** at title/abstract screening | 320 |
> | ⚫ | **DUPLICATES** removed | 4 |
> | ⏳ | **FULL-TEXT SYNTHESIS** (deep notes + qualitative inclusion) | in progress |
>
> **Identification provenance (PRISMA 2020).** Every atomic note in `01_source/` is tagged:
> - `identification: databases` — DOI found in Lens.org export [2round748.csv](csv/2round748.csv) (n = 748 → 424 retained)
> - `identification: other methods` — round-1 corpus, backward citation chaining, supplementary references
>
> **✅ Auditable provenance.** Unlike round 1, every round-2 count below is reconstructable
> from workspace artefacts: the Lens.org export [2round748.csv](csv/2round748.csv) (748 records),
> the screening decision log, and the retained set
> [retained_for_fulltext.csv](csv/retained_for_fulltext.csv) (424 records). The Boolean query and
> filters are documented in [Lens filter condition.md](Lens%20filter%20condition.md).
>
**Scope note.** Section 1 (PRISMA 2020 Flow) and the Screening Summary are the current, auditable record (748 Lens.org records --> 424 retained). **Section 8 is the auto-generated Master Reference Index** of all 526 atomic notes in `01_source/` (432 `identification: databases` + 94 `identification: other methods`). **Sections 2-7 document the qualitative synthesis corpus (69 included studies)** and excluded-study register; these sections are being progressively updated as round-2 full-text synthesis (Phase B) advances.
>
> ### Maturity Codes
> ML1 = Digital Shadow (unidirectional) · ML2 = Cyber-Physical Interface (bidirectional, human-mediated) · ML3 = Cognitive/Autonomous

---


## 1. PRISMA 2020 Flow Reconciliation (Round 2 — auditable)

Single-source search executed on **Lens.org**. Query, year window (2015–2026),
publication-type, external-ID (DOI) and subject filters are documented verbatim in
[Lens filter condition.md](Lens%20filter%20condition.md).

| Stage              | Description                                                |       n | Cumulative |
| ------------------ | ---------------------------------------------------------- | ------: | ---------: |
| **Identification** | Records identified from databases (Lens.org)               |     748 |        748 |
|                    | Records identified from other methods (snowballing, prior) |     ~94 |       ~842 |
| **Deduplication**  | Duplicate records removed                                  |      −4 |        744 |
| **Screening**      | Records screened on title & abstract (3-vector criteria)   |     744 |        744 |
|                    | Records excluded at screening                              |    −320 |        424 |
| **Retained**       | **Records retained for full-text review** (→ `01_source/`) | **424** |    **424** |
| **Eligibility**    | Full-text reports assessed for eligibility                 |       ⏳ |          — |
| **Included**       | Studies included in qualitative synthesis                  |       ⏳ |          — |

> **Screening criteria (3 vectors).** A record was retained only if it satisfied all three:
> **V1 — Digital Twin / CPS / BIM-integration** core relevance; **V2 — AECO / built-asset**
> domain; **V3 — method** (safety, DfS, PtD, quality, DfQ, or sustainability focus). Records
> were excluded when they failed a vector or were dominated by an out-of-domain application.

### Round-2 Screening Summary (exclusions, n = 320)

| Exclusion reason | n |
|---|:---:|
| No DT / CPS / BIM-integration core (fails V1) | 163 |
| Dominant out-of-domain application | 54 |
| No AECO / built-asset relevance (fails V2) | 52 |
| Record type ineligible (editorial, erratum, retracted, etc.) | 21 |
| Out-of-domain **and** no AECO relevance | 15 |
| Energy/HVAC-only, no construction-phase or lifecycle continuity (EC2) | 15 |
| **Total excluded at screening** | **320** |

> **Arithmetic check:** 4 (duplicates) + 320 (excluded) + 424 (retained) = **748** ✓
> Exclusion sub-reasons: 163 + 54 + 52 + 21 + 15 + 15 = **320** ✓

### Round-2 retained set — descriptive profile (n = 424)

| Dimension | Breakdown |
|---|---|
| Publication type | journal article 419 · conference proceedings article 5 |
| Year | 2026: 87 · 2025: 128 · 2024: 73 · 2023: 54 · 2022: 37 · 2021: 25 · 2020: 12 · 2019: 8 |
| Abstract available in export | yes 356 · no 68 (full text required to complete the note) |
| Atomic notes generated | 424 in [01_source/](01_source) (provenance tag `source: lens`) |

> **Other methods:** Backward citation chaining (snowballing) and the round-1 corpus
> (`source: scholar` notes) remain available as supplementary evidence threads.

---

> **Sections 2-7 below document the qualitative synthesis corpus (69 included studies) and excluded-study groupings.** These sections are maintained as the active analytical baseline and are progressively updated as round-2 full-text synthesis advances.

---


## 2. 🟢 INCLUDED — Qualitative Synthesis Corpus (n = 69)

Grouped by thematic cluster (Table 2 of LR_cc.md). Each study met **all** inclusion criteria (IC1–IC3) and scored ≥ 2.5 on the quality appraisal rubric (Table 1).

> **Count correction:** the original corpus listed 70 studies, but ref [90] (Lu et al. 2020)
> is a true duplicate of [57] (same Zotero key). It is struck through below and excluded
> from the count, giving **69** unique included studies. See §8 for the verification map.

---

### 2.1 BIM-to-DT Architecture & Data Assimilation (n = 17)

| Ref | Authors | Year | Title | Journal | ML | QA |
|:---:|---|:---:|---|---|:---:|:---:|
| [1] | Wang, Gan, Hu & Liu | 2022 | DT-enabled built environment sensing via SensorML | Autom. Constr. | ML1 | 4.0 |
| [2] | Akhavian et al. | 2025 | BIM2RDT: Agentic AI Safety-First Framework | arXiv preprint | ML3 | 3.0 |
| [6] | Deng, Menassa & Kamat | 2021 | From BIM to DTs: evolution in AEC-FM industry | ITcon | — | 3.5 |
| [7] | Jiang et al. | 2021 | DT and its implementations in civil engineering | Autom. Constr. | — | 4.0 |
| [8] | Tang et al. | 2019 | BIM and IoT devices integration: review | Autom. Constr. | — | 4.0 |
| [11] | Spinner & Degani | 2024 | Online as-built BIM update for robotic monitoring | J. Intell. Robot. Syst. | ML2 | 3.0 |
| [25] | Jiang et al. | 2022 | DT-enabled real-time sync for precast assembly | Autom. Constr. | ML2 | 4.0 |
| [33] | Opoku et al. | 2021 | DT application in construction: lit. review | J. Build. Eng. | — | 4.0 |
| [34] | Kaewunruen & Xu | 2019 | DT aided sustainability for railway turnout | J. Cleaner Prod. | ML2 | 4.0 |
| [36] | Sepasgozar | 2020 | DT and web-based gaming for construction ed. | Applied Sciences | — | 2.5 |
| [40] | Holmstrom et al. | 2010 | Rapid manufacturing in spare parts supply chain | JMTM | — | 2.5 |
| [51] | Akinci, Fischer & Kunz | 2002 | Automated generation of work spaces | JCEM | — | 3.0 |
| [55] | Glaessgen & Stargel | 2012 | DT paradigm for NASA/USAF vehicles | AIAA Conf. | — | 4.0 |
| [56] | Grieves & Vickers | 2017 | DT: Mitigating emergent behavior in complex systems | Springer Book Ch. | — | 4.0 |
| [57] | Lu et al. | 2020 | DT-driven smart manufacturing: reference model | Robot. CIM | — | 4.5 |
| [58] | Tao & Zhang | 2017 | DT shop-floor: a new paradigm | IEEE Access | — | 4.0 |
| [74] | Omrany et al. | 2023 | DTs in construction: comprehensive review | Sustainability | — | 4.0 |
| ~~[90]~~ | ~~Lu et al.~~ | ~~2020~~ | ~~DT-driven smart manufacturing (duplicate of [57])~~ | ~~Robot. CIM~~ | ~~—~~ | ~~4.5~~ |

> ~~[90]~~ removed as a **true duplicate of [57]** (same Zotero key `6VU4VXU4`); excluded from the n = 17 count.

### 2.2 Semantic Interoperability & Ontologies (n = 14)

| Ref | Authors | Year | Title | Journal | ML | QA |
|:---:|---|:---:|---|---|:---:|:---:|
| [5] | Boje et al. | 2020 | Towards a semantic Construction Digital Twin | Autom. Constr. | ML3(c) | 4.0 |
| [10] | Theiler, Smarsly & Dragos | 2018 | IFC Monitor for structural health monitoring | Adv. Eng. Inform. | — | 3.5 |
| [17] | Zhang, Boukamp & Teizer | 2015 | Ontology-based semantic modeling for JHA | Autom. Constr. | — | 4.5 |
| [20] | Hossain et al. | 2018 | DfS knowledge library for BIM safety reviews | Autom. Constr. | ML2 | 4.0 |
| [39] | Whyte & Hartmann | 2017 | How digitizing building info transforms the BE | Build. Res. & Info. | — | 3.5 |
| [43] | Davies & Harty | 2013 | Implementing 'Site BIM': hospital case study | Autom. Constr. | — | 3.5 |
| [44] | Love & Matthews | 2021 | Benefits management for digital technology | IJIM | — | 4.0 |
| [52] | Zhang & El-Gohary | 2016 | Semantic NLP for automated regulatory compliance | J. Comp. Civ. Eng. | — | 3.5 |
| [64] | Kahneman, Sibony & Sunstein | 2021 | Noise: A Flaw in Human Judgment | Book — Little, Brown | — | 4.0 |
| [65] | Love et al. | 2014 | Benefits realization management BIM framework | Autom. Constr. | — | 3.5 |
| [66] | Tixier et al. | 2016 | NLP for construction safety precursor extraction | Autom. Constr. | — | 3.5 |
| [71] | Jones et al. | 2020 | Characterising the Digital Twin: SLR | CIRP JMST | — | 4.5 |
| [72] | Sepasgozar | 2021 | Differentiating DT from Digital Shadow | Buildings | ML1–3 | 3.5 |
| [73] | Ozturk | 2021 | DT Research in AECO-FM Industry | J. Build. Eng. | — | 4.0 |

### 2.3 Perception, Registration & Computer Vision (n = 12)

| Ref | Authors | Year | Title | Journal | ML | QA |
|:---:|---|:---:|---|---|:---:|:---:|
| [3] | Glatt et al. | 2021 | DT of material flows based on physics simulation | J. Manuf. Syst. | ML2 | 4.0 |
| [4] | Hamel, Ahsan & Raman | 2024 | PMI-DT: Predictive Modeling & Inspection in Mfg. | arXiv preprint | ML2 | 2.5 |
| [12] | Zhang et al. | 2024 | Global BIM-point cloud registration for progress | Autom. Constr. | ML1 | 3.5 |
| [14] | Hu & Gan | 2025 | Semantic navigation for robotic inspection | Autom. Constr. | ML2 | 3.5 |
| [15] | Qiao et al. | 2025 | Global LiDAR registration via Pose Hough Transform | IEEE T-ASE | ML2 | 3.5 |
| [32] | Sacks et al. | 2020 | Construction with DT information systems | Data-Centric Eng. | — | 3.5 |
| [37] | Teizer et al. | 2010 | Autonomous proximity safety alert system | Autom. Constr. | ML1 | 4.0 |
| [38] | Teo, Ling & Chong | 2005 | Framework for PMs to manage construction safety | IJPM | — | 2.5 |
| [49] | Sacks, Rozenfeld & Rosenfeld | 2009 | Spatial-temporal exposure to safety hazards | JCEM | — | 3.5 |
| [53] | Schleich et al. | 2017 | Shaping the DT for design & production eng. | CIRP Annals | ML2 | 4.5 |
| [54] | Rasheed, San & Kvamsdal | 2020 | DT: Values, Challenges and Enablers | IEEE Access | — | 4.0 |
| [70] | Lee, Peña-Mora & Park | 2006 | Dynamic planning and control methodology | JCEM | — | 3.5 |

### 2.4 Design-for-Safety (DfS) Automation (n = 11)

| Ref | Authors | Year | Title | Journal | ML | QA |
|:---:|---|:---:|---|---|:---:|:---:|
| [16] | Zhang et al. | 2013 | BIM and Safety: Automatic Safety Checking | Autom. Constr. | ML2 | 4.5 |
| [21] | Martinez-Aires et al. | 2018 | BIM and safety management: systematic review | Safety Science | — | 3.5 |
| [22] | Zhou, Whyte & Sacks | 2012 | Construction safety and digital design: review | Autom. Constr. | — | 3.5 |
| [23] | Qi et al. | 2014 | BIM in Design to Prevent Worker Falls | J. Comp. Civ. Eng. | ML2 | 3.5 |
| [24] | Zhang et al. | 2015 | Workforce location tracking for BIM safety | Autom. Constr. | ML2 | 3.5 |
| [75] | Liu, Zhang & Wang | 2020 | Indoor safety management framework via DT | Sensors | ML2 | 3.0 |
| [76] | Liu et al. | 2021 | DT-based safety risk coupling in prefab hoisting | Sensors | ML2 | 3.5 |
| [81] | Jiang et al. | 2022 | DT-enabled smart modular integrated construction | Comp. in Industry | ML2 | 4.0 |
| [82] | Ruppert & Abonyi | 2020 | Integration of RTLS into digital twins | J. Ind. Info. Integr. | ML1 | 3.5 |
| [85] | Greif, Stein & Flath | 2020 | DTs for construction site logistics | Comp. in Industry | ML2 | 4.0 |
| [67] | Choi, Yun & Kim | 2021 | Integrated framework: BIM + sensor + ML for risk | Autom. Constr. | ML2 | 3.5 |

### 2.5 Predictive Analytics & Decision Support (n = 9)

| Ref | Authors | Year | Title | Journal | ML | QA |
|:---:|---|:---:|---|---|:---:|:---:|
| [9] | Lu, Xie et al. | 2020 | DT-enabled anomaly detection for built asset O&M | Autom. Constr. | ML1 | 4.5 |
| [13] | Lee et al. | 2025 | Agentic built environments: A review | Energy & Buildings | ML3 | 3.0 |
| [19] | Pan & Zhang | 2021 | BIM-data mining integrated DT framework | Autom. Constr. | ML2 | 4.0 |
| [77] | Zhao et al. | 2022 | Conceptual framework for DT in building O&M | J. Build. Eng. | ML2 | 3.5 |
| [78] | Zhang, Yang & Wang | 2023 | DT technologies in O&M stage: literature review | J. Build. Eng. | — | 4.0 |
| [79] | Shahzad et al. | 2022 | DTs in built environments: characteristics | Buildings | — | 3.5 |
| [80] | Chen et al. | 2021 | Gemini Principles-based DT maturity model | Sustainability | ML1–3 | 3.5 |
| [86] | Hakimi, Gunduz & Ehiagwina | 2024 | DT-enabled smart FM: bibliometric review | Front. Eng. Built Env. | — | 4.0 |
| [87] | Hosamo et al. | 2022 | DT predictive maintenance for AHU | Energy & Buildings | ML2 | 4.0 |

### 2.6 Lifecycle Continuity & Governance (n = 6)

| Ref | Authors | Year | Title | Journal | ML | QA |
|:---:|---|:---:|---|---|:---:|:---:|
| [18] | Broo, Bravo-Haro & Schooling | 2022 | Smart infrastructure digital twin design | Autom. Constr. | ML2 | 4.0 |
| [83] | Qi et al. | 2021 | Enabling technologies and tools for DT | J. Manuf. Syst. | — | 4.5 |
| [84] | Liu et al. | 2021 | Review of DT: concepts, technologies, applications | J. Manuf. Syst. | — | 4.0 |
| [88] | Lee et al. | 2021 | Integrated DT and blockchain for construction | Autom. Constr. | ML2 | 4.0 |
| [89] | Singh et al. | 2021 | Digital Twin: Origin to Future | Appl. Syst. Innov. | — | 3.5 |
| [91] | Tao et al. | 2019 | DTs and CPS toward Smart Mfg. & Industry 4.0 | Engineering | — | 4.5 |

---


## 3. 🔴 EXCLUDED at Full-Text Eligibility (n = 37)

These 37 studies were retrieved in full text and assessed against inclusion criteria IC1–IC3 and exclusion criteria EC1–EC4. Exclusion reasons follow the four categories reported in Section 2.3 of LR_cc.md.

---

### 3.1 Purely Conceptual — No Empirical Data or Prototype (EC1) (n = 18)

| # | Authors | Year | Title (abbreviated) | Journal / Venue | Reason for Exclusion |
|:---:|---|:---:|---|---|---|
| E1 | Hosamo, Nielsen & Svidt | 2022 | DT-based smart FM: bibliometric mapping of AEC-FM | Front. Eng. Built Env. | Bibliometric-only; no prototype, no methodological framework |
| E2 | Opoku, Perera & Osei-Kyei | 2022 | Drivers of DT adoption in construction | J. Build. Eng. | Survey of adoption drivers; managerial focus without technical depth |
| E3 | Lu, Parlikad & Schooling | 2019 | Cambridge campus DT: data-centric architecture | Proc. Intl. CIB Conf. | Conference paper; limited methodological detail |
| E4 | Zhang, Liu & Shi | 2021 | Model engineering for DT in manufacturing | Robotics CIM | Manufacturing-centric vision paper; no AECO empirical content |
| E5 | Lu et al. | 2020 | Developing a DT at building & city levels | J. Mgmt. in Eng. | Conceptual dual-level framework; overlaps with [57] |
| E6 | Rosen et al. | 2015 | About the importance of autonomy & DTs for future | IFAC-PapersOnLine | Vision paper on autonomy; no implementation or validation |
| E7 | Zhao, Feng & Chen | 2022 | DT-based O&M process optimization theory | J. Build. Eng. | Theoretical framework without empirical validation |
| E8 | Lee & Lee | 2021 | Supply-chain DT for off-site modular construction | Sustainability | Conceptual framework; no working prototype or evaluation |
| E9 | Teisserenc & Sepasgozar | 2021 | Blockchain governance for DT-based construction | Buildings | Conceptual blockchain-DT architecture; overlap with [88] |
| E10 | Zhao, Boje & Guerriero | 2023 | Blockchain 3.0 for AECO: paradigm framework | J. Ind. Info. Integr. | High-level blockchain vision; no construction-domain validation |
| E11 | Miller, Alvarez & Hartman | 2018 | Extended MBD framework for DT in manufacturing | J. Manuf. Syst. | Manufacturing CAD/MBD focus; no AECO content |
| E12 | Peng, Zhang & Jia | 2020 | DT-enabled hospital building management | Build. & Environ. | Hospital FM only; purely conceptual architecture with limited methodology |
| E13 | Yitmen, Alizadehsalehi & Akiner | 2021 | Cognitive DT for building lifecycle management | Sustainability | High-level framework without sufficient empirical grounding |
| E14 | Khajavi et al. | 2019 | DT for life cycle assessment in built environment | Sustainable Cities Soc. | Conceptual LCA-DT coupling without prototype |
| E15 | Madni, Madni & Lucero | 2019 | Leveraging DT technology in model-based SE | Systems | Vision paper for model-based systems engineering |
| E16 | Akanmu & Anumba | 2015 | Cyber-physical systems integration of BIM & sensing | Eng. Constr. Arch. Mgmt. | Early CPS-BIM vision without functioning implementation |
| E17 | Brilakis et al. | 2019 | Built environment DT keynote vision | ECPPM Conf. Proc. | Conference keynote/vision; no empirical methodology |
| E18 | Pan & Zhang | 2020 | Role of AI in BIM-based project management | Proc. ISARC | Conference short paper; conceptual only |

### 3.2 No Construction-Domain Relevance (EC — failed IC3) (n = 9)

| # | Authors | Year | Title (abbreviated) | Journal / Venue | Reason for Exclusion |
|:---:|---|:---:|---|---|---|
| E19 | Sun et al. | 2023 | DT in healthcare operations: systematic review | J. Biomed. Inform. | Healthcare domain; no AECO applicability |
| E20 | Shahat, Hyun & Yeom | 2021 | City digital twin potentials: systematic review | Sustainability | City-scale smart city DT; macro-level, no construction focus |
| E21 | Zborowski | 2018 | DT emerging in petroleum sector | J. Pet. Tech. | Oil & gas trade publication; no formal methodology |
| E22 | Iglesias et al. | 2017 | DT for JET divertor maintenance | Fusion Eng. Design | Nuclear fusion domain; no construction relevance |
| E23 | Tao et al. | 2018 | DT-driven product design, manufacturing & service | Int. J. Adv. Manuf. Tech. | Equipment PHM in manufacturing; not transferable to AECO |
| E24 | Söderberg et al. | 2017 | Toward a digital twin for real-time geometry assurance | CIRP Annals | Automotive/manufacturing geometry assurance |
| E25 | Boschert & Rosen | 2016 | DT — the simulation aspect | Mechatronic Futures | Manufacturing simulation textbook chapter |
| E26 | Negri, Fumagalli & Macchi | 2017 | Review of DT in manufacturing contexts | J. Manuf. Syst. | Pure manufacturing; no AECO content |
| E27 | Liu & Jiang | 2016 | DT-based manufacturing intelligence review | Chinese J. Mech. Eng. | Chinese manufacturing review; no construction domain |

### 3.3 Energy/HVAC Management Only (EC2) (n = 6)

| # | Authors | Year | Title (abbreviated) | Journal / Venue | Reason for Exclusion |
|:---:|---|:---:|---|---|---|
| E28 | Lydon et al. | 2019 | Coupled simulation of thermally active building systems | Energy & Buildings | TABS thermal coupling; no construction-phase relevance |
| E29 | Agostinelli & Heydari | 2022 | Predictive maintenance for FM via DT | Book Ch. — Springer | HVAC predictive maintenance only; book section format |
| E30 | Francisco et al. | 2020 | Smart BIM with IoT for building performance management | Build. & Environ. | HVAC energy optimization; no lifecycle continuity |
| E31 | Jia, Srinivasan & Raheem | 2017 | From BIM to DT for HVAC intelligence | Proc. Build. Simul. | HVAC-only building simulation |
| E32 | Haag & Anderl | 2018 | DT — proof of concept for building management | Eng. Sci. Tech. | Building energy monitoring dashboard; HVAC-centric |
| E33 | Barricelli, Casiraghi & Fogli | 2019 | DT survey: definitions & engineering methods | IEEE Access | Energy management perspective; insufficient construction depth |

### 3.4 Insufficient Methodological Description (n = 4)

| # | Authors | Year | Title (abbreviated) | Journal / Venue | Reason for Exclusion |
|:---:|---|:---:|---|---|---|
| E34 | YiShuo | 2020 | DT for off-site prefabricated construction | Thesis — NUS | Master's thesis; limited peer review, single-site, low QA |
| E35 | Rausch, Haas & Shahi | 2020 | Computational algorithms for DT registration | CSCE Conf. Proc. | Conference paper; insufficient algorithmic detail for replication |
| E36 | Hasan, Hasan & Jiang | 2022 | AR and DT for heavy machinery maintenance | J. Ind. Prod. Eng. | Single-machine lab study; low IF; no construction context |
| E37 | Tchana, Ducellier & Remy | 2019 | DT for linear infrastructure monitoring | Proc. PLM Conf. | Conference paper; rudimentary validation on synthetic data only |

---


## 4. ⚪ NOT RETRIEVED (n = 6)

Six full-text reports could not be obtained despite institutional access and direct author requests.

| # | Category | n | Notes |
|:---:|---|:---:|---|
| NR1–NR4 | Inaccessible conference archives | 4 | Older conference proceedings with no digital archive or DOI; institutional interlibrary loan attempts exhausted |
| NR5–NR6 | Non-responsive author contacts | 2 | Direct emails sent to corresponding authors; no response after two follow-up attempts over 8 weeks |

> Per PRISMA 2020 guidance, individual bibliographic details for non-retrieved reports are not recorded, as full-text content was never available for assessment. The n = 6 is subtracted from the 112 sought, yielding 106 assessed.

---


## 5. 🟡 EXCLUDED at Title & Abstract Screening (n = 203)

Per PRISMA 2020 standard practice (Item 16a), records excluded at title/abstract screening are reported **by count only**. Individual documentation is not required, as these records were not read in full text.

| Exclusion Category | Estimated n | Description |
|---|:---:|---|
| Out-of-domain | ~90 | Records addressing domains unrelated to AECO (manufacturing, healthcare, aerospace without transferability) |
| Purely conceptual / editorial | ~60 | Opinion pieces, editorials, trade magazine articles, workshop abstracts |
| No DT/BIM-integration relevance | ~35 | Records mentioning "digital twin" or "BIM" only peripherally (e.g., in future work sections) |
| Duplicates not caught by DOI | ~10 | Conference-then-journal pairs, preprint-then-published pairs identified manually |
| Non-English full text | ~8 | Title/abstract in English but full text in Chinese, Korean, or German |

> **Note:** These are estimated distributions based on screening notes. Two reviewers independently screened all 315 records (Cohen's κ = 0.81, indicating strong inter-rater agreement). Disagreements were resolved through discussion.

---


## 6. ⚫ DUPLICATES REMOVED (n = 97)

Of the 412 records identified from five databases, 97 were duplicates removed via:

| Method | Description |
|---|---|
| **Automated DOI matching** | Primary deduplication using DOI fields across exported BibTeX/RIS files |
| **Manual title matching** | Secondary check for records with missing DOIs — fuzzy title matching with author/year confirmation |
| **Preprint–published pairs** | arXiv/SSRN preprints matched to their subsequently published journal versions |
| **Late-caught duplicate** | Ref [90] (Lu et al. 2020) folded into [57] — same Zotero key `6VU4VXU4` (count correction, +1) |

> **Result:** 412 − 97 = **315 unique records** proceeded to title/abstract screening.

---


## 7. 🔵 SUPPLEMENTARY REFERENCES (Outside Systematic Search)

These references are cited in LR_cc.md for methodological context, standards, or post-SLR evidence but are **not part of the 69-study synthesis corpus**.

### 7.1 Methodology & Reporting Guidelines

| Ref | Authors | Year | Title | Purpose in LR_cc.md |
|:---:|---|:---:|---|---|
| [26] | Page et al. | 2021 | The PRISMA 2020 statement | PRISMA 2020 reporting framework |
| [27] | Kitchenham & Charters | 2007 | Guidelines for performing SLRs in software eng. | QA rubric adapted from this source |

### 7.2 Background / Classification / Taxonomy

| Ref | Authors | Year | Title | Purpose in LR_cc.md |
|:---:|---|:---:|---|---|
| [28] | Kritzinger et al. | 2018 | DT in manufacturing: categorical review | DT maturity classification reference |
| [29] | Fuller et al. | 2020 | DT: Enabling technologies, challenges, open research | General DT technology landscape |
| [30] | Tao et al. | 2019 | DT in industry: State-of-the-art | Five-dimensional DT framework reference |
| [31] | Uhlemann et al. | 2017 | The Digital Twin: Realizing the CPS for Industry 4.0 | CPS-DT relationship background |

### 7.3 Standards

| Ref | Source | Year | Title | Purpose in LR_cc.md |
|:---:|---|:---:|---|---|
| [61] | ISO 23247-1 | 2021 | DT framework for manufacturing — Overview | Convergence criterion formal basis |
| [62] | ISO 19650-1 | 2018 | BIM information management — Concepts & principles | BIM interoperability standards context |

### 7.4 Post-SLR Supplements (published after search cutoff or added during revision)

| Ref | Authors | Year | Title | Journal | Purpose |
|:---:|---|:---:|---|---|---|
| [92] | Martínez-Rojas et al. | 2025 | BIM for Safety: Real-Time Fall Prevention | Applied Sciences | Supplementary safety monitoring evidence |
| [93] | Liu et al. | 2023 | BIM + CV for construction workforce safety | Autom. Constr. | Computer vision safety monitoring |
| [94] | Chen et al. | 2025 | Large VLMs for context-aware construction safety | Autom. Constr. | Emerging AI for safety assessment |
| [95] | Omrany et al. | 2026 | DTs in construction: systematic review (2024–) | ITcon | Updated domain overview |
| [96] | Bolpagni et al. | 2025 | Challenges in Asset Management & DTs | Buildings | Asset management governance |
| [97] | Abdar et al. | 2021 | Review of UQ in deep learning | Info. Fusion | UQ methods for gap analysis |
| [98] | Grenyer et al. | 2021 | Systematic review of multivariate UQ for eng. | CIRP JMST | UQ methods for gap analysis |
| [99] | Lü et al. | 2025 | Review of UQ for frequency responses | Arch. Comp. Meth. Eng. | UQ methods context |
| [100] | Fung et al. | 2010 | Risk Assessment Model for construction safety | IJPM | Construction risk baseline |
| [TBD-A] | AlOmari et al. | 2026 | Cross-domain predictive analytics for construction | (submitted) | Cited as emerging evidence |
| [TBD-B] | Pragna et al. | 2026 | Forward forecasting in CPS environments | (submitted) | Cited as emerging evidence |

### 7.5 ❌ REMOVED References (n = 13)

These reference numbers were originally assigned but subsequently **removed** from the manuscript during quality audit. Reference numbers are retained as placeholders to avoid re-numbering.

| Ref | Original Authors | Year | Removal Reason |
|:---:|---|:---:|---|
| [35] | Ayyalasomayajula, Song & El-Diraby | 2022 | Could not verify DOI; insufficient bibliographic certainty |
| [41] | Olofsson, Lee & Eastman | 2010 | Tangential BIM-planning study; superseded by [32] |
| [42] | Borrmann, König, Koch & Beetz | 2018 | BIM textbook; not primary research |
| [45] | Li | 2021 | Generic UQ review; replaced by domain-specific [97],[98] |
| [46] | Spearpoint & Burch | 2012 | Too early; safety model without DT context |
| [47] | Saltelli et al. | 2008 | Textbook on sensitivity analysis; not primary research |
| [48] | Bedford & Cooke | 2001 | Probabilistic risk analysis textbook; not primary |
| [50] | Eastman, Teicholz, Sacks & Liston | 2018 | BIM Handbook textbook; not primary research |
| [59] | Liu et al. | 2022 | Unverifiable — overlaps with [84], insufficient distinction |
| [60] | Bolpagni, Ciribini & Fioravanti | 2022 | Replaced by verified [96] Bolpagni et al. 2025 |
| [63] | NIST | 2023 | CPS/DT trustworthiness report — pending Zotero verification |
| [68] | Singh & Akinci | 2021 | Duplicate content with other included CV-safety papers |
| [69] | Fang et al. | 2022 | Vision-based behavior analysis review — overlap with [67],[93] |

---

## 8. Master Reference Index -- All Atomic Notes (n = 526)

> Auto-generated from `01_source/*.md` frontmatter. All 526 notes indexed.
> **Identification:** `databases` = DOI in Lens.org export (n = 432); `other methods` = round-1 corpus, snowballing, supplementary (n = 94).

**Identification:** databases = 432, other methods = 94 (total 526)

**Zotero status:** {'unverifiable': 3, 'abstract-grounded': 273, 'verified': 181, 'title-only': 61, 'unsorted': 4, 'partial': 1, 'metadata_only': 3}

**Year distribution:** {'2002': 1, '2005': 1, '2006': 1, '2007': 1, '2009': 1, '2010': 3, '2012': 2, '2013': 2, '2014': 2, '2015': 2, '2016': 2, '2017': 4, '2018': 7, '2019': 13, '2020': 25, '2021': 47, '2022': 46, '2023': 60, '2024': 79, '2025': 135, '2026': 91, '2041': 1}

| # | Ref | Citekey | Authors | Year | Title | Zotero | Status | Ident | V1 (DT) | V2 (AECO) | V3 (Method) |
|:---:|:---:|---|---|:---:|---|---|:---:|:---:|---|---|---|
| 1 | [62] | 19650-12018 | ISO 19650-1 | 2018 | Organization and digitization of information about buildings and civil | -- | unverifiable | other methods |  |  |  |
| 2 | [] | A-E-Kirilov2022 | A.E. Kirilov; K.A. Chernyy; A.I. Tagirov; F.N | 2022 | On the Issue of the Structure of Digital Twins of Hazardous Production | U96DE4FT | abstract-grounded | databases | digital twin|digital twin | construction|structure | safety|risk assessment|ri |
| 3 | [] | A-V-Baulin2025 | A.V. Baulin; M.Kh. Kaufov | 2025 | Improving Organizational and Engineering Reliability during Dismantlin | GFR2M2ZR | abstract-grounded | databases | digital twins|bim|buildin | construction|building|bui | risk|lifecycle |
| 4 | [] | Aaron-Costin2023 | Aaron Costin; Alireza Adibfar; Jennifer Bridg | 2023 | Digital Twin Framework for Bridge Structural Health Monitoring Utilizi | CHSCQWWH | abstract-grounded | databases | digital twin|building inf | building|infrastructure|b | quality|predictive|monito |
| 5 | [97] | Abdar2021 | M. Abdar, F. Pourpanah, S. Hussain, D. Rezaza | 2021 | A review of uncertainty quantification in deep learning: Techniques, a | HWPU8ZWP | verified | other methods |  |  |  |
| 6 | [] | Abdul-Izz-Mohamad-Kamil2025 | Abdul Izz Mohamad Kamil; Mohamad Syazli Fathi | 2025 | Digital twin framework for addressing water management challenges in M | UGRYB7JK | abstract-grounded | databases | digital twin | infrastructure|bridge|urb | predictive|monitoring|mai |
| 7 | [] | Abdullah-Alariyan2025 | Abdullah Alariyan; Rawand A. Mohammed Amin; A | 2025 | Benefits of Artificial Intelligence for Achieving Durable and Sustaina | PBXAFYEU | abstract-grounded | databases | digital twins | construction|built enviro | predictive|machine learni |
| 8 | [] | Abdurahman-Yasin-Yigit2024 | Abdurahman Yasin Yiğit; Murat Uysal | 2024 | Automatic crack detection and structural inspection of cultural herita | V976A2EF | title-only | databases | digital twin | buildings|structural|heri | inspection |
| 9 | [] | Abubakar-Sadiq-Mohammed2025 | Abubakar Sadiq Mohammed; Mark Pim-Wusu; Chris | 2025 | Bibliometric analysis of innovative technology use in sustainable faci | Y598SFSV | abstract-grounded | databases | digital twin|building inf | building|infrastructure|f | artificial intelligence |
| 10 | [] | Adamantios-Bampoulas2026 | Adamantios Bampoulas; Kaiwalya Raj; Anandhi P | 2026 | Ontology-driven energy management in smart buildings: A comprehensive  | BJY6ZZEC | abstract-grounded | databases | digital twin|digital twin | building|buildings | semantic|ontology|predict |
| 11 | [] | Adhban-Farea2026 | Adhban Farea; Michal Otreba; Rahat Ullah; Ted | 2026 | Digital transformation of the AEC industry: a review of BIM implementa | XG2CZGCL | abstract-grounded | databases | digital twins|bim|buildin | construction|building|inf | quality|iot|lifecycle |
| 12 | [] | Adibi2024 | Sasan Adibi, Abbas Rajabifard, Davood Shojaei | 2024 | Sensor-driven digital twin platforms for smart environments: A systema | HHRE3QTR | verified | other methods |  |  |  |
| 13 | [] | Adrian-August-Wildenauer2020 | Adrian August Wildenauer | 2020 | CRITICAL ASSESSMENT OF THE EXISTING DEFINITIONS OF BIM DIMENSIONS ON T | UWMLGECH | verified | databases | bim|building information  | construction|building |  |
| 14 | [] | Afiqah-R-Radzi2023 | Afiqah R. Radzi; Nur Farhana Azmi; Syahrul Ni | 2023 | Relationship between digital twin and building information modeling: a | YJT5DJA6 | abstract-grounded | databases | digital twin|bim|building | construction|building|inf | maintenance |
| 15 | [] | Ahmad-Baghdadi2025 | Ahmad Baghdadi | 2025 | A comprehensive review of digital twin implementation in construction: | XM6DM3CA | verified | databases | digital twin|digital twin | construction|foundation | optimization |
| 16 | [] | Ahmad-Chihadeh2026 | Ahmad Chihadeh; Maria Böttcher; David Crampen | 2026 | Identification and evaluation of uncertainty sources of materials and  | 9FQ7L8LZ | verified | databases | digital twin | road | uncertainty |
| 17 | [] | Ahmed-Farouk-Kineber2023 | Ahmed Farouk Kineber; Atul Kumar Singh; Abdul | 2023 | Modelling the relationship between digital twins implementation barrie | DNCET4GQ | verified | databases | digital twin|digital twin | construction|building | lifecycle |
| 18 | [2] | Akhavian2025 | R. Akhavian, M. Amani, J. Mootz, R. Ashe, B.  | 2025 | Building Information Models to Robot-Ready Site Digital Twins (BIM2RDT | 7REV8TWX | verified | other methods |  |  |  |
| 19 | [51] | Akinci2002 | A. Akinci, M. Fischer, and J. Kunz | 2002 | Automated generation of work spaces required by construction activitie | SHAKQM77 | verified | other methods |  |  |  |
| 20 | [] | Akponanabofa-Henry-Oti2021 | Akponanabofa Henry Oti; Peter Farrell; Fonbey | 2021 | A BIM-driven framework for integrating rules and regulations in the de | FIS6DYWJ | verified | databases | bim|building information  | construction|building | safety|risk |
| 21 | [26] | al.2021 | M. J. Page et al. | 2021 | The PRISMA 2020 statement: an updated guideline for reporting systemat | L6IE92GF | verified | other methods |  |  |  |
| 22 | [13] | al.2025 | J. Lee et al. | 2025 | Agentic built environments: A review, | RQHBTQZ7 | verified | other methods |  |  |  |
| 23 | [15] | al.2025 | Z. Qiao et al. | 2025 | Speak the same language: Global LiDAR registration on BIM using pose H | AXBTD3BN | verified | other methods |  |  |  |
| 24 | [] | Alaa-O-Shehata2025 | Alaa O. Shehata; Ehsan Noroozinejad Farsangi; | 2025 | Enhanced digital twins (EDTs) approach based on advanced inspection an | 4FPWRGX2 | abstract-grounded | databases | digital twin|digital twin | construction|building|arc | life cycle|inspection |
| 25 | [] | Alejandro-Jimenez-Rios2024 | Alejandro Jiménez Rios; Margarita L. Petrou;  | 2024 | Industry 5.0, towards an enhanced built cultural heritage conservation | RA6C6T6M | abstract-grounded | databases | digital twins | construction|buildings|ar | artificial intelligence |
| 26 | [] | Alejandro-Jimenez-Rios2025 | Alejandro Jiménez Rios; Vagelis Plevris; Mari | 2025 | Towards Industry 5.0: a stakeholder analysis to understand the human r | MDVRL744 | verified | databases | digital twin | bridge|heritage |  |
| 27 | [] | Alessandra-Barresi2023 | Alessandra Barresi | 2023 | Urban Digital Twin and urban planning for sustainable cities | D3JR7FME | verified | databases | digital twin | urban | predictive |
| 28 | [] | Alessia-Bellini2025 | Alessia Bellini; Nora Johanne Klungseth; Carm | 2025 | Enabling circular economy in facility management through digital twins | A8KRK7VV | abstract-grounded | databases | digital twin|digital twin | building|facility managem |  |
| 29 | [] | Alex-Donkers2025 | Alex Donkers; Dujuan Yang; Bauke de Vries; Ni | 2025 | Personal indoor comfort models through knowledge discovery in cross-do | UV7SUJXF | verified | databases | digital twins | building|buildings|indoor | quality|semantic|sensor|k |
| 30 | [] | Alexander-Pavlov2024 | Alexander Pavlov; Dmitry Pavlov; Alexander Ku | 2024 | Study of technology for the reliability and survivability modelling of | KC7GNG8G | abstract-grounded | databases | digital twins | construction|structural|s | uncertainty |
| 31 | [] | Alhossein-Alharbi2026 | Alhossein Alharbi; Yunes Alqudsi; Alhasan Ali | 2026 | Unmanned Aerial Systems for Corrosion Detection: Multi‐Sensor Technolo | NPQ8AXNH | abstract-grounded | databases | digital twins | construction|infrastructu | safety|quality|deep learn |
| 32 | [] | Ali-Matin-Nazar2026 | Ali Matin Nazar; Xiaosheng Ji | 2026 | Triboelectric nanogenerators for intelligent and sustainable civil inf | 2464BFNF | abstract-grounded | databases | digital twin | infrastructure|bridge|tun | artificial intelligence|m |
| 33 | [] | Ali-Shehadeh2025 | Ali Shehadeh | 2025 | Optimizing construction supply chain efficiency: a blockchain and digi | 3EW7ZAD2 | abstract-grounded | databases | digital twins | construction|building|inf | simulation|real-time|bloc |
| 34 | [] | Alireza-Moghayedi2026 | Alireza Moghayedi; Bankole Awuzie | 2026 | Unlocking sustainability futures: a framework for digital product pass | HJ87TI4P | abstract-grounded | databases | digital twins|bim | construction|built enviro | predictive|monitoring|iot |
| 35 | [] | AlOmari2026 | Mohamad Al Omari, Mohammed Itair, Mojtaba Esl | 2026 | An integrated analytics method for structured accident analysis and sa | IENSAMVE | verified | other methods |  |  |  |
| 36 | [] | Alsaffar-Alhadi2025 | Alsaffar Alhadi; Beach Dr Tom; Rezgui Yacine | 2025 | Enhancing asset management: Integrating digital twins for continuous p | H6B8AZTV | abstract-grounded | databases | digital twin|digital twin | construction|building|bui | safety|quality|predictive |
| 37 | [] | Amaal-Ehab-Zhairy2025 | Amaal Ehab Zhairy; Ahmed Osama Daoud; Ahmed G | 2025 | Transforming facility management with BIM, IoT, and Digital Twin: a da | II6UC6LR | title-only | databases | digital twin|bim | facility management | quality|monitoring|iot |
| 38 | [] | Amir-Faraji2025 | Amir Faraji; Shima Homayoon Arya; Elnaz Ghase | 2025 | Exploring the metaverse: integrating emerging technologies for Industr | 77HTGURN | abstract-grounded | databases | digital twin|building inf | construction|civil engine | uncertainty|artificial in |
| 39 | [] | Amirreza-Rashidi2024 | Amirreza Rashidi; Hadi Sarvari; Daniel W.M. C | 2024 | A systematic taxonomic review of the application of BIM and digital tw | ZIUX9DUJ | abstract-grounded | databases | digital twins|bim|buildin | construction|built enviro | life cycle|energy |
| 40 | [] | Anant-Deogaonkar2026 | Anant Deogaonkar; Himanshu Shukla | 2026 | Enhancing construction management and procurement efficiency through a | FENEAHJJ | abstract-grounded | databases | digital twin|digital twin | construction|building|inf | predictive|causal|iot|lif |
| 41 | [] | Andrei-Hodorog2020 | Andrei Hodorog; Ioan Petri; Yacine Rezgui; Je | 2020 | Building information modelling knowledge harvesting for energy efficie | 9L7AQ4N2 | verified | databases | bim|building information  | construction|built enviro | semantic|energy |
| 42 | [] | Annalaura-Vuoto2023 | Annalaura Vuoto; Marco Francesco Funari; Paul | 2023 | Shaping Digital Twin Concept for Built Cultural Heritage Conservation: | WUMWISHG | abstract-grounded | databases | digital twin|building inf | aeco|construction|buildin |  |
| 43 | [] | Antonio-Salzano2025 | Antonio Salzano; Stefano Cascone; Enrico P. Z | 2025 | HVAC System Performance in Educational Facilities: A Case Study on the | FMBEDTTY | abstract-grounded | databases | digital twin|digital twin | construction|building | predictive|monitoring|iot |
| 44 | [] | Antreas-Kantaros2022 | Antreas Kantaros; Dimitrios Piromalis | 2022 | Setting up a Digital Twin Assisted Greenhouse Architecture | 2EPPUGV5 | verified | databases | digital twin|digital twin | architecture | quality|automation |
| 45 | [] | Anuja-Talla2022 | Anuja Talla; Stephen McIlwaine | 2022 | Industry 4.0 and the circular economy: using design-stage digital tech | 4VZU4ET4 | verified | databases | digital twins|building in | construction|building | artificial intelligence|b |
| 46 | [] | Aochun-Tang2025 | Aochun Tang; Xiaojun Shi; Guo Qin; Haotian Sh | 2025 | A digital twin-based system for timely simulation of bridge structural | CLRBFNNA | title-only | databases | digital twin | bridge|structural | simulation |
| 47 | [] | Apeesada-Sompolgrunk2026 | Apeesada Sompolgrunk; Hamed Golzad; Henry Liu | 2026 | The evolution of digital twins within the big BIM data landscape | X6AZ9677 | abstract-grounded | databases | digital twins|bim|buildin | building|foundation | lifecycle|real-time |
| 48 | [] | Arash-Hosseini-Gourabpasi2024 | Arash Hosseini Gourabpasi; Mazdak Nik-Bakht | 2024 | BIM-based automated fault detection and diagnostics of HVAC systems in | VBC25A7T | abstract-grounded | databases | digital twin|bim|building | building|buildings | sensor|fault |
| 49 | [] | Aravind-Poshnath2025 | Aravind Poshnath; Yiqun Chen; Behzad Rismanch | 2025 | Adaptive spatial planning for equitable renewable energy allocation in | GCZ4DEZS | abstract-grounded | databases | digital twin | building|buildings|urban | energy |
| 50 | [] | Arnulf-Hagen2024 | Arnulf Hagen; Trond Michael Andersen | 2024 | Asset management, condition monitoring and Digital Twins: damage detec | BSRPC4VR | verified | databases | digital twin|digital twin | infrastructure|asset mana | risk|machine learning|mon |
| 51 | [] | Ashtarout-Ammar2024 | Ashtarout Ammar; Francesca Maier; William S.  | 2024 | Practical Application of Digital Twins for Transportation Asset Data M | V24IVAFT | abstract-grounded | databases | digital twin|digital twin | asset management|architec | safety|predictive|lifecyc |
| 52 | [] | August-M-S-Thomsen2025 | August M.S. Thomsen; Jakob Bjørnskov; Muhyidd | 2025 | Ontology-based Digital Twins for informed decision-making: Scenario te | F62KAYCM | abstract-grounded | databases | digital twins | building|buildings|indoor | quality|ontology|predicti |
| 53 | [] | August-M-S-Thomsen2026 | August M.S. Thomsen; Jakob Bjørnskov; Muhyidd | 2026 | Ontology-driven digital twins for optimized recommissioning of hospita | PL984CZI | verified | databases | digital twin|digital twin | building|buildings | semantic|ontology|energy| |
| 54 | [] | Aya-Elshabshiri2025 | Aya Elshabshiri; Ameera Ghanim; Aseel Hussien | 2025 | Integration of Building Information Modeling and Digital Twins in the  | CDGQD4FP | title-only | databases | digital twins|building in | building | lifecycle|maintenance |
| 55 | [] | Ayodeji-Emmanuel-Oke2024 | Ayodeji Emmanuel Oke; Victor Adetunji Arowoiy | 2024 | Digital twin technology (DTT) in a developing construction industry: e | RHHWHFDI | title-only | databases | digital twin | construction |  |
| 56 | [] | Baiping-Dong2026 | Baiping Dong; Ahsan Shahbaz; Theodoros L. Kar | 2026 | Integration of cyber-physical systems and digital twins in structural  | QSFT36XV | title-only | databases | digital twins|cyber-physi | structural |  |
| 57 | [] | Basak-Keskin2022 | Basak Keskin; Baris Salman; Ozan Koseoglu | 2022 | Architecting a BIM-Based Digital Twin Platform for Airport Asset Manag | E936LLFJ | abstract-grounded | databases | digital twin|bim|building | building|infrastructure|a | life cycle |
| 58 | [] | Beatriz-Campos-Fialho2023 | Beatriz Campos Fialho; Ricardo Codinhoto; Már | 2023 | Statistical critical reactive maintenance characterisation for digital | 8UT3SSSX | verified | databases | digital twin|digital twin | building|buildings|facili | lifecycle|maintenance |
| 59 | [] | Behailu-Temesgen-Habe2025 | Behailu Temesgen Habe | 2025 | Explainable digital twins for circular construction: A systematic revi | RVRRKY4C | title-only | databases | digital twins | construction|urban | real-time |
| 60 | [] | Berkay-Akturk2024 | Berkay Aktürk; Pınar Irlayıcı Çakmak | 2024 | Digital twins for enhanced construction project management | UQIYWVJ2 | abstract-grounded | databases | digital twin|digital twin | construction|building | lifecycle |
| 61 | [] | Bilal-Manzoor2025 | Bilal Manzoor; Maxwell Fordjour Antwi-Afari;  | 2025 | Critical Success Factors for Implementing Digital Twin Technology in C | ITZHNZ4U | abstract-grounded | databases | digital twin | construction | predictive|lifecycle|main |
| 62 | [5] | Boje2020 | Calin Boje, Annie Guerriero, Sylvain Kubicki, | 2020 | Towards a semantic Construction Digital Twin: Directions for future re | 6RG2MC52 | verified | databases | digital twin|cyber-physic | construction|building|bui | semantic|monitoring|senso |
| 63 | [96] | Bolpagni2025 | M. Bolpagni et al. | 2025 | Challenges in Asset Management and Digital Twins: Industry Insights | KSJE5VBV | verified | other methods |  |  |  |
| 64 | [18] | Broo2022 | D. Gürdür Broo, M. Bravo-Haro, J. Schooling | 2022 | Design and implementation of a smart infrastructure digital twin | 6X33TIE6 | verified | other methods |  |  |  |
| 65 | [] | Buddhika-Priyankara-Arsecularatne2024 | Buddhika Priyankara Arsecularatne; Navodana R | 2024 | Review of reducing energy consumption and carbon emissions through dig | RIQFMLIK | abstract-grounded | databases | digital twin|digital twin | construction|built enviro | monitoring|lifecycle|carb |
| 66 | [] | Calin-Boje2020 | Calin Boje; Annie Guerriero; Sylvain Kubicki; | 2020 | Towards a semantic Construction Digital Twin: directions for future re | 6RG2MC52 | abstract-grounded | databases | digital twin|cyber-physic | construction|building|bui | semantic|monitoring|senso |
| 67 | [] | Calin-Boje2023 | Calin Boje; Álvaro José Hahn Menacho; Antonin | 2023 | A framework using BIM and digital twins in facilitating LCSA for build | 7B9E9VCP | abstract-grounded | databases | digital twin|digital twin | construction|building|bui | lifecycle|life cycle |
| 68 | [] | Canxin-Huang2026 | Canxin Huang; Liangpeng Wan; Guangyi Shi; Hui | 2026 | Research on an intelligent monitoring system for the entire tunnel con | SH738FEA | abstract-grounded | databases | digital twin|bim | construction|tunnel | safety|risk assessment|ri |
| 69 | [] | Carlos-Alejandro-Diaz-Schery2026 | Carlos Alejandro Diaz Schery; Rodrigo Goyanne | 2026 | An integrative framework for BIM, digital twin and generative AI conve | M26AE7XT | abstract-grounded | databases | digital twin|bim|building | construction|building | artificial intelligence|m |
| 70 | [] | Carolina-Silva-Araujo2025 | Carolina Silva Araújo; Emerson de Andrade Mar | 2025 | Proposal of a conceptual model of digital twins for construction sites | M5A7TNFC | verified | databases | digital twin|digital twin | construction|infrastructu | quality|monitoring |
| 71 | [] | Chang-Su-Shim2019 | Chang-Su Shim; Ngoc-Son Dang; Sokanya Lon; Ch | 2019 | Development of a bridge maintenance system for prestressed concrete br | ETKQP34Z | abstract-grounded | databases | digital twin | bridge|structural|concret | maintenance |
| 72 | [27] | Charters2007 | B. Kitchenham and S. Charters | 2007 | Guidelines for performing systematic literature reviews in software en | -- | unverifiable | other methods |  |  |  |
| 73 | [] | Chathuri-Widanage2024 | Chathuri Widanage; Ki Pyung Kim | 2024 | Integrating Design for Manufacture and Assembly (DfMA) with BIM for in | SGKH4GMQ | abstract-grounded | databases | bim|building information  | construction|building|inf | carbon|automation |
| 74 | [80] | Chen2021 | Z. Chen, A. K. Parlikad et al. | 2021 | Gemini Principles-Based Digital Twin Maturity Model for Asset Manageme | UG9GN8KS | verified | other methods |  |  |  |
| 75 | [] | Chenhao-Wang2025 | Chenhao Wang; Yang Ming; Hang Liu; Yutong Den | 2025 | Security-Enhanced Data Transmission With Fine-Grained and Flexible Rev | 4Y83XTAC | abstract-grounded | databases | digital twin | construction|concrete | real-time |
| 76 | [67] | Choi2021 | M. Choi, K. Yun, and Y. Kim | 2021 | An integrated framework for accident risk prediction using BIM, sensor | VSGTL8SJ | verified | other methods |  |  |  |
| 77 | [] | Chuanbao-Sun2022 | Chuanbao Sun; Xudong Zhou | 2022 | Use of Digital Twins‐Based Intelligent Navigation Visual Sensing Techn | QGMI7BCA | verified | databases | digital twins | structure | safety|sensor|real time |
| 78 | [] | Chung-Van-Pham2024 | Chung Van Pham; Cuong Xuan Cao; Canh Van Le;  | 2024 | BIM and TLS Point Cloud Integration for Information Management of Unde | 7JW2VVRL | abstract-grounded | databases | digital twin|bim|building | building|foundation | safety|point cloud|life c |
| 79 | [] | Danhui-Dan2022 | Danhui Dan; Yufeng Ying; Liangfu Ge | 2022 | Digital Twin System of Bridges Group Based on Machine Vision Fusion Mo | 9QSIEIBW | abstract-grounded | databases | digital twin | infrastructure|bridge|str | safety|monitoring |
| 80 | [] | Danhui-Dan2025 | Danhui Dan; Ruiyang Pan; Zhaowen Kong; Xingfe | 2025 | A digital twin model of traffic flow load for full bridge deck geared  | TIC6DTLD | title-only | databases | digital twin | bridge |  |
| 81 | [] | Daniel-Winarski2025 | Daniel Winarski; Marc Lamparelli; Keith Landr | 2025 | Creating a vibrational digital-twin of a Bell UH-1H helicopter tail-ro | TWI6SGCM | abstract-grounded | databases | digital twin|digital-twin | construction|structural|f | predictive|artificial int |
| 82 | [] | Dat-Huynh2020 | Dat Huynh; Sy Nguyen-Ky | 2020 | Engaging Building Automation Data Visualisation Using Building Informa | ZK65BMDF | abstract-grounded | databases | digital twin|bim|building | building|buildings|facili | semantic|monitoring|lifec |
| 83 | [] | David-Whitmore2024 | David Whitmore; Ilias Krystallis; Eleni Papad | 2024 | Digital twins in the asset life cycle: are we there yet? | JCY8I94H | abstract-grounded | databases | digital twins | civil engineering|infrast | life cycle|maintenance |
| 84 | [] | De-Graft-Joe-Opoku2021 | De-Graft Joe Opoku; Srinath Perera; Robert Os | 2021 | Digital twin application in the construction industry: A literature re | -- | unsorted | databases | digital twin | construction |  |
| 85 | [] | De-Graft-Joe-Opoku2024 | De-Graft Joe Opoku; Srinath Perera; Robert Os | 2024 | Digital twin for indoor condition monitoring in living labs: Universit | UAZ7JLZ9 | verified | databases | digital twin|building inf | construction|building|ind | quality|monitoring|real-t |
| 86 | [] | De-Zhang2025 | De Zhang; Yan Jiang; Jun Liu; Guokai Xiong; S | 2025 | Design, protection, perception and planning of mobile robots in nuclea | 69MDNLHA | abstract-grounded | databases | digital twin|bim|building | construction|building | artificial intelligence|o |
| 87 | [6] | Deng2021 | Min Deng, Carol C. Menassa, Vineet R. Kamat | 2021 | From BIM to digital twins: A systematic review of the evolution of int | 739GLUD3 | verified | other methods |  |  |  |
| 88 | [] | Dewa-Ayu-Nyoman-Ardi-Utami2026 | Dewa Ayu Nyoman Ardi Utami; Tri Joko Wahyu Ad | 2026 | Toward an AI-Enabled Digital Twin Decision-Support Architecture for Pr | VY46I8YR | title-only | databases | digital twin | architecture|road|urban | risk|predictive|decision- |
| 89 | [] | Diego-Espinosa-Gispert2023 | Diego Espinosa Gispert; Ibrahim Yitmen; Habib | 2023 | Development of an ontology-based asset information model for predictiv | AQGLTX69 | abstract-grounded | databases | digital twin | building|facility managem | ontology|predictive|energ |
| 90 | [] | Dimitrios-Loverdos2023 | Dimitrios Loverdos; Vasilis Sarhosis | 2023 | Geometrical digital twins of masonry structures for documentation and  | W3BSHBAV | abstract-grounded | databases | digital twin|digital twin | construction|structural|s | machine learning|inspecti |
| 91 | [] | Doney-Abraham2025 | Doney Abraham; Gizem Erceylan; Vasileios Gkio | 2025 | Towards enhanced cybersecurity in industrial control systems: a system | U5KV744C | verified | databases | digital twins|cyber-physi | infrastructure | predictive|machine learni |
| 92 | [] | Donghai-Liu2023 | Donghai Liu; Chenyang Sun; Junjie Chen; Lei L | 2023 | Multisensory and BIM-Integrated Digital Twin to Improve Urban Excavati | KI3R4K3K | abstract-grounded | databases | digital twin|bim|building | construction|building|roa | safety|risk|simulation|re |
| 93 | [] | Donglian-Gu2024 | Donglian Gu; Qingrui Yue; Li Li; Chujin Sun;  | 2024 | Vision-Based Digital Shadowing to Reveal Hidden Structural Dynamics of | 47IG8PJU | abstract-grounded | databases | digital shadow | building|buildings|struct | risk|monitoring|structura |
| 94 | [] | Dongsheng-Xu2026 | Dongsheng Xu; Jin Yang; Haiyan Zheng; Bin Che | 2026 | Digital twin system for deepwater well construction: Enhancing operati | M3UYXNNU | title-only | databases | digital twin | construction | safety |
| 95 | [] | Dragana-Nikolic2025 | Dragana Nikolić; Ian Ewart | 2025 | Going beyond net zero: digital twins for achieving socio-ecological su | ZFA45DL9 | abstract-grounded | databases | digital twins | built environment|buildin | energy |
| 96 | [] | E-V-Sumarokov2026 | E. V. Sumarokov; A. V. Obryadina; D. V. Kuzev | 2026 | Automation of geometric parameters control for reinforced concrete str | HQM9RIP6 | abstract-grounded | databases | digital twin|bim|building | building|concrete | quality|monitoring|point  |
| 97 | [52] | El-Gohary2016 | J. Zhang and N. M. El-Gohary | 2016 | Semantic NLP-based information extraction from construction regulatory | VDR5RZP3 | verified | other methods |  |  |  |
| 98 | [] | Eric-Ohene2024 | Eric Ohene; Gabriel Nani; Maxwell Fordjour An | 2024 | Big data analytics in the AEC industry: scientometric review and synth | MRZA2F8F | abstract-grounded | databases | digital twin|building inf | construction|building|fac | safety|risk assessment|ri |
| 99 | [] | Erica-Lenticchia2025 | Erica Lenticchia; Gaetano Miraglia; Jorge Ale | 2025 | Sensitivity driven model updating: a multi-step procedure for structur | 2RMMUZXD | abstract-grounded | databases | digital twin|digital twin | buildings|structural|stru | predictive|monitoring|mai |
| 100 | [] | Erwei-Tian2026 | Erwei Tian | 2026 | Quantum Encryption Techniques for Securing Low-Voltage Communication S | QTQJQ6IW | abstract-grounded | databases | digital twin | structure | risk|energy|maintenance |
| 101 | [] | Esa-Halmetoja2019 | Esa Halmetoja | 2019 | The conditions data model supporting building information models in fa | IZUV9VGD | abstract-grounded | databases | bim|building information  | construction|building|bui | quality|energy|maintenanc |
| 102 | [] | Esa-HALMETOJA2022 | Esa HALMETOJA; Natalija LEPKOVA | 2022 | Utilising Building Information Models in Facility Maintenance and Oper | DB542BX7 | abstract-grounded | databases | bim|building information  | construction|building|bui | maintenance |
| 103 | [] | Evelyn-F-Y-Liew2026 | Evelyn F.Y. Liew; Dominic E.L. Ong; Mohammud  | 2026 | Mapping the future of sustainable construction: Review on digitalisati | VXD65ZL5 | abstract-grounded | databases | digital twin|bim|building | construction|built enviro | lifecycle|life cycle|carb |
| 104 | [] | Eyal-Levenberg2024 | Eyal Levenberg; Lucija Barisic | 2024 | A Digital Twin Concept for Civil Infrastructure | 2BYBE3Z9 | abstract-grounded | databases | digital twin | civil engineering|infrast | monitoring |
| 105 | [] | F-Geremicca2026 | F. Geremicca; A. Fascetti; J.C. Brigham; M.M. | 2026 | Digital twins for sustainable buildings: From framework to strategy gu | 53WLEE5A | abstract-grounded | databases | digital twin|digital twin | built environment|buildin | semantic|decision support |
| 106 | [] | Fahim-Ullah2024 | Fahim Ullah; Oluwole Olatunji; Siddra Qayyum | 2024 | A scoping review of green Internet of Things in construction and smart | QP9UKB6Q | abstract-grounded | databases | digital twins|building in | construction|built enviro | safety|monitoring|iot |
| 107 | [] | Fangshi-Shi2026 | Fangshi Shi; Wei Yuan; Xinzhan Qin; Wei Wang; | 2026 | The Research on the Construction Method of a Slope Digital Twin Model  | UT44PP5T | verified | databases | digital twin | construction|slope | safety|monitoring|optimis |
| 108 | [] | Fareed-Salih2025 | Fareed Salih; Islam H. El-adaway | 2025 | Investigating the Correlation and Synergy of Artificial Intelligence T | 5GH8PW95 | abstract-grounded | databases | digital twin|bim|building | construction|building | safety|machine learning|a |
| 109 | [] | Fareed-Salih2025 | Fareed Salih; Islam H. El-adaway | 2025 | Exploring the Adoption of Construction Technologies in Infrastructure  | 9E4YXHC9 | abstract-grounded | databases | digital twin|bim|building | construction|building|bui | safety|iot|automation|rea |
| 110 | [] | Faris-Elghaish2024 | Faris Elghaish; Sandra Matarneh; M. Reza Hoss | 2024 | Predictive digital twin technologies for achieving net zero carbon emi | 7WADNETG | verified | databases | digital twin|digital twin | construction|built enviro | quality|predictive|artifi |
| 111 | [] | Faris-Elghaish2025 | Faris Elghaish; Saeed Reza Mohandes; Farzad R | 2025 | Predictive digital monitoring of construction resources: an integrated | 2GF8PV3B | abstract-grounded | databases | digital twin|digital twin | construction|building|sit | safety|ontology|predictiv |
| 112 | [] | Farzin-Naghibalsadati2024 | Farzin Naghibalsadati; Arash Gitifar; Sagar R | 2024 | Temporal evolution and thematic shifts in sustainable construction and | DPMXIEST | abstract-grounded | databases | digital twin|digital twin | construction|building |  |
| 113 | [] | Fathima-Nishara-Abdeen2025 | Fathima Nishara Abdeen; Samad M.E. Sepasgozar | 2025 | A user-driven design approach towards developing a citizen-centric dig | VYR74FWK | abstract-grounded | databases | digital twin|digital twin | infrastructure|urban | fault|real time |
| 114 | [] | Fatma-Handan-Sarigul2025 | Fatma Handan Sarigul; Husnu Murat Gunaydin | 2025 | Integrated BIM, GIS and interoperable digital technologies in lifecycl | 3ZCWGF7T | abstract-grounded | databases | digital twins|bim|buildin | construction|building|bui | safety|quality|semantic|l |
| 115 | [] | Federico-Gulisano2026 | Federico Gulisano; Juan Gallego; Freddy Richa | 2026 | Piezoresistive mechanism of asphalt mixtures with carbon fibers | L3C2SYZV | abstract-grounded | databases | digital twin | infrastructure|road|pavem | safety|monitoring|carbon| |
| 116 | [] | Felice-Carlo-Ponzo2024 | Felice Carlo Ponzo; Gianluca Auletta; Paolo I | 2024 | DInSAR–SBAS satellite monitoring of infrastructures: how temperature a | QNXEX9SE | verified | databases | digital twin | bridge|structural|structu | safety|monitoring|structu |
| 117 | [] | Feng-Han2026 | Feng Han; Yingjian An | 2026 | Construction Path of Shanghai Oriental Hub Municipal Pipeline Full Cyc | 7YQSUSI4 | verified | databases | digital twin|building inf | construction|building|pip | safety|artificial intelli |
| 118 | [] | Feng-Jiang2022 | Feng Jiang; Ling Ma; Tim Broyd; Weiya Chen; H | 2022 | Digital twin enabled sustainable urban road planning | 4E5M5F99 | title-only | databases | digital twin | road|urban |  |
| 119 | [] | Feng-Jiang2022 | Feng Jiang; Ling Ma; Tim Broyd; Ke Chen; Hanb | 2022 | Underpass clearance checking in highway widening projects using digita | 9ZREBFMU | abstract-grounded | databases | digital twin|digital twin | highway|road | safety |
| 120 | [] | Fengyi-Guo2026 | Fengyi Guo; Cynthia Changxin Wang; Jun Sun; K | 2026 | An intelligent construction system based on digital twin and foundatio | HNW78REE | verified | databases | digital twin|digital twin | construction|foundation|s | safety|risk|monitoring|se |
| 121 | [] | Fidel-Lozano-Galant2025 | Fidel Lozano-Galant; Angela Montalvo; Edison  | 2025 | An open-source GIS app for digitalising bridge inspections and automat | MLB6GHW7 | title-only | databases | bim | bridge |  |
| 122 | [] | Filip-Biljecki2023 | Filip Biljecki; Yoong Shin Chow; Kay Lee | 2023 | Quality of crowdsourced geospatial building information: A global asse | IVA4YRH8 | abstract-grounded | databases | digital twins | built environment|buildin | quality|life cycle|energy |
| 123 | [] | Frank-Ato-Ghansah2023 | Frank Ato Ghansah; Weisheng Lu | 2023 | Cyber-physical systems and digital twins for \ | GGDYKR33 | abstract-grounded | databases | digital twins|cyber-physi | aeco|construction|built e | lifecycle|maintenance |
| 124 | [] | Frank-Ato-Ghansah2023 | Frank Ato Ghansah; Weisheng Lu | 2023 | Major opportunities of digital twins for smart buildings: a scientomet | Q5BP48DI | abstract-grounded | databases | digital twin|digital twin | aeco|construction|buildin | real-time |
| 125 | [] | Frank-Ato-Ghansah2024 | Frank Ato Ghansah | 2024 | Digital twins for smart building at the facility management stage: a s | J8L73M3W | abstract-grounded | databases | digital twins | building|buildings|facili | uncertainty|monitoring|en |
| 126 | [] | Frank-Ato-Ghansah2026 | Frank Ato Ghansah; Liupengfei Wu; Caleb Debra | 2026 | An enabling framework towards digital twins implementation model for s | 5566JR2Y | abstract-grounded | databases | digital twins | built environment|buildin |  |
| 127 | [99] | Fu2026 | Yifan Fu, Yujie Zhao, Yan Zhu, Hongchao Zheng | 2026 | A review of uncertainty quantification in digital twins for engineerin | K3PFBG7P | partial | other methods |  |  |  |
| 128 | [29] | Fuller2020 | Aidan Fuller, Zhong Fan, Charles Day, Chris B | 2020 | Digital Twin: Enabling technologies, challenges and open research | SSR5IGBW | verified | other methods |  |  |  |
| 129 | [100] | Fung2010 | I. W. H. Fung, V. W. Y. Tam, T. Y. Lo, L. L.  | 2010 | Developing a Risk Assessment Model for construction safety | WG9ID8KK | verified | other methods |  |  |  |
| 130 | [] | G-P-Lydon2019 | G.P. Lydon; Stefan Caranovic; Illias Hischier | 2019 | Coupled simulation of thermally active building systems to support a d | CJQWKNPG | abstract-grounded | databases | digital twin | construction|building|bui | lifecycle|energy|simulati |
| 131 | [] | Gabor-Hasulyo2026 | Gábor Hasulyó | 2026 | Dynamic Digital Twin Network for Real-Time Safety Monitoring and Predi | 22Y4G8JK | title-only | databases | digital twin | infrastructure | safety|risk assessment|ri |
| 132 | [] | Gabriela-Bastos-Porsani2023 | Gabriela Bastos Porsani; Núria Casquero-Modre | 2023 | Empirical evaluation of EnergyPlus infiltration model for a case study | 88SYYGJZ | abstract-grounded | databases | digital twins | building|buildings|indoor | quality|uncertainty|energ |
| 133 | [] | Galina-Paskaleva2021 | Galina Paskaleva; Alexandra Mazak-Huemer; Man | 2021 | Leveraging integration facades for model-based tool interoperability | LWFJZR8Z | abstract-grounded | databases | bim | construction|building|fac | semantic |
| 134 | [14] | Gan2025 | D. Hu and V. J. L. Gan | 2025 | Semantic navigation for automated robotic inspection and indoor enviro | EVBNP6SE | verified | other methods |  |  |  |
| 135 | [] | Gang-Yu2020 | Gang Yu; Shuang Zhang; Min Hu; Y. Ken Wang | 2020 | Prediction of Highway Tunnel Pavement Performance Based on Digital Twi | WU2JWWKC | verified | databases | digital twin|bim|building | building|tunnel|highway|p | machine learning|neural n |
| 136 | [] | Geng-Tian2026 | Geng Tian; Shaoxiang Qin; Dingyang Geng; Dong | 2026 | AI-enhanced large-eddy simulation for urban wind flows: accelerating s | 43VJRDEL | abstract-grounded | databases | digital twins | building|urban | safety|deep learning|simu |
| 137 | [] | Geontae-Kim2024 | Geontae Kim; Youngjin Cha | 2024 | 3D Pixelwise damage mapping using a deep attention based modified Nerf | NKAPFLQ4 | abstract-grounded | databases | digital twin|digital twin | infrastructure|asset mana | quality|deep learning|mon |
| 138 | [] | Geza-Fischl2026 | Géza Fischl; Ibrahim Yitmen; Sajitha Hewa Dur | 2026 | Facilitating Level 3 framework for developing a Collaborative Digital  | 5IS47HXS | abstract-grounded | databases | digital twin|bim|building | building|bridge|architect | quality|artificial intell |
| 139 | [3] | Glatt2021 | Moritz Glatt, Chantal Sinnwell, Li Yi, Sean D | 2021 | Modeling and implementation of a digital twin of material flows based  | HK9GVDQT | verified | other methods |  |  |  |
| 140 | [] | Gozde-Basak-Ozturk2021 | Gozde Basak Ozturk | 2021 | Digital Twin Research in the AECO-FM Industry | -- | unsorted | databases | digital twin | aeco |  |
| 141 | [85] | Greif2020 | T. Greif, N. Stein, and C. M. Flath | 2020 | Peeking into the void: Digital twins for construction site logistics, | 3MAJ4UNU | verified | other methods |  |  |  |
| 142 | [98] | Grenyer2021 | A. Grenyer, J. A. Erkoyuncu, Y. Zhao, R. Roy | 2021 | A systematic review of multivariate uncertainty quantification for eng | NLAZ35NI | verified | other methods |  |  |  |
| 143 | [] | Guoliang-Shi2024 | Guoliang Shi; Zhansheng Liu; Dechun Lu; Zeqia | 2024 | Construction error control method of large-span spatial structures bas | CK6YP84B | title-only | databases | digital twin | construction |  |
| 144 | [] | Guoliang-Shi2024 | Guoliang Shi; Zhansheng Liu; Dechun Lu; Qingw | 2024 | Optimization method of cable structure demolition driven by digital tw | 68TTGWV7 | title-only | databases | digital twin | structure | optimization |
| 145 | [] | Götz2022 | Carl Sebastian Götz, Pelle Karlsson, Ibrahim  | 2022 | Exploring applicability, interoperability and integrability of Blockch | 56AMFECQ | verified | databases |  |  |  |
| 146 | [] | Habib-Sadri2025 | Habib Sadri | 2025 | AI-driven integration of digital twins and blockchain for smart buildi | WUC348UV | abstract-grounded | databases | digital twins | building|buildings|bridge | predictive|artificial int |
| 147 | [] | Haidar-Hosamo-Hosamo2022 | Haidar Hosamo Hosamo; Mohsen Hosamo Hosamo | 2022 | Digital Twin Technology for Bridge Maintenance using 3D Laser Scanning | NH7GTWBW | verified | databases | digital twin|digital twin | construction|civil engine | safety|risk|machine learn |
| 148 | [] | Haidar-Hosamo-Hosamo2022 | Haidar Hosamo Hosamo; Aksa Imran; Juan Carden | 2022 | A Review of the Digital Twin Technology in the AEC‐FM Industry | -- | unsorted | databases | digital twin|bim|building | construction|building|bui | semantic|predictive|senso |
| 149 | [] | Haidar-Hosamo-Hosamo2023 | Haidar Hosamo Hosamo; Henrik Kofoed Nielsen;  | 2023 | Digital Twin framework for automated fault source detection and predic | 2E4UQ7PZ | abstract-grounded | databases | digital twin|bim|building | building|buildings|facili | ontology|predictive|senso |
| 150 | [] | Haidar-Hosamo-Hosamo2023 | Haidar Hosamo Hosamo; Henrik Kofoed Nielsen;  | 2023 | Improving building occupant comfort through a digital twin approach: A | CFSUJAEW | abstract-grounded | databases | digital twin|bim|building | building|buildings | quality|ontology|predicti |
| 151 | [] | Haidar-Hosamo2022 | Haidar Hosamo; Mohsen Hosamo Hosamo; Henrik K | 2022 | Digital Twin of HVAC system (HVACDT) for multiobjective optimization o | JWEEALHL | verified | databases | digital twin|bim|building | building | neural network|sensor|ene |
| 152 | [] | Haishan-Xia2022 | Haishan Xia; Zishuo Liu; Maria Efremochkina;  | 2022 | Study on city digital twin technologies for sustainable smart city des | 422TPHLI | title-only | databases | digital twin|building inf | building|city|smart city |  |
| 153 | [86] | Hakimi2024 | O. Hakimi, H. Liu, O. Abudayyeh | 2024 | Digital twin-enabled smart facility management: A bibliometric review | 9EYC52IG | verified | other methods |  |  |  |
| 154 | [4] | Hamel2024 | C. Hamel, M. M. Ahsan, S. Raman | 2024 | PMI-DT: Leveraging Digital Twins and Machine Learning for Predictive M | 4B9RB46D | verified | other methods |  |  |  |
| 155 | [] | Hao-yang-Zhao2026 | Hao-yang Zhao; Chen Wang; Jian-sheng Fan | 2026 | Reverse Variational Autoencoder: A probabilistic inference framework f | 6PRWDF3D | abstract-grounded | databases | digital twin | bridge|structural|structu | deep learning|monitoring| |
| 156 | [] | Hao-Zhang2025 | Hao Zhang; Junwei Yan; Jun Yang; Wei Meng; Sh | 2025 | Two-stage point cloud registration using multi-scale edge convolution  | TA4L998Z | title-only | databases | digital twin | construction|bridge | monitoring|point cloud|re |
| 157 | [] | Haofeng-Yan2025 | Haofeng Yan; Changyong Liu; Xincong Yang; Kai | 2025 | Real-Time Digital Twin–Driven 3D Near-Miss Detection System at Constru | XSJ5VR8F | abstract-grounded | databases | digital twin | construction|site | safety|monitoring|simulat |
| 158 | [39] | Hartmann2017 | J. Whyte and A. Hartmann | 2017 | How digitizing building information transforms the built environment, | PITWT7WC | verified | databases |  |  |  |
| 159 | [43] | Harty2013 | A. C. Davies and N. Harty | 2013 | Implementing 'Site BIM': A case study of ICT innovation on a large hos | D4JSMC88 | verified | other methods |  |  |  |
| 160 | [] | Hayford-Pittri2026 | Hayford Pittri; Godawatte Arachchige Gimhan R | 2026 | Blockchain-enabled construction supply chain management: a scientometr | HNWHHZ39 | abstract-grounded | databases | digital twins|bim|buildin | construction|building | iot|real-time|blockchain |
| 161 | [] | Hector-Aroquipa2025 | Hector Aroquipa; Alvaro Hurtado; Christiam An | 2025 | Methodological framework for integrating structural health monitoring  | Y3KBLB9J | abstract-grounded | databases | digital twin|digital-twin | building|buildings|struct | monitoring|sensor|structu |
| 162 | [] | Heng-Sun2022 | Heng Sun; Zhe Liu | 2022 | Research on Intelligent Dispatching System Management Platform for Con | CMQBYYV4 | verified | databases | digital twin|digital twin | construction|built enviro | artificial intelligence|m |
| 163 | [] | Hessam-Kaveh2025 | Hessam Kaveh; Reda Alhajj | 2025 | Advancing civil infrastructure with digital twins: a review of applica | AM9KT67F | verified | databases | digital twins | civil engineering|buildin | safety|predictive|machine |
| 164 | [40] | Holmstrom2010 | J. V. Holmstrom, J. Partanen, J. Tuomi, and M | 2010 | Rapid manufacturing in the spare parts supply chain: Alternative appro | WBZTQ4RJ | verified | other methods |  |  |  |
| 165 | [] | Hong-Xu2022 | Hong Xu; Yihua Duo; Tao Tang | 2022 | A digital twin framework for construction and operation of the radioac | BKNFYCKF | abstract-grounded | databases | digital twin | construction|structure | safety |
| 166 | [] | Hongshuo-Sun2025 | Hongshuo Sun; Li Song; Chenxing Cui; Zhiwu Yu | 2025 | Bridge performance prediction based on nonlinear stochastic processes  | P6FVI8H3 | title-only | databases | digital twins | bridge |  |
| 167 | [] | Hongzhe-Yue2026 | Hongzhe Yue; Qian Wang; Minru Zhao; Zhouzhou  | 2026 | Advancements in Digital Twin Applications for Intelligent Construction | VJNKYRYT | abstract-grounded | databases | digital twin|digital twin | construction|foundation | quality|predictive|lifecy |
| 168 | [] | Hosamo2022 | Haidar Hosamo Hosamo, Hassan Hosamo, Mazen A. | 2022 | A review of the digital twin technology in the AEC-FM industry | 3QSAUVYC | verified | databases | digital twin|bim|building | construction|building|bui | semantic|predictive|senso |
| 169 | [87] | Hosamo2022b | H. Hosamo, P. R. Svennevig, K. Svidt, D. Han, | 2022 | A digital twin predictive maintenance framework of air handling units  | ID2GIXE3 | verified | other methods |  |  |  |
| 170 | [20] | Hossain2018 | M. A. Hossain, E. L. S. Abbott, D. K. H. Chua | 2018 | Design-for-Safety knowledge library for BIM-integrated safety risk rev | 7JMAKZYT | verified | other methods |  |  |  |
| 171 | [] | Hossein-Omrany2022 | Hossein Omrany; Amirhosein Ghaffarianhoseini; | 2022 | The uptake of City Information Modelling (CIM): a comprehensive review | 9BMDI3GG | abstract-grounded | databases | digital twin|bim | building|infrastructure|f | quality|energy |
| 172 | [] | Hossein-Omrany2024 | Hossein Omrany; Karam M. Al-Obaidi | 2024 | Application of digital twin technology for Urban Heat Island mitigatio | 6FKYAAVP | abstract-grounded | databases | digital twin | urban | optimisation |
| 173 | [] | Hristo-Vassilev2024 | Hristo Vassilev; Marius Laska; Jörg Blankenba | 2024 | Uncertainty-aware point cloud segmentation for infrastructure projects | IRMQ64IM | abstract-grounded | databases | digital twins | construction|infrastructu | quality|semantic|predicti |
| 174 | [] | Huamei-Zhu2025 | Huamei Zhu; Mengqi Huang; Pengxuan Ji; Feng X | 2025 | Transforming the maintenance of underground infrastructure through Dig | QBI42PUZ | abstract-grounded | databases | digital twin|digital twin | infrastructure|structural | predictive|machine learni |
| 175 | [] | Huimin-Li2024 | Huimin Li; Yafei Zhang; Yongchao Cao; Jing Zh | 2024 | Applications of artificial intelligence in the AEC industry: a review  | M9AU2ZLG | abstract-grounded | databases | digital twins | construction|architecture | safety|risk|artificial in |
| 176 | [] | Ibrahim-Bahreldin2025 | Ibrahim Bahreldin; Hossam Samir; Rahif Maddah | 2025 | Leveraging advanced digital technologies for smart city development in | HMV8FD38 | abstract-grounded | databases | digital twins | infrastructure|urban|city | carbon|energy |
| 177 | [] | Ioan-Petri2025 | Ioan Petri; Amin Amin; Ali Ghoroghi; Andrei H | 2025 | Digital twins for dynamic life cycle assessment in the built environme | NIZHE8EH | verified | databases | digital twin|digital twin | construction|built enviro | safety|semantic|predictiv |
| 178 | [] | Iryna-Osadcha2023 | Iryna Osadcha; Andrius Jurelionis; Paris Foka | 2023 | Geometric parameter updating in digital twin of built assets: A system | SNJYV7B2 | abstract-grounded | databases | digital twin | construction|building|bui | quality|monitoring|life-c |
| 179 | [] | Ismail-Erkek2026 | Ismail Erkek; Erdal Irmak | 2026 | Explainable digital twin–driven ensemble anomaly detection framework f | HHX4S7FQ | verified | databases | digital twin|cyber-physic | infrastructure | deep learning|monitoring| |
| 180 | [61] | ISO23247-2021 | ISO 23247-1 | 2021 | Automation systems and integration - Digital twin framework for manufa | -- | unverifiable | other methods |  |  |  |
| 181 | [] | J-Dong2023 | J Dong; Y Schwartz; A Mavrogianni; I Korolija | 2023 | A review of approaches and applications in building stock energy and i | F64L6WLU | abstract-grounded | databases | digital twin | building|indoor | quality|life cycle|energy |
| 182 | [] | Jack-C-P-Cheng2024 | Jack C.P. Cheng; Jiaying Zhang; Helen H.L. Kw | 2024 | Thermal performance improvement for residential heritage building pres | XY8PX3X4 | title-only | databases | digital twins | building|heritage |  |
| 183 | [] | Jack-Huang2025 | Jack Huang; André Broekman; George Markou; Hu | 2025 | Framework for a practical and cost-effective IoT-enhanced structural h | X5MXICDX | verified | databases | digital twin | infrastructure|asset mana | risk|monitoring|sensor|io |
| 184 | [] | Javier-Sanchez-Haro2025 | Javier Sánchez-Haro; Marianela García; Guille | 2025 | Digital twin for predictive maintenance on the Espartxo Bridge. Applic | 6VGUD2NX | abstract-grounded | databases | digital twin|digital mode | bridge|structural|geotech | risk|predictive|monitorin |
| 185 | [] | Jayantha-Kodikara2024 | Jayantha Kodikara; Arooran Sounthararajah; Li | 2024 | Reimagining unbound road pavement technology: Integrating testing, des | HCWYBZMX | abstract-grounded | databases | digital twin|bim|building | construction|building|inf | predictive|lifecycle|main |
| 186 | [] | Jean-Benezech2019 | Jean Benezech; Guillaume Couégnat | 2019 | Variational segmentation of textile composite preforms from X-ray comp | MNRQS97U | abstract-grounded | databases | digital twins | construction|structure | optimization |
| 187 | [] | Jennifer-Li2019 | Jennifer Li; David Greenwood; Mohamad Kassem | 2019 | Blockchain in the built environment and construction industry: A syste | 3YVJLUC7 | abstract-grounded | databases | bim | construction|built enviro | decision support|energy|b |
| 188 | [] | Jiaheng-Li2025 | Jiaheng Li; Feng Han; Long Shi; Zelong Liu; C | 2025 | Rapid integration strategy for oblique photogrammetry terrain and high | NJGLSGIT | abstract-grounded | databases | digital twin|bim|building | building|infrastructure|h | quality|monitoring|optimi |
| 189 | [] | Jiajun-Li2024 | Jiajun Li; Boan Tao; Frédéric Bosché; Chris X | 2024 | Automated generation and semantic segmentation of roof orthophoto for  | 63B59L9G | abstract-grounded | databases | digital twin | building|buildings|struct | safety|semantic|deep lear |
| 190 | [] | Jiamin-Huang2024 | Jiamin Huang; Ping Wu; Wangxin Li; Jun Zhang; | 2024 | Exploring the Applications of Digital Twin Technology in Enhancing Sus | FFYJXEXV | verified | databases | digital twin|digital twin | civil engineering | lifecycle |
| 191 | [] | Jiaming-Wu2021 | Jiaming Wu; Jian Chen; Guoliang Chen; Zhe Wu; | 2021 | Development of Data Integration and Sharing for Geotechnical Engineeri | KK37Y7K3 | verified | databases | bim|building information  | construction|building|inf |  |
| 192 | [] | Jian-Sheng-Fan2025 | Jian-Sheng Fan; Mu-Nan Xu; Yan-Chang Li; Yi-F | 2025 | Mechanics-based digital twin model for structural construction using 3 | DJAKYPW6 | title-only | databases | digital twin | construction|structural |  |
| 193 | [] | Jianfeng-Zhao2022 | Jianfeng Zhao; Haibo Feng; Qian Chen; Borja G | 2022 | Developing a conceptual framework for the application of digital twin  | -- | unsorted | databases | digital twin | building | maintenance |
| 194 | [7] | Jiang2021 | Feng Jiang, Ling Ma, Tim Broyd, Ke Chen | 2021 | Digital twin and its implementations in the civil engineering sector | LD8ZIQKW | verified | other methods |  |  |  |
| 195 | [25] | Jiang2022 | Y. Jiang, M. Li, M. Li, X. Liu, R. Y. Zhong,  | 2022 | Digital twin-enabled real-time synchronization for planning, schedulin | BEXVG4GB | verified | other methods |  |  |  |
| 196 | [81] | Jiang2022b | Y. Jiang, M. Li, D. Guo, W. Wu, R. Y. Zhong,  | 2022 | Digital twin-enabled smart modular integrated construction system for  | DXRTQ89R | verified | other methods |  |  |  |
| 197 | [] | Jianjie-Wu2025 | Jianjie Wu; Xingyu Luo; Hongliang Mei; Yuxian | 2025 | Efficient Tunnel Modeling in Unity3D with Data-Driven CSG Approach | CVHJ3XKD | abstract-grounded | databases | digital twin | tunnel|structural|structu | maintenance|optimization |
| 198 | [] | Jianjun-Miao2021 | Jianjun Miao; Shundong Lan | 2021 | Application of Visual Sensing Image Processing Technology under Digita | Y2KWIZW4 | verified | databases | digital twins | urban | sensor|simulation|real ti |
| 199 | [] | Jianyong-Shi2023 | Jianyong Shi; Zeyu Pan; Liu Jiang; Peizhi Che | 2023 | Research on a methodology for intelligent seismic performance evaluati | 327K59P5 | abstract-grounded | databases | digital twins|bim | construction|building|bui | quality|semantic|ontology |
| 200 | [] | Jiayi-Yan2025 | Jiayi Yan; Qiuchen Lu; Nan Li; Long Chen; Mic | 2025 | Common data environment for digital twins from building to city levels | 3XXCV2GZ | abstract-grounded | databases | digital twin|digital twin | building|infrastructure|c |  |
| 201 | [] | Jiaying-Zhang2024 | Jiaying Zhang; Helen H.L. Kwok; Jack C.P. Che | 2024 | Heritage building facades preservation: Automatic fresh air curtain wa | 5MVQ3YX6 | title-only | databases | digital twins | building|heritage |  |
| 202 | [] | Jifar-M-Hunde2025 | Jifar M. Hunde; Tesfatsyon S. Ochono; Damitha | 2025 | Data-driven and physics-based modeling approaches and their integratio | YCYV29G5 | abstract-grounded | databases | digital twin|digital twin | construction|building|arc | real-time |
| 203 | [] | Jingqi-Zhang2024 | Jingqi Zhang; Shaohua Jiang | 2024 | Digital twin for sustainable development in building automation | FBUPLRG3 | abstract-grounded | databases | digital twin | construction|building | quality|predictive|energy |
| 204 | [] | Jinsong-Zhu2025 | Jinsong Zhu; Ziyi Wang; Yuanhao Zhang; Yanlei | 2025 | A knowledge foundation and prospect review on thermal response of brid | EDBV5ZDE | abstract-grounded | databases | digital twin|digital twin | construction|infrastructu | safety|monitoring|mainten |
| 205 | [] | Jinyue-Zhang2020 | Jinyue Zhang; Lijun Zi; Yuexian Hou; Mingen W | 2020 | A Deep Learning-Based Approach to Enable Action Recognition for Constr | LMWSUM7Y | abstract-grounded | databases | digital twin | construction | deep learning|neural netw |
| 206 | [] | Jinzhi-Wang2026 | Jinzhi Wang | 2026 | Research on the construction method of intelligent operation and maint | DGQ22SIW | verified | databases | digital twin|digital twin | construction|infrastructu | predictive|deep learning| |
| 207 | [] | Jisong-Zhang2020 | Jisong Zhang; Lihua Zhao; Guoqian Ren; Haijia | 2020 | Special issue \ | E23T3S8L | verified | databases | digital twin|bim | building|infrastructure|s |  |
| 208 | [] | Jiu-Lin-Li2021 | Jiu-Lin Li; Li-Min Chen; Hao Xu | 2021 | Intelligent Construction, Operation, and Maintenance of a Large Wastew | X2VGIYHC | abstract-grounded | databases | bim|building information  | construction|building|fou | deep learning|monitoring| |
| 209 | [] | Joaquim-Cebolla-Alemany2024 | Joaquim Cebolla-Alemany; Marcel Macarulla Mar | 2024 | Optimizing indoor air models through k-means clustering of nanoparticl | YN4LEZAM | abstract-grounded | databases | digital twins | building|indoor | quality|predictive|optimi |
| 210 | [71] | Jones2020 | David Jones, Chris Snider, Aydin Nassehi, Jas | 2020 | Characterising the Digital Twin: A systematic literature review | 9FNSJ6UJ | verified | other methods |  |  |  |
| 211 | [] | Joshua-David-Lee2026 | Joshua David Lee | 2026 | Prologue: Beyond single use: looking back and looking forward at the o | 2DK3YFYK | abstract-grounded | databases | digital twin | construction|built enviro | artificial intelligence |
| 212 | [] | Ju-Hyun-Lee2023 | Ju Hyun Lee; Michael J. Ostwald; Samaneh Aras | 2023 | BIM-Enabled Design Collaboration Processes in Remote Architectural Pra | PL2CGXV9 | abstract-grounded | databases | bim|building information  | building|architectural |  |
| 213 | [] | Juan-Carlos-Sanchez-Quesada2024 | Juan Carlos Sánchez-Quesada; Emma Moliner; An | 2024 | Train-track-bridge interaction effects on highly skewed girder bridges | BFX7K33W | abstract-grounded | databases | digital twins | bridge|railway | safety |
| 214 | [] | Juan-Moyano2022 | Juan Moyano; Ignacio Gil-Arizón; Juan E. Niet | 2022 | Analysis and management of structural deformations through parametric  | KM2YKYXN | abstract-grounded | databases | digital twins|bim | construction|building|bui | quality|point cloud |
| 215 | [] | Juan-Tan2026 | Juan Tan; Mehdi Koohmishi; Guoqing Jing; Sakd | 2026 | Circular economy applications in railway infrastructure: A comprehensi | EVMGXTKY | abstract-grounded | databases | digital twin|bim|building | construction|building|inf | iot|lifecycle|maintenance |
| 216 | [] | Junwei-Yan2025 | Junwei Yan; Hao Zhang; Qingsong Ai; Yongyang  | 2025 | Digital twin-based bridge geometric quality inspection using knowledge | ZMUZFZBG | title-only | databases | digital twin | bridge | quality|inspection |
| 217 | [] | Junxiang-Zhu2025 | Junxiang Zhu; Mun On Wong; Nicholas Nisbet; J | 2025 | Semantics-based connectivity graph for indoor pathfinding powered by I | E9UPI6EW | abstract-grounded | databases | digital twin | building|buildings|facili | semantic |
| 218 | [] | Junxiang-Zhu2025 | Junxiang Zhu; Nicholas Nisbet; Mengtian Yin;  | 2025 | Releasing the power of graph for building information discovery | 8IQWAXNK | abstract-grounded | databases | digital twin | building|structure|founda |  |
| 219 | [] | Jurad-Sukhnandan2025 | Jurad Sukhnandan; Georgios A. Drosopoulos | 2025 | A machine learning approach used to predict the peak displacement, bas | GXALRAT6 | abstract-grounded | databases | digital twins | structural|structure | machine learning|real-tim |
| 220 | [] | Jussi-Myllarniemi2024 | Jussi Myllärniemi; Pasi Hellsten; Viivi Siuko | 2024 | Lifecycle information management for asset owner | YECLF5CG | abstract-grounded | databases | digital twin|bim|building | construction|building|inf | lifecycle |
| 221 | [] | Kabir-Ibrahim2024 | Kabir Ibrahim; Taofeek Tunde Okanlawon; Luqma | 2024 | Construction 4.0: enhancing sustainable construction practices by eval | 5SR4Y4DJ | abstract-grounded | databases | digital twin|digital twin | construction|built enviro | quality |
| 222 | [64] | Kahneman2021 | D. Kahneman, O. Sibony, C. R. Sunstein | 2021 | Noise: A Flaw in Human Judgment | -- | metadata_only | other methods |  |  |  |
| 223 | [] | Kai-Wen-Zhang2026 | Kai-Wen Zhang; You-Lin Xu; You Dong; Zhong-Ch | 2026 | Digital twin-driven multi-metrics condition assessment of eccentricall | AY9UE4PY | title-only | databases | digital twin | concrete |  |
| 224 | [] | Kai-Zhang2025 | Kai Zhang; Yakun Wang; Bo Dai | 2025 | Research on structural health assessment methods for long‐distance und | SLNN8EAQ | abstract-grounded | databases | digital twin | structural|structure|foun | maintenance|inspection |
| 225 | [] | Kaichao-Wang2025 | Kaichao Wang; Chunxia Zhang; Yachao Qian; Wul | 2025 | Digital twin safety analysis of large-span spatial structure based on  | CNTT6QFM | title-only | databases | digital twin | structure | safety |
| 226 | [] | Kaiqi-Lin2021 | Kaiqi Lin; You Lin Xu; Xinzheng Lu; Zhongguo  | 2021 | Digital twin-based collapse fragility assessment of a long-span cable- | QQLDL97Y | title-only | databases | digital twin | bridge |  |
| 227 | [] | Kaiqi-Lin2022 | Kaiqi Lin; You-Lin Xu; Xinzheng Lu; Zhongguo  | 2022 | Digital twin-based life-cycle seismic performance assessment of a long | ESFWAA7G | title-only | databases | digital twin | bridge | life-cycle |
| 228 | [] | Kaixin-Hu2023 | Kaixin Hu; Daguang Han; Guocheng Qin; Yin Zho | 2023 | Semi-automated Generation of Geometric Digital Twin for Bridge Based o | 8PLQA95G | verified | databases | digital twin|digital twin | bridge|site | quality|point cloud|maint |
| 229 | [] | Kari-Alanne2022 | Kari Alanne; Seppo Sierla | 2022 | An overview of machine learning applications for smart buildings | W93ZJWHS | abstract-grounded | databases | digital twins | building|buildings|buildi | machine learning|artifici |
| 230 | [] | Karim-Farghaly2024 | Karim Farghaly; Ranjith Soman; Jennifer Whyte | 2024 | cSite ontology for production control of construction sites | XB6SPBW2 | abstract-grounded | databases | digital twins | construction | ontology |
| 231 | [] | Karoline-Figueiredo2024 | Karoline Figueiredo; Ahmed W.A. Hammad; Rodri | 2024 | Integrating Digital Twin and Blockchain for dynamic building Life Cycl | LZEJ4ZSB | title-only | databases | digital twin | building | life cycle|blockchain |
| 232 | [] | Katherine-Wilsdon2023 | Katherine Wilsdon; Joshua Hansel; M. Ross Kun | 2023 | Autonomous control of heat pipes through digital twins: Application to | PFLGCDJ9 | abstract-grounded | databases | digital twin|digital twin | construction | risk|predictive|monitorin |
| 233 | [] | Kathrin-Braun2022 | Kathrin Braun; Cordula Kropp; Yana Boeva | 2022 | Constructing platform capitalism: inspecting the political techno-econ | ENSGE43J | verified | databases | bim|building information  | construction|building|bui |  |
| 234 | [] | Kavita-Sohal2023 | Kavita Sohal; Suresh Renukappa; Subashini Sur | 2023 | The uptake of digital twins in delivering infrastructure sector projec | J5KBTUPL | abstract-grounded | databases | digital twins | infrastructure | artificial intelligence|m |
| 235 | [] | Ke-MA2025 | Ke MA; Yusheng TANG; Zhiliang GAO; Hu KE | 2025 | Digital twin model of high-arch dams driven by microseismic damage and | RB4PP7ST | verified | databases | digital twin | construction|dam | safety|monitoring|energy| |
| 236 | [] | Kexin-Liu2025 | Kexin Liu; Vicente A. González; Gaang Lee; Ma | 2025 | A scoping review of fire safety on building construction sites: curren | DVI8PCN5 | abstract-grounded | databases | digital twins | construction|building | safety|risk assessment|ri |
| 237 | [] | Khaled-Galal-Ahmed2025 | Khaled Galal Ahmed; Neveen Hamza; Alaa Omar K | 2025 | Retrofit with residents: proposed locally responsive participatory met | PK59YMI8 | abstract-grounded | databases | digital twin|bim|building | building|housing | energy|simulation |
| 238 | [] | Khaled-Galal-Ahmed2025 | Khaled Galal Ahmed; Baraah Hamdoon; Amera Bal | 2025 | Trihybrid Method for Energy Efficiency Retrofitting of Public Housing  | HNA9LQZ7 | abstract-grounded | databases | digital twins|bim|buildin | building|infrastructure|h | energy|simulation |
| 239 | [] | Kiana-Movahedian-Attar2024 | Kiana Movahedian Attar; Hamidreza Abbasianjah | 2024 | Digital Twins for Improving the Construction Safety: Literature Conten | RCZV5RIX | title-only | databases | digital twins | construction | safety |
| 240 | [] | Kilian-Speiser2024 | Kilian Speiser; Jochen Teizer | 2024 | Automatic creation of personalised virtual construction safety trainin | ZJXKZ4M5 | abstract-grounded | databases | digital twin|digital twin | construction|building | safety|hazard |
| 241 | [94] | Kim2025 | T. Kim, S. Kim, W.-C. Chern, S. Park, D. Kim, | 2025 | Optimizing large vision-language models for context-aware construction | R3P4YWR6 | verified | other methods |  |  |  |
| 242 | [] | Kok-Kwang-Phoon2022 | Kok-Kwang Phoon; Wengang Zhang | 2022 | Future of machine learning in geotechnics | LGFQ3PR8 | abstract-grounded | databases | digital twin | geotechnical|site | machine learning |
| 243 | [] | Konstantinos-Adamos2023 | Konstantinos Adamos; George Stergiopoulos; Mi | 2023 | Enhancing attack resilience of cyber-physical systems through state de | 9AY2A3AL | verified | databases | digital twins|cyber-physi | infrastructure|architectu | risk assessment|risk|deci |
| 244 | [] | Konstantinos-Gkoumas2024 | Konstantinos Gkoumas; Marcin Stepniak; Ilias  | 2024 | New technologies for bridge inspection and monitoring: a perspective f | BGBRAGQ6 | verified | databases | digital twins | infrastructure|bridge | safety|artificial intelli |
| 245 | [] | Konstantinos-Trevlopoulos2026 | Konstantinos Trevlopoulos; Pierre Gehl; Cater | 2026 | Interpretable damage state-dependent fragility models for multi-hazard | 9HAFKTNB | abstract-grounded | databases | digital twin | building|structural|concr | safety|risk|predictive|de |
| 246 | [28] | Kritzinger2018 | Werner Kritzinger, Matthias Karner, Georg Tra | 2018 | Digital Twin in manufacturing: A categorical literature review and cla | J4XB34RN | verified | other methods |  |  |  |
| 247 | [93] | Kulinan2024 | A. S. Kulinan, M. Park, P. P. W. Aung, G. Cha | 2024 | Advancing construction site workforce safety monitoring through BIM an | P52VFZEH | verified | other methods |  |  |  |
| 248 | [] | Kushani-Semasinghe2026 | Kushani Semasinghe; Srinath Perera; Samudaya  | 2026 | Artificial intelligence–based strategies for indoor environmental qual | LBBSXG2A | abstract-grounded | databases | digital twin|digital twin | building|buildings|indoor | quality|machine learning| |
| 249 | [70] | Lee2006 | S. H. Lee, F. Peña-Mora, M. Park | 2006 | Dynamic planning and control methodology for strategic and operational | -- | metadata_only | other methods |  |  |  |
| 250 | [88] | Lee2021 | D. Lee, S. H. Lee, N. Masoud, M. S. Krishnan, | 2021 | Integrated digital twin and blockchain framework to support accountabl | JQBEN9IR | verified | other methods |  |  |  |
| 251 | [] | Li-Gao2025 | Li Gao; Shan Chen | 2025 | Digital twin-based vibration displacement sensing and recognition tech | 8SQRYRC7 | verified | databases | digital twin | construction|building|str | safety|quality|neural net |
| 252 | [] | Li-Xu2025 | Li Xu; Yang Zou; Yuqian Lu; Alice Chang-Richa | 2025 | Automation in manufacturing and assembly of industrialised constructio | EGGW68RX | abstract-grounded | databases | digital twins | construction | safety|quality|deep learn |
| 253 | [] | Liala-Baiardi2019 | Liala Baiardi; Ingrid Paoletti; Valentina Pug | 2019 | Digital control room for the project and management of complex buildin | 2JKKLKQ7 | abstract-grounded | databases | bim | construction|building|bui | life cycle |
| 254 | [] | Liang-Gao2023 | Liang Gao; Limin Zhang; Yang Hong; Hong-Xin C | 2023 | Flood hazards in urban environment | ERFW4EGK | abstract-grounded | databases | digital twin | urban | uncertainty|optimisation| |
| 255 | [] | Lichini-Nikesha-Kumari-Weerasinghe2025 | Lichini Nikesha Kumari Weerasinghe; Amos Dark | 2025 | Digital twin for sustainable decision-making in building net zero carb | ZST8NH8L | abstract-grounded | databases | digital twin | construction|building | carbon|energy|simulation |
| 256 | [] | Lin-Lin2025 | Lin Lin; Panpan Shen; Chunhao Jiang; Yifeng L | 2025 | G-Twin – Graph neural network-based digital twin for real-time and hig | WGJZRM39 | title-only | databases | digital twin | structural | neural network|monitoring |
| 257 | [] | Lingling-Ren2026 | Lingling Ren | 2026 | Digital Twin System Construction and Simulation Optimization for Colla | ACC7CXX4 | verified | databases | digital twin | construction|foundation | artificial intelligence|o |
| 258 | [] | Linhong-Wang2026 | Linhong Wang; Jun Zhang; Hongyang Liang; Peng | 2026 | Digital twin-enabled real-time heavy equipment scheduling with rolling | V9RBRBZ4 | abstract-grounded | databases | digital twin | construction|earthwork | quality|optimization|real |
| 259 | [] | Linjun-Lu2026 | Linjun Lu; Yuandong Pan; Brian Sheil; Peihang | 2026 | Regional graph-based pavement condition data quality assessment in sup | ZD8U8DJ3 | abstract-grounded | databases | digital twins | infrastructure|highway|ro | quality|maintenance |
| 260 | [] | Linna-Geng2026 | Linna Geng; Shengping Li; Ehsan Noroozinejad  | 2026 | How do digital technologies reduce carbon emissions in the constructio | TNFEZLL2 | abstract-grounded | databases | digital twins|bim|buildin | construction|building|arc | iot|life cycle|carbon|ene |
| 261 | [] | Linxuan-Wang2024 | Linxuan Wang; Nanjiang Chen | 2024 | Towards digital-twin-enabled facility management: the natural language | SNT6NQNK | abstract-grounded | databases | digital twin|digital-twin | construction|building|bui | knowledge graph |
| 262 | [] | Lior-Skoury2026 | Lior Skoury; Ofer Asaf; Aaron Sprecher; Achim | 2026 | Data-informed Digital Twin for large-scale 3D printing in construction | RV9PQEMC | abstract-grounded | databases | digital twin|digital twin | construction|architecture | quality|predictive|monito |
| 263 | [75] | Liu2020 | Zhansheng Liu, Anshan Zhang, Jianxiang Wang | 2020 | A framework for an indoor safety management system based on digital tw | VI3RUWW4 | verified | other methods |  |  |  |
| 264 | [76] | Liu2021 | Z. Liu, X. Meng, Z. Xing, C. Jiang | 2021 | Digital twin-based safety risk coupling of prefabricated building hois | CDL7QW8N | verified | other methods |  |  |  |
| 265 | [84] | Liu2021 | M. Liu, S. Fang, H. Dong, C. Xu | 2021 | Review of digital twin about concepts, technologies, and industrial ap | 2P9ECH2E | verified | other methods |  |  |  |
| 266 | [] | Longxuan-Wang2023 | Longxuan Wang; Hongbo Liu; Zhihua Chen; Fan Z | 2023 | Combined digital twin and hierarchical deep learning approach for inte | LJ732ERR | title-only | databases | digital twin | structure | deep learning |
| 267 | [] | Lotta-Kannari2025 | Lotta Kannari; Nina Wessberg; Sara Hirvonen;  | 2025 | Reinforcement learning for control and optimization of real buildings: | DJ7JAPL6 | abstract-grounded | databases | digital twin | building|buildings | safety|machine learning|a |
| 268 | [65] | Love2014 | P. Love, J. Matthews, G. Simpson, A. Hill, an | 2014 | A benefits realization management building information modeling framew | C26978RE | verified | other methods |  |  |  |
| 269 | [] | Lu&Parlikad2020 | Qiuchen Lu, Ajith Kumar Parlikad, Philip Wood | 2020 | Developing a Digital Twin at building and city levels: Case study of W | 7ANHKRIU | verified | other methods |  |  |  |
| 270 | [9] | Lu&Xie2020 | Qiuchen Lu, Xiang Xie, Ajith Kumar Parlikad,  | 2020 | Digital Twin-enabled anomaly detection for built asset monitoring in o | PTY562CM | verified | other methods |  |  |  |
| 271 | [] | Lu-Lian2022 | Lu Lian; Yao Yan | 2022 | Digital Visual Sensing Design Teaching Using Digital Twins | 62J2VNRT | verified | databases | digital twin|digital twin | foundation | monitoring|sensor |
| 272 | [57] | Lu2020 | Y. Lu, C. Liu, K. I.-K. Wang, H. Huang, and X | 2020 | Digital Twin-driven smart manufacturing: Connotation, reference model, | 6VU4VXU4 | verified | other methods |  |  |  |
| 273 | [] | Luca-Pinciroli2026 | Luca Pinciroli; Seyed Ali Hosseini; Mei Chen; | 2026 | Risk assessment for modern industry | 7V85CDY6 | abstract-grounded | databases | digital twins|cyber-physi | bridge | safety|risk assessment|ri |
| 274 | [] | Luca-Rampini2023 | Luca Rampini; Fulvio Re Cecconi | 2023 | Synthetic images generation for semantic understanding in facility man | F6ETXLA4 | abstract-grounded | databases | digital twins|bim | facility management|pipel | semantic |
| 275 | [] | Lucas-Bellini-Machado2025 | Lucas Bellini Machado; Ruan Richelly Santos;  | 2025 | Advancements of Digital Twin Technology for Bridges and Tunnels: A Sys | JPHF3PY9 | abstract-grounded | databases | digital twin|digital twin | infrastructure|asset mana | safety|monitoring|life-cy |
| 276 | [90] | LuYuqian2020 | Y. Lu, C. Liu, K. I-K. Wang, H. Huang, X. Xu | 2020 | Digital Twin-driven smart manufacturing: Connotation, reference model, | 6VU4VXU4 | verified | other methods |  |  |  |
| 277 | [] | M-Franciosi2024 | M. Franciosi; M. Kasser; M. Viviani | 2024 | Digital twins in bridge engineering for streamlined maintenance and en | 8U862S4V | abstract-grounded | databases | digital twin|digital twin | construction|bridge|struc | safety|life cycle|mainten |
| 278 | [] | M-Pregnolato2022 | M. Pregnolato; S. Gunner; E. Voyagaki; R. De  | 2022 | Towards Civil Engineering 4.0: Concept, workflow and application of Di | 4PFFHRSS | abstract-grounded | databases | digital twins | construction|civil engine |  |
| 279 | [] | M-Repetto2026 | M. Repetto | 2026 | Cybersecurity Digital Twins: Concept, blueprint, and challenges for mu | 5WDI3BIK | abstract-grounded | databases | digital twin|digital twin | architecture |  |
| 280 | [] | Machado2023 | F. V. Machado, F. T. Berssaneti | 2023 | Construction 4.0 maturity model: A survey of academia and the construc | PTD7AVWZ | verified | other methods |  |  |  |
| 281 | [] | Mahdi-Rezaali2025 | Mahdi Rezaali; Seyed Hossein Hosseini Nourzad | 2025 | Feasibility of Modern Project Management Implementation in the Constru | NT8SCTPN | abstract-grounded | databases | digital twin|bim|building | construction|building | quality |
| 282 | [] | Maksym-Spiryagin2023 | Maksym Spiryagin; Johannes Edelmann; Florian  | 2023 | Vehicle system dynamics in digital twin studies in rail and road domai | S8DTESXA | verified | databases | digital twin|digital twin | construction|road |  |
| 283 | [] | Mannino-Antonino2019 | Mannino Antonino; Moretti Nicola; Dejaco Mari | 2019 | Office building occupancy monitoring through image recognition sensors | LKINB8B7 | abstract-grounded | databases | digital twin|bim|building | aeco|construction|buildin | artificial intelligence|m |
| 284 | [] | Manuel-Bandala2024 | Manuel Bandala; Patrick Chard; Neil Cockbain; | 2024 | Digital twin challenges and opportunities for nuclear fuel manufacturi | XGVG95QH | verified | databases | digital twin | construction |  |
| 285 | [] | Marcin-Gorski2025 | Marcin Górski; Krzysztof Grzyb; Jakub Zając | 2025 | Robotic devices for Structural Health Monitoring | 9AD2CEV7 | abstract-grounded | databases | digital twin|building inf | construction|building|str | safety|quality|monitoring |
| 286 | [] | Marco-Lindner2026 | Marco Lindner; Henrik Funke; Sandra Gelbrich; | 2026 | Continuous Production of Thin‐Walled, Fiber‐Reinforced Precision Concr | BW6CX8KM | abstract-grounded | databases | digital twin | construction|concrete|mod | quality |
| 287 | [] | Marcos-Massao-Futai2022 | Marcos Massao Futai; Túlio N. Bittencourt; He | 2022 | Challenges in the application of digital transformation to inspection  | 8Z6ZF6KG | abstract-grounded | databases | digital twins | infrastructure|bridge|str | safety|predictive|monitor |
| 288 | [] | Marek-Jasek2025 | Marek Jašek; Darja Kubečková | 2025 | The digital twin on a residential housing in the Czech Republic on the | XFSADITI | abstract-grounded | databases | digital twin|bim|building | construction|building|bui | quality|carbon |
| 289 | [] | Maria-Azzalin2025 | Maria Azzalin | 2025 | Research and Academic Entrepreneurship: Technological Transfer in the  | Q5SVBVM6 | abstract-grounded | databases | digital twins | construction|built enviro |  |
| 290 | [] | Maria-Megia2024 | María Megía; Francisco Javier Melero; Manuel  | 2024 | Generative Adversarial Networks for Improved Model Training in the Con | BXDDTD8J | verified | databases | digital twin|digital twin | aeco|construction|archite | quality|monitoring |
| 291 | [] | Mariam-Elnour2024 | Mariam Elnour; Ahmad M. Ahmad; Shimaa Abdelka | 2024 | Empowering smart cities with digital twins of buildings: Applications  | 5CR2QTJ6 | abstract-grounded | databases | digital twin|digital twin | building|buildings|infras | machine learning|energy|s |
| 292 | [] | Mark-Allan2025 | Mark Allan; Abbas Rajabifard; Benny Chen; Gre | 2025 | Utilising urban digital twins for sustainable urban regeneration: Melb | JMATYUUA | abstract-grounded | databases | digital twin|digital twin | urban | quality |
| 293 | [] | Markus-Hofmeister2024 | Markus Hofmeister; George Brownbridge; Michae | 2024 | Cross-domain flood risk assessment for smart cities using dynamic know | 7ZKCICE7 | abstract-grounded | databases | digital twins | building|infrastructure|b | risk assessment|risk|real |
| 294 | [] | Martina-Signorini2025 | Martina Signorini; Alice Paola Pomè | 2025 | Shaping the future of facility management. Market and literature insig | F5C4S7RP | abstract-grounded | databases | digital twin | construction|facility man | predictive|artificial int |
| 295 | [21] | Martinez-Aires2018 | M. D. Martinez-Aires, M. Lopez-Alonso, and M. | 2018 | Building information modeling and safety management: A systematic revi | TF4RA96S | verified | other methods |  |  |  |
| 296 | [] | Masoud-Mohammadi2023 | Masoud Mohammadi; Maria Rashidi; Mojtaba Gorj | 2023 | Modern damage measurement of structural elements: Experiment, terrestr | 26SQDNPT | abstract-grounded | databases | digital twin | construction|structural|s | monitoring|structural hea |
| 297 | [] | Masthanvali-Mogal2025 | Masthanvali Mogal; Chandra Shekar Chennamalla | 2025 | Environmental Factors and Off-Highway Vehicle Safety Abstract | JD79H25I | abstract-grounded | databases | digital twins | construction|highway | safety|predictive|mainten |
| 298 | [] | Mateusz-Poszaj-Mazurek2026 | Mateusz Płoszaj-Mazurek; Anna Tofiluk | 2026 | A workflow for LLM-assisted IFC data enrichment to support circular re | 2DB37KT5 | abstract-grounded | databases | digital twins|bim|buildin | construction|building|bui | semantic|artificial intel |
| 299 | [] | Matthew-Bartos2021 | Matthew Bartos; Branko Kerkez | 2021 | Pipedream: An interactive digital twin model for natural and urban dra | 4RFH2LND | abstract-grounded | databases | digital twin|digital twin | urban | quality|sensor|maintenanc |
| 300 | [44] | Matthews2021 | Peter E.D. Love, Jane Matthews | 2021 | The 'how' of benefits management for digital technology: From engineer | S9KGUJLS | verified | other methods |  |  |  |
| 301 | [] | Matthias-Kalla2023 | Matthias Kalla; Oya Kalaycioglu; Robert Hecht | 2023 | Station biophilia – assessing the perception of greenery on railway pl | Y8L4TID6 | abstract-grounded | databases | digital twin | buildings|railway|urban | safety|semantic |
| 302 | [] | Mauricio-de-Oliveira-Gondak2025 | Maurício de Oliveira Gondak; Cleiton Hluszko; | 2025 | Guide to digital technologies for circularity in the project lifecycle | GR9HDM7P | abstract-grounded | databases | digital twins|bim|buildin | construction|building | lifecycle|carbon|blockcha |
| 303 | [] | Max-Mowbray2021 | Max Mowbray; Thomas R. Savage; Chufan Wu; Ziq | 2021 | Machine learning for biochemical engineering: A review | R982Y6UG | abstract-grounded | databases | digital twins | construction | machine learning |
| 304 | [] | Meiqi-Lu2024 | Meiqi Lu; Maxwell Fordjour Antwi-Afari | 2024 | A scientometric analysis and critical review of digital twin applicati | YDCE26GZ | abstract-grounded | databases | digital twin | construction|asset manage | artificial intelligence|m |
| 305 | [] | Meisam-Jaberi2025 | Meisam Jaberi; Charlotte Dautremont; Erik A.  | 2025 | An evaluation of digital capabilities to enable a sustainable built as | VFI3YTUY | verified | databases | digital twin|digital twin | built asset|building|indo | quality|sensor|energy|sim |
| 306 | [] | Mergen-Kor2022 | Mergen Kor; Ibrahim Yitmen; Sepehr Alizadehsa | 2022 | An investigation for integration of deep learning and digital twins to | FKLPV2RE | abstract-grounded | databases | digital twins | construction|building | decision-support|deep lea |
| 307 | [] | Michael-Bekele-Maru2023 | Michael Bekele Maru; Yusen Wang; Hansun Kim;  | 2023 | Improved building facade segmentation through digital twin-enabled Ran | 4XWTBWHY | abstract-grounded | databases | digital twin | construction|building|arc | deep learning|point cloud |
| 308 | [] | Milos-Milasinovic2023 | Miloš Milašinović; Damjan Ivetić; Milan Stojk | 2023 | Failure Conditions Assessment of Complex Water Systems Using Fuzzy Log | 8NTQBDS5 | abstract-grounded | databases | digital twins | infrastructure|dam | risk|causal|energy|mainte |
| 309 | [] | Ming-Guo2025 | Ming Guo; Xiaoke Shang; Jiawei Zhao; Yanru Sh | 2025 | Digital twin models for architectural heritage conservation | A9KX5D9N | title-only | databases | digital twin | architectural|heritage |  |
| 310 | [] | Mingchao-Li2021 | Mingchao Li; Qiaorong Lu; Shuo Bai; Mengxi Zh | 2021 | Digital twin-driven virtual sensor approach for safe construction oper | H3NC5M52 | title-only | databases | digital twin | construction | sensor |
| 311 | [] | Minhaj-Uddin-Ahmad2026 | Minhaj Uddin Ahmad; Sagar Dasgupta; Mizanur R | 2026 | Lessons Learned from the Real-World Deployment of Multisensor Fusion f | HEVK3EDL | abstract-grounded | databases | digital twin | infrastructure|bridge | safety|predictive|sensor| |
| 312 | [] | MinQi2019 | Qingfei Min, Yangguang Lu, Zhiyong Liu, Chao  | 2019 | Machine learning based digital twin framework for production optimizat | WSF2RF5M | verified | other methods |  |  |  |
| 313 | [] | Mirko-Baratta2024 | Mirko Baratta; Valerio Di Mascio; Daniela Mis | 2024 | Development of a NG Engine Predictive Simulation Model and Investigati | CWRXNDFI | abstract-grounded | databases | digital twin | infrastructure | predictive|energy|simulat |
| 314 | [] | Mirsalar-Kamari2022 | Mirsalar Kamari; Jaeyoon Kim; Youngjib Ham | 2022 | Analyzing Safety Risk Imposed by Jobsite Debris to Nearby Built Enviro | LRQ4MPUT | abstract-grounded | databases | digital twins | construction|built enviro | safety|risk assessment|ri |
| 315 | [] | Mohammad-Azizur-Rahman2024 | Mohammad Azizur Rahman; Abinash Barooah; Muha | 2024 | Single and multiphase flow leak detection in onshore/offshore pipeline | DTKXRQS3 | abstract-grounded | databases | digital twin | construction|pipeline | quality|machine learning| |
| 316 | [] | Mohanraj-Arumugam2024 | Mohanraj Arumugam | 2024 | BIM AND AI INTEGRATION FOR SMART AND SUSTAINABLE INFRASTRUCTURE: A COM | IDBD7TFA | abstract-grounded | databases | digital twin|bim|building | construction|building|inf | predictive|machine learni |
| 317 | [] | Nan-Ma2026 | Nan Ma; Rania Labib; Robert Amor; Adrian Chon | 2026 | Ten questions concerning Large Language Models (LLMs) for building app | S5X3D92F | abstract-grounded | databases | digital twins | construction|built enviro | life cycle|energy|mainten |
| 318 | [] | Naveen-Narayanan2025 | Naveen Narayanan; S. P. Harsha | 2025 | Advancements in Vibration-Based Damage Detection for Railway Tracks: A | RM3P5BMJ | abstract-grounded | databases | digital twin | infrastructure|structural | safety|predictive|machine |
| 319 | [] | Necati-Catbas2023 | Necati Catbas; Onur Avci | 2023 | A review of latest trends in bridge health monitoring | Y2RYK9D5 | abstract-grounded | databases | digital twins | civil engineering|bridge| | safety|machine learning|d |
| 320 | [] | Negin-Khosh-Amadi2026 | Negin Khosh-Amadi; Saeed Talebi; Franco Cheun | 2026 | Development of a spatially contextualised and AI-enabled digital twin  | GXK2JGXL | title-only | databases | digital twin | indoor | quality |
| 321 | [] | Nehal-Elshaboury2025 | Nehal Elshaboury; Wael M. AlMetwaly; Amr Hesh | 2025 | Integrated BIM-GIS framework for holistic building stock assessment us | MR3JI45K | title-only | databases | digital twin|bim | building |  |
| 322 | [] | Nicola-Moretti2025 | Nicola Moretti; Yin-Chi Chan; Momoko Nakaoka; | 2025 | Data integration for space-aware Digital Twins of hospital operations | SXDLSN8P | abstract-grounded | databases | digital twin|digital twin | built asset|building|arch | simulation |
| 323 | [] | Nima-Moghimi2026 | Nima Moghimi; Oldouz Arshang; Farook Hamzeh | 2026 | Digital twins in offsite construction: Current implementations, challe | 3PF4T3LM | abstract-grounded | databases | digital twin|digital twin | construction|bridge|site| | monitoring |
| 324 | [] | Nour-Samaro2025 | Nour Samaro; Timo Hartmann; Fuad Baba; Susana | 2025 | Developing a system reference architecture for assessing risks of heat | CWL4I4JV | abstract-grounded | databases | digital twins|bim|buildin | built environment|buildin | risk assessment|risk|deci |
| 325 | [] | null-AkinyemiAbiodun2022 | null AkinyemiAbiodun; null ErdoganBilge; null | 2022 | Briefing: Process digital twin: lessons learned from a construction ca | B3EIZQ92 | abstract-grounded | databases | digital twin | construction |  |
| 326 | [] | Obinna-C-Madubuike2023 | Obinna C. Madubuike; Chimay J. Anumba | 2023 | Digital Twin–Based Health Care Facilities Management | K388NE9M | abstract-grounded | databases | digital twin | facilities management|ind | safety|quality|monitoring |
| 327 | [] | Olympia-Ageli2026 | Olympia Ageli; Athanasios Chassiakos | 2026 | Balancing indoor environmental quality and energy efficiency in buildi | LGKAWR8D | title-only | databases | digital twins | buildings|indoor | quality|energy |
| 328 | [] | Omar-Doukari2026 | Omar Doukari; Tugce Bacnak; Elham Mahamedi | 2026 | Stakeholder-informed renovation digital twin for multi-domain monitori | VFRKG77L | abstract-grounded | databases | digital twin | aeco|construction|built e | safety|quality|predictive |
| 329 | [] | Omobolanle-Ruth-Ogunseiju2021 | Omobolanle Ruth Ogunseiju; Johnson Olayiwola; | 2021 | Digital twin-driven framework for improving self-management of ergonom | ACZQMMUG | abstract-grounded | databases | digital twin|digital twin | construction | real-time |
| 330 | [74] | Omrany2023 | H. Omrany, K. M. Al-Obaidi, A. Husain, and A. | 2023 | Digital twins in the construction industry: A comprehensive review of  | CW78JTWI | verified | other methods |  |  |  |
| 331 | [33] | Opoku2021 | D.-G. Opoku, S. Perera, R. Osei-Kyei, and M.  | 2021 | Digital twin application in the construction industry: A literature re | LUGQBL7W | verified | databases | digital twin | construction |  |
| 332 | [73] | Ozturk2021 | G. B. Ozturk | 2021 | Digital Twin Research in the AECO-FM Industry, | BLMII5EA | verified | databases | digital twin | aeco |  |
| 333 | [] | Parinaz-Ebrahimian2025 | Parinaz Ebrahimian; Maryam Bitaraf | 2025 | Automated model updating of digital twins using double-deep Q network  | 3GB249Z6 | title-only | databases | digital twins | architecture |  |
| 334 | [] | Parsa-Namaki2025 | Parsa Namaki; Hossein Shahir; Mona Ahani; Ami | 2025 | A novel digital twin framework for improving urban sustainability–feas | SSC26KVU | title-only | databases | digital twin | buildings|urban |  |
| 335 | [] | Parshva-Patel2023 | Parshva Patel; Roy Sturgill; Hala Nassereddin | 2023 | Current Benefits of ASCE 75 and its Potential to Affect Digital As-Bui | K5G7YVSE | abstract-grounded | databases | digital twins | construction|civil engine | safety|quality |
| 336 | [] | Patrick-Forman2026 | Patrick Forman; Luca Dannemann; Peter Mark | 2026 | Adaptive, Modularized Constructions Made in a Flux | JTD8KQHF | abstract-grounded | databases | digital twin | construction|building|str |  |
| 337 | [] | Pedro-F-Pereira2022 | Pedro F. Pereira; Nuno M.M. Ramos | 2022 | Low-cost Arduino-based temperature, relative humidity and CO2 sensors  | GKMR8ZKD | abstract-grounded | databases | digital twins | indoor | quality|sensor|carbon|ene |
| 338 | [] | Pedro-Meda2026 | Pedro Mêda; Diego Calvetti; Helena Corvacho;  | 2026 | European sustainable built environment vision framework: critical revi | FYDFNI56 | abstract-grounded | databases | digital twins | construction|built enviro | energy |
| 339 | [] | Peiman-Tavakoli2023 | Peiman Tavakoli; Ibrahim Yitmen; Habib Sadri; | 2023 | Blockchain-based digital twin data provenance for predictive asset man | BV5Y9TQ3 | abstract-grounded | databases | digital twin | built environment|buildin | predictive|maintenance|re |
| 340 | [] | Pekka-Isto2020 | Pekka Isto; Tapio Heikkilä; Aarne Mammela; Mi | 2020 | 5G Based Machine Remote Operation Development Utilizing Digital Twin | M4WPLWVT | verified | databases | digital twin | infrastructure|architectu | real-time |
| 341 | [] | Peng-Xiao2026 | Peng Xiao | 2026 | A Data-Driven Digital Twin-Based Framework for Attack Chain Modeling a | DB6AV7U6 | verified | databases | digital twin|cyber-physic | architecture | energy|simulation |
| 342 | [] | Peng-Yang2020 | Peng Yang; Zhang Ming; Yu Fangqiang; Xu Jingl | 2020 | Digital Twin Hospital Buildings: An Exemplary Case Study through Conti | 6VGXIJ7F | verified | databases | digital twin|bim | construction|building|bui | quality|lifecycle|energy| |
| 343 | [] | Pengfei-Jia2026 | Pengfei Jia | 2026 | Data-physics fusion-based dual-drive dynamic simulation of power syste | CCNYAESK | verified | databases | digital twin|digital twin | construction | simulation |
| 344 | [] | Perdana-Miraj2025 | Perdana Miraj; Tong Wang; Alexander Koutamani | 2025 | Organising digital twin in the built environment: a systematic review  | KD9LNZIB | verified | databases | digital twin | construction|built enviro | safety|lifecycle|maintena |
| 345 | [92] | Pereira2025 | F. Pereira, M. de las Nieves González García, | 2025 | BIM for Safety: Applying Real-Time Monitoring Technologies to Prevent  | EWGI4UA4 | verified | other methods |  |  |  |
| 346 | [] | Philipp-Hagedorn2026 | Philipp Hagedorn; Nina Krautgartner; Franzisk | 2026 | Linking Design, Deconstruction and Characterization: A Digital Ecosyst | 9U9THI7U | abstract-grounded | databases | digital twins | construction|building|bui | simulation |
| 347 | [] | Piotr-azinski2025 | Piotr Łaziński; Stefan Pradelok; Marcin Jasiń | 2025 | Reconstruction of the road bridge on Monte Cassino Avenue in Koszalin | IRKUBURF | abstract-grounded | databases | digital twin | infrastructure|facility m | safety|risk|life cycle |
| 348 | [] | Pome2023 | Andrea Giovanni Pomè, Cinzia Maria Luisa Sign | 2023 | Digital twin for the built environment: Review of current research and | NURYJTQW | verified | other methods |  |  |  |
| 349 | [] | Pooya-Rezadoost2025 | Pooya Rezadoost; Behrouz Asgarian | 2025 | A hybrid data-driven algorithm for digital twin of tubular joints in o | UJILXG78 | abstract-grounded | databases | digital twin|digital twin | structural | quality|predictive|monito |
| 350 | [] | Pradeep-Alva2024 | Pradeep Alva; Martín Mosteiro-Romero; Clayton | 2024 | Mitigating operational greenhouse gas emissions in ageing residential  | GBGSTB56 | abstract-grounded | databases | digital twin | built environment|buildin | carbon|maintenance|inspec |
| 351 | [] | Pragna2026 | K. Sai Pragna, Yukta Paranjpe, Suraj Mallapur | 2026 | An integrated machine learning approach for accident risk classificati | WHW4PTNF | verified | other methods |  |  |  |
| 352 | [] | Qasim-Zaheer2026 | Qasim Zaheer; Shi Qiu; Zunaira Atta; S Muhamm | 2026 | Transforming railway transportation: the role of emerging technologies | TKZAE9XE | abstract-grounded | databases | digital twin | infrastructure|railway | safety|predictive|artific |
| 353 | [23] | Qi2014 | J. Qi, R. R. A. Issa, S. Olbina, and J. Hinze | 2014 | Use of Building Information Modeling in Design to Prevent Construction | QW2EQIJ5 | verified | other methods |  |  |  |
| 354 | [83] | Qi2021 | Q. Qi, F. Tao, T. Hu, N. Anwer, A. Liu, Y. We | 2021 | Enabling technologies and tools for digital twin, | FFM3DXDC | verified | other methods |  |  |  |
| 355 | [] | Qianmai-Luo2024 | Qianmai Luo; Chengshuang Sun; Ying Li; Zhenqi | 2024 | Applications of digital twin technology in construction safety risk ma | 3646US9N | abstract-grounded | databases | digital twin | construction|site | safety|risk|decision supp |
| 356 | [] | Radford2021 | Alec Radford, Jong Wook Kim, Chris Hallacy, A | 2021 | Learning Transferable Visual Models From Natural Language Supervision  | WMDJY52E | verified | other methods |  |  |  |
| 357 | [] | Rafael-Chehab-Canto-Pereira2024 | Rafael Chehab Canto Pereira; Pedro Nogueira d | 2024 | BIM-enabled strategies for dams and hydroelectric structures: a compre | SK5VP4H2 | abstract-grounded | databases | digital twins|bim | construction|structure|da | safety|quality|maintenanc |
| 358 | [] | RajratnaKharat2018 | Rajratna Kharat, Vikas Bavane | 2018 | Detection of cracks on concrete surfaces using digital image processin | 9SMJBZXV | verified | other methods |  |  |  |
| 359 | [] | Ranjith-K-Soman2025 | Ranjith K. Soman; Karim Farghaly; Grant Mills | 2025 | Digital twin construction with a focus on human twin interfaces | FGAMEIKE | abstract-grounded | databases | digital twin|digital twin | construction | machine learning |
| 360 | [54] | Rasheed2020 | Adil Rasheed, Omer San, Trond Kvamsdal | 2020 | Digital Twin: Values, Challenges and Enablers From a Modeling Perspect | MKZ3HU7D | verified | other methods |  |  |  |
| 361 | [] | Rebecca-Ward2023 | Rebecca Ward; Ruchi Choudary; Melanie Jans Si | 2023 | The challenges of using live-streamed data in a predictive digital twi | 9EL7VW7K | verified | databases | digital twin|digital twin | infrastructure | quality|predictive|simula |
| 362 | [] | Roberto-Brandin2024 | Roberto Brandín; Sepehr Abrishami | 2024 | IoT-BIM and blockchain integration for enhanced data traceability in o | 8ZQL5BC3 | abstract-grounded | databases | bim|building information  | building|infrastructure|a | quality|iot|real-time|blo |
| 363 | [] | Rolando-Chacon2023 | Rolando Chacón; Carlos Ramonell; Hector Posad | 2023 | Digital twinning during load tests of railway bridges - case study: th | P3IB6ZYS | verified | databases | digital twin | construction|bridge|railw | maintenance|simulation |
| 364 | [] | Rolando-Chacon2023 | Rolando Chacón; Joan R. Casas; Carlos Ramonel | 2023 | Requirements and challenges for infusion of SHM systems within Digital | W7WI8FSS | verified | databases | digital twin | structural|pipeline | monitoring|structural hea |
| 365 | [] | Rolando-Chacon2024 | Rolando Chacón; Hector Posada; Carlos Ramonel | 2024 | Digital twinning of building construction processes. Case study: A rei | SST937PL | abstract-grounded | databases | digital twin|digital twin | construction|building|str | safety|monitoring|knowled |
| 366 | [] | Rolando-Chacon2026 | Rolando Chacón; Carlos Ramonell; Marc Ventosa | 2026 | Semantic digital twins for masonry bridges: Structuring geometrical, m | TKDRSKP9 | abstract-grounded | databases | digital twin|digital twin | infrastructure|bridge|str | quality|semantic|scan-to- |
| 367 | [] | Runze-Mao2025 | Runze Mao; Yuanjiang Li; Guoyuan Li; Hans Pet | 2025 | A Systematic Survey of Digital Twin Applications: Transferring Knowled | B7NQRD5P | abstract-grounded | databases | digital twin | bridge | safety|predictive|monitor |
| 368 | [] | Ruodan-Lu2019 | Ruodan Lu; Ioannis Brilakis | 2019 | Digital twinning of existing reinforced concrete bridges from labelled | 76LLSD64 | abstract-grounded | databases | digital twin|digital twin | bridge|foundation|concret | quality|point cloud|autom |
| 369 | [] | Ruonan-Wang2026 | Ruonan Wang | 2026 | A data-driven predictive maintenance framework for smart buildings: In | J4DTPCK9 | title-only | databases | digital twin | buildings | predictive|machine learni |
| 370 | [82] | Ruppert2020 | T. Ruppert and J. Abonyi | 2020 | Integration of real-time locating systems into digital twins | IJUPSPJB | verified | other methods |  |  |  |
| 371 | [] | S-J-Jiang2025 | S.J. Jiang; Y.L. Xu; S.M. Li; D.H. Dan; G.Q.  | 2025 | Digital twin-based identification of aerodynamic admittance functions  | HAPFB79E | title-only | databases | digital twin | bridge |  |
| 372 | [] | S-V-Fedosov2026 | S. V. Fedosov; I. V. Krasilnikov; V. E. Rumya | 2026 | Methods of heat and mass transfer theory for modeling raw arbolite blo | JMH2DVDC | abstract-grounded | databases | digital twin | structural | quality|risk |
| 373 | [49] | Sacks2009 | R. Sacks, S. Rozenfeld, and Y. Rosenfeld | 2009 | Spatial and temporal exposure to safety hazards in construction, | RL2W6VYI | verified | other methods |  |  |  |
| 374 | [32] | Sacks2020 | R. Sacks, I. Brilakis, P. Pikas, H. Xie, and  | 2020 | Construction with digital twin information systems, | FBV29DAQ | verified | other methods |  |  |  |
| 375 | [] | Saeed-Reza-Mohandes2024 | Saeed Reza Mohandes; Atul Kumar Singh; Abdulw | 2024 | Determining the stationary digital twins implementation barriers for s | 3YMFX45Y | abstract-grounded | databases | digital twin|digital twin | construction|building|arc | quality|real-time |
| 376 | [] | Sakibu-Seidu2025 | Sakibu Seidu; Daniel W.M. Chan; Margaret Dami | 2025 | Leveraging digital technologies and machine learning for climate resil | WHKUGBU6 | verified | databases | digital twins|building in | construction|building|bui | machine learning |
| 377 | [] | Salih-Sarp2024 | Salih Sarp; Murat Kuzlu; Vukica Jovanovic; Ze | 2024 | Digitalization of railway transportation through AI-powered services:  | WANUG77J | verified | databases | digital twin | infrastructure|architectu | safety|artificial intelli |
| 378 | [] | Samad-M-E-Sepasgozar2021 | Samad M. E. Sepasgozar; Mohsen Ghobadi; Sara  | 2021 | Metrics development and modelling the mixed reality and digital twin a | B7F5UYJR | abstract-grounded | databases | digital twin | aeco|construction|archite | safety|risk|predictive |
| 379 | [] | Samuel-Aklashie2026 | Samuel Aklashie; Kofi Agyekum; Eric Tutu Tcha | 2026 | Blockchain-digital twin integration in construction material passports | WQ4RM3RC | abstract-grounded | databases | digital twin|digital twin | construction|buildings | quality|monitoring|lifecy |
| 380 | [] | Samuel-Jimenez2021 | Samuel Jimenez; Darren Bookless; Radhika Nath | 2021 | Automated maintenance feasibility testing on the EU DEMO Automated Ins | FGSPN6ZQ | abstract-grounded | databases | digital twin | architecture | safety|maintenance|inspec |
| 381 | [] | Samuel-Park2024 | Samuel Park; Jaekyoung Kim; Yejin Kim; Junsuk | 2024 | Participatory Framework for Urban Pluvial Flood Modeling in the Digita | L2BVXH4V | title-only | databases | digital twin | urban |  |
| 382 | [] | Sanjar-Ahmad2023 | Sanjar Ahmad; Maksym Spiryagin; Qing Wu; Este | 2023 | Development of a Digital Twin for prediction of rail surface damage in | JZ9XG3CQ | verified | databases | digital twin|digital shad | railway | predictive|sensor|mainten |
| 383 | [] | Sara-Rashidian2025 | Sara Rashidian; SK Tahsin Hossain; Kirsty Vol | 2025 | Enabling circularity in construction: A technology-phase alignment of  | AAP5RYKU | abstract-grounded | databases | digital twins|bim|buildin | construction|building|bui | predictive|artificial int |
| 384 | [] | Saviz-Moghtadernejad2026 | Saviz Moghtadernejad; Zoubir Lounis; Jieying  | 2026 | Digitalizing Bridge Management: Current Trends, Challenges, and a Prac | HZ5CK5GM | abstract-grounded | databases | digital twins | infrastructure|bridge|hig | safety|monitoring|life-cy |
| 385 | [53] | Schleich2017 | J. B. Schleich, N. Anwer, L. Mathieu, and S.  | 2017 | Shaping the digital twin for design and production engineering, | MNQ7TJ9H | verified | other methods |  |  |  |
| 386 | [] | Sebastjan-Meza2021 | Sebastjan Meža; Alenka Mauko Pranjić; Rok Vez | 2021 | Digital Twins and Road Construction Using Secondary Raw Materials | Q9E2BMW8 | verified | databases | digital twin|digital twin | construction|civil engine | monitoring |
| 387 | [] | Selen-Gecgel-Cetin2026 | Selen Geçgel Çetin; Barş Dönmez; Güneş Karabu | 2026 | Advancing Lunar Communication Through Interdomain Space Networks and D | PSNST2NJ | abstract-grounded | databases | digital twin | infrastructure|architectu | risk|real-time |
| 388 | [] | Seongha-Hwang2026 | Seongha Hwang; Karen Blay; Mohamed Osmani; Mi | 2026 | Blockchain-Integrated Relational Project Governance | NUVL3IK5 | abstract-grounded | databases | digital twins | construction|building | quality|artificial intell |
| 389 | [36] | Sepasgozar2020 | M. Sepasgozar | 2020 | Digital twin and web-based virtual gaming technologies for online educ | 2I3BUC9T | verified | other methods |  |  |  |
| 390 | [72] | Sepasgozar2021 | S. M. E. Sepasgozar | 2021 | Differentiating digital twin from digital shadow: Elucidating a paradi | NT452J52 | verified | other methods |  |  |  |
| 391 | [] | Sepehr-Alizadehsalehi2021 | Sepehr Alizadehsalehi; Ibrahim Yitmen | 2021 | Digital twin-based progress monitoring management model through realit | KURDXPIK | abstract-grounded | databases | digital twin|bim | construction|structural | semantic|monitoring|real- |
| 392 | [] | Seth-Guikema2024 | Seth Guikema; Roger Flage | 2024 | Digital twins as a security risk? | KBS6YF4M | verified | databases | digital twin|digital twin | building | risk|hazard |
| 393 | [] | Seyi-Stephen2025 | Seyi Stephen; Clinton Aigbavboa; Ayodeji Oke; | 2025 | Enhancing sustainability through the integration of digital twins in s | T6HP5VTH | verified | databases | digital twins | construction |  |
| 394 | [79] | Shahzad2022 | M. Shahzad, M. T. Shafiq, D. Sturges, and S.  | 2022 | Digital twins in built environments: An investigation of the character | IX4N6UJ9 | verified | other methods |  |  |  |
| 395 | [] | Shanshan-Hu2023 | Shanshan Hu; Qingwei Liang; Hancheng Huang; C | 2023 | Construction of a digital twin system for the blended-wing-body underw | THJ4Z83T | abstract-grounded | databases | digital twin | construction|building | safety|sensor|simulation |
| 396 | [] | Shengjun-Tang2023 | Shengjun Tang; Hongsheng Huang; Yunjie Zhang; | 2023 | Skeleton-guided generation of synthetic noisy point clouds from as-bui | YRWEPR6G | title-only | databases | bim | indoor |  |
| 397 | [] | Shengnan-Zhang2026 | Shengnan Zhang | 2026 | Digital Twin Technology-Enabled Water Resources Asset Accounting Super | GCMCPUEM | verified | databases | digital twin | asset management | quality|risk|monitoring|a |
| 398 | [] | Shi-Qiu2023 | Shi Qiu; Xianhua Liu; Jun Peng; Weidong Wang; | 2023 | Fine-Grained Point Cloud Semantic Segmentation of Complex Railway Brid | YQ47YXFC | verified | databases | digital twin | infrastructure|bridge|rai | quality|semantic|point cl |
| 399 | [] | Shi-Qiu2025 | Shi Qiu; Qasim Zaheer; Fahad Ali; Saif Wajid; | 2025 | Exploring the impact of digital twin technology in infrastructure mana | C8LFJNVC | verified | databases | digital twin|digital twin | building|infrastructure | artificial intelligence|i |
| 400 | [] | Shi-Qiu2025 | Shi Qiu; Qasim Zaheer; S. Muhammad Ahmed Hass | 2025 | LiDAR-Simulated Multimodal and Self-Supervised Contrastive Digital Twi | 9W6ZVZSQ | abstract-grounded | databases | digital twin|digital twin | infrastructure | safety|monitoring|point c |
| 401 | [] | Shuangping-Li2025 | Shuangping Li; Bin Zhang; Guangqin Tong; Yong | 2025 | Online Intelligent Monitoring System and Key Technologies for Dam Oper | ZVUCU665 | abstract-grounded | databases | digital twin|bim|building | building|infrastructure|s | safety|machine learning|a |
| 402 | [] | Shubham-Baisthakur2021 | Shubham Baisthakur; Arunasis Chakraborty | 2021 | Experimental verification for load rating of steel truss bridge using  | BTD9ADR2 | abstract-grounded | databases | digital twin | bridge|structure | risk|sensor|simulation |
| 403 | [] | Silvia-Galvan-Nunez2025 | Silvia Galván-Núñez; Ryan Alishio; Christophe | 2025 | Digital Twin Vision for Freight Railroads: A Case Study in North Ameri | XZTTEJPS | abstract-grounded | databases | digital twin|digital twin | infrastructure | safety|predictive|monitor |
| 404 | [] | Simon-Elias-Bibri2025 | Simon Elias Bibri; Jeffrey Huang; Osama Omar; | 2025 | Synergistic integration of digital twins and zero energy buildings for | QD2LYWF4 | abstract-grounded | databases | digital twins|cyber-physi | buildings|urban | predictive|artificial int |
| 405 | [] | Simon-Kosse2026 | Simon Kosse; Patrick Forman; Peter Gänz; Bene | 2026 | Digital Twin‐Based Quality Control: Ensuring Precision in Precast Conc | JL8F4AQ3 | abstract-grounded | databases | digital twin | bridge|structural|structu | quality|monitoring |
| 406 | [89] | Singh2021 | M. Singh, E. Fuenmayor, E. P. Hinchy, Y. Qiao | 2021 | Digital Twin: Origin to Future, | R2NLMGZ8 | verified | other methods |  |  |  |
| 407 | [] | Sitsofe-Kwame-Yevu2023 | Sitsofe Kwame Yevu; Emmanuel Kingsford Owusu; | 2023 | Digital twin-enabled prefabrication supply chain for smart constructio | K4MMWQIM | title-only | databases | digital twin | construction|building | carbon |
| 408 | [] | Siyuan-Meng2026 | Siyuan Meng; Longyong Wu; Maosu Li; Anthony G | 2026 | Automated window detection for digital twin buildings: A generalized ' | MX8XMSQ6 | abstract-grounded | databases | digital twin|digital twin | construction|buildings | semantic|deep learning|en |
| 409 | [] | Soheila-Kookalani2026 | Soheila Kookalani; Stephen Green; Peihang Luo | 2026 | Mapping digital twin applications in infrastructure and the built envi | 69KEXEK7 | abstract-grounded | databases | digital twin|digital twin | construction|built enviro | predictive|artificial int |
| 410 | [] | Solomon-Alemneh-Adimass2026 | Solomon Alemneh Adimass; Arkadiusz Żak | 2026 | Review of Digital Twin in Structural Dynamics to Improve Condition Mon | 7GYU8BC7 | verified | databases | digital twin|digital twin | infrastructure|structural | predictive|monitoring|str |
| 411 | [11] | Spinner2024 | Patrick Spinner, Amir Degani | 2024 | Online as-built building information model update for robotic monitori | ULJGBQZ6 | verified | other methods |  |  |  |
| 412 | [55] | Stargel2012 | E. Glaessgen and D. Stargel | 2012 | The digital twin paradigm for future NASA and U.S. Air Force vehicles, | 8B7R5BZU | verified | other methods |  |  |  |
| 413 | [] | Stephane-Gazzotti2021 | Stephane Gazzotti; F. Ferlay; L. Meunier; P.  | 2021 | Virtual and Augmented Reality Use Cases for Fusion Design Engineering | KFJA5WXD | verified | databases | digital twins | infrastructure|site | safety|life cycle|mainten |
| 414 | [] | Sugantha-Muthusamy2025 | Sugantha Muthusamy | 2025 | Hybrid Safety Framework for Autonomous Off-Highway Vehicles | GNA2ESQM | abstract-grounded | databases | digital twin | construction|architecture | safety|sensor|fault|simul |
| 415 | [] | Sun2023 | Tianqi Sun, Sicheng He, Zheng Li | 2023 | Industry 4.0 and digital twin in the context of the COVID-19 pandemic: | RA62TL5J | verified | other methods |  |  |  |
| 416 | [] | Sungmin-Yoon2023 | Sungmin Yoon | 2023 | Building digital twinning: Data, information, and models | F5DBNXII | abstract-grounded | databases | digital twin|digital twin | building | life cycle |
| 417 | [] | Sungmin-Yoon2025 | Sungmin Yoon; Jihwan Song; Jiteng Li | 2025 | Ontology-enabled AI agent-driven intelligent digital twins for buildin | PY2YRU83 | title-only | databases | digital twins | building | ontology|maintenance |
| 418 | [] | Sunil-Prajapat2025 | Sunil Prajapat; Dheeraj Kumar; Pankaj Kumar;  | 2025 | Quantum Secure Energy-Efficient Authentication Protocol for Digital Tw | N8FFURIM | abstract-grounded | databases | digital twins|cyber-physi | infrastructure|road | safety|quality|energy|opt |
| 419 | [] | Syed-Mostasim-Hasnain-Saif2026 | Syed Mostasim Hasnain Saif; Jeyoon Lee; Peng  | 2026 | Metadata schema for virtual sensors in digital twin-enabled building s | G9IAZGT2 | title-only | databases | digital twin | building |  |
| 420 | [] | Sylvia-Keler2025 | Sylvia Keßler; Maria Pina Limongelli; Eftychi | 2025 | Special theme: Advanced through‐life management of existing concrete s | IQ8GTSWL | abstract-grounded | databases | digital twins|bim|buildin | construction|civil engine | safety|predictive|decisio |
| 421 | [] | T-Hielscher2023 | T. Hielscher; S. Khalil; N. Virgona; S.A. Had | 2023 | A neural network based digital twin model for the structural health mo | B224CZ86 | abstract-grounded | databases | digital twin | infrastructure|asset mana | predictive|neural network |
| 422 | [] | Tahreer-M-Fayyad2024 | Tahreer M Fayyad; Su Taylor; Kun Feng; Felix  | 2024 | A scientometric analysis of drone-based structural health monitoring a | DHQZ9E9N | abstract-grounded | databases | digital twins | infrastructure|structural | safety|machine learning|d |
| 423 | [8] | Tang2019 | Shu Tang, Dennis R. Shelden, Charles M. Eastm | 2019 | A review of building information modeling (BIM) and the internet of th | 4ZA4SRVJ | verified | other methods |  |  |  |
| 424 | [] | Tao-Han2025 | Tao Han; Tao Ma; Jiangyin Xiao | 2025 | Proactive perceptive road: a digital twin-driven intelligent road infr | XLM5T7EY | abstract-grounded | databases | digital twin | construction|infrastructu | quality|monitoring|mainte |
| 425 | [] | Tao2018 | Fei Tao, Meng Zhang, Yushan Liu, A. Y. C. Nee | 2018 | Digital twin-driven prognostics and health management for complex equi | FDTN2LDT | verified | other methods |  |  |  |
| 426 | [30] | Tao2019 | Fei Tao, He Zhang, Ang Liu, A. Y. C. Nee | 2019 | Digital twin in industry: State-of-the-art | MERRUE6E | verified | other methods |  |  |  |
| 427 | [91] | Tao2019b | F. Tao, Q. Qi, L. Wang, A. Y. C. Nee | 2019 | Digital Twins and Cyber-Physical Systems toward Smart Manufacturing an | -- | metadata_only | other methods |  |  |  |
| 428 | [58] | TaoZhang2017 | F. Tao and M. Zhang | 2041 | Digital twin shop-floor: A new shop-floor paradigm toward smart manufa | 2E3WDWM9 | verified | other methods |  |  |  |
| 429 | [] | Teisserenc2021 | Benjamin Teisserenc, Samad Sepasgozar | 2021 | Adoption of blockchain technology through digital twins in the constru | EN7S2R5T | verified | other methods |  |  |  |
| 430 | [37] | Teizer2010 | J. Teizer, B. Allread, C. Fullerton, and J. H | 2010 | Autonomous pro-active real-time construction worker and equipment oper | MVVXZSXY | verified | other methods |  |  |  |
| 431 | [] | Tengxiang-Su2021 | Tengxiang Su; Haijiang Li; Yi An | 2021 | A BIM and machine learning integration framework for automated propert | MNGH7DLJ | abstract-grounded | databases | bim | construction|real estate | predictive|machine learni |
| 432 | [38] | Teo2005 | Evelyn Ai Lin Teo, Florence Yean Yng Ling, Ad | 2005 | Framework for project managers to manage construction safety | QGV65BAU | verified | other methods |  |  |  |
| 433 | [10] | Theiler2018 | M. Theiler, S. Smarsly, K. Dragos | 2018 | IFC Monitor - An IFC schema extension for modeling structural health m | H98THTQ4 | verified | other methods |  |  |  |
| 434 | [] | Tianqi-Zhao2026 | Tianqi Zhao; Fei Hu; Hongye Gou; Junming Wang | 2026 | Digital twins for static and dynamic responses of a continuous rigid f | 6Z8GPFFQ | title-only | databases | digital twins | bridge | optimization |
| 435 | [] | Tianxiang-Bu2025 | Tianxiang Bu; Junqing Zhu; Tao Ma | 2025 | Automatic Modeling Framework of Existing Road Based on Point Cloud Map | LWK8YXUM | abstract-grounded | databases | digital twin|digital twin | building|infrastructure|s | quality|point cloud |
| 436 | [66] | Tixier2016 | J. P. Tixier, G. Hallowell, B. Rajagopalan, a | 2016 | Automated content analysis for construction safety: A natural language | X5U62SNQ | verified | other methods |  |  |  |
| 437 | [] | Truong-An-Pham2025 | Truong-An Pham; Veerasak Likhitruangsilp; Thu | 2025 | Common data environment of a BIM-based digital twin for real-time cons | HCDFG9S7 | abstract-grounded | databases | digital twin|bim|building | construction|building|sit | monitoring|sensor|iot|rea |
| 438 | [] | Truong-An-Pham2026 | Truong-An Pham; Photios G. Ioannou; Veerasak  | 2026 | Designing a BIM-enhanced digital twin architecture for construction po | 35NYTZKR | title-only | databases | digital twin|bim | construction|building|arc |  |
| 439 | [31] | Uhlemann2017 | M. Uhlemann, C. Lehmann, and R. Steinhilper | 2017 | The Digital Twin: Realizing the cyber-physical production system for i | 7XF73XIE | verified | other methods |  |  |  |
| 440 | [] | Vahid-Bakhtiari2023 | Vahid Bakhtiari; Farzad Piadeh; Kourosh Behza | 2023 | A critical review for the application of cutting-edge digital visualis | GM2I4AQX | abstract-grounded | databases | digital twin | urban | risk|real-time |
| 441 | [] | Vahid-Mousavi2025 | Vahid Mousavi; Maria Rashidi; Shayan Ghazimog | 2025 | Transformer-based time-series GAN for data augmentation in bridge digi | MR7KZQ29 | abstract-grounded | databases | digital twins | infrastructure|bridge|str | quality|deep learning|mon |
| 442 | [] | Valerian-Vanessa-Tuhaise2023 | Valerian Vanessa Tuhaise; Joseph Handibry Mba | 2023 | Technologies for digital twin applications in construction | A2JIG6I7 | abstract-grounded | databases | digital twin|digital twin | construction | monitoring|real-time |
| 443 | [] | Vanessa-Saback2025 | Vanessa Saback; Jens Eliasson; Cosmin Daescu; | 2025 | Digital twins for asset management: case study of snow galleries in No | A22TIBPU | verified | databases | digital twin|digital twin | construction|asset manage | predictive|monitoring|str |
| 444 | [56] | Vickers2017 | M. Grieves and J. Vickers | 2017 | Digital twin: Mitigating unpredictable, undesirable emergent behavior  | UXYJS9VB | verified | other methods |  |  |  |
| 445 | [] | Victor-Adetunji-Arowoiya2024 | Victor Adetunji Arowoiya; Ayodeji Emmanuel Ok | 2024 | Driving Factors for the Adoption of Digital Twin Technology Implementa | H4LZ47X5 | abstract-grounded | databases | digital twin | construction|architecture | safety|quality |
| 446 | [] | Victor-Arowoiya2025 | Victor Arowoiya; Ayodeji Oke; Melissa Chan; A | 2025 | Benefits of adopting digital twin technology (DTT) in the Nigerian con | PTJZHT69 | title-only | databases | digital twin | construction |  |
| 447 | [] | Vikas-Swarnakar2025 | Vikas Swarnakar; Abdelrahman E. E. Eltoukhy;  | 2025 | Unlocking circular economy potential in construction and demolition: a | E6PVVYV9 | abstract-grounded | databases | digital twin | construction | quality|artificial intell |
| 448 | [] | Vincenzo-Gattulli2022 | Vincenzo Gattulli; Fabio Franchi; Fabio Grazi | 2022 | Design and evaluation of 5G-based architecture supporting data-driven  | RWGL6LFJ | verified | databases | digital twins | structural|architecture|c | quality|monitoring|sensor |
| 449 | [] | Vu-Hong-Son-Pham2025 | Vu Hong Son Pham; Duy Hieu Pham; Thu Anh Nguy | 2025 | Optimizing construction site layouts with dynamic multi-objective meth | B6VK9YPI | abstract-grounded | databases | digital twins|bim|buildin | construction|building|sit | quality|risk|optimization |
| 450 | [] | Wadhwa-Khushi2023 | Wadhwa Khushi; Babbar Himanshi | 2023 | Digital Twin in the Motorized (Automotive / Vehicle) Industry | CC4EBG6T | abstract-grounded | databases | digital twin | construction | quality |
| 451 | [] | Wahib-A-AlAmmari2025 | Wahib A. Al‐Ammari; Ahmad K. Sleiti; Matthew  | 2025 | Development of Digital/Visual Twin for Real‐Time Leak Detection in Gas | SUN3MQZG | abstract-grounded | databases | digital twin | pipeline | safety|machine learning|m |
| 452 | [] | Wahib-Saif2026 | Wahib Saif; Omar Doukari; Mohamad Kassem | 2026 | Stakeholder-centric whole-lifecycle framework for guiding the developm | VKB7SFJD | abstract-grounded | databases | digital twins | construction | lifecycle |
| 453 | [1] | Wang2022 | Mengfei Wang, Vincent J. L. Gan, Zhen-Zhong H | 2022 | Digital twin-enabled built environment sensing and monitoring through  | BZQ3K5G8 | verified | other methods |  |  |  |
| 454 | [95] | Wang2026 | Y. Wang, A. Rezaei, S. Hicks | 2026 | Digital twins in the construction industry: A systematic review of cur | 8NJMGBZY | verified | other methods |  |  |  |
| 455 | [] | Wei-Hu2026 | Wei Hu; Cheng Chang; Han Wu; Kang Lai; Yiyu C | 2026 | Digital Twin-enabled failure prediction for indoor air quality: A CNN- | ZSDLWA6Q | title-only | databases | digital twin | indoor | quality |
| 456 | [] | Wei-Hu2026 | Wei Hu; Yifu Ou; Haiyi Liu; Peizhou Ni; Cheng | 2026 | Integrating digital twin technologies for maintenance 4.0 in the build | KCQYUWPC | abstract-grounded | databases | digital twin | building|asset management | predictive|monitoring|ene |
| 457 | [] | Wenbo-Hu2024 | Wenbo Hu; Weidong Wang; Xianhua Liu; Jun Peng | 2024 | Hybrid Pixel‐Level Crack Segmentation for Ballastless Track Slab Using | UTKQSJHY | verified | databases | digital twin | structural | deep learning|maintenance |
| 458 | [] | Wenjian-Yan2026 | Wenjian Yan | 2026 | The Application of Digital Twin Technology in the Revitalization of Ji | MYFVDNTV | verified | databases | digital twin | heritage | semantic|point cloud|regi |
| 459 | [] | Wenming-Su2025 | Wenming Su; Ying Huang; Ben Zhang; Jinqiao Ch | 2025 | Development of a digital twin-driven bridge construction safety monito | FATKDFH9 | abstract-grounded | databases | digital twin|digital mode | construction|bridge|struc | safety|monitoring|real-ti |
| 460 | [] | Wynand-Jacobus-Van-der-Merwe-Steyn2020 | Wynand Jacobus Van der Merwe Steyn | 2020 | Selected implications of a hyper-connected world on pavement engineeri | BWGXEZZS | verified | databases | digital twin | infrastructure|road|pavem | safety|sensor|lifecycle|a |
| 461 | [] | Xi-Hu2024 | Xi Hu; Rayan H. Assaad | 2024 | A BIM-enabled digital twin framework for real-time indoor environment  | YHGRDBQ8 | title-only | databases | digital twin|bim | indoor | monitoring|iot|real-time |
| 462 | [] | Xi-Zhu2021 | Xi Zhu; Tengfei Bao; Justin K. W. Yeoh; Ningx | 2021 | Enhancing dam safety evaluation using dam digital twins | KPX4YIZG | title-only | databases | digital twins | dam | safety |
| 463 | [] | Xiao-Li2024 | Xiao Li; Feng-Liang Zhang; Wei Xiang; Wei-Xia | 2024 | Structural health monitoring system based on digital twins and real-ti | D6PWWWF2 | title-only | databases | digital twins | structural | monitoring|structural hea |
| 464 | [] | Xiao-Lin2025 | Xiao Lin; Ziyang Guo; Xinxiang Jin; Hongling  | 2025 | Digital twin-enabled safety monitoring system for seamless worker-robo | J57WPA9F | title-only | databases | digital twin | construction | safety|monitoring |
| 465 | [] | Xiao-Tang2024 | Xiao Tang; Junlin Heng; Sakdirat Kaewunruen;  | 2024 | Artificial Intelligence-Powered Digital Twins for Sustainable and Resi | CS8TAVCA | abstract-grounded | databases | digital twins | civil engineering|buildin | safety|artificial intelli |
| 466 | [] | Xiaoming-Li2022 | Xiaoming Li; Jian Luo; Yulei Li; Weixi Wang;  | 2022 | Application of effective water-energy management based on digital twin | VC3ENQ7F | title-only | databases | digital twins | construction | energy |
| 467 | [] | Xiaoming-Yu2026 | Xiaoming Yu; Peng Wang; Jun Wang; Zhijun Chen | 2026 | A Digital Twin-Based Method for Degradation Parameter Identification o | RP6YVITN | verified | databases | digital twin | bridge | monitoring|optimization|r |
| 468 | [] | Xinran-Liu2022 | Xinran Liu; Ji Jiang | 2022 | Digital Twins by Physical Education Teaching Practice in Visual Sensin | 9ABPAPGS | verified | databases | digital twins | architecture | monitoring|sensor|simulat |
| 469 | [] | Xintong-Li2026 | Xintong Li; Yixuan Tang; Yiyuan Zhao | 2026 | Digital twin technology supporting urban public space renewal | 7VWWFV8M | verified | databases | digital twin | urban | quality|predictive|optimi |
| 470 | [] | Xiyuan-Zhang2025 | Xiyuan Zhang; Jiehao Zheng; Peixian Li; Yue Y | 2025 | A review of building digital twins: Framework and enabling technologie | 9UGJK475 | title-only | databases | digital twins | building |  |
| 471 | [34] | Xu2019 | S. Kaewunruen and Q. Xu | 2019 | Digital twin aided sustainability-based lifecycle management for railw | 8FF6EVCW | verified | other methods |  |  |  |
| 472 | [] | Xuan-Zhou2023 | Xuan Zhou; Claudio Sbarufatti; Marco Giglio;  | 2023 | A fuzzy-set-based joint distribution adaptation method for regression  | R8634BL6 | abstract-grounded | databases | digital twin | structural | simulation |
| 473 | [] | Xuebo-Li2026 | Xuebo Li | 2026 | Research on Digital Twin Construction and Immersive Teaching Applicati | IPS4WER5 | verified | databases | digital twin | construction|foundation|c | quality|semantic|point cl |
| 474 | [] | Yafeng-Wen2025 | Yafeng Wen | 2025 | Research on the intelligent construction of prefabricated building bas | 5URH8Q52 | abstract-grounded | databases | digital twin | construction|building|bui | safety|predictive|artific |
| 475 | [] | Yajian-Wang2022 | Yajian Wang; Pengpeng Li; Jianfeng Li | 2022 | The monitoring approaches and non-destructive testing technologies for | ZPALKBEZ | abstract-grounded | databases | digital twin | structural|pipeline|urban | monitoring|defect|inspect |
| 476 | [] | Yaman-Zendaki2024 | Yaman Zendaki; Ba‐Trung Cao; Janosch Staschei | 2024 | Coupling process controlling data and numerical simulation in mechanis | M3C4PPZP | abstract-grounded | databases | digital twin | construction|tunnel|site | quality|simulation |
| 477 | [] | Yan-Gao2023 | Yan Gao; Haijiang Li; Guanyu Xiong; Honghong  | 2023 | AIoT-informed digital twin communication for bridge maintenance | Z2XGMT6C | verified | databases | digital twin | bridge | safety|maintenance|fault |
| 478 | [] | Yang-He2024 | Yang He; Yulin Ding; Qing Zhu; Haoyu Wu; Yong | 2024 | Reliable simulation analysis for high-temperature inrush water hazard  | EVLJ5LED | abstract-grounded | databases | digital twin | construction|tunnel|struc | safety|risk|machine learn |
| 479 | [] | Yang-Su2025 | Yang Su; Weiwei Chen; Jiaxin Ling; Diran Yu | 2025 | Zero‐shot point cloud segmentation for hydro power plant components | T9XWG6H8 | abstract-grounded | databases | digital twin | construction|building|fou | semantic|decision support |
| 480 | [] | Yanhu-Han2025 | Yanhu Han; Mengqing Chen; Na Li; Man Ji; Xiao | 2025 | Digital twin in construction safety management: Recent advances, chall | 4MPYXPVA | title-only | databases | digital twin | construction | safety |
| 481 | [] | Yaoyi-Cai2026 | Yaoyi Cai | 2026 | Research on the Digital Narrative Expression Mechanism of Rural Intang | XGYSQPAG | abstract-grounded | databases | digital twin|digital twin | building|heritage | simulation|knowledge grap |
| 482 | [] | Yaqi-Zhang2025 | Yaqi Zhang; Chunyu Ji; Jing Ye; Heng Zou; Lan | 2025 | Architectural identity in smart city development: a multi-criteria stu | WX8IWGYJ | abstract-grounded | databases | digital twin|digital twin | infrastructure|architectu | decision support|uncertai |
| 483 | [] | Yawen-Zhang2025 | Yawen Zhang; Xianhua Cai | 2025 | Research on Digital Twin Model Construction Method for Smart Highway | GV2PJHXZ | abstract-grounded | databases | digital twin|digital twin | construction|infrastructu | safety|predictive|mainten |
| 484 | [] | Ye-Zhang2021 | Ye Zhang; A. Meina; Xuhao Lin; Kun Zhang; Zhe | 2021 | Digital Twin in Computational Design and Robotic Construction of Woode | ADRU9AUQ | verified | databases | digital twin|cyber-physic | construction|building|arc | real-time |
| 485 | [] | Yi-Liu2023 | Yi Liu; Jian-Min Zhang; Yan-Tao Min; Yantao Y | 2023 | A digital twin-based framework for simulation and monitoring analysis  | 2PL2FGA9 | abstract-grounded | databases | digital twin | construction|structural | safety|monitoring|sensor| |
| 486 | [] | Yifei-Ding2023 | Yifei Ding; Yuxin Zhang; Xinyan Huang | 2023 | Intelligent emergency digital twin system for monitoring building fire | FD9JA2LI | title-only | databases | digital twin | building | monitoring |
| 487 | [] | Yihao-Ren2025 | Yihao Ren; Pan Lu; Chengbo Ai; Amin Keramati | 2025 | Hybrid Local-Feature-Based Approach for Automated Rail Extraction from | 453QLA6G | abstract-grounded | databases | digital twins | infrastructure | quality|artificial intell |
| 488 | [] | Yonghui-An2025 | Yonghui An; Jianren Ning; Chuanchuan Hou; Jin | 2025 | Efficient low-collision UAV-based automated structural surface inspect | VJAS7MLD | title-only | databases | digital twin | structural | inspection |
| 489 | [] | Young-Je-Park2025 | Young Je Park; Won Young Choi; Hyunguk Choi;  | 2025 | Deciphering the microstructural complexities of compacted carbon fiber | BXLS4QET | abstract-grounded | databases | digital twin|digital twin | structure | artificial intelligence|c |
| 490 | [] | Yu-Chen2025 | Yu Chen; Chao Lin; Xianfeng Li; Shiori Kubo;  | 2025 | Automated dimension estimation of bridge components using semantic seg | 6PN66QDF | abstract-grounded | databases | digital-twin | infrastructure|bridge|str | safety|semantic|deep lear |
| 491 | [] | Yu-Gao2026 | Yu Gao; Tak Wing Yiu; Xuesong Shen; Vivian W. | 2026 | Large language models in smart construction: a systematic review of im | 62EPY8TW | abstract-grounded | databases | digital twins|building in | construction|building|fou | safety|semantic|artificia |
| 492 | [] | Yu-He2024 | Yu He; Yafei Ma; Ke Huang; Lei Wang; Jianren  | 2024 | Digital twin Bayesian entropy framework for corrosion fatigue life pre | EX97YC7E | title-only | databases | digital twin | bridge |  |
| 493 | [] | Yu-Xin2025 | Yu Xin; Yu-Sen Cai; Zuo-Cai Wang; Jun Li; Wei | 2025 | Hybrid‐Driven Digital Twin Framework for Time‐Variant Reliability Asse | H44DBEK3 | verified | databases | digital twin | construction|structural|s | simulation |
| 494 | [] | Yuandong-Pan2022 | Yuandong Pan; Alexander Braun; Ioannis Brilak | 2022 | Enriching geometric digital twins of buildings with small objects by f | P4H4EBXB | abstract-grounded | databases | digital twin|digital twin | buildings|structural|pipe | safety|semantic|monitorin |
| 495 | [] | Yuchong-Qian2024 | Yuchong Qian; Jiawei Leng; Kai Zhou; Yuxuan L | 2024 | How to measure and control indoor air quality based on intelligent dig | TKXPD8B7 | title-only | databases | digital twin | indoor | quality |
| 496 | [] | Yun-Zhou2021 | Yun Zhou; Xiao Wei; Ying Peng | 2021 | The Modelling of Digital Twins Technology in the Construction Process  | 9AWFV8WX | verified | databases | digital twins|bim|buildin | construction|building|bui | safety|risk|energy|real t |
| 497 | [] | Yuning-Cui2025 | Yuning Cui; Mingyu Liu; Xiongfei Su; Alois Kn | 2025 | Frequency-Prompted Image Restoration to Enhance Perception in Intellig | RHL8MDAU | abstract-grounded | databases | digital twins | infrastructure | quality |
| 498 | [] | Yunlong-Yao2026 | Yunlong Yao | 2026 | A scientometric review of building information modeling in project and | 8V5MNVZT | abstract-grounded | databases | digital twin|digital twin | construction|building|bri | iot|lifecycle|simulation| |
| 499 | [] | Yuwen-Chen2026 | Yuwen Chen | 2026 | An Evacuation Path Optimization Model Combining Digital Twins and Inte | 7T7GBRM8 | verified | databases | digital twin|digital twin | building|road | optimization|simulation|r |
| 500 | [] | Zaid-Osama2024 | Zaid Osama | 2024 | The digital twin framework: A roadmap to the development of user- cent | DUTW7LR6 | abstract-grounded | databases | digital twin|digital twin | construction|built enviro | real-time |
| 501 | [] | Zeyu-Pan2020 | Zeyu Pan; Jianyong Shi; Liu Jiang | 2020 | A Novel HDF-Based Data Compression and Integration Approach to Support | 49IHE87F | verified | databases | digital twin|bim|building | building|city |  |
| 502 | [] | Zezhou-Wu2022 | Zezhou Wu; Kaiwen Deng; Changhong Chen; Heng  | 2022 | STATUS QUO AND FUTURE TRENDS OF BIM-BASED COORDINATION RESEARCH: A CRI | Q24DWZKA | abstract-grounded | databases | bim|building information  | building |  |
| 503 | [16] | Zhang2013 | S. Zhang, J. Teizer, J.-K. Lee, C. M. Eastman | 2013 | Building Information Modeling (BIM) and Safety: Automatic Safety Check | 9X7JKF5U | verified | other methods |  |  |  |
| 504 | [24] | Zhang2015 | S. Zhang, J. Teizer, N. Pradhananga, and C. M | 2015 | Workforce location tracking to model, visualize and analyze workspace  | NIPJ4XUG | verified | other methods |  |  |  |
| 505 | [17] | Zhang2015 | S. Zhang, F. Boukamp, and J. Teizer | 2015 | Ontology-based semantic modeling of construction safety knowledge: Tow | GPNWB45Y | verified | other methods |  |  |  |
| 506 | [19] | Zhang2021 | Y. Pan and L. Zhang | 2021 | A BIM-data mining integrated digital twin framework for advanced proje | YGJSXUXV | verified | other methods |  |  |  |
| 507 | [78] | Zhang2023 | A. Zhang, J. Yang, F. Wang | 2023 | Application and enabling digital twin technologies in the operation an | S49XVYIT | verified | databases |  |  |  |
| 508 | [12] | Zhang2024 | Y. Zhang, L. Lu, X. Luo, and J. Pan | 2024 | Global BIM-point cloud registration and association for construction p | NHRTZV6T | verified | other methods |  |  |  |
| 509 | [] | Zhansheng-Liu2020 | Zhansheng Liu; Bai Wenyan; Xiuli Du; Anshan Z | 2020 | Digital Twin-based Safety Evaluation of Prestressed Steel Structure | PVJWRTJK | verified | databases | digital twin | structural|structure|stee | safety|risk assessment|ri |
| 510 | [] | Zhansheng-Liu2021 | Zhansheng Liu; Antong Jiang; Anshan Zhang; Ze | 2021 | Intelligent Prediction Method for Operation and Maintenance Safety of  | BJV3GR75 | verified | databases | digital twin | structural|structure|stee | safety|risk|monitoring|li |
| 511 | [] | Zhansheng-Liu2025 | Zhansheng Liu; Chengkuan Ji; Guoliang Shi; Ya | 2025 | Structural safety risk prediction method for terminal building steel r | 86DIMMR5 | abstract-grounded | databases | digital twin | construction|building|str | safety|risk|machine learn |
| 512 | [] | Zhansheng-Liu2025 | Zhansheng Liu; Weiyi Li; Qinwen Zhang; Meihao | 2025 | Research progress and trends of intelligent technology construction in | 7CKWEAWV | abstract-grounded | databases | digital twin|bim | construction|building|inf | safety|semantic|risk|iot |
| 513 | [] | Zhao-Liang2021 | Zhao Liang; Hong Zhang; Qian Wang; Haining Wa | 2021 | Digital-Twin-Based Evaluation of Nearly Zero-Energy Building for Exist | IUCH2B6D | verified | databases | digital twins|digital-twi | construction|building|bui | scan-to-bim|carbon|energy |
| 514 | [77] | Zhao2022 | J. Zhao, H. Feng, Q. Chen, B. García de Soto | 2022 | Developing a conceptual framework for the application of digital twin  | K9UNRWVK | verified | databases | digital twin | building | maintenance |
| 515 | [] | Zhao2023 | Yuxi Zhao, Zhenglin Chen, Fan Xue | 2023 | Blockchain-based decentralized digital twin for smart city resilience | QZPIVMLR | verified | other methods |  |  |  |
| 516 | [] | Zhe-Zheng2022 | Zhe Zheng; Wenjie Liao; Jiarui Lin; Yucheng Z | 2022 | Digital Twin‐Based Investigation of a Building Collapse Accident | WI99625X | verified | databases | digital twin | building|structural|site | simulation |
| 517 | [] | Zhen-Zhong-Hu2026 | Zhen-Zhong Hu; Yilin Li; Fu-Ping Gao; Jian-Mi | 2026 | Digital disaster prevention for ocean engineering: Current progress an | 5JMWQFV7 | abstract-grounded | databases | digital twins | structural | safety|risk|predictive|de |
| 518 | [] | Zhimian-Hao2022 | Zhimian Hao; Chonghuan Zhang; Alexei A. Lapki | 2022 | Efficient surrogates construction of chemical processes: Case studies  | 67SFNYY6 | abstract-grounded | databases | digital twins | construction|building | quality|carbon |
| 519 | [] | Zhipeng-Wang2023 | Zhipeng Wang; Yixuan Geng; Limin Jia; Yong Qi | 2023 | Self-Attentive Local Aggregation Learning With Prototype Guided Regula | QZG8MSP5 | abstract-grounded | databases | digital twins | construction|railway | semantic|deep learning|po |
| 520 | [] | Zhiyao-Tian2026 | Zhiyao Tian; Shunhua Zhou; Xianfei Yin; Qiyu  | 2026 | A Bayesian pressure‑inversion–driven method for establishing mechanica | S78F4AQL | abstract-grounded | databases | digital twins | tunnel |  |
| 521 | [] | Zhong-Cheng-Zeng2025 | Zhong-Cheng Zeng; You-Lin Xu; Yong-Ding Tian; | 2025 | Digital twin-empowered performance evaluation of cracked reinforced co | 2BVWZLUT | abstract-grounded | databases | digital twin | structural|concrete | quality|point cloud|optim |
| 522 | [] | Zhonghua-Xu2021 | Zhonghua Xu; Changguo Dai; Jing Wang; Lejun L | 2021 | Construction and Application of Recognition Model for Black-Odorous Wa | KBBEP9ST | abstract-grounded | databases | digital twins | construction|civil engine | quality|neural network |
| 523 | [] | Zhongzhi-Xie2026 | Zhongzhi Xie | 2026 | The construction and implementation path of digital factory under the  | RLYUVRRI | abstract-grounded | databases | digital twin | construction|architecture | energy|automation|optimiz |
| 524 | [22] | Zhou2012 | W. Zhou, J. Whyte, and R. Sacks | 2012 | Construction safety and digital design: A review, | XDWWGWWX | verified | other methods |  |  |  |
| 525 | [] | Zhuang-Tan2025 | Zhuang Tan; Hongye Gou; Wenhao Li; Ye Peng; J | 2025 | Digital twin-based cyber-physical system for intelligent monitoring an | CDXJ6P3I | title-only | databases | digital twin|cyber-physic | railway | predictive|monitoring |
| 526 | [] | Zhuang-Tan2026 | Zhuang Tan; Wenhao Li; Hongye Gou; Xin Huang; | 2026 | Digital twin-based multi-objective parameter identification for a cabl | ITVK3BS9 | title-only | databases | digital twin | bridge |  |

> **Total:** 526 notes. databases = 432, other methods = 94.