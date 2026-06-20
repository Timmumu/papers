# LR_Matrix — PRISMA 2020 Full Reconciliation (Round 2)
## Cognitive Full-Lifecycle Digital Twin Framework for the AECO Industry

> **Companion document to LR_cc.md (Round 2)**
> Round-2 reconciliation of the **748 records** identified from the Lens.org search
> (single source), screened down to **424 records retained for full-text review**.
> **Last updated:** 15 Jun 2026 (round-2 screening completion + full-text enrichment in progress)
>
> ### Status Tags (Round 2)
> | Emoji | PRISMA Stage | Count |
> |:---:|---|:---:|
> | 🟢 | **RETAINED** for full-text review (→ atomic notes in `01_source/`) | 424 |
> | 🔴 | **EXCLUDED** at title/abstract screening | 320 |
> | ⚫ | **DUPLICATES** removed | 4 |
> | ⏳ | **FULL-TEXT SYNTHESIS** (deep notes + qualitative inclusion) | in progress |
>
> **✅ Auditable provenance.** Unlike round 1, every round-2 count below is reconstructable
> from workspace artefacts: the Lens.org export [2round748.csv](2round748.csv) (748 records),
> the screening decision log, and the retained set
> [retained_for_fulltext.csv](retained_for_fulltext.csv) (424 records). The Boolean query and
> filters are documented in [Lens filter condition.md](Lens%20filter%20condition.md).
>
> **Scope note.** Sections 1 and the *Round-2 Screening Summary* below are the current,
> auditable round-2 record. **Sections 2–8 are the Round-1 qualitative-synthesis corpus
> (412 records → 69 included), carried forward unchanged** as the analytical baseline; the
> full-text synthesis of the 424 round-2 records is being built incrementally (Phase B) and
> will supersede those tables as deep notes are completed.
>
> ### Maturity Codes
> ML1 = Digital Shadow (unidirectional) · ML2 = Cyber-Physical Interface (bidirectional, human-mediated) · ML3 = Cognitive/Autonomous

---


## 1. PRISMA 2020 Flow Reconciliation (Round 2 — auditable)

Single-source search executed on **Lens.org**. Query, year window (2015–2026),
publication-type, external-ID (DOI) and subject filters are documented verbatim in
[Lens filter condition.md](Lens%20filter%20condition.md).

| Stage              | Description                                                  |       n | Cumulative |
| ------------------ | ------------------------------------------------------------ | ------: | ---------: |
| **Identification** | Records identified — Lens.org (single database)              |     748 |        748 |
| **Deduplication**  | Duplicate records removed                                    |      −4 |        744 |
| **Screening**      | Records screened on title & abstract (3-vector criteria)     |     744 |        744 |
|                    | Records excluded at screening                                |    −320 |        424 |
| **Retained**       | **Records retained for full-text review** (→ `01_source/`)   | **424** |    **424** |
| **Eligibility**    | Full-text reports assessed for eligibility                   |       ⏳ |          — |
| **Included**       | Studies included in qualitative synthesis                    |       ⏳ |          — |

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

> ⬇️ **Sections 2–8 below are the Round-1 carried-forward synthesis corpus** (412 records →
> 69 included). They are retained as the analytical baseline and verification worktable;
> the round-2 full-text synthesis (Phase B) will replace them as deep notes are completed.

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


## 8. Master Reference Index — PRISMA Status & Source-File Verification Map

Complete index of every reference appearing in LR_cc.md, cross-checked against the
atomic-note corpus (`01_source/`, `02_removed/`). This is a **verification worktable**:
each row links the reference number to its backing note file, Zotero key, and
verification status, and surfaces any integrity discrepancy for manual reconciliation.

> **⚠️ Provenance caveat.** The PRISMA flow counts (412 / 97 / 315 / 203 / 112 / 6 /
> 106 / 37 / 69) are **illustrative narrative figures** taken from LR_cc.md §2.3. They
> are **arithmetically self-consistent but not independently reconstructable** from any
> artefact in the workspace — there is no database export, deduplication log, or
> screening spreadsheet. Treat them as placeholders pending a real search-export audit.

### Column legend

- **In 69?** — counted in the corrected qualitative-synthesis corpus (✓ = yes, ✗ = no).
- **Verif** — Zotero status from note frontmatter: ✅ verified · ◐ metadata-only · ⚠ unverifiable · ✗ no note · n/a standard/non-Zotero.
- **Flag** — `—` clean; otherwise an integrity issue needing reconciliation.

