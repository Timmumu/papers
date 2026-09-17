# -*- coding: utf-8 -*-
"""Append AH/AI lines to the Step-3 sections of the 151 full-coded atomic notes."""
import os, sys
sys.path.insert(0, r'h:\phd\6.pjt\LR1\papers\scripts')
import step3_data, step3_extra
from screening_data import S

S3 = step3_data.S3
AH, AI = step3_extra.AH, step3_extra.AI
OUT = r'h:\phd\6.pjt\LR1\papers\01_source_3rd_SLR'

full = sorted(n for n, v in S3.items() if v[0] == 'Yes' and v[1] == 'Yes' and v[2] == 'Yes')
updated, skipped = [], []
for n in full:
    p = os.path.join(OUT, S[n][7] + '.md')
    if not os.path.exists(p):
        print('!! missing note', S[n][7])
        skipped.append(n)
        continue
    t = open(p, encoding='utf-8').read()
    if 'Strength & gap filled (AH)' in t:
        skipped.append(n)
        continue
    i = t.rfind('## Step-3')
    if i == -1:
        print('!! no step3 section', S[n][7])
        skipped.append(n)
        continue
    seg = t[i:]
    insert = '\n\n**Strength & gap filled (AH):** %s\n\n**Deficiencies & future work (AI):** %s\n' % (AH[n], AI[n])
    j = seg.find('(full-text source:')
    if j == -1:
        j = seg.find('Source: Endnote library')
    if j == -1:
        seg = seg.rstrip() + insert
    else:
        seg = seg[:j] + insert + seg[j:]
    t = t[:i] + seg
    open(p, 'w', encoding='utf-8').write(t)
    updated.append(n)
print('notes updated:', len(updated), '| skipped:', len(skipped))
