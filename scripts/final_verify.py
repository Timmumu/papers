# -*- coding: utf-8 -*-
"""Final verification: data file, atomic notes, matrix consistency + tallies."""
import os, re, sys
sys.path.insert(0, r'h:\phd\6.pjt\LR1\papers\scripts')
import step3_data, step3_extra
from screening_data import S
from collections import Counter

S3 = step3_data.S3
AH, AI = step3_extra.AH, step3_extra.AI
OUT = r'h:\phd\6.pjt\LR1\papers\01_source_3rd_SLR'
MAT1 = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\SLR summary matrix step 1.md'
MAT3 = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\SLR summary matrix step 3.md'

print('=== DATA ===')
print('S3 entries:', len(S3))
print('bad lengths:', [n for n, v in S3.items() if len(v) not in (15, 16)])
print('without SRC:', [n for n, v in S3.items() if len(v) < 16])
print('SRC labels:', dict(Counter(v[15] for v in S3.values() if len(v) > 15)))
full = [n for n, v in S3.items() if v[0] == 'Yes' and v[1] == 'Yes' and v[2] == 'Yes']
print('AH entries:', len(AH), '| AI entries:', len(AI))
print('full-coded missing AH/AI:', [n for n in full if n not in AH or n not in AI])
empty = [(n, 'AH' if not AH[n].strip() else 'AI') for n in full if not AH[n].strip() or not AI[n].strip()]
print('empty AH/AI:', empty)

print()
print('=== NOTES ===')
nohave = [(n, S[n][7]) for n in sorted(S3)
          if not os.path.exists(os.path.join(OUT, S[n][7] + '.md'))
          or '## Step-3' not in open(os.path.join(OUT, S[n][7] + '.md'), encoding='utf-8').read()]
print('notes missing step3 section:', nohave)

print()
print('=== MATRIX (split files) ===')
t1 = open(MAT1, encoding='utf-8').read()
rows1 = [l for l in t1.splitlines() if re.match(r'^\| \d{4} \|', l)]
print('step1 file rows:', len(rows1))
step1_noyear = 0
step1_bad_doi = 0
for l in rows1:
    c = [x.strip() for x in l.strip().strip('|').split('|')]
    if len(c) != 13:
        step1_bad_doi += 1
        continue
    if not c[3]:
        step1_noyear += 1
    if not c[12]:
        step1_bad_doi += 1
print('step1 rows without year:', step1_noyear)
print('step1 rows with empty DOI cell:', step1_bad_doi)
t3 = open(MAT3, encoding='utf-8').read()
rows3 = [l for l in t3.splitlines() if re.match(r'^\| \d{4} \|', l)]
coded3 = [l for l in rows3 if re.match(r'^\| \d{4} \|.*?\| (Yes|No) \| (Yes|No) \| (Yes|No) \|', l)]
print('step3 file rows:', len(rows3), '| coded rows:', len(coded3))
print('step3 coded rows without source mark:', sum(1 for l in coded3 if '[Full-text source:' not in l))
# AH/AI columns present: every full-coded row must have non-empty AH and AI (cells 24/25)
nc = 0
s2_bad = []
fd_bad = []
doi_missing = []
doi_bad = []
for l in coded3:
    cells = [c.strip() for c in l.strip().strip('|').split('|')]
    if len(cells) != 27:
        print('!! column count anomaly:', cells[:4], len(cells))
        continue
    pqr = (cells[4], cells[5], cells[6])
    if pqr == ('Yes', 'Yes', 'Yes'):
        if len(cells[24]) < 30 or len(cells[25]) < 30:
            nc += 1
            print('!! thin AH/AI:', cells[0], len(cells[24]), len(cells[25]))
        if cells[7] != 'Include' or cells[8]:
            s2_bad.append((cells[0], 'include-row', cells[7], cells[8]))
        if not cells[17]:
            fd_bad.append((cells[0], 'missing AC1 fusion depth', ''))
        elif cells[17] not in ('Co-present', 'Aligned', 'Fused', 'SINGLE', 'Unclear'):
            fd_bad.append((cells[0], 'bad FD value', cells[17]))
        if cells[17] and not cells[18]:
            fd_bad.append((cells[0], 'FD without evidence', cells[17]))
        if cells[17] and cells[19] not in ('High', 'Medium', 'Low'):
            fd_bad.append((cells[0], 'bad confidence', cells[19]))
        if not cells[26]:
            doi_missing.append(cells[0])
        elif not re.match(r'^10\.\d', cells[26]):
            doi_bad.append((cells[0], cells[26][:40]))
    else:
        if cells[7] != 'Exclude' or not cells[8]:
            s2_bad.append((cells[0], 'exclude-row', cells[7], cells[8]))
print('full-coded rows with thin AH/AI cells:', nc)
print('Stage-2 decision/reason anomalies:', s2_bad)
print('fusion-depth anomalies:', fd_bad)
print('full-coded rows with empty DOI cell:', doi_missing)
print('full-coded rows with malformed DOI:', doi_bad)
print('step3 missing section present:', '## Included papers missing full text' in t3)

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
