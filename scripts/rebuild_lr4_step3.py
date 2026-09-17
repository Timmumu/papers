# -*- coding: utf-8 -*-
"""Rebuild the LR4 Step-3 markdown (04d_LR4/SLR summary matrix step 3.md)
from step3_lr4_data.py (authoritative) + step3_lr4_extra.py + step3_lr4_fusion.py,
with corpus metadata and the included-but-uncoded (missing full text) section.

Usage: .venv\\Scripts\\python.exe scripts/rebuild_lr4_step3.py
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'scripts'))
import step3_lr4_data, step3_lr4_extra, step3_lr4_fusion  # noqa: E402
from screening_data_lr4 import S4, decision  # noqa: E402

SS = os.path.join(ROOT, '04d_LR4', '5. SLR matrix', 'ss')
OUT3 = os.path.join(ROOT, '04d_LR4', 'SLR summary matrix step 3.md')
COV = os.path.join(SS, 'coverage_lr4.json')

with open(os.path.join(SS, 'corpus_lr4.json'), encoding='utf-8') as f:
    CORPUS = json.load(f)
BYROW = {rec['row']: rec for rec in CORPUS}

S3L = step3_lr4_data.S3L
AH = step3_lr4_extra.AH
AI = step3_lr4_extra.AI
FD = step3_lr4_fusion.FD
FDEV = step3_lr4_fusion.FDEV
FDCF = step3_lr4_fusion.FDCF

INCLUDED = sorted(r for r, t in S4.items() if decision(t[:5]) == 'Include')


def authors_disp(aus):
    parts = [p.strip() for p in (aus or '').split(';') if p.strip()]
    if not parts:
        return 'Anon.'
    first = parts[0]
    if ',' in first:
        seg = first.split(',')[0].strip()
        ini = first.split(',', 1)[1].strip()
        nm = seg + (', ' + ini if ini else '')
    else:
        toks = [t for t in re.split(r'[\s,]+', first) if t]
        last = toks[-1] if toks else ''
        last_core = last.rstrip('.')
        if last != last_core or re.match(r'^[A-Za-z][A-Za-z]?\.?$', last_core):
            nm = (toks[-2] if len(toks) >= 2 else last_core) + ', ' + last_core
        else:
            nm = last.rstrip('.')
    return nm + (' et al.' if len(parts) > 1 else '')


def esc(s):
    return re.sub(r'\s+', ' ', s or '').replace('|', '/').strip()


def tier_short(t):
    if 'Tier 1' in t:
        return 'Tier 1 - Digital Model (static, no live data)'
    if 'Tier 2' in t:
        return 'Tier 2 - Digital Shadow (one-way physical to virtual)'
    if 'Tier 3' in t:
        return 'Tier 3 - Digital Twin (bidirectional, two-way)'
    if 'Tier 4' in t:
        return 'Tier 4 - Cognitive / Self-improving'
    return 'Unclear'


def stage2_reason(v):
    ag = v[14] if len(v) > 14 else ''
    if 'RETRACTED' in (ag or '').upper():
        return 'Retracted article'
    nos = []
    for tag, val in (('P', v[0]), ('Q', v[1]), ('R', v[2])):
        if val != 'Yes':
            nos.append('%s=No' % tag)
    return '; '.join(nos) if nos else ''


full = [r for r in S3L if S3L[r][0] == 'Yes' and S3L[r][1] == 'Yes' and S3L[r][2] == 'Yes']
excl = [r for r in S3L if r not in full]

L = [
    '# SLR Summary Matrix — Step 3 Deep-Read Coding',
    '',
    'Review: *A Self-Improving Cognitive Digital Twin for Design-for-Safety and Design-for-Quality in the Built Environment.*',
    'Coded from verified full text (Prompt B). **%d papers coded** — %d full-coded + %d Stage-2 excluded.' % (len(S3L), len(full), len(excl)),
    'Every row carries a `[Full-text source: ...]` mark in AG. AH = strength & gaps filled; AI = deficiencies & future work.',
    '',
    '| ID | Author | Title | Year | P | Q | R | S | T | U | V | W | X | Z | AA | AB | AC | AC1 | AC2 | AC3 | AD | AE | AF | AG | AH | AI | DOI |',
    '| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |',
]
for r in sorted(S3L):
    rec = BYROW[r]
    v = S3L[r]
    P, Q, R, tier = v[0], v[1], v[2], tier_short(v[3])
    if r in full:
        V, W, X, Z, AA, AB, AC, AD, AE, AF = v[4:14]
        s_dec, s_reason = 'Include', ''
        fd, fdev, fdcf = FD.get(r, ''), FDEV.get(r, ''), FDCF.get(r, '')
    else:
        V = W = X = Z = AA = AB = AC = AD = AE = AF = ''
        s_dec, s_reason = 'Exclude', stage2_reason(v)
        fd = fdev = fdcf = ''
    AG = v[14] if len(v) > 14 else ''
    SRC = v[15] if len(v) > 15 else ''
    ag = esc(AG) + ((' [Full-text source: %s]' % SRC) if SRC else '')
    L.append('| R%03d | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |' % (
        r, esc(authors_disp(rec['authors'])), esc(rec['title']), rec['year'],
        P, Q, R, s_dec, s_reason, tier, V, W, X, Z, AA, AB, AC,
        fd, fdev, fdcf, AD, AE, AF, ag, esc(AH.get(r, '')), esc(AI.get(r, '')),
        rec['doi'] or ''))

# included-but-uncoded section
uncoded = [r for r in INCLUDED if r not in S3L]
cov = {}
if os.path.exists(COV):
    try:
        cov = json.load(open(COV, encoding='utf-8'))
    except Exception:
        cov = {}

def miss_reason(r):
    v = cov.get(str(r), {})
    if not v:
        return 'not staged'
    if v.get('status') == 'no-candidate':
        return 'no matching PDF in Endnote library'
    if v.get('status') == 'unverified':
        return 'Endnote candidate(s) found but identity not verified'
    return 'full text unavailable'

L.append('')
L.append('## Included papers missing full text (not yet coded)')
L.append('')
L.append('| ID | Author | Title | Year | Reason | DOI |')
L.append('| --- | --- | --- | --- | --- | --- |')
for r in uncoded:
    rec = BYROW[r]
    L.append('| R%03d | %s | %s | %s | %s | %s |' % (
        r, esc(authors_disp(rec['authors'])), esc(rec['title']),
        rec['year'], miss_reason(r), rec['doi'] or ''))

with open(OUT3, 'w', encoding='utf-8') as f:
    f.write('\n'.join(L) + '\n')
print('Rebuilt LR4 Step-3: %d coded rows + %d missing -> %s' % (len(S3L), len(uncoded), OUT3))
