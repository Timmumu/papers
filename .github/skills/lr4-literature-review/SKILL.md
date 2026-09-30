---
name: lr4-literature-review
description: 'Redo the LR4 AECO digital-twin literature-review exercise for 04d_LR4 using 0.1a.Corpus_Merged-956 nos. v2.csv. Use when asked to do first screening from title, keywords, and abstract; extract Endnote full text for Step-1 includes; study included full texts one by one; rebuild SLR summary matrix step 1 or step 3; continue LR4 coding; or keep 04d_LR4 aligned with the proven 04c_LR 3round workflow.'
argument-hint: '[round folder or corpus path]'
user-invocable: true
---

# LR4 Literature Review Workflow

## Purpose

Use this skill to rerun the full LR4 exercise in `04d_LR4` from the merged CSV through three concrete stages:

1. Step-1 screening from title, keywords, and abstract
2. local Endnote full-text staging and verification for included papers
3. paper-by-paper Step-3 deep reading and matrix rebuild

This skill is specifically for reproducing the proven `04c_LR 3round` workflow against the LR4 corpus while keeping the LR4 data stores, scripts, and outputs isolated.

Use this full workflow skill when the user wants the end-to-end rerun. If the user wants only one phase, prefer the narrower companion skills `lr4-step1-screening` or `lr4-step3-deep-read`.

## Default Targets

- Corpus CSV: `04d_LR4/2. vosviewer/0.1a.Corpus_Merged-956 nos. v2.csv`
- Step-1 output: `04d_LR4/SLR summary matrix step 1.md`
- Step-3 output: `04d_LR4/SLR summary matrix step 3.md`
- LR4 authoritative stores: `04d_LR4/5. SLR matrix/ss/corpus_lr4.json` and `04d_LR4/5. SLR matrix/ss/coverage_lr4.json`

## When To Use

- User asks to do the LR4 exercise again from the merged 956-paper corpus.
- User asks for first screening from title, author keywords, index keywords, and abstract.
- User asks to extract full text for Step-1 included papers from the local Endnote library.
- User asks to do detailed full-text study one paper at a time.
- User asks to rebuild or continue `SLR summary matrix step 1.md` or `SLR summary matrix step 3.md` in `04d_LR4`.

## Workflow Outcome

The skill should produce or maintain:

- a complete LR4 Step-1 screening matrix aligned with `04c_LR 3round/SLR summary matrix step 1.md`
- verified staged PDFs and companion TXT extracts for included papers
- a markdown summary list for papers with no matched or no verified full text
- a Step-3 coded matrix aligned with `04c_LR 3round/SLR summary matrix step 3.md`
- auditable LR4 source-of-truth files rather than manual markdown-only edits

## Required Inputs

Expect the LR4 CSV to contain these usable fields:

- `Title`
- `Abstract`
- `Author Keywords`
- `Index Keywords`
- `Year`
- `DOI`
- `Source`
- `EID`
- author fields

Expected full-text source:

- local Endnote attachment storage on disk

## Proven LR4 Assets

Use the existing LR4 implementation first, instead of inventing a new one.

Primary scripts:

- `./scripts/lr4_parse_corpus.py`
- `./scripts/screening_data_lr4.py`
- `./scripts/rebuild_lr4_step1.py`
- `./scripts/stage_fulltext_lr4.py`
- `./scripts/rebuild_lr4_step3.py`
- `./scripts/validate_lr4_step3.py`
- `./scripts/append_step3_lr4_notes.py`
- `./scripts/make_lr4_code_extracts.py`
- `./scripts/peek_lr4.py`

Supporting Prompt definitions:

- `04c_LR 3round/2 stage PRISMA guideline.md`

## Core Rules

- Default to a full rerun from scratch unless the user explicitly asks to continue from an existing LR4 baseline.
- Reuse the same Step-1 `G-H-I-J-K` logic defined in Prompt A from `04c_LR 3round/2 stage PRISMA guideline.md`.
- Reuse the same Step-3 full-text coding logic defined in Prompt B from that same file.
- Be conservative: if title, keywords, or abstract do not clearly satisfy a criterion, code `No`.
- Do not use the markdown matrices as the source of truth.
- Keep LR4 outputs round-specific; do not point default scripts at `04c` outputs.
- Preserve the existing LR4 fusion-depth fields `AC1`, `AC2`, and `AC3` unless the user explicitly changes the schema.
- After Step 3, update only the consolidated LR4 outputs by default; do not append results back into per-paper notes unless the user asks.

## Procedure

### 1. Prepare The LR4 Corpus Store

1. Confirm the LR4 folder structure exists.
2. Confirm the merged CSV exists at the default path unless the user provided another corpus.
3. Parse the CSV into the LR4 authoritative store with `./scripts/lr4_parse_corpus.py`.
4. Treat `04d_LR4/5. SLR matrix/ss/corpus_lr4.json` as the record-level source of truth.
5. If slug collisions appear on Windows because of case-insensitive paths, resolve them in the LR4 corpus store before downstream staging.

Decision points:

- If the corpus path changes, update only LR4-specific config or invocation, not shared `04c` outputs.
- If CSV headers drift, fix parsing at the corpus-store layer before touching screening or rebuild logic.

### 2. Run Step-1 Screening

