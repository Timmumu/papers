# SLR LLM Prompts — Step 1 (Screening) & Step 3 (Deep-Read Coding)

Two production-ready prompts for the `SLR_Master_Matrix_4Steps.xlsx` workflow. Each is fully self-contained: paste the entire prompt into a fresh chat that has **no prior context**. Both assume the model may know nothing about your review, so every term is defined and every tricky case is pinned down.

- **Prompt A (Step 1)** screens each paper from its **title + abstract only** and returns matrix columns **G–K + Source** (→ auto-decides Include/Exclude).
- **Prompt B (Step 3)** codes each **included paper from its full text** and returns matrix columns **P–R (Stage-2) + U–AG (deep-read angles)**.

> **Batch size:** feed 10–20 papers per call, not all 450 at once — long batches degrade consistency. Keep the definitions block identical across every batch so coding stays stable.

---

# PROMPT A — STEP 1: TITLE/ABSTRACT SCREENING

Copy everything in the box below into the model, then append your batch of papers at the end.

```
ROLE
You are a meticulous systematic-literature-review screening assistant. You will screen academic papers for a review titled "A Self-Improving Cognitive Digital Twin for Design-for-Safety and Design-for-Quality in the Built Environment." You have NO prior context, so follow ONLY the definitions and rules below. Do not use outside assumptions.

WHAT THIS REVIEW IS ABOUT
The review studies DIGITAL TWINS used in the built-environment (construction) industry to improve the SAFETY and QUALITY of designs. You will decide, from each paper's TITLE and ABSTRACT ONLY, whether it should pass initial screening.

KEY DEFINITIONS (use these exactly)
- AECO = Architecture, Engineering, Construction and Operations = the built-environment / construction industry: buildings, bridges, tunnels, roads, infrastructure, civil engineering, and the operation/maintenance of such built assets. It EXCLUDES manufacturing, automotive, aerospace, shipbuilding, power/electrical equipment, electronics, healthcare/medical, and agriculture.
- Digital Twin (DT) = a live virtual replica of a physical asset that is connected to it by data (sensors, monitoring, or real-time updates). It is MORE than a static 3D model or a Building Information Modelling (BIM) model. A paper "has a Digital Twin as its core" only if it actually builds, proposes, or studies a digital twin — not if it merely mentions the phrase.
- Building Information Modelling (BIM) = a static, design-stage digital model. BIM alone is NOT a Digital Twin.
- Design for Safety (DfS) = designing to prevent construction or operation safety incidents (e.g. fall from height, struck-by, hazards, accident prevention, occupational risk).
- Design for Quality (DfQ) = designing to prevent defects, rework, non-conformance, or quality failures.
- Prevention through Design (PtD) = eliminating risks at the design stage before construction begins. Closely related to Design for Safety and Design for Quality.

THE FIVE SCREENING QUESTIONS (answer each strictly "Yes" or "No")
G. Domain is AECO (built environment)? — Yes if the paper's application is buildings/infrastructure/civil/construction/operation of built assets. No if manufacturing, automotive, aerospace, power/electrical equipment, healthcare, agriculture, or a generic non-construction context.
H. Digital Twin is core (not just a buzzword)? — Yes if a digital twin is actually built, proposed, framed, or empirically studied. No if "digital twin" appears only in passing, in the introduction/future-work as a slogan, or the work is really just BIM/3D modelling/a database with no live data linkage.
I. About Design for Safety, Design for Quality, or Prevention through Design? — Yes if the paper addresses safety, hazards, accidents, defects, rework, quality, or prevention-through-design in the built environment. No if it is purely about energy, cost, scheduling, comfort, sustainability, or asset performance WITH NO safety or quality angle.
J. Publication type OK? — Yes if it is a peer-reviewed journal article, conference paper, or review. No if it is an editorial, erratum, retraction, book/book chapter, note, short abstract-only item, or patent.
K. Written in English (full text)? — Yes if the full text is in English. No if the full text is in another language (even when the abstract is in English). If the abstract gives no language signal, assume Yes.

DECISION RULES
- Judge ONLY from the title and abstract provided. Do NOT search or infer beyond the text.
- If you are genuinely unsure on any question, answer "No" (conservative) and explain briefly in the note.
- Do NOT write an overall include/exclude verdict or an exclusion reason — the spreadsheet computes those automatically from your five answers.

EDGE CASES (apply consistently)
1. Manufacturing digital twin that is only "applied to a building component factory" → domain is manufacturing → G = No.
2. Power-equipment / electrical-grid digital twin → G = No (not AECO), even if multimodal or self-learning.
3. Paper about BIM for clash detection, with "towards digital twin" in the last sentence → H = No (DT is a buzzword here).
4. Structural Health Monitoring (SHM) of a bridge using a digital twin → G = Yes, H = Yes; I = Yes ONLY if it frames damage/defect/safety (usually yes); otherwise No.
5. Energy-optimisation or HVAC digital twin for a building with no safety/defect/quality angle → G = Yes, H = Yes, I = No.
6. Construction-safety paper using computer vision but NO digital twin → H = No.
7. A review/survey paper about digital twins in construction → J = Yes (review is an allowed type); answer G/H/I on its stated scope. (It may later be tagged as a competing review, but it still passes type screening.)
8. Non-English full text with an English abstract (e.g. indexed in CNKI) → K = No.
9. Editorial or special-issue preface that discusses digital twins → J = No.
10. Digital twin for "smart city" traffic only, no building/infrastructure asset and no safety/quality → likely G = Yes (infrastructure) but I = No; use judgement and note it.
11. If the abstract is missing or unreadable → answer all five "No" and note "abstract unavailable".

OUTPUT FORMAT (return a Markdown table, one row per paper, columns EXACTLY as below; no extra prose)
| ID | Source database | G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type OK | K English | Note |
Use only "Yes" or "No" in columns G–K. Source database must be one of: Scopus, Web of Science, Backward-snowball, Forward-snowball. Keep the Note under 15 words.

PAPERS TO SCREEN
(Paste each paper as: ID | Source | Title | Abstract)
<< paste your batch here >>
```

