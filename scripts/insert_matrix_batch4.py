# -*- coding: utf-8 -*-
"""Insert the 38 newly-coded Batch-4 rows into the matrix Step-3 table.

IMPORTANT: anchors at the STEP-3 table's 3906 row (the row that starts with
'| 3906 | Yes | Yes | Yes | Unclear' and lives inside '## Step 3 Deep-Read
Coding'), NOT the first '| 3906 |' occurrence (that was the Batch-3 bug that
dropped rows into the Step-1 table).
"""
import os, re, sys
sys.path.insert(0, r'h:\phd\6.pjt\LR1\papers\scripts')
from step3_data import S3
from screening_data import S

MAT = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\SLR summary matrix.md'
NEW = [24, 28, 44, 109, 110, 138, 143, 155, 158, 162, 163, 176, 181, 185, 194,
       195, 196, 204, 208, 235, 247, 254, 260, 277, 302, 313, 329, 332, 347, 361,
       377, 398, 401, 408, 414, 420, 427, 428]

# map index -> rid
RIS = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\429 papers.txt'
txt = open(RIS, encoding='utf-8', errors='replace').read()
recs = re.split(r'\nER  -\s*\n', txt)
meta = {}
n = 0
for r in recs:
    if 'TY  -' not in r:
        continue
    n += 1
    m = re.search(r'^ID  - (.*?)$', r, re.M)
    meta[n] = m.group(1).strip() if m else ''

def tier_short(t):
    if 'Tier 1' in t:
        return 'Tier 1 - Digital Model (static, no live data)'
    if 'Tier 2' in t:
        return 'Tier 2 - Digital Shadow (one-way physical to virtual)'
    if 'Tier 3' in t:
        return 'Tier 3 - Digital Twin (bidirectional, two-way)'
    if 'Tier 4' in t:
        return 'Tier 4 - Cognitive / Self-improving'
    return 'Unclear'

mat = open(MAT, encoding='utf-8').read()
lines = mat.splitlines()

# Locate Step-3 table region
step3_idx = None
for i, l in enumerate(lines):
    if l.startswith('## Step 3 Deep-Read Coding'):
        step3_idx = i
        break
assert step3_idx is not None, 'Step-3 heading not found'

# Find the LAST Step-3 data row (3906) AFTER the heading
anchor = None
for k in range(step3_idx, len(lines)):
    if re.match(r'^\|\s*3906\s*\|', lines[k]):
        anchor = k
assert anchor is not None, 'Step-3 3906 row not found after heading'
print('Step-3 heading at line', step3_idx + 1)
print('Step-3 3906 anchor at line', anchor + 1)

rows = []
for n in NEW:
    v = S3[n]
    rid = meta[n]
    P, Q, R, tier, V, W, X, Z, AA, AB, AC, AD, AE, AF, AG = v
    if P == 'Yes' and Q == 'Yes' and R == 'Yes':
        rows.append('| %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |' % (
            rid, P, Q, R, tier_short(tier), V, W, X, Z, AA, AB, AC, AD, AE, AF, AG))
    else:
        rows.append('| %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |' % (
            rid, P, Q, R, tier_short(tier), V, W, X, Z, AA, AB, AC, AD, AE, AF, AG))

insert_at = anchor + 1
new_lines = lines[:insert_at] + rows + lines[insert_at:]

with open(MAT, 'w', encoding='utf-8') as f:
    f.write('\n'.join(new_lines))

print('Inserted', len(rows), 'rows after line', insert_at + 1)
print('Sample:', rows[0])
