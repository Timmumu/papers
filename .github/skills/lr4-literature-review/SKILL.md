---
name: lr4-literature-review
description: 'Repeat the AECO digital-twin literature review workflow for 04d_LR4 using 0.1a.Corpus_Merged-956 nos. v2.csv. Use when asked to do first screening from title, keywords, and abstract; extract Endnote full text for included papers; perform step-3 deep reading; rebuild SLR summary matrix step 1 and SLR summary matrix step 3; or keep 04d_LR4 aligned with the proven 04c_LR 3round structure.'
argument-hint: '[round folder or corpus path]'
user-invocable: true
---

# LR4 Literature Review Workflow

## Purpose

Use this skill to rerun the established SLR workflow for a new corpus in `04d_LR4` while preserving the working style and deliverable structure proven in `04c_LR 3round`.

Default target corpus:
- `04d_LR4/2. vosviewer/0.1a.Corpus_Merged-956 nos. v2.csv`

Primary deliverables:
- `04d_LR4/SLR summary matrix step 1.md`
- verified staged full text files under the `04d_LR4` full-text folders
- `04d_LR4/SLR summary matrix step 3.md`

## When To Use

- User asks to repeat the literature review on a new merged CSV corpus.
- User mentions `04d_LR4`, `0.1a.Corpus_Merged-956 nos. v2.csv`, `step 1 screening`, `Endnote full text`, `step 3 deep read`, or `SLR summary matrix`.
- User wants the same folder logic, matrix logic, and coding discipline already used in `04c_LR 3round`.

## Inputs

Expect the CSV to provide at least these fields, already confirmed in the LR4 corpus:
- `Title`
- `Year`
- `DOI`
- `Abstract`
- `Author Keywords`
- `Index Keywords`
- `Source`
- `EID`
- author fields

Expected local full-text source:
- Endnote attachment library on disk, not remote APIs

## Default Assumptions

- Reuse the same review scope as the completed `04c_LR 3round` study unless the user explicitly changes the research question.
- Reuse the exact same Step-1 `G-H-I-J-K` screening logic as `04c_LR 3round/2 stage PRISMA guideline.md` Prompt A.
- Reuse the full Step-3 coding framework and matrix shape currently used by `04c_LR 3round`.
- Preserve the `AC1`, `AC2`, and `AC3` fusion-depth fields by default in every new round that follows this workflow.
- Be conservative during screening: if the title/keywords/abstract do not clearly satisfy the criterion, code `No` and exclude.
- Do not hand-edit the matrix as the source of truth. Keep an authoritative data store plus rebuild scripts.
- Prefer extracting shared utilities for reusable LR workflows, while keeping round-specific data and outputs isolated so existing `04c` results remain untouched.

## Folder Expectations

Keep `04d_LR4` structurally parallel to `04c_LR 3round` as far as practical.

At minimum preserve these working areas:
- `04d_LR4/0. filter/`
- `04d_LR4/1. papers retrieved/`
- `04d_LR4/2. vosviewer/`
- `04d_LR4/3. fulltext L1/`
- `04d_LR4/4. fulltext L2/`
- `04d_LR4/5. SLR matrix/`

If intermediate artifacts are needed, create them under `04d_LR4/5. SLR matrix/ss/` or a clearly named sibling folder rather than scattering temporary files.

## Procedure

### 1. Inspect And Map The Corpus

1. Confirm the LR4 folder structure and locate the merged CSV.
2. Read the CSV header and identify the fields needed for Step 1, full-text lookup, and Step 3 output.
3. Define a stable record identifier for the new round.
4. Decide whether to create LR4-specific scripts such as:
   - `scripts/screening_data_lr4.py`
   - `scripts/rebuild_lr4_step1_matrix.py`
   - `scripts/step3_data_lr4.py`
   - `scripts/rebuild_lr4_step3_matrix.py`
5. Extract shared parsing, rebuilding, verification, and staging helpers when they can support future rounds.
6. Keep round-specific data modules and output writers separate whenever shared code would otherwise risk overwriting prior work.

Decision rule:
- Default to shared utilities for reusable mechanics such as CSV parsing, matrix rendering, Endnote matching, text extraction, and validation.
- Keep review-round facts isolated in round-specific data stores, config values, and output targets.
- Never point a shared script at `04c` outputs by default.

### 2. Build Step 1 Screening

1. Parse each CSV record into an authoritative screening store.
2. Screen using title, abstract, author keywords, and index keywords.
3. Apply the same `G-H-I-J-K` logic used in `04c` Prompt A.
4. Make the Step-1 decision from those criterion columns.
5. Write a concise but auditable note for every record, especially for edge cases.
6. Rebuild `04d_LR4/SLR summary matrix step 1.md` from the authoritative store.

Minimum Step-1 output columns should remain consistent with the established matrix style:
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