---

# PROMPT B — STEP 3: FULL-TEXT DEEP-READ CODING

Use this ONLY on papers that passed Step 1 **and** whose PDF full text you have on hand. Paste the full text (or a faithful long extract) of one paper at a time for best accuracy; small batches (3–5) are acceptable if full texts are short.

```
ROLE
You are a meticulous systematic-literature-review coding assistant. You will read the FULL TEXT of a construction/built-environment academic paper and code it on fixed dimensions for a review about self-improving cognitive digital twins for Design-for-Safety and Design-for-Quality. You have NO prior context; use ONLY the definitions and options below, and base every answer on the paper's actual content. Never invent details not in the text.

KEY DEFINITIONS
- AECO = Architecture, Engineering, Construction and Operations (the built-environment industry).
- Digital Twin (DT) = a live virtual replica connected to a physical asset by data; more than a static Building Information Modelling (BIM) or 3D model.
- Design for Safety (DfS) = designing to prevent safety incidents (fall from height, hazards, accidents).
- Design for Quality (DfQ) = designing to prevent defects, rework, quality failures.
- Prevention through Design (PtD) = eliminating risk at the design stage.
- "bidirectional" = data flows BOTH ways, physical-to-virtual AND virtual-to-physical (the twin can act back on the asset). One-way flow is only a digital shadow.

PART 1 — STAGE-2 FULL-TEXT CONFIRMATION (answer strictly "Yes"/"No")
P. Digital Twin is the actual subject (full text)? — Yes if the study genuinely builds/evaluates/frames a digital twin. No if, on reading the full text, the digital twin turns out to be only mentioned, aspirational, or actually just BIM/3D/a database.
Q. Design for Safety / Design for Quality confirmed in full text? — Yes if safety, hazard, accident, defect, rework, or quality is a genuine focus. No if it is really energy/cost/comfort/scheduling only.
R. Methodology is clear enough to code? — Yes if methods, data, and approach are described well enough to classify. No if it is too vague, purely a viewpoint, or gives no usable methodological detail.
(If P, Q, or R is "No", the paper is excluded at Stage-2; you may then leave Part 2 blank.)

PART 2 — DEEP-READ CODING (only if P, Q, R are all "Yes")

U. Digital Twin capability tier — choose ONE:
   - Tier 1 - Digital Model (static, no live data): a virtual model with no automated data link.
   - Tier 2 - Digital Shadow (one-way physical to virtual): live data flows from asset to model only (e.g. monitoring, dashboards).
   - Tier 3 - Digital Twin (bidirectional, two-way): the model can also act back on the physical asset (control, automated feedback).
   - Tier 4 - Cognitive / Self-improving: the twin learns and improves its own predictive model over time (adaptation, convergence, self-updating).
   - Unclear: cannot determine from the text.
   Rule: do NOT over-rate. Most papers are Tier 2. Assign Tier 4 ONLY if the paper explicitly demonstrates learning/self-improvement, not merely mentions it.

V, W, X. Lifecycle phase coverage — put 1 if the paper covers that phase, else 0:
   V = Design phase; W = Construction phase; X = Operation phase. (A paper may cover more than one.)

Z. Design-for-X target — choose ONE: Design for Safety (DfS) / Design for Quality (DfQ) / Both / Other.

AA. Self-improvement / convergence — choose ONE:
   - None: no self-improvement idea at all.
   - Mentioned only: the words self-improving/adaptive/learning/convergence appear, but nothing is implemented.
   - Implemented: an actual learning/updating mechanism is built and demonstrated.
   - Convergence-characterised: the paper additionally analyses or proves convergence (an update rule + a stated criterion/metric).

AB. Methodology — choose the ONE dominant method:
   Computer Vision / CNN / object-detection · Graph Neural Network (GNN) · LSTM / RNN (recurrent networks) · Transformer / Large Language Model (LLM) · Reinforcement Learning (RL) · Bayesian / probabilistic · Agent-based model (ABM) · Finite Element Method / physics-based · Ontology / semantic · Statistical / change-point · Digital Twin platform (no machine learning) · Other / Mixed.

AC. Data modality — choose ONE:
   - Single (one data type): uses one kind of data (e.g. images only, or sensor time-series only).
   - Multi (two or more data types): fuses two or more (e.g. vision + point cloud, or geometry + sensor + text/semantic).

AD. Validation level — choose ONE:
   - Conceptual (no test): framework/idea only, no empirical test.
   - Simulation: tested in simulation or synthetic data.
   - Single case study: validated on one real project/asset.
   - Cross-project (multiple real projects): validated across two or more real projects/assets.

AE. Quality appraisal score (0 to 5) — your overall methodological rigour rating: 0 = negligible, 5 = exemplary (clear methods, data, validation, and limitations).

AF. Thematic cluster — choose ONE:
   BIM-to-Digital-Twin architecture · Semantic interoperability · Perception / Computer Vision · Design for Safety · Predictive analytics / decision support · Lifecycle / governance · Other.

AG. Key evidence / notes — one to two sentences quoting or paraphrasing the specific evidence for the tier and self-improvement codes (so a human can audit your decision).

EDGE CASES
1. Paper claims "cognitive digital twin" in the title but the method is only monitoring → Tier 2 or 3, AA = "Mentioned only" (do not reward the title).
2. Reinforcement Learning is discussed as future work but not used → AB is the method actually used; AA = "Mentioned only".
3. Uses BIM geometry PLUS IoT sensor data → AC = "Multi".
4. Bridge SHM predicting damage from one bridge's data → V/W/X per phases (usually Operation = 1), AD = "Single case study".
5. Framework paper with an architecture diagram but no experiment → AD = "Conceptual (no test)", and P may still be Yes if a DT is genuinely proposed.
6. Design-stage safety prediction that also uses construction feedback → V = 1 AND W = 1 (cross-phase).
7. If self-improvement is claimed but no update rule/metric is shown → at most "Implemented"; reserve "Convergence-characterised" for an explicit convergence argument.
8. If genuinely unclear on the tier → "Unclear", and explain in AG.

OUTPUT FORMAT (return a Markdown table, one row per paper, columns EXACTLY as below; no extra prose)
| ID | P DT-subject | Q DfS/DfQ | R codable | U Tier | V Design | W Constr | X Oper | Z DfX | AA Self-improve | AB Methodology | AC Modality | AD Validation | AE QA(0-5) | AF Cluster | AG Key evidence |
Use only the exact option strings defined above. For V/W/X use 1 or 0. Leave U–AG blank if P/Q/R contains any "No".

FULL TEXT TO CODE
(Paste as: ID | Title | Full text or long extract)
<< paste one paper here >>
```

---

## How the outputs map back to the matrix

| Prompt | Returns columns | Paste into matrix columns | The matrix then auto-computes |
|---|---|---|---|
| **A — Step 1** | G, H, I, J, K, Source, Note | F (Source), G–K | `L` decision, `M` single exclusion reason |
| **B — Step 3** | P, Q, R + U–AG | P–R, U–AG | `S` decision, `T` reason, `Y` cross-phase, all Step-3 report tables |

## Consistency tips

1. **Freeze the definitions block.** Never edit the definitions between batches, or codes will drift across your 450 papers.
2. **Do Step 1 on abstracts only; never let it guess a tier.** The capability tier and self-improvement codes require the full text — that is why they live in Prompt B.
3. **One paper per call for Prompt B when possible.** Tier and convergence judgements are the highest-stakes, lowest-consistency codes; give the model room.
4. **Spot-check.** Re-code ~10% of papers yourself (or in a second model run) and compare — report the agreement as your reliability check in the methods section.
5. **Keep the Note / Key-evidence columns.** They are your audit trail; reviewers value being able to see why each borderline call was made.
```
