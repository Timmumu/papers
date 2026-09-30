---
name: lr4-step3-deep-read
description: 'Run only LR4 Step 3 deep reading for 04d_LR4. Use when asked to study verified fulltext papers one by one, continue LR4 coding from full texts, validate or rebuild SLR summary matrix step 3, or finish Step 3 without rerunning Step 1.'
argument-hint: '[LR4 folder or verified-fulltext subset]'
user-invocable: true
---

# LR4 Step 3 Deep Read

## Purpose

Use this skill when the user wants only the full-text coding phase of LR4.

This skill assumes Step 1 has already been completed and that verified full-text coverage is already available or will be checked before coding begins.

## Default Targets

- Coverage store: `04d_LR4/5. SLR matrix/ss/coverage_lr4.json`
- Step-3 matrix: `04d_LR4/SLR summary matrix step 3.md`
- LR4 Step-3 code stores: `scripts/step3_lr4_data.py`, `scripts/step3_lr4_extra.py`, `scripts/step3_lr4_fusion.py`

## When To Use

- User asks to do only Step 3.
- User wants detailed full-text study one paper at a time.
- User wants to continue LR4 coding from verified PDFs and TXT extracts.
- User wants to validate or rebuild `SLR summary matrix step 3.md` without rerunning Step 1.

## Core Rules

- Do not rerun Step 1 unless the user explicitly asks.
- Use only verified full-text papers as coding input.
- Apply the frozen Prompt B logic from `04c_LR 3round/2 stage PRISMA guideline.md`.
- Code only what is explicitly evidenced in the full text.
- Update only the consolidated Step-3 matrix outputs by default; do not backfill per-paper notes unless requested.

## Primary Assets

- `./scripts/rebuild_lr4_step3.py`
- `./scripts/validate_lr4_step3.py`
- `./scripts/make_lr4_code_extracts.py`
- `./scripts/peek_lr4.py`
- `./scripts/append_step3_lr4_notes.py`
- `04c_LR 3round/2 stage PRISMA guideline.md`

## Procedure

### 1. Confirm Step-3 Inputs

1. Confirm Step 1 and verified full-text coverage already exist.
2. Use `coverage_lr4.json` to determine which papers are verified, unverified, or missing.
3. Exclude unverified and missing-fulltext papers from Step-3 coding unless the user explicitly asks to resolve coverage first.

### 2. Code Verified Full Texts

1. Read the actual full text paper by paper.
2. Apply the Prompt B Stage-2 confirmation and deep-read coding scheme.
3. Store results in `step3_lr4_data.py`, `step3_lr4_extra.py`, and `step3_lr4_fusion.py`.
4. Use `./scripts/make_lr4_code_extracts.py` and `./scripts/peek_lr4.py` for extracts and spot checks.

### 3. Rebuild And Validate

1. Rebuild the consolidated Step-3 matrix with `./scripts/rebuild_lr4_step3.py`.
2. Validate consistency with `./scripts/validate_lr4_step3.py`.
3. Keep matrix-only updates as the default output.
4. Use `./scripts/append_step3_lr4_notes.py` only if the user explicitly asks for note-level backfill.

## Deliverables

- `04d_LR4/SLR summary matrix step 3.md`
- updated LR4 Step-3 authoritative coding modules

## Completion Gate

Step 3 is complete only when all intended verified full-text papers are coded, the matrix rebuild succeeds, and `validate_lr4_step3.py` passes.

## Example Prompts

- `/lr4-step3-deep-read continue LR4 Step 3 from verified full texts only`
- `/lr4-step3-deep-read rebuild and validate 04d_LR4/SLR summary matrix step 3.md`
- `/lr4-step3-deep-read code the remaining verified LR4 full texts one by one`