Quality rules:
- `Include` only when all required Step-1 criteria are satisfied.
- `Unsure` is not a final category. Resolve conservatively to exclusion unless the existing review protocol says otherwise.
- Notes must make the decision easy to verify from title/keywords/abstract alone.

### 3. Stage Full Text From Endnote

1. Collect the Step-1 included set.
2. Search the local Endnote attachment library for each included paper.
3. Copy matched PDFs into the LR4 full-text staging area using a stable naming pattern.
4. Extract companion text files from staged PDFs for downstream verification and coding.
5. Verify staged files against metadata.
6. Track included papers with no verified full text separately.

Verification rule hierarchy:
- First choice: DOI match in front matter.
- Fallback: strong title-signature match.
- Last fallback: all major title words present when DOI is absent from front matter.

Guardrails:
- Do not trust filename-only matching.
- Treat local Endnote disk attachments as the primary source when network access is blocked.
- Remove incorrect staged files instead of silently keeping ambiguous matches.

### 4. Perform Step 3 Deep Reading

1. Iterate through verified full-text papers one by one.
2. Read the actual full text, not only metadata.
3. Apply the established Prompt B coding framework used in `04c`.
4. Store each coded decision in an LR4 Step-3 data module, not directly in markdown.
5. Rebuild `04d_LR4/SLR summary matrix step 3.md` from the authoritative data.
6. Keep missing-fulltext records in a clearly separated section if they cannot be coded.

Unless the user overrides the schema, carry forward the current Step-3 structure including:
- DT built/evaluated
- DfS/DfQ scope
- methodology
- Stage-2 decision and exclusion reason
- DT tier
- lifecycle phase coverage
- DfX focus
- self-improvement
- method
- data modality
- fusion depth, evidence, confidence
- validation
- QA score
- cluster
- detailed evidence
- strengths and gap filled
- deficiencies and future work
- DOI

Deep-read quality rules:
- Code only what is implemented or explicitly evidenced in the full text.
- Keep evidence fields specific enough for later verification.
- Separate conceptual claims from demonstrated system behavior.
- When fusion depth is ambiguous, downgrade confidence rather than overstating integration.

### 5. Validate After Every Meaningful Batch

After any substantive batch of edits or coding:

1. Run a narrow validation step immediately.
2. Check matrix row counts against the authoritative store.
3. Check required columns and allowed values.
4. Check staged PDF and TXT pairing.
5. Check full-text identity consistency.
6. Check DOI formatting where available.

Preferred validation order:
1. behavior-specific checker for the touched slice
2. matrix rebuild for the target round
3. focused verifier for LR4 outputs
4. diff inspection only if no narrower executable check exists

## Recommended Implementation Pattern

- Keep source-of-truth data in scripts or structured data files.
- Generate markdown matrices from those sources.
- Make idempotent updaters for note insertion or matrix rebuilds.
- Validate immediately after the first substantive edit to a new script.
- Use small reversible edits rather than broad rewrites.

## Quality Gates Before Declaring A Round Complete

- Step-1 matrix exists and row count matches the LR4 corpus.
- Every Step-1 row has an auditable decision note.
- Included papers have either a verified staged full text or an explicit missing-fulltext status.
- Step-3 matrix is rebuilt from authoritative coded data, not manual markdown edits.
- All controlled vocabularies used in Step 3 are internally consistent.
- No orphan staged files remain.
- The LR4 folder structure stays recognizable relative to `04c_LR 3round`.

## Ambiguities To Confirm With The User

Confirmed defaults for this workspace:

1. LR4 reuses the exact same Step-1 `G-H-I-J-K` criteria and full Step-3 schema as `04c`.
2. LR4 preserves the fusion-depth trio `AC1-AC3` by default.
3. New automation should prefer shared reusable scripts for future review rounds, with round-specific data isolated from one another.

Open only if still unspecified in a future run:

1. Where unmatched or missing-fulltext papers should be reported inside `04d_LR4`.

## Example Prompts

- `/lr4-literature-review use 04d_LR4 and build Step 1 from 0.1a.Corpus_Merged-956 nos. v2.csv`
- `/lr4-literature-review extract Endnote full text for all LR4 Step-1 includes and verify staged PDFs`
- `/lr4-literature-review continue LR4 Step-3 deep reading and rebuild the matrix`
- `/lr4-literature-review audit whether 04d_LR4 still matches the 04c round structure`

## Related Assets To Reuse

- `04c_LR 3round/2 stage PRISMA guideline.md`
- `04c_LR 3round/SLR summary matrix step 1.md`
- `04c_LR 3round/SLR summary matrix step 3.md`
- `scripts/screening_data.py`
- `scripts/step3_data.py`
- `scripts/step3_extra.py`
- `scripts/step3_fusion.py`
- full-text verification scripts already proven in the repository