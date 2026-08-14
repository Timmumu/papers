# -*- coding: utf-8 -*-
"""Normalize step3_data.py tuple layout and repair atomic-note Step-3 sections.

Problem: 68 Batch-5 entries are stored as (P..AF, 'Endnote', AG) with the
source label at index 14 and the AG evidence at index 15, while the matrix
rebuild script and note append scripts expect (P..AF, AG, SRC).

Fix:
1. Regenerate scripts/step3_data.py with canonical tuples
   (P,Q,R,U,V,W,X,Z,AA,AB,AC,AD,AE,AF,AG[,SRC]) using repr() so the file is
   unambiguous. Batch comments preceding each entry are preserved.
2. Repair the last Step-3 section in the 75 atomic notes appended today
   (targets minus the first 9), rewriting them from normalized data.
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

import step3_data
S3 = step3_data.S3

# ---------- normalize tuples ----------
changed_swap, changed_append = [], []
for n, v in list(S3.items()):
    if len(v) == 16:
        # stored as (P..AF, 'Endnote', AG) -> canonical (P..AF, AG, 'Endnote')
        if len(v[14]) < 40 and len(v[15]) > 40:
            v = v[:14] + (v[15], v[14])
            S3[n] = v
            changed_swap.append(n)
        else:
            # already canonical (AG short + source long is impossible) - keep
            pass
    elif len(v) == 15 and n in (72, 76):
        S3[n] = v + ('Endnote',)
        changed_append.append(n)

print('swapped:', len(changed_swap))
print('appended source:', changed_append)

# sanity: all 16-elem entries now have short source at index 15
bad = [n for n, v in S3.items() if len(v) > 15 and len(v[15]) > 60]
print('still-bad 16-elem:', bad)

# ---------- regenerate data file ----------
src = open(DATA, encoding='utf-8').read()
comment_of = {}
for m in re.finditer(r'^(#(?:[^\n]*\n)#?[^\n]*?)\n?S3\[(\d+)\]', src, re.M):
    pass
# simpler: for each entry find preceding comment line(s) in original text
for n in S3:
    m = re.search(r'\n([ \t]*#(?:[^\n]*))\nS3\[%d\]' % n, src)
    if m:
        comment_of[n] = m.group(1)

header = '''"""Step-3 deep-read codes for included papers.

Keyed by paper index n (1-429). Value tuple:
(P, Q, R, U-Tier, V, W, X, Z-DfX, AA-selfimprove, AB-method, AC-modality,
 AD-validation, AE-QA, AF-cluster, AG-key evidence[, SRC-fulltext-source])

Only papers with P=Q=R=Yes get full codes. Otherwise P/Q/R recorded, rest blank.
16th element (optional) = full-text source label, e.g. 'Endnote'.
"""
S3 = {}
'''
lines = [header]
for n in sorted(S3):
    if n in comment_of:
        lines.append(comment_of[n])
    lines.append('S3[%d] = (%s)' % (n, ', '.join(repr(x) for x in S3[n])))
    lines.append('')
open(DATA, 'w', encoding='utf-8').write('\n'.join(lines))
print('data file regenerated,', len(S3), 'entries')

import importlib
importlib.reload(step3_data)
S3 = step3_data.S3

# ---------- repair the 75 notes ----------
from screening_data import S

def tier_short(t):
    if 'Tier 1' in t: return 'Tier 1 - Digital Model (static, no live data)'
    if 'Tier 2' in t: return 'Tier 2 - Digital Shadow (one-way physical to virtual)'
    if 'Tier 3' in t: return 'Tier 3 - Digital Twin (bidirectional, two-way)'
    if 'Tier 4' in t: return 'Tier 4 - Cognitive / Self-improving'
    return 'Unclear'

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
        srcline = '\n(full-text source: %s)' % SRC
    elif 'Full-text source' in AG:
        srcline = ''
    else:
        srcline = '\n(full-text source: Endnote)'
    if P == 'Yes' and Q == 'Yes' and R == 'Yes':
        tier, V, W, X, Z, AA, AB, AC, AD, AE, AF = v[3:14]
        sec = ("## Step-3 Deep-Read Coding (Prompt B)\n\n"
               "| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |\n"
               "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|\n"
               "| %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |\n\n"
               "**Key evidence (AG):** %s%s\n"
               % (P, Q, R, tier_short(tier), V, W, X, Z, AA, AB, AC, AD, AE, AF, AG, srcline))
    else:
        sec = ("## Step-3 Deep-Read Coding (Prompt B)\n\n"
               "**Stage-2 exclusion:** P=%s, Q=%s, R=%s. %s%s\n"
               % (P, Q, R, AG, srcline))
    text = open(path, encoding='utf-8').read()
    idx = text.rfind('## Step-3 Deep-Read Coding')
    if idx == -1:
        print('!! no step3 section in note', slug)
        skipped.append(slug)
        continue
    text = text[:idx] + sec
    open(path, 'w', encoding='utf-8').write(text)
    repaired.append(slug)

print('repaired notes: %d | skipped: %s' % (len(repaired), skipped))
