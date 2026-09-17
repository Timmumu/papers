# -*- coding: utf-8 -*-
"""Append Step-3 sections (coding table + fusion + AH/AI) to the LR4 per-paper
notes in 01_source_4th_SLR/. Reads the authoritative stores.

Usage: .venv\\Scripts\\python.exe scripts/append_step3_lr4_notes.py
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SS = os.path.join(ROOT, '04d_LR4', '5. SLR matrix', 'ss')
NOTES = os.path.join(ROOT, '01_source_4th_SLR')
sys.path.insert(0, os.path.join(ROOT, 'scripts'))

import step3_lr4_data, step3_lr4_extra, step3_lr4_fusion
from screening_data_lr4 import S4, decision

S3L = step3_lr4_data.S3L
AH = step3_lr4_extra.AH
AI = step3_lr4_extra.AI
FD = step3_lr4_fusion.FD
FDEV = step3_lr4_fusion.FDEV
FDCF = step3_lr4_fusion.FDCF

with open(os.path.join(SS, 'corpus_lr4.json'), encoding='utf-8') as f:
    CORPUS = json.load(f)
BYROW = {rec['row']: rec for rec in CORPUS}

INCLUDED = sorted(r for r, t in S4.items() if decision(t[:5]) == 'Include')

def note_path(r):
    return os.path.join(NOTES, BYROW[r]['slug'] + '.md')

for r in INCLUDED:
    if r not in S3L:
        continue
    v = S3L[r]
    P, Q, R = v[0], v[1], v[2]
    full = (P == 'Yes' and Q == 'Yes' and R == 'Yes')
    src = v[15] if len(v) > 15 else ''
    L = []
    L.append('')
    L.append('## Step-3 Deep-Read Coding (Prompt B)')
    L.append('| P DT-subject | Q DfS/DfQ | R codable | U Tier | V Design | W Constr | X Oper | Z DfX | AA Self-improve | AB Methodology | AC Modality | AD Validation | AE QA(0-5) | AF Cluster |')
    L.append('|---|---|---|---|---|---|---|---|---|---|---|---|---|---|')
    if full:
        L.append('| %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |' % (
            P, Q, R, v[3], v[4], v[5], v[6], v[7], v[8], v[9], v[10], v[11], v[12], v[13]))
        if r in FD:
            L.append('')
            L.append('| AC1 fusion depth | AC2 fusion evidence | AC3 confidence |')
            L.append('|---|---|---|')
            L.append('| %s | %s | %s |' % (FD[r], FDEV[r], FDCF[r]))
    else:
        L.append('| %s | %s | %s | Stage-2 Exclude |  |  |  |  |  |  |  |  |  |  |' % (P, Q, R))
    L.append('')
    L.append('**Key evidence (AG):** %s' % v[14])
    if src:
        L.append('')
        L.append('*Full-text source: %s*' % src)
    if full:
        if r in AH:
            L.append('')
            L.append('**AH — strength & gap filled:** %s' % AH[r])
        if r in AI:
            L.append('')
            L.append('**AI — deficiencies & future work:** %s' % AI[r])
    L.append('')

    p = note_path(r)
    txt = open(p, encoding='utf-8').read()
    if '## Step-3 Deep-Read Coding (Prompt B)' in txt:
        txt = re.split(r'\n## Step-3 Deep-Read Coding \(Prompt B\)', txt)[0].rstrip()
    open(p, 'w', encoding='utf-8').write(txt + '\n' + '\n'.join(L))

print('notes updated for %d coded rows' % len(S3L))
