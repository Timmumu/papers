# -*- coding: utf-8 -*-
"""Append fusion-depth lines to atomic notes for papers already coded in step3_fusion."""
import os, sys
sys.path.insert(0, r'h:\phd\6.pjt\LR1\papers\scripts')
import step3_fusion
from screening_data import S

OUT = r'h:\phd\6.pjt\LR1\papers\01_source_3rd_SLR'
FD = step3_fusion.FD

updated, skipped = [], []
for n in sorted(FD):
    p = os.path.join(OUT, S[n][7] + '.md')
    if not os.path.exists(p):
        print('!! missing note', S[n][7])
        skipped.append(n)
        continue
    t = open(p, encoding='utf-8').read()
    if 'Fusion depth (AC1)' in t:
        skipped.append(n)
        continue
    i = t.rfind('## Step-3')
    if i == -1:
        print('!! no step3 section', S[n][7])
        skipped.append(n)
        continue
    seg = t[i:]
    insert = ('\n\n**Fusion depth (AC1):** %s\n\n**Fusion evidence (AC2):** %s\n\n**Confidence (AC3):** %s\n'
              % (FD[n], step3_fusion.FDEV[n], step3_fusion.FDCF[n]))
    j = seg.find('(full-text source:')
    if j == -1:
        j = seg.find('Source: Endnote library')
    if j == -1:
        seg = seg.rstrip() + insert
    else:
        seg = seg[:j] + insert + seg[j:]
    open(p, 'w', encoding='utf-8').write(t[:i] + seg)
    updated.append(n)
print('notes updated:', updated)
print('skipped:', skipped)