### 8.1 Included synthesis corpus + numbered references [1]–[100], [TBD]

| Ref | Authors (Year) | Short Title | Status | In 69? | Theme | Backing Note | Zotero | Verif | Flag |
|:---:|---|---|:---:|:---:|---|---|---|:---:|---|
| [1] | Wang et al. (2022) | DT-enabled built-env sensing (SensorML) | 🟢 | ✓ | BIM-to-DT | [Wang2022](01_source/Wang2022.md) | BZQ3K5G8 | ✅ | — |
| [2] | Akhavian et al. (2025) | BIM2RDT agentic AI safety | 🟢 | ✓ | BIM-to-DT | [Akhavian2025](01_source/Akhavian2025.md) | 7REV8TWX | ✅ | Preprint (non-peer-reviewed) |
| [3] | Glatt et al. (2021) | DT of material flows | 🟢 | ✓ | Perception | [Glatt2021](01_source/Glatt2021.md) | HK9GVDQT | ✅ | — |
| [4] | Hamel et al. (2024) | PMI-DT predictive modeling | 🟢 | ✓ | Perception | [Hamel2024](01_source/Hamel2024.md) | 4B9RB46D | ✅ | Preprint (non-peer-reviewed) |
| [5] | Boje et al. (2020) | Semantic Construction DT | 🟢 | ✓ | Semantic | [Boje2020](01_source/Boje2020.md) | 6RG2MC52 | ✅ | — |
| [6] | Deng et al. (2021) | From BIM to DTs (AEC-FM) | 🟢 | ✓ | BIM-to-DT | [Deng2021](01_source/Deng2021.md) | 739GLUD3 | ✅ | — |
| [7] | Jiang et al. (2021) | DT implementations in civil eng | 🟢 | ✓ | BIM-to-DT | [Jiang2021](01_source/Jiang2021.md) | LD8ZIQKW | ✅ | — |
| [8] | Tang et al. (2019) | BIM & IoT integration review | 🟢 | ✓ | BIM-to-DT | [Tang2019](01_source/Tang2019.md) | 4ZA4SRVJ | ✅ | — |
| [9] | Lu, Xie et al. (2020) | DT anomaly detection O&M | 🟢 | ✓ | Predictive | [Lu&Xie2020](01_source/Lu&Xie2020.md) | PTY562CM | ✅ | — |
| [10] | Theiler et al. (2018) | IFC Monitor for SHM | 🟢 | ✓ | Semantic | [Theiler2018](01_source/Theiler2018.md) | H98THTQ4 | ✅ | — |
| [11] | Spinner & Degani (2024) | Online as-built BIM update | 🟢 | ✓ | BIM-to-DT | [Spinner2024](01_source/Spinner2024.md) | ULJGBQZ6 | ✅ | Dup note [Degani2024](01_source/Degani2024.md) shares key — merge |
| [12] | Zhang et al. (2024) | Global BIM–point-cloud registration | 🟢 | ✓ | Perception | [Zhang2024](01_source/Zhang2024.md) | NHRTZV6T | ✅ | — |
| [13] | Lee et al. (2025) | Agentic built environments | 🟢 | ✓ | Predictive | [Lee2025](01_source/Lee2025.md) | RQHBTQZ7 | ✅ | — |
| [14] | Hu & Gan (2025) | Semantic navigation, robotic insp | 🟢 | ✓ | Perception | [Gan2025](01_source/Gan2025.md) | EVBNP6SE | ✅ | — |
| [15] | Qiao et al. (2025) | Global LiDAR registration | 🟢 | ✓ | Perception | [Qiao2025-15](01_source/Qiao2025-15.md) | AXBTD3BN | ✅ | — |
| [16] | Zhang et al. (2013) | BIM automatic safety checking | 🟢 | ✓ | DfS | [Zhang2013](01_source/Zhang2013.md) | 9X7JKF5U | ✅ | — |
| [17] | Zhang, Boukamp & Teizer (2015) | Ontology-based JHA | 🟢 | ✓ | Semantic | [Zhang2015](01_source/Zhang2015.md) | GPNWB45Y | ✅ | — |
| [18] | Broo et al. (2022) | Smart infrastructure DT design | 🟢 | ✓ | Lifecycle | [Broo2022](01_source/Broo2022.md) | 6X33TIE6 | ✅ | — |
| [19] | Pan & Zhang (2021) | BIM-data-mining DT framework | 🟢 | ✓ | Predictive | [Pan&Zhang2021](01_source/Pan&Zhang2021.md) | YGJSXUXV | ✅ | Dup note [Zhang2021](01_source/Zhang2021.md) shares key — merge |
| [20] | Hossain et al. (2018) | DfS knowledge library | 🟢 | ✓ | Semantic | [Hossain2018](01_source/Hossain2018.md) | 7JMAKZYT | ✅ | — |
| [21] | Martinez-Aires et al. (2018) | BIM & safety mgmt review | 🟢 | ✓ | DfS | [Martinez-Aires2018](01_source/Martinez-Aires2018.md) | TF4RA96S | ✅ | — |
| [22] | Zhou, Whyte & Sacks (2012) | Safety & digital design review | 🟢 | ✓ | DfS | [Zhou2012](01_source/Zhou2012.md) | XDWWGWWX | ✅ | — |
| [23] | Qi et al. (2014) | BIM to prevent worker falls | 🟢 | ✓ | DfS | [Qi2014](01_source/Qi2014.md) | QW2EQIJ5 | ✅ | — |
| [24] | Zhang et al. (2015) | Workforce location tracking | 🟢 | ✓ | DfS | [Zhang2015-24](01_source/Zhang2015-24.md) | NIPJ4XUG | ✅ | — |
| [25] | Jiang et al. (2022) | DT real-time sync, precast | 🟢 | ✓ | BIM-to-DT | [Jiang2022](01_source/Jiang2022.md) | BEXVG4GB | ✅ | — |
| [26] | Page et al. (2021) | PRISMA 2020 statement | 🔵 | ✗ | Methodology | [Page2021](01_source/Page2021.md) | L6IE92GF | ✅ | — |
| [27] | Kitchenham & Charters (2007) | SLR guidelines | 🔵 | ✗ | Methodology | [Charters2007](02_removed/Charters2007.md) | — | ⚠ | **Conflict:** actively cited yet note sits in `02_removed/` |
| [28] | Kritzinger et al. (2018) | DT categorical review | 🔵 | ✗ | Background | [Kritzinger2018](01_source/Kritzinger2018.md) | J4XB34RN | ✅ | — |
| [29] | Fuller et al. (2020) | DT enabling technologies | 🔵 | ✗ | Background | [Fuller2020](01_source/Fuller2020.md) | SSR5IGBW | ✅ | — |
| [30] | Tao et al. (2019) | DT in industry: state-of-the-art | 🔵 | ✗ | Background | [Tao2019](01_source/Tao2019.md) | MERRUE6E | ✅ | — |
| [31] | Uhlemann et al. (2017) | DT realizing CPS for I4.0 | 🔵 | ✗ | Background | [Uhlemann2017](01_source/Uhlemann2017.md) | 7XF73XIE | ✅ | — |
| [32] | Sacks et al. (2020) | Construction with DT info systems | 🟢 | ✓ | Perception | [Sacks2020](01_source/Sacks2020.md) | FBV29DAQ | ✅ | — |
| [33] | Opoku et al. (2021) | DT application in construction (review) | 🟢 | ✓ | BIM-to-DT | [Opoku2021](01_source/Opoku2021.md) | LUGQBL7W | ✅ | [Chen2021](01_source/Chen2021.md) frontmatter mis-tags this ref (→ [80]) |
| [34] | Kaewunruen & Xu (2019) | DT-aided railway turnout | 🟢 | ✓ | BIM-to-DT | [Xu2019](01_source/Xu2019.md) | 8FF6EVCW | ✅ | — |
| [35] | Ayyalasomayajula et al. (2022) | (removed) | ❌ | ✗ | Removed | [Ayyalasomayajula2022](02_removed/Ayyalasomayajula2022.md) | — | ⚠ | Unverifiable DOI |
| [36] | Sepasgozar (2020) | DT & web gaming for ed | 🟢 | ✓ | BIM-to-DT | [Sepasgozar2020](01_source/Sepasgozar2020.md) | 2I3BUC9T | ✅ | — |
| [37] | Teizer et al. (2010) | Proximity safety alert system | 🟢 | ✓ | Perception | [Teizer2010](01_source/Teizer2010.md) | MVVXZSXY | ✅ | — |
| [38] | Teo, Ling & Chong (2005) | PM safety mgmt framework | 🟢 | ✓ | Perception | [Teo2005](01_source/Teo2005.md) | QGV65BAU | ✅ | — |
| [39] | Whyte & Hartmann (2017) | Digitizing building information | 🟢 | ✓ | Semantic | [Hartmann2017](01_source/Hartmann2017.md) | PITWT7WC | ✅ | — |
| [40] | Holmstrom et al. (2010) | Rapid mfg in spare-parts chain | 🟢 | ✓ | BIM-to-DT | [Holmstrom2010](01_source/Holmstrom2010.md) | WBZTQ4RJ | ✅ | — |
| [41] | Olofsson et al. (2010) | (removed) | ❌ | ✗ | Removed | [Olofsson2010](02_removed/Olofsson2010.md) | — | ⚠ | Superseded by [32] |
| [42] | Borrmann et al. (2018) | (removed) | ❌ | ✗ | Removed | _(no note)_ | — | ✗ | Textbook, not primary |
| [43] | Davies & Harty (2013) | Implementing 'Site BIM' | 🟢 | ✓ | Semantic | [Harty2013](01_source/Harty2013.md) | D4JSMC88 | ✅ | — |
| [44] | Love & Matthews (2021) | Benefits mgmt for digital tech | 🟢 | ✓ | Semantic | [Matthews2021](01_source/Matthews2021.md) | S9KGUJLS | ✅ | [Ruppert2018](01_source/Ruppert2018.md) mis-tags this ref (is dup of [82]) |
| [45] | Li (2021) | (removed) | ❌ | ✗ | Removed | [Li2021](02_removed/Li2021.md) | UY7CT3JA | ✅ | Replaced by [97],[98] |
| [46] | Spearpoint & Burch (2012) | (removed) | ❌ | ✗ | Removed | [Burch2012](02_removed/Burch2012.md) | — | ⚠ | No DT context |
| [47] | Saltelli et al. (2008) | (removed) | ❌ | ✗ | Removed | [Saltelli2008](02_removed/Saltelli2008.md) | — | ◐ | **Conflict:** still listed/cited in LR_cc.md §5.4 |
| [48] | Bedford & Cooke (2001) | (removed) | ❌ | ✗ | Removed | _(no note)_ | — | ✗ | Textbook |
| [49] | Sacks, Rozenfeld & Rosenfeld (2009) | Spatial-temporal hazard exposure | 🟢 | ✓ | Perception | [Sacks2009](01_source/Sacks2009.md) | RL2W6VYI | ✅ | — |
| [50] | Eastman et al. (2018) | (removed) | ❌ | ✗ | Removed | _(no note)_ | — | ✗ | Textbook (BIM Handbook) |
| [51] | Akinci, Fischer & Kunz (2002) | Automated work-space generation | 🟢 | ✓ | BIM-to-DT | [Akinci2002](01_source/Akinci2002.md) | SHAKQM77 | ✅ | — |
| [52] | Zhang & El-Gohary (2016) | Semantic NLP for compliance | 🟢 | ✓ | Semantic | [El-Gohary2016](01_source/El-Gohary2016.md) | VDR5RZP3 | ✅ | Frontmatter wrongly tags file `[63]` → should be `[52]` |
| [53] | Schleich et al. (2017) | Shaping the DT | 🟢 | ✓ | Perception | [Schleich2017](01_source/Schleich2017.md) | MNQ7TJ9H | ✅ | — |
| [54] | Rasheed, San & Kvamsdal (2020) | DT: values, challenges, enablers | 🟢 | ✓ | Perception | [Rasheed2020](01_source/Rasheed2020.md) | MKZ3HU7D | ✅ | Dup note [Rasheed1980](01_source/Rasheed1980.md) shares key — merge |
| [55] | Glaessgen & Stargel (2012) | DT paradigm (NASA/USAF) | 🟢 | ✓ | BIM-to-DT | [Glaessgen2012](01_source/Glaessgen2012.md) | 8B7R5BZU | ✅ | Dup note [Stargel2012](01_source/Stargel2012.md) — same paper/key |
| [56] | Grieves & Vickers (2017) | DT mitigating emergent behavior | 🟢 | ✓ | BIM-to-DT | [Grieves2026](01_source/Grieves2026.md) | 83PUTURG | ✅ | Dup note [Vickers2017](01_source/Vickers2017.md) (key UXYJS9VB); citekey year wrong |
| [57] | Lu et al. (2020) | DT smart-mfg reference model | 🟢 | ✓ | BIM-to-DT | [Lu2020](01_source/Lu2020.md) | 6VU4VXU4 | ✅ | — |
| [58] | Tao & Zhang (2017) | DT shop-floor | 🟢 | ✓ | BIM-to-DT | [TaoZhang2017](01_source/TaoZhang2017.md) | 2E3WDWM9 | ✅ | — |
| [59] | Liu et al. (2022) | (removed) | ❌ | ✗ | Removed | [Liu2022](02_removed/Liu2022.md) | — | ⚠ | Unverifiable overlap w/ [84] |
| [60] | Bolpagni et al. (2022) | (removed) | ❌ | ✗ | Removed | [Bolpagni2022](02_removed/Bolpagni2022.md) | — | ⚠ | Replaced by [96] |
| [61] | ISO 23247-1 (2021) | DT framework for mfg | 🔵 | ✗ | Standard | [23247-12021](01_source/23247-12021.md) | — | n/a | — |
| [62] | ISO 19650-1 (2018) | BIM information management | 🔵 | ✗ | Standard | [19650-12018](01_source/19650-12018.md) | — | n/a | — |
| [63] | NIST (2023) | (removed) | ❌ | ✗ | Removed | [NIST2023](02_removed/NIST2023.md) | — | ◐ | **Conflict:** [El-Gohary2016](01_source/El-Gohary2016.md) also tagged `[63]` |
| [64] | Kahneman, Sibony & Sunstein (2021) | Noise: a flaw in human judgment | 🟢 | ✓ | Semantic | _(no note)_ | — | ✗ | **Missing backing note** |
| [65] | Love et al. (2014) | Benefits realization BIM | 🟢 | ✓ | Semantic | [Love2014](01_source/Love2014.md) | C26978RE | ✅ | — |
| [66] | Tixier et al. (2016) | NLP safety-precursor extraction | 🟢 | ✓ | Semantic | [Tixier2016](01_source/Tixier2016.md) | X5U62SNQ | ✅ | — |
| [67] | Choi, Yun & Kim (2021) | BIM + sensor + ML for risk | 🟢 | ✓ | DfS | [Choi2021](01_source/Choi2021.md) | VSGTL8SJ | ✅ | Verify author (LR_Matrix flags "Langroodi" mismatch) |
| [68] | Singh & Akinci (2021) | (removed) | ❌ | ✗ | Removed | [Akinci2021](02_removed/Akinci2021.md) | X8SNRHBX | ✅ | Duplicate content |
| [69] | Fang et al. (2022) | (removed) | ❌ | ✗ | Removed | [Fang2022-69](02_removed/Fang2022-69.md) | GWQU2ZRA | ✅ | Overlap w/ [67],[93] |
| [70] | Lee, Peña-Mora & Park (2006) | Dynamic planning & control | 🟢 | ✓ | Perception | _(no note)_ | — | ✗ | **Missing backing note** |
| [71] | Jones et al. (2020) | Characterising the DT (SLR) | 🟢 | ✓ | Semantic | [Jones2020](01_source/Jones2020.md) | 9FNSJ6UJ | ✅ | — |
| [72] | Sepasgozar (2021) | DT vs Digital Shadow | 🟢 | ✓ | Semantic | [Sepasgozar2021](01_source/Sepasgozar2021.md) | NT452J52 | ✅ | — |
| [73] | Ozturk (2021) | DT research in AECO-FM | 🟢 | ✓ | Semantic | [Ozturk2021](01_source/Ozturk2021.md) | BLMII5EA | ✅ | — |
| [74] | Omrany et al. (2023) | DTs in construction review | 🟢 | ✓ | BIM-to-DT | [Omrany2023](01_source/Omrany2023.md) | CW78JTWI | ✅ | — |
| [75] | Liu, Zhang & Wang (2020) | Indoor safety mgmt via DT | 🟢 | ✓ | DfS | [Liu2020](01_source/Liu2020.md) | VI3RUWW4 | ✅ | — |
| [76] | Liu et al. (2021) | DT safety-risk coupling, hoisting | 🟢 | ✓ | DfS | [Liu2021](01_source/Liu2021.md) | CDL7QW8N | ✅ | Dup note [Liu&Meng2021](01_source/Liu&Meng2021.md) shares key — merge |
| [77] | Zhao et al. (2022) | Conceptual DT O&M framework | 🟢 | ✓ | Predictive | [Zhao2022](01_source/Zhao2022.md) | K9UNRWVK | ✅ | Frontmatter wrongly tags file `[82]` → should be `[77]` |
| [78] | Zhang, Yang & Wang (2023) | DT technologies in O&M (review) | 🟢 | ✓ | Predictive | [Zhang2023](01_source/Zhang2023.md) | S49XVYIT | ✅ | Frontmatter wrongly tags file `[83]` → should be `[78]` |
| [79] | Shahzad et al. (2022) | DTs in built env: characteristics | 🟢 | ✓ | Predictive | [Shahzad2022](01_source/Shahzad2022.md) | IX4N6UJ9 | ✅ | — |
| [80] | Chen et al. (2021) | Gemini-Principles DT maturity | 🟢 | ✓ | Predictive | [Chen2021](01_source/Chen2021.md) | UG9GN8KS | ✅ | Frontmatter wrongly tags file `[33]` → should be `[80]` |
| [81] | Jiang et al. (2022) | DT modular integrated construction | 🟢 | ✓ | DfS | [Jiang2022-81](01_source/Jiang2022-81.md) | DXRTQ89R | ✅ | — |
| [82] | Ruppert & Abonyi (2020) | RTLS into digital twins | 🟢 | ✓ | DfS | [Ruppert2020](01_source/Ruppert2020.md) | IJUPSPJB | ✅ | [Zhao2022](01_source/Zhao2022.md) also tagged `[82]`; [Ruppert2018](01_source/Ruppert2018.md) dup |
| [83] | Qi et al. (2021) | Enabling technologies & tools for DT | 🟢 | ✓ | Lifecycle | [Qi2021](01_source/Qi2021.md) | FFM3DXDC | ✅ | [Zhang2023](01_source/Zhang2023.md) also tagged `[83]` (→ [78]) |
| [84] | Liu et al. (2021) | Review of DT: concepts & tech | 🟢 | ✓ | Lifecycle | [Liu2021b](01_source/Liu2021b.md) | 2P9ECH2E | ✅ | — |
| [85] | Greif, Stein & Flath (2020) | DTs for site logistics | 🟢 | ✓ | DfS | [Greif2020](01_source/Greif2020.md) | 3MAJ4UNU | ✅ | — |
| [86] | Hakimi et al. (2024) | DT smart-FM bibliometric | 🟢 | ✓ | Predictive | [Hakimi2024](01_source/Hakimi2024.md) | 9EYC52IG | ✅ | — |
| [87] | Hosamo et al. (2022) | DT predictive maintenance, AHU | 🟢 | ✓ | Predictive | [Hosamo1988](01_source/Hosamo1988.md) (citekey Hosamo2022b) | ID2GIXE3 | ✅ | Filename year wrong (1988→2022); unassigned [Hosamo2022](01_source/Hosamo2022.md) also exists |
| [88] | Lee et al. (2021) | DT + blockchain for construction | 🟢 | ✓ | Lifecycle | [Lee2021](01_source/Lee2021.md) | JQBEN9IR | ✅ | — |
| [89] | Singh et al. (2021) | Digital Twin: origin to future | 🟢 | ✓ | Lifecycle | [Singh2021](01_source/Singh2021.md) | R2NLMGZ8 | ✅ | — |
| [90] | Lu et al. (2020) | DT smart mfg (**duplicate of [57]**) | ⚫ | ✗ | _(was BIM-to-DT)_ | [Lu2020-90](01_source/Lu2020-90.md) | 6VU4VXU4 | ✅ | **True duplicate of [57]** (same key) — removed from synthesis (70→69) |
| [91] | Tao et al. (2019) | DTs & CPS toward Smart Mfg | 🟢 | ✓ | Lifecycle | _(no distinct note)_ | — | ✗ | No dedicated note ([Tao2019](01_source/Tao2019.md) = [30]); verify possible conflation |
| [92] | Martínez-Rojas et al. (2025) | BIM real-time fall prevention | 🔵 | ✗ | Post-SLR Safety | [Pereira2025](01_source/Pereira2025.md) | EWGI4UA4 | ✅ | Verify citekey vs author |
| [93] | Liu et al. (2023) | BIM + CV for workforce safety | 🔵 | ✗ | Post-SLR Safety | [Kulinan2024](01_source/Kulinan2024.md) | P52VFZEH | ✅ | Verify citekey vs author/year |
| [94] | Chen et al. (2025) | VLMs for construction safety | 🔵 | ✗ | Post-SLR VLM | [Kim2025](01_source/Kim2025.md) | R3P4YWR6 | ✅ | Verify citekey vs author |
| [95] | Omrany et al. (2026) | DTs in construction (2024– review) | 🔵 | ✗ | Post-SLR review | [Wang2026](01_source/Wang2026.md) | 8NJMGBZY | ✅ | Verify: note = Wang2026, matrix author = Omrany2026 |
| [96] | Bolpagni et al. (2025) | Challenges in asset mgmt & DTs | 🔵 | ✗ | Post-SLR Asset | [Bolpagni2025](01_source/Bolpagni2025.md) | KSJE5VBV | ✅ | — |
| [97] | Abdar et al. (2021) | UQ in deep learning review | 🔵 | ✗ | Post-SLR UQ | [Abdar2021](01_source/Abdar2021.md) | HWPU8ZWP | ✅ | — |
| [98] | Grenyer et al. (2021) | Multivariate UQ review | 🔵 | ✗ | Post-SLR UQ | [Grenyer2021](01_source/Grenyer2021.md) | NLAZ35NI | ✅ | — |
| [99] | Lü et al. (2025) | UQ for frequency responses | 🔵 | ✗ | Post-SLR UQ | [Fu2026](01_source/Fu2026.md) | K3PFBG7P | ✅ | Verify: note = Fu2026, matrix author = Lü2025 |
| [100] | Fung et al. (2010) | Risk-assessment model | 🔵 | ✗ | Post-SLR Risk | [Fung2010](01_source/Fung2010.md) | WG9ID8KK | ✅ | — |
| [TBD-A] | AlOmari et al. (2026) | Cross-domain predictive analytics | 🔵 | ✗ | Post-SLR | [AlOmari2026](01_source/AlOmari2026.md) | IENSAMVE | ✅ | `ref` blank; file has encoding mojibake |
| [TBD-B] | Pragna et al. (2026) | Forward forecasting in CPS | 🔵 | ✗ | Post-SLR | [Pragna2026](01_source/Pragna2026.md) | WHW4PTNF | ✅ | `ref` blank |

