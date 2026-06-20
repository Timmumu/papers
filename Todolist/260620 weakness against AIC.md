Let me do a thorough, independent appraisal of LR.md against Automation in Construction standards.

---

## Independent Appraisal: LR.md for *Automation in Construction*

**Journal:** Automation in Construction (Elsevier, Q1, IF ≈ 10.5)
**Manuscript type:** Systematic Literature Review
**Verdict:** **Not yet publishable — Major Revision Required before submission**

---

### 1. Contribution & Novelty — ⭐⭐⭐ (of 5)

**Strengths:**
- The convergence framework (backward causal updating + forward forecasting) with formal mathematical definitions is a genuine intellectual contribution that distinguishes this from descriptive DT surveys
- The five-gap matrix (Table 3) is structured, falsifiable, and actionable
- The maturity classification (Levels 1–3 with percentage distributions) provides a useful diagnostic tool

**Weaknesses:**
- Core novelty claim ("first to systematically interrogate methodological validity") is partially undermined by overlapping findings in Jones2020, Omrany2023, and Shahzad2022 — the gap is narrower than argued
- The UQ deficit finding (97.1% deterministic), while striking, is not entirely surprising given the field's immaturity; the paper doesn't sufficiently distinguish whether this is a genuine oversight by the community or an artifact of the search strategy
- **The framework (§5) is not validated** — the paper explicitly states "not a validated system." AIC expects empirical grounding even in review papers that propose frameworks. At minimum, a worked example or simulation study would be expected.

---

### 2. Methodological Rigor — ⭐⭐ (of 5)

**Strengths:**
- PRISMA 2020 flow is documented
- Round-2 search is auditable (748→424 trackable from CSV exports)
- Quality appraisal rubric (Table 1) adapted from Kitchenham & Charters

**❌ CRITICAL ISSUE: Round-1/Round-2 corpus mismatch.**
The abstract claims "synthesizing 69 peer-reviewed articles" from a PRISMA-compliant search. However:
- §2.1-2.3 describe a **round-2** Lens.org search (748→424 retained, screening in progress)
- §3-5 synthesize a **round-1** corpus of 69 studies from a *different* search (five databases, 412 records)
- §2.4's quality appraisal uses round-1 numbers (106 assessed, 37 excluded) that the paper itself describes as "illustrative narrative figures... not independently reconstructable"

**This is a fatal transparency problem.** A reviewer will ask: "Which search produced the 69 studies you synthesized? If the round-1 search, why report a different round-2 search in §2.1? If the round-2 search, why are the synthesis sections based on round-1?" This must be resolved before any submission.

**❌ Single-source search.** PRISMA 2020 recommends minimum two databases. Lens.org alone, while an aggregator, is atypical for a top-tier SLR. The justification ("broad, reproducible coverage") needs strengthening with comparative coverage analysis.

**❌ Wikilink formatting.** References like `[[Deng2021#^sec-2-ladder]]` are Obsidian syntax, not standard academic citation format. AIC uses numbered references. These must be converted.

**❌ Preprint/submitted reliance.** Key claims rely on [2] Akhavian2025 (arXiv preprint), [4] Hamel2024 (arXiv), [TBD-A], [TBD-B] (submitted). AIC reviewers will question whether non-peer-reviewed sources can anchor Level-3 maturity claims.

---

### 3. Internal Consistency — ⭐⭐ (of 5)

| Issue | Detail |
|---|---|
| Abstract vs. body | Abstract says 69 studies, 2010–2025; §2.3 says 424 retained, 2019–2026 |
| §2.3 vs. §2.4 | §2.3 describes round-2 screening (424 retained); §2.4 describes round-1 QA (106 assessed, 37 excluded → 69 included). Different corpora, conflated reporting |
| "Round-1 corpus carried forward" callout | Buried in a blockquote; most readers will miss it |
| QA numbers | 106 assessed − 37 excluded = 69 included ✓, but 106 ≠ 112 (the number sought in §2.3 of the original round-1 manuscript). Discrepancy acknowledged but unresolved |

---

### 4. Evidence Quality — ⭐⭐⭐ (of 5)

**Strengths:**
- 69 studies across 6 thematic clusters provide reasonable coverage
- Gap analysis (%) is quantified from the synthesis corpus
- Evidence block IDs (`^sec-abstract`, etc.) enable traceability

