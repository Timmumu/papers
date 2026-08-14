# -*- coding: utf-8 -*-
"""Normalize step3_data.py tuple layout and repair atomic-note Step-3 sections.

Problem found: 68 Batch-5 entries are stored as (P..AF, 'Endnote', AG) with
source at index 14 and AG at 15, while the matrix rebuild script and the note
append scripts expect (P..AF, AG, SRC). The matrix/notes currently show
'Endnote' where the evidence text should be.

This script:
1. Rewrites step3_data.py: for those 68 entries swap v[14] and v[15] so layout
   becomes (P..AF, AG, 'Endnote'). Also appends 'Endnote' as 16th element for
   entries 72, 76 (currently len-15 without any source mark).
2. Repairs the last 'Step-3 Deep-Read Coding' section in the 75 atomic notes
   appended today (targets minus the first 9), rewriting it from the
   normalized data with correct AG and an explicit full-text source line.
"""
import os, re, sys
sys.path.insert(0, r'h:\phd\6.pjt\LR1\papers\scripts')

DATA = r'h:\phd\6.pjt\LR1\papers\scripts\step3_data.py'
OUT = r'h:\phd\6.pjt\LR1\papers\01_source_3rd_SLR'

FIRST9 = {15, 23, 35, 46, 47, 61, 65, 67, 68}
ALL = [15,23,35,46,47,61,65,67,68,72,76,78,84,88,97,102,104,111,112,118,128,129,
       137,141,144,148,154,167,168,183,203,205,207,210,211,221,225,226,238,239,
       255,256,273,278,283,292,294,297,298,300,308,318,320,321,322,324,333,335,
       340,343,349,357,358,359,360,366,368,372,379,382,386,388,393,396,404,405,
       409,411,413,416,418,421,426,429]

def tier_short(t):
    if 'Tier 1' in t: return 'Tier 1 - Digital Model (static, no live data)'
    if 'Tier 2' in t: return 'Tier 2 - Digital Shadow (one-way physical to virtual)'
    if 'Tier 3' in t: return 'Tier 3 - Digital Twin (bidirectional, two-way)'
    if 'Tier 4' in t: return 'Tier 4 - Cognitive / Self-improving'
    return 'Unclear'

# ---- 1. normalize step3_data.py -------------------------------------------
src = open(DATA, encoding='utf-8').read()
for n in ALL:
    if n in FIRST9:
        continue  # len-15 with inline source in AG already; leave
    pat = re.compile(r"(S3\[%d\] = \(.*?\n'(?:[^']|\\')*'\))" % n, re.S)
    m = pat.search(src)
    if not m:
        print('!! entry not found', n)
        continue
    block = m.group(0)
    # extract last two single-quoted strings
    strs = re.findall(r"'(?:[^'\\]|\\.)*'", block)
    if len(strs) < 2:
        print('!! bad block', n)
        continue
    # check layout: is second-to-last string 'Endnote' (source first)?
    if strs[-2] == "'Endnote'":
        new_block = block[:block.rfind(strs[-2])] + strs[-1] + ', ' + "'Endnote')"
        # trim the old final "', 'Endnote')" tail: simpler - rebuild explicitly
        prefix = block[:block.rfind(strs[-2])]
        new_block = prefix + strs[-1] + ', ' + "'Endnote')"
        src = src.replace(block, new_block, 1)
        print('swapped', n)
    else:
        print('skip (already ordered?)', n, strs[-2][:40])
open(DATA, 'w', encoding='utf-8').write(src)

import importlib
import step3_data
importlib.reload(step3_data)
S3 = step3_data.S3

# append missing source for 72, 76
for n in [72, 76]:
    v = S3[n]
    if len(v) == 15:
        src = open(DATA, encoding='utf-8').read()
        pat = re.compile(r"(S3\[%d\] = \(.*?\n'(?:[^']|\\')*'\))" % n, re.S)
        m = pat.search(src)
        block = m.group(0)
        new_block = block[:-1] + ", 'Endnote')"
        src = src.replace(block, new_block, 1)
        open(DATA, 'w', encoding='utf-8').write(src)
        print('src added', n)

importlib.reload(step3_data)
S3 = step3_data.S3

# ---- 2. repair the 75 atomic notes ----------------------------------------
from screening_data import S
TODO = [n for n in ALL if n not in FIRST9]
repaired, skipped = [], []
for n in TODO:
    slug = S[n][7]
    path = os.path.join(OUT, slug + '.md')
    if not os.path.exists(path):
        print('!! missing note', slug)
        skipped.append(slug)
        continue
    v = S3[n]
    P, Q, R = v[0], v[1], v[2]
    AG = v[14]
    SRC = v[15] if len(v) > 15 else ''
    if SRC:
        srcline = f'\n(full-text source: {SRC})'
    elif 'Full-text source' in AG:
        srcline = ''  # AG already carries the source mark inline
    else:
        srcline = '\n(full-text source: Endnote)'
    if P == 'Yes' and Q == 'Yes' and R == 'Yes':
        tier, V, W, X, Z, AA, AB, AC, AD, AE, AF = v[3:14]
        sec = f"""## Step-3 Deep-Read Coding (Prompt B)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| {P} | {Q} | {R} | {tier_short(tier)} | {V} | {W} | {X} | {Z} | {AA} | {AB} | {AC} | {AD} | {AE} | {AF} |

**Key evidence (AG):** {AG}
{srcline}"""
    else:
        sec = f"""## Step-3 Deep-Read Coding (Prompt B)

**Stage-2 exclusion:** P={P}, Q={Q}, R={R}. {AG}
{srcline}"""
    text = open(path, encoding='utf-8').read()
    # find LAST Step-3 section heading
    idx = text.rfind('## Step-3 Deep-Read Coding')
    if idx == -1:
        print('!! no step3 section in note', slug)
        skipped.append(slug)
        continue
    text = text[:idx] + sec + '\n'
    open(path, 'w', encoding='utf-8').write(text)
    repaired.append(slug)

print(f'repaired notes: {len(repaired)} | skipped: {len(skipped)}')