1. Screen each paper from title, abstract, author keywords, and index keywords only.
2. Apply the `G-H-I-J-K` definitions exactly as frozen in Prompt A.
3. Store screening judgments in the LR4 screening modules and aggregate them through `./scripts/screening_data_lr4.py`.
4. Rebuild the markdown output with `./scripts/rebuild_lr4_step1.py`.
5. Check that the resulting matrix matches the LR4 corpus row count.

Expected Step-1 deliverable shape:

- `ID`
- `Author`
- `Title`
- `Year`
- `Source`
- `G`
- `H`
- `I`
- `J`
- `K`
- `Decision`
- `Note`
- `DOI`

Decision rule:

- Include only when all required Step-1 criteria pass.
- Do not leave `Unsure` as a final state.
- Notes must make the decision auditable from title, keywords, and abstract alone.

### 3. Extract And Verify Full Text

1. Take the Step-1 included set as input.
2. Search the local Endnote attachment library for candidate PDFs.
3. Stage matched files into `04d_LR4/3. fulltext L1/` and downstream LR4 locations using `./scripts/stage_fulltext_lr4.py` and related verified helpers.
4. Extract companion TXT files for downstream coding.
5. Record coverage and verification status in `04d_LR4/5. SLR matrix/ss/coverage_lr4.json`.
6. Keep unmatched, ambiguous, and unverified cases explicitly tracked.
7. Emit a user-facing markdown summary list for papers with no matched full text or no verified full text.

Verification hierarchy:

- DOI evidence in front matter
- strong normalized title match
- last-resort major-title-word match only when DOI evidence is absent

Guardrails:

- Never trust filename-only matching.
- Remove false-positive staged files instead of carrying them forward.
- Prefer local Endnote disk evidence over remote discovery when the task is to reproduce the LR4 workflow.

### 4. Perform Step-3 Deep Reading

1. Work through verified full-text papers one by one.
2. Read the actual paper text, not metadata summaries.
3. Apply the Prompt B coding framework from `04c_LR 3round/2 stage PRISMA guideline.md`.
4. Store codes in LR4 data modules such as `step3_lr4_data.py`, `step3_lr4_extra.py`, and `step3_lr4_fusion.py` rather than editing markdown directly.
5. Rebuild the markdown matrix with `./scripts/rebuild_lr4_step3.py`.
6. Do not update per-paper notes by default.
7. Use `./scripts/make_lr4_code_extracts.py` and `./scripts/peek_lr4.py` for coding extracts and spot-checks.
8. Only use `./scripts/append_step3_lr4_notes.py` if the user explicitly asks to push Step-3 results back into paper notes.

Minimum Step-3 expectations:

- confirm Stage-2 inclusion from full text
- code DT tier, lifecycle phase, DfX target, self-improvement, method, modality, validation, QA, cluster, and evidence
- preserve LR4 fusion-depth coding and confidence fields
- separate full-text-confirmed evidence from speculative claims

### 5. Validate Immediately After Each Batch

After the first substantive change in a slice, run one focused validation before doing more editing.

Preferred validation order:

1. rebuild the touched LR4 matrix
2. run the focused LR4 checker for that slice
3. inspect row counts and controlled values
4. inspect diffs only if no narrower executable validation exists

Concrete LR4 validation checks:

- Step 1: `./scripts/rebuild_lr4_step1.py`
- Full-text staging: verify PDF and TXT pairing plus `coverage_lr4.json`
- Step 3: `./scripts/validate_lr4_step3.py`, then `./scripts/rebuild_lr4_step3.py`

## Completion Gates

Do not call the LR4 exercise complete until all of the following are true:

- `SLR summary matrix step 1.md` exists and matches the corpus row count
- every Step-1 row has an auditable note
- every Step-1 include has either verified full text, explicit unverified status, or explicit no-candidate status
- `SLR summary matrix step 3.md` is rebuilt from authoritative LR4 data stores
- controlled vocabularies in Step 3 stay internally consistent with Prompt B
- staged files and coverage records do not contain unresolved false positives

## Known LR4 Baseline

This workspace already established a completed LR4 baseline that can be reused or audited:

- corpus size: 956 rows
- Step-1 result: 244 includes and 712 excludes
- verified full text: 151
- unverified full text: 63
- no candidate: 30
- Step-3 coded rows: 151

Treat those numbers as a reproducibility target unless the corpus or decision protocol changes.

## Ambiguities To Confirm With The User

Current defaults for this workspace:

1. Rerun LR4 from scratch unless the user explicitly requests continuation or audit-only behavior.
2. Generate a markdown summary list for papers with unmatched or unverified full text, not only `coverage_lr4.json`.
3. After Step 3, update only the consolidated LR4 matrix outputs unless the user explicitly requests note-level backfill.

Ask only if a future task overrides one of those defaults.

## Example Prompts

- `/lr4-literature-review rebuild LR4 Step 1 from 04d_LR4/2. vosviewer/0.1a.Corpus_Merged-956 nos. v2.csv`
- `/lr4-literature-review extract Endnote full text for all LR4 Step-1 includes and verify coverage`
- `/lr4-literature-review code LR4 full texts one by one and rebuild Step 3`
- `/lr4-literature-review validate whether current 04d_LR4 still reproduces the 04c workflow`

## Companion Skills

- `lr4-literature-review`: full rerun from scratch
- `lr4-step1-screening`: Step 1 only
- `lr4-step3-deep-read`: Step 3 only