### 8.2 Aggregate PRISMA buckets (count-only)

| Cohort | Status | PRISMA Stage | See |
|:---:|:---:|---|---|
| E1–E37 | 🔴 | Excluded at full-text eligibility | Section 3 |
| NR1–NR6 | ⚪ | Not retrieved | Section 4 |
| (n≈203) | 🟡 | Excluded at title/abstract screening | Section 5 |
| (n=97) | ⚫ | Duplicates removed (96 + folded [90]) | Section 6 |

### 8.3 Orphan / unassigned notes (in `01_source/` but outside the [1]–[100] scheme)

These notes carry an empty `ref:` field and are **not** mapped to any numbered reference.
They require triage: assign a ref, move to `02_removed/`, or confirm as background-only.

| Note | Zotero | Likely role / action |
|---|---|---|
| [Hosamo2022](01_source/Hosamo2022.md) | 3QSAUVYC | DT review (AEC-FM) — candidate for E1 or supplementary |
| [Lu&Parlikad2020](01_source/Lu&Parlikad2020.md) | 7ANHKRIU | Cambridge campus DT — candidate for E3/E5 |
| [Teisserenc2021](01_source/Teisserenc2021.md) | EN7S2R5T | Blockchain DT governance — candidate for E9 |
| [Zhao2023](01_source/Zhao2023.md) | QZPIVMLR | Blockchain 3.0 AECO — candidate for E10 |
| [Sun2023](01_source/Sun2023.md) | RA62TL5J | DT in healthcare — candidate for E19 |
| [Tao2018](01_source/Tao2018.md) | FDTN2LDT | DT product design/mfg — candidate for E23 |
| [Adibi2024](01_source/Adibi2024.md) | HHRE3QTR | Unmapped — triage |
| [Götz2022](01_source/Götz2022.md) | 56AMFECQ | Unmapped — triage |
| [Machado2023](01_source/Machado2023.md) | PTD7AVWZ | Unmapped — triage |
| [Pome2023](01_source/Pome2023.md) | NURYJTQW | Unmapped — triage |
| [MinQi2019](01_source/MinQi2019.md) | WSF2RF5M | Unmapped — triage |
| [RajratnaKharat2018](01_source/RajratnaKharat2018.md) | 9SMJBZXV | Unmapped — triage |
| [Radford2021](01_source/Radford2021.md) | WMDJY52E | Unmapped (GPT/LLM) — likely out-of-domain |

