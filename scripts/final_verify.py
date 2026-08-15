# -*- coding: utf-8 -*-
"""Final verification: data file, atomic notes, matrix consistency + tallies."""
import os, re, sys
sys.path.insert(0, r'h:\phd\6.pjt\LR1\papers\scripts')
import step3_data
from screening_data import S
from collections import Counter

S3 = step3_data.S3
OUT = r'h:\phd\6.pjt\LR1\papers\01_source_3rd_SLR'
MAT = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\SLR summary matrix.md'

print('=== DATA ===')
print('S3 entries:', len(S3))
print('bad lengths:', [n for n, v in S3.items() if len(v) not in (15, 16)])
print('without SRC:', [n for n, v in S3.items() if len(v) < 16])
print('SRC labels:', dict(Counter(v[15] for v in S3.values() if len(v) > 15)))

print()
print('=== NOTES ===')
nohave = [(n, S[n][7]) for n in sorted(S3)
          if not os.path.exists(os.path.join(OUT, S[n][7] + '.md'))
          or '## Step-3' not in open(os.path.join(OUT, S[n][7] + '.md'), encoding='utf-8').read()]
print('notes missing step3 section:', nohave)

print()
print('=== MATRIX ===')
t = open(MAT, encoding='utf-8').read()
lines = t.splitlines()
i1 = next(i for i, l in enumerate(lines) if l.startswith('## Step 1'))
i2 = next(i for i, l in enumerate(lines) if l.startswith('## Included'))
i3 = next(i for i, l in enumerate(lines) if l.startswith('## Step 3'))
print('step1 rows:', len([l for l in lines[i1:i2] if re.match(r'^\|\s*\d{1,4}\s*\|', l)]))
step3 = t[i3:] if False else '\n'.join(lines[i3:])
rows = [l for l in lines[i3:] if re.match(r'^\| \d{4} \|', l)]
print('step3 rows:', len(rows))
print('step3 rows without source mark:', sum(1 for l in rows if '[Full-text source:' not in l))

print()
print('=== TALLIES ===')
full = [n for n, v in S3.items() if v[0] == 'Yes' and v[1] == 'Yes' and v[2] == 'Yes']
excl = [n for n in S3 if n not in full]
print('full-coded:', len(full), '| stage2-excluded:', len(excl))
print('tiers:', dict(Counter(S3[n][3] for n in full)))
print('AA:', dict(Counter(S3[n][8] for n in full)))
print('Z:', dict(Counter(S3[n][7] for n in full)))
print('V/W/X sums:', sum(S3[n][4] for n in full), sum(S3[n][5] for n in full), sum(S3[n][6] for n in full))
print('excluded reasons (P/Q/R):', dict(Counter(('P' if S3[n][0] != 'Yes' else '') + ('Q' if S3[n][1] != 'Yes' else '') + ('R' if S3[n][2] != 'Yes' else '') for n in excl)))
