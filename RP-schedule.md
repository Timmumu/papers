# RP-schedule — 5-year Part-time PhD Monthly Plan

> Companion to `RP.md`. 60-month schedule for a part-time programme starting **Sep 2026** (adjust month indices if start date differs). One row per month; quarters and milestones highlighted in **bold**. Decision gates (G1–G5) are mandatory go/no-go points where the corresponding falsifiability statement in `RP.md` is evaluated.

---

## 0. Effort and resourcing assumptions

| Item | Assumption |
|---|---|
| Effective research time | ~20 h/week + 4 leave bursts/year × 1 week each |
| Annualised effort | ≈ 0.4–0.5 FTE |
| 5-year part-time total | ≈ 2.0–2.5 FTE-years |
| Cloud budget (Vertex AI + LLM API) | ≈ USD 5 000 / year, pin to open-weight LLM after schema freeze |
| Data sources, Stage 1 | Two anchor case projects (candidate's employer) only |
| Hardware | Vertex AI A100 GPU on-demand for O2 training (≈ 200 GPU-hours/year) |
| Critical collaborators | Supervisor (Prof. Ng) + one external mathematician for O3 Lyapunov proof |

---

## 1. Year-level milestones (read this first)

| Year | Headline outcome | Decision gate |
|---|---|---|
| Year 1 | Data + ethics secured; O1 (NLP extraction) MVP working on one project | **G1** end-Y1: O1 precision/recall ≥ 0.70, κ ≥ 0.6 — else simplify schema |
| Year 2 | O2 (GNN forward predictor) trained, conformally calibrated on case 1 | **G2** end-Y2: calibrated coverage within ±10 pp of nominal — else freeze conformal layer, proceed |
| Year 3 | O3 (convergence loop) running on parametric variants; Lyapunov spec | **G3** end-Y3: monotone decrease of L(state) observed — else report as empirical decrease |
| Year 4 | O4 (coupling) experiments; sustainability head integrated; case 2 validation | **G4** end-Y4: positive correlation checkpoint ↔ iterations-to-convergence — else decompose contributions |
| Year 5 | Thesis written, submitted, defended | **G5** Month-57: thesis ready for examination |

---

## 2. Monthly plan (60 rows)

> **Legend.** Action = primary work; Deliverable = artefact ready by end of month; Risk = single most-likely failure that month; Bypass = the cheapest fallback action if the risk fires.

### Year 1 — Foundation (Months 1–12) — Sep 2026 → Aug 2027

| Month | Action | Deliverable | Risk | Bypass |
|---|---|---|---|---|
| M01 | Confirmation of registration; supervisor sign-off on RP v2; LR_cc finalisation | Registration confirmed; RP v2 archived | Schedule slip on registration paperwork | Shift M02 schedule by ≤ 2 weeks |
| M02 | Ethics application (IRB) for industry data; NDA with employer drafted | IRB submitted; NDA executed | NDA negotiation > 6 weeks | Begin O1 prototyping on public RIDDOR data only |
| M03 | Data inventory of case 1: BIM (IFC), NCRs, RFIs, emails, photos; storage on Cloud Storage | Data manifest CSV; raw store frozen as v1 | Missing BIM versions or NCR gaps | Document gaps as case-1 caveats; do not re-scope |
| M04 | Define Esmaeili/Tixier attribute schema variant; ground-truth annotation guideline v1 | Annotation guideline PDF; 50 documents pre-annotated | Schema drift among annotators | Pin to Tixier 2016 vocabulary verbatim; defer extension |
| M05 | LLM provider selection (Gemini vs DeepSeek); cost model | Provider decision memo; budget log | Vertex AI quota delay | Run extraction on local Ollama (DeepSeek-7B) |
| M06 | O1 v0.1 — structured-output prompting on 50 documents | JSON outputs + source-span citations | LLM hallucination rate > 30 % | Tighten JSON schema + reject ungrounded fields |
| M07 | Recruit second annotator (RA or postgrad); annotate 200 documents | 200-doc gold set; inter-annotator κ measurement | κ < 0.6 | Re-train annotator; re-draft guideline |
| M08 | O1 v0.2 — GraphRAG over Neo4j; cross-document linkage | Neo4j graph dump v1; precision/recall report | Neo4j ingestion script too slow | Use SQLite + NetworkX as interim graph store |
| M09 | O1 v0.3 — CLIP photo–text alignment | Photo-to-element retrieval evaluation | CLIP zero-shot fails on site clutter | Fine-tune CLIP on 500 photo–RFI pairs |
| M10 | O1 evaluation on held-out 100 documents; cross-jurisdiction test on RIDDOR sample | P/R report; cross-jurisdiction memo | **G1 fails (P/R < 0.7)** | Demote O1 to attribute *suggestion* tool; downstream uses human-in-loop labels |
| M11 | Write paper draft 1 (O1 methodology + case 1 evaluation) | Draft 1 to supervisor | Writing displaces engineering | Block 2 days/week for writing only |
| M12 | **Confirmation of candidature panel; G1 decision recorded** | Confirmation report; presentation | Panel requests scope change | Negotiate with supervisor before panel; protect O3/O4 |

### Year 2 — Forward predictor (Months 13–24) — Sep 2027 → Aug 2028

| Month | Action | Deliverable | Risk | Bypass |
|---|---|---|---|---|
| M13 | Submit O1 paper to Automation in Construction or AEI | Submission receipt | Reviewer-1 delay | Continue O2 work; do not block |
| M14 | BIM-to-graph extraction pipeline (IFC → PyTorch Geometric) | `ifc2pyg` script + topology validation report | IFC parsing edge cases | Fallback to IfcOpenShell + manual element filtering |
| M15 | O2 v0.1 — GNN backbone (no cross-modal attention yet) | Defect-head accuracy baseline | Class imbalance (defects rare) | Focal loss + over-sampling |
| M16 | O2 v0.2 — Cross-modal attention to O1 text + CLIP photo embeddings | Ablation table v1 | Attention does not help over geometry-only | Report null result; keep geometry-only as default |
| M17 | O2 v0.3 — Safety head + sustainability head (shared backbone) | Three-head training run on case 1 | Sustainability labels too sparse | Use EPD database + 1 contractor ESG report only |
| M18 | O2 calibration — MAPIE conformal layer; reliability diagram | ECE + empirical coverage report | Coverage drifts under distribution shift | Re-calibrate per-project; document caveat |
| M19 | Element-level k-fold validation; ablation with/without O1 features | Cross-validation tables | Small-n inflates variance | Bootstrap CIs; honest report |
| M20 | External validation — train on case 1, test on case 2 (BIM only, no labels yet) | Generalisation memo | Performance drops > 50 % | Document as case-study-evidence; flag for Stage 2 |
| M21 | Write paper draft 2 (O2 methodology + calibration + ablation) | Draft 2 to supervisor | **G2 fails (coverage > ±10 pp)** | Freeze conformal layer; cite as limitation in thesis |
| M22 | **G2 decision recorded; submit O2 paper** | Submission receipt | API cost overrun | Move bulk inference to nightly batch jobs |
| M23 | Start O3 theoretical work — read control-theory literature on Lyapunov functions, contraction mappings | Annotated bibliography + 1-page proof sketch | Mathematics out of comfort zone | Engage external mathematician (1 day/month consulting) |
| M24 | Mid-candidature progress review | Annual report submitted | Reviewer questions O3 feasibility | Show proof sketch from M23 as evidence |

### Year 3 — Convergence loop (Months 25–36) — Sep 2028 → Aug 2029

| Month | Action | Deliverable | Risk | Bypass |
|---|---|---|---|---|
| M25 | O3 v0.1 — define design parameter vector for case 1 BIM (≈ 20–50 parameters); parametric variant generator | Variant generator script; 100 synthetic variants | Variant space combinatorial explosion | Restrict to top-5 sensitivity-ranked parameters (use SA from M28) |
| M26 | O3 v0.2 — Python orchestrator calling O2 Vertex Endpoint; BigQuery iteration store | Round-trip latency benchmark | Endpoint latency > 5 s/call | Use batch endpoint or local model copy |
| M27 | O3 v0.3 — gradient-free perturbation update (random-direction line search) | First end-to-end loop run | Loop diverges | Add trust-region cap; clamp parameter range |
| M28 | Sensitivity analysis (Sobol indices) on O2 to identify dominant parameters | Tornado diagram per case | Sobol computationally expensive | Use Morris elementary effects as cheap surrogate |
| M29 | Lyapunov candidate $L(\text{state})$ specification + Chebyshev termination spec | Formal write-up draft | Monotone-decrease not guaranteed under noise | Add concentration-inequality buffer; report expected decrease |
| M30 | **G3 evaluation — run loop on 5 variants of case 1; check $L(t+1) \le L(t)$** | Decision memo | **G3 fails (no monotone decrease)** | Demote claim to *empirical decrease* observed in N/5 runs |
| M31 | Baseline comparison — Optuna TPE on same parameter space | Baseline performance table | TPE outperforms O3 | Report honestly; reposition O3 as *interpretable* alternative |
| M32 | Pareto-frontier analysis (defect-density × carbon × cost) | Pareto plots | Pareto front degenerate | Add additional objectives (cost or duration) |
| M33 | Replicate on case 2 BIM | Cross-case O3 results | Case 2 too different for transfer | Run case 2 from scratch; report as case-study evidence |
| M34 | Write paper draft 3 (O3 methodology + Lyapunov + benchmarks) | Draft 3 to supervisor | Mathematical reviewer rejection | Have external mathematician co-author for credibility |
| M35 | Submit O3 paper to ASCE J. Comp. Civ. Eng. or AEI | Submission receipt | Mid-candidature paperwork | Block 1 week for admin |
| M36 | **End-Y3 review; G3 outcome locked in thesis outline** | Updated thesis outline | Scope creep pressure | Defer all extensions to Stage 2 in writing |

### Year 4 — Coupling & integration (Months 37–48) — Sep 2029 → Aug 2030

| Month | Action | Deliverable | Risk | Bypass |
|---|---|---|---|---|
| M37 | O4 v0.1 — Vertex Pipelines re-training workflow; model registry setup | Pipeline DAG; first scheduled retrain | Pipeline orchestration overhead | Manual monthly retrain via cron + logged commits |
| M38 | Generate (variant, predicted, realised-proxy) tuples from O3 runs to date | Training tuple dataset v1 | Realised proxy too noisy | Use next-iteration prediction consensus as proxy |
| M39 | Re-train O1 + O2 on enlarged corpus (case 1 + O3 tuples); freeze checkpoint v2 | Checkpoint v2 in registry | Catastrophic forgetting | Mix original + new data 50:50 |
| M40 | Re-run O3 loop with O2-v2 on case 1; record iterations-to-convergence | First co-improvement data point | No measurable improvement | Increase O3 step budget; investigate label noise |
| M41 | Re-train O2 → checkpoint v3; re-run O3 | Checkpoint v3 + run | Cumulative cost overrun | Pause re-training; use last good checkpoint |
| M42 | Re-train → v4 + run; full case 1 co-improvement curve (4 checkpoints) | Co-improvement plot draft | Slope flat / negative | Switch to per-objective decomposition narrative |
| M43 | Replicate co-improvement on case 2 | Case-2 co-improvement plot | Case 2 lacks tuples | Use cross-case tuples (transfer scenario) |
| M44 | Statistical significance test (paired test on iterations-to-convergence) | p-value + effect size | **G4 fails (no positive correlation)** | Report decomposed O1/O2/O3 contributions; reframe O4 as diagnostic |
| M45 | Sustainability head deep dive — embodied carbon MAE on case 1+2 | Carbon-MAE report | EPD coverage too sparse | Use ICE database defaults; document data limitation |
| M46 | Write paper draft 4 (O4 coupling + thesis chapter 6 draft) | Draft 4 to supervisor | Writing fatigue | Skeleton-first writing; revise to prose later |
| M47 | Submit O4 paper to top-tier (Automation in Construction or Engineering) | Submission receipt | Review delay | Continue thesis assembly |
| M48 | **End-Y4 review; G4 outcome locked; thesis chapters 1–6 outlined** | Chapter outlines + 30 % drafted | Supervisor unavailable | Maintain weekly written updates |

### Year 5 — Write-up, viva, contingency (Months 49–60) — Sep 2030 → Aug 2031

| Month | Action | Deliverable | Risk | Bypass |
|---|---|---|---|---|
| M49 | Thesis chapter 1 (intro) + 2 (LR) final drafts (reuse LR_cc) | Chapters 1–2 to supervisor | Reuse rights from any joint paper | Cite own papers; rewrite where needed |
| M50 | Thesis chapter 3 (methodology) final draft | Chapter 3 to supervisor | Method changes during write-up | Lock methodology at start of M50 |
| M51 | Thesis chapter 4 (O1) + 5 (O2) final drafts | Chapters 4–5 to supervisor | Late reviewer comments on O1 paper | Add as appendix; do not re-do experiments |
| M52 | Thesis chapter 6 (O3) + 7 (O4) final drafts | Chapters 6–7 to supervisor | Co-improvement curve weak | Honest reporting + decomposition narrative |
| M53 | Thesis chapter 8 (discussion, contributions, limitations, future work) | Chapter 8 + full TOC | Future-work creep | Cap each future track at 0.5 page |
| M54 | Full integration pass; cross-reference check; figure/table audit | Thesis v0.9 | Inconsistent terminology | Run terminology checker script across .md/.tex |
| M55 | Supervisor + 1 critical reader full review (4 weeks) | Reviewer comments | Major rewrite requested | Negotiate scope of revision; defer to viva corrections |
| M56 | Address reviewer comments; thesis v1.0 | Thesis v1.0 | Slip into M57 | Buffer of M58 absorbs slip |
| M57 | **Submit thesis for examination (G5)** | Submission confirmed | External examiner unavailable | Two examiner nominations from M48 onwards |
| M58 | Viva preparation: mock viva with supervisor + colleague | Mock viva notes; defence slide deck | Anxiety / question gaps | Re-read RP-methods.md; rehearse falsifiability bullets |
| M59 | **Viva voce examination** | Viva outcome (corrections expected) | Major corrections | Plan M60 for revisions |
| M60 | Corrections + final binding + archive open-source code/data release | Final thesis lodged; GitHub release tagged | Re-examination required | Reserve 3 months unscheduled if needed |

---

## 3. Critical bypass / decision points (consolidated)

| Gate | Month | Test | If pass | If fail (bypass) |
|---|---|---|---|---|
| **G1** | M12 | O1 P/R ≥ 0.70, κ ≥ 0.6 | Proceed to O2 | Simplify schema; demote O1 to human-in-loop *suggestion* tool; thesis claim becomes "O1 as an attribute-extraction assistant" |
| **G2** | M21–M22 | Calibrated coverage within ±10 pp; O1-features beat geometry-only ablation | Proceed to O3 | Freeze conformal layer; document as limitation; keep point-prediction O3 |
| **G3** | M30 | Monotone decrease of $L(\text{state})$ observed | Proceed to O4 | Demote to *empirical decrease in N/5 runs*; still publishable as case study |
| **G4** | M44 | Positive correlation checkpoint ↔ iterations-to-convergence (significant) | O4 claim survives | Decompose into per-objective contributions; reposition O4 as diagnostic study |
| **G5** | M57 | Thesis submittable per supervisor + 1 critical reader | Submit | Use M58 buffer; renegotiate timeline only if critical |

---

## 4. Cross-cutting workstreams (run in parallel — do not appear as separate months)

| Workstream | Cadence | Owner | Notes |
|---|---|---|---|
| Literature monitoring (LR_cc updates) | Weekly 1 h | Candidate | One commit/week to `MD/LR_cc.md` |
| Atomic notes corpus maintenance | Monthly | Candidate | One Phase-3x sweep / quarter |
| Code & data versioning (GitHub, DVC) | Continuous | Candidate | Tag at each gate G1–G5 |
| Supervisor meeting | Monthly | Both | Standing 1-h slot; agenda + minutes in repo |
| Cloud cost review | Quarterly | Candidate | Quota alarm at 80 % of monthly budget |
| Backup of case-study data | Quarterly | Candidate | Encrypted offline copy per NDA |
| Conference participation | Annual | Candidate | 1 conference paper/year aligned with paper drafts |

---

## 5. Sensitivity of the schedule to part-time reality

| Slip scenario | Likely cause | Recovery |
|---|---|---|
| +2 months on Y1 | NDA / IRB delay | Defer M03–M04 by 2 months; absorb in M12 buffer |
| +3 months on Y2 | Class imbalance + calibration tuning | Simplify O2 to defect-only head; promote safety/sustainability to Stage 2 |
| +3 months on Y3 | Lyapunov proof harder than expected | Demote to empirical; engage external mathematician earlier |
| +4 months on Y4 | Coupling effect statistically marginal | Extend O4 by 2 months; cut thesis chapter 8 future-work tracks (b) and (e) |
| Career disruption | Job change | Use accrued annual leave for intensive 4-week sprint at next gate |

---

## 6. Effort allocation summary (target)

| Category | % of total effort | Justification |
|---|---|---|
| Engineering (O1 + O2 + O3 + O4) | 55 % | The core technical contribution |
| Theoretical work (Lyapunov, conformal) | 10 % | Concentrated in Y3 |
| Data + ethics + governance | 10 % | Heaviest in Y1 |
| Experimentation + evaluation | 10 % | Spread across all years |
| Writing (papers + thesis) | 15 % | Heaviest in Y2 end, Y3 end, Y4 end, all of Y5 |
| **Total** | **100 %** | ≈ 2.0–2.5 FTE-years over 5 calendar years |

---

## 7. Use of this schedule

- Bring this document to monthly supervisor meetings.
- Update **only** the *Deliverable* and *Risk-fired* columns; do not casually re-schedule rows.
- A formal re-baseline is allowed at G1, G2, G3, G4, G5 — nowhere else.
- If three consecutive months slip beyond their deliverable, escalate to supervisor + invoke the matching bypass column.
