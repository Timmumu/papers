# -*- coding: utf-8 -*-
"""Code S3[106] Guo2025-quality (real full paper now available via Endnote)."""
import os, re, sys
sys.path.insert(0, r'h:\phd\6.pjt\LR1\papers\scripts')
DATA = r'h:\phd\6.pjt\LR1\papers\scripts\step3_data.py'
OUT = r'h:\phd\6.pjt\LR1\papers\01_source_3rd_SLR'

import step3_data
from screening_data import S
S3 = step3_data.S3

S3[106] = ('Yes','Yes','Yes','Tier 2 - Digital Shadow (one-way physical to virtual)',0,0,1,
    'Design for Quality (DfQ)','None','Digital Twin platform (no machine learning)',
    'Multi (two or more data types)','Single case study',4,'BIM-to-Digital-Twin architecture',
    'Sky-space-ground integrated remote sensing monitoring DT framework for multi-source Data-BIM integration in residential quality monitoring (Beijing U Civil Eng & Arch, J Building Eng 2025): RBIM (residential building information model) aggregates full-lifecycle project data; SSIoT (surveying sensors + IoT) links physical things to cyberspace; multi-sensor monitoring (monitoring LiDAR, automated monitoring robots, GNSS, drones) with BIM collaborative multi-source data fusion; cloud platform unifies data processing/storage avoiding information islands; experiments: 8-phase LiDAR monitoring of a frame building tracking target-sphere centre displacement to assess building deformation trends, accuracy verification of self-developed LSIIS centre-extraction algorithm vs PCL/ICP/WTLS (Faro + Livox LiDAR), building settlement monitoring analysis with BIM-sensor linkage. One-way monitoring to DT platform for O&M quality management; no actuation, no learning loop.',
    'Endnote')

# regenerate data file (canonical repr form, preserving comments)
src = open(DATA, encoding='utf-8').read()
comment_of = {}
for n in S3:
    m = re.search(r'\n([ \t]*#(?:[^\n]*))\nS3\[%d\]' % n, src)
    if m:
        comment_of[n] = m.group(1)
if 106 not in comment_of:
    comment_of[106] = '# Batch 7 - Endnote upload (Guo2025-quality full paper)'

header = '''"""Step-3 deep-read codes for included papers.

Keyed by paper index n (1-429). Value tuple:
(P, Q, R, U-Tier, V, W, X, Z-DfX, AA-selfimprove, AB-method, AC-modality,
 AD-validation, AE-QA, AF-cluster, AG-key evidence[, SRC-fulltext-source])

Only papers with P=Q=R=Yes get full codes. Otherwise P/Q/R recorded, rest blank.
16th element (optional) = full-text source label (e.g. 'Endnote').
"""
S3 = {}
'''
lines = [header]
for n in sorted(S3):
    lines.append(comment_of.get(n, '# Batch'))
    lines.append('S3[%d] = (%s)' % (n, ', '.join(repr(x) for x in S3[n])))
    lines.append('')
open(DATA, 'w', encoding='utf-8').write('\n'.join(lines))
print('data file regenerated:', len(S3), 'entries')

import importlib
importlib.reload(step3_data)
S3 = step3_data.S3
print('bad lengths:', [n for n, v in S3.items() if len(v) not in (15, 16)])

# note
slug = S[106][7]
v = S3[106]
P, Q, R = v[0], v[1], v[2]
AG, SRC = v[14], v[15]
tier, V, W, X, Z, AA, AB, AC, AD, AE, AF = v[3:14]
sec = ("## Step-3 Deep-Read Coding (Prompt B)\n\n"
       "| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |\n"
       "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|\n"
       "| %s | %s | %s | Tier 2 - Digital Shadow (one-way physical to virtual) | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |\n\n"
       "**Key evidence (AG):** %s\n\n(full-text source: %s)\n"
       % (P, Q, R, V, W, X, Z, AA, AB, AC, AD, AE, AF, AG, SRC))
path = os.path.join(OUT, slug + '.md')
t = open(path, encoding='utf-8').read()
if '## Step-3 Deep-Read Coding' in t:
    idx = t.rfind('## Step-3')
    t = t[:idx] + sec
else:
    t = t.rstrip() + '\n\n' + sec
open(path, 'w', encoding='utf-8').write(t)
print('note updated:', slug)
