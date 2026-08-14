# -*- coding: utf-8 -*-
"""Append Step-3 sections to atomic notes for Batch-5 papers coded AFTER the
initial 9 (which were already appended). Then the matrix is rebuilt separately.
"""
import os, re, sys
sys.path.insert(0, r'h:\phd\6.pjt\LR1\papers\scripts')
from step3_data import S3
from screening_data import S

OUT = r'h:\phd\6.pjt\LR1\papers\01_source_3rd_SLR'

# Already appended in the first batch-5 run:
ALREADY = {15, 23, 35, 46, 47, 61, 65, 67, 68}

# All batch-5 target indices
ALL = [15,23,35,46,47,61,65,67,68,72,76,78,84,88,97,102,104,111,112,118,128,129,
       137,141,144,148,154,167,168,183,203,205,207,210,211,221,225,226,238,239,
       255,256,273,278,283,292,294,297,298,300,308,318,320,321,322,324,333,335,
       340,343,349,357,358,359,360,366,368,372,379,382,386,388,393,396,404,405,
       409,411,413,416,418,421,426,429]

TODO = [n for n in ALL if n not in ALREADY]

def tier_short(t):
    if 'Tier 1' in t: return 'Tier 1 - Digital Model (static, no live data)'
    if 'Tier 2' in t: return 'Tier 2 - Digital Shadow (one-way physical to virtual)'
    if 'Tier 3' in t: return 'Tier 3 - Digital Twin (bidirectional, two-way)'
    if 'Tier 4' in t: return 'Tier 4 - Cognitive / Self-improving'
    return 'Unclear'

updated, missing = [], []
for n in TODO:
    slug = S[n][7]
    path = os.path.join(OUT, slug + '.md')
    if not os.path.exists(path):
        print('!! missing note', slug)
        missing.append(slug)
        continue
    v = S3[n]
    P, Q, R = v[0], v[1], v[2]
    if P == 'Yes' and Q == 'Yes' and R == 'Yes':
        tier, V, W, X, Z, AA, AB, AC, AD, AE, AF, AG = v[3:15]
        sec = f"""
## Step-3 Deep-Read Coding (Prompt B) — full text verified via Endnote library (front-matter DOI/title match)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| {P} | {Q} | {R} | {tier_short(tier)} | {V} | {W} | {X} | {Z} | {AA} | {AB} | {AC} | {AD} | {AE} | {AF} |

**Key evidence (AG):** {AG}
"""
    else:
        AG = v[14]
        sec = f"""
## Step-3 Deep-Read Coding (Prompt B) — full text verified via Endnote library (front-matter DOI/title match)

**Stage-2 exclusion:** P={P}, Q={Q}, R={R}. {AG}
"""
    open(path, 'a', encoding='utf-8').write(sec)
    updated.append(slug)

print(f'updated: {len(updated)} | missing: {missing}')