**Weaknesses:**
- Thematic commentary is thin — typically 1-3 sentences per study, without critical engagement with methodology flaws in individual papers
- The 12 Level-3 studies receive superficial treatment; only Akhavian2025 is identified as having a working prototype, yet its limitations are not discussed
- Supplementary references [92]–[100], [TBD-A], [TBD-B] are cited in the synthesis but were never screened through the PRISMA pipeline — this is a methodological inconsistency

---

### 5. Writing Quality — ⭐⭐⭐⭐ (of 5)

**Strengths:**
- Clear, academic English throughout
- Well-structured argument: literature → gaps → framework → discussion
- Mathematical formalism (§5.2-5.3) is precise and well-integrated
- Mermaid diagrams aid comprehension

**Weaknesses:**
- Introduction (§1) has a run-on sentence (paragraph 3: "Several recent reviews have surveyed... [95], current implementations are predominantly descriptive...") — grammatical splice
- Some repetitive framing: "cognitive, closed-loop" appears >10 times
- Callout blocks (the `>` blockquotes) interrupt the academic flow and read as internal development notes, not polished manuscript text

---

### 6. Practical Significance — ⭐⭐⭐ (of 5)

**Strengths:**
- The gap matrix (Table 3) is directly usable as a due-diligence checklist for practitioners evaluating DT vendors
- The maturity classification gives organisations a self-assessment tool

**Weaknesses:**
- No case study, pilot, or worked example to ground the framework in real construction practice
- The convergence criterion ($\mathbb{E}[\Delta_t] < \epsilon$) is elegant but not demonstrated on any data — a reviewer will ask "has anyone come close?"
- Practical barriers (cost, training, legacy BIM incompatibility) are not discussed

---

### Summary Scorecard

| Criterion | Rating | AIC Standard |
|---|---|---|
| Contribution & Novelty | ⭐⭐⭐ | Needs sharper positioning vs. existing reviews |
| Methodological Rigor | ⭐⭐ | **Fatal**: round-1/round-2 mismatch; single-source search |
| Internal Consistency | ⭐⭐ | Abstract, §2, §3 describe different corpora |
| Evidence Quality | ⭐⭐⭐ | Adequate depth but thin per-study engagement |
| Writing Quality | ⭐⭐⭐⭐ | Well-written, minor grammatical issues |
| Practical Significance | ⭐⭐⭐ | Framework is useful but unvalidated |
| **OVERALL** | **⭐⭐½** | **Major Revision Required** |

---

### Required Actions Before AIC Submission

| Priority | Action |
|:---:|---|
| **P0** | **Resolve the round-1/round-2 corpus mismatch.** Either (a) complete Phase B and rebuild §3-5 from the 424 round-2 records, or (b) clearly separate the two rounds as distinct phases of an ongoing review with a unified narrative |
| **P0** | **Add a second database** to the search strategy, or provide a rigorous single-source justification with comparative coverage analysis vs. Scopus/Web of Science |
| **P1** | **Convert all wikilinks** to standard numeric citations `[1]`, `[2]` |
| **P1** | **Replace or caveat preprint references** — Akhavian2025 and Hamel2024 need peer-reviewed alternatives or explicit preprint caveats |
| **P1** | **Fill the PRISMA flowchart** (`figure/PRISMA-flowchart.md` is empty) |
| **P2** | **Deepen thematic synthesis** — 2-3 paragraph critical engagement with 5-8 key studies per cluster |
| **P2** | **Add a worked example** or simulation study demonstrating the convergence criterion on hypothetical data |
| **P2** | **Remove or convert development callouts** (blockquotes) to standard manuscript prose |
| **P3** | **Consolidate supplementary references** [92]–[100] into the PRISMA pipeline or clearly separate as "post-hoc additions" |
| **P3** | **Fix the introduction sentence splice** and reduce repetitive framing |

---

### Realistic Publication Pathway

1. **Now → Complete Phase B** (full-text synthesis of 424 round-2 records)
2. **Month 1–2**: Rebuild §3-5 from round-2 corpus; add second database search
3. **Month 3**: Deepen thematic commentary; add worked example; convert formatting
4. **Target**: Submission-ready by end of 2026
5. **Alternative**: If Phase B is distant, publish as a **two-part series** — Part I: Systematic search + bibliometric profile (the round-2 screening); Part II: Thematic synthesis + framework (after Phase B)