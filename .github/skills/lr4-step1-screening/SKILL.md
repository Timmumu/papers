---
name: lr4-step1-screening
description: 'Run only LR4 Step 1 screening for 04d_LR4 from 0.1a.Corpus_Merged-956 nos. v2.csv. Use when asked to screen by title, abstract, author keywords, and index keywords only; rebuild SLR summary matrix step 1; or audit Step-1 include/exclude decisions without doing fulltext or Step 3.'
argument-hint: '[corpus path or LR4 folder]'
user-invocable: true
---

# LR4 Step 1 Screening

## Purpose

Use this skill when the user wants only the first-screening phase of LR4.

This skill stops after producing the Step-1 screening outputs. It does not stage full text and does not perform Step-3 deep reading.

## Default Targets

- Corpus CSV: `04d_LR4/2. vosviewer/0.1a.Corpus_Merged-956 nos. v2.csv`
- Authoritative corpus store: `04d_LR4/5. SLR matrix/ss/corpus_lr4.json`
- Step-1 matrix: `04d_LR4/SLR summary matrix step 1.md`

## When To Use

- User asks to do only the first screening.
- User wants title, keyword, and abstract screening only.
- User wants to rebuild `SLR summary matrix step 1.md`.
- User wants to review or audit `G-H-I-J-K` decisions without touching fulltext or Step 3.

## Core Rules

- Default to rerunning Step 1 from scratch unless the user explicitly asks to continue from an existing LR4 screening state.
- Apply the frozen Prompt A criteria from `04c_LR 3round/2 stage PRISMA guideline.md`.
- Judge only from title, abstract, author keywords, and index keywords.
- Be conservative: if a criterion is unclear, code `No`.
- Do not hand-edit markdown as the source of truth.

## Primary Assets

- `./scripts/lr4_parse_corpus.py`
- `./scripts/screening_data_lr4.py`
- `./scripts/rebuild_lr4_step1.py`
- `04c_LR 3round/2 stage PRISMA guideline.md`

## Procedure

### 1. Prepare LR4 Screening Inputs

1. Confirm the LR4 folder structure and target CSV.
2. Parse the merged CSV into `corpus_lr4.json` with `./scripts/lr4_parse_corpus.py`.
3. Resolve any slug collisions in the authoritative LR4 corpus store before screening.

### 2. Apply Step-1 Screening

1. Evaluate each paper against `G-H-I-J-K`.
2. Use title, abstract, author keywords, and index keywords only.
3. Store decisions in the LR4 screening modules aggregated by `./scripts/screening_data_lr4.py`.
4. Rebuild the markdown matrix with `./scripts/rebuild_lr4_step1.py`.

### 3. Validate Step-1 Output

1. Confirm row count matches the LR4 corpus.
2. Confirm each row has an auditable note.
3. Confirm no final `Unsure` state remains.
4. Rebuild the matrix immediately after any substantive screening update.

## Deliverables

- `04d_LR4/SLR summary matrix step 1.md`
- updated LR4 screening source-of-truth data

## Completion Gate

Step 1 is complete only when the matrix exists, row counts match the corpus, and every row has a defensible note.

## Example Prompts

- `/lr4-step1-screening rebuild LR4 Step 1 from 04d_LR4/2. vosviewer/0.1a.Corpus_Merged-956 nos. v2.csv`
- `/lr4-step1-screening screen the LR4 corpus by title, keywords, and abstract only`
- `/lr4-step1-screening audit current G-H-I-J-K decisions and rebuild the Step-1 matrix`