### 8.4 Integrity flags requiring reconciliation

1. **Frontmatter `ref` mis-tags (4 files).** [El-Gohary2016](01_source/El-Gohary2016.md) `[63]→[52]`; [Chen2021](01_source/Chen2021.md) `[33]→[80]`; [Zhao2022](01_source/Zhao2022.md) `[82]→[77]`; [Zhang2023](01_source/Zhang2023.md) `[83]→[78]`. The correct holders ([33] Opoku2021, [82] Ruppert2020, [83] Qi2021) exist separately, so each ref still resolves — but the note frontmatter must be fixed.
2. **Ref [63] double-claim.** Both [NIST2023](02_removed/NIST2023.md) (removed) and [El-Gohary2016](01_source/El-Gohary2016.md) carry `[63]`.
3. **Missing backing notes (2 included refs).** [64] Kahneman *Noise* and [70] Lee, Peña-Mora & Park (2006) have no note in `01_source/`.
4. **[91] has no distinct note.** Only [Tao2019](01_source/Tao2019.md) (= [30]) and [Tao2018](01_source/Tao2018.md) exist; confirm whether [91] is a separate paper or a conflation.
5. **File-level duplicate notes (same Zotero key, one ref).** [11] Degani2024/Spinner2024 · [19] Zhang2021/Pan&Zhang2021 · [54] Rasheed2020/Rasheed1980 · [55] Glaessgen2012/Stargel2012 · [56] Grieves2026/Vickers2017 · [76] Liu2021/Liu&Meng2021 · [82] Ruppert2020/Ruppert2018. Merge each pair.
6. **Removed-but-cited.** [27] Kitchenham & Charters and [47] Saltelli sit in `02_removed/` yet remain cited in LR_cc.md — resolve their status.
7. **Citekey ↔ author mismatches (supplementary).** [92] Pereira2025, [93] Kulinan2024, [94] Kim2025, [95] Wang2026, [99] Fu2026 — note filenames do not match the author/year printed in LR_cc.md. Verify which is authoritative.
8. **[87] filename anomaly.** Note saved as `Hosamo1988.md` (citekey `Hosamo2022b`), real year 2022.
9. **[TBD-A] encoding.** [AlOmari2026](01_source/AlOmari2026.md) contains mojibake in author/CJK fields.

