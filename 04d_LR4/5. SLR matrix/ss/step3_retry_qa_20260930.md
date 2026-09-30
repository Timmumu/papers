# LR4 Step-3 Retry and QA Note - 2026-09-30

## Full-text retry

- Starting state: 31 non-verified Step-3 papers.
- Automated direct publisher PDF retry was run for all 31 non-verified rows.
- Direct retry result: 31 misses; no HTML/error page was accepted as PDF.
- Direct retry log: `direct_pdf_retry_20260930_223011.json`.
- Local EndNote index retry found one high-confidence DOI+title match: R330 Zhang2026f, DOI `10.1080/15732479.2026.2656943`.
- R330 PDF was staged in L1/L2, full text was extracted, coverage was updated to verified, and Step-3 coding was completed.

## Step-3 coding update

- Matrix rebuilt after R330 coding.
- Final Step-3 count: 214 coded rows = 200 full-coded + 14 Stage-2 excluded.
- Remaining non-verified coverage: 30 rows = 26 unverified + 4 no-candidate.

## QA sampling

Random/stratified QA checked recent browser-coded rows, a Stage-2 exclusion, earlier ported rows, and the newly recovered R330:

- Recent full-coded: R487, R536, R671, R746, R869, R918.
- Stage-2 exclude: R477.
- Earlier/ported examples: R008, R057, R089.
- Newly recovered: R330.

Result: sampled coding fields were consistent with the available full-text extracts or paper evidence. No systematic coding defect was found, so checking was not expanded.

## Validation

- `scripts/validate_lr4_step3.py`: `coded=214 full=200 stage2-excl=14`, `VALIDATION OK`.
- `04d_LR4/SLR summary matrix step 3.md` header confirms 214 coded papers.