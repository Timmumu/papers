# -*- coding: utf-8 -*-
"""Append Step-3 sections to atomic notes + insert matrix Step-3 rows for the
9 Batch-5 papers coded so far. Adds SOURCE column to the matrix Step-3 table.
"""
import os, re, sys
sys.path.insert(0, r'h:\phd\6.pjt\LR1\papers\scripts')
from step3_data import S3
from screening_data import S

OUT = r'h:\phd\6.pjt\LR1\papers\01_source_3rd_SLR'
MAT = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\SLR summary matrix.md'
RIS = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\429 papers.txt'

# the 9 Batch-5 papers coded so far
BATCH5 = [15, 23, 35, 46, 47, 61, 65, 67, 68]

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

# 1) append to atomic notes
print('=== atomic notes ===')
for n in BATCH5:
    slug = S[n][7]
    path = os.path.join(OUT, slug + '.md')
    if not os.path.exists(path):
        print('!! missing note', slug)
        continue
    v = S3[n]
    P, Q, R, tier, V, W, X, Z, AA, AB, AC, AD, AE, AF, AG = v[:15]
    SRC = v[15] if len(v) > 15 else ''
    src_line = f' (full-text source: {SRC})' if SRC else ''
    if P == 'Yes' and Q == 'Yes' and R == 'Yes':
        sec = f"""
## Step-3 Deep-Read Coding (Prompt B){src_line}

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| {P} | {Q} | {R} | {tier_short(tier)} | {V} | {W} | {X} | {Z} | {AA} | {AB} | {AC} | {AD} | {AE} | {AF} |

**Key evidence (AG):** {AG}
"""
    else:
        sec = f"""
## Step-3 Deep-Read Coding (Prompt B){src_line}

**Stage-2 exclusion:** P={P}, Q={Q}, R={R}. {AG}
"""
    open(path, 'a', encoding='utf-8').write(sec)
    print('updated', slug)

# 2) insert into matrix Step-3 table (anchor at Step-3 3906 row, after existing rows)
mat = open(MAT, encoding='utf-8').read()
lines = mat.splitlines()
step3_idx = next(i for i, l in enumerate(lines) if l.startswith('## Step 3 Deep-Read Coding'))
anchor = None
for k in range(step3_idx, len(lines)):
    if re.match(r'^\|\s*3906\s*\|', lines[k]):
        anchor = k
assert anchor is not None

# check if a SOURCE column header exists; if not, note it but don't restructure the table
header = lines[step3_idx + 2]
print('Step-3 header:', header[:80])

rows = []
for n in BATCH5:
    v = S3[n]
    rid = rid_of[n]
    P, Q, R, tier, V, W, X, Z, AA, AB, AC, AD, AE, AF, AG = v[:15]
    SRC = v[15] if len(v) > 15 else ''
    # append source into AG so it's visible without restructuring the table
    ag_with_src = (AG + f' [Full-text source: {SRC}]') if SRC else AG
    rows.append('| %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |' % (
        rid, P, Q, R, tier_short(tier), V, W, X, Z, AA, AB, AC, AD, AE, AF, ag_with_src))

insert_at = anchor + 1
new_lines = lines[:insert_at] + rows + lines[insert_at:]
open(MAT, 'w', encoding='utf-8').write('\n'.join(new_lines))
print(f'\ninserted {len(rows)} matrix rows after Step-3 row 3906')
