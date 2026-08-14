# -*- coding: utf-8 -*-
"""Rebuild the matrix Step-3 table from scratch using step3_data.py.

The current matrix Step-3 table is corrupted (batch-4 insert was lost and
batch-5 insert used a wrong anchor). This script replaces the entire Step-3
table with a clean rebuild from step3_data.py, preserving the Step-1 table
and included-papers list above it.
"""
import os, re, sys
sys.path.insert(0, r'h:\phd\6.pjt\LR1\papers\scripts')
from step3_data import S3
from screening_data import S

MAT = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\SLR summary matrix.md'
RIS = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\429 papers.txt'

# rid lookup
txt = open(RIS, encoding='utf-8', errors='replace').read()
recs = re.split(r'\nER  -\s*\n', txt)
rid_of = {}
n = 0
for r in recs:
    if 'TY  -' not in r:
        continue
    n += 1
    m = re.search(r'^ID  - (.*?)$', r, re.M)
    rid_of[n] = m.group(1).strip() if m else ''

def tier_short(t):
    if 'Tier 1' in t: return 'Tier 1 - Digital Model (static, no live data)'
    if 'Tier 2' in t: return 'Tier 2 - Digital Shadow (one-way physical to virtual)'
    if 'Tier 3' in t: return 'Tier 3 - Digital Twin (bidirectional, two-way)'
    if 'Tier 4' in t: return 'Tier 4 - Cognitive / Self-improving'
    return 'Unclear'

mat = open(MAT, encoding='utf-8').read()
lines = mat.splitlines()

# find Step-3 heading
step3_idx = next(i for i, l in enumerate(lines) if l.startswith('## Step 3 Deep-Read Coding'))
# keep everything before Step-3 heading
before = lines[:step3_idx + 1]

# build new Step-3 table
header = '| ID   | P   | Q   | R   | U Tier                                                | V   | W   | X   | Z                       | AA             | AB                                          | AC                             | AD                   | AE  | AF                               | AG                                                                                                                                                                                                                                                    |'
sep =    '| ---- | --- | --- | --- | ----------------------------------------------------- | --- | --- | --- | ----------------------- | -------------- | ------------------------------------------- | ------------------------------ | -------------------- | --- | -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |'

rows = []
for n in sorted(S3.keys()):
    v = S3[n]
    rid = rid_of[n]
    P, Q, R, tier, V, W, X, Z, AA, AB, AC, AD, AE, AF, AG = v[:15]
    SRC = v[15] if len(v) > 15 else ''
    ag_with_src = (AG + f' [Full-text source: {SRC}]') if SRC else AG
    rows.append('| %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |' % (
        rid, P, Q, R, tier_short(tier), V, W, X, Z, AA, AB, AC, AD, AE, AF, ag_with_src))

new_step3 = [header, sep] + rows
new_lines = before + new_step3

open(MAT, 'w', encoding='utf-8').write('\n'.join(new_lines))
print(f'Rebuilt Step-3 table: {len(rows)} rows')
print(f'Total lines now: {len(new_lines)}')
