# -*- coding: utf-8 -*-
"""v2: write/upgrade fusion-depth blocks (detailed FDN format) into atomic notes."""
import os, re, sys
sys.path.insert(0, r'h:\phd\6.pjt\LR1\papers\scripts')
import step3_fusion
from screening_data import S

OUT = r'h:\phd\6.pjt\LR1\papers\01_source_3rd_SLR'
FD = step3_fusion.FD
FDN = step3_fusion.FDN
FDEV = step3_fusion.FDEV
FDCF = step3_fusion.FDCF

OLD_BLOCK = re.compile(
    r'\*\*Fusion depth \(AC1\):\*\*.*?'
    r'(?P<cf>\*\*Confidence \(AC3\):\*\*[^\n]*)\n?',
    re.S)

updated, skipped, missing = [], [], []
for n in sorted(FD):
    slug = S[n][7]
    p = os.path.join(OUT, slug + '.md')
    if not os.path.exists(p):
        missing.append(n)
        print('!! missing note', n, slug)
        continue
    t = open(p, encoding='utf-8').read()
    # remove any existing fusion block (old or new format)
    t2, k = OLD_BLOCK.subn('', t)
    if n in FDN:
        block = FDN[n]
    else:
        block = ('**Fusion depth (AC1):** %s\n\n'
                 '**Fusion evidence (AC2):** %s\n\n'
                 '**Confidence (AC3):** %s\n' % (FD[n], FDEV[n], FDCF[n]))
    i = t2.rfind('## Step-3')
    if i == -1:
        skipped.append(n)
        print('!! no step3 section', n, slug)
        continue
    seg = t2[i:]
    j = seg.find('(full-text source:')
    if j == -1:
        j = seg.find('Source: Endnote library')
    if j == -1:
        seg = seg.rstrip() + '\n\n' + block
    else:
        seg = seg[:j] + block + '\n' + seg[j:]
    open(p, 'w', encoding='utf-8').write(t2[:i] + seg)
    updated.append(n)
print('updated:', len(updated))
print('missing notes:', missing)
print('skipped (no step3):', skipped)
