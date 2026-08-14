# -*- coding: utf-8 -*-
"""Append Step-3 deep-read sections to atomic notes for the 38 newly coded papers.
Source: full text verified via Endnote library (front-matter DOI/title match, coverage re-scan 2026-08-12).
"""
import os, sys
sys.path.insert(0, r'h:\phd\6.pjt\LR1\papers\scripts')
from step3_data import S3
from screening_data import S

OUT = r'h:\phd\6.pjt\LR1\papers\01_source_3rd_SLR'

# indices of the 38 newly coded papers
NEW = [24, 28, 44, 109, 110, 138, 143, 155, 158, 162, 163, 176, 181, 185, 194,
       195, 196, 204, 208, 235, 247, 254, 260, 277, 302, 313, 329, 332, 347, 361,
       377, 398, 401, 408, 414, 420, 427, 428]

def tier_short(t):
    if 'Tier 1' in t:
        return 'Tier 1 - Digital Model'
    if 'Tier 2' in t:
        return 'Tier 2 - Digital Shadow'
    if 'Tier 3' in t:
        return 'Tier 3 - Digital Twin (bidirectional)'
    if 'Tier 4' in t:
        return 'Tier 4 - Cognitive'
    return 'Unclear'

updated, missing = [], []
for n in NEW:
    slug = S[n][7]
    path = os.path.join(OUT, slug + '.md')
    if not os.path.exists(path):
        print('!! missing note', slug)
        missing.append(slug)
        continue
    v = S3[n]
    P, Q, R, tier, V, W, X, Z, AA, AB, AC, AD, AE, AF, AG = v
    if P == 'Yes' and Q == 'Yes' and R == 'Yes':
        sec = f"""
## Step-3 Deep-Read Coding (Prompt B) — full text verified via Endnote library (front-matter DOI/title match, coverage re-scan 2026-08-12)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| {P} | {Q} | {R} | {tier_short(tier)} | {V} | {W} | {X} | {Z} | {AA} | {AB} | {AC} | {AD} | {AE} | {AF} |

**Key evidence (AG):** {AG}
"""
    else:
        sec = f"""
## Step-3 Deep-Read Coding (Prompt B) — full text verified via Endnote library (front-matter DOI/title match, coverage re-scan 2026-08-12)

**Stage-2 exclusion:** P={P}, Q={Q}, R={R}. {AG}
"""
    open(path, 'a', encoding='utf-8').write(sec)
    updated.append(slug)
    print('updated', slug)

print('\nupdated:', len(updated), '| missing:', missing)