### 8.5 Cross-file action list (NOT auto-applied — for your sign-off)

| # | File | Action needed |
|:---:|---|---|
| C1 | [LR_cc.md](LR_cc.md) §2.3 vs §2.4 | Resolve contradiction: "107 assessed → 37 excluded → 70" vs "89 assessed → 19 removed → 70". |
| C2 | [LR_cc.md](LR_cc.md) §8 | Decide [47] Saltelli & [63] NIST status (currently listed/cited but moved to `02_removed/`). |
| C3 | [LR_cc.md](LR_cc.md) | Add backing for [64], [70], [91] or reclassify. |
| C4 | [LR_Matrix.md](LR_Matrix.md) | Reconcile orphan [101] (exists only in matrix, absent from LR_cc.md numbering). |
| C5 | [figure/PRISMA-flowchart.md](figure/PRISMA-flowchart.md) | File is empty (0 bytes) — populate with the (corrected) flow diagram. |
| C6 | `01_source/` frontmatter | Apply the 4 `ref` mis-tag fixes (flag 1) and merge 7 duplicate-note pairs (flag 5). |

---

### Verification Totals (corrected)

| Category | Original | Corrected | Note |
|---|:---:|:---:|---|
| 🟢 Included in synthesis | 70 | **69** | [90] folded into [57] as duplicate |
| 🔴 Excluded at full-text eligibility | 37 | 37 | — |
| ⚪ Not retrieved | 6 | 6 | — |
| 🟡 Excluded at title/abstract screening | 203 | 203 | — |
| ⚫ Duplicates removed | 96 | **97** | +1 for [90] |
| **Total records identified** | **412** | **412** | unchanged |
| 🔵 Supplementary (outside search) | 19 | 19 | — |
| ❌ Removed reference placeholders | 13 | 13 | — |

> **Corrected arithmetic check:** 69 + 37 + 6 + 203 + 97 = **412** ✓
> *(Original 70 + 37 + 6 + 203 + 96 = 412 also balanced, but double-counted [90].)*
>
> **Caveat (repeat):** these totals are illustrative narrative figures; no database
> export, dedup log, or screening sheet exists in the workspace to substantiate the
> 412 / 97 / 315 / 203 / 112 / 6 / 106 / 37 / 69 chain. Backing data is required before
> these can be cited as audited counts.

---

*End of PRISMA 2020 Reconciliation Matrix*
